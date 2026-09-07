import unittest
from pathlib import Path
from unittest import mock

from tools import research_dispatch as rd
from tools import research_runtime_reducer as rr


TASK_ID = "RS-INTENT-GEN-SIM"
CURRENT_PUBLICATION = "TP2-CURRENT-INTENT"
OLD_PUBLICATION = "TP2-OLD-INTENT"


def task():
    return {
        "task_id": TASK_ID,
        "title": "Synthetic intent generation gate",
        "kind": "RESEARCH",
        "owner": "taskbook/unassigned",
        "base_state": "READY",
        "priority": "P0",
        "leverage": "HIGH",
        "frontier": "simulation",
        "next_action": "continue",
        "dependencies": [],
        "source_refs": [],
        "last_progress_at": "2026-09-01T00:00:00+00:00",
        "hard_block": None,
        "claim_lease_minutes": 30,
        "identity_lane": "INTENTGEN",
        "publication_id": CURRENT_PUBLICATION,
        "taskbook_blob_sha1": "sha1:" + "2" * 40,
        "registration_source": "IMMUTABLE_TASK_RECORD",
    }


def event(publication_marker=...):
    value = {
        "schema": rr.EVENT_SCHEMA,
        "event": "CLAIM",
        "task_id": TASK_ID,
        "claim_id": "claim-intent-generation",
        "at": "2026-09-01T00:01:00+00:00",
        "researcher_id": "EM-INTENTGEN-7A4C21",
        rd.GITHUB_META_KEY: {
            "server_authenticated": True,
            "issue_number": 240,
            "comment_id": 101,
            "author_login": "awdawmip",
            "author_user_id": 30957095,
            "author_association": "OWNER",
            "control_authorized": True,
            "created_at": "2026-09-01T00:01:00+00:00",
            "updated_at": "2026-09-01T00:01:00+00:00",
            "edited": False,
        },
    }
    if publication_marker is not ...:
        value["publication_id"] = publication_marker
    return value


def intent(publication_id):
    return {
        "record_schema": "ENTERPRISE_MATH_RESEARCH_EXECUTION_RECORD_V1",
        "record_state": "CLAIM_INTENT",
        "task_id": TASK_ID,
        "claim_id": "claim-intent-generation",
        "publication_id": publication_id,
        "researcher_id": "EM-INTENTGEN-7A4C21",
        "owner_lease_minutes": 30,
    }


class ExecutionIntentPublicationGateTests(unittest.TestCase):
    def filter(self, claim_event, execution_intent):
        with mock.patch.object(
            rd.research_execution_records,
            "intent_for_claim",
            return_value=execution_intent,
        ):
            return rd._filter_registered_events(
                task(), [claim_event], Path("."), result_state=None
            )

    def test_old_generation_intent_cannot_authorize_current_generation_claim(self):
        accepted, rejected = self.filter(
            event(CURRENT_PUBLICATION), intent(OLD_PUBLICATION)
        )
        self.assertEqual([], accepted)
        self.assertTrue(any("execution intent publication_id" in item["reason"] for item in rejected))

    def test_old_generation_intent_cannot_authorize_publicationless_claim(self):
        accepted, rejected = self.filter(event(), intent(OLD_PUBLICATION))
        self.assertEqual([], accepted)
        self.assertTrue(any("execution intent publication_id" in item["reason"] for item in rejected))

    def test_current_intent_rejects_explicitly_mismatched_event_publication(self):
        accepted, rejected = self.filter(
            event(OLD_PUBLICATION), intent(CURRENT_PUBLICATION)
        )
        self.assertEqual([], accepted)
        self.assertTrue(any("CLAIM publication_id" in item["reason"] for item in rejected))

    def test_current_intent_may_bind_claim_when_event_omits_publication(self):
        accepted, rejected = self.filter(event(), intent(CURRENT_PUBLICATION))
        self.assertEqual([], rejected)
        self.assertEqual(1, len(accepted))
        self.assertEqual(CURRENT_PUBLICATION, accepted[0]["publication_id"])

    def test_current_intent_and_current_event_publication_are_accepted(self):
        accepted, rejected = self.filter(
            event(CURRENT_PUBLICATION), intent(CURRENT_PUBLICATION)
        )
        self.assertEqual([], rejected)
        self.assertEqual(1, len(accepted))
        self.assertEqual(CURRENT_PUBLICATION, accepted[0]["publication_id"])


if __name__ == "__main__":
    unittest.main()
