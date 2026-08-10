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
            "created_by_role": "RESEARCH_DRIVER",
            "task_authority": "DRIVER_APPROVED",
        }

    def write_taskbook(self, path, metadata):
        path.write_text(
            "<!-- ENTERPRISE_MATH_TASK_V1\n"
            + json.dumps(metadata)
            + "\n-->\n# task\n",
            encoding="utf-8",
        )

    def write_proposal_bundle(self, path, *, parent_task_id="RS-PARENT"):
        path.write_text(
            json.dumps(
                {
                    "schema": rs.PROPOSAL_SCHEMA,
                    "parent_task_id": parent_task_id,
                    "created_by_role": "RESEARCHER",
                    "at": "2026-08-10T19:30:00+08:00",
                    "candidates": [
                        {
                            "proposal_id": "P-1",
                            "title": "Candidate branch",
                            "research_question": "Does the candidate theorem hold?",
                            "why_now": "A new obstruction appeared in the parent task.",
                            "expected_leverage": "HIGH",
                            "evidence_refs": ["parent-result:T1"],
                        },
                        {
                            "proposal_id": "P-2",
                            "title": "Second branch",
                            "research_question": "Is there a minimal repair?",
                            "why_now": "The same checkpoint exposes a second route.",
                            "expected_leverage": "MEDIUM",
                            "evidence_refs": ["parent-result:C1"],
                        },
                    ],
                }
            ),
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
            self.assertEqual("RESEARCH_DRIVER", task["created_by_role"])
            self.assertEqual("DRIVER_APPROVED", task["task_authority"])

    def test_taskbook_cannot_weaken_context_isolation(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "task.md"
            metadata = self.metadata()
            metadata["memory_policy"] = "TRUST_MEMORY"
            self.write_taskbook(path, metadata)
            with self.assertRaises(rs.SchedulerError):
                rs.parse_taskbook(path)

    def test_new_taskbook_without_driver_authority_is_not_dispatchable(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "task.md"
            metadata = self.metadata("RS-NEW-UNAPPROVED")
            metadata.pop("created_by_role")
            metadata.pop("task_authority")
            self.write_taskbook(path, metadata)
            with self.assertRaises(rs.SchedulerError):
                rs.parse_taskbook(path)

    def test_grandfathered_taskbook_does_not_break_ongoing_research(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "task.md"
            metadata = self.metadata("RS-R006-CROSS-POWER-COLLAPSE-WELL-ALGEBRA")
            metadata.pop("created_by_role")
            metadata.pop("task_authority")
            self.write_taskbook(path, metadata)
            task = rs.parse_taskbook(path)
            self.assertEqual("RESEARCH_DRIVER", task["created_by_role"])
            self.assertEqual("GRANDFATHERED_DRIVER_APPROVED", task["task_authority"])

    def test_load_taskbooks_ignores_readme_and_agents(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            self.write_taskbook(root / "task.md", self.metadata())
            (root / "README.md").write_text("reader", encoding="utf-8")
            (root / "AGENTS.md").write_text("rules", encoding="utf-8")
            tasks = rs.load_taskbooks(root)
            self.assertEqual(["RS-TASKBOOK"], [task["task_id"] for task in tasks])

    def test_proposal_bundle_batches_candidates_but_never_dispatches_them(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            self.write_proposal_bundle(root / "bundle.json")
            proposals = rs.load_proposal_queue(root)
            self.assertEqual(["P-1", "P-2"], [item["proposal_id"] for item in proposals])
            self.assertTrue(all(item["review_state"] == "PENDING_DRIVER_REVIEW" for item in proposals))
            self.assertTrue(all(item["dispatchable"] is False for item in proposals))
            self.assertTrue(all(item["created_by_role"] == "RESEARCHER" for item in proposals))

    def test_proposal_bundle_does_not_enter_task_merge(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            self.write_proposal_bundle(root / "bundle.json")
            proposals = rs.load_proposal_queue(root)
            config = {"tasks": [{"task_id": "LEGACY"}]}
            self.assertEqual(2, len(proposals))
            self.assertEqual(["LEGACY"], [item["task_id"] for item in config["tasks"]])

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

    def test_selected_task_exposes_researcher_role_and_context_contract(self):
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
        self.assertEqual("RESEARCHER", chosen["session_role"])
        self.assertEqual("EXPLICIT_CURRENT_CONVERSATION_ONLY", chosen["driver_activation"])


if __name__ == "__main__":
    unittest.main()
