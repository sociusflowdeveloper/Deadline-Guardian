"""Fictional draft rendering and confined exclusive-write regression checks."""
from __future__ import annotations

import copy
import csv
import io
import json
import os
from pathlib import Path
import stat
import sys
import tempfile
import unittest
from unittest import mock

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'skills/academic-deadline-drift-guard/scripts'))
import exporter
import reconcile
from comparator import compare_snapshots
from exporter import export_report, render_report
from validator import ValidationError, open_workspace

BEFORE = json.loads((ROOT / 'examples/fictional-before.json').read_text())
AFTER = json.loads((ROOT / 'examples/fictional-after.json').read_text())


class RenderTests(unittest.TestCase):
    def setUp(self):
        self.result = compare_snapshots(copy.deepcopy(BEFORE), copy.deepcopy(AFTER))

    def test_json_is_exact_canonical_draft_and_does_not_mutate(self):
        original = copy.deepcopy(self.result)
        self.assertEqual(original, json.loads(render_report(self.result, 'json')))
        self.assertEqual(original, self.result)

    def test_csv_keeps_both_sides_evidence_and_review_fields(self):
        rows = list(csv.DictReader(io.StringIO(render_report(self.result, 'csv').decode())))
        self.assertEqual(['before', 'after'], [r['side'] for r in rows])
        self.assertEqual(BEFORE['records'][0]['source_excerpt'], rows[0]['source_excerpt'])
        for row in rows:
            self.assertEqual('REVIEW_REQUIRED', row['result_status'])
            self.assertEqual('True', row['requires_user_review'])
            self.assertEqual('False', row['user_confirmed'])

    def test_csv_formula_controls_delimiters_quotes_and_newlines(self):
        for text in ('=1+1', '+SUM(A1)', '-1+1', '@SUM(A1)', '  =1', '\t=1', '\r=1', '\n=1'):
            with self.subTest(text=text):
                self.result['changes'][0]['before'][0]['title'] = text
                row = next(csv.DictReader(io.StringIO(render_report(self.result, 'csv').decode())))
                self.assertEqual("'" + text, row['title'])
        text = 'Text,"quoted"\nnext line'
        self.result['changes'][0]['before'][0]['source_excerpt'] = text
        row = next(csv.DictReader(io.StringIO(render_report(self.result, 'csv').decode())))
        self.assertEqual(text, row['source_excerpt'])

    def test_markdown_html_links_images_and_structure_are_literal(self):
        text = '<script>x</script> ![x](https://invalid.test)\n# head | `code` *bold*'
        self.result['changes'][0]['candidates'][0]['source_excerpt'] = text
        output = render_report(self.result, 'markdown').decode()
        self.assertNotIn('<script>', output)
        self.assertNotIn('![x](', output)
        self.assertNotIn('https://invalid.test', output)
        self.assertIn('https&#58;//invalid&#46;test', output)
        self.assertIn('&lt;script&gt;', output)
        self.assertIn('\\!\\[x\\]\\(', output)
        self.assertIn('&#10;\\#', output)
        self.assertIn('User confirmed: false', output)
        self.assertEqual(text, self.result['changes'][0]['candidates'][0]['source_excerpt'])

    def test_empty_draft_and_confirmed_content_rejection(self):
        empty = dict(self.result, changes=[])
        for format in ('json', 'csv', 'markdown'):
            self.assertTrue(render_report(empty, format))
        empty_rows = list(csv.DictReader(io.StringIO(render_report(empty, 'csv').decode())))
        self.assertEqual('REVIEW_REQUIRED', empty_rows[0]['result_status'])
        self.assertEqual('True', empty_rows[0]['requires_user_review'])
        self.assertEqual('False', empty_rows[0]['user_confirmed'])
        for field, value in (('confirmed_changes', [{}]), ('result_status', 'CONFIRMED')):
            with self.assertRaises(ValidationError):
                render_report(dict(self.result, **{field: value}), 'json')
        self.result['changes'][0]['user_confirmed'] = True
        with self.assertRaises(ValidationError):
            render_report(self.result, 'markdown')


class WriteTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.result = compare_snapshots(copy.deepcopy(BEFORE), copy.deepcopy(AFTER))

    def write(self, name, format='json'):
        with open_workspace(str(self.root)) as workspace:
            export_report(workspace, name, format, self.result)

    def test_all_formats_private_exclusive_and_no_leftover_temp(self):
        (self.root / 'reports').mkdir()
        for format, extension in exporter.SUFFIXES.items():
            name = 'reports/draft' + extension
            self.write(name, format)
            path = self.root / name
            self.assertEqual(render_report(self.result, format), path.read_bytes())
            self.assertEqual(0o600, stat.S_IMODE(path.stat().st_mode))
            with self.assertRaises(ValidationError):
                self.write(name, format)
        self.assertFalse(list(self.root.rglob('*.tmp')))

    def test_bad_path_missing_parent_existing_input_and_symlinks(self):
        (self.root / 'input.json').write_text('DO NOT CHANGE')
        (self.root / 'dir.json').mkdir()
        (self.root / 'link.json').symlink_to('input.json')
        (self.root / 'dangling.json').symlink_to('absent')
        (self.root / 'linked').symlink_to(self.root, target_is_directory=True)
        for name in ('/tmp/escape.json', '../escape.json', './draft.json', 'a/../draft.json', 'a//draft.json', 'missing/draft.json', 'draft.JSON', 'draft.csv', 'bad\\draft.json', 'input.json', 'dir.json', 'link.json', 'dangling.json', 'linked/draft.json'):
            with self.subTest(name=name), self.assertRaises(ValidationError) as caught:
                self.write(name)
            self.assertEqual('UNSAFE_PATH', caught.exception.code)
        self.assertEqual('DO NOT CHANGE', (self.root / 'input.json').read_text())
        self.assertFalse((self.root / 'draft.json').exists())

    def test_failed_write_cleans_own_temp_and_no_destination(self):
        with mock.patch.object(exporter.os, 'write', side_effect=OSError('PRIVATE detail')):
            with self.assertRaises(ValidationError) as caught:
                self.write('draft.json')
        self.assertEqual('UNSAFE_PATH $.output', str(caught.exception))
        self.assertEqual([], list(self.root.iterdir()))

    def test_short_writes_are_completed(self):
        real_write = os.write
        with mock.patch.object(exporter.os, 'write', side_effect=lambda fd, data: real_write(fd, data[:7])):
            self.write('draft.json')
        self.assertEqual(self.result, json.loads((self.root / 'draft.json').read_text()))

    def test_destination_created_during_publish_is_not_overwritten(self):
        real_link = os.link
        def race(source, destination, **kwargs):
            (self.root / destination).write_text('OTHER WRITER')
            return real_link(source, destination, **kwargs)
        # Preserve capability test membership when replacing the function.
        with mock.patch.object(exporter.os, 'link', side_effect=race) as linked:
            with mock.patch.object(exporter.os, 'supports_dir_fd', os.supports_dir_fd | {linked}), mock.patch.object(exporter.os, 'supports_follow_symlinks', os.supports_follow_symlinks | {linked}):
                with self.assertRaises(ValidationError):
                    self.write('draft.json')
        self.assertEqual('OTHER WRITER', (self.root / 'draft.json').read_text())
        self.assertEqual(['draft.json'], [p.name for p in self.root.iterdir()])

    def test_parent_rename_during_write_fails_and_cleans_in_moved_directory(self):
        (self.root / 'reports').mkdir()
        real_write = os.write
        def race(fd, data):
            (self.root / 'reports').rename(self.root / 'moved')
            (self.root / 'reports').mkdir()
            return real_write(fd, data)
        with mock.patch.object(exporter.os, 'write', side_effect=race):
            with self.assertRaises(ValidationError):
                self.write('reports/draft.json')
        self.assertEqual([], list((self.root / 'moved').iterdir()))
        self.assertEqual([], list((self.root / 'reports').iterdir()))

    def test_postpublish_failure_cleans_owned_output(self):
        real_verify = exporter._verify_links
        def verify(links, path):
            if any(name == 'draft.json' for _, name, _ in links):
                raise ValidationError('UNSAFE_PATH', path)
            real_verify(links, path)
        with mock.patch.object(exporter, '_verify_links', side_effect=verify):
            with self.assertRaises(ValidationError):
                self.write('draft.json')
        self.assertEqual([], list(self.root.iterdir()))

    def test_unsupported_publish_capability_fails_before_staging(self):
        with open_workspace(str(self.root)) as workspace:
            with mock.patch.object(exporter.os, 'supports_dir_fd', os.supports_dir_fd - {os.link}):
                with self.assertRaises(ValidationError):
                    export_report(workspace, 'draft.json', 'json', self.result)
        self.assertEqual([], list(self.root.iterdir()))

    def test_existing_hardlink_and_cleanup_replacement_are_preserved(self):
        (self.root / 'input.json').write_text('INPUT')
        os.link(self.root / 'input.json', self.root / 'draft.json')
        with self.assertRaises(ValidationError):
            self.write('draft.json')
        self.assertEqual('INPUT', (self.root / 'input.json').read_text())
        (self.root / 'draft.json').unlink()
        real_verify = exporter._verify_links
        def verify(links, path):
            if any(name == 'draft.json' for _, name, _ in links):
                (self.root / 'draft.json').unlink()
                (self.root / 'draft.json').write_text('OTHER WRITER')
                raise ValidationError('UNSAFE_PATH', path)
            real_verify(links, path)
        with mock.patch.object(exporter, '_verify_links', side_effect=verify):
            with self.assertRaises(ValidationError):
                self.write('draft.json')
        self.assertEqual('OTHER WRITER', (self.root / 'draft.json').read_text())
        self.assertFalse(list(self.root.glob('*.tmp')))

    def test_encoding_failure_happens_before_any_write(self):
        self.result['changes'][0]['before'][0]['title'] = '\ud800'
        with self.assertRaises(ValidationError):
            self.write('draft.md', 'markdown')
        self.assertEqual([], list(self.root.iterdir()))
        self.write('draft.json')
        self.assertEqual(self.result, json.loads((self.root / 'draft.json').read_text()))


class ExportCliTests(unittest.TestCase):
    def test_cli_exports_and_errors_without_input_disclosure(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, value in (('before.json', BEFORE), ('after.json', AFTER)):
                (root / name).write_text(json.dumps(value))
            args = ['--workspace', directory, '--before', 'before.json', '--after', 'after.json']
            for format, suffix in exporter.SUFFIXES.items():
                output = io.StringIO()
                with mock.patch('sys.stdout', output):
                    code = reconcile.main(args + ['--output', 'draft' + suffix, '--format', format])
                self.assertEqual(0, code)
                self.assertEqual('EXPORTED_DRAFT: REVIEW_REQUIRED; no confirmed changes.\n', output.getvalue())
            for extra, code in ((['--output', 'new.json'], 2), (['--format', 'json'], 2), (['--output', 'before.json', '--format', 'json'], 3), (['--output', '../PRIVATE.json', '--format', 'json'], 3)):
                error = io.StringIO()
                with mock.patch('sys.stderr', error):
                    self.assertEqual(code, reconcile.main(args + extra))
                self.assertNotIn('PRIVATE', error.getvalue())
                self.assertNotIn(BEFORE['records'][0]['title'], error.getvalue())
            self.assertEqual(BEFORE, json.loads((root / 'before.json').read_text()))
