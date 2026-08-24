import json
import pathlib
import tempfile
import unittest

from tools import research_scheduler as rs

ROOT = pathlib.Path(__file__).resolve().parents[1]


def legacy_task(task_id="RS-OLD", state="READY", owner="owner/a"):
    return {
        "task_id": task_id, "title": task_id, "kind": "RESEARCH", "owner": owner,
        "base_state": state, "priority": "P1", "leverage": "HIGH",
        "frontier": "frontier", "next_action": "next", "dependencies": [],
        "source_refs": [], "last_progress_ref": "seed",
        "last_progress_at": "2026-08-23T10:00:00+08:00", "hard_block": None,
    }


def config():
    return json.loads((ROOT / "research_scheduler.json").read_text())


def v2(kind, task_id="RS-T", at="2026-08-24T16:10:00+08:00", **extra):
    e = {"schema": rs.V2_SCHEMA, "event": kind, "task_id": task_id, "at": at}
    e.update(extra); return e


class V2Tests(unittest.TestCase):
    def setUp(self):
        self.td = tempfile.TemporaryDirectory(); self.root = pathlib.Path(self.td.name)
        (self.root / "research_tasks").mkdir()
        cfg = config(); (self.root / "research_scheduler.json").write_text(json.dumps(cfg))
        legacy = {"schema":"ENTERPRISE_MATH_RESEARCH_SCHEDULER_V1","tasks":[legacy_task()]}
        (self.root / "research_scheduler_v1_legacy.json").write_text(json.dumps(legacy))
        self.cfg = cfg
    def tearDown(self): self.td.cleanup()
    def now(self, s="2026-08-24T16:20:00+08:00"): return rs.parse_time(s)

    def write_structured(self, task_id, *, marker=False):
        meta = legacy_task(task_id)
        if marker:
            meta["scheduler_registration"] = {"schema":"ENTERPRISE_MATH_SCHEDULER_TASK_REGISTRATION_V2","publication_required":True}
        text = rs.TASKBOOK_PREFIX + json.dumps(meta) + rs.TASKBOOK_SUFFIX + "\n# T\n"
        (self.root / "research_tasks" / f"{task_id}.md").write_text(text)

    def test_repository_scheduler_contract(self):
        owners_path = ROOT / "branch_governance_overrides.json"
        if not owners_path.exists():
            self.skipTest("repository owner registry not present in isolated fixture checkout")
        cfg = rs.load_json(ROOT / "research_scheduler.json")
        owners = rs.load_json(owners_path)
        self.assertEqual([], rs.validate_scheduler(cfg, owners, root=ROOT))
        ids = {t["task_id"] for t in rs.materialize_tasks(cfg, [], root=ROOT)}
        self.assertIn("RS-PRIME-FUSION-F1-LEAN-FINITE-ALGEBRA-FORMALIZATION", ids)

    def test_unregistered_taskbook_is_durable_orphan(self):
        self.write_structured("RS-ORPH")
        task = {x["task_id"]: x for x in rs.materialize_tasks(self.cfg, [], root=self.root)}["RS-ORPH"]
        self.assertEqual("ORPHANED", task["base_state"])
        state = rs.reduce_task(task, [], config=self.cfg, now=self.now())
        self.assertEqual("ORPHAN_RECOVERY", state["dispatch_state"])
        self.assertTrue(state["orphan_records"])

    def test_v2_taskbook_is_registered_but_not_dispatchable_until_publish(self):
        self.write_structured("RS-V2", marker=True)
        task = {x["task_id"]: x for x in rs.materialize_tasks(self.cfg, [], root=self.root)}["RS-V2"]
        self.assertEqual("DRAFT", task["base_state"])
        self.assertEqual("DORMANT", rs.reduce_task(task, [], config=self.cfg, now=self.now())["dispatch_state"])

    def test_free_researcher_publish_then_cross_driver_approve(self):
        payload = legacy_task("RS-FREE")
        events = [v2("PUBLISH", "RS-FREE", publisher_role="RESEARCHER", publisher_id="EM-FREE-ABC123", task=payload, publication_ref="PR #1")]
        task = {x["task_id"]: x for x in rs.materialize_tasks(self.cfg, events, root=self.root)}["RS-FREE"]
        state = rs.reduce_task(task, events, config=self.cfg, now=self.now())
        self.assertEqual("REVIEW_PENDING", state["state"])
        events += [v2("REVIEW_CLAIM", "RS-FREE", at="2026-08-24T16:11:00+08:00", reviewer_id="EM-DVR-111AAA", review_claim_id="r1")]
        events += [v2("APPROVE", "RS-FREE", at="2026-08-24T16:12:00+08:00", reviewer_id="EM-DVR-111AAA", review_claim_id="r1", taskbook_ref="research_tasks/FREE.md@abcdef1", review_ref="review.md@abcdef2")]
        state = rs.reduce_task(task, events, config=self.cfg, now=self.now())
        self.assertEqual("READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])

    def test_publisher_cannot_self_review(self):
        payload = legacy_task("RS-X")
        events = [v2("PUBLISH", "RS-X", publisher_role="RESEARCH_DRIVER", publisher_id="EM-DVR-111AAA", task=payload)]
        events += [v2("REVIEW_CLAIM", "RS-X", at="2026-08-24T16:11:00+08:00", reviewer_id="EM-DVR-111AAA", review_claim_id="r1")]
        task = {x["task_id"]: x for x in rs.materialize_tasks(self.cfg, events, root=self.root)}["RS-X"]
        state = rs.reduce_task(task, events, config=self.cfg, now=self.now())
        self.assertEqual("REVIEW_PENDING", state["state"]); self.assertIsNone(state["review_claim_id"])
        self.assertTrue(state["ignored_events"])

    def approved_claim_events(self, task_id="RS-X", executor="EM-RX-ABC123"):
        payload = legacy_task(task_id)
        return [
            v2("PUBLISH", task_id, publisher_role="RESEARCH_DRIVER", publisher_id="EM-DVR-111AAA", task=payload),
            v2("REVIEW_CLAIM", task_id, at="2026-08-24T16:11:00+08:00", reviewer_id="EM-DVR-222BBB", review_claim_id="pub-review"),
            v2("APPROVE", task_id, at="2026-08-24T16:12:00+08:00", reviewer_id="EM-DVR-222BBB", review_claim_id="pub-review", taskbook_ref="research_tasks/X.md@abcdef1", review_ref="review.md@abcdef2"),
            v2("CLAIM", task_id, at="2026-08-24T16:13:00+08:00", claim_id="c1", execution_id=executor, actor_role="RESEARCHER", lease_minutes=10),
        ]

    def test_lease_expiry_creates_orphan_not_handoff(self):
        events = self.approved_claim_events()
        task = {x["task_id"]: x for x in rs.materialize_tasks(self.cfg, events, root=self.root)}["RS-X"]
        state = rs.reduce_task(task, events, config=self.cfg, now=self.now("2026-08-24T16:24:00+08:00"))
        self.assertEqual("ORPHANED", state["state"]); self.assertEqual("ORPHAN_RECOVERY", state["dispatch_state"])
        self.assertEqual("LEASE_EXPIRED", state["orphan_records"][-1]["reason"])

    def test_orphan_requires_adopt(self):
        self.write_structured("RS-ORPH")
        events = [v2("ADOPT", "RS-ORPH", claim_id="a1", execution_id="EM-RORPH-ABC123", actor_role="RESEARCHER", recovery_ref="PR #9")]
        task = {x["task_id"]: x for x in rs.materialize_tasks(self.cfg, events, root=self.root)}["RS-ORPH"]
        state = rs.reduce_task(task, events, config=self.cfg, now=self.now())
        self.assertEqual("CLAIMED", state["state"]); self.assertEqual("LEASED", state["dispatch_state"])

    def test_direct_done_forbidden_submit_and_cross_review_required(self):
        events = self.approved_claim_events(executor="EM-RX-ABC123")
        events += [v2("DONE", "RS-X", at="2026-08-24T16:14:00+08:00", claim_id="c1", execution_id="EM-RX-ABC123")]
        task = {x["task_id"]: x for x in rs.materialize_tasks(self.cfg, events, root=self.root)}["RS-X"]
        state = rs.reduce_task(task, events, config=self.cfg, now=self.now("2026-08-24T16:15:00+08:00"))
        self.assertNotEqual("DONE", state["state"])
        events += [v2("SUBMIT", "RS-X", at="2026-08-24T16:15:00+08:00", claim_id="c1", execution_id="EM-RX-ABC123", return_ref="return.md@abcdef3")]
        events += [v2("REVIEW_CLAIM", "RS-X", at="2026-08-24T16:16:00+08:00", reviewer_id="EM-DVR-333CCC", review_claim_id="ret-review")]
        events += [v2("REVIEW", "RS-X", at="2026-08-24T16:17:00+08:00", reviewer_id="EM-DVR-333CCC", review_claim_id="ret-review", verdict="ACCEPT", review_ref="driver_review.md@abcdef4")]
        state = rs.reduce_task(task, events, config=self.cfg, now=self.now())
        self.assertEqual("DONE", state["state"]); self.assertEqual("EM-DVR-333CCC", state["review"]["reviewer_id"])

    def test_executor_driver_cannot_self_review_return(self):
        events = self.approved_claim_events(executor="EM-DVR-333CCC")
        events += [v2("SUBMIT", "RS-X", at="2026-08-24T16:14:00+08:00", claim_id="c1", execution_id="EM-DVR-333CCC", return_ref="r.md@abcdef3")]
        events += [v2("REVIEW_CLAIM", "RS-X", at="2026-08-24T16:15:00+08:00", reviewer_id="EM-DVR-333CCC", review_claim_id="rr")]
        task = {x["task_id"]: x for x in rs.materialize_tasks(self.cfg, events, root=self.root)}["RS-X"]
        state = rs.reduce_task(task, events, config=self.cfg, now=self.now())
        self.assertEqual("RETURN_REVIEW", state["state"]); self.assertIsNone(state["review_claim_id"])

    def test_v1_event_after_cutover_is_ignored(self):
        task = legacy_task("RS-OLD")
        event = {"schema":rs.V1_SCHEMA,"event":"CLAIM","task_id":"RS-OLD","at":"2026-08-24T16:01:00+08:00","claim_id":"old"}
        state = rs.reduce_task(task, [event], config=self.cfg, now=self.now())
        self.assertEqual("READY", state["state"]); self.assertTrue(state["ignored_events"])

    def test_historical_v1_done_is_preserved(self):
        task = legacy_task("RS-OLD")
        events = [
            {"schema":rs.V1_SCHEMA,"event":"CLAIM","task_id":"RS-OLD","at":"2026-08-24T15:40:00+08:00","claim_id":"c"},
            {"schema":rs.V1_SCHEMA,"event":"DONE","task_id":"RS-OLD","at":"2026-08-24T15:50:00+08:00","claim_id":"c","progress_ref":"PR #old"},
        ]
        state = rs.reduce_task(task, events, config=self.cfg, now=self.now())
        self.assertEqual("DONE", state["state"]); self.assertEqual("LEGACY_V1_PRE_CUTOVER", state["review"]["authority"])

    def test_republish_resets_old_terminal_generation(self):
        task = legacy_task("RS-X")
        events = [
            {"schema":rs.V1_SCHEMA,"event":"SUPERSEDE","task_id":"RS-X","at":"2026-08-24T15:50:00+08:00"},
            v2("PUBLISH", "RS-X", publisher_role="RESEARCHER", publisher_id="EM-FREE-ABC123", task=legacy_task("RS-X")),
        ]
        state = rs.reduce_task(task, events, config=self.cfg, now=self.now())
        self.assertEqual("REVIEW_PENDING", state["state"]); self.assertEqual(1, state["generation"])

    def test_migrate_external_live_task(self):
        payload = legacy_task("RS-LIVE")
        events = [v2("MIGRATE", "RS-LIVE", driver_id="EM-DVR-111AAA", migration_ref="PR #619", target_state="IN_PROGRESS", task=payload, claim_id="migration-619", execution_id="EM-PFF1-6DA3FD", lease_minutes=60)]
        task = {x["task_id"]: x for x in rs.materialize_tasks(self.cfg, events, root=self.root)}["RS-LIVE"]
        state = rs.reduce_task(task, events, config=self.cfg, now=self.now())
        self.assertEqual("IN_PROGRESS", state["state"]); self.assertEqual("EM-PFF1-6DA3FD", state["execution_id"])

    def test_select_review_never_returns_self_review(self):
        payload = legacy_task("RS-A")
        events = [v2("PUBLISH", "RS-A", publisher_role="RESEARCH_DRIVER", publisher_id="EM-DVR-111AAA", task=payload)]
        self.assertIsNone(rs.select_review(self.cfg, events, self.now(), reviewer_id="EM-DVR-111AAA", root=self.root))
        self.assertEqual("RS-A", rs.select_review(self.cfg, events, self.now(), reviewer_id="EM-DVR-222BBB", root=self.root)["task_id"])

    def test_registry_report_lists_orphans(self):
        self.write_structured("RS-ORPH")
        report = rs.registry_report(self.cfg, [], self.now(), root=self.root)
        self.assertIn("RS-ORPH", report["orphans"])

if __name__ == "__main__": unittest.main()
