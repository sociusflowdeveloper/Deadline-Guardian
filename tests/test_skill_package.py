"""Self-contained package resources and real copied-folder CLI smoke checks."""
from __future__ import annotations

import json
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/academic-deadline-drift-guard'


class SkillPackageTests(unittest.TestCase):
    def test_frontmatter_and_local_references(self):
        text = (SKILL / 'SKILL.md').read_text()
        match = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
        self.assertIsNotNone(match)
        metadata = dict(line.split(': ', 1) for line in match.group(1).splitlines())
        self.assertEqual({'name', 'description'}, set(metadata))
        self.assertEqual(SKILL.name, metadata['name'])
        self.assertRegex(metadata['name'], r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
        self.assertLessEqual(len(metadata['name']), 64)
        self.assertTrue(metadata['description'])
        self.assertLessEqual(len(metadata['description']), 1024)
        self.assertLess(len(text.splitlines()), 500)
        for target in re.findall(r'\]\(([^)]+)\)', text):
            self.assertNotIn('://', target)
            self.assertTrue((SKILL / target).is_file(), target)

    def test_bundled_resources_match_normative_sources(self):
        for name in ('snapshot-v1.schema.json', 'result-v1.schema.json'):
            self.assertEqual((ROOT / 'schemas' / name).read_bytes(), (SKILL / 'references' / name).read_bytes())
        for name in ('fictional-before.json', 'fictional-after.json'):
            self.assertEqual((ROOT / 'examples' / name).read_bytes(), (SKILL / 'references' / name).read_bytes())
        self.assertEqual((ROOT / 'LICENSE').read_bytes(), (SKILL / 'LICENSE').read_bytes())
        source = (ROOT / 'CONTRACT.md').read_text()
        normative = source[source.index('## 1. Scope and precedence'):source.index('## 8. Acceptance and evidence')]
        bundled = (SKILL / 'references/contract.md').read_text()
        self.assertEqual(normative.rstrip(), bundled[bundled.index('## 1. Scope and precedence'):].rstrip())

    def test_documented_commands_work_with_only_copied_skill_folder(self):
        commands = []
        for name in ('SKILL.md', 'references/usage.md'):
            for command in re.findall(r'```bash\n(.*?)\n```', (SKILL / name).read_text(), re.DOTALL):
                commands.append(shlex.split(command))
        self.assertEqual(2, len(commands))
        with tempfile.TemporaryDirectory() as directory:
            copied = Path(directory) / SKILL.name
            shutil.copytree(SKILL, copied, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
            initial = {str(p.relative_to(copied)): p.read_bytes() for p in copied.rglob('*') if p.is_file()}
            for index, command in enumerate(commands):
                self.assertEqual('python', command[0])
                command[0] = sys.executable
                result = subprocess.run(command, cwd=copied, capture_output=True, text=True, timeout=10)
                self.assertEqual(0, result.returncode, result.stderr)
                self.assertEqual('', result.stderr)
                if index == 0:
                    draft = json.loads(result.stdout)
                    self.assertEqual('REVIEW_REQUIRED', draft['result_status'])
                    self.assertEqual([], draft['confirmed_changes'])
                    self.assertEqual('CHANGED', draft['changes'][0]['status'])
                    self.assertEqual(initial, {str(p.relative_to(copied)): p.read_bytes() for p in copied.rglob('*') if p.is_file()})
                else:
                    self.assertEqual('EXPORTED_DRAFT: REVIEW_REQUIRED; no confirmed changes.\n', result.stdout)
                    self.assertIn('REVIEW_REQUIRED', (copied / 'fictional-draft.md').read_text())
            current = {str(p.relative_to(copied)): p.read_bytes() for p in copied.rglob('*') if p.is_file()}
            self.assertEqual({'fictional-draft.md'}, current.keys() - initial.keys())
            for path, payload in initial.items():
                self.assertEqual(payload, current[path], path)
