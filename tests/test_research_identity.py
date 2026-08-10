import importlib.util
from datetime import datetime, timezone
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_tool(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


identity = load_tool("research_identity", "tools/research_identity.py")
scheduler = load_tool("research_scheduler", "tools/research_scheduler.py")


class ResearchIdentityTests(unittest.TestCase):
    def test_claim_identity_is_deterministic_and_lane_readable(self):
        rid1 = identity.deterministic_claim_id(
            "RS-R012-A3A4-RELATION-GENESIS-CATEGORY-BOUNDARY",
            "claim-alpha",
        )
        rid2 = identity.deterministic_claim_id(
            "RS-R012-A3A4-RELATION-GENESIS-CATEGORY-BOUNDARY",
            "claim-alpha",
        )
        rid3 = identity.deterministic_claim_id(
            "RS-R012-A3A4-RELATION-GENESIS-CATEGORY-BOUNDARY",
            "claim-beta",
        )
        self.assertEqual(rid1, rid2)
        self.assertNotEqual(rid1, rid3)
        self.assertTrue(rid1.startswith("EM-R012-"))
        self.assertTrue(identity.valid_researcher_id(rid1))
        self.assertEqual(
            identity.registration_path(rid1),
            f"projects/enterprise-math/researchers/{rid1}.json",
        )

    def test_direct_allocation_self_bootstraps(self):
        rid = identity.allocate_direct(
            task_id="RS-P017-GLOBAL-CAPACITY",
            role="RESEARCHER",
        )
        self.assertTrue(rid.startswith("EM-P017-"))
        self.assertTrue(identity.valid_researcher_id(rid))
        payload = identity.identity_payload(
            researcher_id=rid,
            task_id="RS-P017-GLOBAL-CAPACITY",
            role="RESEARCHER",
            source="DIRECT_AUTO_GENERATED",
        )
        self.assertEqual(payload["registration_state"], "REGISTER_PENDING")
        self.assertEqual(
            payload["registration_path"],
            f"projects/enterprise-math/researchers/{rid}.json",
        )
        self.assertEqual(
            identity.allocate_direct(
                task_id=None,
                role="RESEARCH_DRIVER",
                primary_driver=True,
            ),
            "EM-DRIVER-01",
        )

    def test_scheduler_claim_auto_allocates_identity(self):
        task = {
            "task_id": "RS-R012-A3A4-RELATION-GENESIS-CATEGORY-BOUNDARY",
            "base_state": "READY",
        }
        events = [
            {
                "event": "CLAIM",
                "task_id": task["task_id"],
                "claim_id": "claim-alpha",
                "actor": "agent",
                "at": "2026-08-11T00:00:00+08:00",
            }
        ]
        state = scheduler.reduce_task(
            task,
            events,
            default_lease_minutes=120,
            now=datetime(2026, 8, 10, 16, 30, tzinfo=timezone.utc),
        )
        expected = scheduler.researcher_id_for_claim(task, "claim-alpha")
        self.assertEqual(state["researcher_id"], expected)
        self.assertEqual(state["last_researcher_id"], expected)
        self.assertEqual(state["identity_source"], "AUTO_CLAIM_DERIVED")
        self.assertEqual(state["dispatch_state"], "LEASED")

    def test_wrong_explicit_identity_cannot_write_live_claim(self):
        task = {
            "task_id": "RS-R012-A3A4-RELATION-GENESIS-CATEGORY-BOUNDARY",
            "base_state": "READY",
        }
        correct = scheduler.researcher_id_for_claim(task, "claim-alpha")
        events = [
            {
                "event": "CLAIM",
                "task_id": task["task_id"],
                "claim_id": "claim-alpha",
                "researcher_id": correct,
                "at": "2026-08-11T00:00:00+08:00",
            },
            {
                "event": "PROGRESS",
                "task_id": task["task_id"],
                "claim_id": "claim-alpha",
                "researcher_id": "EM-R012-BAD1",
                "at": "2026-08-11T00:05:00+08:00",
                "progress_ref": "bad-progress",
            },
        ]
        state = scheduler.reduce_task(
            task,
            events,
            default_lease_minutes=120,
            now=datetime(2026, 8, 10, 16, 30, tzinfo=timezone.utc),
        )
        self.assertEqual(state["state"], "CLAIMED")
        self.assertEqual(state["researcher_id"], correct)
        self.assertEqual(len(state["ignored_events"]), 1)
        self.assertIn("does not match live claim identity", state["ignored_events"][0]["reason"])

    def test_handoff_releases_live_identity_but_keeps_last(self):
        task = {"task_id": "RS-P017-GLOBAL-CAPACITY", "base_state": "READY"}
        rid = scheduler.researcher_id_for_claim(task, "claim-a")
        events = [
            {
                "event": "CLAIM",
                "task_id": task["task_id"],
                "claim_id": "claim-a",
                "at": "2026-08-11T00:00:00+08:00",
            },
            {
                "event": "HANDOFF",
                "task_id": task["task_id"],
                "claim_id": "claim-a",
                "researcher_id": rid,
                "at": "2026-08-11T00:10:00+08:00",
                "next_action": "continue in a new conversation",
            },
        ]
        state = scheduler.reduce_task(
            task,
            events,
            default_lease_minutes=120,
            now=datetime(2026, 8, 10, 16, 30, tzinfo=timezone.utc),
        )
        self.assertIsNone(state["researcher_id"])
        self.assertEqual(state["last_researcher_id"], rid)
        self.assertEqual(state["dispatch_state"], "NEEDS_DISPATCH")


if __name__ == "__main__":
    unittest.main()
