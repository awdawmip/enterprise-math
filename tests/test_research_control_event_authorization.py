import json
import unittest
from unittest import mock

from tools import research_dispatch as dispatch


ISSUE_URL = "https://api.github.com/repos/awdawmip/enterprise-math/issues/240"


def event_body(task_id="RS-T", claim_id="claim-1"):
    return json.dumps(
        {
            "schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V1",
            "event": "CLAIM",
            "task_id": task_id,
            "claim_id": claim_id,
            "actor": "body-is-not-authority",
            "at": "1900-01-01T00:00:00Z",
        },
        separators=(",", ":"),
    )


def comment(*, login="awdawmip", user_id=30957095, association="OWNER"):
    return {
        "id": 7001,
        "issue_url": ISSUE_URL,
        "user": {"login": login, "id": user_id},
        "author_association": association,
        "created_at": "2026-08-26T05:00:00Z",
        "updated_at": "2026-08-26T05:00:00Z",
        "body": event_body(),
        "performed_via_github_app": None,
    }


class ControlEventAuthorizationTests(unittest.TestCase):
    def test_exact_owner_server_actor_is_authorized_without_app_dependency(self):
        event = dispatch.github_comment_event(comment())
        self.assertIsNotNone(event)
        self.assertTrue(event["_github"]["control_authorized"])
        self.assertEqual("awdawmip", event["_github"]["author_login"])
        self.assertEqual(30957095, event["_github"]["author_user_id"])
        self.assertEqual("OWNER", event["_github"]["author_association"])

    def test_login_id_and_association_are_all_authority_fields(self):
        for override in (
            {"login": "outsider"},
            {"user_id": 1},
            {"association": "CONTRIBUTOR"},
        ):
            event = dispatch.github_comment_event(comment(**override))
            self.assertIsNotNone(event)
            self.assertFalse(event["_github"]["control_authorized"], override)

    def test_unauthorized_event_is_ignored_not_stream_dos(self):
        event = dispatch.github_comment_event(comment(login="outsider", user_id=88, association="NONE"))
        task = {"task_id": "RS-T", "registration_source": "IMMUTABLE_TASK_RECORD"}
        accepted, rejected = dispatch._event_authentication_filter(task, [event])
        self.assertEqual([], accepted)
        self.assertEqual(1, len(rejected))
        self.assertIn("not authorized", rejected[0]["reason"])

    def test_body_actor_cannot_compensate_for_unauthorized_github_actor(self):
        raw = comment(login="outsider", user_id=88, association="NONE")
        payload = json.loads(raw["body"])
        payload["actor"] = "awdawmip"
        payload["researcher_id"] = "EM-T-ABC123"
        raw["body"] = json.dumps(payload)
        event = dispatch.github_comment_event(raw)
        self.assertFalse(event["_github"]["control_authorized"])


if __name__ == "__main__":
    unittest.main()
