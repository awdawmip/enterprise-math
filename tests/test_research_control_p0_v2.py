import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools import research_dispatch as dispatch
from tools import research_execution_records as executions
from tools import research_result_records as results
from tools import research_runtime_guard as guard
from tools import research_task_records as records

ROOT = Path(__file__).resolve().parents[1]
REGISTERED_TASK = "RS-QUADRATIC-PACKET-HIGHER-JET-AUTOMORPHISM-NO-SECTION-INDEPENDENT-AUDIT"


def runtime_state(task_id, registration=None):
    return {
        "parent_objective": {"objective_id": "OBJ-P0-TEST", "status": "OPEN"},
        "task_registration": registration or {"state": "DONE", "registry_key": task_id},
        "task": {
            "task_id": task_id,
            "status": "ACTIVE",
            "taskbook_source": "source",
            "owner_branch": "owner/test",
        },
        "owner_claim": {
            "claim_id": "claim-1",
            "researcher_id": "EM-TEST-ABC123",
            "owner_lease_until": "2026-08-26T12:00:00+08:00",
        },
        "session": {"session_id": "session-1", "last_activity_at": "2026-08-25T12:00:00+08:00"},
        "durable_frontier": {"remote_head": "deadbeef", "execution_stamp": "stamp", "durable_outputs": []},
        "current_unfinished_unit": "unit",
        "next_action": {"description": "continue", "executable": True},
        "terminal_scope": None,
        "final_allowed": False,
        "control": {},
    }


def auth(comment_id, *, edited=False):
    return {
        "server_authenticated": True,
        "issue_number": 240,
        "comment_id": comment_id,
        "author_login": "awdawmip",
        "author_user_id": 30957095,
        "author_association": "OWNER",
        "control_authorized": True,
        "created_at": "2026-08-25T14:00:00+00:00",
        "updated_at": "2026-08-25T14:00:00+00:00",
        "body_sha256": "sha256:" + "a" * 64,
        "edited": edited,
        "performed_via_github_app": "chatgpt-codex-connector",
    }


class RuntimeAuthorizationTests(unittest.TestCase):
    def test_forged_registration_cannot_authorize_unknown_task(self):
        with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "neither immutably registered"):
            guard.canonicalize_registration(runtime_state("RS-DEFINITELY-NOT-A-REAL-TASK"), purpose="pre_final", root=ROOT)

    def test_caller_registration_state_is_replaced_by_repository_authority(self):
        safe = guard.canonicalize_registration(
            runtime_state(REGISTERED_TASK, registration={"state": "DONE", "registry_key": REGISTERED_TASK}),
            purpose="pre_final",
            root=ROOT,
        )
        self.assertEqual("IMMUTABLE_REGISTERED", safe["task_registration"]["state"])
        self.assertEqual(REGISTERED_TASK, safe["task_registration"]["registry_key"])
        self.assertTrue(safe["task_registration"]["publication_id"])

    def test_legacy_fresh_redispatch_is_rejected_even_with_forged_registration(self):
        state = runtime_state(
            "RS-P017-GLOBAL-CAPACITY",
            registration={"state": "LEGACY_BASELINE_REGISTERED", "fresh_redispatch": True},
        )
        with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "fresh redispatch"):
            guard.canonicalize_registration(state, purpose="pre_final", root=ROOT)


class ExecutionIntentTests(unittest.TestCase):
    def test_execution_intent_pins_publication_identity_branch_base_and_outputs(self):
        record = executions.prepare_intent(
            task_id=REGISTERED_TASK,
            claim_id="claim-test-1",
            researcher_id=None,
            theorem_owner="QUADRATIC_PACKET_FRONTIER",
            execution_branch="research/test-execution-intent",
            execution_branch_base="a" * 40,
            allowed_outputs=["research_returns/", "research_output/evidence/"],
            owner_lease_minutes=120,
            prepared_at="2026-08-25T22:30:00+08:00",
            root=ROOT,
        )
        current = records.current_records(ROOT)[REGISTERED_TASK]
        self.assertEqual(current["publication_id"], record["publication_id"])
        self.assertEqual(current["taskbook_blob_sha1"], record["taskbook_blob_sha1"])
        self.assertEqual("claim-test-1", record["claim_id"])
        self.assertEqual("QUADRATIC_PACKET_FRONTIER", record["theorem_owner"])
        self.assertEqual("research/test-execution-intent", record["execution_branch"])
        self.assertEqual("a" * 40, record["execution_branch_base"])
        self.assertEqual(["research_returns/", "research_output/evidence/"], record["allowed_outputs"])
        self.assertTrue(record["researcher_id"].startswith("EM-QPHJA-"))


class UnifiedDispatchTests(unittest.TestCase):
    def setUp(self):
        # These tests exercise event/dispatch semantics, not the mutable live
        # repository result overlay. The real QPHJA task is now terminal, so pin
        # a no-result fixture here instead of allowing production progress to
        # change the meaning of the control-plane unit tests.
        self._result_state_patch = mock.patch.object(
            dispatch.research_result_records, "task_result_state", return_value=None
        )
        self._result_state_patch.start()
        self.addCleanup(self._result_state_patch.stop)

    def registered_definition(self):
        return next(item for item in dispatch.merged_definitions(ROOT) if item["task_id"] == REGISTERED_TASK)

    def inline_claim(self, **overrides):
        task = self.registered_definition()
        value = {
            "schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V1",
            "event": "CLAIM",
            "task_id": REGISTERED_TASK,
            "actor": "test",
            "at": "2026-08-25T22:00:00+08:00",
            "claim_id": "inline-claim-1",
            "publication_id": task["publication_id"],
            "theorem_owner": "QUADRATIC_PACKET_FRONTIER",
            "execution_branch": "research/inline-claim-test",
            "execution_branch_base": "a" * 40,
            "allowed_outputs": ["research_returns/", "research_output/evidence/"],
            "lease_minutes": 120,
            "_github": auth(1001),
        }
        value.update(overrides)
        return value

    def test_registered_and_legacy_tasks_share_one_view_without_duplicates(self):
        definitions = dispatch.merged_definitions(ROOT)
        by_id = {item["task_id"]: item for item in definitions}
        self.assertEqual(len(definitions), len(by_id))
        self.assertEqual("IMMUTABLE_TASK_RECORD", by_id[REGISTERED_TASK]["registration_source"])
        self.assertEqual("FROZEN_LEGACY_BASELINE", by_id["RS-P017-GLOBAL-CAPACITY"]["registration_source"])

    def test_registered_task_is_dispatchable_without_static_scheduler_row(self):
        state = dispatch.reduce_definition(
            self.registered_definition(),
            [],
            now=dispatch.research_scheduler.parse_time("2026-08-25T22:20:00+08:00"),
            root=ROOT,
        )
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        self.assertEqual("IMMUTABLE_TASK_RECORD", state["registration_source"])

    def test_bare_registered_live_event_is_not_runtime_authority(self):
        event = self.inline_claim()
        event.pop("_github")
        state = dispatch.reduce_definition(
            self.registered_definition(),
            [event],
            now=dispatch.research_scheduler.parse_time("2026-08-25T22:02:00+08:00"),
            root=ROOT,
        )
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        self.assertTrue(any("server-authenticated" in item["reason"] for item in state["ignored_events"]))

    def test_incomplete_registered_claim_envelope_is_ignored(self):
        events = [{
            "schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V1",
            "event": "CLAIM",
            "task_id": REGISTERED_TASK,
            "actor": "test",
            "at": "2026-08-25T22:00:00+08:00",
            "claim_id": "missing-envelope",
            "lease_minutes": 120,
            "_github": auth(1002),
        }]
        state = dispatch.reduce_definition(
            self.registered_definition(),
            events,
            now=dispatch.research_scheduler.parse_time("2026-08-25T22:02:00+08:00"),
            root=ROOT,
        )
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        self.assertTrue(any("publication_id" in item["reason"] for item in state["ignored_events"]))

    def test_inline_claim_envelope_needs_no_preclaim_repository_record(self):
        event = self.inline_claim()
        with mock.patch.object(dispatch.research_execution_records, "intent_for_claim", return_value=None):
            state = dispatch.reduce_definition(
                self.registered_definition(),
                [event],
                now=dispatch.research_scheduler.parse_time("2026-08-25T22:02:00+08:00"),
                root=ROOT,
            )
        self.assertEqual("LEASED", state["dispatch_state"])
        self.assertEqual("inline-claim-1", state["claim_id"])
        self.assertTrue(state["researcher_id"].startswith("EM-QPHJA-"))
        self.assertFalse(state["ignored_events"])
        self.assertEqual("GITHUB_SERVER_COMMENT_ENVELOPE", state["event_authentication"])

    def test_inline_claim_rejects_stale_publication_without_extra_remote_write(self):
        event = self.inline_claim(publication_id="TP-STALE")
        with mock.patch.object(dispatch.research_execution_records, "intent_for_claim", return_value=None):
            state = dispatch.reduce_definition(
                self.registered_definition(),
                [event],
                now=dispatch.research_scheduler.parse_time("2026-08-25T22:02:00+08:00"),
                root=ROOT,
            )
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        self.assertTrue(any("publication_id" in item["reason"] for item in state["ignored_events"]))

    def test_edited_registered_event_does_not_mutate_runtime_history(self):
        event = self.inline_claim(_github=auth(1003, edited=True))
        state = dispatch.reduce_definition(
            self.registered_definition(),
            [event],
            now=dispatch.research_scheduler.parse_time("2026-08-25T22:02:00+08:00"),
            root=ROOT,
        )
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        self.assertTrue(any("edited scheduler event" in item["reason"] for item in state["ignored_events"]))

    def test_registered_done_without_reviewed_result_is_ignored_after_valid_intent(self):
        intent = {
            "task_id": REGISTERED_TASK,
            "claim_id": "c1",
            "researcher_id": "EM-QPHJA-ABC123",
            "owner_lease_minutes": 120,
        }
        events = [
            {"schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V1", "event": "CLAIM", "task_id": REGISTERED_TASK, "actor": "test", "at": "2026-08-25T22:00:00+08:00", "claim_id": "c1", "_github": auth(1010)},
            {"schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V1", "event": "DONE", "task_id": REGISTERED_TASK, "actor": "test", "at": "2026-08-25T22:01:00+08:00", "claim_id": "c1", "result_id": "RR-NOT-REVIEWED", "_github": auth(1011)},
        ]
        with mock.patch.object(dispatch.research_execution_records, "intent_for_claim", return_value=intent):
            state = dispatch.reduce_definition(
                self.registered_definition(),
                events,
                now=dispatch.research_scheduler.parse_time("2026-08-25T22:02:00+08:00"),
                root=ROOT,
            )
        self.assertEqual("LEASED", state["dispatch_state"])
        self.assertTrue(any("review" in item["reason"] for item in state["ignored_events"]))

    def test_unreviewed_frozen_result_is_not_researcher_dispatchable(self):
        pending = {
            "state": "AWAITING_DRIVER_REVIEW",
            "terminal": False,
            "result": {"result_id": "RR-PENDING", "_record_path": "research_result_records/test.json"},
            "review": None,
        }
        with mock.patch.object(dispatch.research_result_records, "task_result_state", return_value=pending):
            state = dispatch.reduce_definition(
                self.registered_definition(),
                [],
                now=dispatch.research_scheduler.parse_time("2026-08-25T22:02:00+08:00"),
                root=ROOT,
            )
        self.assertEqual("AWAITING_REVIEW", state["dispatch_state"])


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
            result = {"record_schema": results.RESULT_SCHEMA, "result_id": "RR-ONE", "task_id": "RS-T", "frozen_at": "2026-08-25T22:00:00+08:00"}
            review = {"record_schema": results.REVIEW_SCHEMA, "review_id": "DR-ONE", "result_id": "RR-ONE", "task_id": "RS-T", "driver_id": "EM-DVR-ABC123", "reviewed_at": "2026-08-25T22:01:00+08:00", "disposition": "ACCEPTED", "terminal": True}
            (result_dir / "RR-ONE.json").write_text(json.dumps(result), encoding="utf-8")
            (review_dir / "DR-ONE.json").write_text(json.dumps(review), encoding="utf-8")
            with mock.patch.object(
                results._driver_followup,
                "state_for_review",
                return_value={
                    "required": False,
                    "ready": True,
                    "state": "LEGACY_PRE_CUTOVER",
                    "packet": None,
                },
            ):
                state = results.task_result_state("RS-T", root)
            self.assertEqual("TERMINAL", state["state"])
            self.assertTrue(state["terminal"])


if __name__ == "__main__":
    unittest.main()
