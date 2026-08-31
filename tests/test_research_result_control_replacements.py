import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import research_result_control_replacements as replacements
from tools import research_result_records as public_results


DRIVER = "EM-DVR-ABC123"
COMMENT_ID = 9201
AUTH_TIME = "2026-08-28T03:22:00+00:00"


def write_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def git_blob(path: Path) -> str:
    data = path.read_bytes()
    return "sha1:" + hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def driver_contract():
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


def control_policy():
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


def authority_record():
    body = json.dumps(
        {
            "schema": "ENTERPRISE_MATH_DRIVER_AUTH_EVENT_V1",
            "event": "AUTHORIZE",
            "driver_id": DRIVER,
            "scope": "CONTROL_PLANE",
            "authority": "RESEARCH_DRIVER",
            "at": AUTH_TIME,
            "reason": "result replacement test",
        },
        separators=(",", ":"),
    )
    rid = "DA-" + hashlib.sha256(
        f"{DRIVER}\0AUTHORIZE\0{COMMENT_ID}".encode("utf-8")
    ).hexdigest()[:20].upper()
    return {
        "record_schema": "ENTERPRISE_MATH_DRIVER_AUTHORITY_RECORD_V1",
        "authority_record_id": rid,
        "driver_id": DRIVER,
        "event": "AUTHORIZE",
        "scope": "CONTROL_PLANE",
        "authority": "RESEARCH_DRIVER",
        "source_repository": "awdawmip/enterprise-math",
        "source_issue": 240,
        "source_comment_id": COMMENT_ID,
        "source_comment_url": f"https://api.github.com/repos/awdawmip/enterprise-math/issues/comments/{COMMENT_ID}",
        "source_issue_url": "https://api.github.com/repos/awdawmip/enterprise-math/issues/240",
        "source_body": body,
        "source_body_sha256": "sha256:" + hashlib.sha256(body.encode()).hexdigest(),
        "source_created_at": AUTH_TIME,
        "source_updated_at": AUTH_TIME,
        "source_server_author": {"login": "owner", "user_id": 7, "author_association": "OWNER"},
        "server_authenticated": True,
        "control_authorized": True,
        "edited": False,
        "github_app_is_authority": False,
        "global_knowledge_is_authority": False,
        "working_truth_granted": False,
        "foundation_authority_granted": False,
        "canonical_promotion_granted": False,
    }


def replacement_contract():
    return {
        "schema": "ENTERPRISE_MATH_RESULT_CONTROL_REPLACEMENT_CONTRACT_V1",
        "status": "ACTIVE_CANONICAL_CANDIDATE",
        "record_schema": "ENTERPRISE_MATH_RESULT_CONTROL_REPLACEMENT_RECORD_V1",
    }


def result(result_id, *, execution="ER-SAME", manifest_extra=False, owner="1" * 40, frozen="2026-08-28T03:30:00Z"):
    manifest = [
        {"path": "return.md", "git_blob_sha1": "sha1:" + "a" * 40, "sha256": "sha256:" + "b" * 64}
    ]
    if manifest_extra:
        manifest.append(
            {"path": "definition.md", "git_blob_sha1": "sha1:" + "c" * 40, "sha256": "sha256:" + "d" * 64}
        )
    return {
        "record_schema": "ENTERPRISE_MATH_RESEARCH_RESULT_RECORD_V1",
        "result_id": result_id,
        "task_id": "RS-T",
        "publication_id": "TP2-T",
        "execution_record_id": execution,
        "claim_id": "claim-t",
        "taskbook_path": "research_tasks/T.md",
        "taskbook_blob_sha1": "sha1:" + "e" * 40,
        "execution_branch": "research/t",
        "execution_branch_base": "f" * 40,
        "return_path": "return.md",
        "return_blob_sha1": "sha1:" + "a" * 40,
        "return_sha256": "sha256:" + "b" * 64,
        "owner_head": owner,
        "researcher_id": "EM-T-ABC123",
        "frozen_at": frozen,
        "terminal_verdict": "INTEGRATED",
        "hard_target_disposition": "SATISFIED",
        "unresolved_residue": "NONE",
        "output_manifest": manifest,
        "method_harvest": "NO_TOOL_PAYLOAD",
        "independence_status": "NOT_APPLICABLE",
        "source_exposure_status": "NOT_APPLICABLE",
        "next_control_plane_recommendation": "review control generation",
        "driver_review_required": True,
    }


class ControlResultReplacementTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        write_json(self.root / "research_driver_authority_contract.json", driver_contract())
        write_json(self.root / "research_control_event_authorization.json", control_policy())
        auth = authority_record()
        write_json(
            self.root / "research_driver_authority_records" / DRIVER / f"{auth['authority_record_id']}.json",
            auth,
        )
        write_json(self.root / "research_result_control_replacement_contract.json", replacement_contract())
        self.old_path = self.root / "research_result_records" / "RS-T" / "RR-OLD.json"
        self.new_path = self.root / "research_result_records" / "RS-T" / "RR-NEW.json"
        write_json(self.old_path, result("RR-OLD", owner="1" * 40, frozen="2026-08-28T03:30:00Z"))
        corrected = result(
            "RR-NEW",
            manifest_extra=True,
            owner="2" * 40,
            frozen="2026-08-28T03:40:00Z",
        )
        corrected["hard_target_disposition"] = "SATISFIED / OUTPUT_MANIFEST_REGENERATED"
        write_json(self.new_path, corrected)
        self.auth = auth

    def tearDown(self):
        self.temp.cleanup()

    def write_edge(self, **overrides):
        value = {
            "record_schema": "ENTERPRISE_MATH_RESULT_CONTROL_REPLACEMENT_RECORD_V1",
            "replacement_id": replacements.replacement_id("RR-OLD", "RR-NEW"),
            "historical_result_id": "RR-OLD",
            "corrected_result_id": "RR-NEW",
            "historical_record_path": "research_result_records/RS-T/RR-OLD.json",
            "historical_record_blob_sha1": git_blob(self.old_path),
            "corrected_record_path": "research_result_records/RS-T/RR-NEW.json",
            "corrected_record_blob_sha1": git_blob(self.new_path),
            "resolution": "CONTROL_ONLY_REFREEZE_SUPERSEDES",
            "operational_result_id": "RR-NEW",
            "history_preserved": True,
            "parallel_evidence": False,
            "driver_id": DRIVER,
            "created_at": "2026-08-28T03:45:00Z",
            "driver_authority_record_id": self.auth["authority_record_id"],
            "driver_authority_source_comment_id": COMMENT_ID,
            "reason": ["Same execution; corrected result strictly expands the frozen manifest."],
            "working_truth_granted": False,
            "foundation_authority_granted": False,
            "canonical_promotion_granted": False,
            "successor_triggered": False,
        }
        value.update(overrides)
        path = self.root / "research_result_control_replacements" / "RR-OLD" / f"{value['replacement_id']}.json"
        write_json(path, value)
        return path

    def test_valid_same_execution_refreeze_filters_historical_operational_result(self):
        self.write_edge()
        ids = [item["result_id"] for item in public_results.iter_results(self.root)]
        self.assertEqual(["RR-NEW"], ids)
        self.assertEqual([], replacements.audit(self.root))

    def test_historical_reviews_leave_operational_review_view(self):
        self.write_edge()
        write_json(
            self.root / "research_result_reviews" / "RR-OLD" / "DR-OLD.json",
            {"review_id": "DR-OLD", "result_id": "RR-OLD"},
        )
        write_json(
            self.root / "research_result_reviews" / "RR-NEW" / "DR-NEW.json",
            {"review_id": "DR-NEW", "result_id": "RR-NEW"},
        )
        replaced = set(public_results._replacement_edges(self.root))
        ids = [
            item["review_id"]
            for item in public_results._BASE_ITER_REVIEWS(self.root)
            if item.get("result_id") not in replaced
        ]
        self.assertEqual({"RR-OLD"}, replaced)
        self.assertEqual(["DR-NEW"], ids)

    def test_distinct_execution_cannot_be_reclassified_as_control_replacement(self):
        corrected = json.loads(self.new_path.read_text())
        corrected["execution_record_id"] = "ER-DIFFERENT"
        write_json(self.new_path, corrected)
        self.write_edge(corrected_record_blob_sha1=git_blob(self.new_path))
        errors = replacements.audit(self.root)
        self.assertTrue(any("execution_record_id" in error for error in errors))

    def test_manifest_must_strictly_expand(self):
        corrected = json.loads(self.new_path.read_text())
        corrected["output_manifest"] = json.loads(self.old_path.read_text())["output_manifest"]
        write_json(self.new_path, corrected)
        self.write_edge(corrected_record_blob_sha1=git_blob(self.new_path))
        errors = replacements.audit(self.root)
        self.assertTrue(any("strict path superset" in error for error in errors))

    def test_mathematical_terminal_verdict_cannot_change(self):
        corrected = json.loads(self.new_path.read_text())
        corrected["terminal_verdict"] = "REFUTED"
        write_json(self.new_path, corrected)
        self.write_edge(corrected_record_blob_sha1=git_blob(self.new_path))
        errors = replacements.audit(self.root)
        self.assertTrue(any("terminal_verdict" in error for error in errors))

    def test_replacement_requires_source_backed_driver_authority(self):
        self.write_edge(driver_id="EM-DVR-NOAUTH")
        errors = replacements.audit(self.root)
        self.assertTrue(any("no source-backed ACTIVE authority" in error for error in errors))

    def test_replacement_chain_must_be_acyclic(self):
        self.write_edge()
        third_path = self.root / "research_result_records" / "RS-T" / "RR-THIRD.json"
        third = result(
            "RR-THIRD",
            manifest_extra=True,
            owner="3" * 40,
            frozen="2026-08-28T03:50:00Z",
        )
        third["hard_target_disposition"] = "SATISFIED / OUTPUT_MANIFEST_REGENERATED / SECOND_CONTROL_REFREEZE"
        third["output_manifest"].append(
            {"path": "certificate.md", "git_blob_sha1": "sha1:" + "9" * 40, "sha256": "sha256:" + "8" * 64}
        )
        write_json(third_path, third)
        edge_id = replacements.replacement_id("RR-NEW", "RR-THIRD")
        write_json(
            self.root / "research_result_control_replacements" / "RR-NEW" / f"{edge_id}.json",
            {
                "record_schema": "ENTERPRISE_MATH_RESULT_CONTROL_REPLACEMENT_RECORD_V1",
                "replacement_id": edge_id,
                "historical_result_id": "RR-NEW",
                "corrected_result_id": "RR-THIRD",
                "historical_record_path": "research_result_records/RS-T/RR-NEW.json",
                "historical_record_blob_sha1": git_blob(self.new_path),
                "corrected_record_path": "research_result_records/RS-T/RR-THIRD.json",
                "corrected_record_blob_sha1": git_blob(third_path),
                "resolution": "CONTROL_ONLY_REFREEZE_SUPERSEDES",
                "operational_result_id": "RR-THIRD",
                "history_preserved": True,
                "parallel_evidence": False,
                "driver_id": DRIVER,
                "created_at": "2026-08-28T03:55:00Z",
                "driver_authority_record_id": self.auth["authority_record_id"],
                "driver_authority_source_comment_id": COMMENT_ID,
                "reason": ["Second control-only manifest refreeze."],
                "working_truth_granted": False,
                "foundation_authority_granted": False,
                "canonical_promotion_granted": False,
                "successor_triggered": False,
            },
        )
        ids = [item["result_id"] for item in public_results.iter_results(self.root)]
        self.assertEqual(["RR-THIRD"], ids)


if __name__ == "__main__":
    unittest.main()
