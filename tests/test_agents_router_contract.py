import json
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







    def test_agents_routes_to_canonical_project_entries(self):
        text = read("AGENTS.md")
        self.assertIn("CONTRIBUTING.md#agentproject-task-entry", text)
        self.assertIn("control_plane/current_control_authority.json", text)
        self.assertIn("definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md", text)
        self.assertIn("private-repository access is not a prerequisite", text)
        # Every public relative route must resolve without private account access.
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if not target.startswith("https://"):
                self.assertTrue((ROOT / target.split("#")[0]).is_file(), target)
        contract = json.loads(read("research_dispatch_contract.json"))
        self.assertEqual("research_control_dispatch.py", contract["canonical_tool"])
        envelope = contract["server_event_envelope"]
        self.assertEqual("GitHub comment_id", envelope["ordering_authority"])
        self.assertFalse(envelope["body_actor_authority"])
        self.assertFalse(envelope["body_at_authority"])


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
