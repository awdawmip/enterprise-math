"""Preserve audited FREE derivation provenance through actual V2 functions.

All books and records are local temporary fixtures. These checks exercise the
publication structure and evidence binding, not live role authority or proof
acceptance.
"""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from control_plane import research_task_records_impl as core
from control_plane import research_task_semantic_integrity_fault_isolation as semantic_isolation
from tools import research_task_records as records
from tools import research_taskbook


REPO = Path(__file__).resolve().parents[1]


class FreeDerivedTaskPublicationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.contract = json.loads((REPO / "research_taskbook_contract.json").read_text())
        (self.root / "research_taskbook_contract.json").write_text(json.dumps(self.contract))
        self.book = self.root / "research_tasks" / "LOCAL-FREE-DERIVED.md"
        self.book.parent.mkdir()
        self.source_refs = ["LOCAL-FIXTURE/candidate-proof.md", "LOCAL-FIXTURE/phase-b-audit.md"]
        # Exercise the strict immutable-record contract, independently of any
        # global bootstrap's operational/quarantine audit wrapper.
        self.audit = getattr(records, "strict_audit", records.audit)

    def audit_local_fixture(self):
        # These temporary publication fixtures have no production quarantine manifest.
        # Exercise the strict record audit while preserving live bootstrap behavior.
        with patch.object(semantic_isolation, "open_quarantines", return_value={}):
            return self.audit(self.root)

    def write_book(self, state="DERIVED_NOT_AXIOM", *, body=None, **changes):
        meta = {
            "task_id": "LOCAL-FREE-DERIVED",
            "title": "Continue an audited derived result",
            "base_state": "DRAFT",
            "origin_kind": "FREE_AXIOM_CANDIDATE",
            "origin_candidate_id": "LOCAL-CANDIDATE-DERIVED",
            "origin_candidate_state": state,
            "task_lineage": "NEW_DIRECTION",
            "frontier": "A local fixture states a derived lemma under the original assumptions.",
            "next_action": "Determine the remaining extension or retain an exact obstruction.",
            "priority": "P1",
            "leverage": "HIGH",
            "identity_lane": "FREE-DERIVED-FIXTURE",
            "source_refs": self.source_refs,
            "evidence_status": "LOCAL_AUDITED_FIXTURE_NOT_LIVE_ACCEPTANCE",
        }
        meta.update(changes)
        if body is None:
            body = (
                "Preserve the candidate's derivation and its Phase-B classification. "
                "Investigate the named remaining extension under the same source assumptions; "
                "a proof or an exact obstruction settles this local question."
            )
        self.book.write_text(research_taskbook.render_taskbook(meta, body), encoding="utf-8")
        return meta

    def prepare(self, role="RESEARCHER", parent="LOCAL-PARENT"):
        records.prepare_taskbook(self.book, publisher_role=role,
                                 parent_objective_id=parent, root=self.root)
        return core._prepared(self.book, root=self.root)[0]

    def build(self, meta, role="RESEARCHER", **changes):
        args = dict(path=self.book, publisher_role=role,
                    publisher_id="LOCAL-PUBLISHER-NOT-A-LIVE-IDENTITY",
                    research_value="The remaining extension has a distinct testable outcome.",
                    published_at="2026-11-19T08:30:00+00:00",
                    supersedes_publication_id=None, root=self.root)
        args.update(changes)
        return records.build_record(meta, **args)

    def save(self, record):
        path = records.record_path(self.root, record["task_id"], record["publication_id"])
        records._save_json_exclusive(path, record)
        return path

    def test_derived_result_survives_prepare_record_and_audit_for_existing_roles(self):
        for role in ("RESEARCHER", "RESEARCH_DRIVER"):
            with self.subTest(role=role):
                self.write_book()
                meta = self.prepare(role)
                record = self.build(meta, role)
                saved = self.save(record)
                self.assertEqual([], self.audit_local_fixture())
                self.assertEqual("FREE_AXIOM_CANDIDATE", record["origin_kind"])
                self.assertEqual("LOCAL-CANDIDATE-DERIVED", record["origin_candidate_id"])
                self.assertEqual("DERIVED_NOT_AXIOM", record["origin_candidate_state"])
                self.assertEqual(self.source_refs, record["source_refs"])
                self.assertEqual(meta["evidence_status"], record["evidence_status"])
                self.assertEqual("LOCAL-PARENT", record["parent_objective_id"])
                self.assertEqual(role, record["publisher_role"])
                self.assertFalse(record["working_truth_granted"])
                self.assertFalse(record["canonical_promotion_granted"])
                self.assertEqual("P2" if role == "RESEARCHER" else "P1",
                                 record["effective_priority"])
                self.assertEqual(records.taskbook_blob(self.book), record["taskbook_blob_sha1"])
                saved.unlink()

    def test_previous_audited_classes_keep_the_same_publication_path(self):
        for state in ("AUDITED_AXIOM_CANDIDATE", "AUDITED_REPLACEMENT_CANDIDATE",
                      "EXACT_NEGATIVE_OBSTRUCTION"):
            with self.subTest(state=state):
                self.write_book(state)
                meta = self.prepare()
                self.assertEqual(state, self.build(meta)["origin_candidate_state"])

    def test_raw_and_other_classifications_do_not_become_publishable(self):
        for state in ("DISCOVERY_IN_PROGRESS", "BLIND_CANDIDATE_FROZEN",
                      "PHASE_B_AUDIT_IN_PROGRESS", "FALSIFIED",
                      "DUPLICATE_OR_ALREADY_KNOWN", "PRIOR_ART_ANALOGUE",
                      "IMPLEMENTATION_ARTIFACT"):
            with self.subTest(state=state):
                self.write_book(state)
                before = self.book.read_bytes()
                with self.assertRaisesRegex(core.TaskRecordError, "TB-ORIGIN-CANDIDATE-STATE"):
                    self.prepare("RESEARCH_DRIVER")
                self.assertEqual(before, self.book.read_bytes())
                self.assertEqual([], records.iter_records(self.root))

    def test_missing_candidate_identity_state_and_unknown_origin_are_rejected(self):
        for field in ("origin_candidate_id", "origin_candidate_state"):
            with self.subTest(field=field):
                self.write_book(**{field: ""})
                with self.assertRaisesRegex(core.TaskRecordError, "TB-ORIGIN-CANDIDATE"):
                    self.prepare()
        self.write_book(origin_kind="UNREGISTERED_ORIGIN")
        with self.assertRaisesRegex(core.TaskRecordError, "TB-ORIGIN-VALUE"):
            self.prepare()

    def test_existing_publisher_parent_and_scientific_content_requirements_remain(self):
        self.write_book()
        with self.assertRaisesRegex(core.TaskRecordError, "unsupported publisher role"):
            self.prepare("CONTROL_PLANE_MAINTENANCE")
        with self.assertRaisesRegex(core.TaskRecordError, "parent_objective_id is required"):
            self.prepare(parent="")
        for body in ("# Title only", "<insert source and scientific question>"):
            with self.subTest(body=body):
                self.write_book(body=body)
                with self.assertRaises(core.TaskRecordError):
                    self.prepare()

    def test_publisher_and_research_value_are_still_required(self):
        self.write_book()
        meta = self.prepare()
        for field in ("publisher_id", "research_value"):
            with self.subTest(field=field):
                with self.assertRaisesRegex(core.TaskRecordError, "publisher_id and research_value are required"):
                    self.build(meta, **{field: ""})

    def test_immutable_record_rejects_drift_and_publication_cannot_grant_acceptance(self):
        self.write_book()
        record = self.build(self.prepare())
        path = self.save(record)
        self.book.write_text(self.book.read_text() + "\nChanged premise.\n")
        self.assertTrue(any("taskbook blob drift" in error for error in self.audit_local_fixture()))
        self.write_book()
        self.prepare()
        for field in ("working_truth_granted", "canonical_promotion_granted"):
            changed = dict(record, **{field: True})
            path.write_text(json.dumps(changed))
            with self.subTest(field=field):
                self.assertTrue(any("cannot grant" in error for error in self.audit_local_fixture()))

    def test_old_contract_reproduces_the_original_hold_with_the_same_validator(self):
        old = copy.deepcopy(self.contract)
        old["task_origin_contract"]["free_candidate_allowed_states"].remove("DERIVED_NOT_AXIOM")
        (self.root / "research_taskbook_contract.json").write_text(json.dumps(old))
        self.write_book()
        with self.assertRaisesRegex(core.TaskRecordError, "TB-ORIGIN-CANDIDATE-STATE"):
            self.prepare()

    def test_task_eligibility_agrees_without_expanding_foundation_intake(self):
        lifecycle = json.loads((REPO / "research_axiom_candidate_state_machine.json").read_text())
        allowed = set(self.contract["task_origin_contract"]["free_candidate_allowed_states"])
        self.assertEqual(allowed, set(lifecycle["task_publication"]["eligible_from"]))
        self.assertEqual(allowed, set(lifecycle["explicit_task_transition"]["allowed_from"]))
        self.assertNotIn("DERIVED_NOT_AXIOM", lifecycle["foundation_intake"]["eligible_from"])
        self.assertFalse(lifecycle["task_publication"]["publication_grants_foundation_status"])
        self.assertFalse(lifecycle["task_publication"]["origin_may_be_relabelled_driver_roadmap"])


if __name__ == "__main__":
    unittest.main()
