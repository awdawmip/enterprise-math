import json
import copy
import tempfile
import unittest
from pathlib import Path

from control_plane import check_control_semantic_verification_requests as requests


ROOT = Path(__file__).resolve().parents[1]


class ControlSemanticVerificationRequestTests(unittest.TestCase):
    def test_only_architecture_request_remains_closed_and_nonexecutive(self):
        reports = requests.check(ROOT)
        self.assertEqual(1, len(reports))
        self.assertIn("CSV-ARCHITECTURE-V2-PUBLICATION-CUTOVER-001", reports[0])
        self.assertIn("CLOSED_NONEXECUTABLE_NO_TASK_REQUIRED", reports[0])
        self.assertNotIn("CSV-AMBIGUOUS-DISPATCH-FIELD-MEANING-002", reports[0])

    def test_control_requests_cannot_masquerade_as_tasks(self):
        data = json.loads(
            (ROOT / "control_plane" / "control_semantic_verification_requests.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(1, len(data["requests"]))
        self.assertEqual(requests.CLOSED_REQUEST_STATUS, data["status"])
        for row in data["requests"]:
            self.assertFalse(row["is_research_task"])
            self.assertFalse(row["claimable"])
            self.assertFalse(row["runtime_dispatchable"])
            self.assertFalse(row["authority_granted"])
            self.assertEqual(requests.CLOSED_REQUEST_STATE, row["state"])
            self.assertIsNone(row["future_authorized_publication"])
            self.assertEqual(0, row["resolution"]["changed_pointer_count"])
            for field in (
                "task_publication_required", "governance_approval_granted",
                "migration_authority_granted",
            ):
                self.assertFalse(row["resolution"][field])

    def open_fixture(self):
        """An explicit open-debt fixture, not a reopening of repository history."""
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        control = root / "control_plane"
        control.mkdir()
        data = json.loads((ROOT / "control_plane/control_semantic_verification_requests.json").read_text(encoding="utf-8"))
        migrations = json.loads((ROOT / "control_plane/control_semantic_migration_registry.json").read_text(encoding="utf-8"))
        data["status"] = requests.OPEN_REQUEST_STATUS
        row = data["requests"][0]
        row["state"] = requests.OPEN_REQUEST_STATE
        row["required_verification"] = ["Verify this synthetic unresolved pointer change."]
        for field in ("resolution", "historical_control_structural_evidence", "required_verification_completed"):
            row.pop(field)
        row["future_authorized_publication"] = {
            "kind": "GOVERNANCE",
            "publication_contract": "research_task_publication_contract_v2.json",
            "publication_tool": "tools/research_task_records.py",
            "publisher_role_must_be_one_of": ["RESEARCH_DRIVER", "FOUNDATION_STEWARD"],
        }
        related = set(row["related_migration_ids"])
        for migration in migrations["entries"]:
            if migration["migration_id"] in related:
                migration["state"] = "REQUIRES_GOVERNANCE_VERIFICATION"
        (control / "control_semantic_migration_registry.json").write_text(json.dumps(migrations), encoding="utf-8")
        path = control / "control_semantic_verification_requests.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        return root, path, data

    def test_open_request_requires_authorized_immutable_v2_future_contract(self):
        root, _, data = self.open_fixture()
        publication = data["requests"][0]["future_authorized_publication"]
        self.assertEqual("GOVERNANCE", publication["kind"])
        self.assertEqual("research_task_publication_contract_v2.json", publication["publication_contract"])
        self.assertEqual("tools/research_task_records.py", publication["publication_tool"])
        self.assertEqual({"RESEARCH_DRIVER", "FOUNDATION_STEWARD"}, set(publication["publisher_role_must_be_one_of"]))
        self.assertIn("OPEN_NONEXECUTABLE", requests.check(root)[0])

    def test_open_request_rejects_authority_and_future_contract_drift(self):
        root, path, original = self.open_fixture()
        self.assertIn("OPEN_NONEXECUTABLE", requests.check(root)[0])
        mutations = [
            ("kind", "RESEARCH", "must be GOVERNANCE"),
            ("publication_contract", "legacy.json", "V2 publication contract"),
            ("publication_tool", "legacy.py", "immutable V2 publication tool"),
            ("publisher_role_must_be_one_of", ["CONTROL_PLANE_MAINTENANCE"], "unsupported future publisher"),
        ]
        for field, value, message in mutations:
            with self.subTest(field=field):
                data = copy.deepcopy(original)
                data["requests"][0]["future_authorized_publication"][field] = value
                path.write_text(json.dumps(data), encoding="utf-8")
                with self.assertRaisesRegex(requests.VerificationRequestError, message):
                    requests.check(root)
        for field in ("is_research_task", "claimable", "runtime_dispatchable", "authority_granted"):
            with self.subTest(field=field):
                data = copy.deepcopy(original)
                data["requests"][0][field] = True
                path.write_text(json.dumps(data), encoding="utf-8")
                with self.assertRaisesRegex(requests.VerificationRequestError, field + "=false"):
                    requests.check(root)


if __name__ == "__main__":
    unittest.main()
