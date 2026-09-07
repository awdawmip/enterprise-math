"""Real publication/Result fixtures across the composed event authority gates."""
from __future__ import annotations

import copy
import json
import shutil
import tempfile
import unittest
from datetime import timedelta
from pathlib import Path

from control_plane import research_control_bootstrap as bootstrap
from control_plane import research_result_authority_fault_isolation as isolation
from tools import research_dispatch as dispatch
from tools import research_result_records as results
from tools import research_runtime_guard as guard
from tools import research_runtime_reducer as reducer
from tools import research_task_records as publications
from tests.test_research_runtime_claim_authority import auth, state as runtime_state
from tests.test_research_task_record_compatibility import _write_current_record, _write_semantic_fixture

ROOT = Path(__file__).resolve().parents[1]
RID = "RR-012E775840E54D36F41E"
PUBLISHED = "2026-09-07T02:21:00+00:00"


def setUpModule():
    bootstrap.install(ROOT)


class RegisteredEventControlCompositionTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.row = copy.deepcopy(isolation.quarantine_rows(ROOT)[RID])
        for pin in self.row["dependency_pins"]:
            target = self.root / pin["path"]
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / pin["path"], target)
        self.save(isolation.QUARANTINE_FILE, {
            "schema": isolation.SCHEMA, "status": "ACTIVE", "entries": [self.row],
        })
        _write_semantic_fixture(self.root)
        self.pub = self.load(self.row["publication_record_path"])
        self.rr = self.load(self.row["record_path"])
        self.task_id = self.row["task_id"]
        self.pub_id = self.row["publication_id"]
        self.freeze = reducer.parse_time(self.rr["frozen_at"])
        self.before = {pin["path"]: (self.root / pin["path"]).read_bytes()
                       for pin in self.row["dependency_pins"]}
        self.assertIn(RID, isolation.validated_rows(self.root))

    def tearDown(self):
        self.assertEqual(self.before, {path: (self.root / path).read_bytes()
                                      for path in self.before})

    def save(self, relative, value):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")

    def load(self, relative):
        return json.loads((self.root / relative).read_text(encoding="utf-8"))

    def definition(self):
        return dispatch.registered_definition(self.pub, self.root)

    def unheld_definition(self):
        record = _write_current_record(
            self.root, task_id="RS-EVENT-CROSS", publication_id="TP2-EVENT-CROSS",
            parent_objective_id="OBJ-EVENT-CROSS", claimable=True, published_at=PUBLISHED,
        )
        record_path = f"research_task_records/{record['task_id']}/{record['publication_id']}.json"
        self.assertEqual([], [error for error in publications.audit(self.root)
                              if error.startswith(record_path + ": ")])
        self.assertEqual(record, {key: value for key, value in
                                  publications.current_records(self.root)[record["task_id"]].items()
                                  if key != "_record_path"})
        return dispatch.registered_definition(record, self.root)

    def event(self, task, kind, index, at, **fields):
        timestamp = at.isoformat() if hasattr(at, "isoformat") else at
        meta = auth(index)
        meta.update(created_at=timestamp, updated_at=timestamp)
        return {
            "schema": reducer.EVENT_SCHEMA, "event": kind, "task_id": task["task_id"],
            "at": timestamp, "_github": meta, **fields,
        }

    def claim(self, task, index, at, claim_id="cross-owner", **fields):
        return self.event(
            task, "CLAIM", index, at, claim_id=claim_id,
            researcher_id="EM-CROSS-ABC123", publication_id=task["publication_id"],
            theorem_owner=task.get("owner") or "taskbook/unassigned",
            execution_branch="research/event-composition-fixture", execution_branch_base="b" * 40,
            allowed_outputs=["research_returns/"], lease_minutes=120, **fields,
        )

    def reduce(self, task, events, now):
        return dispatch.reduce_definition(task, events, now=now, root=self.root)

    def test_real_intent_binding_precedes_publication_clock_and_held_filter(self):
        task = self.definition()
        intent = self.load(self.row["execution_record_path"])
        selected = dispatch.research_execution_records.intent_for_claim(
            self.task_id, intent["claim_id"], self.root)
        self.assertEqual(self.row["execution_record_path"], selected["_record_path"])
        self.assertEqual(intent, {key: value for key, value in selected.items() if key != "_record_path"})
        published = reducer.parse_time(self.pub["published_at"])
        self.assertLess(published, self.freeze)
        for index, at, rejected in ((8101, published - timedelta(seconds=1), True),
                                    (8102, published, False)):
            with self.subTest(at=at):
                event = self.event(task, "CLAIM", index, at,
                                   claim_id=intent["claim_id"], researcher_id=intent["researcher_id"])
                accepted, errors = dispatch._filter_registered_events(task, [event], self.root)
                if rejected:
                    self.assertEqual([], accepted)
                    self.assertTrue(any("predates current task publication" in row["reason"]
                                        for row in errors))
                else:
                    self.assertEqual([], errors)
                    self.assertEqual(self.pub_id, accepted[0]["publication_id"])

    def test_prepublication_claim_cannot_supply_handoff_or_done_blocking_authority(self):
        task = self.unheld_definition()
        published = reducer.parse_time(PUBLISHED)
        for kind in ("HANDOFF", "DONE"):
            with self.subTest(kind=kind):
                events = [self.claim(task, 8201, published - timedelta(seconds=1)),
                          self.event(task, kind, 8202, published + timedelta(seconds=1),
                                     claim_id="cross-owner", next_action="unscoped return")]
                state = self.reduce(task, events, published + timedelta(hours=3))
                self.assertEqual("READY", state["state"])
                self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
                self.assertIsNone(state.get("hard_block"))
                reasons = [row["reason"] for row in state["ignored_events"]]
                self.assertTrue(any("predates current task publication" in reason for reason in reasons))
                expected = "scope contract" if kind == "HANDOFF" else "requires a frozen result"
                self.assertTrue(any(expected in reason for reason in reasons))

    def test_real_unheld_publication_supports_typed_continuation_and_frozen_return(self):
        task = self.unheld_definition()
        published = reducer.parse_time(PUBLISHED)
        for scope, expected in (("CONTINUATION", "NEEDS_DISPATCH"),
                                ("FROZEN_RETURN_AWAITING_DRIVER_REVIEW", "AWAITING_REVIEW")):
            with self.subTest(scope=scope):
                events = [self.claim(task, 8301, published),
                          self.event(task, "HANDOFF", 8302, published + timedelta(minutes=1),
                                     claim_id="cross-owner", handoff_scope=scope,
                                     next_action="continue or freeze according to explicit scope")]
                state = self.reduce(task, events, published + timedelta(minutes=2))
                self.assertEqual(expected, state["dispatch_state"])
                self.assertEqual(scope, state["handoff_scope"])
                self.assertIsNot(state.get("terminal"), True)
                self.assertIsNone(results.task_result_state(task["task_id"], self.root,
                                                            task["publication_id"]))

    def test_live_postpublication_claim_still_supplies_ambiguous_handoff_barrier(self):
        task = self.unheld_definition()
        published = reducer.parse_time(PUBLISHED)
        events = [self.claim(task, 8401, published),
                  self.event(task, "HANDOFF", 8402, published + timedelta(minutes=1),
                             claim_id="cross-owner", next_action="unscoped return")]
        state = self.reduce(task, events, published + timedelta(hours=3))
        self.assertEqual("BLOCKED", state["dispatch_state"])
        self.assertEqual("REGISTERED_HANDOFF_SCOPE_REQUIRED", state["hard_block"]["code"])
        self.assertEqual("cross-owner", state["hard_block"]["claim_id"])

    def test_typed_handoff_done_and_reopen_cannot_restore_exact_held_generation(self):
        task = self.definition()
        old = self.claim(task, 8501, self.freeze - timedelta(minutes=1))
        at = dispatch.HANDOFF_SCOPE_CUTOVER + timedelta(minutes=1)
        held = results.task_result_state(self.task_id, self.root, self.pub_id)
        for marker in ({"handoff_scope": dispatch.HANDOFF_SCOPE_FROZEN_RETURN},
                       {"terminal_scope": dispatch.DRIVER_REVIEW_TERMINAL_SCOPE},
                       {"result_id": RID}):
            with self.subTest(marker=marker):
                events = [old, self.claim(task, 8502, at),
                          self.event(task, "HANDOFF", 8503, at, claim_id="cross-owner",
                                     next_action="request Driver review", **marker),
                          self.event(task, "DONE", 8504, at, claim_id="cross-owner", result_id=RID),
                          self.event(task, "UNBLOCK", 8505, at, publication_id=self.pub_id,
                                     next_action="reopen held generation"),
                          self.event(task, "SUPERSEDE", 8506, at, publication_id=self.pub_id,
                                     next_action="close held generation")]
                implicit = dispatch._filter_registered_events(task, events, self.root)
                explicit = dispatch._filter_registered_events(task, events, self.root, held)
                self.assertEqual(explicit, implicit)
                self.assertEqual([8501], [event["_github"]["comment_id"] for event in implicit[0]])
                state = self.reduce(task, events, at + timedelta(minutes=1))
                self.assertEqual("BLOCKED", state["dispatch_state"])
                self.assertFalse(state["terminal"])
                self.assertEqual(isolation.STATE, state["hard_block"]["code"])
                self.assertIsNone(state["result_id"])
                self.assertIsNone(state["review_id"])
        runtime = runtime_state()
        runtime["task"]["task_id"] = self.task_id
        runtime["task_registration"]["registry_key"] = self.task_id
        runtime["parent_objective"]["objective_id"] = self.pub["parent_objective_id"]
        with self.assertRaisesRegex(guard.RuntimeAuthorizationError, isolation.STATE):
            guard.authorize_execution(runtime, events=[old], now=self.freeze, root=self.root)

    def test_mixed_cohort_keeps_valid_lane_authority_separate_from_held_publication(self):
        other = self.pub["supersedes_publication_id"]
        _write_current_record(self.root, task_id=self.task_id, publication_id=other,
                              parent_objective_id=self.pub["parent_objective_id"], claimable=True,
                              published_at=self.pub["published_at"])
        lanes = [{"lane_id": lane, "publication_id": pub, "lane_role": "AUDIT",
                  "purpose": "exact publication boundary",
                  "output_prefix": f"research_returns/parallel/EC-CROSS/{lane}/"}
                 for lane, pub in (("held", self.pub_id), ("independent", other))]
        self.save(f"research_execution_cohorts/{self.task_id}/EC-CROSS.json", {
            "schema": "ENTERPRISE_MATH_PARALLEL_EXECUTION_COHORT_V1", "task_id": self.task_id,
            "cohort_id": "EC-CROSS", "record_state": "ACTIVE", "opened_by": "EM-DVR-ABC123",
            "opened_at": self.freeze.isoformat(), "lanes": lanes,
            "two_reference_passes_required": True, "synthesis_required": True,
            "working_truth_granted": False, "canonical_promotion_granted": False,
        })
        state = self.reduce(self.definition(), [], self.freeze)
        self.assertEqual("COHORT_ACTIVE", state["dispatch_state"])
        self.assertEqual([self.pub_id], state["withheld_lane_publication_ids"])
        for lane, pub, authorized in (("held", self.pub_id, False), ("independent", other, True)):
            with self.subTest(lane=lane):
                definition = {**self.definition(), "publication_id": pub}
                event = self.claim(definition, 8601, self.freeze + timedelta(minutes=1),
                                   execution_cohort_id="EC-CROSS", execution_lane_id=lane)
                event["allowed_outputs"] = [f"research_returns/parallel/EC-CROSS/{lane}/"]
                self.assertLess(reducer.parse_time(self.pub["published_at"]),
                                reducer.parse_time(event["at"]))
                runtime = runtime_state()
                runtime["task"]["task_id"] = self.task_id
                runtime["task_registration"]["registry_key"] = self.task_id
                runtime["parent_objective"]["objective_id"] = self.pub["parent_objective_id"]
                runtime["execution_scope"] = {"execution_cohort_id": "EC-CROSS", "execution_lane_id": lane}
                if authorized:
                    decision = guard.authorize_execution(runtime, events=[event],
                                                         now=self.freeze + timedelta(minutes=2), root=self.root)
                    self.assertTrue(decision["authorized"])
                    self.assertEqual(pub, decision["execution_binding"]["publication_id"])
                else:
                    with self.assertRaisesRegex(guard.RuntimeAuthorizationError, isolation.STATE):
                        guard.authorize_execution(runtime, events=[event],
                                                  now=self.freeze + timedelta(minutes=2), root=self.root)

    def test_public_dispatch_snapshot_keeps_exact_dependency_drift_guard(self):
        path = self.root / self.row["derived_reviews"][0]["review_record_path"]
        before = path.read_bytes()
        try:
            with self.assertRaisesRegex(isolation.ResultAuthorityIsolationError, "snapshot inputs changed"):
                with dispatch._dispatch_result_read_snapshot(self.root):
                    self.assertEqual(isolation.STATE,
                                     results.task_result_state(self.task_id, self.root, self.pub_id)["state"])
                    path.write_bytes(before + b"\n")
        finally:
            path.write_bytes(before)

    def test_registered_filters_leave_other_task_and_nonregistered_events_untouched(self):
        task = self.unheld_definition()
        event = self.event(task, "HANDOFF", 8701, PUBLISHED, claim_id="outside")
        other = {**event, "task_id": "RS-UNRELATED"}
        self.assertEqual(([other], []), dispatch._filter_registered_events(task, [other], self.root, None))
        unregistered = {**task, "registration_source": "DIRECT_LIBRARY"}
        self.assertEqual(([event], []),
                         dispatch._filter_registered_events(unregistered, [event], self.root, None))

    def test_all_composed_core_hooks_remain_live(self):
        for name in ("registered_definition", "_filter_registered_events", "_block_unreviewed_registered_done",
                     "_overlay_result_state", "_overlay_active_cohort", "_dispatch_result_read_snapshot"):
            self.assertIs(getattr(dispatch._core, name), getattr(dispatch, name), name)

    def test_nonstring_handoff_fields_are_controlled_rejections(self):
        task = self.unheld_definition()
        start = reducer.parse_time(PUBLISHED)
        owner = self.claim(task, 9001, start)
        for field in ("handoff_scope", "terminal_scope", "terminal_candidate"):
            for malformed in ({}, [], True, 1):
                with self.subTest(field=field, malformed=malformed):
                    event = self.event(task, "HANDOFF", 9002, start + timedelta(minutes=1),
                                       claim_id="cross-owner", next_action="malformed scope",
                                       **{field: malformed})
                    public = self.reduce(task, [owner, event], start + timedelta(hours=3))
                    self.assertEqual("BLOCKED", public["dispatch_state"])
                    self.assertEqual("REGISTERED_HANDOFF_SCOPE_REQUIRED", public["hard_block"]["code"])
                    pure = reducer.reduce_task(task, [owner, event], default_lease_minutes=120,
                                               now=start + timedelta(minutes=2))
                    self.assertEqual("LEASED", pure["dispatch_state"])
                    self.assertEqual("cross-owner", pure["claim_id"])
                    self.assertEqual(1, len(pure["ignored_events"]))
                    self.assertIn(field, pure["ignored_events"][0]["reason"])

    def test_terminal_barrier_replay_uses_resolved_task_and_caller_lease(self):
        task = self.unheld_definition()
        start = reducer.parse_time(PUBLISHED)
        for lease, progress_minute, terminal_minute, expected in (
            (120, 10, 110, "BLOCKED"), (10, 5, 20, "NEEDS_DISPATCH"),
        ):
            for lease_source in ("task", "caller_default"):
                definition = {**task, "claim_lease_minutes": lease}
                if lease_source == "caller_default":
                    definition.pop("claim_lease_minutes")
                for kind in ("HANDOFF", "DONE"):
                    with self.subTest(lease=lease, lease_source=lease_source, kind=kind):
                        owner = self.claim(definition, 9101, start)
                        owner["lease_minutes"] = lease
                        progress = self.event(definition, "PROGRESS", 9102,
                                              start + timedelta(minutes=progress_minute),
                                              claim_id="cross-owner", progress_ref="durable fixture update")
                        self.assertNotIn("lease_minutes", progress)
                        terminal = self.event(definition, kind, 9103,
                                              start + timedelta(minutes=terminal_minute),
                                              claim_id="cross-owner", next_action="ambiguous owner return")
                        prior = reducer.reduce_task(definition, [owner, progress],
                                                    default_lease_minutes=lease,
                                                    now=start + timedelta(minutes=terminal_minute))
                        self.assertEqual(expected == "BLOCKED", prior["dispatch_state"] == "LEASED")
                        state = dispatch.reduce_definition(
                            definition, [owner, progress, terminal], now=start + timedelta(hours=4),
                            default_lease_minutes=lease if lease_source == "caller_default" else 77,
                            root=self.root,
                        )
                        self.assertEqual(expected, state["dispatch_state"])
                        if expected == "BLOCKED":
                            code = ("REGISTERED_HANDOFF_SCOPE_REQUIRED" if kind == "HANDOFF" else
                                    "REGISTERED_DONE_REQUIRES_TERMINAL_DRIVER_REVIEW")
                            self.assertEqual(code, state["hard_block"]["code"])
                        else:
                            self.assertIsNone(state.get("hard_block"))

    def test_terminal_barriers_share_live_researcher_identity_with_reducer(self):
        task = self.unheld_definition()
        start = reducer.parse_time(PUBLISHED)
        owner = self.claim(task, 9201, start)
        for researcher, matches in ((None, True), (" em-cross-abc123 ", True),
                                    ("EM-OTHER-ABC123", False), ({}, False)):
            for kind in ("HANDOFF", "DONE"):
                with self.subTest(researcher=researcher, kind=kind):
                    event = self.event(task, kind, 9202, start + timedelta(minutes=1),
                                       claim_id="cross-owner", researcher_id=researcher,
                                       next_action="same claim, independently checked researcher")
                    state = self.reduce(task, [owner, event], start + timedelta(hours=3))
                    self.assertEqual("BLOCKED" if matches else "NEEDS_DISPATCH", state["dispatch_state"])
                    if not matches:
                        self.assertIsNone(state.get("hard_block"))
                    typed = {**event, "event": "HANDOFF", "handoff_scope": "CONTINUATION"}
                    control = self.reduce(task, [owner, typed], start + timedelta(minutes=2))
                    self.assertEqual("NEEDS_DISPATCH" if matches else "LEASED", control["dispatch_state"])
                    if not matches:
                        self.assertTrue(any("researcher_id" in row["reason"] for row in control["ignored_events"]))


if __name__ == "__main__":
    unittest.main()
