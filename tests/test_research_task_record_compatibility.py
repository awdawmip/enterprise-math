import json
import tempfile
import unittest
from pathlib import Path

from control_plane import check_research_task_records_compatibility as compat
from tools import research_task_records


TASK_ID = "RS-T"
PUB_ID = "TP2-LEGACY"
TASKBOOK = "research_tasks/legacy.md"


class TaskRecordCompatibilityTests(unittest.TestCase):
    def fixture(self) -> tuple[tempfile.TemporaryDirectory, Path]:
        td = tempfile.TemporaryDirectory()
        root = Path(td.name)
        taskbook = root / TASKBOOK
        taskbook.parent.mkdir(parents=True, exist_ok=True)
        taskbook.write_text(
            """<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-T",
  "parent_objective_id": "OBJ-T",
  "task_authority": "PUBLISHED_REGISTERED",
  "base_state": "READY"
}
-->
# Legacy task

## Mother question
A real question.

## Frozen inputs
Pinned inputs.

## Hard target
Exact target.

## Research value
Retained value.

## Success and kill criteria
Exact success and kill conditions.
""",
            encoding="utf-8",
        )
        blob = research_task_records.taskbook_blob(taskbook)
        record = {
            "record_schema": research_task_records.RECORD_SCHEMA,
            "record_state": "ACTIVE",
            "task_id": TASK_ID,
            "registry_key": TASK_ID,
            "publication_id": PUB_ID,
            "publication_generation": 1,
            "supersedes_publication_id": None,
            "publication_transaction": research_task_records.PUBLICATION_TRANSACTION_V2,
            "taskbook_path": TASKBOOK,
            "taskbook_blob_sha1": blob,
            "parent_objective_id": "OBJ-T",
            "working_truth_granted": False,
            "canonical_promotion_granted": False,
        }
        path = root / "research_task_records" / TASK_ID / f"{PUB_ID}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(record) + "\n", encoding="utf-8")
        waiver = {
            "schema": compat.WAIVER_SCHEMA,
            "status": "ACTIVE",
            "waivers": [
                {
                    "waiver_id": "W-1",
                    "task_id": TASK_ID,
                    "publication_id": PUB_ID,
                    "taskbook_path": TASKBOOK,
                    "taskbook_blob_sha1": blob,
                    "scope": compat.WAIVER_SCOPE,
                    "legacy_section_aliases": {
                        "Frozen inputs and scope": "Frozen inputs",
                        "Hard target and required outputs": "Hard target",
                        "Research value to preserve": "Research value",
                        "Success, kill, and return criteria": "Success and kill criteria",
                    },
                    "working_truth_granted": False,
                    "foundation_authority_granted": False,
                    "canonical_promotion_granted": False,
                    "successor_triggered": False,
                }
            ],
        }
        (root / compat.WAIVER_FILE).write_text(json.dumps(waiver) + "\n", encoding="utf-8")
        return td, root

    def test_exact_blob_pinned_legacy_aliases_are_the_only_suppressed_errors(self):
        td, root = self.fixture()
        try:
            raw = research_task_records.audit(root)
            self.assertEqual(4, len(raw))
            self.assertEqual([], compat.audit(root))
        finally:
            td.cleanup()

    def test_blob_drift_is_never_suppressed(self):
        td, root = self.fixture()
        try:
            path = root / TASKBOOK
            path.write_text(path.read_text(encoding="utf-8") + "\nchanged\n", encoding="utf-8")
            errors = compat.audit(root)
            self.assertTrue(any("taskbook blob drift" in item for item in errors), errors)
            self.assertTrue(any("pinned taskbook blob drift" in item for item in errors), errors)
        finally:
            td.cleanup()

    def test_extra_missing_required_section_cannot_hide_behind_waiver(self):
        td, root = self.fixture()
        try:
            path = root / TASKBOOK
            text = path.read_text(encoding="utf-8").replace("## Mother question\nA real question.\n\n", "")
            path.write_text(text, encoding="utf-8")
            record_path = root / "research_task_records" / TASK_ID / f"{PUB_ID}.json"
            record = json.loads(record_path.read_text(encoding="utf-8"))
            new_blob = research_task_records.taskbook_blob(path)
            record["taskbook_blob_sha1"] = new_blob
            record_path.write_text(json.dumps(record) + "\n", encoding="utf-8")
            waiver_path = root / compat.WAIVER_FILE
            waiver = json.loads(waiver_path.read_text(encoding="utf-8"))
            waiver["waivers"][0]["taskbook_blob_sha1"] = new_blob
            waiver_path.write_text(json.dumps(waiver) + "\n", encoding="utf-8")
            errors = compat.audit(root)
            self.assertTrue(any("waiver scope does not exactly equal current body-policy errors" in item for item in errors), errors)
            self.assertTrue(any("Mother question" in item for item in errors), errors)
        finally:
            td.cleanup()


if __name__ == "__main__":
    unittest.main()
