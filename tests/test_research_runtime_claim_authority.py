import unittest
from pathlib import Path

from tools import research_runtime_guard as guard
from tools import research_scheduler as scheduler
from tools import research_task_records as records


ROOT = Path(__file__).resolve().parents[1]
TASK_ID = "RS-QUADRATIC-PACKET-HIGHER-JET-AUTOMORPHISM-NO-SECTION-INDEPENDENT-AUDIT"


def state(owner_claim=None):
    return {
        "parent_objective": {"objective_id": "OBJ-CLAIM-AUTH", "status": "OPEN"},
        "task_registration": {"state": "FORGED", "registry_key": TASK_ID},
        "task": {"task_id": TASK_ID, "status": "ACTIVE"},
        "owner_claim": owner_claim or {},
        "session": {"session_id": "s1", "last_activity_at": "2026-08-26T05:00:30+00:00"},
        "durable_frontier": {"remote_head": "a" * 40, "execution_stamp": "NONE", "durable_outputs": []},
        "current_unfinished_unit": "proof",
        "next_action": {"description": "continue", "executable": True},
        "terminal_scope": None,
        "final_allowed": False,
        "control": {},
    }


def auth(comment_id=8001, *, authorized=True):
    return {
        "server_authenticated": True,
        "issue_number": 240,
        "comment_id": comment_id,
        "author_login": "awdawmip" if authorized else "outsider",
        "author_user_id": 30957095 if authorized else 88,
        "author_association": "OWNER" if authorized else "NONE",
        "control_authorized": authorized,
        "created_at": "2026-08-26T05:00:00+00:00",
        "updated_at": "2026-08-26T05:00:00+00:00",
        "body_sha256": "sha256:" + "a" * 64,
        "edited": False,
        "performed_via_github_app": "chatgpt-codex-connector",
    }


def claim(*, authorized=True):
    record = records.current_records(ROOT)[TASK_ID]
    return {
        "schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V1",
        "event": "CLAIM",
        "task_id": TASK_ID,
        "actor": "descriptive-only",
        "at": "2026-08-26T05:00:00+00:00",
        "claim_id": "runtime-auth-claim-1",
        "publication_id": record["publication_id"],
        "theorem_owner": "QUADRATIC_PACKET_FRONTIER",
        "execution_branch": "research/runtime-claim-authority-test",
        "execution_branch_base": "b" * 40,
        "allowed_outputs": ["research_returns/", "research_output/evidence/"],
        "lease_minutes": 120,
        "_github": auth(authorized=authorized),
    }


class RegisteredRuntimeClaimAuthorityTests(unittest.TestCase):
    def test_registered_execution_without_issue_event_evidence_is_forbidden(self):
        with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "requires canonical Issue #240 event evidence"):
            guard.authorize_execution(state(), events=None, root=ROOT)

    def test_unauthorized_claim_cannot_authorize_execution(self):
        with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "current winning live"):
            guard.authorize_execution(
                state(),
                events=[claim(authorized=False)],
                now=scheduler.parse_time("2026-08-26T05:01:00+00:00"),
                root=ROOT,
            )

    def test_expired_claim_cannot_authorize_execution(self):
        with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "current winning live"):
            guard.authorize_execution(
                state(),
                events=[claim()],
                now=scheduler.parse_time("2026-08-26T08:00:00+00:00"),
                root=ROOT,
            )

    def test_caller_owner_claim_must_match_canonical_winner(self):
        with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "caller owner_claim.claim_id"):
            guard.authorize_execution(
                state({"claim_id": "forged-other-claim"}),
                events=[claim()],
                now=scheduler.parse_time("2026-08-26T05:01:00+00:00"),
                root=ROOT,
            )

    def test_winning_claim_authorizes_exact_execution_binding(self):
        result = guard.authorize_execution(
            state(),
            events=[claim()],
            now=scheduler.parse_time("2026-08-26T05:01:00+00:00"),
            root=ROOT,
        )
        binding = result["execution_binding"]
        current = records.current_records(ROOT)[TASK_ID]
        self.assertTrue(result["authorized"])
        self.assertEqual("CURRENT_AUTHORIZED_WINNING_ISSUE_240_CLAIM", result["authorization_authority"])
        self.assertEqual(current["publication_id"], binding["publication_id"])
        self.assertEqual("runtime-auth-claim-1", binding["claim_id"])
        self.assertEqual("research/runtime-claim-authority-test", binding["execution_branch"])
        self.assertEqual("b" * 40, binding["execution_branch_base"])
        self.assertEqual(["research_returns/", "research_output/evidence/"], binding["allowed_outputs"])
        self.assertEqual(8001, binding["server_comment_id"])
        self.assertEqual("awdawmip", binding["server_author_login"])
        self.assertEqual(binding["claim_id"], result["owner_claim"]["claim_id"])
        self.assertEqual(binding["researcher_id"], result["owner_claim"]["researcher_id"])


if __name__ == "__main__":
    unittest.main()
