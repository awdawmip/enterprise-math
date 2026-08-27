from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools import research_task_records as records
from tools import research_taskbook


TASK_ID = "TST-LEGACY-HEADING-COMPAT"
HIST = "TP2-HIST-LEGACY"
LIVE = "TP2-LIVE-CURRENT"
PARENT = "TST_PARENT_OBJECTIVE"
HIST_PATH = "research_tasks/TST_LEGACY_HEADING_COMPAT.md"
LIVE_PATH = "research_tasks/TST_CURRENT_HEADING_COMPAT.md"

CURRENT_BODY = """# Current task

## Mother question

Current mother question.

## Frozen inputs and scope

Current frozen inputs.

## Hard target and required outputs

Current hard target.

## Research value to preserve

Current research value.

## Success, kill, and return criteria

Current success criteria.
"""

LEGACY_BODY = """# Historical task

## Mother question

Historical mother question.

## Frozen inputs

Historical frozen inputs.

## Hard target

Historical hard target and outputs.

## Research value

Historical research value.

## Success and kill criteria

Historical success and kill criteria.
"""


def _meta() -> dict[str, object]:
    return {
        "task_id": TASK_ID,
        "parent_objective_id": PARENT,
        "task_authority": "PUBLISHED_REGISTERED",
        "base_state": "READY",
    }


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def _write_fixture(
    root: Path,
    *,
    historical_body: str = LEGACY_BODY,
    include_waiver: bool = True,
) -> tuple[Path, str]:
    hist_path = root / HIST_PATH
    live_path = root / LIVE_PATH
    hist_path.parent.mkdir(parents=True, exist_ok=True)
    hist_path.write_text(research_taskbook.render_taskbook(_meta(), historical_body), encoding="utf-8")
    live_path.write_text(research_taskbook.render_taskbook(_meta(), CURRENT_BODY), encoding="utf-8")
    hist_blob = records.taskbook_blob(hist_path)
    live_blob = records.taskbook_blob(live_path)

    base_record = {
        "record_schema": records.RECORD_SCHEMA,
        "record_state": "ACTIVE",
        "task_id": TASK_ID,
        "registry_key": TASK_ID,
        "publication_transaction": records.PUBLICATION_TRANSACTION_V2,
        "parent_objective_id": PARENT,
        "working_truth_granted": False,
        "canonical_promotion_granted": False,
    }
    _write_json(
        root / "research_task_records" / TASK_ID / f"{HIST}.json",
        {
            **base_record,
            "publication_id": HIST,
            "taskbook_path": HIST_PATH,
            "taskbook_blob_sha1": hist_blob,
        },
    )
    _write_json(
        root / "research_task_records" / TASK_ID / f"{LIVE}.json",
        {
            **base_record,
            "publication_id": LIVE,
            "taskbook_path": LIVE_PATH,
            "taskbook_blob_sha1": live_blob,
        },
    )
    _write_json(
        root / records.RESOLUTION_FILE,
        {
            "schema": records.RESOLUTION_SCHEMA,
            "status": "ACTIVE",
            "resolutions": [
                {
                    "task_id": TASK_ID,
                    "canonical_publication_id": LIVE,
                    "quarantined_publication_ids": [HIST],
                    "working_truth_granted": False,
                    "canonical_promotion_granted": False,
                    "successor_triggered": False,
                }
            ],
        },
    )
    if include_waiver:
        _write_json(
            root / records.COMPATIBILITY_FILE,
            {
                "schema": records.COMPATIBILITY_SCHEMA,
                "status": "ACTIVE",
                "waivers": [
                    {
                        "waiver_id": "TRCW-TEST-HIST",
                        "task_id": TASK_ID,
                        "publication_id": HIST,
                        "taskbook_path": HIST_PATH,
                        "taskbook_blob_sha1": hist_blob,
                        "scope": records.COMPATIBILITY_SCOPE,
                        "legacy_section_aliases": {
                            "Frozen inputs and scope": "Frozen inputs",
                            "Hard target and required outputs": "Hard target",
                            "Research value to preserve": "Research value",
                            "Success, kill, and return criteria": "Success and kill criteria",
                        },
                        "operational": False,
                        "history_preserved": True,
                        "working_truth_granted": False,
                        "foundation_authority_granted": False,
                        "canonical_promotion_granted": False,
                        "successor_triggered": False,
                    }
                ],
            },
        )
    return hist_path, hist_blob


class TaskRecordCompatibilityTests(unittest.TestCase):
    def test_current_repository_task_record_audit_passes(self) -> None:
        self.assertEqual([], records.audit(records.ROOT))

    def test_exact_blob_pinned_legacy_aliases_pass(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            _write_fixture(root)
            self.assertEqual([], records.audit(root))

    def test_same_legacy_body_without_waiver_fails(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            _write_fixture(root, include_waiver=False)
            errors = records.audit(root)
            self.assertTrue(any("Frozen inputs and scope" in item for item in errors))
            self.assertTrue(any("Success, kill, and return criteria" in item for item in errors))

    def test_blob_drift_is_never_waived(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            hist_path, _ = _write_fixture(root)
            hist_path.write_text(hist_path.read_text(encoding="utf-8") + "\nDRIFT\n", encoding="utf-8")
            errors = records.audit(root)
            self.assertTrue(any("taskbook blob drift" in item for item in errors))
            self.assertTrue(any("pinned taskbook blob drift" in item for item in errors))

    def test_extra_missing_current_section_exceeds_waiver_scope(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            body = LEGACY_BODY.replace(
                "## Mother question\n\nHistorical mother question.\n\n", ""
            )
            _write_fixture(root, historical_body=body)
            errors = records.audit(root)
            self.assertTrue(
                any("waiver scope does not exactly equal current body-policy errors" in item for item in errors)
            )
            self.assertTrue(any("Mother question" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
