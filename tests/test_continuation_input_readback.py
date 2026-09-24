"""Current input pins are usable without inventing historical research evidence."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from control_plane import research_continuation as continuation
from tools import research_dispatch, research_result_records, research_task_records, research_taskbook


class InputReadbackTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.sha = 'a' * 40
        self.input = 'driver_reviews/previous_task.md'
        self.book = 'research_tasks/current.md'
        self.pub = 'research_task_records/RS-TEST/TP2-TEST.json'
        self.record = {'task_id': 'RS-TEST', 'publication_id': 'TP2-TEST', 'taskbook_path': self.book}
        self.definition = {**self.record, 'last_progress_ref': self.input, 'last_progress_at': '2026-08-29T01:00:00Z'}
        self.runtime = {**self.definition, 'claim_id': None, 'dispatch_state': 'NEEDS_DISPATCH',
                        'state': 'HANDOFF_READY', 'last_claim_id': 'OLD', 'last_claim_comment_id': 101,
                        'next_action': 'Prove the next exact finite case', 'last_researcher_id': 'EM-OLD'}
        self.manifest = {'schema': 'ENTERPRISE_MATH_SOURCE_BLOB_MANIFEST_V1', 'source_commit': self.sha, 'blobs': {}}
        self.publish(self.book, research_taskbook.render_taskbook({'task_id': 'RS-TEST'}, 'Frozen finite question.'))
        self.publish(self.pub, json.dumps(self.record))
        self.publish(self.input, 'Historical input: this text is not a new claimant result.\n')
        (self.root / 'EM_SNAPSHOT_READY.json').write_text(json.dumps({'sha': self.sha}))

    def publish(self, path, text):
        file = self.root / path
        file.parent.mkdir(parents=True, exist_ok=True)
        raw = text.encode()
        file.write_bytes(raw)
        self.manifest['blobs'][path] = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        (self.root / 'EM_SOURCE_BLOBS.json').write_text(json.dumps(self.manifest))

    def packet(self):
        with mock.patch.object(continuation, '_definition', return_value=self.definition), \
             mock.patch.object(research_task_records, 'current_records', return_value={'RS-TEST': self.record}), \
             mock.patch.object(research_dispatch, 'reduce_definition', return_value=self.runtime), \
             mock.patch.object(research_result_records, 'task_result_state', return_value=None):
            return continuation.continuation_packet('RS-TEST', root=self.root, events=[],
                now=continuation.datetime.fromisoformat('2026-09-23T00:00:00+00:00'), source_commit=self.sha)

    def test_bare_input_is_current_pin_not_historical_owner_evidence(self):
        packet = self.packet()
        pin = packet['progress_reference_readback']['pin']
        self.assertEqual(self.sha, pin['source_commit'])
        self.assertEqual('CURRENT_TASK_DEFINITION_INPUT_READBACK', pin['provenance'])
        self.assertFalse(pin['historical_bytes_verified'])
        self.assertFalse(pin['mathematical_acceptance_granted'])
        seed = packet['continuation_seed']
        self.assertEqual(('RS-TEST', 'TP2-TEST', 'OLD', 101), tuple(seed[k] for k in
            ('task_id', 'publication_id', 'previous_claim_id', 'previous_comment_id')))
        self.assertFalse(seed['completed_research_units_verified'])
        self.assertEqual([], packet['immutable_external_artifact_candidates'])
        self.assertFalse(packet['execution_authorized'])

    def test_new_owner_progress_is_not_relabelled_as_initial_input(self):
        self.runtime['last_progress_at'] = '2026-09-22T01:00:00Z'
        packet = self.packet()
        self.assertIsNone(packet['continuation_seed'])
        self.assertEqual('CURRENT_RUNTIME_REFERENCE_READBACK', packet['progress_reference_readback']['pin']['provenance'])

    def test_dirty_or_unpublished_input_never_receives_an_immutable_pin(self):
        (self.root / self.input).write_text('dirty')
        self.assertIsNone(self.packet()['progress_reference_readback'])
        self.manifest['blobs'].pop(self.input)
        (self.root / 'EM_SOURCE_BLOBS.json').write_text(json.dumps(self.manifest))
        self.assertIsNone(self.packet()['continuation_seed'])

    def test_fixed_branch_pin_remains_on_its_original_commit(self):
        self.runtime['last_progress_ref'] = f'https://github.com/awdawmip/enterprise-math/blob/{"b"*40}/research_returns/old.md'
        packet = self.packet()
        self.assertIsNone(packet['progress_reference_readback'])
        self.assertEqual('b'*40, packet['immutable_external_artifact_candidates'][0]['source_commit'])

    def test_live_claim_cannot_use_input_seed_to_bypass_takeover(self):
        self.runtime.update(claim_id='OLD', dispatch_state='LEASED', last_owner_activity_at='2026-09-23T00:00:00Z')
        self.assertIsNone(self.packet()['continuation_seed'])

    def test_restricted_input_is_not_exposed(self):
        from control_plane import research_source_firewall
        with mock.patch.object(research_source_firewall, 'validate_config', return_value={'allowed_source_pins': []}):
            packet = self.packet()
        self.assertIsNone(packet['progress_reference_readback'])
        self.assertIsNone(packet['continuation_seed'])
        self.assertNotIn(self.input, [pin['path'] for pin in packet['source_artifacts']])

    def test_completed_record_consumption_has_no_compute_prerequisite(self):
        self.runtime['dispatch_state'] = 'COMPLETE'
        packet = self.packet()
        self.assertFalse(packet['delivery_requirements']['local_environment_is_global_start_gate'])
        self.assertEqual('NOT_REQUIRED_FOR_COMPLETED_RECORD_CONSUMPTION', packet['delivery_requirements']['scientific_compute'])

    def test_declared_main_dependencies_and_blob_inputs_are_readable_and_exact(self):
        dependency = 'research_returns/previous.md'
        self.publish(dependency, 'Preserve the exact previous theorem statement.')
        meta = {'task_id': 'RS-TEST', 'dependencies': [dependency + '@main'],
                'source_refs': [self.input + '#blob=' + self.manifest['blobs'][self.input]]}
        self.publish(self.book, research_taskbook.render_taskbook(meta, 'Frozen question.'))
        packet = self.packet()
        self.assertIn(dependency, [pin['path'] for pin in packet['source_artifacts']])
        self.assertIn(self.input, [pin['path'] for pin in packet['source_artifacts']])
        meta['source_refs'] = [self.input + '#blob=' + 'f'*40]
        self.publish(self.book, research_taskbook.render_taskbook(meta, 'Frozen question.'))
        # A contradictory frozen input assertion must not be satisfied by a
        # separate progress-ref lookup of the same path.
        packet = self.packet()
        self.assertTrue(any('declared input blob differs' in item['error'] for item in packet['artifact_errors']))
        self.assertNotIn(self.input, [pin['path'] for pin in packet['source_artifacts']])
        self.assertIsNone(packet['continuation_seed'])

    def use_publication_marker(self):
        self.definition['last_progress_ref'] = self.record['publication_id']
        self.runtime['last_progress_ref'] = self.record['publication_id']

    def test_exact_initial_publication_marker_is_input_not_prior_research(self):
        self.use_publication_marker()
        original_claim = {key: self.runtime[key] for key in
                          ('last_claim_id', 'last_claim_comment_id', 'last_researcher_id')}
        packet = self.packet()
        seed = packet['continuation_seed']
        self.assertEqual('CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS', seed['state'])
        self.assertEqual([], seed['completed_units'])
        self.assertFalse(seed['completed_research_units_verified'])
        self.assertEqual(('RS-TEST', 'TP2-TEST', 'OLD', 101), tuple(seed[key] for key in
                         ('task_id', 'publication_id', 'previous_claim_id', 'previous_comment_id')))
        pin = seed['input_artifacts'][0]
        self.assertEqual(self.pub, pin['path'])
        self.assertEqual(self.sha, pin['source_commit'])
        self.assertEqual(self.manifest['blobs'][self.pub], pin['git_blob_sha1'])
        self.assertEqual('CURRENT_TASK_DEFINITION_INPUT_READBACK', pin['provenance'])
        self.assertFalse(pin['historical_bytes_verified'])
        self.assertFalse(pin['mathematical_acceptance_granted'])
        self.assertEqual('TP2-TEST', packet['progress_reference_readback']['original_reference'])
        self.assertEqual([], packet['frontier_template']['completed_units'])
        self.assertEqual([], packet['immutable_external_artifact_candidates'])
        self.assertFalse(packet['execution_authorized'])
        self.assertEqual(original_claim, {key: packet['runtime'][key] for key in original_claim})
        self.assertEqual(['EM-OLD'], packet['frontier_template']['contributor_ids'])

    def test_other_or_stale_publication_marker_cannot_seed_current_task(self):
        for marker in ('TP2-OTHER', 'TP2-STALE'):
            with self.subTest(marker=marker):
                self.definition['last_progress_ref'] = marker
                self.runtime['last_progress_ref'] = marker
                self.assertIsNone(self.packet()['continuation_seed'])

    def test_publication_marker_must_match_definition_reference_and_time(self):
        self.use_publication_marker()
        self.definition['last_progress_ref'] = self.input
        self.assertIsNone(self.packet()['continuation_seed'])
        self.use_publication_marker()
        self.runtime['last_progress_at'] = '2026-09-24T01:00:00Z'
        self.assertIsNone(self.packet()['continuation_seed'])
        self.definition['last_progress_at'] = None
        self.runtime['last_progress_at'] = None
        self.assertIsNone(self.packet()['continuation_seed'])

    def test_publication_marker_cannot_replace_live_owner_or_checkpoint(self):
        self.use_publication_marker()
        self.runtime.update(claim_id='OLD', dispatch_state='LEASED',
                            last_owner_activity_at='2026-09-23T00:00:00Z')
        self.assertIsNone(self.packet()['continuation_seed'])
        self.runtime.update(claim_id=None, dispatch_state='NEEDS_DISPATCH')
        for state in ('SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED', 'UNKNOWN'):
            with self.subTest(state=state), mock.patch.object(continuation, 'checkpoint_frontier',
                    return_value={'state': state, 'source_artifacts': [], 'execution_authorized': False}):
                self.assertIsNone(self.packet()['continuation_seed'])

    def test_publication_marker_requires_recorded_predecessor_and_dispatch(self):
        self.use_publication_marker()
        for key, value in (('last_claim_id', None), ('last_claim_comment_id', None),
                           ('last_claim_comment_id', True), ('dispatch_state', 'COMPLETE')):
            old = self.runtime[key]
            with self.subTest(key=key, value=value):
                self.runtime[key] = value
                self.assertIsNone(self.packet()['continuation_seed'])
            self.runtime[key] = old

    def test_publication_marker_requires_verified_current_record_bytes(self):
        self.use_publication_marker()
        (self.root / self.pub).write_text('dirty publication')
        self.assertIsNone(self.packet()['continuation_seed'])
        self.manifest['blobs'].pop(self.pub)
        (self.root / 'EM_SOURCE_BLOBS.json').write_text(json.dumps(self.manifest))
        self.assertIsNone(self.packet()['continuation_seed'])

    def test_publication_marker_respects_source_firewall(self):
        self.use_publication_marker()
        from control_plane import research_source_firewall
        with mock.patch.object(research_source_firewall, 'validate_config',
                               return_value={'allowed_source_pins': []}):
            packet = self.packet()
        self.assertIsNone(packet['continuation_seed'])
        self.assertIsNone(packet['progress_reference_readback'])
