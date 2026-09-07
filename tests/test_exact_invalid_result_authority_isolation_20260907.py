"""Exact Result isolation through real registries, public reduction and guard."""
from __future__ import annotations

import copy
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import timedelta
from pathlib import Path

from control_plane import research_control_bootstrap as bootstrap
from control_plane import research_result_authority_fault_isolation as isolation
from control_plane import research_result_records_impl as impl
from control_plane import research_runtime_guard_core as guard_core
from tools import research_dispatch as dispatch
from tools import research_result_records as results
from tools import research_runtime_guard as guard
from tools import research_runtime_reducer as reducer
from tools import research_task_records as publications
from test_research_runtime_claim_authority import auth, state as runtime_state
from test_research_task_record_compatibility import _write_current_record, _write_semantic_fixture

ROOT = Path(__file__).resolve().parents[1]
RID = "RR-012E775840E54D36F41E"


def setUpModule():
    bootstrap.install(ROOT)


class ExactInvalidResultAuthorityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.row = copy.deepcopy(isolation.quarantine_rows(ROOT)[RID])
        for pin in self.row["dependency_pins"]:
            target = self.root / pin["path"]
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / pin["path"], target)
        self.save_registry()
        _write_semantic_fixture(self.root)
        self.task_id = self.row["task_id"]
        self.pub_id = self.row["publication_id"]
        self.rr = self.load(self.row["record_path"])
        self.pub = self.load(self.row["publication_record_path"])
        self.before = {x["path"]: (self.root / x["path"]).read_bytes() for x in self.row["dependency_pins"]}
        self.freeze = reducer.parse_time(self.rr["frozen_at"])

    def load(self, relative):
        return json.loads((self.root / relative).read_text(encoding="utf-8"))

    def save(self, relative, value):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")

    def save_registry(self):
        self.save(isolation.QUARANTINE_FILE, {
            "schema": isolation.SCHEMA, "status": "ACTIVE", "entries": [self.row],
        })

    def assert_rejected(self, text):
        with self.assertRaisesRegex(isolation.ResultAuthorityIsolationError, text):
            isolation.validated_rows(self.root)

    def state(self, scope=None):
        value = runtime_state()
        value["task"]["task_id"] = self.task_id
        value["task_registration"]["registry_key"] = self.task_id
        value["parent_objective"]["objective_id"] = self.pub["parent_objective_id"]
        if scope:
            value["execution_scope"] = scope
        return value

    def claim(self, *, after=False, publication=None, lane=None):
        timestamp = (self.freeze + timedelta(minutes=1 if after else -1)).isoformat()
        meta = auth(8702 if after else 8701)
        meta.update(created_at=timestamp, updated_at=timestamp)
        event = {
            "schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V1", "event": "CLAIM",
            "task_id": self.task_id, "publication_id": publication or self.pub_id,
            "actor": "historical-owner", "at": timestamp, "claim_id": "fixture-owner",
            "researcher_id": "EM-FIXTURE-ABC123", "theorem_owner": "FIXTURE",
            "execution_branch": "research/result-authority-fixture", "execution_branch_base": "b" * 40,
            "allowed_outputs": ["research_returns/"], "lease_minutes": 120, "_github": meta,
        }
        if lane:
            event.update(execution_cohort_id="EC-FIXTURE", execution_lane_id=lane,
                         allowed_outputs=[f"research_returns/parallel/EC-FIXTURE/{lane}/"])
        return event

    def cohort(self, *, mixed=False, other_only=False):
        other = self.pub["supersedes_publication_id"]
        if mixed or other_only:
            _write_current_record(self.root, task_id=self.task_id, publication_id=other,
                                  parent_objective_id=self.pub["parent_objective_id"], claimable=True)
        lanes = []
        if not other_only:
            lanes.append({"lane_id": "held", "publication_id": self.pub_id, "lane_role": "AUDIT",
                          "purpose": "exact held lane", "output_prefix": "research_returns/parallel/EC-FIXTURE/held/"})
        if mixed or other_only:
            lanes.append({"lane_id": "independent", "publication_id": other, "lane_role": "AUDIT",
                          "purpose": "retained independent lane", "output_prefix": "research_returns/parallel/EC-FIXTURE/independent/"})
        if len(lanes) == 1:
            lanes.append({**lanes[0], "lane_id": "second", "output_prefix": "research_returns/parallel/EC-FIXTURE/second/"})
        self.save(f"research_execution_cohorts/{self.task_id}/EC-FIXTURE.json", {
            "schema": "ENTERPRISE_MATH_PARALLEL_EXECUTION_COHORT_V1", "task_id": self.task_id,
            "cohort_id": "EC-FIXTURE", "record_state": "ACTIVE", "opened_by": "EM-DVR-ABC123",
            "opened_at": self.freeze.isoformat(), "lanes": lanes,
            "two_reference_passes_required": True, "synthesis_required": True,
            "working_truth_granted": False, "canonical_promotion_granted": False,
        })
        return other

    def clean_sibling(self, *, independent=True):
        value = copy.deepcopy(self.rr)
        value.update(result_id="RR-FIXTURE-CLEAN", method_harvest="NO_TOOL_PAYLOAD",
                     independence_status="NOT_APPLICABLE", source_exposure_status="NOT_APPLICABLE")
        if independent:
            value.update(execution_record_id="ER-FIXTURE-CLEAN", claim_id="claim-clean",
                         researcher_id="EM-CLEAN-ABC123", execution_branch="research/independent")
            execution = self.load(self.row["execution_record_path"])
            execution.update({key: value[key] for key in ("execution_record_id", "claim_id", "researcher_id", "execution_branch")})
            self.save(f"research_execution_records/{self.task_id}/ER-FIXTURE-CLEAN.json", execution)
        self.save(f"research_result_records/{self.task_id}/RR-FIXTURE-CLEAN.json", value)
        return value

    def test_exact_record_and_dependency_bytes_are_preserved(self):
        self.assertEqual({RID}, set(isolation.validated_rows(self.root)))
        self.assertEqual([], results.iter_results(self.root))
        self.assertEqual([], results.iter_reviews(self.root))
        self.assertEqual(self.before, {p: (self.root / p).read_bytes() for p in self.before})

    def test_schema_flags_and_noncanonical_paths_fail_closed(self):
        original = copy.deepcopy(self.row)
        for key, value in (("terminality_granted", True), ("record_path", "../outside.json"),
                           ("execution_identity_basis", "GENERIC_RECORD_ID_ALIAS")):
            with self.subTest(key=key):
                self.row = {**copy.deepcopy(original), key: value}
                self.save_registry()
                with self.assertRaises(isolation.ResultAuthorityIsolationError):
                    isolation.validated_rows(self.root)

    def test_same_error_text_with_changed_dependency_bytes_is_rejected(self):
        book = self.root / self.rr["taskbook_path"]
        book.write_bytes(book.read_bytes() + b"\nExtra immutable-byte drift.\n")
        rr = {**self.rr, "_record_path": self.row["record_path"]}
        strict = impl.audit_result_record(rr, self.load(self.row["execution_record_path"]), self.root)
        self.assertEqual([self.row["record_path"] + ": " + x for x in self.row["allowed_result_audit_errors"]], strict)
        self.assert_rejected("exact dependency byte drift")

    def test_complete_dependency_set_rejects_omission(self):
        self.row["dependency_pins"] = [x for x in self.row["dependency_pins"] if x["path"] != self.rr["taskbook_path"]]
        self.save_registry()
        self.assert_rejected("dependency set incomplete")

    def test_complete_strict_error_set_rejects_missing_and_extra(self):
        original = list(self.row["allowed_result_audit_errors"])
        for errors in (original[:-1], original + ["unregistered extra fault"]):
            self.row["allowed_result_audit_errors"] = errors
            self.save_registry()
            self.assert_rejected("complete raw strict error set drift")

    def test_stale_suppression_and_unregistered_extra_error_survive(self):
        exact = [self.row["record_path"] + ": " + x for x in self.row["allowed_result_audit_errors"]]
        self.assertEqual([], isolation.audit_against(exact, self.root))
        self.assertEqual(["outside: extra"], isolation.audit_against(exact + ["outside: extra"], self.root))
        self.assertTrue(any("stale or unused" in x for x in isolation.audit_against(exact[:-1], self.root)))

    def test_duplicate_and_alternate_path_result_are_rejected(self):
        for relative in (f"research_result_records/{self.task_id}/DUPLICATE.json", f"research_result_records/RS-OTHER/{RID}.json"):
            with self.subTest(path=relative):
                self.save(relative, self.rr)
                self.assert_rejected("complete raw Result source path set drift")
                (self.root / relative).unlink()

    def test_extra_or_missing_review_source_is_rejected(self):
        review_row = self.row["derived_reviews"][0]
        original = self.load(review_row["review_record_path"])
        self.save(f"research_result_reviews/{RID}/DR-EXTRA.json", {**original, "review_id": "DR-EXTRA"})
        self.assert_rejected("complete derived review source set drift")

    def test_snapshot_cannot_authorize_after_dependency_or_store_addition(self):
        for mutation in ("dependency", "duplicate"):
            with self.subTest(mutation=mutation):
                with self.assertRaisesRegex(isolation.ResultAuthorityIsolationError, "snapshot inputs changed"):
                    with isolation.authority_snapshot(self.root):
                        self.assertIn(RID, isolation.validated_rows(self.root))
                        if mutation == "dependency":
                            path = self.root / self.rr["taskbook_path"]
                            path.write_bytes(path.read_bytes() + b"\n")
                        else:
                            self.save(f"research_result_records/RS-OTHER/{RID}.json", self.rr)
                if mutation == "dependency":
                    path.write_bytes(self.before[self.rr["taskbook_path"]])
                else:
                    (self.root / f"research_result_records/RS-OTHER/{RID}.json").unlink()

    def test_exact_generation_withheld_is_nonterminal_without_fake_result(self):
        value = results.task_result_state(self.task_id, self.root, self.pub_id)
        self.assertEqual(isolation.STATE, value["state"])
        self.assertFalse(value["terminal"])
        self.assertIsNone(value["result"])
        self.assertIsNone(value["review"])
        self.assertEqual(self.rr["claim_id"], value["historical_execution_claims"][0]["claim_id"])
        self.assertIsNone(results.task_result_state(self.task_id, self.root, "TP2-OTHER"))

    def test_valid_independent_sibling_remains_operational(self):
        sibling = self.clean_sibling()
        self.assertEqual([], impl.audit_result_record(sibling, impl.execution_map(self.root)[sibling["execution_record_id"]], self.root))
        self.assertEqual({sibling["result_id"]}, set(results.result_map(self.root)))
        value = results.task_result_state(self.task_id, self.root, self.pub_id)
        self.assertEqual("AWAITING_DRIVER_REVIEW", value["state"])
        self.assertEqual(sibling["result_id"], value["result"]["result_id"])

    def test_new_current_generation_does_not_inherit_historical_hold(self):
        _write_current_record(self.root, task_id=self.task_id, publication_id="TP2-NEW-CURRENT",
                              parent_objective_id=self.pub["parent_objective_id"], claimable=True,
                              publication_generation=3, supersedes_publication_id=self.pub_id)
        self.assertEqual("TP2-NEW-CURRENT", publications.current_records(self.root)[self.task_id]["publication_id"])
        self.assertIsNone(results.task_result_state(self.task_id, self.root))
        self.assertEqual(isolation.STATE, results.task_result_state(self.task_id, self.root, self.pub_id)["state"])

    def test_no_current_publication_cannot_fall_back_to_held_history(self):
        self.save(self.row["publication_record_path"], {**self.pub, "record_state": "CLOSED"})
        data = (self.root / self.row["publication_record_path"]).read_bytes()
        blob, sha = isolation._digests(data)
        self.row["publication_record_blob_sha1"] = blob
        for pin in self.row["dependency_pins"]:
            if pin["path"] == self.row["publication_record_path"]:
                pin.update(git_blob_sha1=blob, sha256=sha)
        self.save_registry()
        self.assertNotIn(self.task_id, publications.current_records(self.root))
        self.assertIsNone(results.task_result_state(self.task_id, self.root))
        self.assertEqual(isolation.STATE, results.task_result_state(self.task_id, self.root, self.pub_id)["state"])

    def test_same_execution_copy_cannot_replace_without_normal_contract(self):
        self.clean_sibling(independent=False)
        with self.assertRaisesRegex(isolation.ResultAuthorityIsolationError, "validated replacement authority"):
            results.iter_results(self.root)

    def test_history_claim_survives_but_dispatch_and_real_public_guard_block(self):
        task = dispatch.registered_definition(self.pub, self.root)
        old, new = self.claim(), self.claim(after=True)
        events = [old, new]
        for index, kind in enumerate(("HANDOFF", "DONE", "UNBLOCK"), 2):
            event = {**new, "event": kind, "_github": {**new["_github"], "comment_id": 8702 + index}}
            events.append(event)
        value = results.task_result_state(self.task_id, self.root, self.pub_id)
        authenticated, rejected = dispatch._filter_registered_events(task, events, self.root, value)
        self.assertEqual([old["_github"]["comment_id"]], [x["_github"]["comment_id"] for x in authenticated])
        reduced = dispatch.reduce_definition(task, [old], now=self.freeze + timedelta(minutes=2), root=self.root)
        self.assertEqual("BLOCKED", reduced["dispatch_state"])
        self.assertEqual(old["claim_id"], reduced["claim_id"])
        self.assertFalse(reduced["terminal"])
        for operation in (
            lambda: guard.authorize_execution(self.state(), events=[old], now=self.freeze, root=self.root),
            lambda: guard.canonical_live_claim_binding(self.task_id, [old], now=self.freeze, root=self.root),
            lambda: guard.adopt_stale_session(self.state(), {}, replacement_session_id="s2", events=[old], now=self.freeze, root=self.root),
        ):
            with self.assertRaisesRegex(guard.RuntimeAuthorizationError, isolation.STATE):
                operation()

    def test_same_publication_cohort_cannot_override_hold_or_authorize_lane(self):
        self.cohort()
        task = dispatch.registered_definition(self.pub, self.root)
        value = dispatch.reduce_definition(task, [], now=self.freeze, root=self.root)
        self.assertEqual("BLOCKED", value["dispatch_state"])
        scope = {"execution_cohort_id": "EC-FIXTURE", "execution_lane_id": "held"}
        with self.assertRaisesRegex(guard.RuntimeAuthorizationError, isolation.STATE):
            guard.authorize_execution(self.state(scope), events=[self.claim(lane="held")], now=self.freeze, root=self.root)
        with self.assertRaisesRegex(guard.RuntimeAuthorizationError, isolation.STATE):
            guard.adopt_stale_session(self.state(scope), {}, replacement_session_id="s2", events=[], now=self.freeze, root=self.root)

    def test_mixed_cohort_preserves_independent_retained_lane_real_authorization(self):
        other = self.cohort(mixed=True)
        task = dispatch.registered_definition(self.pub, self.root)
        value = dispatch.reduce_definition(task, [], now=self.freeze, root=self.root)
        self.assertEqual("COHORT_ACTIVE", value["dispatch_state"])
        self.assertEqual([self.pub_id], value["withheld_lane_publication_ids"])
        scope = {"execution_cohort_id": "EC-FIXTURE", "execution_lane_id": "independent"}
        event = self.claim(publication=other, lane="independent")
        decision = guard.authorize_execution(self.state(scope), events=[event], now=self.freeze, root=self.root)
        self.assertTrue(decision["authorized"])
        self.assertEqual(other, decision["execution_binding"]["publication_id"])

    def test_repeated_install_keeps_registry_and_original_evidence_unchanged(self):
        before = (self.root / isolation.QUARANTINE_FILE).read_bytes()
        isolation.install(self.root)
        isolation.install(self.root)
        self.assertEqual([], results.iter_results(self.root))
        self.assertEqual([], results.iter_reviews(self.root))
        self.assertEqual(before, (self.root / isolation.QUARANTINE_FILE).read_bytes())
        self.assertEqual(self.before, {p: (self.root / p).read_bytes() for p in self.before})

    def test_fresh_import_order_cannot_restore_result_derived_reviews(self):
        script = """
from pathlib import Path
import sys
from control_plane import research_result_authority_fault_isolation as a
from control_plane import research_control_bootstrap as b
from tools import research_result_records as p
root = Path(sys.argv[1])
a.install(root)
b.install(root)
b.install(root)
held = set(a.validated_rows(root))
assert not held.intersection(item['result_id'] for item in p.iter_results(root))
assert not held.intersection(item['result_id'] for item in p.iter_reviews(root))
assert p.iter_reviews._exact_result_authority_filter is True
"""
        process = subprocess.run([sys.executable, "-c", script, str(ROOT)], cwd=ROOT,
                                 capture_output=True, text=True, encoding="utf-8", timeout=45)
        self.assertEqual(0, process.returncode, process.stdout + process.stderr)


if __name__ == "__main__":
    unittest.main()
