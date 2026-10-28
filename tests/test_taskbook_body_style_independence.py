"""Retire presentation-only holds without touching scientific/identity records."""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

from control_plane import research_task_records_impl as core
from control_plane import research_task_integrity_fault_isolation as current
from control_plane import research_task_record_audit_fault_isolation as historical
from tools import research_task_records as records
from tests.test_research_task_record_compatibility import _write_fixture

ROOT = Path(__file__).resolve().parents[1]


class TaskbookBodyStyleIndependenceTests(unittest.TestCase):
    def test_arbitrary_headings_languages_and_prose_preserve_usable_content(self):
        for body in ('研究问题：给定明确输入，证明所述命题或给出反例。',
                     '# Question\n\nAssume x is an integer. Determine whether x=x.',
                     '## Frozen inputs\n\nExact source input.\n## Evidence\n\nA proof or counterexample.'):
            with self.subTest(body=body):
                self.assertEqual([], core.validate_body(body))

    def test_retired_heading_diagnostic_is_not_tied_to_a_label_version(self):
        self.assertTrue(core.is_retired_body_style_error(
            'mandatory body section is missing or empty: 任意旧版标题'))
        self.assertFalse(core.is_retired_body_style_error('taskbook body contains placeholder text'))
        self.assertFalse(core.is_retired_body_style_error('taskbook task_id mismatch'))

    def test_empty_heading_only_and_unfilled_scientific_content_still_rejected(self):
        for body in ('', '  \n', '# Title\n## Question\n', '# Title\n\n<insert exact input>'):
            with self.subTest(body=body):
                self.assertTrue(core.validate_body(body))

    def fixture(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        data = json.loads((ROOT / current.QUARANTINE_FILE).read_text())
        row = copy.deepcopy(next(r for r in data['quarantines'] if all(
            core.is_retired_body_style_error(e) for e in r['allowed_task_record_audit_errors'])))
        data['quarantines'] = [row]
        (root / current.QUARANTINE_FILE).write_text(json.dumps(data))
        for key in ('record_path', 'taskbook_path'):
            p = root / row[key]
            p.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / row[key], p)
        return root, row, data

    def test_style_hold_retires_without_changing_original_record_or_taskbook(self):
        root, row, _ = self.fixture()
        before = {key: (root / row[key]).read_bytes() for key in ('record_path', 'taskbook_path')}
        self.assertEqual({}, current.validated_quarantines(root))
        self.assertEqual(set(), current.suppression_strings(root))
        self.assertEqual(before, {key: (root / row[key]).read_bytes() for key in before})

    def test_retired_hold_does_not_hide_original_record_or_taskbook_byte_drift(self):
        for field in ('record_path', 'taskbook_path'):
            root, row, _ = self.fixture()
            with self.subTest(field=field):
                path = root / row[field]
                path.write_bytes(path.read_bytes() + b'\n')
                with self.assertRaisesRegex(current.TaskIntegrityIsolationError, 'blob drift'):
                    current.validated_quarantines(root)

    def test_actual_empty_or_unfilled_body_keeps_a_real_content_hold(self):
        for body in ('# Title only', '# Task\n\n<insert exact scientific inputs>'):
            root, row, data = self.fixture()
            book = root / row['taskbook_path']
            meta, _ = core.research_taskbook.split_taskbook(book.read_text())
            book.write_text(core.research_taskbook.render_taskbook(meta, body))
            record_path = root / row['record_path']
            record = json.loads(record_path.read_text())
            record['taskbook_blob_sha1'] = core.taskbook_blob(book)
            record_path.write_text(json.dumps(record))
            row['taskbook_blob_sha1'] = record['taskbook_blob_sha1']
            row['record_blob_sha1'] = core.git_blob_sha1_bytes(record_path.read_bytes())
            (root / current.QUARANTINE_FILE).write_text(json.dumps(data))
            before = (root / current.QUARANTINE_FILE).read_bytes()
            derived = current.validated_quarantines(root)[row['task_id']]
            self.assertEqual(core.validate_body(body), derived['allowed_task_record_audit_errors'])
            self.assertEqual('BLOCKED', current.blocked_definition(row['task_id'], derived)['base_state'])
            self.assertEqual(before, (root / current.QUARANTINE_FILE).read_bytes())

    def test_non_style_cause_remains_active(self):
        root, row, data = self.fixture()
        row['allowed_task_record_audit_errors'].append('unknown scientific-input defect')
        (root / current.QUARANTINE_FILE).write_text(json.dumps(data))
        self.assertIn(row['task_id'], current.validated_quarantines(root))
        self.assertEqual({row['record_path'] + ': unknown scientific-input defect'}, current.suppression_strings(root))

    def test_historical_mixed_errors_retain_non_style_checks(self):
        rows = [{'record_path': 'research_task_records/T/P.json',
                 'allowed_task_record_audit_errors': [
                     'mandatory body section is missing or empty: Mother question', 'taskbook blob drift']}]
        with patch.object(historical, 'validated_rows', return_value=rows):
            self.assertEqual({'research_task_records/T/P.json: taskbook blob drift'}, historical.suppression_strings())
            self.assertTrue(historical.audit_against([]))
            self.assertEqual([], historical.audit_against(['research_task_records/T/P.json: taskbook blob drift']))

    def test_old_taskbook_needs_no_heading_waiver_and_still_rejects_byte_drift(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            hist, _ = _write_fixture(root, include_waiver=False)
            self.assertEqual([], records.audit(root))
            hist.write_bytes(hist.read_bytes() + b'\nchanged input\n')
            self.assertTrue(any('taskbook blob drift' in e for e in records.audit(root)))

    def test_primary_twelve_and_addendum_style_holds_retire_other_holds_remain(self):
        rows = current.quarantine_rows(ROOT)
        style = {k for k, row in rows.items() if all(core.is_retired_body_style_error(e)
                 for e in row['allowed_task_record_audit_errors'])}
        remaining = current.validated_quarantines(ROOT)
        primary = json.loads((ROOT / current.QUARANTINE_FILE).read_text())['quarantines']
        self.assertEqual(12, sum(all(core.is_retired_body_style_error(e)
            for e in row['allowed_task_record_audit_errors']) for row in primary))
        self.assertEqual(24, len(style))
        self.assertEqual(set(rows) - style, set(remaining))
        self.assertEqual(3, len(remaining))


if __name__ == '__main__':
    unittest.main()
