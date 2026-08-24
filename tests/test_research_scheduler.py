import json
import pathlib
import tempfile
import unittest

from tools import research_scheduler as rs

ROOT = pathlib.Path(__file__).resolve().parents[1]


def policy():
    return {
        "priority_order": ["P0", "P1", "P2", "P3"],
        "leverage_order": ["HIGH", "MEDIUM", "LOW"],
        "state_order": ["HANDOFF_READY", "CHANGES_REQUESTED", "READY"],
    }


def task(task_id="RS-T1", *, owner="owner/a", state="READY", kind="RESEARCH"):
    return {
        "task_id": task_id,
        "title": task_id,
        "kind": kind,
        "owner": owner if kind == "RESEARCH" else "governance",
        "base_state": state,
        "priority": "P1",
        "leverage": "HIGH",
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


def config(*items):
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
        "selection_policy": policy(),
        "publish_contract": {
            "allowed_publisher_roles": ["RESEARCHER", "RESEARCH_DRIVER", "STEWARD", "USER"],
            "publisher_id_required_for_roles": ["RESEARCHER", "RESEARCH_DRIVER", "STEWARD"],
            "required_task_fields": ["title", "kind", "owner", "priority", "leverage", "frontier", "next_action"],
        },
        "registry_integrity": {
            "taskbook_directory": "research_tasks",
            "auto_register_untracked_taskbooks_as_orphaned": True,
        },
        "tasks": list(items),
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


def publish_event(*, task_id="RS-PUB", role="RESEARCHER", publisher_id="EM-FREE-AB12", owner="owner/a", taskbook_ref=None, policy_state=None):
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
    if taskbook_ref:
        value["taskbook_ref"] = taskbook_ref
    if policy_state is not None:
        value["taskbook_policy_state"] = policy_state
    return value


def review_event(stage, verdict, at="2026-08-25T01:10:00+08:00", *, task_id="RS-PUB", reviewer="EM-DVR-Z9K8", **extra):
    return event(
        "REVIEW", at, task_id=task_id, claim_id=None,
        review_stage=stage, verdict=verdict, reviewer_id=reviewer,
        review_ref="driver_reviews/test.md", **extra,
    )


class SchedulerV2ConfigTests(unittest.TestCase):
    def test_repository_config_validates_and_migrates_r043_chain(self):
        cfg = rs.load_scheduler_bundle(ROOT / "research_scheduler_v2.json")
        own = json.loads((ROOT / "branch_governance_overrides.json").read_text(encoding="utf-8"))
        self.assertEqual([], rs.validate_scheduler(cfg, own))
        by_id = {item["task_id"]: item for item in cfg["tasks"]}
        self.assertEqual("DONE", by_id["RS-R043-NATIVE-SURFACE-FRONTIER-RECONSTRUCTION-MARKOV-CARRIER"]["base_state"])
        self.assertEqual("DONE", by_id["RS-R043C1-NATIVE-SLOT-COMPLETION-G0-INJECTIVITY"]["base_state"])
        self.assertEqual("DONE", by_id["RS-R043C2-G0-FUTURE-SUFFICIENCY-MODULO-SHIELDED-COMPONENTS"]["base_state"])
        self.assertEqual("DONE", by_id["RS-R043C3-UNOCCUPIED-COMPONENT-FRONTIER-CONNECTIVITY"]["base_state"])
        self.assertEqual("READY", by_id["RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE"]["base_state"])

    def test_static_unknown_owner_fails(self):
        errors = rs.validate_scheduler(config(task(owner="missing")), owners("owner/a"))
        self.assertTrue(any("not ACTIVE_OWNER" in error for error in errors))


class SchedulerPublicationTests(unittest.TestCase):
    NOW = rs.parse_time("2026-08-25T02:00:00+08:00")

    def state_for(self, events, task_id="RS-PUB"):
        states, issues = rs.effective_states(config(task()), events, self.NOW, root=ROOT)
        self.assertEqual([], issues)
        return next(state for state in states if state["task_id"] == task_id)

    def test_researcher_publish_is_registered_but_not_dispatchable(self):
        state = self.state_for([publish_event()])
        self.assertEqual("PUBLISHED", state["state"])
        self.assertEqual("NEEDS_REVIEW", state["dispatch_state"])
        self.assertEqual("EM-FREE-AB12", state["publisher_id"])

    def test_driver_cannot_accept_own_publication(self):
        events = [
            publish_event(role="RESEARCH_DRIVER", publisher_id="EM-DVR-Z9K8"),
            review_event("DISPATCH", "ACCEPT", reviewer="EM-DVR-Z9K8"),
        ]
        state = self.state_for(events)
        self.assertEqual("PUBLISHED", state["state"])
        self.assertTrue(any("independent" in item["reason"] for item in state["ignored_events"]))

    def test_independent_driver_accept_makes_ready(self):
        state = self.state_for([publish_event(), review_event("DISPATCH", "ACCEPT")])
        self.assertEqual("READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])

    def test_taskbook_dispatch_accept_requires_policy_pass(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            (root / "research_tasks").mkdir()
            taskbook = root / "research_tasks" / "X.md"
            taskbook.write_text(
                rs.TASKBOOK_PREFIX + json.dumps({"task_id": "RS-PUB", "base_state": "PUBLISHED"}) + rs.TASKBOOK_SUFFIX + "\n",
                encoding="utf-8",
            )
            events = [
                publish_event(taskbook_ref="research_tasks/X.md", policy_state="PENDING_POLICY_REVIEW"),
                review_event("DISPATCH", "ACCEPT"),
            ]
            states, _ = rs.effective_states(config(task()), events, self.NOW, root=root)
            state = next(s for s in states if s["task_id"] == "RS-PUB")
            self.assertEqual("PUBLISHED", state["state"])
            self.assertTrue(any("taskbook_policy_state=PASS" in item["reason"] for item in state["ignored_events"]))

    def test_taskbook_policy_pass_plus_independent_review_makes_ready(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            (root / "research_tasks").mkdir()
            taskbook = root / "research_tasks" / "X.md"
            taskbook.write_text(
                rs.TASKBOOK_PREFIX + json.dumps({"task_id": "RS-PUB", "base_state": "PUBLISHED"}) + rs.TASKBOOK_SUFFIX + "\n",
                encoding="utf-8",
            )
            events = [
                publish_event(taskbook_ref="research_tasks/X.md", policy_state="PASS"),
                review_event("DISPATCH", "ACCEPT"),
            ]
            states, issues = rs.effective_states(config(task()), events, self.NOW, root=root)
            self.assertEqual([], issues)
            state = next(s for s in states if s["task_id"] == "RS-PUB")
            self.assertEqual("READY", state["state"])


class SchedulerExecutionTests(unittest.TestCase):
    def test_v2_lease_expiry_is_orphaned_and_persistent(self):
        events = [event("CLAIM", "2026-08-25T01:00:00+08:00", lease_minutes=30)]
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=rs.parse_time("2026-08-25T01:31:00+08:00"))
        self.assertEqual("ORPHANED", state["state"])
        self.assertEqual("ORPHANED", state["dispatch_state"])
        self.assertEqual("LEASE_EXPIRED", state["orphan_history"][0]["reason"])
        self.assertFalse(state["orphan_history"][0]["legacy_auto_handoff"])

    def test_historical_v1_expiry_records_orphan_but_replays_old_reclaim_semantics(self):
        events = [
            event("CLAIM", "2026-08-25T01:00:00+08:00", schema=rs.V1_EVENT_SCHEMA, claim_id="old1", lease_minutes=30),
            event("CLAIM", "2026-08-25T01:40:00+08:00", schema=rs.V1_EVENT_SCHEMA, claim_id="old2", lease_minutes=30),
        ]
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=rs.parse_time("2026-08-25T01:50:00+08:00"))
        self.assertEqual("old2", state["claim_id"])
        self.assertEqual("CLAIMED", state["state"])
        self.assertEqual("LEGACY_V1_LEASE_EXPIRED", state["orphan_history"][0]["reason"])
        self.assertTrue(state["orphan_history"][0]["legacy_auto_handoff"])

    def test_return_requires_independent_driver_review_before_done(self):
        events = [
            event("CLAIM", "2026-08-25T01:00:00+08:00", researcher_id="EM-R043-AB12"),
            event("RETURN", "2026-08-25T01:10:00+08:00", researcher_id="EM-R043-AB12", return_ref="research_returns/T1.md"),
        ]
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=rs.parse_time("2026-08-25T01:11:00+08:00"))
        self.assertEqual("RETURNED", state["state"])
        self.assertEqual("NEEDS_REVIEW", state["dispatch_state"])
        events.append(review_event("RETURN", "ACCEPT", at="2026-08-25T01:20:00+08:00", task_id="RS-T1"))
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=rs.parse_time("2026-08-25T01:21:00+08:00"))
        self.assertEqual("DONE", state["state"])

    def test_v2_worker_done_is_ignored(self):
        events = [
            event("CLAIM", "2026-08-25T01:00:00+08:00"),
            event("DONE", "2026-08-25T01:10:00+08:00", progress_ref="bad"),
        ]
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=rs.parse_time("2026-08-25T01:11:00+08:00"))
        self.assertEqual("CLAIMED", state["state"])
        self.assertTrue(any("forbids worker DONE" in item["reason"] for item in state["ignored_events"]))

    def test_orphan_recovery_requires_driver(self):
        events = [event("CLAIM", "2026-08-25T01:00:00+08:00", lease_minutes=30)]
        events.append(event(
            "RECOVER", "2026-08-25T01:40:00+08:00", claim_id=None,
            driver_id="EM-DVR-Z9K8", review_ref="driver_reviews/recovery.md",
            next_action="resume exact proof",
        ))
        state = rs.reduce_task(task(), events, default_lease_minutes=30, now=rs.parse_time("2026-08-25T01:41:00+08:00"))
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual(1, len(state["orphan_history"]))


class SchedulerRegistryTests(unittest.TestCase):
    def write_taskbook(self, root, task_id="RS-HIDDEN", state="READY"):
        directory = root / "research_tasks"
        directory.mkdir(parents=True, exist_ok=True)
        meta = {
            "task_id": task_id,
            "title": "hidden legacy task",
            "kind": "RESEARCH",
            "owner": "owner/a",
            "base_state": state,
            "priority": "P1",
            "leverage": "HIGH",
            "frontier": "legacy frontier",
            "next_action": "audit legacy task",
        }
        path = directory / "TASK.md"
        path.write_text(rs.TASKBOOK_PREFIX + json.dumps(meta) + rs.TASKBOOK_SUFFIX + "\n", encoding="utf-8")
        return path

    def test_unregistered_ready_taskbook_is_auto_registered_orphan_not_hidden(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            self.write_taskbook(root)
            tasks, issues = rs.collect_tasks(config(task()), [], root=root)
            self.assertEqual([], issues)
            hidden = next(item for item in tasks if item["task_id"] == "RS-HIDDEN")
            self.assertEqual("ORPHANED", hidden["base_state"])
            self.assertEqual("TASKBOOK_ORPHAN_DISCOVERY", hidden["registry_source"])
            self.assertEqual([], rs.registry_integrity(config(task()), [], root=root))

    def test_auto_discovered_orphan_is_never_selected(self):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            self.write_taskbook(root)
            chosen = rs.select_task(config(), [], rs.parse_time("2026-08-25T02:00:00+08:00"), root=root)
            self.assertIsNone(chosen)

    def test_repository_has_no_invisible_taskbook(self):
        cfg = rs.load_scheduler_bundle(ROOT / "research_scheduler_v2.json")
        self.assertEqual([], rs.registry_integrity(cfg, [], root=ROOT))
        states, issues = rs.effective_states(cfg, [], rs.parse_time("2026-08-25T02:00:00+08:00"), root=ROOT)
        self.assertEqual([], issues)
        self.assertTrue(any(s["registry_source"] == "TASKBOOK_ORPHAN_DISCOVERY" for s in states))
        self.assertEqual("READY", next(s for s in states if s["task_id"] == "RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE")["state"])


if __name__ == "__main__":
    unittest.main()
