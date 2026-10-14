"""Exact X6 custody bytes; synthetic control contexts never grant real authority."""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest import mock

from control_plane import research_historical_result_intake as h
from control_plane import research_historical_source_custody as c
from control_plane import research_result_records_impl as impl
from tools import research_task_records

REPO = Path(__file__).resolve().parents[1]


class ExactSourceCustodyTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.contract = json.loads((REPO / h.CONTRACT).read_text())
        self.target = next(t for t in self.contract['targets'] if t['historical_result_id'] == c.RESULT)
        self.mapping = json.loads((REPO / c.MAP_PIN['path']).read_text())
        paths = {row['physical_path'] for row in self.mapping['entries']}
        paths.update(self.target[key]['path'] for key in ('result_pin', 'execution_pin', 'publication_pin', 'taskbook_pin'))
        paths.update((h.CONTRACT, c.MAP_PIN['path']))
        for rel in paths:
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPO / rel, path)
        self.old = json.loads((self.root / self.target['result_pin']['path']).read_text())
        self.context = {'source_commit': 'a'*40, 'authorized_at': '2026-10-14T16:00:00+00:00',
                        'authority_observed_through_comment_id': 9900000901,
                        'principal': {'driver_id': 'EM-DVR-CUSTODY-FIXTURE', 'session_id': 'fixture-session',
                                      'authority_record_id': 'DA-FIXTURE', 'run_request_id': 'fixture-custody-run'}}
        self.spec = {'run_request_id': 'fixture-custody-run', 'target_task_id': c.TASK, 'publication_id': c.PUBLICATION,
                     'historical_result_id': c.RESULT, 'reason': 'isolated test only'}
        for field, pin, key in [('expected_result_sha256','result_pin','sha256'), ('expected_result_blob_sha1','result_pin','git_blob_sha1'),
                                ('expected_execution_sha256','execution_pin','sha256'), ('expected_execution_blob_sha1','execution_pin','git_blob_sha1'),
                                ('expected_publication_blob_sha1','publication_pin','git_blob_sha1'), ('expected_taskbook_blob_sha1','taskbook_pin','git_blob_sha1')]:
            self.spec[field] = self.target[pin][key]

    def write(self, rel, value):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value) + '\n')

    def inventory(self):
        return {p.relative_to(self.root).as_posix(): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}

    def current(self):
        return mock.patch.object(research_task_records, 'current_records', return_value={c.TASK: {'publication_id': c.PUBLICATION}})

    def make_intake(self):
        # These synthetic contexts test receipt/replay dataflow only. Current
        # GOV authority is intentionally not asserted by this fixture.
        with self.current(), mock.patch.object(h, '_authority') as authority:
            result = h.freeze_intake(self.spec, self.context, root=self.root)
        self.assertTrue(any(call.kwargs.get('fresh') is True and call.kwargs.get('governance') == self.target['authorizing_governance_task_id']
                            for call in authority.call_args_list))
        return result

    def make_review(self, intake):
        path = 'driver_reviews/CUSTODY_FIXTURE.md'
        (self.root / path).parent.mkdir(parents=True, exist_ok=True)
        (self.root / path).write_text('Synthetic review fixture; no mathematical acceptance.\n')
        ip = h.pin(self.root, intake['record_path'])
        rp = h.pin(self.root, path)
        context = {**self.context, 'principal': {'driver_id': 'EM-DVR-NONAUTHOR-FIXTURE', 'session_id': 'review-fixture', 'authority_record_id': 'DA-REVIEW-FIXTURE'}}
        spec = {'target_task_id': c.TASK, 'publication_id': c.PUBLICATION, 'intake_id': intake['record']['intake_id'],
                'expected_intake_sha256': ip['sha256'], 'expected_intake_blob_sha1': ip['git_blob_sha1'],
                'review_path': path, 'expected_review_sha256': rp['sha256'], 'expected_review_blob_sha1': rp['git_blob_sha1'],
                'disposition': 'ACCEPTED', 'reviewer_contribution_ids': ['EM-DVR-NONAUTHOR-FIXTURE'], 'reason': 'synthetic fixture only',
                'portfolio_continuation': {'parent_objective_status': 'OPEN', 'next_action': 'retain remaining parent scope', 'next_task_id': None},
                'supersedes_review_ids': [], 'expected_previous_review_set_sha256': h.review_set_digest([])}
        with self.current(), mock.patch.object(h, '_authority'):
            result = h.freeze_review(spec, context, root=self.root)
        return result

    def test_actual_six_raw_bytes_and_single_observation_pass_without_alias_or_rewrite(self):
        before = self.inventory()
        old, outputs = h._science(self.root, self.target)
        self.assertEqual(old, self.old)
        self.assertEqual(len(outputs), 4)
        self.assertIn(' / 28_CLAIMS_CLASSIFIED / ', old['hard_target_disposition'])
        self.assertEqual(old['output_manifest'][-1]['sha256'], c.OBSERVATION['raw_declared_sha256'])
        self.assertEqual([row['secondary_digest_observation'] for row in outputs if row['secondary_digest_observation']], [c.OBSERVATION])
        for output in outputs:
            self.assertEqual(output['schema'], 'ENTERPRISE_MATH_HISTORICAL_CUSTODY_OUTPUT_V1')
            self.assertEqual(output['logical_path'], output['original_manifest_entry']['path'])
            self.assertTrue((self.root / output['path']).is_file())
            self.assertFalse((self.root / output['logical_path']).exists())
        self.assertNotIn(c.EXECUTION, impl.execution_map(self.root))
        self.assertEqual(before, self.inventory())

    def test_map_pin_is_frozen_in_receipt_and_raw_science_is_not_normalized(self):
        intake = self.make_intake()
        record = intake['record']
        self.assertEqual(record['target_pins']['custody_map_pin'], c.MAP_PIN)
        self.assertEqual(len(record['target_pins']), 5)
        self.assertEqual(record['scientific_record'], self.old)
        self.assertEqual(record['authorization']['payload_sha256'], h._digest(record))
        self.assertEqual(record['historical_authentication_status'], c.UNKNOWN)
        self.assertFalse(record['terminal'])
        with mock.patch.object(h, '_authority'):
            h.validate_intake(record, root=self.root)

    def test_intake_rejects_missing_changed_extra_map_binding_even_with_recomputed_receipt(self):
        original = self.make_intake()['record']
        for action in ('missing', 'changed', 'extra'):
            record = copy.deepcopy(original)
            if action == 'missing':
                record['target_pins'].pop('custody_map_pin')
            elif action == 'changed':
                record['target_pins']['custody_map_pin']['sha256'] = '0'*64
            else:
                record['target_pins']['unexpected_map'] = c.MAP_PIN
            record['authorization'] = h._receipt(record, self.context)
            with self.subTest(action=action), mock.patch.object(h, '_authority'), self.assertRaisesRegex(h.HistoricalIntakeError, 'target pins changed'):
                h.validate_intake(record, root=self.root)

    def test_review_replay_validates_original_map_and_rejects_later_map_drift(self):
        review = self.make_review(self.make_intake())
        with mock.patch.object(h, '_authority'):
            h.validate_review(review['record'], root=self.root)
        path = self.root / c.MAP_PIN['path']
        path.write_bytes(path.read_bytes() + b'\n')
        with mock.patch.object(h, '_authority'), self.assertRaisesRegex(h.HistoricalIntakeError, 'custody evidence byte drift'):
            h.validate_review(review['record'], root=self.root)

    def test_review_cannot_inherit_original_authorship_or_parent_completion(self):
        original = self.make_review(self.make_intake())['record']
        for field, value in [('reviewer_contribution_ids', [self.old['researcher_id']]), ('parent_completion_granted', True)]:
            record = copy.deepcopy(original)
            record[field] = value
            record['authorization'] = h._receipt(record, original['authorization']['context'])
            with self.subTest(field=field), mock.patch.object(h, '_authority'), self.assertRaisesRegex(h.HistoricalIntakeError, 'contributed|exceeds task scope'):
                h.validate_review(record, root=self.root)

    def test_current_authority_failure_still_precedes_science_and_persistence(self):
        with self.current(), mock.patch.object(h, '_authority', side_effect=h.HistoricalIntakeError('current GOV authority unavailable')), mock.patch.object(c, 'science') as science:
            with self.assertRaisesRegex(h.HistoricalIntakeError, 'current GOV authority unavailable'):
                h.freeze_intake(self.spec, self.context, root=self.root)
        science.assert_not_called()
        self.assertFalse((self.root / h.INTAKE_ROOT).exists())

    def test_profile_is_closed_to_exact_target_map_and_literal_false_flags(self):
        changes = [('schema', 'OTHER'), ('map_pin', {**c.MAP_PIN, 'sha256': '0'*64}), ('extra', True)]
        changes += [(field, value) for field in c.FALSE_FLAGS for value in (True, 0)]
        for field, value in changes:
            target = copy.deepcopy(self.target)
            target['historical_source_custody'][field] = value
            with self.subTest(field=field, value=value), self.assertRaises(h.HistoricalIntakeError):
                h._science(self.root, target)
        for field, value in [('task_id', 'RS-OTHER'), ('authorizing_governance_task_id', 'GV-OTHER'), ('historical_authentication_status', 'AUTHENTICATED'), ('historical_execution_evidence', {})]:
            with self.subTest(field=field), self.assertRaises(h.HistoricalIntakeError):
                h._science(self.root, {**self.target, field: value})

    def test_every_raw_byte_and_control_pin_is_exact(self):
        for row in self.mapping['entries']:
            path = self.root / row['physical_path']
            original = path.read_bytes()
            path.write_bytes(original + b'\n')
            with self.subTest(path=row['logical_path']), self.assertRaisesRegex(h.HistoricalIntakeError, 'byte drift'):
                h._science(self.root, self.target)
            path.write_bytes(original)
        for field in ('result_pin', 'execution_pin', 'publication_pin', 'taskbook_pin'):
            target = copy.deepcopy(self.target)
            target[field]['git_blob_sha1'] = '0'*40
            with self.subTest(field=field), self.assertRaisesRegex(h.HistoricalIntakeError, 'byte drift'):
                h._science(self.root, target)

    def test_exact_mapping_requires_all_six_unique_rows_and_no_extra_paths(self):
        for change in ('missing', 'extra', 'duplicate', 'foreign'):
            value = copy.deepcopy(self.mapping)
            if change == 'missing': value['entries'].pop()
            elif change == 'extra': value['entries'].append(copy.deepcopy(value['entries'][0]))
            elif change == 'duplicate': value['entries'][-1] = copy.deepcopy(value['entries'][0])
            else: value['entries'][0]['logical_path'] = 'research_returns/other.md'
            with self.subTest(change=change), self.assertRaises(h.HistoricalIntakeError):
                c._mapping(self.root, value, self.old)

    def test_mapping_path_escape_symlink_and_byte_count_are_rejected(self):
        for field, value in [('logical_path', '../escape'), ('logical_path', '/tmp/escape'), ('physical_path', '../escape'), ('physical_path', c.PREFIX+'/originals/../escape'), ('bytes', True), ('bytes', 1)]:
            mapping = copy.deepcopy(self.mapping)
            mapping['entries'][0][field] = value
            with self.subTest(field=field, value=value), self.assertRaises(h.HistoricalIntakeError):
                c._mapping(self.root, mapping, self.old)
        path = self.root / self.mapping['entries'][0]['physical_path']
        data = path.read_bytes()
        elsewhere = self.root / 'elsewhere'
        elsewhere.write_bytes(data)
        path.unlink()
        path.symlink_to(elsewhere)
        with self.assertRaisesRegex(h.HistoricalIntakeError, 'symlink or escape'):
            h._science(self.root, self.target)

    def test_single_secondary_observation_cannot_be_removed_changed_or_duplicated(self):
        for action in ('remove', 'change', 'duplicate'):
            mapping = copy.deepcopy(self.mapping)
            if action == 'remove': mapping['secondary_digest_observations'] = []
            elif action == 'change': mapping['secondary_digest_observations'][0]['actual_sha256'] = '0'*64
            else: mapping['secondary_digest_observations'] *= 2
            with self.subTest(action=action), self.assertRaisesRegex(h.HistoricalIntakeError, 'single exact secondary'):
                c._mapping(self.root, mapping, self.old)

    def test_canonical_raw_copy_or_alternate_er_alias_is_rejected(self):
        for row in self.mapping['entries'][-2:]:
            path = self.root / row['logical_path']
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes((self.root / row['physical_path']).read_bytes())
            with self.subTest(logical=row['logical_path']), self.assertRaisesRegex(h.HistoricalIntakeError, 'outside canonical logical paths'):
                h._science(self.root, self.target)
            path.unlink()
        er = json.loads((self.root / self.target['execution_pin']['path']).read_text())
        self.write('research_execution_records/RS-OTHER/alternate.json', er)
        with self.assertRaisesRegex(h.HistoricalIntakeError, 'cannot enter the canonical execution map'):
            h._science(self.root, self.target)

    def test_readonly_view_has_only_verified_bytes_and_never_enters_execution_map(self):
        view = c._ScientificView({'logical.md': b'original'})
        original = view / 'logical.md'
        self.assertTrue(original.exists())
        self.assertEqual(original.read_bytes(), b'original')
        for attr in ('write_bytes', 'write_text', 'open', '__fspath__'):
            self.assertFalse(hasattr(original, attr))
        for attr in ('glob', 'rglob', 'iterdir'):
            self.assertFalse(hasattr(view, attr))
        with self.assertRaisesRegex(h.HistoricalIntakeError, 'unmapped custody path'):
            view / 'other.md'
        actual = impl.execution_map
        with mock.patch.object(impl, 'execution_map', wraps=actual) as executions:
            h._science(self.root, self.target)
        self.assertEqual(executions.call_args_list, [mock.call(self.root)])

    def test_additional_or_missing_ordinary_audit_errors_are_rejected(self):
        for errors in (c.ERRORS + ['invalid terminal_verdict'], c.ERRORS[:-1]):
            with self.subTest(errors=errors), mock.patch.object(impl, 'audit_result_record', return_value=['RR: '+x for x in errors]):
                with self.assertRaisesRegex(h.HistoricalIntakeError, 'unapproved failure or changed diagnosis'):
                    h._science(self.root, self.target)
        target = copy.deepcopy(self.target)
        target['allowed_ordinary_audit_errors'].append('invalid terminal_verdict')
        with self.assertRaisesRegex(h.HistoricalIntakeError, 'only its exact historical diagnosis'):
            h._science(self.root, target)

    def test_existing_four_targets_keep_exact_original_four_pin_shape(self):
        others = [t for t in self.contract['targets'] if t['historical_result_id'] != c.RESULT]
        self.assertEqual(len(others), 4)
        for target in others:
            self.assertEqual(h._target_pins(target), {key: target[key] for key in ('result_pin','execution_pin','publication_pin','taskbook_pin')})


if __name__ == '__main__':
    unittest.main()
