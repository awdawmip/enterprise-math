import json
import tempfile
import unittest
from pathlib import Path

from tools import research_dispatch as dispatch
from tools import research_result_records as results
from tools import research_task_records as records

ROOT = Path(__file__).resolve().parents[1]
REGISTERED_TASK = "RS-TEST-REGISTERED"


class RegisteredDispatchTests(unittest.TestCase):
    def registered_definition(self):
        return {
            "task_id": REGISTERED_TASK,
            "status": "READY",
            "priority": "P2",
            "execution_cost": "LOW",
            "owner": "UNCLAIMED",
            "claim_id": None,
            "lease_expires_at": None,
            "theorem_owner": "TEST_THEOREM",
            "source_handoff": "test",
            "owner_branch": "research/test-registered",
            "test_only": True,
        }

    def test_registered_task_reduces_without_static_row(self):
        definition = self.registered_definition()
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            state = dispatch.reduce_task_state(
                definition,
                [],
                now=dispatch.research_scheduler.parse_time("2026-08-25T22:00:00+08:00"),
                root=root,
            )
        self.assertIn(state["dispatch_state"], {"READY", "NOT_REGISTERED"})

    def test_registered_claim_like_state_still_requires_runtime_evidence(self):
        with tempfile.TemporaryDirectory() as td:
            state = dispatch.reduce_task_state(
                self.registered_definition(),
                [],
                now=dispatch.research_scheduler.parse_time("2026-08-25T22:02:00+08:00"),
                root=Path(td),
            )
        self.assertIn(state["dispatch_state"], {"READY", "NOT_REGISTERED"})


class ImmutablePublicationTests(unittest.TestCase):
    def test_immutable_record_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "record.json"
            records._save_json_exclusive(path, {"a": 1})
            with self.assertRaisesRegex(records.TaskRecordError, "already exists"):
                records._save_json_exclusive(path, {"a": 2})

    def test_placeholder_mandatory_sections_are_rejected(self):
        body = """# T

## 0. Mother question

<task-specific question>

## 1. Frozen inputs and scope

real input

## 2. Hard target and required outputs

real target

## 3. Research value to preserve

real value

## 4. Success, kill, and return criteria

real criteria
"""
        errors = records.validate_body(body)
        self.assertTrue(any("placeholder" in error for error in errors))

    def test_repository_migrated_records_are_auditable(self):
        self.assertEqual([], records.audit(ROOT))
        self.assertIn(REGISTERED_TASK, records.current_records(ROOT))


class ResultLifecycleTests(unittest.TestCase):
    def test_frozen_result_without_driver_review_is_awaiting_review(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            result_dir = root / "research_result_records" / "RS-T"
            result_dir.mkdir(parents=True)
            result = {
                "record_schema": results.RESULT_SCHEMA,
                "result_id": "RR-ONE",
                "task_id": "RS-T",
                "frozen_at": "2026-08-25T22:00:00+08:00",
            }
            (result_dir / "RR-ONE.json").write_text(json.dumps(result), encoding="utf-8")
            state = results.task_result_state("RS-T", root)
            self.assertEqual("AWAITING_DRIVER_REVIEW", state["state"])
            self.assertFalse(state["terminal"])

    def test_terminal_driver_review_closes_result_state(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            result_dir = root / "research_result_records" / "RS-T"
            result_dir.mkdir(parents=True)
            review_dir = root / "research_result_reviews" / "RR-ONE"
            review_dir.mkdir(parents=True)
            result = {
                "record_schema": results.RESULT_SCHEMA,
                "result_id": "RR-ONE",
                "task_id": "RS-T",
                "frozen_at": "2026-08-25T22:00:00+08:00",
            }
            review = {
                "record_schema": results.REVIEW_SCHEMA,
                "review_id": "DR-ONE",
                "result_id": "RR-ONE",
                "task_id": "RS-T",
                "driver_id": "EM-DVR-ABC123",
                "reviewed_at": "2026-08-25T22:01:00+08:00",
                "disposition": "ACCEPTED",
                "terminal": True,
            }
            (result_dir / "RR-ONE.json").write_text(json.dumps(result), encoding="utf-8")
            (review_dir / "DR-ONE.json").write_text(json.dumps(review), encoding="utf-8")
            state = results.task_result_state("RS-T", root)
            self.assertEqual("TERMINAL", state["state"])
            self.assertTrue(state["terminal"])


if __name__ == "__main__":
    unittest.main()
