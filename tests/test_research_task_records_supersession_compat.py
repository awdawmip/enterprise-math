import unittest
from pathlib import Path
from unittest.mock import patch

from tools import research_task_records as records


class SupersessionCompatibilityTests(unittest.TestCase):
    def test_only_superseded_mandatory_body_errors_are_grandfathered(self):
        old = "research_task_records/RS-T/TP2-OLD.json"
        current = "research_task_records/RS-T/TP2-NEW.json"
        raw_errors = [
            f"{old}: mandatory body section is missing or empty: Frozen inputs and scope",
            f"{old}: taskbook blob drift",
            f"{current}: mandatory body section is missing or empty: Hard target and required outputs",
        ]
        with patch.object(records, "_legacy_audit", return_value=raw_errors), patch.object(
            records, "_superseded_record_paths", return_value={old}
        ):
            out = records.audit(Path("/tmp/not-used"))
        self.assertNotIn(raw_errors[0], out)
        self.assertIn(raw_errors[1], out)
        self.assertIn(raw_errors[2], out)

    def test_superseded_paths_require_exact_successor_reference(self):
        values = [
            {"publication_id": "TP2-OLD", "_record_path": "old.json"},
            {
                "publication_id": "TP2-NEW",
                "supersedes_publication_id": "TP2-OLD",
                "_record_path": "new.json",
            },
            {"publication_id": "TP2-OTHER", "_record_path": "other.json"},
        ]
        with patch.object(records._impl, "iter_records", return_value=values):
            self.assertEqual({"old.json"}, records._superseded_record_paths(Path("/tmp/not-used")))


if __name__ == "__main__":
    unittest.main()
