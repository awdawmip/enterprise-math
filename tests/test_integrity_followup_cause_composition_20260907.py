"""Preserve independent exact task-integrity and follow-up authority causes."""
from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from control_plane import research_control_bootstrap as bootstrap
from control_plane import research_driver_followup_fault_isolation as followup
from control_plane import research_result_review_audit_fault_isolation as review_audit
from control_plane import research_task_integrity_fault_isolation as integrity
from test_research_task_record_compatibility import _write_semantic_fixture

ROOT = Path(__file__).resolve().parents[1]
OVERLAPS = {
    "RS-GEO6-NATIVE-RELATION-SELECTOR-CORE",
    "RS-GEO6-NATIVE-TRANSLATION-FOLNER-SEMANTICS",
    "RS-GEO6-PHYSICAL-REFINEMENT-SUPPORT-TRANSPORT-CORE",
    "RS-N-COUPLED-PUBLIC-N-DISTRIBUTIONAL-NONEXTERNALIZABILITY",
}
GEO_PACKET = "DFU-998EB492E2A5C7188EC3"
PINS = (
    "task_id", "publication_id", "publication_record_path",
    "publication_record_blob_sha1", "taskbook_path", "taskbook_blob_sha1",
)


def setUpModule():
    bootstrap.install(ROOT)


def _write_json(root, rel, value):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((json.dumps(value, indent=2) + "\n").encode("utf-8"))


def _load(root, rel):
    return json.loads((root / rel).read_text(encoding="utf-8"))


def _definitions(root):
    from tools import research_dispatch

    return {row["task_id"]: row for row in research_dispatch.merged_definitions(root)}


def _installation_snapshot(order):
    """Called in fresh interpreters, before either task blocker is installed."""
    from control_plane import research_nonoperational_review_source_adapter as adapter
    from tools import research_dispatch, research_task_records

    adapter.install(ROOT)  # Real source-basis validation; no runtime task overlay.
    assert not getattr(research_dispatch, "_task_integrity_fault_isolation_installed", False)
    assert not getattr(research_dispatch, "_followup_authority_isolation_installed", False)
    layers = [integrity, followup] if order == "integrity-first" else [followup, integrity]
    for layer in layers:
        layer.install(ROOT)
    bootstrap.install(ROOT)
    before = _definitions(ROOT)
    for layer in [*reversed(layers), *layers]:
        layer.install(ROOT)
    bootstrap.install(ROOT)
    after = _definitions(ROOT)
    assert before == after, "repeated installation changed a definition"
    integrity_errors = integrity.audit_runtime_projection(ROOT)
    followup_errors = followup.audit(ROOT)
    assert integrity_errors == [], integrity_errors
    assert followup_errors == [], followup_errors
    return {"definitions": after, "current": research_task_records.current_records(ROOT)}


class IntegrityFollowupCauseCompositionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.packet = copy.deepcopy(followup.quarantine_rows(ROOT)[GEO_PACKET])
        self.tasks = {t["task_id"]: t for t in self.packet["derived_task_publications"]}
        self.integrity_rows = {
            tid: copy.deepcopy(row) for tid, row in integrity.quarantine_rows(ROOT).items()
            if tid in self.tasks
        }
        for task in self.tasks.values():
            self.copy_source(task["publication_record_path"])
            self.copy_source(task["taskbook_path"])
        self.copy_source(self.packet["packet_path"])
        self.reviews = []
        self.copy_review(self.packet["review_id"])
        self.packets = [self.packet]
        self.save_registries()
        _write_semantic_fixture(self.root)

    def copy_source(self, rel):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((ROOT / rel).read_bytes())

    def copy_review(self, review_id):
        row = copy.deepcopy(review_audit.quarantine_rows(ROOT)[review_id])
        for rel in (row["review_record_path"], row["result_record_path"]):
            self.copy_source(rel)
        self.copy_source(_load(ROOT, row["review_record_path"])["review_path"])
        self.reviews.append(row)

    def save_registries(self):
        _write_json(self.root, followup.QUARANTINE_FILE, {
            "schema": followup.QUARANTINE_SCHEMA, "status": "ACTIVE", "entries": self.packets,
        })
        _write_json(self.root, review_audit.QUARANTINE_FILE, {
            "schema": review_audit.SCHEMA, "status": "ACTIVE", "entries": self.reviews,
        })
        _write_json(self.root, integrity.QUARANTINE_FILE, {
            "schema": integrity.QUARANTINE_SCHEMA, "status": "ACTIVE",
            "quarantines": [
                {key: value for key, value in row.items() if key != "_quarantine_file"}
                for row in self.integrity_rows.values()
            ],
        })

    def add_shared_source(self):
        second = next(row for row in followup.quarantine_rows(ROOT).values()
                      if row.get("source_review_basis") == followup.AUDIT_SOURCE
                      and row["review_id"] != self.packet["review_id"])
        self.copy_review(second["review_id"])
        row = copy.deepcopy(self.packet)
        row.update(packet_id="DFU-COMPOSITION-SHARED", review_id=second["review_id"],
                   result_id=second["result_id"])
        row["packet_path"] = f"research_driver_followups/{row['review_id']}/{row['packet_id']}.json"
        packet = _load(self.root, self.packet["packet_path"])
        packet.update(packet_id=row["packet_id"], review_id=row["review_id"], result_id=row["result_id"])
        _write_json(self.root, row["packet_path"], packet)
        row["packet_blob_sha1"] = followup._git_blob_sha1((self.root / row["packet_path"]).read_bytes())
        self.packets.append(row)
        for source in self.packets:
            for task in source["derived_task_publications"]:
                task["source_packet_ids"] = sorted(r["packet_id"] for r in self.packets)
        self.save_registries()

    def assert_composed(self, root, definitions):
        tasks = followup.derived_task_rows(root)
        rows = followup.validated_quarantines(root)
        intersections = set(tasks) & set(integrity.validated_quarantines(root))
        for tid in intersections:
            with self.subTest(task=tid):
                item = definitions[tid]
                primary = integrity.blocked_definition(tid, integrity.validated_quarantines(root)[tid])
                self.assertEqual("BLOCKED", item["base_state"])
                self.assertIsNone(item["publication_id"])
                self.assertEqual("TASK_INTEGRITY_QUARANTINE", item["registration_source"])
                for key, value in primary["hard_block"].items():
                    self.assertIn(key, item["hard_block"])
                    self.assertEqual(value, item["hard_block"][key])
                cause = item["followup_authority_block"]
                self.assertEqual("DRIVER_FOLLOWUP_AUTHORITY_QUARANTINE", cause["registration_source"])
                self.assertEqual(followup.QUARANTINE_FILE, cause["quarantine_file"])
                self.assertEqual({key: tasks[tid][key] for key in PINS}, {key: cause[key] for key in PINS})
                source_ids = tasks[tid].get("source_packet_ids") or [tasks[tid]["source_packet_id"]]
                self.assertEqual(sorted(source_ids), [r["packet_id"] for r in cause["source_packets"]])
                for source in cause["source_packets"]:
                    declared = rows[source["packet_id"]]
                    for key in ("packet_id", "review_id", "result_id", "packet_path", "packet_blob_sha1"):
                        self.assertEqual(declared[key], source[key])
                    self.assertEqual(declared.get("source_review_basis", followup.AUTHORITY_SOURCE),
                                     source["source_review_basis"])

    def test_four_real_intersections_preserve_both_exact_causes(self):
        from tools import research_task_records

        self.assertEqual(OVERLAPS, set(followup.derived_task_rows(ROOT)) & set(integrity.validated_quarantines(ROOT)))
        self.assert_composed(ROOT, _definitions(ROOT))
        self.assertFalse(OVERLAPS & set(research_task_records.current_records(ROOT)))
        self.assertEqual([], integrity.audit_runtime_projection(ROOT))
        self.assertEqual([], followup.audit(ROOT))

    def test_shared_secondary_cause_retains_all_sources_and_real_integrity_errors(self):
        from control_plane import research_task_records_impl as core
        from tools import research_task_records, research_taskbook

        self.add_shared_source()
        rows = integrity.validated_quarantines(self.root)
        for row in rows.values():
            _, body = research_taskbook.split_taskbook((self.root / row["taskbook_path"]).read_text(encoding="utf-8"))
            self.assertEqual(sorted(row["allowed_task_record_audit_errors"]), sorted(core.validate_body(body)))
        definitions = _definitions(self.root)
        self.assert_composed(self.root, definitions)
        self.assertFalse(set(self.tasks) & set(research_task_records.current_records(self.root)))
        for tid in self.tasks:
            cause = definitions[tid]["followup_authority_block"]
            self.assertEqual(2, len(cause["source_packets"]))
            self.assertEqual(sorted(r["packet_id"] for r in self.packets), cause["hard_block"]["source_packet_ids"])
            self.assertEqual(sorted(r["review_id"] for r in self.reviews), cause["hard_block"]["source_review_ids"])
        self.assertEqual([], integrity.audit_runtime_projection(self.root))
        self.assertEqual([], followup.audit(self.root))

    def test_all_six_cross_registry_pin_conflicts_are_rejected(self):
        tasks = followup.derived_task_rows(self.root)
        for key in PINS:
            with self.subTest(pin=key):
                changed = copy.deepcopy(tasks)
                changed[next(iter(changed))][key] += "-conflict"
                # Exercise the agreement boundary using a genuinely validated
                # integrity registry; no registry validator is replaced.
                with self.assertRaisesRegex(followup.DriverFollowupIsolationError, "exact pin conflict: " + key):
                    followup._integrity_overlaps(changed, self.root)

    def test_integrity_registry_pin_drift_cannot_hide_behind_followup_cause(self):
        self.assert_composed(self.root, _definitions(self.root))
        row = next(iter(self.integrity_rows.values()))
        for key in ("record_blob_sha1", "taskbook_blob_sha1"):
            with self.subTest(pin=key):
                original = row[key]
                row[key] = "sha1:" + "0" * 40
                self.save_registries()
                try:
                    with self.assertRaisesRegex(integrity.TaskIntegrityIsolationError, "blob drift"):
                        _definitions(self.root)
                finally:
                    row[key] = original
                    self.save_registries()

    def test_followup_packet_and_original_task_source_byte_drift_fail_closed(self):
        task = next(iter(self.tasks.values()))
        for rel in (self.packet["packet_path"], task["publication_record_path"], task["taskbook_path"]):
            with self.subTest(path=rel):
                path = self.root / rel
                original = path.read_bytes()
                path.write_bytes(original + b"\n")
                try:
                    with self.assertRaisesRegex((followup.DriverFollowupIsolationError, integrity.TaskIntegrityIsolationError), "blob drift"):
                        _definitions(self.root)
                finally:
                    path.write_bytes(original)

    def test_extra_shared_source_and_omitted_shared_source_fail_closed(self):
        self.add_shared_source()
        packet = _load(self.root, self.packet["packet_path"])
        packet.update(packet_id="DFU-UNDECLARED", review_id="DR-UNDECLARED")
        extra = "research_driver_followups/DR-UNDECLARED/DFU-UNDECLARED.json"
        _write_json(self.root, extra, packet)
        with self.assertRaisesRegex(followup.DriverFollowupIsolationError, "derived source packet set drift"):
            _definitions(self.root)
        (self.root / extra).unlink()
        self.packets.pop()
        self.save_registries()
        with self.assertRaisesRegex(followup.DriverFollowupIsolationError, "declared source packet set drift"):
            _definitions(self.root)

    def test_review_record_byte_drift_is_rejected(self):
        row = self.reviews[0]
        path = self.root / row["review_record_path"]
        path.write_bytes(path.read_bytes() + b"\n")
        with self.assertRaisesRegex(review_audit.ReviewAuditIsolationError, "review record blob drift"):
            _definitions(self.root)

    def test_repaired_review_makes_its_exact_fault_cause_stale(self):
        row = self.reviews[0]
        review = _load(self.root, row["review_record_path"])
        review.update(result_record_sha256=review_audit._sha256(self.root / row["result_record_path"]),
                      review_blob_sha1=review_audit._blob(self.root / review["review_path"]),
                      review_sha256=review_audit._sha256(self.root / review["review_path"]))
        _write_json(self.root, row["review_record_path"], review)
        row["review_record_blob_sha1"] = review_audit._blob(self.root / row["review_record_path"])
        self.save_registries()
        with self.assertRaisesRegex(review_audit.ReviewAuditIsolationError, "exact audit error set drift"):
            _definitions(self.root)

    def test_spoofed_prior_integrity_label_without_registry_overlap_has_no_effect(self):
        self.integrity_rows.clear()
        self.save_registries()
        tasks = followup.derived_task_rows(self.root)
        self.assertEqual({}, followup._integrity_overlaps(tasks, self.root))
        tid, task = next(iter(tasks.items()))
        prior = {"registration_source": "TASK_INTEGRITY_QUARANTINE", "hard_block": {"forged": True},
                 "title": "preserved title", "custom_field": ["preserved"]}
        actual = followup._composed_blocked_definition(tid, task, prior, None, followup.validated_quarantines(self.root))
        self.assertEqual(followup._blocked_definition(tid, task, prior), actual)
        self.assertNotIn("followup_authority_block", actual)
        self.assertEqual("DRIVER_FOLLOWUP_AUTHORITY_QUARANTINE", actual["registration_source"])

    def test_primary_is_reconstructed_from_validated_rows_not_prior_block(self):
        tasks = followup.derived_task_rows(self.root)
        rows = followup.validated_quarantines(self.root)
        intersections = followup._integrity_overlaps(tasks, self.root)
        tid, task = next(iter(tasks.items()))
        prior = {"hard_block": {"publication_id": "FORGED", "record_blob_sha1": "FORGED"},
                 "registration_source": "FORGED", "custom_field": ["preserved"]}
        actual = followup._composed_blocked_definition(tid, task, prior, intersections[tid], rows)
        self.assertEqual(integrity.blocked_definition(tid, intersections[tid])["hard_block"], actual["hard_block"])
        self.assertEqual(["preserved"], actual["custom_field"])

    def test_own_audit_rejects_missing_or_corrupt_secondary_cause(self):
        from tools import research_dispatch

        original = research_dispatch.merged_definitions
        tid = next(iter(self.tasks))
        for damage in ("missing", "publication_record_blob_sha1", "source_packets"):
            with self.subTest(damage=damage):
                def damaged_projection(root):
                    values = copy.deepcopy(original(root))
                    item = next(value for value in values if value["task_id"] == tid)
                    if damage == "missing":
                        item.pop("followup_authority_block")
                    else:
                        item["followup_authority_block"][damage] = [] if damage == "source_packets" else "FORGED"
                    return values
                # Inject a broken consumer projection only: original() still
                # runs all real registry, record, packet and source validators.
                with patch.object(research_dispatch, "merged_definitions", damaged_projection):
                    self.assertIn(f"{tid}: composed follow-up authority cause drifted", followup.audit(self.root))

    def test_own_audit_rejects_missing_null_primary_pin(self):
        from tools import research_dispatch

        original = research_dispatch.merged_definitions
        tid = next(iter(self.tasks))

        def damaged_projection(root):
            values = copy.deepcopy(original(root))
            item = next(value for value in values if value["task_id"] == tid)
            item["hard_block"].pop("operational_publication_id")
            return values

        with patch.object(research_dispatch, "merged_definitions", damaged_projection):
            self.assertIn(f"{tid}: composed integrity hard-block pin drifted", followup.audit(self.root))

    def test_fresh_reverse_and_repeated_installations_preserve_all_definitions(self):
        snapshots = []
        for order in ("integrity-first", "followup-first"):
            with self.subTest(order=order):
                output = self.root / f"{order}.json"
                code = (
                    "import json,sys; from pathlib import Path; "
                    "sys.path.insert(0,str(Path.cwd()/'tests')); "
                    "from test_integrity_followup_cause_composition_20260907 import _installation_snapshot; "
                    "Path(sys.argv[2]).write_text(json.dumps(_installation_snapshot(sys.argv[1]),sort_keys=True),encoding='utf-8')"
                )
                run = subprocess.run([sys.executable, "-c", code, order, str(output)], cwd=ROOT,
                                     capture_output=True, text=True, timeout=180)
                self.assertEqual(0, run.returncode, run.stdout + run.stderr)
                snapshots.append(json.loads(output.read_text(encoding="utf-8")))
        self.assertEqual(2, len(snapshots), "both installation orders must produce a validated snapshot")
        self.assertEqual(snapshots[0], snapshots[1])
        self.assertEqual(193, len(snapshots[0]["definitions"]))
        self.assert_composed(ROOT, snapshots[0]["definitions"])


if __name__ == "__main__":
    unittest.main()
