import unittest
from pathlib import Path

from control_plane import research_startup_transport as startup
from tools import research_runtime_reducer

ROOT = Path(__file__).resolve().parents[1]


class ResearchStartupTransportTests(unittest.TestCase):
    def test_runtime_consumers_do_not_import_deleted_v1_scheduler(self):
        for relative in (
            "research_control_dispatch.py",
            "tools/research_lane_dispatch.py",
            "tools/research_lane_claims.py",
        ):
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertNotIn("research_scheduler", text, relative)

    def test_canonical_dispatch_uses_shared_current_transport(self):
        text = (ROOT / "research_control_dispatch.py").read_text(encoding="utf-8")
        self.assertIn("from control_plane import research_startup_transport", text)
        self.assertIn("research_startup_transport.attach(result)", text)
        self.assertNotIn("STARTUP_TRANSPORT = {", text)

    def test_explicit_runtime_authorize_and_adopt_attach_transport(self):
        text = (ROOT / "tools/research_runtime_guard.py").read_text(encoding="utf-8")
        self.assertIn("from control_plane import research_startup_transport as _startup", text)
        self.assertIn("result = _startup.attach(", text)
        self.assertGreaterEqual(text.count("_startup.attach("), 2)

    def test_transport_forces_idempotent_current_epoch_rebase(self):
        payload = startup.attach({"task_id": "RS-X"})["startup_transport"]
        self.assertEqual(payload["schema"], "ENTERPRISE_MATH_RESEARCH_STARTUP_TRANSPORT_V2")
        self.assertEqual(payload["control_epoch"], startup.CONTROL_EPOCH)
        self.assertTrue(payload["conversation_rebase_required"])
        rebase = payload["conversation_rebase"]
        self.assertEqual(rebase["mode"], "ALWAYS_IDEMPOTENT_ON_CONTROL_ENTRY")
        self.assertEqual(
            rebase["cached_conversation_control_plan"],
            "NONAUTHORITATIVE_REBASE_TO_CURRENT",
        )
        self.assertIn(
            "CI_WAIT_OR_REPEATED_CI_MONITOR_AS_CONVERSATION_BARRIER_WHEN_PENDING_NONBLOCKING",
            rebase["discard"],
        )
        self.assertIn(
            "REMOTE_SEARCH_OR_FETCH_AGENTS_MD_MERELY_FOR_TASK_START",
            rebase["discard"],
        )
        self.assertIn(
            "MANUAL_REPOSITORY_SCAN_OR_VISIBLE_TASK_RECORDS_AS_TASK_AVAILABILITY_AUTHORITY",
            rebase["discard"],
        )
        self.assertIn(
            "HIGHEST_VERIFIED_DURABLE_FRONTIER",
            rebase["preserve"],
        )
        self.assertEqual(
            rebase["ci_pending"],
            "PENDING_NONBLOCKING_CONTINUE_PARENT_TASK",
        )

    def test_transport_makes_canonical_dispatch_sole_task_availability_authority(self):
        payload = startup.attach({"task_id": "RS-X"})["startup_transport"]
        authority = payload["task_availability_authority"]
        self.assertEqual(
            authority["authority"],
            "CANONICAL_RESEARCH_CONTROL_DISPATCH_OUTPUT_ONLY",
        )
        self.assertEqual(
            authority["manual_repository_scan"],
            "NONAUTHORITATIVE_FOR_TASK_AVAILABILITY",
        )
        self.assertEqual(
            authority["higher_priority_leased"],
            "EXCLUDE_FROM_FRESH_CANDIDATES_AND_CONTINUE_CANONICAL_SCAN",
        )
        self.assertEqual(
            authority["free_axiom_discovery"],
            "SEPARATE_ROLE_ROUTE_NOT_ORDINARY_SCHEDULER_FALLBACK",
        )
        self.assertFalse(authority["manual_override_allowed"])
        self.assertIn(
            "CONSUME_CURRENT_CANONICAL_DISPATCH_DECISION",
            payload["hot_start"],
        )

    def test_leased_top_priority_tasks_do_not_block_lower_fresh_candidate(self):
        policy = {
            "selection_policy": {
                "state_order": ["HANDOFF_READY", "READY"],
                "priority_order": ["P0", "P1", "P2", "P3"],
                "leverage_order": ["FOUNDATION", "VERY_HIGH", "HIGH", "MEDIUM", "LOW"],
            }
        }
        states = [
            {
                "task_id": "RS-P0-A",
                "kind": "RESEARCH",
                "state": "READY",
                "dispatch_state": "LEASED",
                "priority": "P0",
                "leverage": "FOUNDATION",
            },
            {
                "task_id": "RS-P0-B",
                "kind": "RESEARCH",
                "state": "HANDOFF_READY",
                "dispatch_state": "LEASED",
                "priority": "P0",
                "leverage": "VERY_HIGH",
            },
            {
                "task_id": "RS-P0-BACKLOG",
                "kind": "RESEARCH",
                "state": "BACKLOG",
                "dispatch_state": "DORMANT",
                "priority": "P0",
                "leverage": "FOUNDATION",
            },
            {
                "task_id": "RS-P1-C",
                "kind": "RESEARCH",
                "state": "READY",
                "dispatch_state": "NEEDS_DISPATCH",
                "priority": "P1",
                "leverage": "HIGH",
            },
            {
                "task_id": "RS-P2-D",
                "kind": "RESEARCH",
                "state": "READY",
                "dispatch_state": "NEEDS_DISPATCH",
                "priority": "P2",
                "leverage": "FOUNDATION",
            },
        ]
        selected = research_runtime_reducer.select_state(states, policy, kind="RESEARCH")
        self.assertIsNotNone(selected)
        self.assertEqual(selected["task_id"], "RS-P1-C")

    def test_transport_is_nonsemantic_and_agents_nonblocking(self):
        payload = startup.attach({"task_id": "RS-X"})["startup_transport"]
        self.assertEqual(
            payload["agents_md"],
            "INJECTED_CONTEXT_ONLY_DO_NOT_REMOTE_SEARCH_OR_FETCH_FOR_TASK_START",
        )
        self.assertEqual(payload["remote_control_reads"], "TRIGGERED_ONLY")
        self.assertEqual(payload["taskbook_policy_digest_impact"], "NONE_CONTROL_TRANSPORT_ONLY")
        self.assertEqual(
            payload["conversation_rebase"]["taskbook_policy_digest_impact"],
            "NONE_CONTROL_TRANSPORT_ONLY",
        )


if __name__ == "__main__":
    unittest.main()
