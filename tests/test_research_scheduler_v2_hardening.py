import json
import pathlib
import tempfile
import unittest

from tools import research_scheduler as rs


def policy():
    return {
        "priority_order": ["P0", "P1", "P2", "P3"],
        "leverage_order": ["HIGH", "MEDIUM", "LOW"],
        "state_order": ["HANDOFF_READY", "READY"],
    }


def cfg(*tasks, discover=False):
    return {
        "schema": rs.SCHEDULER_SCHEMA_V2,
        "claim_lease_minutes": 30,
        "task_states": sorted(rs.V2_TASK_STATES),
        "event_types": sorted(rs.V2_EVENT_TYPES),
        "selection_policy": policy(),
        "tasks": list(tasks),
        "require_static_owner_coverage": False,
        "taskbook_registry": {"discover": discover},
    }


def task(task_id="RS-T", *, owner="owner/a", state="READY"):
    return {
        "task_id": task_id,
        "title": task_id,
        "kind": "RESEARCH",
        "owner": owner,
        "base_state": state,
        "priority": "P1",
        "leverage": "HIGH",
        "frontier": "frontier",
        "next_action": "next",
        "dependencies": [],
        "source_refs": [],
        "last_progress_ref": "seed",
        "last_progress_at": "2026-08-24T10:00:00+08:00",
        "hard_block": None,
    }


def event(kind, at, *, task_id="RS-T", schema=None, **extra):
    value = {
        "schema": schema or rs.EVENT_SCHEMA_V2,
        "event": kind,
        "task_id": task_id,
        "actor": "test",
        "at": at,
    }
    value.update(extra)
    return value


class SchedulerV2HardeningTests(unittest.TestCase):
    def test_publish_rejects_malformed_dynamic_payload(self):
        payload = task("RS-BAD", owner="taskbook/unassigned")
        payload["dependencies"] = [{"target": "x", "action": "BOGUS", "satisfied": False}]
        events = [event(
            "PUBLISH",
            "2026-08-24T11:00:00+08:00",
            task_id="RS-BAD",
            task=payload,
            publisher_role="RESEARCHER",
            publisher_id="EM-FREE-AB12CD",
        )]
        items, diagnostics = rs.materialize_tasks(cfg(), events, taskbook_dir=None)
        self.assertFalse(any(item["task_id"] == "RS-BAD" for item in items))
        self.assertTrue(any("invalid task payload" in row["message"] for row in diagnostics))

    def test_legacy_event_registered_taskbook_replays_instead_of_orphaning(self):
        with tempfile.TemporaryDirectory() as td:
            directory = pathlib.Path(td)
            payload = task("RS-LEGACY")
            (directory / "task.md").write_text(
                "<!-- ENTERPRISE_MATH_TASK_V1\n" + json.dumps(payload) + "\n-->\n",
                encoding="utf-8",
            )
            events = [
                event(
                    "CLAIM", "2026-08-24T12:00:00+08:00",
                    task_id="RS-LEGACY", schema=rs.EVENT_SCHEMA_V1,
                    claim_id="legacy-c", lease_minutes=30,
                ),
                event(
                    "HANDOFF", "2026-08-24T12:10:00+08:00",
                    task_id="RS-LEGACY", schema=rs.EVENT_SCHEMA_V1,
                    claim_id="legacy-c", next_action="resume legacy work",
                ),
            ]
            items, diagnostics = rs.materialize_tasks(cfg(discover=True), events, taskbook_dir=directory)
            self.assertFalse(diagnostics)
            item = next(value for value in items if value["task_id"] == "RS-LEGACY")
            self.assertEqual("LEGACY_EVENT_REGISTERED_TASKBOOK", item["registry_source"])
            self.assertEqual("READY", item["base_state"])
            state = rs.reduce_task(
                item,
                events,
                default_lease_minutes=30,
                now=rs.parse_time("2026-08-24T12:11:00+08:00"),
            )
            self.assertEqual("HANDOFF_READY", state["state"])

    def test_adopt_can_reassign_orphan_to_active_owner(self):
        item = task(owner="inactive/owner", state="ORPHANED")
        item["orphan_reason"] = "LEGACY_OWNER_RETIRED"
        events = [event(
            "ADOPT",
            "2026-08-24T12:40:00+08:00",
            reviewer_id="EM-DVR-ABC123",
            review_ref="driver_reviews/orphan.md",
            assigned_owner="owner/a",
            next_action="resume",
        )]
        state = rs.reduce_task(
            item,
            events,
            default_lease_minutes=30,
            now=rs.parse_time("2026-08-24T12:41:00+08:00"),
            active_research_owners={"owner/a"},
        )
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("owner/a", state["owner"])

    def test_orphan_recovery_review_can_reassign_owner(self):
        item = task(owner="taskbook/unassigned", state="ORPHANED")
        item["orphan_reason"] = "UNREGISTERED_LEGACY"
        events = [event(
            "REVIEW",
            "2026-08-24T12:40:00+08:00",
            review_kind="ORPHAN_RECOVERY",
            verdict="APPROVE",
            reviewer_id="EM-DVR-ABC123",
            review_ref="driver_reviews/orphan.md",
            assigned_owner="owner/a",
            next_action="resume",
        )]
        state = rs.reduce_task(
            item,
            events,
            default_lease_minutes=30,
            now=rs.parse_time("2026-08-24T12:41:00+08:00"),
            active_research_owners={"owner/a"},
        )
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("owner/a", state["owner"])


if __name__ == "__main__":
    unittest.main()
