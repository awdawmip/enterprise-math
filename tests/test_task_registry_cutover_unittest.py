import json
import tempfile
import unittest
from pathlib import Path

from tools import check_task_registry_cutover as cutover
from tools import research_taskbook


class TaskRegistryCutoverTests(unittest.TestCase):
    def make_root(self):
        td = tempfile.TemporaryDirectory()
        root = Path(td.name)
        scheduler = root / "research_scheduler.json"
        scheduler.write_text('{"schema":"legacy","tasks":["A"]}\n', encoding="utf-8")
        digest = research_taskbook.git_blob_identity(scheduler.read_bytes()).hex()
        registry = {
            "legacy_baseline": {
                "mode": "FROZEN_SCHEDULER_DEFINITION_FILE",
                "scheduler_path": "research_scheduler.json",
                "scheduler_git_blob_sha1": digest,
                "classification": "LEGACY_BASELINE_REGISTERED_EXISTING_EXECUTION_ONLY",
                "scheduler_file_may_publish_new_tasks": False,
                "runtime_event_log_may_continue": True,
                "fresh_redispatch_requires_explicit_record": True,
            }
        }
        (root / "research_task_registry.json").write_text(json.dumps(registry), encoding="utf-8")
        return td, root, scheduler

    def test_frozen_legacy_scheduler_passes(self):
        td, root, _ = self.make_root()
        self.addCleanup(td.cleanup)
        self.assertEqual([], cutover.check(root))

    def test_direct_scheduler_task_definition_edit_fails(self):
        td, root, scheduler = self.make_root()
        self.addCleanup(td.cleanup)
        scheduler.write_text('{"schema":"legacy","tasks":["A","NEW-ORPHAN"]}\n', encoding="utf-8")
        errors = cutover.check(root)
        self.assertTrue(any("new/modified tasks must be published" in error for error in errors))

    def test_scheduler_cannot_be_reenabled_as_publication_path(self):
        td, root, _ = self.make_root()
        self.addCleanup(td.cleanup)
        registry = json.loads((root / "research_task_registry.json").read_text(encoding="utf-8"))
        registry["legacy_baseline"]["scheduler_file_may_publish_new_tasks"] = True
        (root / "research_task_registry.json").write_text(json.dumps(registry), encoding="utf-8")
        errors = cutover.check(root)
        self.assertTrue(any("must not be an allowed new-task publication path" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
