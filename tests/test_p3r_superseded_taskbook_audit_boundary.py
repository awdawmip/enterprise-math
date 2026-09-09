"""Exact old-generation containment; corrected P3R publications stay unchanged."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import tempfile
import unittest

from control_plane import research_task_record_audit_fault_isolation as isolation
from control_plane import research_task_records_impl as core
from tools import research_task_records as public

ROOT = Path(__file__).resolve().parents[1]
GENERATIONS = {
    'P3R-ALMOST-NORMAL-CERTIFICATE': ('TP2-436750BA0167CACD2DE0', 'TP2-67A0D169F01CFF865430'),
    'P3R-NONABELIAN-FINITE-OBSERVER': ('TP2-BEFF685705EC4E711719', 'TP2-5A4F26DCA4706C3B933A'),
    'P3R-NORMAL-SURFACE-COKERNEL-PRUNING': ('TP2-F7698D2C41EFB8B15CC0', 'TP2-9E91CE3693C89C8CFD4B'),
    'P3R-PACHNER-OBSTRUCTION-PROFILE': ('TP2-9569FC1AE1E8DC9C62E8', 'TP2-D7AF5D69E1B523D798DC'),
}


class P3RSupersededTaskbookBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        registry = json.loads(ROOT.joinpath(isolation.QUARANTINE_FILE).read_bytes())
        self.rows = [row for row in registry['quarantines'] if row['task_id'] in GENERATIONS]
        self.assertEqual(4, len(self.rows))
        self.frozen = {}
        for task, publications in GENERATIONS.items():
            for publication in publications:
                relative = f'research_task_records/{task}/{publication}.json'
                data = ROOT.joinpath(relative).read_bytes()
                self.capture(relative, data)
                book = json.loads(data)['taskbook_path']
                self.capture(book, ROOT.joinpath(book).read_bytes())
        self.registry = {**registry, 'quarantines': copy.deepcopy(self.rows)}
        self.save_registry()

    def capture(self, relative, data):
        path = self.root.joinpath(relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        self.frozen[relative] = data

    def save_registry(self):
        self.root.joinpath(isolation.QUARANTINE_FILE).write_bytes(
            (json.dumps(self.registry, indent=2) + '\n').encode('utf-8'))

    def raw_errors(self):
        # The public facade explicitly preserves this raw implementation handle.
        # Use it even if another test installed canonical compatibility wrappers.
        return public._STRICT_AUDIT(self.root)

    def test_exact_four_old_errors_only_and_current_generations_unchanged(self):
        raw = self.raw_errors()
        expected = {row['record_path'] + ': taskbook blob drift' for row in self.rows}
        self.assertEqual(expected, set(raw))
        self.assertEqual([], isolation.audit_against(raw, self.root))
        validated = isolation.validated_rows(self.root)
        self.assertEqual({pair[0] for pair in GENERATIONS.values()}, {r['publication_id'] for r in validated})
        current = core.current_records(self.root)
        self.assertEqual({t: pair[1] for t, pair in GENERATIONS.items()},
                         {t: rec['publication_id'] for t, rec in current.items()})
        for relative, data in self.frozen.items():
            self.assertEqual(data, self.root.joinpath(relative).read_bytes())

    def test_missing_registration_exposes_all_four_errors(self):
        raw = self.raw_errors()
        self.registry['quarantines'] = []
        self.save_registry()
        self.assertEqual(raw, isolation.audit_against(raw, self.root))
        self.assertEqual(4, len(raw))

    def test_current_generation_error_is_not_suppressed(self):
        task, (_, current) = next(iter(GENERATIONS.items()))
        path = self.root.joinpath('research_task_records', task, current + '.json')
        rec = json.loads(path.read_bytes())
        rec['taskbook_blob_sha1'] = 'sha1:' + '0' * 40
        path.write_bytes((json.dumps(rec) + '\n').encode())
        errors = isolation.audit_against(self.raw_errors(), self.root)
        self.assertEqual([path.relative_to(self.root).as_posix() + ': taskbook blob drift'], errors)

    def test_registered_record_and_current_book_byte_drift_are_rejected(self):
        row = self.rows[0]
        for field, message in [('record_path', 'record blob drift'), ('taskbook_path', 'taskbook blob drift')]:
            with self.subTest(field=field):
                path = self.root.joinpath(row[field])
                saved = path.read_bytes()
                path.write_bytes(saved + b'\n')
                with self.assertRaisesRegex(isolation.TaskRecordAuditIsolationError, message):
                    isolation.validated_rows(self.root)
                path.write_bytes(saved)

    def test_direct_same_task_supersession_is_required(self):
        task, (_, current) = next(iter(GENERATIONS.items()))
        path = self.root.joinpath('research_task_records', task, current + '.json')
        rec = json.loads(path.read_bytes())
        rec['supersedes_publication_id'] = None
        path.write_bytes((json.dumps(rec) + '\n').encode())
        with self.assertRaisesRegex(isolation.TaskRecordAuditIsolationError, 'not directly superseded'):
            isolation.validated_rows(self.root)

    def test_unlisted_error_and_unused_suppression_fail_closed(self):
        raw = self.raw_errors()
        extra = self.rows[0]['record_path'] + ': parent objective mismatch'
        self.assertEqual([extra], isolation.audit_against(raw + [extra], self.root))
        errors = isolation.audit_against(raw[1:], self.root)
        self.assertTrue(any('stale or unused suppression' in error for error in errors))

    def test_envelope_suffix_is_exact_and_cannot_cover_current_head(self):
        expected = {r['record_path'] + ': ' + r['allowed_publication_envelope_errors'][0] for r in self.rows}
        self.assertEqual(expected, isolation.envelope_suppression_strings(self.root))
        self.assertTrue(all(not any(pair[1] in value for value in expected) for pair in GENERATIONS.values()))
        self.registry['quarantines'][0]['allowed_publication_envelope_errors'] = ['taskbook blob drift']
        self.save_registry()
        with self.assertRaisesRegex(isolation.TaskRecordAuditIsolationError, 'exact record-side taskbook pin defect'):
            isolation.validated_rows(self.root)


if __name__ == '__main__':
    unittest.main()
