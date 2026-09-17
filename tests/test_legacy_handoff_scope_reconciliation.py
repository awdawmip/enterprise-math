"""Issue 1479: bounded scope repair must not become research/review authority."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import research_runtime_reducer as rr


def task(**changes):
    value = {
        "task_id": "RS-E001-IMPULSE-V2", "title": "E001 impulse",
        "kind": "RESEARCH", "owner": "engineering/e001-material-impulse-v2",
        "base_state": "HANDOFF_READY", "priority": "P2", "leverage": "MEDIUM",
        "publication_id": "TP2-E3B582B0D54E868F6828",
        "taskbook_blob_sha1": "sha1:7b9a611b4616e48dfbf3558b49875fb572f16325",
        "publication_published_at": "2026-09-02T00:00:00+00:00",
        "registration_source": "IMMUTABLE_TASK_RECORD",
        "evidence_status": "LEGACY_CONTROL_MIGRATED_HANDOFF_READY",
        "last_progress_ref": "PR #974 / 220baa23270edd203beb6ab0882f22fdb7571180",
        "last_progress_at": "2026-08-30T13:44:46+00:00",
        "next_action": "Driver review of the frozen return", "hard_block": None,
    }
    value.update(changes)
    return value


def event(kind, *, at="2026-09-17T04:10:00+00:00", **changes):
    value = {"schema": rr.EVENT_SCHEMA, "event": kind, "task_id": task()["task_id"],
             "at": at, "publication_id": task()["publication_id"],
             "_github": {"server_authenticated": True, "control_authorized": True,
                         "issue_number": 240, "comment_id": 1001, "edited": False,
                         "created_at": at}}
    value.update(changes)
    return value


def reconciliation(scope=rr.HANDOFF_SCOPE_FROZEN_RETURN, **changes):
    t = task()
    evidence = {
        "repository": "awdawmip/enterprise-math",
        "commit": "220baa23270edd203beb6ab0882f22fdb7571180",
        "path": "research_returns/E001_IMPULSE_CURRENT_HOLD_PASSIVITY_BUDGET_RETURN_20260830.md",
        "git_blob_sha1": "fc734e8cca5e4cd04069858b5a97e724ad4eaf7f",
        # Shape fixture only, not a claimed observation of the original source bytes.
        "sha256": "a" * 64,
    }
    value = event(rr.HANDOFF_SCOPE_RECONCILIATION,
                  taskbook_blob_sha1=t["taskbook_blob_sha1"],
                  source_handoff={"progress_ref": t["last_progress_ref"],
                                  "progress_at": t["last_progress_at"],
                                  "server_comment_id": None},
                  handoff_scope=scope, source_evidence=evidence,
                  progress_ref="https://github.com/awdawmip/enterprise-math/blob/" + evidence["commit"] + "/" + evidence["path"],
                  next_action="Driver review required; no new researcher execution")
    value.update(changes)
    return value


def reduce(events=(), t=None, now="2026-09-17T04:20:00+00:00", module=rr):
    return module.reduce_task(t or task(), events, default_lease_minutes=120,
                              now=module.parse_time(now))


class LegacyHandoffScopeTests(unittest.TestCase):
    def test_real_migrated_e001_frontier_is_not_fresh_work(self):
        s = reduce()
        self.assertEqual(s["dispatch_state"], "BLOCKED")
        self.assertEqual(s["hard_block"]["code"], "LEGACY_HANDOFF_SCOPE_UNRESOLVED")
        self.assertTrue(rr.complete_hard_block(s["hard_block"]))
        self.assertEqual(s["last_progress_ref"], task()["last_progress_ref"])

    def test_no_prose_classification(self):
        for text in ("continue research", "Driver: accept", "PASS", "REFUTED", "", "继续研究"):
            with self.subTest(text=text):
                self.assertEqual(reduce(t=task(next_action=text))["dispatch_state"], "BLOCKED")

    def test_ready_task_is_unchanged(self):
        self.assertEqual(reduce(t=task(base_state="READY"))["dispatch_state"], "NEEDS_DISPATCH")

    def test_nonmigration_handoff_baseline_is_unchanged(self):
        self.assertEqual(reduce(t=task(evidence_status="REGISTERED_TASK"))["dispatch_state"], "NEEDS_DISPATCH")

    def test_legacy_primitive_without_registration_is_unchanged(self):
        self.assertEqual(reduce(t=task(registration_source=None))["dispatch_state"], "NEEDS_DISPATCH")

    def test_new_claim_cannot_bypass_scope_barrier(self):
        s = reduce([event("CLAIM", claim_id="new")])
        self.assertEqual(s["dispatch_state"], "BLOCKED")
        self.assertIsNone(s["claim_id"])
        self.assertIn("reconciliation", s["ignored_events"][0]["reason"])

    def test_historical_owner_race_is_preserved(self):
        e = event("CLAIM", at="2026-09-17T03:50:00+00:00", claim_id="old")
        s = reduce([e])
        self.assertEqual(s["dispatch_state"], "LEASED")
        self.assertEqual(s["claim_id"], "old")

    def test_expired_historical_owner_does_not_restart_old_work(self):
        e = event("CLAIM", at="2026-09-17T01:00:00+00:00", claim_id="old")
        self.assertEqual(reduce([e])["dispatch_state"], "BLOCKED")

    def test_noop_progress_does_not_clear_scope_debt(self):
        c = event("CLAIM", at="2026-09-17T03:00:00+00:00", claim_id="old")
        p = event("PROGRESS", at="2026-09-17T03:01:00+00:00", claim_id="old",
                  progress_ref=task()["last_progress_ref"])
        self.assertEqual(reduce([c, p], now="2026-09-17T06:00:00+00:00")["dispatch_state"], "BLOCKED")

    def test_actual_subsequent_progress_preserves_continuation(self):
        c = event("CLAIM", at="2026-09-17T03:00:00+00:00", claim_id="old")
        p = event("PROGRESS", at="2026-09-17T03:01:00+00:00", claim_id="old", progress_ref="new-durable-frontier")
        self.assertEqual(reduce([c, p], now="2026-09-17T06:00:00+00:00")["dispatch_state"], "NEEDS_DISPATCH")

    def test_valid_frozen_reconciliation_has_no_claim_or_result(self):
        s = reduce([reconciliation()])
        self.assertEqual(s["state"], "FROZEN_RETURN")
        self.assertEqual(s["dispatch_state"], "AWAITING_REVIEW")
        self.assertIsNone(s["claim_id"])
        self.assertNotIn("result_id", s)
        self.assertNotIn("driver_disposition", s)
        self.assertEqual(s["handoff_scope_reconciliation"]["source_handoff"], reconciliation()["source_handoff"])

    def test_frozen_reconciliation_survives_time(self):
        self.assertEqual(reduce([reconciliation()], now="2027-01-01T00:00:00+00:00")["dispatch_state"], "AWAITING_REVIEW")

    def test_valid_continuation_reconciliation_reopens_only_scope(self):
        s = reduce([reconciliation(rr.HANDOFF_SCOPE_CONTINUATION)])
        self.assertEqual(s["dispatch_state"], "NEEDS_DISPATCH")
        self.assertIsNone(s["claim_id"])

    def test_continuation_still_needs_real_claim(self):
        a = reconciliation(rr.HANDOFF_SCOPE_CONTINUATION)
        c = event("CLAIM", at="2026-09-17T04:11:00+00:00", claim_id="real")
        self.assertEqual(reduce([a, c])["claim_id"], "real")

    def test_frozen_result_rejects_later_claim(self):
        c = event("CLAIM", at="2026-09-17T04:11:00+00:00", claim_id="illegal")
        self.assertEqual(reduce([reconciliation(), c])["dispatch_state"], "AWAITING_REVIEW")

    def test_correction_cannot_change_frozen_scope_later(self):
        a = reconciliation()
        b = reconciliation(rr.HANDOFF_SCOPE_CONTINUATION, at="2026-09-17T04:11:00+00:00")
        b["_github"]["created_at"] = b["at"]
        self.assertEqual(reduce([a, b])["dispatch_state"], "AWAITING_REVIEW")

    def test_duplicate_annotation_is_idempotent(self):
        a = reconciliation(); b = copy.deepcopy(a); b["_github"]["comment_id"] += 1
        s = reduce([a, b])
        self.assertEqual(s["dispatch_state"], "AWAITING_REVIEW")
        self.assertEqual(s["handoff_scope_reconciliation"]["server_comment_id"], 1001)

    def test_wrong_publication_rejected(self):
        self.assertEqual(reduce([reconciliation(publication_id="TP2-OTHER")])["dispatch_state"], "BLOCKED")

    def test_wrong_taskbook_rejected(self):
        self.assertEqual(reduce([reconciliation(taskbook_blob_sha1="sha1:" + "0" * 40)])["dispatch_state"], "BLOCKED")

    def test_wrong_task_ignored(self):
        self.assertEqual(reduce([reconciliation(task_id="RS-OTHER")])["dispatch_state"], "BLOCKED")

    def test_changed_frontier_rejected(self):
        for field in ("progress_ref", "progress_at", "server_comment_id"):
            a = reconciliation(); a["source_handoff"][field] = "different"
            with self.subTest(field=field):
                self.assertEqual(reduce([a])["dispatch_state"], "BLOCKED")

    def test_missing_and_forged_authorization_rejected(self):
        for key, val in (("server_authenticated", False), ("control_authorized", False),
                         ("edited", True), ("issue_number", 241), ("comment_id", True), ("comment_id", 0)):
            a = reconciliation(); a["_github"][key] = val
            with self.subTest(key=key, val=val):
                self.assertEqual(reduce([a])["dispatch_state"], "BLOCKED")
        a = reconciliation(); del a["_github"]
        self.assertEqual(reduce([a])["dispatch_state"], "BLOCKED")

    def test_clock_drift_and_prepublication_rejected(self):
        a = reconciliation(); a["_github"]["created_at"] = "2026-09-17T04:09:00+00:00"
        self.assertEqual(reduce([a])["dispatch_state"], "BLOCKED")
        a = reconciliation(at="2026-09-01T00:00:00+00:00")
        a["_github"]["created_at"] = a["at"]
        self.assertEqual(reduce([a])["dispatch_state"], "BLOCKED")

    def test_live_owner_not_stolen(self):
        c = event("CLAIM", at="2026-09-17T03:50:00+00:00", claim_id="old")
        s = reduce([c, reconciliation()])
        self.assertEqual(s["claim_id"], "old")
        self.assertEqual(s["dispatch_state"], "LEASED")

    def test_superseded_done_and_frozen_states_not_reopened(self):
        for state in ("SUPERSEDED", "DONE", "FROZEN_RETURN"):
            with self.subTest(state=state):
                s = reduce([reconciliation()], t=task(base_state=state))
                self.assertEqual(s["state"], state)

    def test_real_hardblock_not_erased(self):
        block = {k: "existing condition" for k in rr.HARD_BLOCK_FIELDS}
        s = reduce([reconciliation()], t=task(base_state="BLOCKED", hard_block=block))
        self.assertEqual(s["hard_block"], block)

    def test_ordinary_unblock_remains_ordinary(self):
        t = task(base_state="BLOCKED", hard_block={k: "existing" for k in rr.HARD_BLOCK_FIELDS})
        self.assertEqual(reduce([event("UNBLOCK")], t=t)["dispatch_state"], "NEEDS_DISPATCH")

    def test_annotation_cannot_assign_math_or_execution_authority(self):
        for field in ("result_id", "review_id", "terminal_verdict", "driver_disposition",
                      "claim_id", "researcher_id", "terminal_scope", "terminal_candidate",
                      "execution_cohort_id", "execution_lane_id"):
            with self.subTest(field=field):
                self.assertEqual(reduce([reconciliation(**{field: "forbidden"})])["dispatch_state"], "BLOCKED")

    def test_evidence_requires_pins_and_immutable_url(self):
        for field, val in (("repository", "another/repo"), ("commit", "main"),
                           ("path", "../return.md"), ("path", "/return.md"),
                           ("path", "a%2fb.md"), ("git_blob_sha1", "x" * 40), ("sha256", "x" * 64)):
            a = reconciliation(); a["source_evidence"][field] = val
            with self.subTest(field=field, val=val):
                self.assertEqual(reduce([a])["dispatch_state"], "BLOCKED")
        self.assertEqual(reduce([reconciliation(progress_ref="https://github.com/awdawmip/enterprise-math/blob/main/return.md")])["dispatch_state"], "BLOCKED")

    def test_malformed_scope_does_not_grant_permission(self):
        for scope in (None, "PASS", "DONE", "AWAITING_REVIEW", ""):
            self.assertEqual(reduce([reconciliation(scope)])["dispatch_state"], "BLOCKED")

    def test_empty_next_action_rejected(self):
        self.assertEqual(reduce([reconciliation(next_action=" ")])["dispatch_state"], "BLOCKED")

    def test_untyped_event_frontier_is_blocked_even_without_migration(self):
        t = task(base_state="READY", evidence_status="REGISTERED_TASK")
        c = event("CLAIM", at="2026-09-03T00:00:00+00:00", claim_id="old")
        h = event("HANDOFF", at="2026-09-03T00:01:00+00:00", claim_id="old", progress_ref="durable-return", next_action="review")
        h["_github"]["comment_id"] = 1002
        s = reduce([c, h], t=t)
        self.assertEqual(s["dispatch_state"], "BLOCKED")
        self.assertEqual(s["hard_block"]["source_handoff"]["server_comment_id"], 1002)

    def test_typed_continuation_and_frozen_handoffs_unchanged(self):
        t = task(base_state="READY", evidence_status="REGISTERED_TASK")
        c = event("CLAIM", at="2026-09-17T04:01:00+00:00", claim_id="real")
        for scope, expected in ((rr.HANDOFF_SCOPE_CONTINUATION, "NEEDS_DISPATCH"),
                                (rr.HANDOFF_SCOPE_FROZEN_RETURN, "AWAITING_REVIEW")):
            h = event("HANDOFF", claim_id="real", handoff_scope=scope, next_action="declared next step")
            self.assertEqual(reduce([c, h], t=t)["dispatch_state"], expected)

    def test_legacy_typed_terminal_marker_preserved(self):
        t = task(base_state="READY", evidence_status="REGISTERED_TASK")
        c = event("CLAIM", at="2026-09-03T00:00:00+00:00", claim_id="old")
        h = event("HANDOFF", at="2026-09-03T00:01:00+00:00", claim_id="old",
                  terminal_candidate="SUCCESS_REVIEW_COMPLETE_AWAITING_DRIVER_DECISION", next_action="review")
        self.assertEqual(reduce([c, h], t=t)["dispatch_state"], "AWAITING_REVIEW")

    def test_foreign_claim_handoff_cannot_change_scope(self):
        t = task(base_state="READY", evidence_status="REGISTERED_TASK")
        c = event("CLAIM", at="2026-09-17T04:01:00+00:00", claim_id="real")
        h = event("HANDOFF", claim_id="foreign", next_action="review")
        self.assertEqual(reduce([c, h], t=t)["claim_id"], "real")

    def test_no_empty_event_stream_claims_live_dispatch(self):
        # Pure reducer test only: live selection must still use the authorized loader.
        self.assertIsNone(reduce([reconciliation()])["claim_id"])

    def test_unrelated_fresh_task_remains_selectable(self):
        old = reduce(); old.update(kind="RESEARCH", priority="P0", leverage="HIGH")
        fresh = reduce(t=task(task_id="RS-FRESH", base_state="READY"))
        fresh.update(kind="RESEARCH", priority="P2", leverage="MEDIUM")
        policy = {"selection_policy": {"state_order": ["HANDOFF_READY", "READY"],
                  "priority_order": ["P0", "P1", "P2", "P3"],
                  "leverage_order": ["HIGH", "MEDIUM", "LOW"]}}
        self.assertEqual(rr.select_state([old, fresh], policy)["task_id"], "RS-FRESH")

    def test_input_records_not_mutated(self):
        t = task(); e = reconciliation(); before = copy.deepcopy((t, e))
        reduce([e], t=t)
        self.assertEqual((t, e), before)

    def test_operational_review_reopen_allows_a_new_owner(self):
        from control_plane.research_handoff_scope_runtime import definition_for_result
        t = definition_for_result(task(), {"state": "RETURN_TO_EXECUTION",
            "review": {"reviewed_at": "2026-09-17T04:05:00+00:00"}})
        s = reduce([event("CLAIM", claim_id="review-authorized")], t=t)
        self.assertEqual(s["claim_id"], "review-authorized")
        self.assertEqual(s["dispatch_state"], "LEASED")

    def test_reopen_does_not_allow_an_earlier_claim(self):
        from control_plane.research_handoff_scope_runtime import definition_for_result
        t = definition_for_result(task(), {"state": "RETURN_TO_EXECUTION",
            "review": {"reviewed_at": "2026-09-17T04:15:00+00:00"}})
        self.assertIsNone(reduce([event("CLAIM", claim_id="too-early")], t=t)["claim_id"])

    def test_reopen_is_an_edge_not_permanent_permission(self):
        from control_plane.research_handoff_scope_runtime import definition_for_result
        t = definition_for_result(task(), {"state": "RETURN_TO_EXECUTION",
            "review": {"reviewed_at": "2026-09-17T04:05:00+00:00"}})
        c = event("CLAIM", claim_id="real")
        h = event("HANDOFF", at="2026-09-17T04:11:00+00:00", claim_id="real",
                  progress_ref="another-return", next_action="review")
        c2 = event("CLAIM", at="2026-09-17T04:12:00+00:00", claim_id="bad-repeat")
        self.assertEqual(reduce([c, h, c2], t=t)["dispatch_state"], "BLOCKED")

    def test_task_cannot_forge_a_review_reopen_flag(self):
        from control_plane.research_handoff_scope_runtime import definition_for_result, REOPEN_KEY
        for result in (None, {"state": "AWAITING_DRIVER_REVIEW"}, {"state": "TERMINAL"},
                       {"state": "WITHHELD_CONTROL_AUTHORITY"},
                       {"state": "RETURN_TO_EXECUTION", "review": {}}):
            with self.subTest(result=result):
                t = definition_for_result(task(**{REOPEN_KEY: "2026-09-17T00:00:00+00:00"}), result)
                self.assertNotIn(REOPEN_KEY, t)
                self.assertEqual(reduce([event("CLAIM", claim_id="forged")], t=t)["dispatch_state"], "BLOCKED")

    def test_adapter_preserves_original_definition(self):
        from control_plane.research_handoff_scope_runtime import definition_for_result
        t = task(); before = copy.deepcopy(t)
        definition_for_result(t, {"state": "RETURN_TO_EXECUTION", "review": {"reviewed_at": "2026-09-17T04:05:00+00:00"}})
        self.assertEqual(t, before)

    def test_bootstrap_installs_reopen_adapter_before_parent_gate(self):
        text = (ROOT / "control_plane/research_control_bootstrap.py").read_text()
        self.assertLess(text.index("    research_handoff_scope_runtime.install(root)"),
                        text.index("    research_parent_objective_dispatch_gate.install(root)"))

    def test_event_transport_must_be_raw_json(self):
        body = json.dumps(reconciliation())
        self.assertIsInstance(json.loads(body), dict)
        for malformed in ("```json\n" + body + "\n```", body + "\nExplanation"):
            with self.assertRaises(json.JSONDecodeError):
                json.loads(malformed)


if __name__ == "__main__":
    unittest.main(verbosity=2)
