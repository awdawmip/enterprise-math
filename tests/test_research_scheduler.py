import json
import pathlib
import tempfile
import unittest

from tools import research_scheduler as rs

ROOT = pathlib.Path(__file__).resolve().parents[1]


def base_policy():
    return {
        "priority_order": ["P0", "P1", "P2", "P3"],
        "leverage_order": ["HIGH", "MEDIUM", "LOW"],
        "state_order": ["HANDOFF_READY", "CHANGES_REQUESTED", "READY"],
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
        "evidence_status": "TEST",
        "last_progress_ref": "seed",
        "last_progress_at": "2026-08-25T00:00:00+08:00",
        "hard_block": None,
        "tags": [],
    }


def config(*tasks):
    return {
        "schema": rs.V2_SCHEMA,
        "claim_lease_minutes": 30,
        "task_states": [
            "BACKLOG", "PUBLISHED", "READY", "CLAIMED", "IN_PROGRESS",
            "RETURNED", "CHANGES_REQUESTED", "HANDOFF_READY", "ORPHANED",
            "BLOCKED", "DONE", "REJECTED", "SUPERSEDED",
        ],
        "event_types": [
            "PUBLISH", "REVIEW", "CLAIM", "HEARTBEAT", "PROGRESS",
            "HANDOFF", "RETURN", "HARD_BLOCK", "UNBLOCK", "ORPHAN",
            "RECOVER", "SUPERSEDE",
        ],
        "selection_policy": base_policy(),
        "publish_contract": {
            "allowed_publisher_roles": ["RESEARCHER", "RESEARCH_DRIVER", "STEWARD", "USER"],
            "publisher_id_required_for_roles": ["RESEARCHER", "RESEARCH_DRIVER", "STEWARD"],
            "required_task_fields": ["title", "kind", "owner", "priority", "leverage", "frontier", "next_action"],
        },
        "registry_integrity": {
            "taskbook_directory": "research_tasks",
            "must_be_registered_taskbook_states": [
                "READY", "CLAIMED", "IN_PROGRESS", "RETURNED",
                "CHANGES_REQUESTED", "HANDOFF_READY", "ORPHANED", "BLOCKED",
            ],
        },
        "tasks": list(tasks),
    }


def owners(*names):
    return {"branches": {name: {"state": "ACTIVE_OWNER"} for name in names}}


def event(kind, at, *, task_id="RS-T1", claim_id="c1", schema=rs.V2_EVENT_SCHEMA, **extra):
    value = {
        "schema": schema,
        "event": kind,
        "task_id": task_id,
        "actor": "test",
        "at": at,
    }
    if claim_id is not None:
        value["claim_id"] = claim_id
    value.update(extra)
    return value


def publish_event(*, task_id="RS-PUB", role="RESEARCHER", publisher_id="EM-FREE-AB12", owner="owner/a", **extra):
    value = event(
        "PUBLISH",
        "2026-08-25T01:00:00+08:00",
        task_id=task_id,
        claim_id=None,
        publisher_role=role,
        publisher_id=publisher_id,
        task={
            "title": "published task",
            "kind": "RESEARCH",
            "owner": owner,
            "priority": "P1",
            "leverage": "HIGH",
            "frontier": "new frontier",
            "next_action": "prove or refute",
            "dependencies": [],
            "source_refs": [],
            "tags": [],
        },
    )
    value.update(extra)
    return value


def dispatch_review(*, task_id="RS-PUB", reviewer="EM-DVR-Z9K8", verdict="ACCEPT", **extra):
    value = event(
        "REVIEW",
        "2026-08-25T01:05:00+08:00",
        task_id=task_id,
        claim_id=None,
        review_stage="DISPATCH",
        verdict=verdict,
        reviewer_id=reviewer,
        review_ref="driver_reviews/test.md",
    )
    value.update(extra)
    return value


class SchedulerValidationTests(unittest.TestCase):
    def test_repository_v2_scheduler_covers_every_active_owner(self):
        cfg = rs.load_scheduler_bundle(ROOT / "research_scheduler_v2.json")
        own = json.loads((ROOT / "branch_governance_overrides.json").read_text(encoding="utf-8"))
        self.assertEqual([], rs.validate_scheduler(cfg, own))

    def test_r043c4_is_migrated_into_registry(self):
        cfg = rs.load_scheduler_bundle(ROOT / "research_scheduler_v2.json")
        ids = {item["task_id"] for item in cfg["tasks"]}
        self.assertIn("RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE", ids)

    def test_unknown_research_owner_fails_static_validation(self):
        cfg = config(task(owner="missing"))
        errors = rs.validate_scheduler(cfg, owners("owner/a"))
        self.assertTrue(any("not ACTIVE_OWNER" in error for error in errors))

    def test_partial_static_hard_block_is_invalid(self):
        item = task()
        item["hard_block"] = {"missing_object": "lemma"}
        errors = rs.validate_scheduler(config(item), owners("owner/a"))
        self.assertTrue(any("partial hard_block" in error for error in errors))


class SchedulerPublishReviewTests(unittest.TestCase):
    def now(self, value="2026-08-25T02:00:00+08:00"):
        return rs.parse_time(value)

    def test_researcher_can_publish_but_task_needs_review(self):
        states, issues = rs.effective_states(config(task()), [publish_event()], self.now())
        self.assertEqual([], issues)
        published = next(state for state in states if state["task_id"] == "RS-PUB")
        self.assertEqual("PUBLISHED", published["state"])
        self.assertEqual("NEEDS_REVIEW", published["dispatch_state"])
        self.assertEqual("EM-FREE-AB12", published["publisher_id"])

    def test_driver_can_publish_but_cannot_self_review_dispatch(self):
        pub = publish_event(role="RESEARCH_DRIVER", publisher_id="EM-DVR-Z9K8")
        states, _ = rs.effective_states(config(task()), [pub, dispatch_review(reviewer="EM-DVR-Z9K8")], self.now())
        published = next(state for state in states if state["task_id"] == "RS-PUB")
        self.assertEqual("PUBLISHED", published["state"])
        self.assertTrue(any("independent" in item["reason"] for item in published["ignored_events"]))

    def test_independent_driver_review_makes_publication_ready(self):
        pub = publish_event()
        states, _ = rs.effective_states(config(task()), [pub, dispatch_review()], self.now())
        published = next(state for state in states if state["task_id"] == "RS-PUB")
        self.assertEqual("READY", published["state"])
        self.assertEqual("NEEDS_DISPATCH", published["dispatch_state"])
        self.assertEqual("EM-DVR-Z9K8", published["dispatch_reviewer_id"])

    def test_unreviewed_publication_cannot_be_claimed(self):
        events = [publish_event(), event("CLAIM", "2026-08-25T01:06:00+08:00", task_id="RS-PUB")]
        states, _ = rs.effective_states(config(task()), events, self.now())
        published = next(state for state in states if state["task_id"] == "RS-PUB")
        self.assertEqual("PUBLISHED", published["state"])
        self.assertIsNone(published["claim_id"])

    def test_dispatch_review_can_assign_real_owner(self):
        pub = publish_event(owner="taskbook/unassigned")
        review = dispatch_review(task_patch={"owner": "owner/a", "frontier": "reviewed frontier"})
        states, _ = rs.effective_states(config(task()), [pub, review], self.now())
        published = next(state for state in states if state["task_id"] == "RS-PUB")
        self.assertEqual("READY", published["state"])
        self.assertEqual("owner/a", published["owner"])
        self.assertEqual("reviewed frontier", published["frontier"])

    def test_duplicate_publish_is_reported(self):
        _, issues = rs.effective_states(config(task()), [publish_event(), publish_event()], self.now())
        self.assertEqual(1, len(issues))
        self.assertIn("duplicate", issues[0]["reason"])


class SchedulerExecutionTests(unittest.TestCase):
    def now(self, value):
        return rs.parse_time(value)

    def test_expired_claim_becomes_persistent_orphan(self):
        events = [event("CLAIM", "2026-08-25T01:00:00+08:00", lease_minutes=30)]
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=self.now("2026-08-25T01:31:00+08:00"))
        self.assertEqual("ORPHANED", state["state"])
        self.assertEqual("ORPHANED", state["dispatch_state"])
        self.assertEqual(1, len(state["orphan_history"]))
        record = state["orphan_history"][0]
        self.assertEqual("LEASE_EXPIRED", record["reason"])
        self.assertEqual("c1", record["claim_id"])
        self.assertIsNotNone(record["researcher_id"])

    def test_expired_claim_is_not_auto_dispatchable(self):
        events = [event("CLAIM", "2026-08-25T01:00:00+08:00", lease_minutes=30)]
        chosen = rs.select_task(config(task()), events, self.now("2026-08-25T01:31:00+08:00"))
        self.assertIsNone(chosen)

    def test_driver_recovers_orphan_to_handoff_ready(self):
        events = [
            event("CLAIM", "2026-08-25T01:00:00+08:00", lease_minutes=30),
            event(
                "RECOVER",
                "2026-08-25T01:40:00+08:00",
                claim_id=None,
                driver_id="EM-DVR-Z9K8",
                review_ref="driver_reviews/recovery.md",
                next_action="resume exact proof",
            ),
        ]
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=self.now("2026-08-25T01:41:00+08:00"))
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("resume exact proof", state["next_action"])
        self.assertEqual(1, len(state["orphan_history"]))

    def test_explicit_orphan_records_branch_and_commit(self):
        events = [
            event(
                "ORPHAN",
                "2026-08-25T01:10:00+08:00",
                claim_id=None,
                orphan_reason="UNREGISTERED_HISTORICAL_BRANCH",
                discovered_by="EM-DVR-Z9K8",
                source_ref="PR #999",
                driver_id="EM-DVR-Z9K8",
                branch="research/old",
                last_commit="abc123",
            )
        ]
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=self.now("2026-08-25T01:20:00+08:00"))
        self.assertEqual("ORPHANED", state["state"])
        self.assertEqual("research/old", state["orphan_history"][0]["branch"])
        self.assertEqual("abc123", state["orphan_history"][0]["last_commit"])

    def test_heartbeat_renews_live_claim(self):
        events = [
            event("CLAIM", "2026-08-25T01:00:00+08:00", lease_minutes=30),
            event("HEARTBEAT", "2026-08-25T01:20:00+08:00", lease_minutes=30),
        ]
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=self.now("2026-08-25T01:40:00+08:00"))
        self.assertEqual("CLAIMED", state["state"])
        self.assertEqual("LEASED", state["dispatch_state"])

    def test_progress_updates_frontier_pointer(self):
        events = [
            event("CLAIM", "2026-08-25T01:00:00+08:00"),
            event("PROGRESS", "2026-08-25T01:10:00+08:00", progress_ref="commit:abc", next_action="prove B"),
        ]
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=self.now("2026-08-25T01:20:00+08:00"))
        self.assertEqual("IN_PROGRESS", state["state"])
        self.assertEqual("commit:abc", state["last_progress_ref"])
        self.assertEqual("prove B", state["next_action"])

    def test_handoff_releases_claim(self):
        events = [
            event("CLAIM", "2026-08-25T01:00:00+08:00"),
            event("HANDOFF", "2026-08-25T01:10:00+08:00", progress_ref="PR #999", next_action="continue proof"),
        ]
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=self.now("2026-08-25T01:11:00+08:00"))
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertIsNone(state["claim_id"])

    def test_return_requires_driver_review_before_done(self):
        events = [
            event("CLAIM", "2026-08-25T01:00:00+08:00"),
            event("RETURN", "2026-08-25T01:10:00+08:00", return_ref="research_returns/T1.md"),
        ]
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=self.now("2026-08-25T01:20:00+08:00"))
        self.assertEqual("RETURNED", state["state"])
        self.assertEqual("NEEDS_REVIEW", state["dispatch_state"])
        self.assertIsNone(state["claim_id"])

    def test_v2_worker_done_is_ignored(self):
        events = [
            event("CLAIM", "2026-08-25T01:00:00+08:00"),
            event("DONE", "2026-08-25T01:10:00+08:00", progress_ref="bad"),
        ]
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=self.now("2026-08-25T01:20:00+08:00"))
        self.assertEqual("CLAIMED", state["state"])
        self.assertTrue(any("forbids worker DONE" in item["reason"] for item in state["ignored_events"]))

    def test_independent_return_review_accepts_to_done(self):
        events = [
            event("CLAIM", "2026-08-25T01:00:00+08:00", researcher_id="EM-R043-AB12"),
            event("RETURN", "2026-08-25T01:10:00+08:00", researcher_id="EM-R043-AB12", return_ref="research_returns/T1.md"),
            event(
                "REVIEW",
                "2026-08-25T01:20:00+08:00",
                claim_id=None,
                review_stage="RETURN",
                verdict="ACCEPT",
                reviewer_id="EM-DVR-Z9K8",
                review_ref="driver_reviews/T1.md",
            ),
        ]
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=self.now("2026-08-25T01:21:00+08:00"))
        self.assertEqual("DONE", state["state"])
        self.assertEqual("COMPLETE", state["dispatch_state"])

    def test_return_changes_requested_is_dispatchable(self):
        events = [
            event("CLAIM", "2026-08-25T01:00:00+08:00"),
            event("RETURN", "2026-08-25T01:10:00+08:00", return_ref="research_returns/T1.md"),
            event(
                "REVIEW",
                "2026-08-25T01:20:00+08:00",
                claim_id=None,
                review_stage="RETURN",
                verdict="CHANGES_REQUESTED",
                reviewer_id="EM-DVR-Z9K8",
                review_ref="driver_reviews/T1.md",
                next_action="repair exact witness",
            ),
        ]
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=self.now("2026-08-25T01:21:00+08:00"))
        self.assertEqual("CHANGES_REQUESTED", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])

    def test_complete_runtime_hard_block_stops_task(self):
        hard_block = {
            "missing_object": "exact lemma X",
            "owner": "owner/b",
            "necessity": "all independent routes require X",
            "unblock_condition": "X proved or disproved",
        }
        events = [
            event("CLAIM", "2026-08-25T01:00:00+08:00"),
            event("HARD_BLOCK", "2026-08-25T01:05:00+08:00", hard_block=hard_block),
        ]
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=self.now("2026-08-25T01:10:00+08:00"))
        self.assertEqual("BLOCKED", state["state"])

    def test_second_claim_cannot_preempt_live_lease(self):
        events = [
            event("CLAIM", "2026-08-25T01:00:00+08:00", claim_id="c1"),
            event("CLAIM", "2026-08-25T01:01:00+08:00", claim_id="c2"),
        ]
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=self.now("2026-08-25T01:05:00+08:00"))
        self.assertEqual("c1", state["claim_id"])

    def test_legacy_v1_done_remains_compatible(self):
        events = [
            event("CLAIM", "2026-08-25T01:00:00+08:00", schema=rs.V1_EVENT_SCHEMA),
            event("DONE", "2026-08-25T01:05:00+08:00", schema=rs.V1_EVENT_SCHEMA, progress_ref="legacy"),
        ]
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=self.now("2026-08-25T01:10:00+08:00"))
        self.assertEqual("DONE", state["state"])
        self.assertEqual("LEGACY_V1_DONE", state["review_history"][0]["stage"])


class SchedulerSelectionTests(unittest.TestCase):
    def test_handoff_ready_precedes_fresh_ready(self):
        handoff = task("RS-H", state="HANDOFF_READY", priority="P2", leverage="LOW")
        ready = task("RS-R", owner="owner/b", state="READY", priority="P0", leverage="HIGH")
        chosen = rs.select_task(config(handoff, ready), [], rs.parse_time("2026-08-25T02:00:00+08:00"))
        self.assertEqual("RS-H", chosen["task_id"])

    def test_changes_requested_precedes_fresh_ready(self):
        repair = task("RS-C", state="CHANGES_REQUESTED", priority="P2", leverage="LOW")
        ready = task("RS-R", owner="owner/b", state="READY", priority="P0", leverage="HIGH")
        chosen = rs.select_task(config(repair, ready), [], rs.parse_time("2026-08-25T02:00:00+08:00"))
        self.assertEqual("RS-C", chosen["task_id"])


class SchedulerRegistryIntegrityTests(unittest.TestCase):
    def _write_taskbook(self, root, task_id, state):
        directory = root / "research_tasks"
        directory.mkdir(parents=True, exist_ok=True)
        meta = {"task_id": task_id, "base_state": state}
        text = rs.TASKBOOK_PREFIX + json.dumps(meta) + rs.TASKBOOK_SUFFIX + "\n"
        (directory / "TASK.md").write_text(text, encoding="utf-8")

    def test_ready_taskbook_missing_registry_fails(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            self._write_taskbook(root, "RS-HIDDEN", "READY")
            errors = rs.registry_integrity(config(task()), [], root=root)
            self.assertTrue(any("absent from scheduler registry" in error for error in errors))

    def test_published_taskbook_can_wait_for_runtime_publish_event(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            self._write_taskbook(root, "RS-PUB", "PUBLISHED")
            self.assertEqual([], rs.registry_integrity(config(task()), [], root=root))

    def test_runtime_publish_registers_task(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            self._write_taskbook(root, "RS-PUB", "PUBLISHED")
            errors = rs.registry_integrity(config(task()), [publish_event()], root=root)
            self.assertEqual([], errors)

    def test_repository_has_no_invisible_executable_taskbook(self):
        cfg = rs.load_scheduler_bundle(ROOT / "research_scheduler_v2.json")
        self.assertEqual([], rs.registry_integrity(cfg, [], root=ROOT))


if __name__ == "__main__":
    unittest.main()
