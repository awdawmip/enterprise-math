import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import research_objective_driver_authority as objective_authority
import research_objective_records as objectives


DRIVER = "EM-DVR-ABC123"
UNAUTHORIZED = "EM-DVR-NOAUTH"
COMMENT_ID = 9101
AUTH_TIME = "2026-08-28T03:22:00+00:00"


def write_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def contract(*, legacy_generations=None, legacy_heads=None):
    return {
        "schema": "ENTERPRISE_MATH_DRIVER_AUTHORITY_CONTRACT_V1",
        "status": "ACTIVE_CANONICAL_CANDIDATE",
        "repository": "awdawmip/enterprise-math",
        "control_issue": 240,
        "source_event_schema": "ENTERPRISE_MATH_DRIVER_AUTH_EVENT_V1",
        "record_schema": "ENTERPRISE_MATH_DRIVER_AUTHORITY_RECORD_V1",
        "global_knowledge_runtime_authority": False,
        "github_app_runtime_authority": False,
        "legacy_objective_generations": legacy_generations or {},
        "legacy_objective_heads": legacy_heads or {},
        "legacy_task_objective_bindings": [],
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


def authority_record():
    body = json.dumps(
        {
            "schema": "ENTERPRISE_MATH_DRIVER_AUTH_EVENT_V1",
            "event": "AUTHORIZE",
            "driver_id": DRIVER,
            "scope": "CONTROL_PLANE",
            "authority": "RESEARCH_DRIVER",
            "at": AUTH_TIME,
            "reason": "objective authority test",
        },
        separators=(",", ":"),
    )
    record_id = "DA-" + hashlib.sha256(
        f"{DRIVER}\0AUTHORIZE\0{COMMENT_ID}".encode("utf-8")
    ).hexdigest()[:20].upper()
    return {
        "record_schema": "ENTERPRISE_MATH_DRIVER_AUTHORITY_RECORD_V1",
        "authority_record_id": record_id,
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
        "source_body_sha256": "sha256:" + hashlib.sha256(body.encode("utf-8")).hexdigest(),
        "source_created_at": AUTH_TIME,
        "source_updated_at": AUTH_TIME,
        "source_server_author": {
            "login": "owner",
            "user_id": 7,
            "author_association": "OWNER",
        },
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


def objective_kwargs(driver=DRIVER, created="2026-08-28T04:00:00+00:00", status="OPEN"):
    value = {
        "objective_id": "OBJ-TEST",
        "objective_status": status,
        "title": "Objective authority test",
        "scope": "Test source-backed Objective control.",
        "success_criteria": ["authority preserved"],
        "closure_criteria": ["all child work resolved"],
        "research_value": "Prevent Driver-ID syntax from becoming Objective authority.",
        "publisher_id": driver,
        "created_at": created,
    }
    if status == "CLOSED":
        value["disposition_reason"] = "test closure"
        value["closure_evidence_refs"] = ["RR-TEST"]
    return value


class ObjectiveDriverAuthorityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        write_json(self.root / "research_driver_authority_contract.json", contract())
        write_json(self.root / "research_control_event_authorization.json", policy())
        record = authority_record()
        write_json(
            self.root
            / "research_driver_authority_records"
            / DRIVER
            / f"{record['authority_record_id']}.json",
            record,
        )

    def tearDown(self):
        self.temp.cleanup()

    def test_authorized_create_and_select_pins_driver_authority(self):
        generation, head = objectives.create_and_select(
            expected_previous_generation_id=None,
            root=self.root,
            **objective_kwargs(),
        )
        self.assertEqual(COMMENT_ID, generation["driver_authority_source_comment_id"])
        self.assertEqual(COMMENT_ID, head["driver_authority_source_comment_id"])
        self.assertEqual(
            generation["driver_authority_record_id"], head["driver_authority_record_id"]
        )
        self.assertEqual([], objectives.audit(self.root))

    def test_driver_syntax_without_source_authority_cannot_close_objective(self):
        first, _ = objectives.create_and_select(
            expected_previous_generation_id=None,
            root=self.root,
            **objective_kwargs(),
        )
        with self.assertRaises(objectives.ObjectiveRecordError):
            objectives.create_and_select(
                expected_previous_generation_id=first["objective_generation_id"],
                root=self.root,
                **objective_kwargs(driver=UNAUTHORIZED, status="CLOSED"),
            )

    def test_backdating_cannot_escape_driver_authority_cutover(self):
        with self.assertRaises(objectives.ObjectiveRecordError):
            objectives.build_generation(
                root=self.root,
                **objective_kwargs(created="1900-01-01T00:00:00+00:00"),
            )

    def test_authorized_historical_binding_pins_driver_authority(self):
        generation, _ = objectives.create_and_select(
            expected_previous_generation_id=None,
            root=self.root,
            **objective_kwargs(),
        )
        write_json(
            self.root / "research_task_records" / "RS-T" / "TP2-T.json",
            {
                "task_id": "RS-T",
                "publication_id": "TP2-T",
                "parent_objective_id": "OBJ-TEST",
                "taskbook_path": "research_tasks/T.md",
                "taskbook_blob_sha1": "sha1:test",
            },
        )
        binding = objectives.bind_historical_task(
            task_id="RS-T",
            publication_id="TP2-T",
            objective_id="OBJ-TEST",
            objective_generation_id=generation["objective_generation_id"],
            bound_by=DRIVER,
            bound_at="2026-08-28T04:10:00+00:00",
            root=self.root,
        )
        self.assertEqual(COMMENT_ID, binding["driver_authority_source_comment_id"])
        self.assertEqual([], objective_authority.audit(self.root))

    def test_unauthorized_historical_binding_fails_closed(self):
        generation, _ = objectives.create_and_select(
            expected_previous_generation_id=None,
            root=self.root,
            **objective_kwargs(),
        )
        write_json(
            self.root / "research_task_records" / "RS-T" / "TP2-T.json",
            {
                "task_id": "RS-T",
                "publication_id": "TP2-T",
                "parent_objective_id": "OBJ-TEST",
                "taskbook_path": "research_tasks/T.md",
                "taskbook_blob_sha1": "sha1:test",
            },
        )
        with self.assertRaises(objectives.ObjectiveRecordError):
            objectives.bind_historical_task(
                task_id="RS-T",
                publication_id="TP2-T",
                objective_id="OBJ-TEST",
                objective_generation_id=generation["objective_generation_id"],
                bound_by=UNAUTHORIZED,
                bound_at="2026-08-28T04:10:00+00:00",
                root=self.root,
            )

    def test_exact_legacy_generation_and_head_bytes_are_exempt(self):
        legacy_generation = self.root / "research_objective_records" / "OBJ-LEGACY" / "OG-LEGACY.json"
        legacy_head = self.root / "research_objective_heads" / "OBJ-LEGACY.json"
        write_json(
            legacy_generation,
            {
                "objective_generation_id": "OG-LEGACY",
                "objective_id": "OBJ-LEGACY",
                "publisher_id": "EM-DVR-OLD001",
                "created_at": "2026-01-01T00:00:00Z",
            },
        )
        write_json(
            legacy_head,
            {
                "objective_id": "OBJ-LEGACY",
                "objective_generation_id": "OG-LEGACY",
                "updated_by": "EM-DVR-OLD001",
                "updated_at": "2026-01-01T00:00:00Z",
            },
        )
        write_json(
            self.root / "research_driver_authority_contract.json",
            contract(
                legacy_generations={"OG-LEGACY": sha256_file(legacy_generation)},
                legacy_heads={
                    "OBJ-LEGACY": {
                        "objective_generation_id": "OG-LEGACY",
                        "head_sha256": sha256_file(legacy_head),
                    }
                },
            ),
        )
        self.assertEqual([], objective_authority.audit(self.root))

    def test_legacy_objective_byte_drift_fails_closed(self):
        legacy_generation = self.root / "research_objective_records" / "OBJ-LEGACY" / "OG-LEGACY.json"
        legacy_head = self.root / "research_objective_heads" / "OBJ-LEGACY.json"
        write_json(
            legacy_generation,
            {
                "objective_generation_id": "OG-LEGACY",
                "objective_id": "OBJ-LEGACY",
                "publisher_id": "EM-DVR-OLD001",
                "created_at": "2026-01-01T00:00:00Z",
            },
        )
        write_json(
            legacy_head,
            {
                "objective_id": "OBJ-LEGACY",
                "objective_generation_id": "OG-LEGACY",
                "updated_by": "EM-DVR-OLD001",
                "updated_at": "2026-01-01T00:00:00Z",
            },
        )
        frozen_generation = sha256_file(legacy_generation)
        frozen_head = sha256_file(legacy_head)
        write_json(
            self.root / "research_driver_authority_contract.json",
            contract(
                legacy_generations={"OG-LEGACY": frozen_generation},
                legacy_heads={
                    "OBJ-LEGACY": {
                        "objective_generation_id": "OG-LEGACY",
                        "head_sha256": frozen_head,
                    }
                },
            ),
        )
        with legacy_head.open("a", encoding="utf-8") as handle:
            handle.write(" \n")
        errors = objective_authority.audit(self.root)
        self.assertTrue(any("byte drift" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
