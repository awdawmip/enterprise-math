import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import research_driver_authority as authority


DRIVER = "EM-DVR-ABC123"
COMMENT_ID = 9001
BODY = json.dumps(
    {
        "schema": "ENTERPRISE_MATH_DRIVER_AUTH_EVENT_V1",
        "event": "AUTHORIZE",
        "driver_id": DRIVER,
        "scope": "CONTROL_PLANE",
        "authority": "RESEARCH_DRIVER",
        "at": "1900-01-01T00:00:00Z",
        "reason": "test bootstrap",
    },
    separators=(",", ":"),
)


def write_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def contract():
    return {
        "schema": "ENTERPRISE_MATH_DRIVER_AUTHORITY_CONTRACT_V1",
        "status": "ACTIVE_CANONICAL_CANDIDATE",
        "repository": "awdawmip/enterprise-math",
        "control_issue": 240,
        "source_event_schema": "ENTERPRISE_MATH_DRIVER_AUTH_EVENT_V1",
        "record_schema": "ENTERPRISE_MATH_DRIVER_AUTHORITY_RECORD_V1",
        "global_knowledge_runtime_authority": False,
        "github_app_runtime_authority": False,
    }


def policy():
    return {
        "schema": "ENTERPRISE_MATH_CONTROL_EVENT_AUTHORIZATION_V1",
        "status": "ACTIVE_CANONICAL",
        "repository": "awdawmip/enterprise-math",
        "issue": 240,
        "mode": "EXACT_SERVER_AUTHOR_ALLOWLIST",
        "authorized_server_authors": [
            {"login": "owner", "user_id": 7, "author_association": ["OWNER"]}
        ],
    }


def record(event="AUTHORIZE", comment_id=COMMENT_ID, created="2026-08-28T03:22:00+00:00"):
    body = BODY if event == "AUTHORIZE" else json.dumps(
        {
            "schema": "ENTERPRISE_MATH_DRIVER_AUTH_EVENT_V1",
            "event": event,
            "driver_id": DRIVER,
            "scope": "CONTROL_PLANE",
            "authority": "RESEARCH_DRIVER",
            "at": "1900-01-01T00:00:00Z",
            "reason": "test revoke",
        },
        separators=(",", ":"),
    )
    rid = "DA-" + hashlib.sha256(f"{DRIVER}\0{event}\0{comment_id}".encode()).hexdigest()[:20].upper()
    return {
        "record_schema": "ENTERPRISE_MATH_DRIVER_AUTHORITY_RECORD_V1",
        "authority_record_id": rid,
        "driver_id": DRIVER,
        "event": event,
        "scope": "CONTROL_PLANE",
        "authority": "RESEARCH_DRIVER",
        "source_repository": "awdawmip/enterprise-math",
        "source_issue": 240,
        "source_comment_id": comment_id,
        "source_comment_url": f"https://api.github.com/repos/awdawmip/enterprise-math/issues/comments/{comment_id}",
        "source_issue_url": "https://api.github.com/repos/awdawmip/enterprise-math/issues/240",
        "source_body": body,
        "source_body_sha256": "sha256:" + hashlib.sha256(body.encode()).hexdigest(),
        "source_created_at": created,
        "source_updated_at": created,
        "source_server_author": {"login": "owner", "user_id": 7, "author_association": "OWNER"},
        "source_performed_via_github_app": "provenance-only",
        "server_authenticated": True,
        "control_authorized": True,
        "edited": False,
        "github_app_is_authority": False,
        "global_knowledge_is_authority": False,
        "working_truth_granted": False,
        "foundation_authority_granted": False,
        "canonical_promotion_granted": False,
    }


class DriverAuthorityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        write_json(self.root / "research_driver_authority_contract.json", contract())
        write_json(self.root / "research_control_event_authorization.json", policy())
        write_json(self.root / "research_driver_followup_legacy_reviews.json", {"review_ids": ["DR-LEGACY"]})
        row = record()
        write_json(self.root / "research_driver_authority_records" / DRIVER / f"{row['authority_record_id']}.json", row)

    def tearDown(self):
        self.temp.cleanup()

    def test_authorized_driver_is_active_only_after_server_event(self):
        self.assertIsNone(authority.active_authority_at(DRIVER, "2026-08-28T03:21:59Z", self.root))
        current = authority.require_active_driver(DRIVER, "2026-08-28T03:22:00Z", self.root)
        self.assertEqual(COMMENT_ID, current["source_comment_id"])

    def test_syntax_alone_is_not_authority(self):
        with self.assertRaises(authority.DriverAuthorityError):
            authority.require_active_driver("EM-DVR-NOAUTH", "2026-08-28T04:00:00Z", self.root)

    def test_generic_execution_identity_is_not_new_driver_identity(self):
        with self.assertRaises(authority.DriverAuthorityError):
            authority.require_active_driver("EM-ABC-ABC123", "2026-08-28T04:00:00Z", self.root)

    def test_wrong_server_actor_fails_closed(self):
        path = next((self.root / "research_driver_authority_records" / DRIVER).glob("*.json"))
        row = json.loads(path.read_text())
        row["source_server_author"]["login"] = "outsider"
        write_json(path, row)
        with self.assertRaises(authority.DriverAuthorityError):
            authority.require_active_driver(DRIVER, "2026-08-28T04:00:00Z", self.root)

    def test_edited_event_fails_closed(self):
        path = next((self.root / "research_driver_authority_records" / DRIVER).glob("*.json"))
        row = json.loads(path.read_text())
        row["edited"] = True
        row["source_updated_at"] = "2026-08-28T03:23:00Z"
        write_json(path, row)
        with self.assertRaises(authority.DriverAuthorityError):
            authority.require_active_driver(DRIVER, "2026-08-28T04:00:00Z", self.root)

    def test_revocation_stops_later_actions_but_not_prior_actions(self):
        revoked = record("REVOKE", COMMENT_ID + 1, "2026-08-28T05:00:00Z")
        write_json(
            self.root / "research_driver_authority_records" / DRIVER / f"{revoked['authority_record_id']}.json",
            revoked,
        )
        self.assertIsNotNone(authority.active_authority_at(DRIVER, "2026-08-28T04:59:59Z", self.root))
        self.assertIsNone(authority.active_authority_at(DRIVER, "2026-08-28T05:00:00Z", self.root))

    def test_post_cutover_review_must_pin_exact_authority(self):
        current = authority.require_active_driver(DRIVER, "2026-08-28T04:00:00Z", self.root)
        review = {
            "review_id": "DR-NEW",
            "driver_id": DRIVER,
            "reviewed_at": "2026-08-28T04:00:00Z",
            "driver_authority_record_id": current["authority_record_id"],
            "driver_authority_source_comment_id": current["source_comment_id"],
        }
        self.assertEqual([], authority.review_authority_errors(review, self.root))
        review["driver_authority_source_comment_id"] = 1
        self.assertTrue(authority.review_authority_errors(review, self.root))

    def test_backdating_does_not_create_legacy_exemption(self):
        review = {
            "review_id": "DR-NEW",
            "driver_id": DRIVER,
            "reviewed_at": "1900-01-01T00:00:00Z",
        }
        self.assertTrue(authority.review_authority_errors(review, self.root))

    def test_exact_legacy_review_id_remains_compatible(self):
        review = {"review_id": "DR-LEGACY", "driver_id": "EM-DRIVER-01", "reviewed_at": "1900-01-01T00:00:00Z"}
        self.assertEqual([], authority.review_authority_errors(review, self.root))


if __name__ == "__main__":
    unittest.main()
