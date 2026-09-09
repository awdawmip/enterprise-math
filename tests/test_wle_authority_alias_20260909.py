"""Exact new WLE source identity compatibility; no broad authority exemption."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest

import research_driver_authority as authority


ROOT = Path(__file__).resolve().parents[1]
RECORD = 'research_driver_authority_records/EM-DVR-WLE3X6/DA-1E692BDC110BA462AE26.json'
RAW_ID = 'DA-1E692BDC110BA462AE26'
NORMALIZED_ID = 'DA-79A23EF7BA38BE9398C5'
BLOB = 'sha1:bcfeb9d75913a149511ab23477f309e3762787ce'


class ExactWleAuthorityAliasTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.payload = json.loads(ROOT.joinpath(authority.COMPATIBILITY).read_text(encoding='utf-8'))
        matches = [row for row in self.payload['id_aliases'] if row['record_path'] == RECORD]
        self.assertEqual(1, len(matches))
        self.alias = matches[0]
        self.payload['id_aliases'] = [self.alias]
        for relative in (authority.CONTRACT, authority.CONTROL_POLICY, RECORD):
            target = self.root.joinpath(relative)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT.joinpath(relative), target)
        self.save_aliases()

    def save_aliases(self):
        self.root.joinpath(authority.COMPATIBILITY).write_text(
            json.dumps(self.payload, indent=2) + '\n', encoding='utf-8', newline='\n')

    def test_raw_history_and_real_source_validation_are_preserved(self):
        path = self.root.joinpath(RECORD)
        original = path.read_bytes()
        raw = json.loads(original)
        self.assertEqual(BLOB, authority._git_blob_sha1(path))
        self.assertEqual([RAW_ID + ': authority_record_id mismatch'], authority.validate_record(raw, self.root))
        self.assertEqual(NORMALIZED_ID, authority._record_id('EM-DVR-WLE3X6', 'AUTHORIZE', 5595884418))
        rows = authority.valid_records(self.root)
        self.assertEqual(1, len(rows))
        self.assertEqual(NORMALIZED_ID, rows[0]['authority_record_id'])
        self.assertEqual(RAW_ID, rows[0]['_raw_authority_record_id'])
        self.assertEqual(raw['source_body'], rows[0]['source_body'])
        self.assertEqual(original, path.read_bytes())
        for flag in ('working_truth_granted', 'foundation_authority_granted', 'canonical_promotion_granted'):
            self.assertIs(False, rows[0][flag])

    def test_authority_still_depends_on_the_real_event_time_and_driver(self):
        self.assertIsNone(authority.active_authority_at('EM-DVR-WLE3X6', '2026-09-09T04:39:11Z', self.root))
        active = authority.require_active_driver('EM-DVR-WLE3X6', '2026-09-09T04:39:12Z', self.root)
        self.assertEqual(5595884418, active['source_comment_id'])
        self.assertIsNone(authority.active_authority_at('EM-DVR-OTHER', '2026-09-09T04:39:12Z', self.root))

    def test_exact_raw_blob_drift_is_rejected(self):
        path = self.root.joinpath(RECORD)
        path.write_bytes(path.read_bytes() + b'\n')
        with self.assertRaisesRegex(authority.DriverAuthorityError, 'immutable authority record blob drift'):
            authority.valid_records(self.root)

    def test_wrong_normalized_id_is_rejected(self):
        self.alias['normalized_authority_record_id'] = 'DA-FORGED'
        self.save_aliases()
        with self.assertRaisesRegex(authority.DriverAuthorityError, 'does not equal current formula'):
            authority.valid_records(self.root)

    def test_missing_and_duplicate_aliases_remain_errors(self):
        self.payload['id_aliases'].append(copy.deepcopy(self.alias))
        self.save_aliases()
        with self.assertRaisesRegex(authority.DriverAuthorityError, 'duplicate alias identity'):
            authority.valid_records(self.root)
        self.payload['id_aliases'] = [self.alias]
        self.save_aliases()
        self.root.joinpath(RECORD).unlink()
        with self.assertRaisesRegex(authority.DriverAuthorityError, 'stale alias path'):
            authority.valid_records(self.root)

    def test_exact_alias_does_not_exempt_invalid_source_scope(self):
        path = self.root.joinpath(RECORD)
        raw = json.loads(path.read_bytes())
        raw['scope'] = 'FOUNDATION'
        path.write_text(json.dumps(raw, indent=2) + '\n', encoding='utf-8', newline='\n')
        self.alias['record_blob_sha1'] = authority._git_blob_sha1(path)
        self.save_aliases()
        with self.assertRaisesRegex(authority.DriverAuthorityError, 'invalid Driver authority scope'):
            authority.valid_records(self.root)


if __name__ == '__main__':
    unittest.main()
