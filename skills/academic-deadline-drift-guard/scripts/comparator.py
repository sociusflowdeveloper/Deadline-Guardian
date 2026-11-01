"""Pure, provisional v1 snapshot comparison; no I/O or source ranking.

Source text is inert evidence. Matching uses module/item IDs only. The contract
in CONTRACT.md defines precedence, including conflicts and unknown precision.
"""
from __future__ import annotations

from datetime import date

from validator import validate_snapshot


def _active_value(record: dict) -> tuple[str, int]:
    """Return calendar day or unbounded integer UTC minute for definite input."""
    day = date.fromisoformat(record['due_date']).toordinal()
    if record['time_precision'] == 'date':
        return 'date', day
    hour, minute = map(int, record['due_time'].split(':'))
    offset = record['timezone']
    offset_hour, offset_minute = map(int, offset[1:].split(':'))
    signed_offset = (offset_hour * 60 + offset_minute) * (1 if offset[0] == '+' else -1)
    return 'minute', day * 1440 + hour * 60 + minute - signed_offset


def _state(records: list[dict]) -> tuple[bool, bool, bool, bool, set[tuple[str, int]]]:
    """Summarise conflict, ambiguity, mixed precision, cancellation and values."""
    cancellation = any(record['explicit_cancellation'] for record in records)
    active = [record for record in records if not record['explicit_cancellation']]
    ambiguous = any(record['time_precision'] == 'unknown' or
                    (record['time_precision'] == 'minute' and record['timezone'] is None)
                    for record in active)
    values = {_active_value(record) for record in active
              if record['time_precision'] == 'date' or
              (record['time_precision'] == 'minute' and record['timezone'] is not None)}
    precisions = {value[0] for value in values}
    conflict = ((cancellation and bool(active)) or
                any(sum(value[0] == precision for value in values) > 1 for precision in precisions))
    return conflict, ambiguous, len(precisions) > 1, cancellation, values


def _decision(before: list[dict], after: list[dict]) -> tuple[str, str]:
    """Apply the fourteen contract rows in order without selecting authority."""
    prior_conflict, prior_ambiguous, prior_mixed, prior_cancelled, prior_values = _state(before)
    conflict, ambiguous, mixed, cancelled, values = _state(after)
    if prior_conflict:
        return 'CONFLICT', 'PRIOR_CONFLICT'
    if conflict:
        return 'CONFLICT', 'MULTIPLE_VALUES'
    if prior_ambiguous or prior_mixed:
        return 'UNVERIFIED', 'PRIOR_UNCERTAINTY'
    if not after:
        return 'UNVERIFIED', 'MISSING_CANDIDATE'
    if ambiguous:
        return 'UNVERIFIED', 'AMBIGUOUS_CANDIDATE'
    if mixed:
        return 'UNVERIFIED', 'INCOMPARABLE_PRECISION'
    if cancelled:
        if not before:
            return 'UNVERIFIED', 'CANCELLATION_WITHOUT_BASELINE'
        if prior_cancelled:
            return 'UNCHANGED', 'ALREADY_CANCELLED'
        return 'REMOVED', 'EXPLICIT_CANCELLATION'
    if prior_cancelled:
        return 'UNVERIFIED', 'REAPPEARED_AFTER_CANCELLATION'
    if not before:
        return 'ADDED', 'NEW_ITEM'
    prior_value, value = next(iter(prior_values)), next(iter(values))
    if prior_value[0] != value[0]:
        return 'UNVERIFIED', 'INCOMPARABLE_PRECISION'
    if prior_value == value:
        return 'UNCHANGED', 'SAME_VALUE'
    return 'CHANGED', 'VALUE_CHANGED'


def _group(records: list[dict]) -> dict[tuple[str, str], list[dict]]:
    groups: dict[tuple[str, str], list[dict]] = {}
    for record in records:
        identity = record['module_id'], record['item_id']
        # Every record field is a validated scalar; copying isolates result data.
        groups.setdefault(identity, []).append(dict(record))
    for group in groups.values():
        group.sort(key=lambda record: record['source_id'])
    return groups


def compare_snapshots(before: object, after: object) -> dict:
    """Validate before then after, returning a deterministic v1 draft result.

    Raises validator.ValidationError on either invalid native snapshot, before
    constructing a report. Use decode_snapshot/read_snapshot for byte-level and
    file guarantees. Does not mutate or retain inputs. All output records and
    exact evidence are copied; no full source body, confirmed change, network,
    file write or authority decision is produced.
    """
    before = validate_snapshot(before, '$.before')
    after = validate_snapshot(after, '$.after')
    prior_groups, candidate_groups = _group(before['records']), _group(after['records'])
    changes = []
    for module_id, item_id in sorted(prior_groups.keys() | candidate_groups.keys()):
        prior = prior_groups.get((module_id, item_id), [])
        candidates = candidate_groups.get((module_id, item_id), [])
        status, reason = _decision(prior, candidates)
        references = {(side, record['source_id'], record['source_excerpt'])
                      for side, records in (('before', prior), ('after', candidates))
                      for record in records}
        changes.append({
            'module_id': module_id, 'item_id': item_id,
            'status': status, 'reason_code': reason,
            'before': prior, 'candidates': candidates,
            'source_references': [dict(side=side, source_id=source, source_excerpt=excerpt)
                                  for side, source, excerpt in sorted(references)],
            'requires_user_review': True, 'user_confirmed': False,
        })
    return {
        'schema_version': '1.0', 'result_status': 'REVIEW_REQUIRED',
        'before_snapshot_id': before['snapshot_id'], 'after_snapshot_id': after['snapshot_id'],
        'changes': changes, 'confirmed_changes': [],
    }
