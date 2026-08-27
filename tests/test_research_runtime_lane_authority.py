import unittest
from unittest import mock

from tools import research_runtime_guard as guard
from tools import research_scheduler as scheduler


TASK_ID = "RS-LANE-TEST"
CURRENT = {
    "task_id": TASK_ID,
    "publication_id": "TP2-CURRENT",
    "record_state": "ACTIVE",
    "claimable": True,
    "_record_path": "research_task_records/RS-LANE-TEST/TP2-CURRENT.json",
}
LANE_RECORD = {
    "task_id": TASK_ID,
    "publication_id": "TP2-RETAINED",
    "record_state": "ACTIVE",
    "claimable": True,
    "_record_path": "research_task_records/RS-LANE-TEST/TP2-RETAINED.json",
}


def runtime_state(*, scope=None, owner_claim=None):
    value = {
        "task": {"task_id": TASK_ID, "status": "ACTIVE"},
        "task_registration": {"state": "FORGED", "registry_key": TASK_ID},
        "owner_claim": owner_claim or {},
        "parent_objective": {"objective_id": "OBJ-LANE", "status": "OPEN"},
        "session": {"session_id": "s", "last_activity_at": "2026-08-27T00:00:00+00:00"},
        "durable_frontier": {"remote_head": "a" * 40, "execution_stamp": "NONE", "durable_outputs": []},
        "current_unfinished_unit": "lane work",
        "next_action": {"description": "continue lane", "executable": True},
        "terminal_scope": None,
        "final_allowed": False,
        "control": {},
    }
    if scope is not None:
        value["execution_scope"] = scope
    return value


def scope():
    return {"execution_cohort_id": "EC-1", "execution_lane_id": "audit"}


def lane_binding():
    return {
        "task_id": TASK_ID,
        "publication_id": "TP2-RETAINED",
        "taskbook_blob_sha1": "sha1:" + "2" * 40,
        "execution_cohort_id": "EC-1",
        "execution_lane_id": "audit",
        "lane_role": "AUDIT",
        "lane_output_prefix": "research_returns/parallel/EC-1/audit/",
        "claim_id": "claim-audit",
        "researcher_id": "EM-AUDIT-ABC123",
        "theorem_owner": "TEST_OWNER",
        "execution_branch": "research/audit",
        "execution_branch_base": "b" * 40,
        "allowed_outputs": ["research_returns/parallel/EC-1/audit/"],
        "owner_lease_until": "2026-08-27T02:00:00+00:00",
        "server_comment_id": 5001,
        "server_author_login": "awdawmip",
        "server_author_user_id": 30957095,
        "binding_source": "CURRENT_AUTHORIZED_WINNING_ISSUE_240_LANE_CLAIM",
    }


class RuntimeLaneAuthorityTests(unittest.TestCase):
    def base_patches(self, *, cohort_terminal=False):
        return (
            mock.patch.object(guard.research_task_records, "current_records", return_value={TASK_ID: dict(CURRENT)}),
            mock.patch.object(
                guard.research_cohort_runtime,
                "active_cohorts",
                return_value=[{"cohort_id": "EC-1", "task_id": TASK_ID, "record_state": "ACTIVE"}],
            ),
            mock.patch.object(
                guard.research_lane_claims,
                "lane_scope",
                return_value={
                    "task_id": TASK_ID,
                    "execution_cohort_id": "EC-1",
                    "execution_lane_id": "audit",
                    "publication_id": "TP2-RETAINED",
                    "publication_record": dict(LANE_RECORD),
                    "lane_role": "AUDIT",
                    "output_prefix": "research_returns/parallel/EC-1/audit/",
                },
            ),
            mock.patch.object(
                guard.research_cohort_runtime,
                "cohort_state",
                return_value={
                    "state": "PARALLEL_SYNTHESIS_TERMINAL" if cohort_terminal else "COHORT_EXECUTION_ACTIVE",
                    "terminal": cohort_terminal,
                },
            ),
        )

    def test_active_cohort_rejects_task_global_execution(self):
        patches = self.base_patches()
        with patches[0], patches[1], patches[2], patches[3]:
            with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "exact lane execution_scope"):
                guard.authorize_execution(runtime_state(), events=[])

    def test_exact_lane_scope_uses_lane_winner(self):
        patches = self.base_patches()
        with patches[0], patches[1], patches[2], patches[3], mock.patch.object(
            guard.research_lane_claims,
            "winning_lane_claim_binding",
            return_value=lane_binding(),
        ):
            result = guard.authorize_execution(
                runtime_state(scope=scope()),
                events=[{"raw": "fixture"}],
                now=scheduler.parse_time("2026-08-27T00:10:00+00:00"),
            )
        self.assertTrue(result["authorized"])
        self.assertEqual("CURRENT_AUTHORIZED_WINNING_ISSUE_240_LANE_CLAIM", result["authorization_authority"])
        self.assertEqual("TP2-RETAINED", result["task_registration"]["publication_id"])
        self.assertEqual("EC-1", result["execution_binding"]["execution_cohort_id"])
        self.assertEqual("audit", result["owner_claim"]["execution_lane_id"])

    def test_old_task_global_terminal_result_does_not_block_explicit_active_lane(self):
        patches = self.base_patches()
        with patches[0], patches[1], patches[2], patches[3], mock.patch.object(
            guard.research_result_records,
            "task_result_state",
            return_value={"state": "TERMINAL", "terminal": True},
        ), mock.patch.object(
            guard.research_lane_claims,
            "winning_lane_claim_binding",
            return_value=lane_binding(),
        ):
            result = guard.authorize_execution(
                runtime_state(scope=scope()),
                events=[{"raw": "fixture"}],
                now=scheduler.parse_time("2026-08-27T00:10:00+00:00"),
            )
        self.assertTrue(result["authorized"])
        self.assertEqual("AUDIT", result["execution_binding"]["lane_role"])

    def test_terminal_cohort_synthesis_blocks_further_lane_execution(self):
        patches = self.base_patches(cohort_terminal=True)
        with patches[0], patches[1], patches[2], patches[3]:
            with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "terminal after exact two-pass synthesis"):
                guard.authorize_execution(runtime_state(scope=scope()), events=[])

    def test_caller_cannot_forge_different_lane_owner(self):
        patches = self.base_patches()
        forged_owner = {
            "claim_id": "claim-audit",
            "researcher_id": "EM-AUDIT-ABC123",
            "execution_cohort_id": "EC-1",
            "execution_lane_id": "research",
        }
        with patches[0], patches[1], patches[2], patches[3], mock.patch.object(
            guard.research_lane_claims,
            "winning_lane_claim_binding",
            return_value=lane_binding(),
        ):
            with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "execution_lane_id"):
                guard.authorize_execution(
                    runtime_state(scope=scope(), owner_claim=forged_owner),
                    events=[{"raw": "fixture"}],
                    now=scheduler.parse_time("2026-08-27T00:10:00+00:00"),
                )

    def test_partial_execution_scope_fails_closed(self):
        with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "both execution_cohort_id"):
            guard.authorize_execution(
                runtime_state(scope={"execution_cohort_id": "EC-1"}),
                events=[],
            )


if __name__ == "__main__":
    unittest.main()
