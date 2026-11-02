"""Fictional contract and decision-precedence tests for the pure T03 engine."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import unittest

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'skills/academic-deadline-drift-guard/scripts'))
from comparator import compare_snapshots
from validator import ValidationError

CASES = json.loads((ROOT / 'examples/contract-cases.json').read_text())['cases']


class ComparatorTests(unittest.TestCase):
    def test_all_contract_cases(self) -> None:
        for case in CASES:
            with self.subTest(case=case['case_id']):
                expected = case['expected']
                if expected['validation'] == 'REJECT':
                    with self.assertRaises(ValidationError) as caught:
                        compare_snapshots(case['before'], case['after'])
                    self.assertEqual(expected['error_code'], caught.exception.code)
                    continue
                result = compare_snapshots(case['before'], case['after'])
                actual = [{key: change[key] for key in ('module_id', 'item_id', 'status', 'reason_code')} for change in result['changes']]
                self.assertEqual(expected['changes'], actual)
                self.assertEqual([], result['confirmed_changes'])
                self.assertEqual('REVIEW_REQUIRED', result['result_status'])
                for change in result['changes']:
                    self.assertIs(True, change['requires_user_review'])
                    self.assertIs(False, change['user_confirmed'])

    def test_reviewed_golden_result(self) -> None:
        before = json.loads((ROOT / 'examples/fictional-before.json').read_text())
        after = json.loads((ROOT / 'examples/fictional-after.json').read_text())
        expected = json.loads((ROOT / 'examples/fictional-draft-result.json').read_text())
        self.assertEqual(expected, compare_snapshots(before, after))

    def test_inputs_and_output_are_independent(self) -> None:
        before, after = copy.deepcopy(CASES[0]['before']), copy.deepcopy(CASES[0]['after'])
        original = copy.deepcopy((before, after))
        result = compare_snapshots(before, after)
        self.assertEqual(original, (before, after))
        result['changes'][0]['before'][0]['title'] = 'Output mutation'
        result['changes'][0]['candidates'][0]['title'] = 'Output mutation'
        self.assertEqual(original, (before, after))

    def test_order_and_agreeing_sources_preserved(self) -> None:
        before, after = copy.deepcopy(CASES[0]['before']), copy.deepcopy(CASES[0]['after'])
        for side in (before, after):
            source, record = copy.deepcopy(side['sources'][0]), copy.deepcopy(side['records'][0])
            source['source_id'] = record['source_id'] = 'aaa'
            side['sources'].append(source)
            side['records'].insert(0, record)
        expected = compare_snapshots(before, after)
        for side in (before, after):
            side['sources'].reverse()
            side['records'].reverse()
        self.assertEqual(expected, compare_snapshots(before, after))
        change = expected['changes'][0]
        self.assertEqual('UNCHANGED', change['status'])
        self.assertEqual(2, len(change['before']))
        self.assertEqual(2, len(change['candidates']))
        self.assertEqual(4, len(change['source_references']))
        refs = [(r['side'], r['source_id'], r['source_excerpt']) for r in change['source_references']]
        self.assertEqual(sorted(set(refs)), refs)

    def test_conflict_survives_added_uncertainty_and_cancellation(self) -> None:
        for case_id in ('candidate-conflict', 'cancel-active-conflict', 'prior-conflict'):
            case = copy.deepcopy(next(c for c in CASES if c['case_id'] == case_id))
            side = case['before'] if case_id == 'prior-conflict' else case['after']
            source, record = copy.deepcopy(side['sources'][0]), copy.deepcopy(side['records'][0])
            source['source_id'] = record['source_id'] = 'unknown-extra'
            record.update(time_precision='unknown', due_date=None, due_time=None, timezone=None, explicit_cancellation=False)
            side['sources'].append(source)
            side['records'].append(record)
            self.assertEqual('CONFLICT', compare_snapshots(case['before'], case['after'])['changes'][0]['status'])

    def test_cancellation_and_unknown_is_conflict(self) -> None:
        case = copy.deepcopy(next(c for c in CASES if c['case_id'] == 'cancel-active-conflict'))
        active = next(r for r in case['after']['records'] if not r['explicit_cancellation'])
        active.update(time_precision='unknown', due_date=None, due_time=None, timezone=None)
        self.assertEqual('MULTIPLE_VALUES', compare_snapshots(case['before'], case['after'])['changes'][0]['reason_code'])

    def test_candidate_conflict_precedes_prior_uncertainty(self) -> None:
        case = copy.deepcopy(next(c for c in CASES if c['case_id'] == 'candidate-conflict'))
        case['before']['records'][0].update(time_precision='unknown', due_date=None, due_time=None, timezone=None)
        self.assertEqual('MULTIPLE_VALUES', compare_snapshots(case['before'], case['after'])['changes'][0]['reason_code'])

    def test_mixed_precision_is_uncertain_not_conflicting(self) -> None:
        for which, reason in (('before', 'PRIOR_UNCERTAINTY'), ('after', 'INCOMPARABLE_PRECISION')):
            case = copy.deepcopy(CASES[0])
            side = case[which]
            source, record = copy.deepcopy(side['sources'][0]), copy.deepcopy(side['records'][0])
            source['source_id'] = record['source_id'] = 'date-only'
            record.update(time_precision='date', due_time=None, timezone=None)
            side['sources'].append(source)
            side['records'].append(record)
            self.assertEqual(reason, compare_snapshots(case['before'], case['after'])['changes'][0]['reason_code'])

    def test_year_bounds_and_offset_arithmetic(self) -> None:
        for day, clock, offset in (('0001-01-01', '00:00', '+14:00'), ('9999-12-31', '23:59', '-14:00')):
            case = copy.deepcopy(CASES[0])
            for side in ('before', 'after'):
                case[side]['records'][0].update(due_date=day, due_time=clock, timezone=offset)
            self.assertEqual('UNCHANGED', compare_snapshots(case['before'], case['after'])['changes'][0]['status'])
        # Independently known day rollover: 2 Jan 00:30 +01 = 1 Jan 23:30 UTC.
        case = copy.deepcopy(CASES[0])
        case['before']['records'][0].update(due_date='2026-01-02', due_time='00:30', timezone='+01:00')
        case['after']['records'][0].update(due_date='2026-01-01', due_time='23:30', timezone='+00:00')
        self.assertEqual('UNCHANGED', compare_snapshots(case['before'], case['after'])['changes'][0]['status'])

    def test_maximum_identity_union_and_no_full_source_bodies(self) -> None:
        case = copy.deepcopy(CASES[0])
        for side, prefix in ((case['before'], 'prior'), (case['after'], 'candidate')):
            record = side['records'][0]
            side['records'] = [dict(record, item_id=f'{prefix}-{index:03}') for index in range(100)]
            side['sources'][0]['text'] += ' SOURCE_BODY_ONLY_NOT_AN_EXCERPT'
        result = compare_snapshots(case['before'], case['after'])
        self.assertEqual(200, len(result['changes']))
        self.assertNotIn('SOURCE_BODY_ONLY_NOT_AN_EXCERPT', json.dumps(result))
        identities = [(c['module_id'], c['item_id']) for c in result['changes']]
        self.assertEqual(sorted(set(identities)), identities)
        self.assertEqual(100, sum(c['status'] == 'ADDED' for c in result['changes']))
        self.assertEqual(100, sum(c['reason_code'] == 'MISSING_CANDIDATE' for c in result['changes']))

    def test_validation_before_any_partial_result(self) -> None:
        case = copy.deepcopy(CASES[0])
        case['before']['schema_version'] = '2.0'
        case['after'] = None
        with self.assertRaises(ValidationError) as caught:
            compare_snapshots(case['before'], case['after'])
        self.assertEqual('UNSUPPORTED_VERSION', caught.exception.code)
        self.assertEqual('$.before.schema_version', caught.exception.field_path)


if __name__ == '__main__':
    unittest.main()
