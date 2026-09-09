"""Typed release evidence must survive current-source and runtime changes."""
from __future__ import annotations

import copy
import hashlib
import json
from contextlib import ExitStack, nullcontext
import unittest
from unittest import mock

import research_control_dispatch as router
import research_driver_authority
import research_driver_followup
from control_plane import research_dependency_release as release
from control_plane import researcher_startup_packet as startup
from tests import test_assigned_research_task_dispatch as fixture_module
from tests.test_assigned_research_task_dispatch import DRIVER, NOW, PARENT, PUB, RESEARCHER, TASK
from tests.test_research_driver_authority import record, write_json
from tests.test_research_task_record_compatibility import _write_current_record
from tools import research_result_records, research_taskbook


class ResearchDependencyReleaseTests(unittest.TestCase):
    def setUp(self):
        self.fx = fixture_module.AssignedResearchTaskDispatchTests()
        self.fx.setUp()
        self.addCleanup(self.fx.doCleanups)
        self.root = self.fx.root
        self.dep = "GV-DEPENDENCY-ARTIFACT-REVIEW"
        self.dep_pub = "TP2-DEPENDENCY-ARTIFACT-REVIEW"
        self.result_task = "RS-DEPENDENCY-COMPLETED-ARTIFACT"
        self.result_pub = "TP2-DEPENDENCY-COMPLETED-ARTIFACT"
        self.rid, self.drid, self.fuid = "RR-DEPENDENCY-FIXTURE", "DR-DEPENDENCY-FIXTURE", "DFU-DEPENDENCY-FIXTURE"
        self.dep_publication = self.publish(self.dep, self.dep_pub, kind="GOVERNANCE")
        self.publish(self.result_task, self.result_pub)
        self.dependencies = [{"task_id": self.dep, "required_artifact": "Accepted exact artifact review"}]
        self.set_dependencies(self.dependencies)

        self.result_path = f"research_result_records/{self.result_task}/{self.rid}.json"
        self.review_path = f"research_result_reviews/{self.rid}/{self.drid}.json"
        self.followup_path = f"research_driver_followups/{self.drid}/{self.fuid}.json"
        self.result = {"result_id": self.rid, "task_id": self.result_task, "publication_id": self.result_pub,
                       "frozen_at": "2026-09-09T10:30:00Z", "_record_path": self.result_path}
        write_json(self.root / self.result_path, {key: value for key, value in self.result.items() if not key.startswith("_")})
        digest = self.digest(self.result_path)
        self.review = {
            "review_id": self.drid, "result_id": self.rid, "task_id": self.result_task,
            "publication_id": self.result_pub, "result_record_path": self.result_path,
            "result_record_sha256": digest, "review_authority_kind": "IMMUTABLE_REVIEW",
            "disposition": "ACCEPTED", "reviewed_at": "2026-09-09T11:05:00Z", "_review_path": self.review_path,
        }
        write_json(self.root / self.review_path, {key: value for key, value in self.review.items() if not key.startswith("_")})
        self.packet = {
            "packet_id": self.fuid, "review_id": self.drid, "result_id": self.rid,
            "review_disposition": "ACCEPTED", "source_result_record_sha256": digest,
            "source_publication_id": self.result_pub, "task_id": self.result_task,
            "created_at": "2026-09-09T11:06:00Z",
        }
        write_json(self.root / self.followup_path, self.packet)
        self.result_state = {"state": "TERMINAL", "terminal": True, "result": self.result, "review": self.review}
        self.followup_state = {"ready": True, "required": True, "packet": self.packet}
        self.gate = {"canonical_main": "a" * 40, "result_id": self.rid,
                     "result_record_sha256": digest, "review_id": self.drid, "followup_id": self.fuid}
        self.review_ref = f"https://github.com/awdawmip/enterprise-math/blob/{'a' * 40}/{self.review_path}"
        self.raw_release = self.fx.comment(
            9050, event="UNBLOCK", at="2026-09-09T11:30:00Z",
            review_obligation_task_id=self.dep, review_obligation_publication_id=self.dep_pub,
            gate_evidence=self.gate, progress_ref=self.review_ref)
        self.raw = [self.raw_release, self.fx.raw_assignment]
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        self.stack.enter_context(mock.patch.object(
            research_result_records, "result_map", return_value={self.rid: self.result}))
        self.stack.enter_context(mock.patch.object(
            research_result_records, "task_result_state",
            side_effect=lambda task_id, *args, **kwargs: self.result_state if task_id == self.result_task else None))
        self.stack.enter_context(mock.patch.object(
            research_driver_followup, "state_for_review", side_effect=lambda *args, **kwargs: self.followup_state))
        self.stack.enter_context(mock.patch.object(
            router.research_dispatch, "_dispatch_result_read_snapshot", return_value=nullcontext()))

    def publish(self, task, pub, *, kind="RESEARCH"):
        return _write_current_record(
            self.root, task_id=task, publication_id=pub, parent_objective_id=PARENT,
            kind=kind, owner="taskbook/unassigned", claimable=True,
            published_at="2026-09-09T10:00:00Z")

    def set_dependencies(self, dependencies, *, base_state="BLOCKED"):
        meta, body = research_taskbook.split_taskbook(self.fx.book.read_text(encoding="utf-8"))
        meta.update(dependencies=copy.deepcopy(dependencies), base_state=base_state,
                    hard_block={"missing_object": "exact review", "owner": DRIVER,
                                "necessity": "required artifact", "unblock_condition": "accepted exact artifact"})
        self.fx.book.write_text(research_taskbook.render_taskbook(meta, body), encoding="utf-8")
        self.fx.publication["taskbook_blob_sha1"] = router.research_task_records.taskbook_blob(self.fx.book)
        self.fx.publication["dependencies"] = copy.deepcopy(dependencies)
        write_json(self.fx.publication_path, self.fx.publication)

    def digest(self, relative):
        return "sha256:" + hashlib.sha256((self.root / relative).read_bytes()).hexdigest()

    def definition(self):
        return next(row for row in router.research_dispatch.merged_definitions(self.root) if row["task_id"] == TASK)

    def proof(self, raw=None):
        return release.resolve(
            self.definition(), self.fx.events(self.raw if raw is None else raw), now=NOW, root=self.root)

    def change_release(self, **changes):
        body = json.loads(self.raw_release["body"])
        body.update(changes)
        changed = copy.deepcopy(self.raw_release)
        changed["body"] = json.dumps(body)
        return changed

    def test_applied_release_selects_task_and_keeps_complete_obligation_evidence(self):
        before = self.fx.book.read_bytes()
        result = self.fx.route(comments=self.raw, real_reducer=True)
        self.assertEqual(result["action"], "CLAIM_NEW_OWNER")
        self.assertEqual(result["selection_status"], "ELIGIBLE")
        proof = result["dependency_release_evidence"]
        self.assertEqual(proof["release_comment_id"], 9050)
        self.assertEqual(proof["obligations"][0]["task_id"], self.dep)
        self.assertEqual(proof["obligations"][0]["result_id"], self.rid)
        self.assertEqual(result["assigned_research_selection"]["dependency_release"], release.compact(proof))
        self.assertFalse(proof["execution_authorized"])
        self.assertFalse(proof["claim_created"])
        self.assertFalse(result["assigned_research_selection"]["execution_authorized"])
        self.assertIsNone(result["target"]["claim_id"])
        self.assertEqual(self.fx.book.read_bytes(), before)
        packet = startup.build_packet({"route": result, "request_id": "dependency-release-fixture",
                                       "source_sha": "a" * 40, "kind": "RESEARCH"}, self.root)
        self.assertEqual(packet["assigned_research_selection"]["dependency_release"], release.compact(proof))
        self.assertNotIn("dependency_release_evidence", packet)
        self.assertLessEqual(packet["packet_bytes"], 8192)

    def test_ready_result_and_prose_alone_cannot_release_dependency(self):
        with self.assertRaisesRegex(release.DependencyReleaseError, "applied UNBLOCK"):
            self.proof(raw=[self.fx.raw_assignment])
        body = json.loads(self.raw_release["body"])
        for key in ("review_obligation_task_id", "review_obligation_publication_id", "gate_evidence"):
            body.pop(key)
        body["reason"] = "All dependencies are ACCEPTED and ready."
        raw = copy.deepcopy(self.raw_release)
        raw["body"] = json.dumps(body)
        with self.assertRaisesRegex(release.DependencyReleaseError, "complete typed"):
            self.proof(raw=[raw])

    def test_ignored_unblock_on_already_ready_task_is_not_a_release_proof(self):
        self.set_dependencies(self.dependencies, base_state="READY")
        with self.assertRaisesRegex(release.DependencyReleaseError, "applied UNBLOCK"):
            self.proof()

    def test_edited_or_wrong_actor_release_is_not_authority(self):
        for change in (
            {"updated_at": "2026-09-09T11:31:00Z"},
            {"user": {"login": "unknown", "id": 99}, "author_association": "NONE"},
        ):
            with self.subTest(change=change):
                raw = {**copy.deepcopy(self.raw_release), **change}
                with self.assertRaises(release.DependencyReleaseError):
                    self.proof(raw=[raw])

    def test_wrong_target_generation_and_future_release_fail_closed(self):
        raw = self.change_release(publication_id="TP2-OTHER-GENERATION")
        with self.assertRaises(release.DependencyReleaseError):
            self.proof(raw=[raw])
        raw = copy.deepcopy(self.raw_release)
        raw["created_at"] = raw["updated_at"] = "2026-09-09T14:00:00Z"
        with self.assertRaisesRegex(release.DependencyReleaseError, "clock"):
            self.proof(raw=[raw])

    def test_source_definition_or_obligation_publication_drift_is_rejected(self):
        definition = self.definition()
        definition["dependencies"] = [{"task_id": self.dep, "required_artifact": "different scope"}]
        with self.assertRaisesRegex(release.DependencyReleaseError, "current task definition"):
            release.resolve(definition, self.fx.events(self.raw), now=NOW, root=self.root)
        raw = self.change_release(review_obligation_publication_id="TP2-OLDER-OBLIGATION")
        with self.assertRaisesRegex(release.DependencyReleaseError, "current operational publication"):
            self.proof(raw=[raw])

    def test_taskbook_and_raw_result_tampering_invalidate_release(self):
        dep_book = self.root / self.dep_publication["taskbook_path"]
        dep_book.write_bytes(dep_book.read_bytes() + b"\nchanged\n")
        with self.assertRaises(release.DependencyReleaseError):
            self.proof()

    def test_raw_result_digest_is_checked_against_unchanged_accepted_view(self):
        (self.root / self.result_path).write_bytes((self.root / self.result_path).read_bytes() + b"\n")
        with self.assertRaisesRegex(release.DependencyReleaseError, "raw Result bytes"):
            self.proof()

    def test_withheld_or_replaced_result_cannot_use_historical_acceptance(self):
        for change in (
            {"state": "AWAITING_DRIVER_REVIEW", "terminal": False},
            {"result": {**self.result, "result_id": "RR-NEWER-RESULT"}},
        ):
            with self.subTest(change=change):
                old = copy.deepcopy(self.result_state)
                self.result_state.update(change)
                with self.assertRaisesRegex(release.DependencyReleaseError, "current terminal"):
                    self.proof()
                self.result_state.clear()
                self.result_state.update(old)

    def test_nonaccepted_review_or_unready_followup_is_rejected(self):
        self.review["disposition"] = "PARKED"
        with self.assertRaisesRegex(release.DependencyReleaseError, "accepted immutable"):
            self.proof()
        self.review["disposition"] = "ACCEPTED"
        self.followup_state["ready"] = False
        with self.assertRaisesRegex(release.DependencyReleaseError, "follow-up"):
            self.proof()

    def test_review_binding_and_source_link_cannot_point_elsewhere(self):
        self.review["result_record_sha256"] = "sha256:" + "0" * 64
        with self.assertRaisesRegex(release.DependencyReleaseError, "accepted immutable"):
            self.proof()
        self.review["result_record_sha256"] = self.gate["result_record_sha256"]
        with self.assertRaisesRegex(release.DependencyReleaseError, "source link"):
            self.proof(raw=[self.change_release(progress_ref=self.review_ref + ".other")])

    def test_future_review_or_followup_cannot_backfill_old_release(self):
        self.review["reviewed_at"] = "2026-09-09T11:40:00Z"
        with self.assertRaisesRegex(release.DependencyReleaseError, "postdates"):
            self.proof()
        self.review["reviewed_at"] = "2026-09-09T11:05:00Z"
        self.packet["created_at"] = "2026-09-09T11:40:00Z"
        with self.assertRaisesRegex(release.DependencyReleaseError, "postdates"):
            self.proof()

    def test_driver_authority_is_checked_at_release_time(self):
        newer = record(comment_id=9300, created="2026-09-09T12:35:00Z")
        path = self.root / "research_driver_authority_records" / DRIVER / (newer["authority_record_id"] + ".json")
        write_json(path, newer)
        self.assertEqual(self.proof()["release_driver_authority_record_id"], self.fx.authority["authority_record_id"])
        revoked = record(event="REVOKE", comment_id=9040, created="2026-09-09T11:20:00Z")
        write_json(path.parent / (revoked["authority_record_id"] + ".json"), revoked)
        with self.assertRaisesRegex(release.DependencyReleaseError, "authority active"):
            self.proof()

    def test_multiple_obligations_require_exact_complete_typed_coverage(self):
        second, second_pub = "GV-DEPENDENCY-SECOND-REVIEW", "TP2-DEPENDENCY-SECOND-REVIEW"
        self.publish(second, second_pub, kind="GOVERNANCE")
        self.set_dependencies(self.dependencies + [{"task_id": second, "required_artifact": "Second declared artifact"}])
        with self.assertRaisesRegex(release.DependencyReleaseError, "complete typed"):
            self.proof()
        body = json.loads(self.raw_release["body"])
        for key in ("review_obligation_task_id", "review_obligation_publication_id", "gate_evidence"):
            body.pop(key)
        entries = [{"task_id": task, "publication_id": pub, "gate_evidence": self.gate,
                    "review_ref": self.review_ref} for task, pub in ((self.dep, self.dep_pub), (second, second_pub))]
        body["dependency_gate_evidence"] = entries
        raw = copy.deepcopy(self.raw_release)
        raw["body"] = json.dumps(body)
        self.assertEqual(len(self.proof(raw=[raw])["obligations"]), 2)
        for wrong in (entries[:1], [entries[0], entries[0]]):
            body["dependency_gate_evidence"] = wrong
            raw["body"] = json.dumps(body)
            with self.assertRaisesRegex(release.DependencyReleaseError, "exactly once"):
                self.proof(raw=[raw])

    def test_duplicate_envelope_is_not_two_release_witnesses(self):
        with self.assertRaisesRegex((release.DependencyReleaseError, router.research_dispatch.DispatchError), "duplicate"):
            self.proof(raw=[self.raw_release, self.raw_release])

    def test_reblock_and_later_untyped_release_invalidate_earlier_proof(self):
        claim = self.fx.comment(
            9400, event="CLAIM", at="2026-09-09T12:05:00Z", claim_id="fixture-live-claim",
            theorem_owner="fixture-owner", execution_branch="research/fixture-release",
            execution_branch_base="b" * 40, allowed_outputs=["research_returns/fixture.md"], lease_minutes=120)
        block = self.fx.comment(
            9401, event="HARD_BLOCK", at="2026-09-09T12:06:00Z", claim_id="fixture-live-claim",
            hard_block={"missing_object": "new prerequisite", "owner": DRIVER,
                        "necessity": "new dependency event", "unblock_condition": "new accepted input"})
        with self.assertRaisesRegex(release.DependencyReleaseError, "new block"):
            self.proof(raw=self.raw + [claim, block])
        untyped = self.fx.comment(9402, event="UNBLOCK", at="2026-09-09T12:07:00Z")
        with self.assertRaisesRegex(release.DependencyReleaseError, "complete typed"):
            self.proof(raw=self.raw + [claim, block, untyped])


if __name__ == "__main__":
    unittest.main()
