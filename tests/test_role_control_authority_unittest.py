import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RoleControlAuthoritySimulationTests(unittest.TestCase):
    def read(self, path: str) -> str:
        return (ROOT / path).read_text(encoding="utf-8")

    def load(self, path: str):
        return json.loads(self.read(path))

    def test_narrow_control_precedence_is_current(self):
        data = self.load("control_plane/current_control_authority.json")
        self.assertEqual("ACTIVE_CANONICAL_CONTROL_PRECEDENCE", data["status"])
        self.assertEqual("research_task_publication_contract_v2.json", data["task_publication"]["contract"])
        self.assertEqual("tools/research_task_records.py", data["task_publication"]["tool"])
        self.assertEqual("READ_ONLY_COMPATIBILITY_AND_AUDIT_ONLY", data["task_publication"]["legacy_role"])
        self.assertEqual("research_control_dispatch.py", data["live_dispatch"]["canonical_entrypoint"])
        self.assertEqual("tools/research_dispatch.py", data["live_dispatch"]["ordinary_fresh_selector"])
        self.assertFalse(data["tool_reuse"]["coverage_lookup_is_tool_use"])
        self.assertTrue(data["tool_reuse"]["relevant_match_requires_reuse_resolution"])
        self.assertFalse(data["tool_reuse"]["execution_unavailability_is_capability_gap"])

    def test_task_publication_human_protocol_is_v2_only_for_new_work(self):
        text = self.read("docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md")
        self.assertIn("CANONICAL TASK PUBLICATION / V2", text)
        self.assertIn("tools/research_task_records.py", text)
        self.assertIn("research_control_dispatch.py", text)
        self.assertNotIn("python tools/research_task_registry.py publish", text)
        self.assertNotIn("python tools/research_task_registry.py new", text)
        self.assertIn("V1 compatibility", text)

    def test_driver_simulation_uses_v2_and_recovery_aware_dispatch(self):
        text = self.read("docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md")
        self.assertIn("V5.3", text)
        self.assertIn("Task publication: `research_task_publication_contract_v2.json`", text)
        self.assertIn("Canonical live dispatch: `research_control_dispatch.py`", text)
        self.assertIn("tools/research_task_registry.py` are V1 compatibility/read-only", text)
        self.assertIn("COVERAGE_LOOKUP != TOOL_USE", text)
        self.assertIn("REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE", text)
        self.assertNotIn("Task registry: `research_task_registry.json`", text)

    def test_free_researcher_simulation_preserves_phase_a_blindness_then_v2_phase_b(self):
        text = self.read("research_roles/EM_FREE_RESEARCHER_ROLE.md")
        self.assertIn("ROLE-SPECIFIC CONTRACT V6.4", text)
        self.assertIn("Task publication: `research_task_publication_contract_v2.json`", text)
        self.assertIn("PROJECT_TOOL_CATALOG", self.read("control_plane/current_control_authority.json"))
        self.assertIn("The shared toolbox/method inventory is hidden as a discovery prior before freeze", text)
        self.assertIn("Phase B — mandatory tool dedup and reuse resolution", text)
        self.assertIn("REUSE_EXECUTED", text)
        self.assertIn("tools/research_task_records.py", text)
        self.assertIn("research_control_dispatch.py", text)
        self.assertNotIn("pass `tools/research_task_registry.py audit`", text)

    def test_tool_lookup_cannot_masquerade_as_tool_use(self):
        policy = self.load("tool_invocation_policy.json")
        self.assertEqual("ENTERPRISE_MATH_TOOL_INVOCATION_POLICY_V2", policy["schema"])
        reuse = policy["reuse_resolution"]
        self.assertFalse(reuse["coverage_hit_is_tool_use"])
        self.assertTrue(reuse["required_after_any_relevant_match"])
        for state in (
            "REUSE_APPLIED",
            "REUSE_EXECUTED",
            "COMPOSE_APPLIED",
            "REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE",
            "EXTEND_EXISTING_TOOL",
            "CAPABILITY_GAP_CONFIRMED",
            "NOT_APPLICABLE",
        ):
            self.assertIn(state, reuse["states"])
        protocol = self.read("docs/ENTERPRISE_TOOL_INVOCATION_PROTOCOL.md")
        self.assertIn("TOOL_COVERAGE_LOOKUP != TOOL_USE", protocol)
        self.assertIn("The third layer discovers executable source but does not execute it", protocol)

    def test_control_plane_maintenance_does_not_inherit_mathematical_toolbox_gate(self):
        policy = self.load("tool_invocation_policy.json")
        control = policy["role_timing"]["CONTROL_PLANE_MAINTENANCE"]
        self.assertFalse(control["mandatory"])
        self.assertEqual("DO_NOT_OPEN", control["mathematical_toolbox_default"])
        self.assertIn("tool routing", control["when_allowed"])
        self.assertIn("not a research mode", control["scope_rule"])
        self.assertIn(
            "CONTROL_PLANE_MAINTENANCE_DOES_NOT_TRIGGER_MATHEMATICAL_TOOLBOX_BY_DEFAULT",
            policy["invariants"],
        )

    def test_v1_registry_surface_fails_closed_for_write_commands(self):
        text = self.read("tools/research_task_registry.py")
        self.assertIn("Read-only V1 task-registry compatibility surface", text)
        self.assertIn("use tools/research_task_records.py for publication", text)
        self.assertIn("for name in (\"new\", \"publish\", \"select\")", text)
        self.assertIn("_forbid(command)", text)

    def test_dispatch_contract_names_recovery_aware_top_level_entry(self):
        dispatch = self.load("research_dispatch_contract.json")
        self.assertEqual("research_control_dispatch.py", dispatch["canonical_tool"])
        self.assertEqual("tools/research_dispatch.py", dispatch["fresh_task_dispatch_tool"])
        self.assertEqual("tools/research_runtime_guard.py", dispatch["session_adoption_tool"])
        self.assertEqual(
            "ADOPT_EXISTING_WINNING_CLAIM_WITHOUT_NEW_CLAIM",
            dispatch["session_liveness_routing"]["valid_owner_plus_stale_session"],
        )

    def test_human_architecture_routes_all_roles_through_current_control_authority(self):
        text = self.read("docs/RESEARCH_ARCHITECTURE.md")
        self.assertIn("ACTIVE / CANONICAL GOVERNANCE / V2.6", text)
        self.assertIn("control_plane/current_control_authority.json", text)
        self.assertIn("research_task_publication_contract_v2.json", text)
        self.assertIn("research_control_dispatch.py", text)
        self.assertIn("TOOL_COVERAGE_LOOKUP != TOOL_USE", text)
        self.assertIn("CONTROL_PLANE_MAINTENANCE", text)
        self.assertNotIn("`research_task_registry.json` = canonical task existence/orphan prevention", text)

    def test_steward_addendum_uses_v2_handoff_and_reuse_resolution(self):
        text = self.read("docs/FOUNDATION_STEWARD_CONTROL_PLANE_ADDENDUM.md")
        self.assertIn("tools/research_task_records.py prepare", text)
        self.assertIn("research_control_dispatch.py", text)
        self.assertIn("COVERAGE_LOOKUP != TOOL_USE", text)
        self.assertIn("REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE", text)
        self.assertNotIn("edit `research_scheduler.json`", text)

    def test_control_plane_role_does_not_gain_research_authority(self):
        text = self.read("AGENTS.md")
        self.assertIn("CONTROL_PLANE_MAINTENANCE", text)
        self.assertIn("grants no Researcher, Driver, Steward, theorem, review, or promotion authority", text)
        precedence = self.load("control_plane/current_control_authority.json")
        expected = precedence["role_expectations"]["CONTROL_PLANE_MAINTENANCE"]
        self.assertIn("NO_RESEARCH_ROLE_IDENTITY", expected)
        self.assertIn("NO_THEOREM_OR_REVIEW_AUTHORITY", expected)


if __name__ == "__main__":
    unittest.main()
