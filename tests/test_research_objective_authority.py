import json
import tempfile
import unittest
from pathlib import Path

import research_objective_authority as authority
import research_objective_records as core


def write_json(path: Path, value: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


class ObjectiveAuthorityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.driver = "EM-DVR-ABC123"

    def payload(self, *, title="Objective", created_at="2026-08-27T00:00:00+00:00"):
        return {
            "objective_id": "OBJ-PARENT",
            "objective_status": "OPEN",
            "title": title,
            "scope": "parent scope",
            "success_criteria": ["success"],
            "closure_criteria": ["children terminal"],
            "research_value": "preserve evidence",
            "publisher_id": self.driver,
            "created_at": created_at,
        }

    def task(self, publication_id: str, published_at: str):
        value = {
            "record_schema": "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2",
            "task_id": "RS-HIST",
            "publication_id": publication_id,
            "parent_objective_id": "OBJ-PARENT",
            "taskbook_path": "research_tasks/HIST.md",
            "taskbook_blob_sha1": "sha1:" + "1" * 40,
            "published_at": published_at,
            "record_state": "ACTIVE",
            "claimable": True,
        }
        write_json(
            self.root / "research_task_records" / "RS-HIST" / f"{publication_id}.json",
            value,
        )
        return value

    def select(self, *, expected=None, title="Objective", created_at="2026-08-27T00:00:00+00:00"):
        return authority.create_and_select(
            expected_previous_generation_id=expected,
            root=self.root,
            **self.payload(title=title, created_at=created_at),
        )

    def test_selection_writes_immutable_receipt_and_audit_requires_it(self):
        generation, head, receipt = self.select()
        path = authority.selection_receipt_path(
            generation["objective_id"], generation["objective_generation_id"], self.root
        )
        self.assertTrue(path.exists())
        self.assertEqual(authority.SELECTION_AUTHORITY, receipt["selection_authority"])
        self.assertEqual(head["updated_at"], receipt["selected_at"])
        self.assertFalse(receipt["final_permission_granted"])
        self.assertEqual([], authority.audit(self.root))

        path.unlink()
        errors = authority.audit(self.root)
        self.assertTrue(any("lacks immutable selection receipt" in item for item in errors))

    def test_retained_open_proposal_without_selection_receipt_cannot_bind(self):
        selected, _, _ = self.select()
        proposal = core.build_generation(
            root=self.root,
            **self.payload(title="retained proposal", created_at="2026-08-27T00:01:00+00:00"),
        )
        core.write_generation(proposal, self.root)
        self.task("TP2-HIST", "2026-08-27T00:01:30+00:00")

        with self.assertRaisesRegex(
            authority.ObjectiveAuthorityError,
            "lacks immutable operational-head selection provenance",
        ):
            authority.bind_historical_task(
                task_id="RS-HIST",
                publication_id="TP2-HIST",
                objective_id="OBJ-PARENT",
                objective_generation_id=proposal["objective_generation_id"],
                bound_by=self.driver,
                bound_at="2026-08-27T00:03:00+00:00",
                root=self.root,
            )
        self.assertNotEqual(selected["objective_generation_id"], proposal["objective_generation_id"])

    def test_former_operational_generation_remains_bindable_for_task_published_during_tenure(self):
        first, _, _ = self.select(created_at="2026-08-27T00:00:00+00:00")
        self.task("TP2-HIST", "2026-08-27T00:01:00+00:00")
        second, _, _ = self.select(
            expected=first["objective_generation_id"],
            title="next operational generation",
            created_at="2026-08-27T00:02:00+00:00",
        )
        binding = authority.bind_historical_task(
            task_id="RS-HIST",
            publication_id="TP2-HIST",
            objective_id="OBJ-PARENT",
            objective_generation_id=first["objective_generation_id"],
            bound_by=self.driver,
            bound_at="2026-08-27T00:03:00+00:00",
            root=self.root,
        )
        self.assertEqual(authority.BINDING_AUTHORITY, binding["binding_authority"])
        self.assertEqual("2026-08-27T00:00:00+00:00", binding["operational_from"])
        self.assertEqual("2026-08-27T00:02:00+00:00", binding["operational_until"])
        record = next(
            item
            for item in core.iter_objective_records(self.root)
            if item["objective_generation_id"] == second["objective_generation_id"]
        )
        self.assertEqual("OPEN", record["objective_status"])
        self.assertEqual([], authority.audit(self.root))

    def test_task_published_after_successor_selection_cannot_back_bind(self):
        first, _, _ = self.select(created_at="2026-08-27T00:00:00+00:00")
        self.select(
            expected=first["objective_generation_id"],
            title="successor",
            created_at="2026-08-27T00:02:00+00:00",
        )
        self.task("TP2-LATE", "2026-08-27T00:03:00+00:00")
        with self.assertRaisesRegex(
            authority.ObjectiveAuthorityError,
            "after the target objective generation stopped being operational",
        ):
            authority.bind_historical_task(
                task_id="RS-HIST",
                publication_id="TP2-LATE",
                objective_id="OBJ-PARENT",
                objective_generation_id=first["objective_generation_id"],
                bound_by=self.driver,
                bound_at="2026-08-27T00:04:00+00:00",
                root=self.root,
            )

    def test_legacy_primitive_sidecar_is_retained_but_cannot_pass_canonical_authority_audit(self):
        first, _, _ = self.select(created_at="2026-08-27T00:00:00+00:00")
        self.task("TP2-PRIMITIVE", "2026-08-27T00:01:00+00:00")
        core.bind_historical_task(
            task_id="RS-HIST",
            publication_id="TP2-PRIMITIVE",
            objective_id="OBJ-PARENT",
            objective_generation_id=first["objective_generation_id"],
            bound_by=self.driver,
            bound_at="2026-08-27T00:01:30+00:00",
            root=self.root,
        )
        errors = authority.audit(self.root)
        self.assertTrue(
            any("binding lacks canonical operational-head authority" in item for item in errors)
        )
        resolved = core.resolve_task_parent_binding(
            self.task("TP2-OTHER", "2026-08-27T00:01:00+00:00"), self.root
        )
        self.assertEqual("LEGACY_UNBOUND", resolved["binding_source"])

    def test_authoritative_resolver_refuses_unproven_legacy_binding(self):
        first, _, _ = self.select(created_at="2026-08-27T00:00:00+00:00")
        task = self.task("TP2-RAW", "2026-08-27T00:01:00+00:00")
        core.bind_historical_task(
            task_id="RS-HIST",
            publication_id="TP2-RAW",
            objective_id="OBJ-PARENT",
            objective_generation_id=first["objective_generation_id"],
            bound_by=self.driver,
            bound_at="2026-08-27T00:01:30+00:00",
            root=self.root,
        )
        with self.assertRaisesRegex(
            authority.ObjectiveAuthorityError,
            "lacks canonical operational-head authority",
        ):
            authority.resolve_authoritative_task_parent_binding(task, self.root)


if __name__ == "__main__":
    unittest.main()
