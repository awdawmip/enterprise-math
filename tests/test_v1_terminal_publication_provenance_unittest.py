import tempfile
import unittest
from pathlib import Path

from tools import research_task_records
from tools import research_task_registry


class V1TerminalPublicationProvenanceTests(unittest.TestCase):
    def _record(self, root: Path, state: str) -> tuple[Path, dict, list[dict]]:
        task_dir = root / "research_tasks"
        task_dir.mkdir(parents=True, exist_ok=True)
        path = task_dir / "TERMINAL_V2_PROVENANCE.md"
        path.write_text("terminal provenance fixture\n", encoding="utf-8")
        meta = {"task_id": "RS-TERMINAL-V2-PROVENANCE"}
        record = {
            "record_schema": research_task_records.RECORD_SCHEMA,
            "record_state": state,
            "task_id": meta["task_id"],
            "publication_id": "TP2-TERMINAL-PROVENANCE",
            "taskbook_path": "research_tasks/TERMINAL_V2_PROVENANCE.md",
            "taskbook_blob_sha1": research_task_registry.blob_sha1(path),
            "publication_transaction": research_task_records.PUBLICATION_TRANSACTION_V2,
        }
        return path, meta, [record]

    def test_closed_v2_record_is_immutable_provenance(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            path, meta, records = self._record(root, "CLOSED")
            self.assertTrue(
                research_task_registry.has_exact_v2_publication_authority(
                    path,
                    meta,
                    records,
                    set(),
                    root=root,
                )
            )

    def test_active_v2_record_remains_provenance(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            path, meta, records = self._record(root, "ACTIVE")
            self.assertTrue(
                research_task_registry.has_exact_v2_publication_authority(
                    path,
                    meta,
                    records,
                    set(),
                    root=root,
                )
            )

    def test_unknown_nonstandard_state_does_not_gain_provenance(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            path, meta, records = self._record(root, "MYSTERY_STATE")
            self.assertFalse(
                research_task_registry.has_exact_v2_publication_authority(
                    path,
                    meta,
                    records,
                    set(),
                    root=root,
                )
            )


if __name__ == "__main__":
    unittest.main()
