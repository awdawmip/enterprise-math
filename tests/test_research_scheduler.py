import json
import pathlib
import tempfile
import unittest

from tools import research_scheduler as rs

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA_V2 = getattr(rs, "CONFIG_SCHEMA_V2", "ENTERPRISE_MATH_RESEARCH_SCHEDULER_V2")


def policy():
    return {
        "priority_order": ["P0", "P1", "P2", "P3"],
        "leverage_order": ["HIGH", "MEDIUM", "LOW"],
        "state_order": ["HANDOFF_READY", "READY"],
    }


def cfg(*items):
    return {
        "schema": SCHEMA_V2,
        "claim_lease_minutes": 30,
        "task_states": [
            "BACKLOG", "PENDING_REVIEW", "READY", "CLAIMED", "IN_PROGRESS",
            "HANDOFF_READY", "RETURNED", "BLOCKED", "ORPHANED", "DONE",
            "REJECTED", "SUPERSEDED",
        ],
        "event_types": [
            "PUBLISH", "REGISTER_ORPHAN", "REVIEW", "CLAIM", "HEARTBEAT",
            "PROGRESS", "RETURN", "HANDOFF", "HARD_BLOCK", "UNBLOCK",
            "ORPHAN", "ADOPT", "DONE", "SUPERSEDE",
        ],
        "selection_policy": policy(),
        "require_static_owner_coverage": False,
        "tasks": list(items),
    }


def owners(*names):
    return {"branches": {name: {"state": "ACTIVE_OWNER"} for name in names}}


def task(task_id="RS-T1", *, owner="owner/a", state="READY", priority="P1", leverage="HIGH"):
    return {
        "task_id": task_id,
        "title": task_id,
        "kind": "RESEARCH",
        "owner": owner,
        "base_state": state,
        "priority": priority,
        "leverage": leverage,
        "frontier": "frontier",
        "next_action": "next",
        "dependencies": [],
        "source_refs": [],
        "last_progress_ref": "seed",
        "last_progress_at": "2026-08-24T10:00:00+08:00",
        "hard_block": None,
    }


def event(kind, at, *, task_id="RS-T1", claim_id=None, schema=None, **extra):
    value = {
        "schema": schema or rs.EVENT_SCHEMA_V2,
        "event": kind,
        "task_id": task_id,
        "actor": "test",
        "at": at,
    }
    if claim_id is not None:
        value["claim_id"] = claim_id
    value.update(extra)
    return value


class SchedulerRepositoryTests(unittest.TestCase):
    def test_v2_config_imports_v1_seed_and_validates(self):
        config = rs.load_scheduler_config(ROOT / "research_scheduler_v2.json")
        owner_map = json.loads((ROOT / "branch_governance_overrides.json").read_text(encoding="utf-8"))
        self.assertEqual(SCHEMA_V2, config["schema"])
        self.assertEqual([], rs.validate_scheduler(config, owner_map))

    def test_unregistered_repository_taskbook_is_visible_as_orphan(self):
        config = rs.load_scheduler_config(ROOT / "research_scheduler_v2.json")
        items, _ = rs.materialize_tasks(config, [], taskbook_dir=ROOT / "research_tasks")
        item = next(
            value for value in items
            if value["task_id"] == "RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE"
        )
        self.assertEqual("ORPHANED", item["base_state"])
        self.assertEqual("TASKBOOK_NOT_REGISTERED_IN_SCHEDULER_V2", item["orphan_reason"])

    def test_invalid_static_owner_is_rejected(self):
        errors = rs.validate_scheduler(cfg(task(owner="missing")), owners("owner/a"))
        self.assertTrue(any("not ACTIVE_OWNER" in row for row in errors))


class SchedulerV2LifecycleTests(unittest.TestCase):
    def now(self, value):
        return rs.parse_time(value)

    def publish(self, *, role="RESEARCHER", publisher="EM-FREE-AB12CD", owner="taskbook/unassigned"):
        events = [
            event(
                "PUBLISH",
                "2026-08-24T11:00:00+08:00",
                task_id="RS-NEW",
                task=task("RS-NEW", owner=owner),
                publisher_role=role,
                publisher_id=publisher,
            )
        ]
        items, diagnostics = rs.materialize_tasks(cfg(), events, taskbook_dir=None)
        self.assertFalse(diagnostics)
        return next(value for value in items if value["task_id"] == "RS-NEW"), events

    def test_free_researcher_can_publish_but_cannot_make_ready(self):
        item, events = self.publish()
        state = rs.reduce_task(
            item, events, default_lease_minutes=30,
            now=self.now("2026-08-24T11:01:00+08:00"),
        )
        self.assertEqual("PENDING_REVIEW", state["state"])
        self.assertEqual("NEEDS_REVIEW", state["dispatch_state"])

    def test_driver_publisher_cannot_self_review_dispatch(self):
        item, events = self.publish(role="RESEARCH_DRIVER", publisher="EM-DVR-ABC123", owner="owner/a")
        events.append(
            event(
                "REVIEW", "2026-08-24T11:05:00+08:00", task_id="RS-NEW",
                review_kind="DISPATCH", verdict="APPROVE",
                reviewer_id="EM-DVR-ABC123", review_ref="self-review",
            )
        )
        state = rs.reduce_task(
            item, events, default_lease_minutes=30,
            now=self.now("2026-08-24T11:06:00+08:00"),
        )
        self.assertEqual("PENDING_REVIEW", state["state"])
        self.assertTrue(state["ignored_events"])

    def test_dispatch_review_requires_active_owner(self):
        item, events = self.publish()
        events.append(
            event(
                "REVIEW", "2026-08-24T11:05:00+08:00", task_id="RS-NEW",
                review_kind="DISPATCH", verdict="APPROVE",
                reviewer_id="EM-DVR-ABC123", review_ref="review",
                assigned_owner="inactive/owner",
            )
        )
        state = rs.reduce_task(
            item, events, default_lease_minutes=30,
            now=self.now("2026-08-24T11:06:00+08:00"),
            active_research_owners={"owner/a"},
        )
        self.assertEqual("PENDING_REVIEW", state["state"])
        self.assertTrue(any("ACTIVE_OWNER" in row["reason"] for row in state["ignored_events"]))

    def test_independent_dispatch_review_releases_ready(self):
        item, events = self.publish()
        events.append(
            event(
                "REVIEW", "2026-08-24T11:05:00+08:00", task_id="RS-NEW",
                review_kind="DISPATCH", verdict="APPROVE",
                reviewer_id="EM-DVR-ABC123", review_ref="review",
                assigned_owner="owner/a",
            )
        )
        state = rs.reduce_task(
            item, events, default_lease_minutes=30,
            now=self.now("2026-08-24T11:06:00+08:00"),
            active_research_owners={"owner/a"},
        )
        self.assertEqual("READY", state["state"])
        self.assertEqual("owner/a", state["owner"])

    def test_lease_expiry_creates_orphan_history(self):
        events = [
            event(
                "CLAIM", "2026-08-24T12:00:00+08:00",
                claim_id="c1", lease_minutes=30,
            )
        ]
        state = rs.reduce_task(
            task(), events, default_lease_minutes=30,
            now=self.now("2026-08-24T12:31:00+08:00"),
        )
        self.assertEqual("ORPHANED", state["state"])
        self.assertEqual("CLAIM_LEASE_EXPIRED", state["orphan_history"][-1]["reason"])
        self.assertIsNone(state["claim_id"])

    def test_orphan_adoption_requires_active_owner(self):
        item = task(owner="inactive/owner", state="ORPHANED")
        events = [
            event(
                "ADOPT", "2026-08-24T12:40:00+08:00",
                reviewer_id="EM-DVR-ABC123", review_ref="review",
                next_action="resume",
            )
        ]
        state = rs.reduce_task(
            item, events, default_lease_minutes=30,
            now=self.now("2026-08-24T12:41:00+08:00"),
            active_research_owners={"owner/a"},
        )
        self.assertEqual("ORPHANED", state["state"])

    def test_worker_return_requires_driver_review_before_done(self):
        events = [
            event("CLAIM", "2026-08-24T13:00:00+08:00", claim_id="c1"),
            event(
                "RETURN", "2026-08-24T13:10:00+08:00",
                claim_id="c1", return_ref="research_returns/x.md",
            ),
        ]
        state = rs.reduce_task(
            task(), events, default_lease_minutes=30,
            now=self.now("2026-08-24T13:11:00+08:00"),
        )
        self.assertEqual("RETURNED", state["state"])
        self.assertEqual("NEEDS_REVIEW", state["dispatch_state"])

        events.append(
            event(
                "REVIEW", "2026-08-24T13:20:00+08:00",
                review_kind="RETURN", verdict="APPROVE",
                reviewer_id="EM-DVR-ABC123", review_ref="driver_reviews/x.md",
            )
        )
        state = rs.reduce_task(
            task(), events, default_lease_minutes=30,
            now=self.now("2026-08-24T13:21:00+08:00"),
        )
        self.assertEqual("DONE", state["state"])
        self.assertEqual("COMPLETE", state["dispatch_state"])

    def test_v2_direct_done_is_rejected_but_v1_done_replays(self):
        v2_events = [
            event("CLAIM", "2026-08-24T13:00:00+08:00", claim_id="c1"),
            event("DONE", "2026-08-24T13:05:00+08:00", claim_id="c1", progress_ref="bad"),
        ]
        state = rs.reduce_task(
            task(), v2_events, default_lease_minutes=30,
            now=self.now("2026-08-24T13:06:00+08:00"),
        )
        self.assertNotEqual("DONE", state["state"])
        self.assertTrue(state["ignored_events"])

        v1_events = [
            event("CLAIM", "2026-08-24T13:00:00+08:00", claim_id="c1", schema=rs.EVENT_SCHEMA_V1),
            event("DONE", "2026-08-24T13:05:00+08:00", claim_id="c1", schema=rs.EVENT_SCHEMA_V1, progress_ref="legacy"),
        ]
        state = rs.reduce_task(
            task(), v1_events, default_lease_minutes=30,
            now=self.now("2026-08-24T13:06:00+08:00"),
        )
        self.assertEqual("DONE", state["state"])

    def test_orphan_is_never_auto_selected(self):
        chosen = rs.select_task(
            cfg(task("RS-O", state="ORPHANED"), task("RS-R", owner="owner/b")),
            [], self.now("2026-08-24T14:00:00+08:00"), taskbook_dir=None,
        )
        self.assertEqual("RS-R", chosen["task_id"])

    def test_invalid_taskbook_is_still_registered_as_synthetic_orphan(self):
        with tempfile.TemporaryDirectory() as td:
            directory = pathlib.Path(td)
            (directory / "broken.md").write_text("# missing machine task metadata", encoding="utf-8")
            items, diagnostics = rs.materialize_tasks(cfg(), [], taskbook_dir=directory)
            self.assertEqual(1, len(items))
            self.assertTrue(items[0]["task_id"].startswith("ORPHAN-FILE-"))
            self.assertEqual("ORPHANED", items[0]["base_state"])
            self.assertTrue(diagnostics)


if __name__ == "__main__":
    unittest.main()
