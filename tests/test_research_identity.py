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
reducer = load_tool("research_runtime_reducer", "tools/research_runtime_reducer.py")


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
        self.assertEqual(payload["researcher_id"], rid)
        self.assertNotIn("driver_id", payload)
        self.assertNotIn("steward_id", payload)
        self.assertEqual(payload["identity_label"], "Researcher-ID")
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

    def test_driver_uses_driver_id_visible_label(self):
        did = identity.allocate_direct(
            task_id=None,
            role="RESEARCH_DRIVER",
            lane="DVR",
        )
        payload = identity.identity_payload(
            execution_id=did,
            task_id=None,
            role="RESEARCH_DRIVER",
            source="DIRECT_AUTO_GENERATED",
        )
        self.assertTrue(did.startswith("EM-DVR-"))
        self.assertEqual(payload["driver_id"], did)
        self.assertNotIn("researcher_id", payload)
        self.assertNotIn("steward_id", payload)
        self.assertEqual(payload["identity_label"], "Driver-ID")
        self.assertEqual(payload["visible_marker"], f"Driver-ID: {did} / CONTROL_PLANE")

    def test_foundation_steward_is_first_class_identity_without_new_registration_gate(self):
        sid = identity.allocate_direct(
            task_id=None,
            role="FOUNDATION_STEWARD",
        )
        payload = identity.identity_payload(
            execution_id=sid,
            task_id=None,
            role="FOUNDATION_STEWARD",
            source="DIRECT_AUTO_GENERATED",
        )
        self.assertTrue(sid.startswith("EM-STW-"))
        self.assertEqual(payload["steward_id"], sid)
        self.assertNotIn("researcher_id", payload)
        self.assertNotIn("driver_id", payload)
        self.assertEqual(payload["identity_label"], "Steward-ID")
        self.assertEqual(payload["visible_marker"], f"Steward-ID: {sid} / FOUNDATION_STEWARD")
        self.assertEqual(payload["registration_state"], "REGISTER_PENDING")
        self.assertEqual(
            payload["registration_path"],
            f"projects/enterprise-math/researchers/{sid}.json",
        )

    def test_foundation_steward_cannot_take_researcher_claim_identity_path(self):
        with self.assertRaisesRegex(ValueError, "scheduler CLAIM identity is a Researcher-ID"):
            identity.main([
                "allocate",
                "--role", "FOUNDATION_STEWARD",
                "--task", "RS-T",
                "--claim-id", "c1",
            ])

    def test_manual_dispatch_preallocates_researcher_identity(self):
        task = "RS-R020-P021-WITNESS-CARDINALITY-DYNAMIC-COMPLETENESS-REAUDIT"
        rid1 = identity.deterministic_dispatch_id(task, "relay-20260811-1", lane="R020")
        rid2 = identity.deterministic_dispatch_id(task, "relay-20260811-1", lane="R020")
        rid3 = identity.deterministic_dispatch_id(task, "relay-20260811-2", lane="R020")
        self.assertEqual(rid1, rid2)
        self.assertNotEqual(rid1, rid3)
        self.assertTrue(rid1.startswith("EM-R020-"))
        payload = identity.identity_payload(
            execution_id=rid1,
            task_id=task,
            role="RESEARCHER",
            source="MANUAL_DISPATCH_DERIVED",
        )
        self.assertEqual(payload["visible_marker"], f"Researcher-ID: {rid1} / {task}")

    def test_runtime_claim_auto_allocates_identity(self):
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
        state = reducer.reduce_task(
            task,
            events,
            default_lease_minutes=120,
            now=datetime(2026, 8, 10, 16, 30, tzinfo=timezone.utc),
        )
        expected = reducer.researcher_id_for_claim(task, "claim-alpha")
        self.assertEqual(state["researcher_id"], expected)
        self.assertEqual(state["last_researcher_id"], expected)
        self.assertEqual(state["identity_source"], "AUTO_CLAIM_DERIVED")
        self.assertEqual(state["dispatch_state"], "LEASED")

    def test_wrong_explicit_identity_cannot_write_live_claim(self):
        task = {
            "task_id": "RS-R012-A3A4-RELATION-GENESIS-CATEGORY-BOUNDARY",
            "base_state": "READY",
        }
        correct = reducer.researcher_id_for_claim(task, "claim-alpha")
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
        state = reducer.reduce_task(
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
        rid = reducer.researcher_id_for_claim(task, "claim-a")
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
        state = reducer.reduce_task(
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
