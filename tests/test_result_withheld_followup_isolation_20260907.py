"""Result-basis follow-up authority regressions using real pinned validators."""
from __future__ import annotations

import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from control_plane import research_control_bootstrap as bootstrap
from control_plane import research_driver_followup_fault_isolation as followup_isolation
from control_plane import research_result_authority_fault_isolation as result_isolation
from control_plane import research_result_records_impl as result_impl
from control_plane import research_result_review_audit_fault_isolation as review_audit
from test_research_task_record_compatibility import _write_current_record, _write_semantic_fixture

ROOT = Path(__file__).resolve().parents[1]
NEW_PACKETS = {
    "DFU-B6A7EAFE760B531C3495", "DFU-1337737608BDE3D7E622",
    "DFU-7D5F26937C1F108DCFB3", "DFU-83B1D6E4C9027A5F3148",
    "DFU-060A48D8E81818A33864",
}
EXISTING_PACKETS = {
    "DFU-E79D7C72DF1A2D5137F5", "DFU-07F2C626AB51FAADD478",
    "DFU-6D3A91B84E205FC713A9", "DFU-9D7E05C41A682BF330D7",
}
FIXTURE_PACKET = "DFU-B6A7EAFE760B531C3495"
VALID_RESULT = "RR-VALID-SIBLING"
VALID_REVIEW = "DR-VALID-SIBLING"
VALID_PACKET = "DFU-VALID-SIBLING"


def setUpModule():
    bootstrap.install(ROOT)


class ResultWithheldFollowupIsolationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.packet_row = copy.deepcopy(followup_isolation.quarantine_rows(ROOT)[FIXTURE_PACKET])
        self.result_row = copy.deepcopy(result_isolation.quarantine_rows(ROOT)[self.packet_row["result_id"]])
        self.task = self.packet_row["derived_task_publications"][0]
        paths = {pin["path"] for pin in self.result_row["dependency_pins"]}
        paths.update({self.packet_row["packet_path"], self.task["publication_record_path"], self.task["taskbook_path"]})
        for relative in paths:
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT / relative).read_bytes())
        self.save_registries()
        # Public task selectors retain the actual semantic gate in the fixture.
        _write_semantic_fixture(self.root)

    def load(self, relative):
        return json.loads((self.root / relative).read_text(encoding="utf-8"))

    def write(self, relative, value):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")

    def blob(self, relative):
        return followup_isolation._git_blob_sha1((self.root / relative).read_bytes())

    def sha256(self, relative):
        return "sha256:" + hashlib.sha256((self.root / relative).read_bytes()).hexdigest()

    def save_registries(self):
        self.write(result_isolation.QUARANTINE_FILE, {
            "schema": result_isolation.SCHEMA, "status": "ACTIVE", "entries": [self.result_row],
        })
        self.write(followup_isolation.QUARANTINE_FILE, {
            "schema": followup_isolation.QUARANTINE_SCHEMA, "status": "ACTIVE", "entries": [self.packet_row],
        })

    def repin_result(self):
        relative = self.result_row["record_path"]
        self.result_row["record_blob_sha1"] = self.blob(relative)
        for pin in self.result_row["dependency_pins"]:
            if pin["path"] == relative:
                pin.update(git_blob_sha1=self.blob(relative), sha256=self.sha256(relative))
        self.save_registries()

    def make_valid_sibling(self, *, same_execution=False):
        """A valid sibling on the same task/publication and an independent execution."""
        result = self.load(self.result_row["record_path"])
        execution = self.load(self.result_row["execution_record_path"])
        if not same_execution:
            identity = {"execution_record_id": "ER-VALID-SIBLING", "claim_id": "CLM-VALID-SIBLING",
                        "execution_branch": "research/valid-sibling-fixture"}
            execution.update(identity)
            result.update(identity)
            self.write(f"research_execution_records/{result['task_id']}/ER-VALID-SIBLING.json", execution)
        result.update(result_id=VALID_RESULT, method_harvest="RESULT_ONLY",
                      independence_status="NOT_APPLICABLE", source_exposure_status="NOT_APPLICABLE")
        relative = f"research_result_records/{result['task_id']}/{VALID_RESULT}.json"
        self.write(relative, result)
        self.assertEqual([], result_impl.audit_result_record(result, execution, self.root))
        review = self.load(self.result_row["derived_reviews"][0]["review_record_path"])
        review.update(review_id=VALID_REVIEW, result_id=VALID_RESULT,
                      execution_record_id=result["execution_record_id"],
                      result_record_path=relative, result_record_sha256=self.sha256(relative))
        self.write(f"research_result_reviews/{VALID_RESULT}/{VALID_REVIEW}.json", review)
        self.assertEqual([], review_audit._review_errors(review, result, self.root))
        # Preserve the frozen successor's publication clock after its review.
        record = _write_current_record(self.root, task_id="RS-VALID-DERIVED",
                                       publication_id="TP2-VALID-DERIVED", parent_objective_id="OBJ-VALID",
                                       published_at=self.load(self.task["publication_record_path"])["published_at"])
        packet = self.load(self.packet_row["packet_path"])
        packet.update(packet_id=VALID_PACKET, review_id=VALID_REVIEW, result_id=VALID_RESULT,
                      task_publications=[{"task_id": record["task_id"], "publication_id": record["publication_id"],
                                          "task_role": "MATHEMATICAL_CONTINUATION"}])
        self.write(f"research_driver_followups/{VALID_REVIEW}/{VALID_PACKET}.json", packet)
        return result, review, packet

    def test_real_nine_packets_and_five_new_task_heads_have_no_authority(self):
        import research_driver_followup as followup
        from tools import research_dispatch, research_result_records, research_task_records

        rows = followup_isolation.validated_quarantines(ROOT)
        selected = {pid: row for pid, row in rows.items() if row.get("source_review_basis") == followup_isolation.RESULT_SOURCE}
        self.assertEqual(NEW_PACKETS, set(selected))
        self.assertTrue(EXISTING_PACKETS <= set(rows))
        self.assertTrue(all(rows[pid]["source_review_basis"] == followup_isolation.AUDIT_SOURCE for pid in EXISTING_PACKETS))
        self.assertFalse((NEW_PACKETS | EXISTING_PACKETS) & {r.get("packet_id") for r in followup.iter_packets(ROOT)})
        sources = result_isolation.validated_review_rows(ROOT)
        self.assertTrue({r["review_id"] for r in selected.values()} <= set(sources))
        self.assertFalse({r["review_id"] for r in selected.values()} & {r.get("review_id") for r in research_result_records.iter_reviews(ROOT)})
        tasks = {t["task_id"] for row in selected.values() for t in row["derived_task_publications"]}
        self.assertEqual(5, len(tasks))
        current = research_task_records.current_records(ROOT)
        definitions = {r["task_id"]: r for r in research_dispatch.merged_definitions(ROOT)}
        for pid, row in selected.items():
            self.assertEqual(followup_isolation.TASK_ISOLATION, row["isolation_kind"])
            self.assertEqual([pid], row["derived_task_publications"][0]["source_packet_ids"])
            self.assertTrue(all(row[flag] is False for flag in followup_isolation._AUTHORITY_FLAGS))
        for task in tasks:
            with self.subTest(task=task):
                self.assertNotIn(task, current)
                self.assertEqual("BLOCKED", definitions[task]["base_state"])
                self.assertIsNone(definitions[task]["publication_id"])

    def test_valid_sibling_result_review_packet_and_unrelated_task_are_preserved(self):
        import research_driver_followup as followup
        from tools import research_dispatch, research_result_records, research_task_records

        self.make_valid_sibling()
        self.assertEqual({FIXTURE_PACKET}, set(followup_isolation.validated_quarantines(self.root)))
        self.assertEqual({VALID_RESULT}, {r["result_id"] for r in research_result_records.iter_results(self.root)})
        self.assertEqual({VALID_REVIEW}, {r["review_id"] for r in research_result_records.iter_reviews(self.root)})
        self.assertEqual({VALID_PACKET}, {r["packet_id"] for r in followup.iter_packets(self.root)})
        current = research_task_records.current_records(self.root)
        self.assertNotIn(self.task["task_id"], current)
        self.assertEqual("TP2-VALID-DERIVED", current["RS-VALID-DERIVED"]["publication_id"])
        definitions = {r["task_id"]: r for r in research_dispatch.merged_definitions(self.root)}
        self.assertEqual("BLOCKED", definitions[self.task["task_id"]]["base_state"])
        self.assertIsNone(definitions[self.task["task_id"]]["publication_id"])
        self.assertEqual("READY", definitions["RS-VALID-DERIVED"]["base_state"])
        self.assertEqual("TP2-VALID-DERIVED", definitions["RS-VALID-DERIVED"]["publication_id"])

    def test_same_execution_result_without_replacement_cannot_supply_sibling_authority(self):
        from tools import research_result_records

        self.make_valid_sibling(same_execution=True)
        with self.assertRaisesRegex(result_isolation.ResultAuthorityIsolationError,
                                    "same-execution recovery lacks validated replacement authority"):
            research_result_records.iter_results(self.root)

    def test_result_basis_cannot_be_disguised_as_driver_or_review_audit(self):
        for basis, error in ((followup_isolation.AUTHORITY_SOURCE, "review-authority quarantined"),
                             (followup_isolation.AUDIT_SOURCE, "immutable-review-audit quarantined")):
            with self.subTest(basis=basis):
                self.packet_row["source_review_basis"] = basis
                self.save_registries()
                with self.assertRaisesRegex(followup_isolation.DriverFollowupIsolationError, error):
                    followup_isolation.validated_quarantines(self.root)

    def test_removed_result_isolation_cannot_reauthorize_its_packet(self):
        self.write(result_isolation.QUARANTINE_FILE, {
            "schema": result_isolation.SCHEMA, "status": "ACTIVE", "entries": [],
        })
        with self.assertRaisesRegex(followup_isolation.DriverFollowupIsolationError, "Result-control-authority withheld"):
            followup_isolation.validated_quarantines(self.root)

    def test_result_review_execution_and_artifact_byte_drift_fail_closed(self):
        review = self.result_row["derived_reviews"][0]
        for relative in (self.result_row["record_path"], self.result_row["execution_record_path"],
                         review["review_record_path"], review["review_artifact_path"]):
            with self.subTest(path=relative):
                path = self.root / relative
                original = path.read_bytes()
                path.write_bytes(original + b" ")
                try:
                    with self.assertRaisesRegex(result_isolation.ResultAuthorityIsolationError, "exact dependency byte drift"):
                        followup_isolation.validated_quarantines(self.root)
                finally:
                    path.write_bytes(original)

    def test_extra_and_stale_result_error_sets_fail_closed_after_repinning(self):
        original_row = copy.deepcopy(self.result_row)
        self.result_row["allowed_result_audit_errors"].append("wrong result schema")
        self.save_registries()
        with self.assertRaisesRegex(result_isolation.ResultAuthorityIsolationError, "complete raw strict error set drift"):
            followup_isolation.validated_quarantines(self.root)
        self.result_row = original_row
        result = self.load(self.result_row["record_path"])
        result["record_schema"] = "WRONG_FIXTURE_SCHEMA"
        self.write(self.result_row["record_path"], result)
        self.repin_result()
        with self.assertRaisesRegex(result_isolation.ResultAuthorityIsolationError, "complete raw strict error set drift"):
            followup_isolation.validated_quarantines(self.root)

    def test_recovered_result_does_not_silently_reactivate_a_frozen_quarantine(self):
        result = self.load(self.result_row["record_path"])
        result.update(method_harvest="RESULT_ONLY", independence_status="NOT_APPLICABLE", source_exposure_status="NOT_APPLICABLE")
        self.write(self.result_row["record_path"], result)
        self.repin_result()
        self.assertEqual([], result_impl.audit_result_record(result, self.load(self.result_row["execution_record_path"]), self.root))
        with self.assertRaisesRegex(result_isolation.ResultAuthorityIsolationError, "complete raw strict error set drift"):
            followup_isolation.validated_quarantines(self.root)

    def test_additional_review_of_the_same_withheld_result_fails_closed(self):
        review = self.load(self.result_row["derived_reviews"][0]["review_record_path"])
        review["review_id"] = "DR-EXTRA"
        self.write(f"research_result_reviews/{review['result_id']}/DR-EXTRA.json", review)
        with self.assertRaisesRegex(result_isolation.ResultAuthorityIsolationError, "complete derived review source set drift"):
            followup_isolation.validated_quarantines(self.root)

    def test_additional_packet_of_the_covered_review_fails_closed(self):
        packet = self.load(self.packet_row["packet_path"])
        packet["packet_id"] = "DFU-EXTRA"
        self.write(f"research_driver_followups/{packet['review_id']}/DFU-EXTRA.json", packet)
        with self.assertRaisesRegex(followup_isolation.DriverFollowupIsolationError, "direct review packet set drift"):
            followup_isolation.validated_quarantines(self.root)

    def test_additional_valid_source_for_pinned_publication_is_not_inferred(self):
        _, _, packet = self.make_valid_sibling()
        packet["task_publications"] = self.load(self.packet_row["packet_path"])["task_publications"]
        self.write(f"research_driver_followups/{VALID_REVIEW}/{VALID_PACKET}.json", packet)
        with self.assertRaisesRegex(followup_isolation.DriverFollowupIsolationError, "derived source packet set drift"):
            followup_isolation.validated_quarantines(self.root)

    def test_packet_publication_and_taskbook_byte_drift_fail_closed(self):
        for relative, error in ((self.packet_row["packet_path"], "packet blob drift"),
                                (self.task["publication_record_path"], "publication record blob drift"),
                                (self.task["taskbook_path"], "taskbook blob drift")):
            with self.subTest(path=relative):
                path = self.root / relative
                original = path.read_bytes()
                path.write_bytes(original + b" ")
                try:
                    with self.assertRaisesRegex(followup_isolation.DriverFollowupIsolationError, error):
                        followup_isolation.validated_quarantines(self.root)
                finally:
                    path.write_bytes(original)

    def test_singleton_explicit_source_set_cannot_claim_an_unregistered_packet(self):
        self.task["source_packet_ids"].append("DFU-UNREGISTERED")
        self.save_registries()
        with self.assertRaisesRegex(followup_isolation.DriverFollowupIsolationError, "declared source packet set drift"):
            followup_isolation.validated_quarantines(self.root)

    def test_result_basis_requires_an_explicit_singleton_source_set(self):
        del self.task["source_packet_ids"]
        self.save_registries()
        with self.assertRaisesRegex(followup_isolation.DriverFollowupIsolationError, "Result basis requires explicit complete source set"):
            followup_isolation.validated_quarantines(self.root)


if __name__ == "__main__":
    unittest.main()
