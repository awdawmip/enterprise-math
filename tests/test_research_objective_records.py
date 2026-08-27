import json
import tempfile
import unittest
from pathlib import Path

import research_objective_records as objectives


def write_json(path: Path, value: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


class ObjectiveGenerationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.driver = "EM-DVR-ABC123"

    def payload(self, *, status="OPEN", title="Objective", scope="scope", **extra):
        value = {
            "objective_id": "OBJ-TEST",
            "objective_status": status,
            "title": title,
            "scope": scope,
            "success_criteria": ["success"],
            "closure_criteria": ["all child work terminal"],
            "research_value": "preserve parallel evidence",
            "publisher_id": self.driver,
            "created_at": extra.pop("created_at", "2026-08-27T00:00:00+00:00"),
        }
        value.update(extra)
        return value

    def create(self, expected=None, **overrides):
        payload = self.payload(**overrides)
        return objectives.create_and_select(
            expected_previous_generation_id=expected,
            root=self.root,
            **payload,
        )

    def test_initial_objective_must_be_open_and_head_pins_digest(self):
        generation, head = self.create()
        self.assertEqual(1, generation["generation"])
        self.assertEqual("OPEN", generation["objective_status"])
        self.assertEqual(generation["objective_generation_id"], head["objective_generation_id"])
        self.assertEqual("OPERATIONAL_OBJECTIVE_CONTROL_ONLY", head["authority"])
        self.assertFalse(head["retained_non_head_generations_rejected"])
        self.assertEqual([], objectives.audit(self.root))
        with self.assertRaisesRegex(objectives.ObjectiveRecordError, "initial objective generation must be OPEN"):
            objectives.build_generation(root=Path(tempfile.mkdtemp()), **self.payload(status="PARKED"))

    def test_multiple_generation_proposals_are_retained_but_head_is_single(self):
        g1, _ = self.create()
        proposal_a = objectives.build_generation(
            root=self.root,
            **self.payload(title="route A", created_at="2026-08-27T00:01:00+00:00"),
        )
        proposal_b = objectives.build_generation(
            root=self.root,
            **self.payload(title="route B", created_at="2026-08-27T00:02:00+00:00"),
        )
        objectives.write_generation(proposal_a, self.root)
        objectives.write_generation(proposal_b, self.root)
        head = objectives.select_head(
            objective_id="OBJ-TEST",
            objective_generation_id=proposal_b["objective_generation_id"],
            expected_previous_generation_id=g1["objective_generation_id"],
            updated_by=self.driver,
            updated_at="2026-08-27T00:03:00+00:00",
            root=self.root,
        )
        self.assertEqual(proposal_b["objective_generation_id"], head["objective_generation_id"])
        self.assertIn(proposal_a["objective_generation_id"], objectives.objective_record_map(self.root))
        self.assertEqual(3, len(objectives.iter_objective_records(self.root)))
        self.assertEqual([], objectives.audit(self.root))

    def test_head_update_requires_expected_previous_and_stale_candidate_cannot_rollback(self):
        g1, _ = self.create()
        stale = objectives.build_generation(
            root=self.root,
            **self.payload(title="stale candidate", created_at="2026-08-27T00:01:00+00:00"),
        )
        objectives.write_generation(stale, self.root)
        fresh, _ = self.create(
            expected=g1["objective_generation_id"],
            title="selected candidate",
            created_at="2026-08-27T00:02:00+00:00",
        )
        with self.assertRaisesRegex(objectives.ObjectiveRecordError, "CAS mismatch"):
            objectives.select_head(
                objective_id="OBJ-TEST",
                objective_generation_id=stale["objective_generation_id"],
                expected_previous_generation_id=g1["objective_generation_id"],
                updated_by=self.driver,
                updated_at="2026-08-27T00:03:00+00:00",
                root=self.root,
            )
        with self.assertRaisesRegex(objectives.ObjectiveRecordError, "not created from the expected current"):
            objectives.select_head(
                objective_id="OBJ-TEST",
                objective_generation_id=stale["objective_generation_id"],
                expected_previous_generation_id=fresh["objective_generation_id"],
                updated_by=self.driver,
                updated_at="2026-08-27T00:03:00+00:00",
                root=self.root,
            )

    def test_closed_requires_evidence_and_reopen_requires_reason(self):
        g1, _ = self.create()
        with self.assertRaisesRegex(objectives.ObjectiveRecordError, "closure_evidence_refs"):
            objectives.build_generation(
                root=self.root,
                **self.payload(
                    status="CLOSED",
                    disposition_reason="done",
                    closure_evidence_refs=[],
                    created_at="2026-08-27T00:01:00+00:00",
                ),
            )
        closed, _ = self.create(
            expected=g1["objective_generation_id"],
            status="CLOSED",
            disposition_reason="all declared work resolved",
            closure_evidence_refs=["driver_reviews/closure.md"],
            created_at="2026-08-27T00:01:00+00:00",
        )
        with self.assertRaisesRegex(objectives.ObjectiveRecordError, "reopen_reason"):
            objectives.build_generation(
                root=self.root,
                **self.payload(created_at="2026-08-27T00:02:00+00:00"),
            )
        reopened, head = self.create(
            expected=closed["objective_generation_id"],
            status="OPEN",
            title="reopened",
            reopen_reason="new independent evidence lane requested",
            created_at="2026-08-27T00:02:00+00:00",
        )
        self.assertEqual("OPEN", reopened["objective_status"])
        self.assertEqual(reopened["objective_generation_id"], head["objective_generation_id"])
        self.assertEqual([], objectives.audit(self.root))

    def test_driver_syntax_is_required_but_record_does_not_grant_truth(self):
        payload = self.payload()
        payload["publisher_id"] = "EM-RESEARCHER-ABC123"
        with self.assertRaisesRegex(objectives.ObjectiveRecordError, "Driver-ID"):
            objectives.build_generation(root=self.root, **payload)
        generation, _ = self.create()
        self.assertFalse(generation["working_truth_granted"])
        self.assertFalse(generation["foundation_authority_granted"])
        self.assertFalse(generation["canonical_promotion_granted"])


class HistoricalTaskObjectiveBindingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.driver = "EM-DVR-ABC123"
        generation, self.head = objectives.create_and_select(
            expected_previous_generation_id=None,
            root=self.root,
            objective_id="OBJ-PARENT",
            objective_status="OPEN",
            title="parent",
            scope="parent scope",
            success_criteria=["success"],
            closure_criteria=["children terminal"],
            research_value="preserve",
            publisher_id=self.driver,
            created_at="2026-08-27T00:00:00+00:00",
        )
        self.generation = generation
        self.task = {
            "record_schema": "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2",
            "task_id": "RS-LEGACY",
            "publication_id": "TP2-LEGACY",
            "parent_objective_id": "OBJ-PARENT",
            "taskbook_path": "research_tasks/LEGACY.md",
            "taskbook_blob_sha1": "sha1:" + "1" * 40,
            "record_state": "ACTIVE",
            "claimable": True,
        }
        write_json(
            self.root / "research_task_records" / "RS-LEGACY" / "TP2-LEGACY.json",
            self.task,
        )

    def test_unbound_historical_task_is_explicitly_legacy_unbound(self):
        record = objectives.research_task_records.iter_records(self.root)[0]
        resolved = objectives.resolve_task_parent_binding(record, self.root)
        self.assertEqual("LEGACY_UNBOUND", resolved["binding_source"])
        self.assertIsNone(resolved["objective_generation_id"])

    def test_historical_sidecar_binds_exact_publication_without_rewriting_task(self):
        before = (
            self.root / "research_task_records" / "RS-LEGACY" / "TP2-LEGACY.json"
        ).read_bytes()
        binding = objectives.bind_historical_task(
            task_id="RS-LEGACY",
            publication_id="TP2-LEGACY",
            objective_id="OBJ-PARENT",
            objective_generation_id=self.generation["objective_generation_id"],
            bound_by=self.driver,
            bound_at="2026-08-27T00:01:00+00:00",
            root=self.root,
        )
        after = (
            self.root / "research_task_records" / "RS-LEGACY" / "TP2-LEGACY.json"
        ).read_bytes()
        self.assertEqual(before, after)
        self.assertEqual("TP2-LEGACY", binding["publication_id"])
        self.assertFalse(binding["final_permission_granted"])
        record = objectives.research_task_records.iter_records(self.root)[0]
        resolved = objectives.resolve_task_parent_binding(record, self.root)
        self.assertEqual("IMMUTABLE_LEGACY_SIDECAR", resolved["binding_source"])
        self.assertEqual(self.generation["objective_generation_id"], resolved["objective_generation_id"])
        self.assertEqual([], objectives.audit(self.root))

    def test_sidecar_cannot_reparent_task(self):
        with self.assertRaisesRegex(objectives.ObjectiveRecordError, "parent_objective_id"):
            objectives.bind_historical_task(
                task_id="RS-LEGACY",
                publication_id="TP2-LEGACY",
                objective_id="OBJ-OTHER",
                objective_generation_id=self.generation["objective_generation_id"],
                bound_by=self.driver,
                bound_at="2026-08-27T00:01:00+00:00",
                root=self.root,
            )

    def test_sidecar_must_target_open_generation(self):
        closed, _ = objectives.create_and_select(
            expected_previous_generation_id=self.generation["objective_generation_id"],
            root=self.root,
            objective_id="OBJ-PARENT",
            objective_status="CLOSED",
            title="closed",
            scope="parent scope",
            success_criteria=["success"],
            closure_criteria=["children terminal"],
            research_value="preserve",
            publisher_id=self.driver,
            created_at="2026-08-27T00:02:00+00:00",
            disposition_reason="done",
            closure_evidence_refs=["driver_reviews/closure.md"],
        )
        with self.assertRaisesRegex(objectives.ObjectiveRecordError, "OPEN objective generation"):
            objectives.bind_historical_task(
                task_id="RS-LEGACY",
                publication_id="TP2-LEGACY",
                objective_id="OBJ-PARENT",
                objective_generation_id=closed["objective_generation_id"],
                bound_by=self.driver,
                bound_at="2026-08-27T00:03:00+00:00",
                root=self.root,
            )

    def test_direct_future_binding_resolves_without_sidecar(self):
        direct = dict(self.task)
        direct["parent_objective_generation_id"] = self.generation["objective_generation_id"]
        resolved = objectives.resolve_task_parent_binding(direct, self.root)
        self.assertEqual("TASK_PUBLICATION_DIRECT", resolved["binding_source"])
        self.assertEqual(self.generation["objective_generation_id"], resolved["objective_generation_id"])


if __name__ == "__main__":
    unittest.main()
