import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ControlPlaneEfficiencyContractTests(unittest.TestCase):
    def test_machine_contract_covers_control_plane_soft_watchdog(self):
        data = json.loads((ROOT / "active_turn_liveness.json").read_text(encoding="utf-8"))
        self.assertIn("CONTROL_PLANE_MAINTENANCE", data["scope"])

        policy = data["control_plane_efficiency"]
        self.assertEqual("COOPERATIVE_SOFT_WATCHDOG", policy["model"])
        self.assertFalse(policy["hard_wall_clock_limit"])
        self.assertTrue(policy["research_compute_may_be_long_if_semantic_frontier_advances"])
        self.assertEqual({"min": 2, "max": 3}, policy["default_control_cycle_tool_calls"])
        self.assertEqual(2, policy["max_consecutive_tool_results_without_material_state_change"])
        self.assertEqual(
            "STOP_SAME_INSPECTION_PATH_AND_RETURN_CURRENT_RESULT_OR_SWITCH_STRATEGY",
            policy["after_two_no_progress_results"],
        )
        self.assertTrue(
            policy["user_interrupt"]["status_report_or_direction_change_preempts_nonessential_diagnostics"]
        )
        self.assertEqual("STOP_DIAGNOSTIC_EXPANSION", policy["sufficient_evidence"]["rule"])
        self.assertEqual("COLLAPSE_TO_ONE_ROOT_CAUSE", policy["same_error_signature"]["rule"])
        self.assertFalse(policy["mutation_authority"]["read_snapshot_is_write_authority"])
        self.assertTrue(
            policy["mutation_authority"]["refresh_target_authority_immediately_before_remote_mutation"]
        )

    def test_entry_routes_to_control_liveness_without_copying_rules(self):
        text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("control_plane/current_control_authority.json", text)
        authority = json.loads((ROOT / "control_plane/current_control_authority.json").read_text())
        self.assertTrue(authority["control_liveness"]["user_interrupt_preempts_nonessential_diagnostics"])
        self.assertFalse(authority["control_liveness"]["external_supervisor_has_mathematical_or_claim_authority"])

    def test_control_plane_mode_does_not_grant_research_authority(self):
        authority = json.loads((ROOT / "control_plane/current_control_authority.json").read_text())
        self.assertIn("NO_THEOREM_OR_REVIEW_AUTHORITY", authority["role_expectations"]["CONTROL_PLANE_MAINTENANCE"])


if __name__ == "__main__":
    unittest.main()
