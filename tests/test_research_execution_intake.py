import json
import pathlib
import unittest

from tools import research_control as rc

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = json.loads((ROOT / "research_control_state_machine.json").read_text())


class ExecutionIntakeControlTests(unittest.TestCase):
    def test_stale_orphan_requires_durable_evidence_ref(self):
        bad = {
            "schema": rc.V2_SCHEMA,
            "event": "ORPHAN",
            "task_id": "RS-X",
            "at": "2026-08-25T12:01:00+08:00",
            "driver_id": "EM-DVR-ABC123",
            "reason": "STALE_CONVERSATION_NO_VERIFIABLE_ACTION_10M",
        }
        errors = rc.validate_events([bad], SPEC)
        self.assertTrue(any("evidence_ref or recovery_ref" in error for error in errors))

        good = dict(bad, recovery_ref="research/checkpoint.md@abcdef1")
        self.assertEqual([], rc.validate_events([good], SPEC))

    def test_new_claim_requires_never_started_frontier_reconciliation(self):
        bad = {
            "schema": rc.V2_SCHEMA,
            "event": "CLAIM",
            "task_id": "RS-X",
            "at": "2026-08-25T12:01:00+08:00",
            "claim_id": "claim-1",
            "execution_id": "EM-RX-ABC123",
        }
        errors = rc.validate_events([bad], SPEC)
        self.assertTrue(any("frontier_class=NEVER_STARTED" in error for error in errors))
        self.assertTrue(any("frontier_ref" in error for error in errors))

        good = dict(
            bad,
            frontier_class="NEVER_STARTED",
            frontier_ref="research_tasks/x.md@abcdef1",
        )
        self.assertEqual([], rc.validate_events([good], SPEC))

    def test_adopt_requires_recoverable_frontier_class(self):
        bad = {
            "schema": rc.V2_SCHEMA,
            "event": "ADOPT",
            "task_id": "RS-X",
            "at": "2026-08-25T12:01:00+08:00",
            "claim_id": "claim-2",
            "execution_id": "EM-RX-DEF456",
            "recovery_ref": "research/checkpoint.md@abcdef1",
            "frontier_class": "VERIFIED_COMPLETE",
        }
        self.assertTrue(any("IN_PROGRESS_RECOVERABLE or UNFINISHED" in error for error in rc.validate_events([bad], SPEC)))

        good = dict(bad, frontier_class="IN_PROGRESS_RECOVERABLE")
        self.assertEqual([], rc.validate_events([good], SPEC))

    def test_pre_intake_cutover_history_is_not_retroactively_rejected(self):
        legacy = {
            "schema": rc.V2_SCHEMA,
            "event": "CLAIM",
            "task_id": "RS-X",
            "at": "2026-08-25T11:59:00+08:00",
            "claim_id": "claim-old",
            "execution_id": "EM-RX-ABC123",
        }
        self.assertEqual([], rc.validate_events([legacy], SPEC))


if __name__ == "__main__":
    unittest.main()
