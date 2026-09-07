"""Exact provenance regressions using temporary books/records and real validators."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from control_plane import check_taskbook_publication_provenance as gate
from control_plane import research_task_semantic_integrity_fault_isolation as semantic

REPO = Path(__file__).resolve().parents[1]


def setUpModule():
    # Exercise the same persistent operational wrappers as the complete shard.
    gate.bootstrap.install(REPO)


class TaskbookPublicationProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write_json("templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json", {
            "schema": gate.core.TASKBOOK_TEMPLATE,
        })
        self.semantic_fixture()

    def write_json(self, path, value):
        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        return p

    def book_record(self, name="T", task="RS-T", publication="TP2-T", **changes):
        p = self.root / f"research_tasks/{name}.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        meta = {
            "task_id": task, "parent_objective_id": "OBJ-T",
            "task_authority": "PUBLISHED_REGISTERED", "base_state": "READY",
        }
        body = "\n\n".join(
            "## " + title + "\n\nA substantive exact fixture statement."
            for title in gate.core.MANDATORY_BODY_SECTIONS
        )
        p.write_text(gate.research_taskbook.render_taskbook(meta, body), encoding="utf-8")
        rec = {
            "record_schema": gate.core.RECORD_SCHEMA, "publication_id": publication,
            "task_id": task, "registry_key": task, "record_state": "ACTIVE",
            "publication_generation": 1,
            "publication_transaction": gate.core.PUBLICATION_TRANSACTION_V2,
            "working_truth_granted": False, "canonical_promotion_granted": False,
            "parent_objective_id": "OBJ-T", "taskbook_path": p.relative_to(self.root).as_posix(),
            "taskbook_blob_sha1": gate.core.taskbook_blob(p),
        }
        rec.update(changes)
        rp = self.write_json(f"research_task_records/{task}/{publication}.json", rec)
        return p, rec, rp

    def audit(self):
        # setUpModule installs the real complete bootstrap on REPO. The fixture
        # supplies actual semantic/record/fork/audit-only inputs consumed by its
        # persistent wrappers; only reinstalling unrelated global review policy
        # on this TEMP root is omitted. No validator or selection is mocked.
        with mock.patch.object(gate.bootstrap, "install"):
            return gate.audit(self.root)

    def semantic_fixture(self):
        """A separate exact nonoperational record for the required registry."""
        book, record, rp = self.book_record(
            "SEMANTIC", "RS-SEMANTIC-FIXTURE", "TP2-SEMANTIC-FIXTURE",
        )
        migration = {"archive_branch": "archive/test-fixture", "source_commit": "1" * 40}
        meta, body = gate.research_taskbook.split_taskbook(book.read_text(encoding="utf-8"))
        meta.update(identity_lane="MIGRATION_WRAPPER", migration_source=migration, source_refs=[])
        book.write_text(gate.research_taskbook.render_taskbook(meta, body), encoding="utf-8")
        source_meta = dict(meta, identity_lane="TASK_RESEARCH", source_refs=["fixture-source-proof"])
        # This is the pre-migration source artifact, not another published book.
        source = self.root / "fixtures/semantic-source.md"
        source.parent.mkdir()
        source.write_text(gate.research_taskbook.render_taskbook(source_meta, body), encoding="utf-8")
        record.update(taskbook_blob_sha1=gate.core.taskbook_blob(book), migration_source=migration)
        self.write_json(rp.relative_to(self.root), record)
        row = {
            "task_id": record["task_id"], "publication_id": record["publication_id"],
            "record_path": rp.relative_to(self.root).as_posix(),
            "record_blob_sha1": gate.core.git_blob_sha1_bytes(rp.read_bytes()),
            "taskbook_path": record["taskbook_path"],
            "taskbook_blob_sha1": gate.core.taskbook_blob(book),
            "source_taskbook_path": source.relative_to(self.root).as_posix(),
            "source_taskbook_blob_sha1": gate.core.taskbook_blob(source),
            "fault_class": semantic.FAULT_CLASS, "isolation_scope": semantic.ISOLATION_SCOPE,
            "semantic_fields": ["identity_lane"],
            "expected_semantics": {"identity_lane": "TASK_RESEARCH"},
            "observed_semantics": {"identity_lane": "MIGRATION_WRAPPER"},
            "required_missing_source_refs": ["fixture-source-proof"],
            "migration_provenance_field": "migration_source",
            "migration_archive_branch": migration["archive_branch"],
            "migration_source_commit": migration["source_commit"],
            "repair_state": semantic.OPEN_REPAIR_STATE,
            "operational_publication_id": None,
            "reason": "Synthetic migration changed the source identity and removed a source ref.",
        }
        for flag in (
            "working_truth_granted", "foundation_authority_granted",
            "canonical_promotion_granted", "successor_triggered",
            "review_disposition_granted", "replacement_publication_granted",
        ):
            row[flag] = False
        self.write_json(semantic.QUARANTINE_FILE, {
            "schema": semantic.QUARANTINE_SCHEMA, "status": "ACTIVE", "quarantines": [row],
        })

    def test_semantic_fixture_is_validated_and_cannot_select_publication(self):
        import research_operational_publications as operational
        from tools import research_task_records

        rows = semantic.validated_quarantines(self.root)
        self.assertEqual({"RS-SEMANTIC-FIXTURE"}, set(rows))
        self.assertEqual([], self.audit())
        self.assertIsNone(operational.selection("RS-SEMANTIC-FIXTURE", self.root))
        self.assertNotIn("RS-SEMANTIC-FIXTURE", research_task_records.current_records(self.root))
        blocked = semantic.blocked_definition("RS-SEMANTIC-FIXTURE", rows["RS-SEMANTIC-FIXTURE"])
        self.assertEqual("BLOCKED", blocked["base_state"])
        self.assertIsNone(blocked["publication_id"])
        source = self.root / rows["RS-SEMANTIC-FIXTURE"]["source_taskbook_path"]
        source.write_bytes(source.read_bytes() + b"\n")
        self.assertTrue(any("source taskbook blob drift" in error for error in self.audit()))

    def audit_only_fixture(self):
        old, record, rp = self.book_record(
            record_state="SUPERSEDED", taskbook_blob_sha1="sha1:" + "0" * 40,
        )
        _, _, successor = self.book_record(
            "NEW", publication="TP2-NEW", publication_generation=2,
            supersedes_publication_id="TP2-T", record_state="CLOSED",
        )
        actual = gate.core.taskbook_blob(old)
        row = {
            "quarantine_id": "TRAQ-T", "task_id": "RS-T", "publication_id": "TP2-T",
            "state": gate.record_audit.STATE, "nonoperational_basis": gate.record_audit.BASIS_SUPERSEDED,
            "operational": False, "history_preserved": True,
            "record_path": rp.relative_to(self.root).as_posix(),
            "record_blob_sha1": gate.core.git_blob_sha1_bytes(rp.read_bytes()),
            "taskbook_path": record["taskbook_path"], "taskbook_blob_sha1": actual,
            "allowed_task_record_audit_errors": ["taskbook blob drift"],
            "allowed_publication_envelope_errors": [
                f"taskbook Git blob drift: declared {record['taskbook_blob_sha1']}, actual {actual}"
            ],
        }
        for flag in (
            "working_truth_granted", "foundation_authority_granted",
            "canonical_promotion_granted", "successor_triggered", "operational_publication_selected",
        ):
            row[flag] = False
        payload = {"schema": gate.record_audit.SCHEMA, "status": "ACTIVE", "quarantines": [row]}
        self.write_json(gate.record_audit.QUARANTINE_FILE, payload)
        return row, payload, successor

    def fork_fixture(self):
        self.book_record(publication_transaction="LEGACY_UNLISTED_TRANSACTION")
        self.book_record("S", publication="TP2-S")
        row = {
            "task_id": "RS-T", "state": gate.fork.QUARANTINE_STATE,
            "publication_ids": ["TP2-T", "TP2-S"], "operational_publication_id": None,
            "isolation_scope": "CONTROL_PLANE_ONLY", "working_truth_granted": False,
            "foundation_authority_granted": False, "canonical_promotion_granted": False,
            "successor_triggered": False,
        }
        payload = {"schema": gate.fork.QUARANTINE_SCHEMA, "status": "ACTIVE", "quarantines": [row]}
        self.write_json(gate.fork.QUARANTINE_FILE, payload)
        return payload

    def legacy_fixture(self):
        path = "control_plane/legacy_control_migration_manifest.json"
        payload = json.loads((REPO / path).read_text(encoding="utf-8"))
        self.write_json(path, payload)
        for _, _, rp, _, bp, _ in gate.LEGACY_HANDOVERS:
            for name in (rp, bp):
                target = self.root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((REPO / name).read_bytes())
        return payload

    def test_exact_active_and_terminal_publications(self):
        _, rec, rp = self.book_record()
        for state in ["ACTIVE", *sorted(gate.core.TERMINAL_RECORD_STATES)]:
            rec["record_state"] = state
            self.write_json(rp.relative_to(self.root), rec)
            self.assertEqual([], self.audit(), state)

    def test_same_task_id_cannot_cover_another_path(self):
        book, _, _ = self.book_record()
        extra = book.with_name("UNPUBLISHED_COPY.md")
        extra.write_bytes(book.read_bytes())
        self.assertIn("research_tasks/UNPUBLISHED_COPY.md: " + gate.ORPHAN_SUFFIX, self.audit())

    def test_task_id_and_blob_drift_are_strict_errors(self):
        _, original, rp = self.book_record()
        for field, value, message in (
            ("task_id", "RS-OTHER", "taskbook task_id mismatch"),
            ("taskbook_blob_sha1", "sha1:" + "0" * 40, "taskbook blob drift"),
        ):
            record = dict(original, **{field: value})
            self.write_json(rp.relative_to(self.root), record)
            self.assertTrue(any(message in e for e in self.audit()), field)

    def test_orphan_and_unlisted_nonstandard_transaction_fail(self):
        book, rec, rp = self.book_record(publication_transaction="MIGRATED_FROM_V1_SHARED_REGISTRY")
        self.assertIn("research_tasks/T.md: " + gate.ORPHAN_SUFFIX, self.audit())
        rp.unlink()
        self.assertTrue(any("no immutable publication record" in e for e in self.audit()))

    def test_strict_body_and_template_errors_are_not_hidden(self):
        book, record, rp = self.book_record()
        meta, _ = gate.research_taskbook.split_taskbook(book.read_text(encoding="utf-8"))
        book.write_text(gate.research_taskbook.render_taskbook(meta, "## Mother question\n\nOnly one section."), encoding="utf-8")
        record["taskbook_blob_sha1"] = gate.core.taskbook_blob(book)
        self.write_json(rp.relative_to(self.root), record)
        self.assertTrue(any("mandatory body section" in e for e in self.audit()))
        self.book_record()
        self.write_json("templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json", {"schema": "BAD"})
        self.assertIn("publication template schema drift", self.audit())

    def test_exact_audit_only_source_and_invalid_pin(self):
        _, payload, _ = self.audit_only_fixture()
        self.assertEqual([], self.audit())
        payload["quarantines"][0]["record_blob_sha1"] = "sha1:" + "0" * 40
        self.write_json(gate.record_audit.QUARANTINE_FILE, payload)
        self.assertTrue(any("record blob drift" in e for e in self.audit()))

    def test_audit_only_stale_error_and_lost_basis_fail(self):
        _, payload, successor = self.audit_only_fixture()
        stale = copy.deepcopy(payload)
        stale["quarantines"][0]["allowed_task_record_audit_errors"].append("wrong record_schema")
        self.write_json(gate.record_audit.QUARANTINE_FILE, stale)
        self.assertTrue(any("stale or unused suppression" in e for e in self.audit()))
        self.write_json(gate.record_audit.QUARANTINE_FILE, payload)
        successor.unlink()
        self.assertTrue(any("not directly superseded" in e for e in self.audit()))

    def test_audit_only_does_not_hide_unrelated_strict_error(self):
        self.audit_only_fixture()
        self.book_record("BAD", "RS-BAD", "TP2-BAD", record_schema="BAD_SCHEMA")
        self.assertTrue(any("TP2-BAD.json: wrong record_schema" in e for e in self.audit()))

    def test_blocked_exact_fork_retains_history_without_selecting(self):
        self.fork_fixture()
        self.assertEqual([], self.audit())
        self.assertNotIn("RS-T", gate.fork.isolated_current_records(self.root))

    def test_unvalidated_or_drifting_fork_does_not_grant_provenance(self):
        payload = self.fork_fixture()
        for mutation in ("missing", "extra_head", "authority"):
            changed = copy.deepcopy(payload)
            if mutation == "missing":
                changed["quarantines"] = []
            elif mutation == "extra_head":
                changed["quarantines"][0]["publication_ids"].append("TP2-MISSING")
            else:
                changed["quarantines"][0]["working_truth_granted"] = True
            self.write_json(gate.fork.QUARANTINE_FILE, changed)
            self.assertTrue(self.audit(), mutation)

    def test_fork_history_cannot_hide_bad_state_or_extra_strict_error(self):
        self.fork_fixture()
        rp = self.root / "research_task_records/RS-T/TP2-T.json"
        rec = json.loads(rp.read_text(encoding="utf-8"))
        rec["record_state"] = "MYSTERY"
        self.write_json(rp.relative_to(self.root), rec)
        self.assertIn("research_tasks/T.md: " + gate.ORPHAN_SUFFIX, self.audit())
        rec["record_state"] = "ACTIVE"
        rec["registry_key"] = "WRONG"
        self.write_json(rp.relative_to(self.root), rec)
        self.assertTrue(any("registry_key mismatch" in e for e in self.audit()))

    def test_two_exact_manifest_handovers_and_drift(self):
        original = self.legacy_fixture()
        self.assertEqual(2, len(gate._legacy_handover_keys(self.root)))
        task = gate.LEGACY_HANDOVERS[0][0]
        for field, value in (("record_path", "research_task_records/WRONG.json"), ("publication_id", "TP2-WRONG")):
            changed = copy.deepcopy(original)
            next(row for row in changed["tasks"] if row["task_id"] == task)[field] = value
            self.write_json("control_plane/legacy_control_migration_manifest.json", changed)
            with self.assertRaisesRegex(ValueError, "manifest row drift"):
                gate._legacy_handover_keys(self.root)
        self.write_json("control_plane/legacy_control_migration_manifest.json", original)
        rp = self.root / gate.LEGACY_HANDOVERS[0][2]
        rp.write_bytes(rp.read_bytes() + b" ")
        with self.assertRaisesRegex(ValueError, "record blob drift"):
            gate._legacy_handover_keys(self.root)

    def test_manifest_missing_entry_or_taskbook_pin_drift_fails(self):
        original = self.legacy_fixture()
        changed = copy.deepcopy(original)
        changed["tasks"] = [r for r in changed["tasks"] if r["task_id"] != gate.LEGACY_HANDOVERS[0][0]]
        self.write_json("control_plane/legacy_control_migration_manifest.json", changed)
        with self.assertRaisesRegex(ValueError, "manifest row drift"):
            gate._legacy_handover_keys(self.root)
        self.write_json("control_plane/legacy_control_migration_manifest.json", original)
        bp = self.root / gate.LEGACY_HANDOVERS[0][4]
        bp.write_bytes(bp.read_bytes() + b"\n")
        with self.assertRaisesRegex(ValueError, "publication/book binding drift"):
            gate._legacy_handover_keys(self.root)


if __name__ == "__main__":
    unittest.main()
