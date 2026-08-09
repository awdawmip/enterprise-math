import copy
import json
import pathlib
import unittest
from datetime import datetime, timezone

from tools import research_scheduler as rs

ROOT = pathlib.Path(__file__).resolve().parents[1]


def base_policy():
    return {
        "priority_order": ["P0", "P1", "P2", "P3"],
        "leverage_order": ["HIGH", "MEDIUM", "LOW"],
        "state_order": ["HANDOFF_READY", "READY"],
    }


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
        "last_progress_at": "2026-08-09T10:00:00+08:00",
        "hard_block": None,
    }


def config(*tasks):
    return {
        "schema": "ENTERPRISE_MATH_RESEARCH_SCHEDULER_V1",
        "claim_lease_minutes": 30,
        "task_states": ["BACKLOG", "READY", "CLAIMED", "IN_PROGRESS", "HANDOFF_READY", "BLOCKED", "DONE", "SUPERSEDED"],
        "event_types": ["CLAIM", "HEARTBEAT", "PROGRESS", "HANDOFF", "HARD_BLOCK", "UNBLOCK", "DONE", "SUPERSEDE"],
        "selection_policy": base_policy(),
        "tasks": list(tasks),
    }


def owners(*names):
    return {
        "branches": {
            name: {"state": "ACTIVE_OWNER"}
            for name in names
        }
    }


def event(kind, at, *, task_id="RS-T1", claim_id="c1", **extra):
    value = {
        "schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V1",
        "event": kind,
        "task_id": task_id,
        "actor": "test",
        "at": at,
    }
    if claim_id is not None:
        value["claim_id"] = claim_id
    value.update(extra)
    return value


class SchedulerValidationTests(unittest.TestCase):
    def test_repository_scheduler_covers_every_active_owner(self):
        cfg = json.loads((ROOT / "research_scheduler.json").read_text(encoding="utf-8"))
        own = json.loads((ROOT / "branch_governance_overrides.json").read_text(encoding="utf-8"))
        self.assertEqual([], rs.validate_scheduler(cfg, own))

    def test_unknown_research_owner_fails_validation(self):
        cfg = config(task(owner="missing"))
        errors = rs.validate_scheduler(cfg, owners("owner/a"))
        self.assertTrue(any("not ACTIVE_OWNER" in error for error in errors))
        self.assertTrue(any("missing scheduler coverage" in error for error in errors))

    def test_partial_static_hard_block_is_invalid(self):
        item = task()
        item["hard_block"] = {"missing_object": "lemma"}
        errors = rs.validate_scheduler(config(item), owners("owner/a"))
        self.assertTrue(any("partial hard_block" in error for error in errors))


class SchedulerReducerTests(unittest.TestCase):
    def now(self, value):
        return rs.parse_time(value)

    def test_expired_claim_returns_to_handoff_ready(self):
        item = task()
        events = [event("CLAIM", "2026-08-09T12:00:00+08:00", lease_minutes=30)]
        state = rs.reduce_task(item, events, default_lease_minutes=30, now=self.now("2026-08-09T12:31:00+08:00"))
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        self.assertIsNone(state["claim_id"])

    def test_heartbeat_renews_live_claim(self):
        item = task()
        events = [
            event("CLAIM", "2026-08-09T12:00:00+08:00", lease_minutes=30),
            event("HEARTBEAT", "2026-08-09T12:20:00+08:00", lease_minutes=30),
        ]
        state = rs.reduce_task(item, events, default_lease_minutes=30, now=self.now("2026-08-09T12:40:00+08:00"))
        self.assertEqual("CLAIMED", state["state"])
        self.assertEqual("LEASED", state["dispatch_state"])
        self.assertEqual("c1", state["claim_id"])

    def test_progress_renews_and_updates_frontier_pointer(self):
        item = task()
        events = [
            event("CLAIM", "2026-08-09T12:00:00+08:00"),
            event(
                "PROGRESS",
                "2026-08-09T12:10:00+08:00",
                progress_ref="commit:abc",
                next_action="prove lemma B",
            ),
        ]
        state = rs.reduce_task(item, events, default_lease_minutes=30, now=self.now("2026-08-09T12:20:00+08:00"))
        self.assertEqual("IN_PROGRESS", state["state"])
        self.assertEqual("commit:abc", state["last_progress_ref"])
        self.assertEqual("prove lemma B", state["next_action"])

    def test_handoff_releases_claim_with_concrete_next_action(self):
        item = task()
        events = [
            event("CLAIM", "2026-08-09T12:00:00+08:00"),
            event(
                "HANDOFF",
                "2026-08-09T12:10:00+08:00",
                progress_ref="PR #999",
                next_action="continue exact boundary proof",
            ),
        ]
        state = rs.reduce_task(item, events, default_lease_minutes=30, now=self.now("2026-08-09T12:11:00+08:00"))
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        self.assertEqual("continue exact boundary proof", state["next_action"])
        self.assertIsNone(state["claim_id"])

    def test_incomplete_runtime_hard_block_is_ignored(self):
        item = task()
        events = [
            event("CLAIM", "2026-08-09T12:00:00+08:00"),
            event("HARD_BLOCK", "2026-08-09T12:05:00+08:00", hard_block={"missing_object": "lemma"}),
        ]
        state = rs.reduce_task(item, events, default_lease_minutes=30, now=self.now("2026-08-09T12:10:00+08:00"))
        self.assertEqual("CLAIMED", state["state"])
        self.assertEqual("LEASED", state["dispatch_state"])
        self.assertTrue(state["ignored_events"])

    def test_complete_runtime_hard_block_stops_task(self):
        item = task()
        hard_block = {
            "missing_object": "exact lemma X",
            "owner": "owner/b",
            "necessity": "every declared frontier needs X and no conditional/counterexample route remains",
            "unblock_condition": "lemma X proved or disproved",
        }
        events = [
            event("CLAIM", "2026-08-09T12:00:00+08:00"),
            event("HARD_BLOCK", "2026-08-09T12:05:00+08:00", hard_block=hard_block),
        ]
        state = rs.reduce_task(item, events, default_lease_minutes=30, now=self.now("2026-08-09T12:10:00+08:00"))
        self.assertEqual("BLOCKED", state["state"])
        self.assertEqual("BLOCKED", state["dispatch_state"])

    def test_second_claim_cannot_preempt_live_lease(self):
        item = task()
        events = [
            event("CLAIM", "2026-08-09T12:00:00+08:00", claim_id="c1"),
            event("CLAIM", "2026-08-09T12:01:00+08:00", claim_id="c2"),
        ]
        state = rs.reduce_task(item, events, default_lease_minutes=30, now=self.now("2026-08-09T12:05:00+08:00"))
        self.assertEqual("c1", state["claim_id"])
        self.assertEqual(1, len(state["ignored_events"]))

    def test_done_task_is_not_dispatchable(self):
        item = task()
        events = [
            event("CLAIM", "2026-08-09T12:00:00+08:00"),
            event("DONE", "2026-08-09T12:05:00+08:00", progress_ref="merge:abc"),
        ]
        state = rs.reduce_task(item, events, default_lease_minutes=30, now=self.now("2026-08-09T13:00:00+08:00"))
        self.assertEqual("DONE", state["state"])
        self.assertEqual("COMPLETE", state["dispatch_state"])


class SchedulerSelectionTests(unittest.TestCase):
    def test_handoff_ready_precedes_fresh_ready_even_at_lower_priority(self):
        handoff = task("RS-H", state="HANDOFF_READY", priority="P2", leverage="LOW")
        ready = task("RS-R", owner="owner/b", state="READY", priority="P0", leverage="HIGH")
        cfg = config(handoff, ready)
        chosen = rs.select_task(cfg, [], rs.parse_time("2026-08-09T13:00:00+08:00"))
        self.assertEqual("RS-H", chosen["task_id"])

    def test_priority_then_leverage_then_oldest_progress_is_deterministic(self):
        a = task("RS-A", priority="P1", leverage="HIGH")
        b = task("RS-B", owner="owner/b", priority="P1", leverage="HIGH")
        a["last_progress_at"] = "2026-08-09T11:00:00+08:00"
        b["last_progress_at"] = "2026-08-09T10:00:00+08:00"
        chosen = rs.select_task(config(a, b), [], rs.parse_time("2026-08-09T13:00:00+08:00"))
        self.assertEqual("RS-B", chosen["task_id"])

    def test_non_hard_dependency_never_blocks_selection(self):
        item = task()
        item["dependencies"] = [{"target": "useful theorem", "action": "TEST", "satisfied": False}]
        chosen = rs.select_task(config(item), [], rs.parse_time("2026-08-09T13:00:00+08:00"))
        self.assertEqual("RS-T1", chosen["task_id"])


if __name__ == "__main__":
    unittest.main()
