import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def assert_status_version_at_least(
    testcase: unittest.TestCase,
    text: str,
    major: int,
    minor: int,
) -> None:
    match = re.search(r"Status: `[^`]* / V(\d+)\.(\d+)`", text)
    testcase.assertIsNotNone(match, "router status version must be parseable")
    assert match is not None
    current = (int(match.group(1)), int(match.group(2)))
    testcase.assertGreaterEqual(current, (major, minor))


class AgentsRouterContractTests(unittest.TestCase):
    def test_agents_is_small_execution_router_not_research_catalog(self):
        text = read("AGENTS.md")
        self.assertIn("STABLE EXECUTION ROUTER", text)
        assert_status_version_at_least(self, text, 3, 0)
        self.assertIn("is not a theorem catalog", text)
        self.assertLess(len(text.splitlines()), 460)
        self.assertLess(len(text), 28500)
        for stale_or_agenda_token in (
            "Issue #164",
            "Research Relay #82",
            "classical pi",
            "root choice",
            "random-walk",
            "graph distance",
            "State Pair",
            "A4 correspondence",
        ):
            self.assertNotIn(stale_or_agenda_token, text)

    def test_agents_routes_source_only_control_fields_through_narrow_precedence(self):
        text = read("AGENTS.md")
        for marker in (
            "Narrow control-authority precedence",
            "control_plane/current_control_authority.json",
            "CONTROL_PRECEDENCE != MATHEMATICAL_PRECEDENCE",
            "READ_SNAPSHOT != REVIEW_WRITE_AUTHORITY",
            "research_review_write_authority.json",
        ):
            self.assertIn(marker, text)
        self.assertIn("does **not** override mathematical truth", text)

    def test_agents_routes_free_to_primitive_substrate_without_menu(self):
        text = read("AGENTS.md")
        self.assertIn("definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md", text)
        self.assertIn("FOUNDATION_FOR_DISCOVERY != CATALOG_OF_CURRENT_ACHIEVEMENTS", text)
        self.assertIn("NO_DEFAULT_DISCOVERY_LENS_MENU", text)
        self.assertIn("do not preload the general current-result router", text)
        self.assertIn("do not supply suggested questions or discovery-lens menus", text)
        self.assertIn("generic exclusion categories", text)

    def test_agents_task_start_is_exact_task_first_not_common_surface_first(self):
        text = read("AGENTS.md")
        self.assertIn("**exact task entry**", text)
        self.assertIn("first exact dependency required to begin", text)
        self.assertIn("Soft routine source-read budget before substantive work: `<= 3`", text)
        self.assertIn("Common Surface is a lookup", text)

    def test_agents_uses_current_candidate_successor_and_promotion_boundaries(self):
        text = read("AGENTS.md")
        for marker in (
            "RAW_AXIOM_CANDIDATE != WORKING_TRUTH != CANONICAL_FOUNDATION",
            "PASS_IS_NOT_A_SUCCESSOR_TRIGGER",
            "READY_PR != PROMOTION_LANE_LEASE",
            "docs/GOVERNANCE_MAINTENANCE_LIVENESS.md",
        ):
            self.assertIn(marker, text)

    def test_agents_preserves_tool_reuse_gate_after_identity_merge(self):
        text = read("AGENTS.md")
        for marker in (
            "tool_invocation_policy.json",
            "docs/ENTERPRISE_TOOL_INVOCATION_PROTOCOL.md",
            "enterprise_toolbox_registry.json",
            "research_method_inventory.json",
            "tools/enterprise_toolbox.py",
            "UNDERSTAND_TASK_FIRST -> TOOL_LOOKUP_SECOND",
            "COVERAGE_LOOKUP != TOOL_USE",
            "REUSE_EXECUTED",
            "REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE",
            "NEW_TOOL_DIRECTION_REQUIRES_CONFIRMED_CAPABILITY_GAP",
            "Discovery-firewall timing exception",
        ):
            self.assertIn(marker, text)

    def test_agents_makes_final_role_identity_footer_unconditional_for_research_roles(self):
        text = read("AGENTS.md")
        self.assertIn("final_response_identity_policy.json", text)
        self.assertIn(
            "ACTIVE_ENTERPRISE_MATH_RESEARCH_ROLE -> EVERY_ASSISTANT_FINAL_RESPONSE_ENDS_WITH_EXACTLY_ONE_ROLE_IDENTITY_MARKER",
            text,
        )
        self.assertIn(
            "`CONTROL_PLANE_MAINTENANCE` alone does not activate a research-role identity marker.",
            text,
        )
        self.assertIn("Driver-ID: <ID> / CONTROL_PLANE", text)
        self.assertIn("Steward-ID: <ID> / FOUNDATION_STEWARD", text)
        self.assertIn("Researcher-ID: <ID> / <TASK_ID>", text)
        self.assertIn("Researcher-ID: <ID> / FREE_AXIOM_DISCOVERY", text)
        self.assertIn("Researcher-ID: <ID> / TASK_RESEARCH", text)
        self.assertIn("Do not use `DIRECT` as a visible researcher scope", text)

    def test_agents_low_burden_dispatch_is_one_claim_and_no_poll_loop(self):
        text = read("AGENTS.md")
        self.assertIn("VALIDATE_CURRENT_PUBLICATION -> CREATE_OR_VERIFY_BRANCH -> ONE_CLAIM -> RESEARCH", text)
        self.assertIn("Do not require a second pre-claim execution-record write", text)
        self.assertIn("Between genuine semantic checkpoints, default added governance operations are zero", text)
        self.assertIn("comment ID orders events", text)
        self.assertIn("Edited event comments do not rewrite runtime history", text)

    def test_agents_has_chat_only_control_plane_soft_watchdog(self):
        text = read("AGENTS.md")
        for marker in (
            "CONTROL_PLANE_MAINTENANCE",
            "Control-plane efficiency soft watchdog",
            "USER_INTERRUPT -> PREEMPT_NONESSENTIAL_DIAGNOSTIC_EXPANSION",
            "SUFFICIENT_EVIDENCE -> STOP_DIAGNOSTIC_EXPANSION",
            "SAME_ERROR_SIGNATURE -> COLLAPSE_TO_ONE_ROOT_CAUSE",
            "READ_SNAPSHOT != WRITE_AUTHORITY",
        ):
            self.assertIn(marker, text)

    def test_tool_surface_matches_agents_role_routing_without_transition_guard(self):
        text = read("docs/EM_RESEARCH_TOOL_SURFACE.md")
        self.assertIn("HOT-PATH V5", text)
        self.assertIn("definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md", text)
        self.assertIn("definitions/00_CURRENT_NATIVE_FOUNDATION.md", text)
        self.assertIn("exact task entry", text)
        self.assertIn("Common Surface is a lookup, not a default context dump", text)
        self.assertNotIn("Until that source governance is promoted", text)
        self.assertIn("suggested question/lens menu", text)

    def test_free_role_preserves_blind_tool_timing_and_has_footer(self):
        text = read("research_roles/EM_FREE_RESEARCHER_ROLE.md")
        self.assertIn("V6.4", text)
        self.assertIn("NO_DEFAULT_DISCOVERY_LENS_MENU", text)
        self.assertIn("Phase B — mandatory tool dedup and reuse resolution", text)
        self.assertIn("tool_invocation_policy.json", text)
        self.assertIn("Researcher-ID: <ID> / FREE_AXIOM_DISCOVERY", text)
        self.assertIn("REUSE_EXECUTED", text)
        self.assertIn("research_task_publication_contract_v2.json", text)
        self.assertIn("tools/research_task_records.py", text)
        for seeded_example in (
            "invariance / locality",
            "composition / cancellation",
            "symmetry breaking",
            "minimal sufficient state",
        ):
            self.assertNotIn(seeded_example, text)


if __name__ == "__main__":
    unittest.main()
