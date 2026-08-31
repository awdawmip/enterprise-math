import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TaskRegistryCliSurfaceTests(unittest.TestCase):
    def test_legacy_taskbook_authoring_doc_routes_new_publication_to_registry_tool(self):
        text = (ROOT / "docs/RESEARCH_TASKBOOK_AUTHORING_AND_REVIEW.md").read_text(encoding="utf-8")
        self.assertIn("tools/research_task_registry.py", text)
        self.assertIn("legacy `tools/research_taskbook.py`", text)
        self.assertIn("not** the canonical publication gate", text)

    def test_publication_protocol_requires_both_registry_and_cutover_audits(self):
        text = (ROOT / "docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md").read_text(encoding="utf-8")
        self.assertIn("python tools/research_task_records.py audit", text)
        self.assertIn("python tools/check_task_registry_cutover.py", text)
        self.assertIn("LEGACY_SCHEDULER_DEFINITION_FILE_MAY_NOT_PUBLISH_NEW_TASKS", text)


if __name__ == "__main__":
    unittest.main()
