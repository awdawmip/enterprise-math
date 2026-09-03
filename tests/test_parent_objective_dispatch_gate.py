import unittest
from pathlib import Path
from unittest.mock import patch

from control_plane import research_parent_objective_dispatch_gate as gate


class ParentObjectiveDispatchGateTests(unittest.TestCase):
    def task(self):
        return {
            "task_id": "RS-X",
            "parent_objective_id": "OBJ-X",
            "registration_source": "IMMUTABLE_TASK_RECORD",
        }

    def test_open_parent_leaves_operational_state_untouched(self):
        state = {"state": "READY", "dispatch_state": "NEEDS_DISPATCH"}
        with patch(
            "research_objective_records.current_head",
            return_value={
                "objective_generation_id": "OG-OPEN",
                "objective_status": "OPEN",
            },
        ):
            out = gate.apply_parent_objective_gate(self.task(), state, Path("."))
        self.assertEqual(out, state)

    def test_closed_parent_revokes_stale_claim_without_erasing_provenance(self):
        state = {
            "state": "ACTIVE",
            "dispatch_state": "OWNED",
            "claim_id": "claim-x",
            "actor": "Researcher",
            "researcher_id": "EM-X-ABC123",
            "lease_until": "2026-09-03T20:00:00+08:00",
        }
        with patch(
            "research_objective_records.current_head",
            return_value={
                "objective_generation_id": "OG-CLOSED",
                "objective_status": "CLOSED",
            },
        ):
            out = gate.apply_parent_objective_gate(self.task(), state, Path("."))
        self.assertEqual(out["state"], "BLOCKED")
        self.assertEqual(out["dispatch_state"], "PARENT_OBJECTIVE_CLOSED")
        self.assertIsNone(out["claim_id"])
        self.assertEqual(
            out["suppressed_operational_state_due_to_parent_objective"]["claim_id"],
            "claim-x",
        )
        block = out["hard_block"]
        self.assertEqual(block["parent_objective_id"], "OBJ-X")
        self.assertEqual(block["objective_generation_id"], "OG-CLOSED")
        self.assertEqual(block["objective_status"], "CLOSED")
        for key in ("missing_object", "owner", "necessity", "unblock_condition"):
            self.assertTrue(block[key])

    def test_parked_parent_overrides_result_reopen(self):
        state = {
            "state": "HANDOFF_READY",
            "dispatch_state": "NEEDS_DISPATCH",
            "result_id": "RR-X",
            "driver_disposition": "RETURN_TO_OWNER",
        }
        with patch(
            "research_objective_records.current_head",
            return_value={
                "objective_generation_id": "OG-PARKED",
                "objective_status": "PARKED",
            },
        ):
            out = gate.apply_parent_objective_gate(self.task(), state, Path("."))
        self.assertEqual(out["state"], "BLOCKED")
        self.assertEqual(out["dispatch_state"], "PARENT_OBJECTIVE_PARKED")
        self.assertEqual(out["result_id"], "RR-X")
        self.assertEqual(
            out["suppressed_operational_state_due_to_parent_objective"]["state"],
            "HANDOFF_READY",
        )


if __name__ == "__main__":
    unittest.main()
