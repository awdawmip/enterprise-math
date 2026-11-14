"""Source reader/reducer integration against synthetic authenticated events."""
import copy
import json
import unittest
from unittest import mock

import test_research_continuation as fixtures
from control_plane import research_continuation as continuation
from tools import research_runtime_reducer as reducer
from tools import research_activity as activity


class ProgressNotesV2Tests(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.ContinuationTests()
        self.f.setUp()
        self.addCleanup(self.f.doCleanups)

    def test_nullable_notes_allow_real_source_frontier_and_preserve_contributors(self):
        frontier = copy.deepcopy(self.f.frontier)
        frontier.update(progress_notes_schema='ENTERPRISE_MATH_RESEARCH_PROGRESS_NOTES_V2', continuation_state='UNKNOWN', next_action=None, current_unfinished_unit=None)
        continuation.validate_frontier(frontier, root=self.f.root, source_commit=fixtures.SOURCE)
        event = self.f.successor()
        event['continuation']['frontier'] = frontier
        result = self.f.reduce(self.f.old, event)
        self.assertEqual('new', result['claim_id'])
        self.assertEqual(['EM-TEST-OLD1'], result['continuation_frontier']['contributor_ids'])
        self.assertIsNone(result['continuation_frontier']['next_action'])
        frontier.pop('progress_notes_schema')
        with self.assertRaises(continuation.ContinuationError):
            continuation.validate_frontier(frontier, root=self.f.root)

    def test_complete_progress_is_not_task_completion_and_clears_stale_action(self):
        event = {**self.f.old, 'event': 'PROGRESS', 'at': '2026-09-20T09:05:00Z',
                 'progress_notes_schema': 'ENTERPRISE_MATH_RESEARCH_PROGRESS_NOTES_V2', 'continuation_state': 'COMPLETE', 'next_action': None, 'progress_ref': 'saved-checkpoint'}
        result = self.f.reduce(self.f.old, event)
        self.assertEqual('old', result['claim_id'])
        self.assertEqual('IN_PROGRESS', result['state'])
        self.assertEqual('COMPLETE', result['continuation_state'])
        self.assertIsNone(result['next_action'])

    def test_later_legacy_progress_does_not_inherit_a_completed_unit_label(self):
        first = {**self.f.old, 'event': 'PROGRESS', 'at': '2026-09-20T09:05:00Z',
                 'progress_notes_schema': 'ENTERPRISE_MATH_RESEARCH_PROGRESS_NOTES_V2', 'continuation_state': 'COMPLETE', 'next_action': None}
        later = {**self.f.old, 'event': 'PROGRESS', 'at': '2026-09-20T09:06:00Z',
                 'next_action': 'new author-selected unit'}
        result = self.f.reduce(self.f.old, first, later)
        self.assertNotIn('continuation_state', result)
        self.assertEqual('new author-selected unit', result['next_action'])

    def test_handoff_without_invented_action_releases_only_current_owner(self):
        event = {**self.f.old, 'event': 'HANDOFF', 'at': '2026-09-20T09:05:00Z',
                 'handoff_scope': 'CONTINUATION', 'progress_notes_schema': 'ENTERPRISE_MATH_RESEARCH_PROGRESS_NOTES_V2', 'continuation_state': 'COMPLETE',
                 'next_action': None, 'progress_ref': 'saved-checkpoint'}
        result = self.f.reduce(self.f.old, event)
        self.assertIsNone(result['claim_id'])
        self.assertEqual('HANDOFF_READY', result['state'])
        self.assertNotIn('result_id', result)
        changed = {**event, 'claim_id': 'foreign-claim'}
        rejected = self.f.reduce(self.f.old, changed)
        self.assertEqual('old', rejected['claim_id'])

    def test_legacy_extra_state_field_does_not_reinterpret_past_handoff(self):
        event = {**self.f.old, 'event': 'HANDOFF', 'at': '2026-09-20T09:05:00Z',
                 'handoff_scope': 'CONTINUATION', 'continuation_state': 'COMPLETE', 'next_action': None}
        result = self.f.reduce(self.f.old, event)
        self.assertEqual('old', result['claim_id'])
        self.assertIn('HANDOFF requires next_action', result['ignored_events'][-1]['reason'])

    def test_checkpoint_v2_reader_retains_immutable_bytes_owner_and_scope_checks(self):
        checkpoint_path = 'research_artifacts/mcp/RS-TEST/old-conversation/v2/_checkpoint.json'
        record = {'schema': 'ENTERPRISE_MATH_MCP_EXECUTION_CHECKPOINT_V2',
            'task_id': 'RS-TEST', 'publication_id': 'TP2-TEST', 'claim_id': 'old',
            'ownership_epoch': 101, 'session_id': 'old-conversation', 'researcher_id': 'EM-TEST-OLD1',
            'progress_notes_schema': 'ENTERPRISE_MATH_RESEARCH_PROGRESS_NOTES_V2', 'continuation_state': 'COMPLETE', 'next_action': None, 'current_unfinished_unit': None,
            'completed_units': ['real fixture bytes'], 'do_not_repeat': [],
            'contributor_ids': ['EM-TEST-OLD1'], 'output_manifest': []}
        path = self.f.root / checkpoint_path
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps(record))
        self.f.publish_fixture(checkpoint_path)
        pointer = {**record, 'schema': 'ENTERPRISE_MATH_MCP_CHECKPOINT_POINTER_V1',
            'authority_granted': False, 'checkpoint_path': checkpoint_path,
            'checkpoint_sha256': continuation.artifact_pin(self.f.root, checkpoint_path, fixtures.SOURCE)['sha256'],
            'created_at': '2026-09-20T09:05:00Z'}
        locator = self.f.root / 'research_artifacts/mcp/RS-TEST/latest_checkpoint.json'
        locator.write_text(json.dumps(pointer))
        self.f.publish_fixture(locator.relative_to(self.f.root).as_posix())
        with mock.patch.object(continuation, '_definition', return_value=self.f.task):
            result = continuation.checkpoint_frontier('RS-TEST', 'TP2-TEST', root=self.f.root,
                events=[{**self.f.old, 'session_id': 'old-conversation'}], source_commit=fixtures.SOURCE)
            self.assertEqual('SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED', result['state'])
            self.assertFalse(result['execution_authorized'])
            self.assertIsNone(result['checkpoint']['next_action'])
            path.write_text('tampered')
            changed = continuation.checkpoint_frontier('RS-TEST', 'TP2-TEST', root=self.f.root,
                events=[self.f.old], source_commit=fixtures.SOURCE)
            self.assertEqual('UNKNOWN', changed['state'])

    def test_missing_activity_is_bookkeeping_pending_without_blocking_independent_research(self):
        result = activity.guard(activity_id=None, root=self.f.root)
        self.assertTrue(result['unshared_research_allowed'])
        self.assertFalse(result['activity_allowed'])
        self.assertFalse(any(result['authority'].values()))
        self.assertEqual(0, activity.main(['--root', str(self.f.root), 'guard']))
        audit = activity.audit_observations(activity_id=None, root=self.f.root)
        self.assertFalse(audit['persistence_allowed'])


if __name__ == '__main__':
    unittest.main()
