import pathlib
import unittest

from tools import research_work_state as ws

ROOT = pathlib.Path(__file__).resolve().parents[1]


def machine():
    return {
        "schema": "ENTERPRISE_MATH_WORK_STATE_MACHINE_V1",
        "board": {"issue": 240},
        "task_publication": {
            "required_event_fields": ["at", "issuer_driver_id", "taskbook_ref", "task"],
            "required_task_fields": [
                "task_id", "title", "kind", "owner", "base_state", "priority",
                "leverage", "frontier", "next_action", "source_refs",
                "last_progress_at", "hard_block"
            ],
        },
        "task_claim": {
            "task_id_required_from_user": False,
            "legacy_unpublished_ready_auto_claim": False,
        },
        "research_completion": {
            "review_request_required_for_new_published_tasks": True,
        },
        "review": {
            "issuer_lock": False,
            "prefer_reviewer_different_from_issuer": True,
            "claim_lease_minutes": 30,
            "events": [
                "REVIEW_REQUEST", "REVIEW_CLAIM", "REVIEW_PROGRESS",
                "REVIEW_HANDOFF", "REVIEW_DONE", "REVIEW_SUPERSEDE",
            ],
            "required_review_request_fields": [
                "review_id", "task_id", "originating_researcher_id",
                "review_objective", "target_refs", "evidence_refs",
                "execution_log_refs", "requested_checks", "priority",
            ],
            "review_done_verdicts": [
                "ACCEPT", "ACCEPT_WITH_NARROWING", "RETURN_TO_RESEARCH",
                "REQUEST_INDEPENDENT_REPLICATION", "ROUTE_TO_FOUNDATION",
                "PROMOTION_READY", "PARK", "REJECT",
            ],
            "review_done_required_fields": [
                "review_id", "reviewer_driver_id", "verdict", "findings",
                "evidence_refs", "next_action", "method_harvest",
                "successor_disposition",
            ],
        },
    }


def legacy_task(task_id="RS-OLD", *, state="READY", priority="P2"):
    return {
        "task_id": task_id,
        "title": task_id,
        "kind": "RESEARCH",
        "owner": "owner/a",
        "base_state": state,
        "priority": priority,
        "leverage": "HIGH",
        "frontier": "old frontier",
        "next_action": "old next",
        "dependencies": [],
        "source_refs": [],
        "last_progress_ref": "seed",
        "last_progress_at": "2026-08-20T10:00:00+08:00",
        "hard_block": None,
    }


def legacy_config(*tasks):
    return {
        "schema": "ENTERPRISE_MATH_RESEARCH_SCHEDULER_V1",
        "claim_lease_minutes": 30,
        "task_states": [
            "BACKLOG", "READY", "CLAIMED", "IN_PROGRESS",
            "HANDOFF_READY", "BLOCKED", "DONE", "SUPERSEDED",
        ],
        "event_types": [
            "CLAIM", "HEARTBEAT", "PROGRESS", "HANDOFF",
            "HARD_BLOCK", "UNBLOCK", "DONE", "SUPERSEDE",
        ],
        "selection_policy": {
            "state_order": ["HANDOFF_READY", "READY"],
            "priority_order": ["P0", "P1", "P2", "P3"],
            "leverage_order": ["HIGH", "MEDIUM", "LOW"],
        },
        "tasks": list(tasks),
    }


def publish_event(
    task_id="RS-NEW",
    *,
    issuer="EM-DVR-ISSUER",
    priority="P0",
    at="2026-08-24T09:01:00+08:00",
    ref_suffix="abcdef123456",
):
    task = legacy_task(task_id, state="READY", priority=priority)
    task["last_progress_at"] = "2026-08-24T09:00:00+08:00"
    return {
        "schema": ws.WORK_SCHEMA,
        "event": "TASK_PUBLISH",
        "at": at,
        "issuer_driver_id": issuer,
        "taskbook_ref": f"research_tasks/{task_id}.md@{ref_suffix}",
        "task": task,
    }


def review_request(review_id, task_id, *, issuer, priority="P1", at="2026-08-24T09:10:00+08:00"):
    return {
        "schema": ws.WORK_SCHEMA,
        "event": "REVIEW_REQUEST",
        "review_id": review_id,
        "task_id": task_id,
        "at": at,
        "originating_researcher_id": "EM-RTEST-ABC123",
        "issuer_driver_id": issuer,
        "review_objective": "verify exact return and route it",
        "target_refs": ["PR #1", "commit:abc"],
        "evidence_refs": ["report.md@abc"],
        "execution_log_refs": ["Issue #240 task log"],
        "requested_checks": ["scope", "counterexample", "method_harvest"],
        "priority": priority,
    }


class WorkMachineTests(unittest.TestCase):
    def test_repository_machine_contract(self):
        cfg = ws.load_json(ROOT / "research_work_state_machine.json")
        self.assertEqual([], ws.validate_machine(cfg))

    def test_task_publish_overlays_legacy_and_becomes_selectable(self):
        cfg = legacy_config(legacy_task())
        events = [publish_event("RS-NEW", priority="P0")]
        composed = ws.composed_scheduler(cfg, events, machine())
        ids = [t["task_id"] for t in composed["tasks"]]
        self.assertIn("RS-NEW", ids)
        chosen = ws.select_task(
            cfg, events, machine(), ws.parse_time("2026-08-24T09:05:00+08:00")
        )
        self.assertEqual("RS-NEW", chosen["task_id"])
        self.assertEqual("research_tasks/RS-NEW.md@abcdef123456", chosen["taskbook_ref"])
        self.assertEqual("EM-DVR-ISSUER", chosen["issuer_driver_id"])
        self.assertTrue(chosen["review_required"])

    def test_noncommit_taskbook_ref_is_rejected(self):
        event = publish_event("RS-BAD", ref_suffix="branch-name")
        self.assertTrue(ws.validate_task_publish(event, machine()))

    def test_unpublished_legacy_ready_is_not_selected_by_generic_claim(self):
        cfg = legacy_config(legacy_task("RS-STALE", state="READY", priority="P0"))
        chosen = ws.select_task(
            cfg, [], machine(), ws.parse_time("2026-08-24T09:05:00+08:00")
        )
        self.assertIsNone(chosen)

    def test_invalid_runtime_event_does_not_make_legacy_ready_claimable(self):
        cfg = legacy_config(legacy_task("RS-STALE", state="READY", priority="P0"))
        events = [
            {
                "schema": ws.LEGACY_SCHEMA,
                "event": "CLAIM",
                "task_id": "RS-STALE",
                "actor": "broken",
                "at": "2026-08-24T08:00:00+08:00"
            }
        ]
        chosen = ws.select_task(
            cfg, events, machine(), ws.parse_time("2026-08-24T09:05:00+08:00")
        )
        self.assertIsNone(chosen)

    def test_runtime_touched_legacy_handoff_remains_claimable(self):
        cfg = legacy_config(legacy_task("RS-LIVE", state="READY", priority="P1"))
        events = [
            {
                "schema": ws.LEGACY_SCHEMA,
                "event": "CLAIM",
                "task_id": "RS-LIVE",
                "actor": "old researcher",
                "at": "2026-08-24T08:00:00+08:00",
                "claim_id": "old-claim",
                "lease_minutes": 30,
            },
            {
                "schema": ws.LEGACY_SCHEMA,
                "event": "HANDOFF",
                "task_id": "RS-LIVE",
                "actor": "old researcher",
                "at": "2026-08-24T08:10:00+08:00",
                "claim_id": "old-claim",
                "progress_ref": "checkpoint:1",
                "next_action": "continue exact proof",
            },
        ]
        chosen = ws.select_task(
            cfg, events, machine(), ws.parse_time("2026-08-24T09:05:00+08:00")
        )
        self.assertEqual("RS-LIVE", chosen["task_id"])
        self.assertEqual("HANDOFF_READY", chosen["state"])

    def test_task_publish_can_refresh_same_id_without_duplicate(self):
        cfg = legacy_config(legacy_task("RS-X", priority="P3"))
        event = publish_event("RS-X", priority="P0")
        composed = ws.composed_scheduler(cfg, [event], machine())
        matching = [t for t in composed["tasks"] if t["task_id"] == "RS-X"]
        self.assertEqual(1, len(matching))
        self.assertEqual("P0", matching[0]["priority"])

    def test_republish_starts_new_generation_after_old_supersede(self):
        cfg = legacy_config(legacy_task("RS-X", priority="P1"))
        events = [
            {
                "schema": ws.LEGACY_SCHEMA,
                "event": "SUPERSEDE",
                "task_id": "RS-X",
                "actor": "old driver",
                "at": "2026-08-24T08:00:00+08:00",
            },
            publish_event(
                "RS-X",
                issuer="EM-DVR-NEW",
                priority="P0",
                at="2026-08-24T09:01:00+08:00",
                ref_suffix="1234abc5678",
            ),
        ]
        chosen = ws.select_task(
            cfg, events, machine(), ws.parse_time("2026-08-24T09:05:00+08:00")
        )
        self.assertEqual("RS-X", chosen["task_id"])
        self.assertEqual("READY", chosen["state"])
        self.assertEqual("EM-DVR-NEW", chosen["issuer_driver_id"])
        self.assertTrue(chosen["taskbook_ref"].endswith("@1234abc5678"))

    def test_work_schema_runtime_event_is_legacy_compatible(self):
        raw = {
            "schema": ws.WORK_SCHEMA,
            "event": "SUPERSEDE",
            "task_id": "RS-OLD",
            "at": "2026-08-24T09:02:00+08:00",
            "actor": "driver",
        }
        normalized = ws.normalized_task_events([raw])
        self.assertEqual(ws.LEGACY_SCHEMA, normalized[0]["schema"])
        self.assertEqual("SUPERSEDE", normalized[0]["event"])

    def test_cross_review_prefers_driver_other_than_issuer_when_priority_equal(self):
        events = [
            review_request(
                "RVW-SAME", "RS-A", issuer="EM-DVR-ME",
                at="2026-08-24T09:00:00+08:00",
            ),
            review_request(
                "RVW-CROSS", "RS-B", issuer="EM-DVR-OTHER",
                at="2026-08-24T09:01:00+08:00",
            ),
        ]
        chosen = ws.select_review(
            events, machine(), ws.parse_time("2026-08-24T09:20:00+08:00"),
            driver_id="EM-DVR-ME",
        )
        self.assertEqual("RVW-CROSS", chosen["review_id"])

    def test_higher_priority_same_issuer_beats_lower_priority_cross_issuer(self):
        events = [
            review_request(
                "RVW-P0-SAME", "RS-A", issuer="EM-DVR-ME", priority="P0",
                at="2026-08-24T09:00:00+08:00",
            ),
            review_request(
                "RVW-P1-CROSS", "RS-B", issuer="EM-DVR-OTHER", priority="P1",
                at="2026-08-24T08:00:00+08:00",
            ),
        ]
        chosen = ws.select_review(
            events, machine(), ws.parse_time("2026-08-24T09:20:00+08:00"),
            driver_id="EM-DVR-ME",
        )
        self.assertEqual("RVW-P0-SAME", chosen["review_id"])

    def test_same_driver_review_is_allowed_when_it_is_the_only_item(self):
        events = [review_request("RVW-ONLY", "RS-A", issuer="EM-DVR-ME")]
        chosen = ws.select_review(
            events, machine(), ws.parse_time("2026-08-24T09:20:00+08:00"),
            driver_id="EM-DVR-ME",
        )
        self.assertEqual("RVW-ONLY", chosen["review_id"])

    def test_review_claim_lease_and_cross_driver_done(self):
        events = [
            review_request("RVW-1", "RS-A", issuer="EM-DVR-ISSUER"),
            {
                "schema": ws.WORK_SCHEMA,
                "event": "REVIEW_CLAIM",
                "review_id": "RVW-1",
                "at": "2026-08-24T09:11:00+08:00",
                "claim_id": "review-claim-1",
                "reviewer_driver_id": "EM-DVR-REVIEWER",
                "lease_minutes": 30,
            },
            {
                "schema": ws.WORK_SCHEMA,
                "event": "REVIEW_DONE",
                "review_id": "RVW-1",
                "at": "2026-08-24T09:15:00+08:00",
                "claim_id": "review-claim-1",
                "reviewer_driver_id": "EM-DVR-REVIEWER",
                "verdict": "ACCEPT",
                "findings": ["scope exact", "no counterexample"],
                "evidence_refs": ["review.md@def"],
                "next_action": "close local task",
                "method_harvest": {"classification": "RESULT_ONLY"},
                "successor_disposition": {"action": "CLOSE"},
            },
        ]
        states = ws.reduce_reviews(
            events, machine(), ws.parse_time("2026-08-24T09:20:00+08:00")
        )
        state = states[0]
        self.assertEqual("DONE", state["state"])
        self.assertEqual("COMPLETE", state["dispatch_state"])
        self.assertEqual("ACCEPT", state["verdict"])
        self.assertFalse(state["same_driver_review"])

    def test_expired_review_claim_returns_to_handoff_ready(self):
        events = [
            review_request("RVW-1", "RS-A", issuer="EM-DVR-ISSUER"),
            {
                "schema": ws.WORK_SCHEMA,
                "event": "REVIEW_CLAIM",
                "review_id": "RVW-1",
                "at": "2026-08-24T09:11:00+08:00",
                "claim_id": "review-claim-1",
                "reviewer_driver_id": "EM-DVR-REVIEWER",
                "lease_minutes": 30,
            },
        ]
        state = ws.reduce_reviews(
            events, machine(), ws.parse_time("2026-08-24T09:42:00+08:00")
        )[0]
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("NEEDS_REVIEW", state["dispatch_state"])


if __name__ == "__main__":
    unittest.main()
