import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import research_objective_records as objective_core
from tools import research_objective_authority as objective_authority
from tools import research_parent_closure as parent_closure


def write_json(path: Path, value: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


class ParentClosureTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.driver = "EM-DVR-ABC123"

    def objective_payload(self, status: str, created_at: str, title: str):
        value = {
            "objective_id": "OBJ-PARENT",
            "objective_status": status,
            "title": title,
            "scope": "parent scope",
            "success_criteria": ["success"],
            "closure_criteria": ["children terminal"],
            "research_value": "preserve evidence",
            "publisher_id": self.driver,
            "created_at": created_at,
        }
        if status == "CLOSED":
            value["disposition_reason"] = "objective evidence complete"
            value["closure_evidence_refs"] = ["evidence/parent-close.json"]
        return value

    def open_objective(self):
        return objective_authority.create_and_select(
            expected_previous_generation_id=None,
            root=self.root,
            **self.objective_payload("OPEN", "2026-08-27T00:00:00+00:00", "open"),
        )

    def close_objective(self, previous: str):
        return objective_authority.create_and_select(
            expected_previous_generation_id=previous,
            root=self.root,
            **self.objective_payload("CLOSED", "2026-08-27T00:02:00+00:00", "closed"),
        )

    def task(self, publication_id: str, generation_id: str | None = None):
        value = {
            "record_schema": "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2",
            "record_state": "ACTIVE",
            "task_id": "RS-CHILD",
            "publication_id": publication_id,
            "parent_objective_id": "OBJ-PARENT",
            "taskbook_path": "research_tasks/CHILD.md",
            "taskbook_blob_sha1": "sha1:" + "1" * 40,
            "published_at": "2026-08-27T00:01:00+00:00",
            "claimable": True,
        }
        if generation_id is not None:
            value["parent_objective_generation_id"] = generation_id
        write_json(
            self.root / "research_task_records" / "RS-CHILD" / f"{publication_id}.json",
            value,
        )
        return value

    def closed_with_bound_child(self):
        opened, _, _ = self.open_objective()
        task = self.task("TP2-CHILD", opened["objective_generation_id"])
        closed, _, _ = self.close_objective(opened["objective_generation_id"])
        return opened, closed, task

    def test_closed_head_plus_terminal_child_derives_parent_complete(self):
        self.closed_with_bound_child()
        with patch.object(
            parent_closure.research_cohort_runtime,
            "task_active_cohort_state",
            return_value=None,
        ), patch.object(
            parent_closure.research_result_records,
            "task_result_state",
            return_value={"state": "TERMINAL", "terminal": True},
        ):
            out = parent_closure.derive_objective_closure("OBJ-PARENT", self.root)
        self.assertTrue(out["derived_parent_complete"])
        self.assertEqual("DERIVED_PARENT_COMPLETE", out["state"])
        self.assertEqual(["RS-CHILD"], out["terminal_active_child_task_ids"])
        self.assertFalse(out["final_permission_granted"])

    def test_open_head_never_derives_complete_even_if_child_terminal(self):
        opened, _, _ = self.open_objective()
        self.task("TP2-CHILD", opened["objective_generation_id"])
        with patch.object(
            parent_closure.research_cohort_runtime,
            "task_active_cohort_state",
            return_value=None,
        ), patch.object(
            parent_closure.research_result_records,
            "task_result_state",
            return_value={"state": "TERMINAL", "terminal": True},
        ):
            out = parent_closure.derive_objective_closure("OBJ-PARENT", self.root)
        self.assertFalse(out["derived_parent_complete"])
        self.assertEqual("OBJECTIVE_HEAD_NOT_CLOSED", out["state"])

    def test_active_unbound_child_fails_closed(self):
        opened, _, _ = self.open_objective()
        self.task("TP2-UNBOUND", None)
        self.close_objective(opened["objective_generation_id"])
        out = parent_closure.derive_objective_closure("OBJ-PARENT", self.root)
        self.assertFalse(out["derived_parent_complete"])
        self.assertEqual("ACTIVE_CHILD_OBJECTIVE_BINDING_UNPROVEN", out["state"])
        self.assertEqual("RS-CHILD", out["unbound_active_children"][0]["task_id"])

    def test_nonterminal_active_cohort_overrides_older_terminal_task_result(self):
        self.closed_with_bound_child()
        cohort = {"state": "ACTIVE_PARALLEL_COHORTS", "terminal": False}
        with patch.object(
            parent_closure.research_cohort_runtime,
            "task_active_cohort_state",
            return_value=cohort,
        ), patch.object(
            parent_closure.research_result_records,
            "task_result_state",
            return_value={"state": "TERMINAL", "terminal": True},
        ) as result_state:
            out = parent_closure.derive_objective_closure("OBJ-PARENT", self.root)
        self.assertFalse(out["derived_parent_complete"])
        self.assertEqual("ACTIVE_CHILD_CONTROL_NOT_TERMINAL", out["state"])
        self.assertEqual("ACTIVE_EXECUTION_COHORT_OVERLAY", out["nonterminal_active_children"][0]["authority"])
        result_state.assert_not_called()

    def test_terminal_active_cohort_is_sufficient_child_control_even_without_task_global_result(self):
        self.closed_with_bound_child()
        cohort = {"state": "TERMINAL_PARALLEL_COHORTS", "terminal": True}
        with patch.object(
            parent_closure.research_cohort_runtime,
            "task_active_cohort_state",
            return_value=cohort,
        ), patch.object(
            parent_closure.research_result_records,
            "task_result_state",
            return_value=None,
        ) as result_state:
            out = parent_closure.derive_objective_closure("OBJ-PARENT", self.root)
        self.assertTrue(out["derived_parent_complete"])
        result_state.assert_not_called()

    def test_primitive_unproven_sidecar_cannot_participate_in_parent_closure(self):
        opened, _, _ = self.open_objective()
        self.task("TP2-RAW", None)
        objective_core.bind_historical_task(
            task_id="RS-CHILD",
            publication_id="TP2-RAW",
            objective_id="OBJ-PARENT",
            objective_generation_id=opened["objective_generation_id"],
            bound_by=self.driver,
            bound_at="2026-08-27T00:01:30+00:00",
            root=self.root,
        )
        self.close_objective(opened["objective_generation_id"])
        out = parent_closure.derive_objective_closure("OBJ-PARENT", self.root)
        self.assertFalse(out["derived_parent_complete"])
        self.assertEqual("ACTIVE_CHILD_OBJECTIVE_BINDING_UNPROVEN", out["state"])
        self.assertIn("lacks canonical operational-head authority", out["unbound_active_children"][0]["reason"])

    def test_missing_current_head_selection_receipt_is_authority_invalid(self):
        opened, _, _ = self.open_objective()
        self.task("TP2-CHILD", opened["objective_generation_id"])
        closed, _, _ = self.close_objective(opened["objective_generation_id"])
        receipt = objective_authority.selection_receipt_path(
            "OBJ-PARENT", closed["objective_generation_id"], self.root
        )
        receipt.unlink()
        out = parent_closure.derive_objective_closure("OBJ-PARENT", self.root)
        self.assertFalse(out["derived_parent_complete"])
        self.assertEqual("OBJECTIVE_AUTHORITY_INVALID", out["state"])
        self.assertIn("lacks immutable selection receipt", out["authority_error"])


if __name__ == "__main__":
    unittest.main()
