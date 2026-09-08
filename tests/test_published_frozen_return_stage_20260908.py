"""Real prepared publications retain a non-executable initial review stage."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

from control_plane import research_control_bootstrap as bootstrap
from control_plane import research_task_records_impl as publication_core
from tools import research_dispatch as dispatch
from tools import research_runtime as runtime
from tools import research_runtime_reducer as reducer
from tools import research_task_records as records
from tools import research_taskbook as taskbooks
import research_control_dispatch as router

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))
from test_research_task_record_compatibility import _write_semantic_fixture

TASK_ID = "RS-A3-A4-GENERATED-SUPPORT"
OLD_RECORD = "research_task_records/RS-A3-A4-GENERATED-SUPPORT/TP2-F4F7A34423E2D6CDC0CF.json"
OLD_BOOK = "research_tasks/LEGACY_CONTROL_MIGRATION_RS_A3_A4_GENERATED_SUPPORT_20260902.md"
PUBLISHED = "2026-09-08T00:00:00+00:00"
CLAIMED = "2026-09-08T00:05:00+00:00"
NOW = reducer.parse_time("2026-09-08T00:25:00+00:00")


def setUpModule():
    bootstrap.install(ROOT)


class PublishedFrozenReturnStageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="em-fr-stage-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        policy = taskbooks.policy_manifest(ROOT)
        for relative in {
            "research_taskbook_policy.json", *policy["policy_inputs"],
            "research_control_event_authorization.json", "research_runtime_policy_v2.json",
            OLD_RECORD, OLD_BOOK,
        }:
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT / relative).read_bytes())
        # Real unrelated semantic-fault fixture satisfies the canonical installed
        # validators. No source validator, publication selector or Result is mocked.
        _write_semantic_fixture(self.root)
        self.old_bytes = {path: (self.root / path).read_bytes() for path in (OLD_RECORD, OLD_BOOK)}
        self.old_record = json.loads(self.old_bytes[OLD_RECORD])
        self.original_meta, self.original_body = taskbooks.split_taskbook(self.old_bytes[OLD_BOOK].decode())

    def publish(self, state, *, task_id=TASK_ID, hard_block=None, next_action="Driver review of the preserved return"):
        meta = copy.deepcopy(self.original_meta)
        meta.update(task_id=task_id, base_state=state, next_action=next_action, hard_block=hard_block)
        path = self.root / "research_tasks" / f"{task_id}_{state}_fixture.md"
        path.write_text(taskbooks.render_taskbook(meta, self.original_body), encoding="utf-8", newline="\n")
        prepared = records.prepare_taskbook(path, publisher_role="RESEARCH_DRIVER",
            parent_objective_id=meta["parent_objective_id"], root=self.root)
        checked, body = publication_core._prepared(path, self.root)
        self.assertEqual(prepared, checked)
        self.assertEqual(state, checked["base_state"])
        self.assertEqual(self.original_body, body)
        self.assertEqual("PASS", checked["policy_review"]["review_state"])
        self.assertEqual(taskbooks.policy_digest(self.root), checked["policy_review"]["policy_digest"])
        record = records.build_record(checked, path=path, publisher_role="RESEARCH_DRIVER",
            publisher_id="EM-DVR-TEMP-FIXTURE", research_value=self.old_record["research_value"],
            published_at=PUBLISHED,
            supersedes_publication_id=self.old_record["publication_id"] if task_id == TASK_ID else None,
            root=self.root)
        target = records.record_path(self.root, task_id, record["publication_id"])
        publication_core._save_json_exclusive(target, record)
        self.assertEqual([], records.audit(self.root))
        self.assertTrue(record["claimable"])
        self.assertEqual("ACTIVE", record["record_state"])
        self.assertFalse(record["working_truth_granted"])
        self.assertFalse(record["canonical_promotion_granted"])
        current = records.current_records(self.root)[task_id]
        self.assertEqual(record["publication_id"], current["publication_id"])
        definition = next(value for value in dispatch.merged_definitions(self.root) if value["task_id"] == task_id)
        return record, definition

    def comment(self, definition, kind="CLAIM", comment_id=1, at=CLAIMED, **changes):
        # Synthetic server objects exist only inside TEMP execution tests; no
        # Issue comment, identity, execution record or claim is persisted.
        payload = {"schema": reducer.EVENT_SCHEMA, "event": kind,
            "task_id": definition["task_id"], "publication_id": definition["publication_id"],
            "claim_id": "temporary-fixture-claim", "theorem_owner": definition["owner"],
            "execution_branch": "research/temporary-frozen-stage-fixture", "execution_branch_base": "a" * 40,
            "allowed_outputs": ["research_returns/temporary-fixture/"], "lease_minutes": 120}
        payload.update(changes)
        raw = {"id": comment_id, "body": json.dumps(payload),
            "issue_url": dispatch.GITHUB_ISSUE_URL, "created_at": at, "updated_at": at,
            "user": {"login": "awdawmip", "id": 30957095}, "author_association": "OWNER"}
        return dispatch.github_comment_event(raw, root=self.root)

    def reduce(self, definition, events=()):
        return dispatch.reduce_definition(definition, list(events), now=NOW, root=self.root)

    def test_superseding_frozen_return_keeps_review_stage_and_original_bytes(self):
        record, definition = self.publish("FROZEN_RETURN")
        self.assertEqual(2, record["publication_generation"])
        self.assertEqual(self.old_record["publication_id"], record["supersedes_publication_id"])
        for key in ("task_id", "owner", "frontier", "parent_objective_id", "origin_kind", "task_lineage", "parent_task_id"):
            self.assertEqual(self.old_record[key], record[key], key)
        for path, content in self.old_bytes.items():
            self.assertEqual(content, (self.root / path).read_bytes(), path)
        self.assertEqual("FROZEN_RETURN", definition["base_state"])
        state = self.reduce(definition)
        self.assertEqual("FROZEN_RETURN", state["state"])
        self.assertEqual("AWAITING_REVIEW", state["dispatch_state"])
        self.assertIsNone(state["claim_id"])
        self.assertIsNone(dispatch.research_result_records.task_result_state(TASK_ID, self.root))
        selected = reducer.select_state([state], reducer.load_policy(self.root))
        self.assertIsNone(selected)
        route = router.route_from_candidates([], observations={}, now=NOW, fresh_task=selected, fresh_lane=None)
        self.assertEqual(runtime.NO_DISPATCH, route["action"])
        self.assertFalse(route["new_claim_required"])

    def test_frozen_initial_stage_rejects_otherwise_valid_current_claim(self):
        _, definition = self.publish("FROZEN_RETURN")
        state = self.reduce(definition, [self.comment(definition)])
        self.assertEqual("AWAITING_REVIEW", state["dispatch_state"])
        self.assertIsNone(state["claim_id"])
        self.assertTrue(any(item["reason"] == "task is not dispatchable" for item in state["ignored_events"]))

    def test_ordinary_handoff_keeps_fresh_and_typed_continuation_routes(self):
        _, definition = self.publish("HANDOFF_READY")
        state = self.reduce(definition)
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        selected = reducer.select_state([state], reducer.load_policy(self.root))
        route = router.route_from_candidates([], observations={}, now=NOW, fresh_task=selected, fresh_lane=None)
        self.assertEqual(runtime.CLAIM_NEW_OWNER, route["action"])
        resumed = self.reduce(definition, [self.comment(definition), self.comment(definition, "HANDOFF", 2,
            "2026-09-08T00:10:00+00:00", handoff_scope="CONTINUATION", next_action="Continue the preserved unit")])
        self.assertEqual("HANDOFF_READY", resumed["state"])
        self.assertEqual("NEEDS_DISPATCH", resumed["dispatch_state"])

    def test_ready_claim_and_existing_owner_session_recovery_are_preserved(self):
        _, definition = self.publish("READY")
        state = self.reduce(definition, [self.comment(definition)])
        self.assertEqual("LEASED", state["dispatch_state"])
        self.assertEqual("temporary-fixture-claim", state["claim_id"])
        stale = runtime.dispatch_decision(state, session_last_activity_at=CLAIMED, now=NOW)
        self.assertEqual(runtime.ADOPT_OWNER_CLAIM, stale["action"])
        self.assertTrue(stale["owner_claim_preserved"])
        self.assertFalse(stale["new_claim_required"])
        active = runtime.dispatch_decision(state, session_last_activity_at=NOW.isoformat(), now=NOW)
        self.assertEqual(runtime.KEEP_CURRENT_SESSION, active["action"])
        self.assertFalse(active["new_claim_required"])

    def test_blocked_initial_stage_and_hard_block_remain_unchanged(self):
        hard_block = {"owner": "fixture-dependency-owner", "missing_object": "fixture dependency",
            "necessity": "the current unit needs this dependency", "unblock_condition": "supply the dependency"}
        _, definition = self.publish("BLOCKED", hard_block=hard_block)
        state = self.reduce(definition)
        self.assertEqual("BLOCKED", state["dispatch_state"])
        self.assertEqual(hard_block, state["hard_block"])
        self.assertIsNone(reducer.select_state([state], reducer.load_policy(self.root)))

    def test_review_stage_is_generic_and_does_not_infer_from_prose(self):
        _, waiting = self.publish("FROZEN_RETURN", task_id="RS-ANOTHER-REVIEW-FIXTURE", next_action="Inspect the preserved artifact")
        _, ready = self.publish("READY", task_id="RS-ANOTHER-READY-FIXTURE", next_action="Driver review PR #955")
        self.assertEqual("AWAITING_REVIEW", self.reduce(waiting)["dispatch_state"])
        self.assertEqual("NEEDS_DISPATCH", self.reduce(ready)["dispatch_state"])


if __name__ == "__main__":
    unittest.main()
