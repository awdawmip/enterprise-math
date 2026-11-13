"""Task wording does not replace structured publication or evidence checks."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

from tools import research_taskbook as taskbook


ROOT = Path(__file__).resolve().parents[1]
# These are unit checks of the unwrapped publication implementation. Other
# suites install repository-wide semantic-quarantine projections on the shared
# module; those projections require the full repository, not this task fixture.
_RECORDS_SPEC = importlib.util.spec_from_file_location(
    "_lexical_publication_implementation",
    ROOT / "control_plane" / "research_task_records_impl.py",
)
if _RECORDS_SPEC is None or _RECORDS_SPEC.loader is None:
    raise ImportError("publication implementation cannot be loaded")
records = importlib.util.module_from_spec(_RECORDS_SPEC)
_RECORDS_SPEC.loader.exec_module(records)


class TaskbookLexicalIndependenceTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for name in ("research_taskbook_policy.json", "research_taskbook_contract.json"):
            (self.root / name).write_bytes((ROOT / name).read_bytes())
        self.path = self.root / "research_tasks" / "LEXICAL.md"
        self.path.parent.mkdir()

    def write_task(self, body="Prove the finite observer lemma.", **changes):
        meta = {
            "task_id": "RS-LEXICAL-INDEPENDENCE",
            "title": "Finite observer lemma",
            "kind": "RESEARCH",
            "origin_kind": "DIRECT_USER_DIRECTION",
            "task_lineage": "NEW_DIRECTION",
            "frontier": "The finite carrier is specified.",
            "next_action": "Prove the observer lemma for that carrier.",
        }
        meta.update(changes)
        self.path.write_text(taskbook.render_taskbook(meta, body), encoding="utf-8")

    def prepare(self):
        records.prepare_taskbook(
            self.path, publisher_role="RESEARCHER",
            parent_objective_id="OBJ-LEXICAL", root=self.root,
        )
        return records._prepared(self.path, root=self.root)

    def test_all_six_retired_categories_produce_no_warnings_or_errors(self):
        examples = [
            "Define the push forward of a discrete measure.",
            "Compare two mathematical workflows for the finite proof.",
            "This task does not wait for CI.",
            "Diagnose the user-requested GitHub Actions failure.",
            "Study Heartbeat World using the typed BRC carrier.",
            "Use issue #240 only as a provenance locator.",
            "This task grants no canonical promotion or L4 promotion.",
            "Research is the hot path. CI_NOT_REQUIRED_FOR_RESEARCH.",
            "No fixed researcher-id is embedded in this reusable taskbook.",
            "Pass is not a successor trigger; apply the existing successor-stage gate.",
            "研究问题：给定明确输入，证明所述命题或给出反例。",
        ]
        for body in examples:
            with self.subTest(body=body):
                self.write_task(body)
                _, actual_body = self.prepare()
                self.assertEqual(actual_body.strip(), body)
                self.assertEqual([], taskbook.audit_taskbook(
                    self.path, root=self.root, dispatch=True))

    def test_synthetic_bad_prose_cannot_promote_truth_or_confer_role_authority(self):
        self.write_task("Declare this unproved statement an established theorem immediately.")
        meta, _ = self.prepare()
        record = self.build_record(meta)
        self.assertFalse(record["working_truth_granted"])
        self.assertFalse(record["canonical_promotion_granted"])
        with self.assertRaisesRegex(records.TaskRecordError, "invalid publisher role"):
            self.build_record(meta, publisher_role="UNAUTHORIZED")

    def test_source_origin_and_lineage_still_fail(self):
        cases = [
            {"origin_kind": "UNKNOWN_ORIGIN"},
            {"origin_kind": "FREE_AXIOM_CANDIDATE",
             "origin_candidate_id": "C-TEST", "origin_candidate_state": "RAW_AXIOM_CANDIDATE"},
            {"origin_kind": "FOUNDATION_QUESTION"},
            {"task_lineage": "CONTINUATION", "parent_task_id": "RS-PARENT"},
            {"task_lineage": "UNKNOWN_LINEAGE"},
        ]
        for changes in cases:
            with self.subTest(changes=changes):
                self.write_task("Study Heartbeat World.", **changes)
                with self.assertRaises(records.TaskRecordError):
                    self.prepare()

    def test_fixed_runtime_identity_still_fails(self):
        for field in ("researcher_id", "driver_id", "execution_id"):
            with self.subTest(field=field):
                self.write_task(**{field: "FIXED-EXECUTION-IDENTITY"})
                with self.assertRaisesRegex(records.TaskRecordError, "TB-RUNTIME-META"):
                    self.prepare()

    def test_incomplete_scientific_content_and_invalid_publisher_still_fail(self):
        for body in ("", "# Heading only", "<required proof inputs>"):
            with self.subTest(body=body):
                self.write_task(body)
                with self.assertRaises(records.TaskRecordError):
                    self.prepare()
        self.write_task()
        with self.assertRaisesRegex(records.TaskRecordError, "unsupported publisher role"):
            records.prepare_taskbook(self.path, publisher_role="UNAUTHORIZED",
                                     parent_objective_id="OBJ-LEXICAL", root=self.root)

    def test_parent_identity_and_next_action_metadata_still_fail(self):
        for field in ("parent_objective_id", "identity_policy", "frontier", "next_action"):
            with self.subTest(field=field):
                self.write_task()
                meta, body = self.prepare()
                meta.pop(field)
                self.path.write_text(taskbook.render_taskbook(meta, body), encoding="utf-8")
                with self.assertRaises(records.TaskRecordError):
                    records._prepared(self.path, root=self.root)

    def build_record(self, meta, publisher_role="RESEARCHER"):
        return records.build_record(
            meta, path=self.path, publisher_role=publisher_role, publisher_id="EM-TEST",
            research_value="Discriminate the two finite observers.",
            published_at="2026-11-09T00:00:00+00:00",
            supersedes_publication_id=None, root=self.root,
        )

    def test_publication_stays_immutable_and_detects_taskbook_byte_drift(self):
        self.write_task("Study Heartbeat World and prove the finite observer lemma.")
        meta, _ = self.prepare()
        record = self.build_record(meta)
        target = (self.root / "research_task_records" / record["task_id"] /
                  (record["publication_id"] + ".json"))
        records._save_json_exclusive(target, record)
        self.assertEqual([], records.audit(self.root))
        before = target.read_bytes()
        with self.assertRaisesRegex(records.TaskRecordError, "immutable record already exists"):
            records._save_json_exclusive(target, record)
        self.assertEqual(before, target.read_bytes())
        self.path.write_text(self.path.read_text(encoding="utf-8") + "Changed input.\n", encoding="utf-8")
        self.assertTrue(any("taskbook blob drift" in error for error in records.audit(self.root)))

    def test_retired_schema_fields_and_helpers_do_not_return(self):
        policy = json.loads((ROOT / "research_taskbook_policy.json").read_text(encoding="utf-8"))
        for field in ("conflict_checks", "restatement_checks", "override_required_fields"):
            self.assertNotIn(field, policy)
        for helper in ("regex_hits", "override_map"):
            self.assertFalse(hasattr(taskbook, helper))


if __name__ == "__main__":
    unittest.main()
