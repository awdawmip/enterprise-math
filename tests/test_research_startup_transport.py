import unittest
from pathlib import Path

from control_plane import research_startup_transport as startup

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
            "HIGHEST_VERIFIED_DURABLE_FRONTIER",
            rebase["preserve"],
        )
        self.assertEqual(
            rebase["ci_pending"],
            "PENDING_NONBLOCKING_CONTINUE_PARENT_TASK",
        )

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
