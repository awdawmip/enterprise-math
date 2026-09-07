"""Real-validator regressions for exact invalid-review follow-up source sets."""
from __future__ import annotations

import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from control_plane import research_control_bootstrap as bootstrap
from control_plane import research_driver_followup_fault_isolation as isolation
from control_plane import research_result_review_audit_fault_isolation as review_audit
from test_research_task_record_compatibility import _write_current_record

ROOT = Path(__file__).resolve().parents[1]
REVIEWS = {
    "DR-007256B8119682DF8EFA", "DR-19B757A8E5D817B5E495",
    "DR-4B7A2D91E6C0538FA124", "DR-4C239DD3C0C251A78E45",
    "DR-8E3C51A7D2B9046F1C85", "DR-B66959082DC75F6225C0",
    "DR-C20A9201B684ECE69AF8", "DR-C6A128F3B95D407E2A71",
}


def setUpModule():
    bootstrap.install(ROOT)


class ReviewFollowupSourceSetIsolationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.review_rows = []
        self.packet_rows = []
        record = _write_current_record(
            self.root, task_id="RS-DERIVED", publication_id="TP2-DERIVED",
            parent_objective_id="OBJ-FIXTURE",
        )
        rp = "research_task_records/RS-DERIVED/TP2-DERIVED.json"
        self.task = {
            "task_id": record["task_id"], "publication_id": record["publication_id"],
            "publication_record_path": rp,
            "publication_record_blob_sha1": self.blob(rp),
            "taskbook_path": record["taskbook_path"],
            "taskbook_blob_sha1": self.blob(record["taskbook_path"]),
            "source_packet_ids": ["DFU-A", "DFU-B"],
        }
        for label in ("A", "B", "C"):
            self.make_review(label)
            self.make_packet(label, [] if label == "C" else [copy.deepcopy(self.task)])
        self.save_registries()

    def write_json(self, rel, value):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")

    def load(self, rel):
        return json.loads((self.root / rel).read_text(encoding="utf-8"))

    def blob(self, rel):
        return isolation._git_blob_sha1((self.root / rel).read_bytes())

    def sha256(self, rel):
        return "sha256:" + hashlib.sha256((self.root / rel).read_bytes()).hexdigest()

    def save_registries(self):
        self.write_json(review_audit.QUARANTINE_FILE, {
            "schema": review_audit.SCHEMA, "status": "ACTIVE", "entries": self.review_rows,
        })
        self.write_json(isolation.QUARANTINE_FILE, {
            "schema": isolation.QUARANTINE_SCHEMA, "status": "ACTIVE", "entries": self.packet_rows,
        })

    def make_review(self, label):
        result_path = f"research_result_records/RS-SOURCE-{label}/RR-{label}.json"
        result = {
            "record_schema": review_audit.impl.RESULT_SCHEMA,
            "result_id": f"RR-{label}", "task_id": f"RS-SOURCE-{label}",
            "publication_id": f"TP2-SOURCE-{label}", "execution_record_id": f"ER-{label}",
        }
        self.write_json(result_path, result)
        artifact = f"fixtures/review-{label}.md"
        path = self.root / artifact
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"Original fixture review {label}.\n", encoding="utf-8")
        review_path = f"research_result_reviews/RR-{label}/DR-{label}.json"
        review = {
            **result, "record_schema": review_audit.impl.REVIEW_SCHEMA,
            "review_id": f"DR-{label}", "result_record_path": result_path,
            "result_record_sha256": "sha256:" + "0" * 64,
            "review_path": artifact, "review_blob_sha1": "sha1:" + "0" * 40,
            "review_sha256": "sha256:" + "0" * 64,
            "disposition": "ACCEPTED", "destination_class": "TOOL", "terminal": True,
        }
        self.write_json(review_path, review)
        self.review_rows.append({
            "review_id": review["review_id"], "result_id": result["result_id"],
            "task_id": result["task_id"], "review_record_path": review_path,
            "review_record_blob_sha1": self.blob(review_path),
            "result_record_path": result_path, "result_record_blob_sha1": self.blob(result_path),
            "state": review_audit.STATE, "operational": False, "history_preserved": True,
            "allowed_review_audit_errors": ["result record digest drift", "review artifact digest drift"],
            **{flag: False for flag in review_audit.AUTHORITY_FLAGS},
        })

    def make_packet(self, label, tasks):
        path = f"research_driver_followups/DR-{label}/DFU-{label}.json"
        packet = {
            "schema": "ENTERPRISE_MATH_DRIVER_REVIEW_FOLLOWUP_V1",
            "packet_id": f"DFU-{label}", "review_id": f"DR-{label}", "result_id": f"RR-{label}",
            "decision": "TASK_SET_PUBLISHED" if tasks else "PARENT_CLOSED",
            "task_publications": [{"task_id": t["task_id"], "publication_id": t["publication_id"]} for t in tasks],
        }
        self.write_json(path, packet)
        self.packet_rows.append({
            "packet_id": packet["packet_id"], "review_id": packet["review_id"],
            "result_id": packet["result_id"], "packet_path": path, "packet_blob_sha1": self.blob(path),
            "state": isolation.QUARANTINE_STATE, "operational": False, "history_preserved": True,
            "source_review_basis": isolation.AUDIT_SOURCE,
            "isolation_kind": isolation.TASK_ISOLATION if tasks else isolation.PACKET_ONLY,
            "packet_decision": packet["decision"], "derived_task_publications": tasks,
            "expected_post_review_isolation_error": "packet references unknown review",
            "reason": "Exact synthetic invalid-review authority with a complete packet source set.",
            **{flag: False for flag in isolation._AUTHORITY_FLAGS},
        })

    def rewrite_review(self, label, change):
        row = next(r for r in self.review_rows if r["review_id"] == f"DR-{label}")
        review = self.load(row["review_record_path"])
        change(review)
        self.write_json(row["review_record_path"], review)
        row["review_record_blob_sha1"] = self.blob(row["review_record_path"])
        self.save_registries()

    def test_real_eight_reviews_packets_and_five_tasks_have_no_operational_authority(self):
        import research_driver_followup as followup
        from tools import research_dispatch, research_result_records, research_task_records

        reviews = review_audit.validated_rows(ROOT)
        rows = isolation.validated_quarantines(ROOT)
        selected = {pid: r for pid, r in rows.items() if r["review_id"] in REVIEWS}
        self.assertEqual(REVIEWS, {r["review_id"] for r in selected.values()})
        self.assertTrue(REVIEWS <= set(reviews))
        self.assertEqual(8, len(selected))
        closure_only = [r for r in selected.values() if r["isolation_kind"] == isolation.PACKET_ONLY]
        self.assertEqual(4, len(closure_only))
        self.assertTrue(all(r["derived_task_publications"] == [] for r in closure_only))
        self.assertFalse(REVIEWS & {r.get("review_id") for r in research_result_records.iter_reviews(ROOT)})
        self.assertFalse(set(selected) & {r.get("packet_id") for r in followup.iter_packets(ROOT)})
        tasks = {t["task_id"] for r in selected.values() for t in r["derived_task_publications"]}
        self.assertEqual(5, len(tasks))
        current = research_task_records.current_records(ROOT)
        definitions = {r["task_id"]: r for r in research_dispatch.merged_definitions(ROOT)}
        for task in tasks:
            with self.subTest(task=task):
                self.assertNotIn(task, current)
                self.assertEqual("BLOCKED", definitions[task]["base_state"])
                self.assertIsNone(definitions[task]["publication_id"])

    def test_complete_shared_source_set_is_preserved_without_dictionary_overwrite(self):
        self.assertEqual(3, len(isolation.validated_quarantines(self.root)))
        task = isolation.derived_task_rows(self.root)["RS-DERIVED"]
        self.assertEqual(["DFU-A", "DFU-B"], task["source_packet_ids"])
        self.assertEqual(["DR-A", "DR-B"], task["source_review_ids"])
        self.assertNotIn("source_packet_id", task)
        blocked = isolation._blocked_definition("RS-DERIVED", task, None)
        self.assertEqual("BLOCKED", blocked["base_state"])
        self.assertEqual(["DFU-A", "DFU-B"], blocked["hard_block"]["source_packet_ids"])
        self.assertTrue({"DFU-A", "DFU-B", "DR-A", "DR-B"} <= set(blocked["source_refs"]))
        packets = [self.load(r["packet_path"]) for r in self.packet_rows]
        self.assertEqual([], isolation.operational_packets(packets, self.root))

    def test_both_exact_closure_spellings_remain_packet_only(self):
        row = self.packet_rows[2]
        for decision in ("PARENT_CLOSED", "PARENT_OBJECTIVE_CLOSURE"):
            with self.subTest(decision=decision):
                packet = self.load(row["packet_path"])
                packet["decision"] = row["packet_decision"] = decision
                self.write_json(row["packet_path"], packet)
                row["packet_blob_sha1"] = self.blob(row["packet_path"])
                self.save_registries()
                self.assertEqual([], isolation.validated_quarantines(self.root)["DFU-C"]["derived_task_publications"])
                self.assertEqual({"RS-DERIVED"}, set(isolation.derived_task_rows(self.root)))

    def test_shared_source_set_cannot_omit_one_registered_packet(self):
        self.packet_rows.pop(1)
        self.save_registries()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "declared source packet set drift"):
            isolation.validated_quarantines(self.root)
        self.packet_rows[0]["derived_task_publications"][0]["source_packet_ids"] = ["DFU-A"]
        self.save_registries()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "derived source packet set drift"):
            isolation.validated_quarantines(self.root)

    def test_shared_source_set_must_be_explicit_in_every_row(self):
        del self.packet_rows[1]["derived_task_publications"][0]["source_packet_ids"]
        self.save_registries()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "explicit complete source set"):
            isolation.validated_quarantines(self.root)

    def test_additional_unregistered_publication_source_fails_closed(self):
        packet = self.load(self.packet_rows[0]["packet_path"])
        packet.update(packet_id="DFU-EXTRA", review_id="DR-UNREGISTERED")
        self.write_json("research_driver_followups/DR-UNREGISTERED/DFU-EXTRA.json", packet)
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "derived source packet set drift"):
            isolation.validated_quarantines(self.root)

    def test_additional_closure_packet_from_covered_review_fails_closed(self):
        packet = self.load(self.packet_rows[2]["packet_path"])
        packet["packet_id"] = "DFU-EXTRA"
        self.write_json("research_driver_followups/DR-C/DFU-EXTRA.json", packet)
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "direct review packet set drift"):
            isolation.validated_quarantines(self.root)

    def test_packet_only_cannot_hide_an_undeclared_task_or_fabricate_one(self):
        row = self.packet_rows[2]
        packet = self.load(row["packet_path"])
        packet["task_publications"] = [{"task_id": "RS-DERIVED", "publication_id": "TP2-DERIVED"}]
        self.write_json(row["packet_path"], packet)
        row["packet_blob_sha1"] = self.blob(row["packet_path"])
        self.save_registries()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "derived publication set drift"):
            isolation.validated_quarantines(self.root)
        row["derived_task_publications"] = [self.task]
        self.save_registries()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "exact empty closure task set"):
            isolation.validated_quarantines(self.root)

    def test_packet_only_requires_an_explicit_empty_list_and_exact_decision(self):
        row = self.packet_rows[2]
        packet = self.load(row["packet_path"])
        del packet["task_publications"]
        self.write_json(row["packet_path"], packet)
        row["packet_blob_sha1"] = self.blob(row["packet_path"])
        self.save_registries()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "malformed exact packet task set"):
            isolation.validated_quarantines(self.root)
        packet.update(task_publications=[], decision="TASK_SET_PUBLISHED")
        self.write_json(row["packet_path"], packet)
        row["packet_blob_sha1"] = self.blob(row["packet_path"])
        self.save_registries()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "exact packet decision drift"):
            isolation.validated_quarantines(self.root)

    def test_review_pin_drift_and_removed_quarantine_fail_closed(self):
        path = self.root / self.review_rows[0]["review_record_path"]
        path.write_bytes(path.read_bytes() + b" ")
        with self.assertRaisesRegex(review_audit.ReviewAuditIsolationError, "review record blob drift"):
            isolation.validated_quarantines(self.root)
        self.review_rows.pop(0)
        self.save_registries()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "source review is not immutable-review-audit quarantined"):
            isolation.validated_quarantines(self.root)

    def test_extra_and_stale_review_errors_are_not_suppressed(self):
        self.review_rows[0]["allowed_review_audit_errors"].append("wrong review schema")
        self.save_registries()
        with self.assertRaisesRegex(review_audit.ReviewAuditIsolationError, "exact audit error set drift"):
            isolation.validated_quarantines(self.root)
        self.review_rows[0]["allowed_review_audit_errors"].pop()
        self.rewrite_review("A", lambda review: review.update(record_schema="WRONG"))
        with self.assertRaisesRegex(review_audit.ReviewAuditIsolationError, "exact audit error set drift"):
            isolation.validated_quarantines(self.root)

    def test_recovered_source_review_does_not_auto_reactivate_its_chain(self):
        def recover(review):
            review["result_record_sha256"] = self.sha256(review["result_record_path"])
            review["review_blob_sha1"] = self.blob(review["review_path"])
            review["review_sha256"] = self.sha256(review["review_path"])
        self.rewrite_review("A", recover)
        with self.assertRaisesRegex(review_audit.ReviewAuditIsolationError, "exact audit error set drift"):
            isolation.validated_quarantines(self.root)

    def test_packet_publication_and_taskbook_byte_drift_fail_closed(self):
        for rel, error in (
            (self.packet_rows[0]["packet_path"], "packet blob drift"),
            (self.task["publication_record_path"], "publication record blob drift"),
            (self.task["taskbook_path"], "taskbook blob drift"),
        ):
            with self.subTest(path=rel):
                path = self.root / rel
                original = path.read_bytes()
                path.write_bytes(original + b"\n")
                try:
                    with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, error):
                        isolation.validated_quarantines(self.root)
                finally:
                    path.write_bytes(original)

    def test_identical_copies_cannot_replace_canonical_source_paths(self):
        row = self.packet_rows[0]
        original_path = row["packet_path"]
        alias = "fixtures/copied-packet.json"
        self.write_json(alias, self.load(original_path))
        row.update(packet_path=alias, packet_blob_sha1=self.blob(alias))
        self.save_registries()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "exact source packet path mismatch"):
            isolation.validated_quarantines(self.root)
        row.update(packet_path=original_path, packet_blob_sha1=self.blob(original_path))
        task = row["derived_task_publications"][0]
        alias = "fixtures/copied-publication.json"
        self.write_json(alias, self.load(task["publication_record_path"]))
        task.update(publication_record_path=alias, publication_record_blob_sha1=self.blob(alias))
        self.save_registries()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "exact publication record path mismatch"):
            isolation.validated_quarantines(self.root)

    def test_shared_pin_or_arbitrary_task_identity_changes_are_rejected(self):
        changed = self.packet_rows[1]["derived_task_publications"][0]
        changed["taskbook_blob_sha1"] = "sha1:" + "0" * 40
        self.save_registries()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "publication taskbook pin mismatch"):
            isolation.validated_quarantines(self.root)
        changed["taskbook_blob_sha1"] = self.task["taskbook_blob_sha1"]
        changed["task_id"] = "RS-OTHER"
        self.save_registries()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "derived publication set drift"):
            isolation.validated_quarantines(self.root)

    def test_unrelated_packet_is_preserved_and_authority_flags_cannot_be_enabled(self):
        unrelated = {"packet_id": "DFU-UNRELATED", "review_id": "DR-UNRELATED", "task_publications": []}
        packets = [self.load(r["packet_path"]) for r in self.packet_rows] + [unrelated]
        self.assertEqual([unrelated], isolation.operational_packets(packets, self.root))
        for flag in isolation._AUTHORITY_FLAGS:
            with self.subTest(flag=flag):
                self.packet_rows[0][flag] = True
                self.save_registries()
                with self.assertRaisesRegex(isolation.DriverFollowupIsolationError, "cannot grant"):
                    isolation.validated_quarantines(self.root)
                self.packet_rows[0][flag] = False


if __name__ == "__main__":
    unittest.main()
