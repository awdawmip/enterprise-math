import json
import pathlib
import tempfile
import unittest

from tools import research_scheduler as rs


class ResearchTaskbookTests(unittest.TestCase):
    def metadata(self, task_id="RS-TASKBOOK"):
        return {
            "task_id": task_id,
            "title": "Taskbook",
            "kind": "RESEARCH",
            "owner": rs.TASKBOOK_UNASSIGNED_OWNER,
            "base_state": "READY",
            "priority": "P1",
            "leverage": "HIGH",
            "frontier": "frontier",
            "next_action": "next action",
            "dependencies": [],
            "source_refs": [],
            "evidence_status": "CANDIDATE_RESEARCH_HANDOFF",
            "last_progress_ref": "taskbook",
            "last_progress_at": "2026-08-10T11:00:00+08:00",
            "hard_block": None,
        }

    def write_taskbook(self, path, metadata):
        path.write_text(
            "<!-- ENTERPRISE_MATH_TASK_V1\n"
            + json.dumps(metadata)
            + "\n-->\n# task\n",
            encoding="utf-8",
        )

    def test_taskbook_parser_reads_metadata_and_injects_isolation(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "task.md"
            self.write_taskbook(path, self.metadata())
            task = rs.parse_taskbook(path)
            self.assertEqual("RS-TASKBOOK", task["task_id"])
            self.assertTrue(task["_taskbook_path"].endswith("task.md"))
            self.assertEqual("TASK_ISOLATED", task["context_mode"])
            self.assertEqual("UNTRUSTED_HINT_ONLY", task["memory_policy"])
            self.assertEqual("EXPLICIT_ONLY", task["cross_task_import_policy"])

    def test_taskbook_cannot_weaken_context_isolation(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "task.md"
            metadata = self.metadata()
            metadata["memory_policy"] = "TRUST_MEMORY"
            self.write_taskbook(path, metadata)
            with self.assertRaises(rs.SchedulerError):
                rs.parse_taskbook(path)

    def test_load_taskbooks_ignores_readme_and_agents(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            self.write_taskbook(root / "task.md", self.metadata())
            (root / "README.md").write_text("reader", encoding="utf-8")
            (root / "AGENTS.md").write_text("rules", encoding="utf-8")
            tasks = rs.load_taskbooks(root)
            self.assertEqual(["RS-TASKBOOK"], [task["task_id"] for task in tasks])

    def test_unassigned_taskbook_is_valid_without_registry_owner(self):
        legacy = {
            "schema": "ENTERPRISE_MATH_RESEARCH_SCHEDULER_V1",
            "claim_lease_minutes": 120,
            "task_states": ["BACKLOG", "READY", "CLAIMED", "IN_PROGRESS", "HANDOFF_READY", "BLOCKED", "DONE", "SUPERSEDED"],
            "event_types": ["CLAIM", "HEARTBEAT", "PROGRESS", "HANDOFF", "HARD_BLOCK", "UNBLOCK", "DONE", "SUPERSEDE"],
            "selection_policy": {
                "priority_order": ["P0", "P1", "P2", "P3"],
                "leverage_order": ["HIGH", "MEDIUM", "LOW"],
                "state_order": ["HANDOFF_READY", "READY"],
            },
            "tasks": [],
        }
        task = self.metadata()
        task["_taskbook_path"] = "research_tasks/task.md"
        config = rs.merge_taskbooks(legacy, [task])
        self.assertEqual([], rs.validate_scheduler(config, {"branches": {}}))

    def test_taskbook_merge_does_not_mutate_central_config(self):
        config = {"tasks": [{"task_id": "LEGACY"}]}
        task = self.metadata("SCOUT")
        merged = rs.merge_taskbooks(config, [task])
        self.assertEqual(["LEGACY", "SCOUT"], [item["task_id"] for item in merged["tasks"]])
        self.assertEqual(["LEGACY"], [item["task_id"] for item in config["tasks"]])

    def test_legacy_research_tasks_also_inherit_isolation(self):
        config = {"tasks": [self.metadata("LEGACY-RESEARCH")]}
        normalized = rs.normalize_research_context(config)
        task = normalized["tasks"][0]
        self.assertEqual("TASK_ISOLATED", task["context_mode"])
        self.assertEqual("UNTRUSTED_HINT_ONLY", task["memory_policy"])
        self.assertEqual("EXPLICIT_ONLY", task["cross_task_import_policy"])

    def test_selected_task_exposes_context_contract(self):
        item = self.metadata("RS-SELECT")
        config = {
            "schema": "ENTERPRISE_MATH_RESEARCH_SCHEDULER_V1",
            "claim_lease_minutes": 120,
            "task_states": ["BACKLOG", "READY", "CLAIMED", "IN_PROGRESS", "HANDOFF_READY", "BLOCKED", "DONE", "SUPERSEDED"],
            "event_types": ["CLAIM", "HEARTBEAT", "PROGRESS", "HANDOFF", "HARD_BLOCK", "UNBLOCK", "DONE", "SUPERSEDE"],
            "selection_policy": {
                "priority_order": ["P0", "P1", "P2", "P3"],
                "leverage_order": ["HIGH", "MEDIUM", "LOW"],
                "state_order": ["HANDOFF_READY", "READY"],
            },
            "tasks": [item],
        }
        chosen = rs.select_task(config, [], rs.parse_time("2026-08-10T12:00:00+08:00"))
        self.assertEqual("TASK_ISOLATED", chosen["context_mode"])
        self.assertEqual("UNTRUSTED_HINT_ONLY", chosen["memory_policy"])
        self.assertEqual("EXPLICIT_ONLY", chosen["cross_task_import_policy"])


if __name__ == "__main__":
    unittest.main()
