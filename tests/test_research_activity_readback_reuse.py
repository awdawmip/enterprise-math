"""Synthetic local records only; no remote publication, research or claims."""
import copy
import base64
import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools import research_activity as activity


def observation(path, data):
    commit = 'a' * 40
    pin = {'repository': activity.REPOSITORY, 'commit': commit, 'path': path,
           'sha256': hashlib.sha256(data).hexdigest()}
    blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    return {**pin, 'readback': {
        'tool_name': 'github_fetch_file', 'observation_id': 'synthetic-local-fixture',
        'arguments': {'repository_full_name': pin['repository'], 'ref': commit, 'path': path},
        'result': {'isError': False, 'structuredContent': {
            'content': data.decode(), 'encoding': 'utf-8', 'sha': blob,
            'display_url': f"https://github.com/{pin['repository']}/blob/{commit}/{path}",
        }},
    }}


class ResearchActivityReadbackReuseTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / 'source'
        self.root.mkdir()
        self.activity_id = 'RA-TESTREUSE01'
        self.session_id = 'synthetic-local-session'
        self.source = observation('research_notes/synthetic-first.md', b'first synthetic source\n')
        activity.register(root=self.root, activity_id=self.activity_id, mode='TASK_RESEARCH',
                          session_id=self.session_id, researcher_id='EM-TEST-1234')


    def path(self):
        return activity.record_path(self.activity_id, self.root)


    def checkpoint(self, event_id, source=None, expected=None):
        return activity.checkpoint(self.activity_id, root=self.root, event_id=event_id,
            expected_sha256=expected or activity.digest(self.path().read_bytes()),
            em_sources=[self.source if source is None else source])


    def guard(self, registration=None):
        return activity.guard(activity_id=self.activity_id, root=self.root,
            session_id=self.session_id, boundary='pre-final', new_semantic_progress=False,
            registration_source=registration or observation(
                f'{activity.STORE}/{self.activity_id}.json', self.path().read_bytes()))


    def test_same_path_size_and_mtime_cannot_hide_changed_receipt_bytes(self):
        record = self.checkpoint('first')
        self.guard()
        receipt = self.root / record['checkpoints'][0]['em_sources'][0]['verification_receipt']
        before = receipt.stat()
        raw = receipt.read_bytes()
        changed = raw.replace(b'first synthetic source', b'other synthetic source')
        self.assertNotEqual(changed, raw)
        self.assertEqual(len(changed), len(raw))
        receipt.write_bytes(changed)
        os.utime(receipt, ns=(before.st_atime_ns, before.st_mtime_ns))
        with self.assertRaisesRegex(activity.ActivityError, 'receipt bytes drift'):
            self.guard()


    def test_mcp_observation_computes_one_blob_identity(self):
        source = copy.deepcopy(self.source)
        observed = source['readback']
        observed['tool_name'] = 'em_mcp_github_contents'
        content = observed['result']['structuredContent']
        raw = content['content'].encode()
        observed['github_response'] = {
            'type': 'file', 'path': source['path'], 'encoding': 'base64',
            'sha': content['sha'], 'size': len(raw), 'html_url': content['display_url'],
            'content': base64.b64encode(raw).decode(),
        }
        with patch.object(activity, 'blob_id', wraps=activity.blob_id) as blob:
            verified = activity.verify_observation(observed, source)
        self.assertEqual(blob.call_count, 1)
        self.assertEqual(verified['git_blob_sha1'], content['sha'])


    def test_changed_pinned_payload_is_rejected_even_with_a_matching_outer_digest(self):
        record = self.checkpoint('first')
        accepted = record['checkpoints'][0]['em_sources'][0]
        receipt = self.root / accepted['verification_receipt']
        payload = json.loads(receipt.read_bytes())
        payload['result']['structuredContent']['content'] = 'different source bytes'
        raw = activity.encoded(payload)
        sha = activity.digest(raw)
        accepted['verification_receipt_sha256'] = sha
        accepted['verification_receipt'] = f'{activity.STORE}/{self.activity_id}/readbacks/{sha}.json'
        (self.root / accepted['verification_receipt']).write_bytes(raw)
        with self.assertRaisesRegex(activity.ActivityError, 'content/blob/immutable URL'):
            activity._events(record, self.root)


    def test_cas_idempotency_and_conflicting_event_rules_remain(self):
        original = self.checkpoint('first')
        raw = self.path().read_bytes()
        self.assertEqual(self.checkpoint('first', expected='0' * 64), original)
        with self.assertRaisesRegex(activity.ActivityError, 'expected_sha256 mismatch'):
            self.checkpoint('new', expected='0' * 64)
        different = observation('research_notes/different.md', b'different\n')
        with self.assertRaisesRegex(activity.ActivityError, 'event_id conflict'):
            self.checkpoint('first', different)
        self.assertEqual(self.path().read_bytes(), raw)
        self.assertFalse(self.path().with_suffix('.lock').exists())


    def test_guard_reads_one_record_snapshot_and_rejects_a_newer_registration(self):
        self.checkpoint('first')
        current = activity.read(self.activity_id, self.root)
        newer = copy.deepcopy(current)
        newer['checkpoints'].append({'event_id': 'concurrent-debt', 'em_sources': [],
            'kb_sources': [], 'state': 'SYNC_DEBT', 'repairs_event_id': None})
        registration = observation(f'{activity.STORE}/{self.activity_id}.json', activity.encoded(newer))
        original_events = activity._events
        def concurrent_update(record, root):
            result = original_events(record, root)
            self.path().write_bytes(activity.encoded(newer))
            return result
        original_read = Path.read_bytes
        reads = []
        def read(path):
            reads.append(path)
            return original_read(path)
        with patch.object(activity, '_events', concurrent_update), patch.object(Path, 'read_bytes', read):
            with self.assertRaisesRegex(activity.ActivityError, 'registration publication does not match'):
                self.guard(registration)
        self.assertEqual(reads.count(self.path()), 1)


    def test_source_receipt_digest_is_computed_once(self):
        raw = activity.encoded(self.source['readback'])
        with patch.object(activity, 'digest', wraps=activity.digest) as digest:
            accepted, receipt = activity._source(self.source, self.activity_id)
        self.assertEqual(sum(call.args[0] == raw for call in digest.call_args_list), 1)
        self.assertEqual(receipt[1], raw)
        self.assertEqual(accepted['verification_receipt_sha256'], hashlib.sha256(raw).hexdigest())

    def test_persisted_observations_are_still_checked_on_each_operation(self):
        self.checkpoint('first')
        with patch.object(activity, 'verify_observation', wraps=activity.verify_observation) as verify:
            self.guard()
            self.guard()
        research_checks = [call for call in verify.call_args_list
                           if call.args[1]['path'] == self.source['path']]
        self.assertEqual(len(research_checks), 2)

    def test_repeated_sidecar_is_read_and_validated_once_in_each_operation(self):
        self.checkpoint('first')
        record = self.checkpoint('second')
        receipt = self.root / record['checkpoints'][0]['em_sources'][0]['verification_receipt']
        original_read = Path.read_bytes
        raw = original_read(receipt)
        for _ in range(2):
            reads = []
            def read(path):
                reads.append(path)
                return original_read(path)
            with patch.object(Path, 'read_bytes', read), \
                 patch.object(activity, 'verify_observation', wraps=activity.verify_observation) as verify, \
                 patch.object(activity, 'digest', wraps=activity.digest) as digest:
                self.assertEqual(list(activity._events(record, self.root)), ['first', 'second'])
            self.assertEqual(reads.count(receipt), 1)
            self.assertEqual(verify.call_count, 1)
            self.assertEqual(sum(call.args[0] == raw for call in digest.call_args_list), 1)

    def test_matching_actual_digest_does_not_relax_canonical_receipt_binding(self):
        record = self.checkpoint('first')
        source = record['checkpoints'][0]['em_sources'][0]
        original = self.root / source['verification_receipt']
        raw = json.dumps(json.loads(original.read_bytes()), separators=(',', ':')).encode()
        self.assertNotEqual(raw, original.read_bytes())
        sha = activity.digest(raw)
        source['verification_receipt_sha256'] = sha
        source['verification_receipt'] = f'{activity.STORE}/{self.activity_id}/readbacks/{sha}.json'
        (self.root / source['verification_receipt']).write_bytes(raw)
        with self.assertRaisesRegex(activity.ActivityError, 'stored source/verification fields drift'):
            activity._events(record, self.root)

    def test_new_call_detects_deleted_sidecar(self):
        record = self.checkpoint('first')
        self.guard()
        (self.root / record['checkpoints'][0]['em_sources'][0]['verification_receipt']).unlink()
        with self.assertRaises(FileNotFoundError):
            self.guard()

    def test_duplicate_receipt_cannot_substitute_a_different_source_pin(self):
        record = self.checkpoint('first')
        second = copy.deepcopy(record['checkpoints'][0])
        second['event_id'] = 'different-pin'
        second['em_sources'][0]['sha256'] = '0' * 64
        record['checkpoints'].append(second)
        with self.assertRaises(activity.ActivityError):
            activity._events(record, self.root)

    def test_existing_receipt_and_new_receipt_both_validate_on_every_call(self):
        self.checkpoint('first')
        second = observation('research_notes/second.md', b'second\n')
        record = self.checkpoint('second', second)
        for _ in range(2):
            with patch.object(activity, 'verify_observation', wraps=activity.verify_observation) as verify:
                self.assertEqual(len(activity._events(record, self.root)), 2)
            self.assertEqual(verify.call_count, 2)

    def test_session_binding_is_checked_on_each_guard(self):
        self.checkpoint('first')
        self.guard()
        with self.assertRaisesRegex(activity.ActivityError, 'different or unknown original session'):
            activity.guard(activity_id=self.activity_id, root=self.root,
                           session_id='different-live-session')

    def test_write_lock_remains_mandatory(self):
        self.checkpoint('first')
        before = self.path().read_bytes()
        lock = self.path().with_suffix('.lock')
        lock.write_text('existing-writer')
        with self.assertRaisesRegex(activity.ActivityError, 'write in progress'):
            self.checkpoint('next')
        self.assertEqual(self.path().read_bytes(), before)
        self.assertEqual(lock.read_text(), 'existing-writer')

    def test_repair_must_follow_the_debt_it_names(self):
        record = self.checkpoint('first')
        row = record['checkpoints'][0]
        row['repairs_event_id'] = 'later-debt'
        record['checkpoints'].append({'event_id': 'later-debt', 'em_sources': [],
            'kb_sources': [], 'state': 'SYNC_DEBT', 'repairs_event_id': None})
        with self.assertRaisesRegex(activity.ActivityError, 'earlier event'):
            activity._events(record, self.root)


if __name__ == '__main__':
    unittest.main()
