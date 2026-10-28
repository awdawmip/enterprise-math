"""Isolated regression fixtures; no fixture authorizes a real Source write.

The established current-publisher fixture substitutes the Result/review catalog
only. New tests exercise real DA validation, review receipts/independence,
taskbook preflight, exact pins and the native packet/publisher validators.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import shutil
import sys
import unittest
from unittest import mock

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(BASE / "tests"))
from control_plane import research_driver_followup_fault_isolation as isolation
from control_plane import research_driver_followup_transaction as transaction

from test_followup_current_publisher import CurrentPublisherBindingTests, CURRENT, SESSION, CREATED, authorization, write_json
import research_driver_authority as authority
import research_driver_followup as followup
from tools import research_task_records as tasks, research_taskbook as books
from control_plane import research_continuation_write_authority as receipts
from control_plane import research_result_review_audit_fault_isolation as review_audit
from control_plane import research_task_semantic_integrity_fault_isolation as semantic

TASK = "RS-RSA-EXPONENT-COLLISION-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT"
OLD = "TP2-DCBF9A9ACA18BF64FFCF"


class PublicationScopeRepairTests(unittest.TestCase):
    def setUp(self):
        self.fixture = CurrentPublisherBindingTests("runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        for relative in ["research_taskbook_policy.json", "research_taskbook_contract.json"]:
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(BASE / relative, destination)
        write_json(self.root / receipts.CUTOVER, {
            "schema": "ENTERPRISE_MATH_CONTINUATION_RECORD_CUTOVER_V1", "records": {},
        })
        # The full CI shard installs this real wrapper before collecting tests.
        # Its canonical registry must be nonempty. Keep unrelated historical
        # quarantine bytes/pins in the specimen store instead of weakening that
        # validator or pretending an empty registry satisfies its contract.
        registry = BASE / semantic.QUARANTINE_FILE
        payload = json.loads(registry.read_text())
        self.assertTrue(all(row["task_id"] not in {TASK, "RS-OLD"} for row in payload["quarantines"]))
        shutil.copyfile(registry, self.root / semantic.QUARANTINE_FILE)
        for row in payload["quarantines"]:
            for field in ("record_path", "taskbook_path", "source_taskbook_path"):
                destination = self.root / row[field]
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(BASE / row[field], destination)
        source = BASE / f"research_task_records/{TASK}/{OLD}.json"
        self.anchor = json.loads(source.read_text())
        original = self.root / self.anchor["taskbook_path"]
        original.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(BASE / self.anchor["taskbook_path"], original)
        write_json(self.root / f"research_task_records/{TASK}/{OLD}.json", self.anchor)
        self.original_bytes = original.read_bytes()
        meta, body = books.split_taskbook(original.read_text())
        self.meta = copy.deepcopy(meta)
        self.body = body
        self.new_path = self.root / "research_tasks/RSA_PROSPECTIVE_FIXTURE.md"
        self.new_path.write_text(books.render_taskbook(self.meta, body))
        # The specimen reviewed target is independently admitted to the native
        # catalogs by the established fixture. It is not a real RSA Result.
        self.fixture.result.update(publication_id="TP2-OLD", execution_record_id="ER-SPECIMEN",
                                   researcher_id="EM-RES-SPECIMEN", contributor_ids=[], method_harvest="RESULT_ONLY")
        raw_result = {key: value for key, value in self.fixture.result.items() if not key.startswith("_")}
        write_json(self.root / self.fixture.result["_record_path"], raw_result)
        parent_meta = copy.deepcopy(self.meta)
        parent_meta.update(task_id="RS-OLD", registry_key="RS-OLD")
        parent_path = self.root / "research_tasks/SOURCE_SPECIMEN.md"
        parent_path.write_text(books.render_taskbook(parent_meta, body))
        write_json(self.root / "research_task_records/RS-OLD/TP2-OLD.json", {
            "task_id": "RS-OLD", "publication_id": "TP2-OLD", "parent_objective_id": self.meta["parent_objective_id"],
            "record_state": "ACTIVE", "publication_generation": 1,
            "record_schema": tasks.RECORD_SCHEMA, "registry_key": "RS-OLD",
            "taskbook_path": parent_path.relative_to(self.root).as_posix(),
            "taskbook_blob_sha1": tasks.taskbook_blob(parent_path),
            "working_truth_granted": False, "canonical_promotion_granted": False,
        })
        artifact = self.root / "fixtures/prospective-review.md"
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text("Independent specimen review of exact preserved Result.\n")
        review = self.fixture.review
        review.update(record_schema=review_audit.impl.REVIEW_SCHEMA, driver_id=CURRENT, task_id="RS-OLD",
                      publication_id="TP2-OLD", execution_record_id="ER-SPECIMEN", terminal=True,
                      result_record_sha256="sha256:" + hashlib.sha256((self.root / review["result_record_path"]).read_bytes()).hexdigest(),
                      review_path=artifact.relative_to(self.root).as_posix(),
                      review_blob_sha1=isolation._git_blob_sha1(artifact.read_bytes()),
                      review_sha256="sha256:" + hashlib.sha256(artifact.read_bytes()).hexdigest(),
                      driver_authority_record_id=authorization()["authority_record_id"],
                      driver_authority_source_comment_id=901, reviewer_contribution_ids=[])
        self.save_review()
        self.new = tasks.build_record(self.meta, path=self.new_path, publisher_role="RESEARCH_DRIVER",
            publisher_id=CURRENT, research_value=self.anchor["research_value"], published_at=CREATED,
            supersedes_publication_id=OLD, root=self.root)
        self.save_new()
        gates = [{"gate": gate, "decision": "REQUIRED" if gate == "EXTERNAL_PRIOR_ART_DUPLICATION" else "NOT_REQUIRED",
                  "reason": "explicit prospective specimen gate", "evidence_refs": []} for gate in followup.GATES]
        self.packet = followup.build_packet(review_id=review["review_id"], decision="TASK_SET_PUBLISHED",
            gate_decisions=gates, task_publications=[{"task_id": TASK, "publication_id": self.new["publication_id"],
                "task_role": "EXTERNAL_PRIOR_ART_DUPLICATION"}], driver_id=CURRENT, created_at=CREATED,
            publishing_driver_id=CURRENT, publisher_session_id=SESSION, root=self.root)
        self.save_packet()
        self.old_packet = {"task_id": "RS-OLD", "source_publication_id": "TP2-OLD"}
        self.row = {"result_id": self.fixture.result["result_id"]}
        self.task_pin = {"task_id": TASK, "publication_id": OLD,
                         "taskbook_path": self.anchor["taskbook_path"]}

    def save_review(self):
        review = self.fixture.review
        raw = {key: value for key, value in review.items() if not key.startswith("_") and key != "write_authorization"}
        raw["write_authorization"] = receipts.build_receipt(raw, "REVIEW", {
            "source_commit": "3dacc0a07af1c1078795a95552b0a9cd153fb589", "authorized_at": review["reviewed_at"],
            "authority_observed_through_comment_id": 901,
            "principal": {"driver_id": CURRENT, "session_id": SESSION,
                          "authority_record_id": authorization()["authority_record_id"]},
        })
        review["write_authorization"] = raw["write_authorization"]
        write_json(self.root / review["_review_path"], raw)

    def save_new(self):
        write_json(self.root / f"research_task_records/{TASK}/{self.new['publication_id']}.json", self.new)

    def save_packet(self):
        write_json(self.root / f"research_driver_followups/{self.packet['review_id']}/{self.packet['packet_id']}.json", self.packet)

    def refresh_publication_identity(self):
        old_record = self.root / f"research_task_records/{TASK}/{self.new['publication_id']}.json"
        old_packet = self.root / f"research_driver_followups/{self.packet['review_id']}/{self.packet['packet_id']}.json"
        old_record.unlink()
        old_packet.unlink()
        self.new["taskbook_blob_sha1"] = tasks.taskbook_blob(self.new_path)
        self.new["publication_id"] = tasks.publication_id(
            TASK, self.new["taskbook_blob_sha1"], CURRENT, self.meta["parent_objective_id"])
        self.packet["task_publications"][0]["publication_id"] = self.new["publication_id"]
        self.packet["packet_id"] = followup.packet_id(self.packet["review_id"], "TASK_SET_PUBLISHED", [self.new["publication_id"]])
        self.save_new()
        self.save_packet()

    def check(self):
        isolation._validate_independent_successor(self.task_pin, self.row, self.old_packet,
                                                 {self.new["publication_id"]}, self.root)

    def test_strict_native_specimen_success_and_original_bytes_preserved(self):
        self.check()
        self.assertEqual(self.original_bytes, (self.root / self.anchor["taskbook_path"]).read_bytes())
        self.assertEqual(2, self.new["publication_generation"])
        self.assertEqual([], authority.review_authority_errors(self.fixture.review, self.root))
        self.assertIsNone(receipts.receipt_error(self.fixture.review, "REVIEW", self.root))

    def test_bootstrapped_semantic_current_records_wrapper_precedes_fixture_selection(self):
        semantic.install(self.root)
        from control_plane import research_task_records_impl as core
        self.assertTrue(core._task_semantic_integrity_fault_isolation_installed)
        self.assertNotIn(TASK, semantic.open_quarantines(self.root))
        self.assertEqual(self.new["publication_id"], tasks.current_records(self.root)[TASK]["publication_id"])

    def configure_old_quarantine(self):
        from control_plane import research_driver_review_authority_fault_isolation as old_reviews
        from tools import research_dispatch
        old_review = copy.deepcopy(self.fixture.review)
        old_review.update(review_id="DR-INVALID", driver_id="EM-RSA-45F14F")
        old_review.pop("write_authorization", None)
        review_path = "research_result_reviews/RR-OLD/DR-INVALID.json"
        write_json(self.root / review_path, {key: value for key, value in old_review.items() if not key.startswith("_")})
        write_json(self.root / old_reviews.QUARANTINE_FILE, {
            "schema": old_reviews.QUARANTINE_SCHEMA, "status": "ACTIVE", "entries": [{
                "review_id": "DR-INVALID", "result_id": "RR-OLD", "task_id": "RS-OLD",
                "review_record_path": review_path,
                "review_record_blob_sha1": isolation._git_blob_sha1((self.root / review_path).read_bytes()),
                "state": old_reviews.QUARANTINE_STATE, "operational": False, "history_preserved": True,
                "allowed_authority_errors": ["post-cutover review driver_id must use EM-DVR-* syntax"],
                "reason": "Exact specimen preserves invalid old author without granting authority.",
                **{flag: False for flag in old_reviews._AUTHORITY_FLAGS},
            }],
        })
        packet_path = "research_driver_followups/DR-INVALID/DFU-INVALID.json"
        old_packet = {**self.old_packet, "packet_id": "DFU-INVALID", "review_id": "DR-INVALID", "result_id": "RR-OLD",
                      "decision": "TASK_SET_PUBLISHED", "task_publications": [{"task_id": TASK, "publication_id": OLD}]}
        write_json(self.root / packet_path, old_packet)
        record_path = f"research_task_records/{TASK}/{OLD}.json"
        pin = {**self.task_pin, "publication_record_path": record_path,
               "publication_record_blob_sha1": isolation._git_blob_sha1((self.root / record_path).read_bytes()),
               "taskbook_blob_sha1": self.anchor["taskbook_blob_sha1"]}
        write_json(self.root / isolation.QUARANTINE_FILE, {
            "schema": isolation.QUARANTINE_SCHEMA, "status": "ACTIVE", "entries": [{
                "packet_id": "DFU-INVALID", "review_id": "DR-INVALID", "result_id": "RR-OLD",
                "packet_path": packet_path, "packet_blob_sha1": isolation._git_blob_sha1((self.root / packet_path).read_bytes()),
                "state": isolation.QUARANTINE_STATE, "operational": False, "history_preserved": True,
                "derived_task_publications": [pin], "expected_post_review_isolation_error": "packet references unknown review",
                "reason": "Exact synthetic nonoperational source review, preserved forever.",
                **{flag: False for flag in isolation._AUTHORITY_FLAGS},
            }],
        })
        return old_packet

    def test_four_reader_surfaces_preserve_old_quarantine_and_select_new_publication(self):
        from tools import research_dispatch
        self.configure_old_quarantine()
        self.assertIn("DFU-INVALID", isolation.validated_quarantines(self.root))
        isolation.install(self.root)
        self.assertEqual(self.new["publication_id"], tasks.current_records(self.root)[TASK]["publication_id"])
        definitions = {item["task_id"]: item for item in research_dispatch.merged_definitions(self.root)}
        self.assertEqual(self.new["publication_id"], definitions[TASK]["publication_id"])
        self.assertEqual("READY", definitions[TASK]["base_state"])
        self.assertNotIn("DFU-INVALID", {item["packet_id"] for item in followup.iter_packets(self.root)})
        self.assertEqual([], isolation.audit(self.root))
        self.assertEqual(self.original_bytes, (self.root / self.anchor["taskbook_path"]).read_bytes())

    def materialize_specimen(self, *, fail_postcheck=False):
        self.configure_old_quarantine()
        (self.root / f"research_task_records/{TASK}/{self.new['publication_id']}.json").unlink()
        (self.root / f"research_driver_followups/{self.packet['review_id']}/{self.packet['packet_id']}.json").unlink()
        self.new_path.unlink()
        isolation.install(self.root)
        sections = tasks._section_payloads(self.body)
        task_spec = {key: copy.deepcopy(self.meta[key]) for key in (
            "task_id", "title", "frontier", "next_action", "kind", "priority", "leverage", "identity_lane",
            "origin_kind", "task_lineage", "parent_task_id", "successor_gate", "source_refs", "dependencies")}
        task_spec.update(task_role="EXTERNAL_PRIOR_ART_DUPLICATION", research_value=self.anchor["research_value"],
            taskbook_filename="RSA_NATIVE_GEN2_FIXTURE.md", supersedes_publication_id=OLD,
            mother_question=sections["Mother question"], frozen_inputs_and_scope=sections["Frozen inputs and scope"],
            hard_target_and_required_outputs=sections["Hard target and required outputs"],
            research_value_to_preserve=sections["Research value to preserve"],
            success_kill_and_return_criteria=sections["Success, kill, and return criteria"])
        # The global governance post-audit is out of scope for this specimen
        # store. The native packet validator, real publication audit and exact
        # isolation audit all remain enabled; no Source operation is invoked.
        with mock.patch.object(transaction, "_candidate_post_audit",
                               side_effect=lambda packet, root, created: ["injected late audit failure"]
                               if fail_postcheck else isolation.audit(root)):
            outcome = transaction.materialize(review_id=self.fixture.review["review_id"],
                spec={"decision": "TASK_SET_PUBLISHED", "gate_decisions": self.packet["gate_decisions"], "tasks": [task_spec]},
                created_at=CREATED, root=self.root, publishing_driver_id=CURRENT, publisher_session_id=SESSION)
        return outcome

    def test_existing_native_materializer_can_generate_same_task_gen2_before_full_audit(self):
        outcome = self.materialize_specimen()
        current = tasks.current_records(self.root)[TASK]
        self.assertEqual(2, current["publication_generation"])
        self.assertEqual(OLD, current["supersedes_publication_id"])
        self.assertEqual(current["publication_id"], outcome["task_publications"][0]["publication_id"])
        self.assertEqual(self.original_bytes, (self.root / self.anchor["taskbook_path"]).read_bytes())

    def test_late_audit_failure_rolls_back_new_outputs_and_keeps_old_quarantine(self):
        with self.assertRaisesRegex(transaction.DriverFollowupTransactionError, "injected late audit failure"):
            self.materialize_specimen(fail_postcheck=True)
        self.assertFalse((self.root / "research_tasks/RSA_NATIVE_GEN2_FIXTURE.md").exists())
        self.assertEqual([f"{OLD}.json"], sorted(path.name for path in (self.root / "research_task_records" / TASK).glob("*.json")))
        self.assertTrue((self.root / "research_driver_followups/DR-INVALID/DFU-INVALID.json").is_file())
        self.assertEqual(self.original_bytes, (self.root / self.anchor["taskbook_path"]).read_bytes())

    def test_missing_followup_fails_even_with_safe_publication_pop(self):
        (self.root / f"research_driver_followups/{self.packet['review_id']}/{self.packet['packet_id']}.json").unlink()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "one exact native"):
            self.check()

    def test_revoked_source_driver_at_publication_fails(self):
        self.fixture.add_authorization(authorization(event="REVOKE", comment=902))
        self.packet["created_at"] = "2026-09-03T00:00:00+00:00"
        self.save_packet()
        with self.assertRaises(Exception):
            self.check()

    def test_math_scope_drift_fails_with_recomputed_publication_identity(self):
        self.new_path.write_text(books.render_taskbook(self.meta, self.body.replace("NO_MATERIAL_MATCH", "NOVEL_THEOREM")))
        self.refresh_publication_identity()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "frozen scope"):
            self.check()

    def test_parent_drift_fails(self):
        self.meta["parent_objective_id"] = "OTHER-PARENT"
        self.new_path.write_text(books.render_taskbook(self.meta, self.body))
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "frozen scope"):
            self.check()

    def test_extra_semantic_section_or_claim_in_wrapper_fails(self):
        for body in (self.body + "\n## New theorem\nAdditional factoring claim.\n",
                     "Additional factoring claim.\n" + self.body):
            with self.subTest(body=body[:40]):
                self.new_path.write_text(books.render_taskbook(self.meta, body))
                self.refresh_publication_identity()
                with self.assertRaises(isolation.DriverFollowupIsolationError):
                    self.check()

    def test_record_blob_drift_fails(self):
        self.new["taskbook_blob_sha1"] = "sha1:" + "0" * 40
        self.save_new()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "blob drift"):
            self.check()

    def test_record_cannot_omit_or_change_frozen_next_action(self):
        for remove in (False, True):
            with self.subTest(remove=remove):
                self.new["next_action"] = "Change the factoring theorem instead of conducting the audit."
                if remove:
                    del self.new["next_action"]
                self.save_new()
                with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "record/taskbook mismatch"):
                    self.check()

    def test_missing_cross_task_and_skipped_generation_chains_fail(self):
        for changes in ({"supersedes_publication_id": "TP2-MISSING"},
                        {"supersedes_publication_id": "TP2-OLD"},
                        {"publication_generation": 7}):
            with self.subTest(changes=changes):
                original = copy.deepcopy(self.new)
                self.new.update(changes)
                self.save_new()
                with self.assertRaises(isolation.DriverFollowupIsolationError):
                    self.check()
                self.new = original
                self.save_new()

    def test_publication_before_new_review_fails(self):
        self.new["published_at"] = "2026-08-30T00:00:00+00:00"
        self.save_new()
        with self.assertRaisesRegex(Exception, "before the review"):
            self.check()

    def test_future_publication_cannot_borrow_an_earlier_packet_authority(self):
        self.new["published_at"] = "2099-01-01T00:00:00+00:00"
        self.save_new()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "publication time is outside"):
            self.check()

    def test_missing_publisher_binding_fails(self):
        del self.packet["materialization_publisher"]
        self.save_packet()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "publisher binding"):
            self.check()

    def test_changed_receipt_payload_sha_fails_after_refreshing_review_pin(self):
        self.fixture.review["write_authorization"]["payload_sha256"] = "0" * 64
        raw = {key: value for key, value in self.fixture.review.items() if not key.startswith("_")}
        write_json(self.root / self.fixture.review["_review_path"], raw)
        self.packet["materialization_publisher"] = followup._materialization_binding(
            self.packet["review_id"], CURRENT, SESSION, CREATED, self.root)
        self.save_packet()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "payload-bound"):
            self.check()

    def test_absent_cutover_cannot_disable_prospective_review_receipt_validation(self):
        (self.root / receipts.CUTOVER).unlink()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "without a legacy exemption"):
            self.check()

    def test_legacy_pin_cannot_exempt_prospective_review_receipt_validation(self):
        path = self.root / self.fixture.review["_review_path"]
        data = path.read_bytes()
        write_json(self.root / receipts.CUTOVER, {
            "schema": "ENTERPRISE_MATH_CONTINUATION_RECORD_CUTOVER_V1", "records": {
                receipts.record_path(self.fixture.review, "REVIEW"): {
                    "sha256": hashlib.sha256(data).hexdigest(),
                    "git_blob_sha1": isolation._git_blob_sha1(data).removeprefix("sha1:"),
                },
            },
        })
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "without a legacy exemption"):
            self.check()

    def test_review_artifact_and_receipt_sha_drift_fail(self):
        (self.root / self.fixture.review["review_path"]).write_text("changed review")
        with self.assertRaises(Exception):
            self.check()

    def test_reviewer_authorship_overlap_fails_native_receipt(self):
        self.fixture.review["reviewer_contribution_ids"] = ["EM-RES-SPECIMEN"]
        self.save_review()
        # Rebind the frozen publisher to the changed exact review; a digest
        # refresh alone still cannot turn overlapping authorship into review.
        self.packet["materialization_publisher"] = followup._materialization_binding(
            self.packet["review_id"], CURRENT, SESSION, CREATED, self.root)
        self.save_packet()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "native integrity"):
            self.check()

    def test_hirr_is_not_a_native_driver_review_alias(self):
        self.fixture.review["record_schema"] = "ENTERPRISE_MATH_HISTORICAL_RESULT_REVIEW_V1"
        self.save_review()
        self.packet["materialization_publisher"] = followup._materialization_binding(
            self.packet["review_id"], CURRENT, SESSION, CREATED, self.root)
        self.save_packet()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "native integrity"):
            self.check()

    def test_ambiguous_heads_fail(self):
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "unambiguous"):
            isolation._validate_independent_successor(self.task_pin, self.row, self.old_packet,
                {self.new["publication_id"], "TP2-FORK"}, self.root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
