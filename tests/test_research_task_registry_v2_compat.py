import tempfile
import unittest
from pathlib import Path

from tools import research_task_records as records
from tools import research_task_registry as registry


class ExactV2AuthorityCompatibilityTests(unittest.TestCase):
    def make_taskbook(self, root: Path, content: str = "taskbook\n") -> Path:
        path = root / "research_tasks" / "T.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def exact_record(self, path: Path) -> dict:
        return {
            "record_schema": records.RECORD_SCHEMA,
            "record_state": "ACTIVE",
            "publication_transaction": records.PUBLICATION_TRANSACTION_V2,
            "task_id": "RS-T",
            "taskbook_path": "research_tasks/T.md",
            "taskbook_blob_sha1": registry.blob_sha1(path),
        }

    def test_exact_current_v2_publication_is_valid_compatibility_authority(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            path = self.make_taskbook(root)
            current = {"RS-T": self.exact_record(path)}
            self.assertTrue(
                registry.has_exact_v2_publication_authority(
                    path,
                    {"task_id": "RS-T"},
                    current,
                    root=root,
                )
            )

    def test_wrong_path_blob_transaction_or_state_does_not_bypass(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            path = self.make_taskbook(root)
            record = self.exact_record(path)
            for field, bad in (
                ("taskbook_path", "research_tasks/OTHER.md"),
                ("taskbook_blob_sha1", "sha1:" + "0" * 40),
                ("publication_transaction", "NOT_V2"),
                ("record_state", "CLOSED"),
            ):
                broken = dict(record)
                broken[field] = bad
                self.assertFalse(
                    registry.has_exact_v2_publication_authority(
                        path,
                        {"task_id": "RS-T"},
                        {"RS-T": broken},
                        root=root,
                    ),
                    field,
                )

    def test_missing_v1_and_missing_v2_remains_unrecognized(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            path = self.make_taskbook(root)
            self.assertFalse(
                registry.has_exact_v2_publication_authority(
                    path,
                    {"task_id": "RS-T"},
                    {},
                    root=root,
                )
            )


if __name__ == "__main__":
    unittest.main()
