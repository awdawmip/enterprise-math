import json
import tempfile
import unittest
from pathlib import Path

from tools import research_task_registry as registry
from tools import research_taskbook

ROOT = Path(__file__).resolve().parents[1]


def base_meta(**overrides):
    value = {
        "task_id": "RS-TEST-PUB",
        "title": "Publication test",
        "kind": "RESEARCH",
        "owner": "taskbook/unassigned",
        "base_state": "READY",
        "priority": "P0",
        "leverage": "HIGH",
        "frontier": "preserve unresolved residue",
        "next_action": "test exact residue",
        "origin_kind": "DIRECT_USER_DIRECTION",
        "task_lineage": "NEW_DIRECTION",
        "parent_task_id": None,
    }
    value.update(overrides)
    return value


class TaskPublicationAuthorityTests(unittest.TestCase):
    def test_researcher_publication_is_claimable_without_driver_approval_and_rank_is_bounded(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "task.md"
            path.write_text(research_taskbook.render_taskbook(base_meta(), "# test\n"), encoding="utf-8")
            entry = registry.publication_entry(
                base_meta(),
                path=path,
                publisher_role="RESEARCHER",
                publisher_id="EM-TEST-ABC123",
                parent_objective_id="OBJ-ROOT",
                research_value="this residue would otherwise be lost",
                published_at="2026-08-25T20:30:00+08:00",
            )
        self.assertTrue(entry["claimable"])
        self.assertEqual(entry["registry_state"], "CLAIMABLE")
        self.assertEqual(entry["effective_priority"], "P2")
        self.assertEqual(entry["effective_leverage"], "MEDIUM")
        self.assertEqual(entry["publisher_priority_request"], "P0")
        self.assertFalse(entry["working_truth_granted"])
        self.assertFalse(entry["canonical_promotion_granted"])
        self.assertEqual(entry["parent_objective_id"], "OBJ-ROOT")

    def test_driver_uses_same_publication_record_but_keeps_declared_rank(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "task.md"
            path.write_text(research_taskbook.render_taskbook(base_meta(), "# test\n"), encoding="utf-8")
            entry = registry.publication_entry(
                base_meta(),
                path=path,
                publisher_role="RESEARCH_DRIVER",
                publisher_id="EM-DVR-ABC123",
                parent_objective_id="OBJ-ROOT",
                research_value="portfolio task",
                published_at="2026-08-25T20:30:00+08:00",
            )
        self.assertEqual(entry["template_version"], "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1")
        self.assertEqual(entry["effective_priority"], "P0")
        self.assertEqual(entry["effective_leverage"], "HIGH")
        self.assertFalse(entry["working_truth_granted"])

    def test_publication_rejects_orphan_parent_or_missing_research_value(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "task.md"
            path.write_text(research_taskbook.render_taskbook(base_meta(), "# test\n"), encoding="utf-8")
            with self.assertRaisesRegex(registry.RegistryError, "parent_objective_id"):
                registry.publication_entry(
                    base_meta(),
                    path=path,
                    publisher_role="RESEARCHER",
                    publisher_id="EM-TEST-ABC123",
                    parent_objective_id="",
                    research_value="value",
                    published_at="2026-08-25T20:30:00+08:00",
                )
            with self.assertRaisesRegex(registry.RegistryError, "research_value"):
                registry.publication_entry(
                    base_meta(),
                    path=path,
                    publisher_role="RESEARCHER",
                    publisher_id="EM-TEST-ABC123",
                    parent_objective_id="OBJ",
                    research_value="",
                    published_at="2026-08-25T20:30:00+08:00",
                )

    def test_free_research_raw_candidate_cannot_publish_but_audited_candidate_can(self):
        raw = base_meta(
            origin_kind="FREE_AXIOM_CANDIDATE",
            origin_candidate_id="AX-1",
            origin_candidate_state="BLIND_CANDIDATE_FROZEN",
        )
        audited = dict(raw)
        audited["origin_candidate_state"] = "AUDITED_AXIOM_CANDIDATE"
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "task.md"
            path.write_text(research_taskbook.render_taskbook(raw, "# test\n"), encoding="utf-8")
            with self.assertRaisesRegex(registry.RegistryError, "audited candidate"):
                registry.publication_entry(
                    raw,
                    path=path,
                    publisher_role="RESEARCHER",
                    publisher_id="EM-FREE-ABC123",
                    parent_objective_id="FREE-OBJ",
                    research_value="preserve audited direction",
                    published_at="2026-08-25T20:30:00+08:00",
                )
            path.write_text(research_taskbook.render_taskbook(audited, "# test\n"), encoding="utf-8")
            entry = registry.publication_entry(
                audited,
                path=path,
                publisher_role="RESEARCHER",
                publisher_id="EM-FREE-ABC123",
                parent_objective_id="FREE-OBJ",
                research_value="preserve audited direction",
                published_at="2026-08-25T20:30:00+08:00",
            )
        self.assertEqual(entry["origin_kind"], "FREE_AXIOM_CANDIDATE")
        self.assertTrue(entry["claimable"])


class TaskRegistryOrphanAuditTests(unittest.TestCase):
    def make_root(self):
        td = tempfile.TemporaryDirectory()
        root = Path(td.name)
        (root / "research_tasks").mkdir()
        (root / "templates").mkdir()
        (root / "research_taskbook_policy.json").write_text(
            json.dumps({"policy_inputs": []}), encoding="utf-8"
        )
        contract = json.loads((ROOT / "research_task_publication_contract.json").read_text(encoding="utf-8"))
        (root / "research_task_publication_contract.json").write_text(
            json.dumps(contract), encoding="utf-8"
        )
        template = json.loads((ROOT / "templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json").read_text(encoding="utf-8"))
        (root / "templates" / "RESEARCH_TASK_PUBLICATION_TEMPLATE.json").write_text(
            json.dumps(template), encoding="utf-8"
        )
        (root / "research_task_registry.json").write_text(
            json.dumps(
                {
                    "schema": "ENTERPRISE_MATH_RESEARCH_TASK_REGISTRY_V1",
                    "status": "ACTIVE_CANONICAL_TASK_REGISTRY",
                    "tasks": [],
                }
            ),
            encoding="utf-8",
        )
        return td, root

    def write_current_pass_task(self, root, task_id="RS-ORPHAN"):
        digest = research_taskbook.policy_digest(root)
        meta = base_meta(
            task_id=task_id,
            task_authority="PUBLISHED_REGISTERED",
            publication_contract="RESEARCH_TASK_PUBLICATION_V1",
            publication_template="RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
            registry_key=task_id,
            parent_objective_id="OBJ",
            created_by_role="RESEARCHER",
            identity_policy="AUTO_RESOLVE_OR_ALLOCATE",
            final_response_identity_policy="INHERIT_GLOBAL",
            policy_review={
                "policy_set": "research_taskbook_policy.json",
                "policy_digest": digest,
                "review_state": "PASS",
                "temporary_overrides": [],
            },
        )
        path = root / "research_tasks" / f"{task_id}.md"
        path.write_text(research_taskbook.render_taskbook(meta, "# task\n"), encoding="utf-8")
        return path, meta

    def test_current_policy_pass_task_without_registry_record_is_orphan_failure(self):
        td, root = self.make_root()
        self.addCleanup(td.cleanup)
        self.write_current_pass_task(root)
        errors = registry.audit_registry(root=root)
        self.assertTrue(any("orphaned" in error for error in errors))

    def test_matching_registered_task_passes_and_publication_cannot_grant_truth(self):
        td, root = self.make_root()
        self.addCleanup(td.cleanup)
        path, meta = self.write_current_pass_task(root, "RS-REGISTERED")
        entry = {
            "task_id": "RS-REGISTERED",
            "registry_key": "RS-REGISTERED",
            "publication_id": "TP-TEST",
            "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
            "template_version": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
            "taskbook_path": "research_tasks/RS-REGISTERED.md",
            "taskbook_blob_sha1": registry.blob_sha1(path),
            "publisher_role": "RESEARCHER",
            "publisher_id": "EM-TEST-ABC123",
            "published_at": "2026-08-25T20:30:00+08:00",
            "parent_objective_id": "OBJ",
            "origin_kind": meta["origin_kind"],
            "kind": "RESEARCH",
            "task_lineage": meta["task_lineage"],
            "registry_state": "CLAIMABLE",
            "claimable": True,
            "effective_priority": "P2",
            "effective_leverage": "MEDIUM",
            "priority_source": "RESEARCHER_DEFAULT",
            "research_value": "preserve exact residue",
            "terminal_scope": "TASK",
            "working_truth_granted": False,
            "canonical_promotion_granted": False,
        }
        data = json.loads((root / "research_task_registry.json").read_text(encoding="utf-8"))
        data["tasks"] = [entry]
        (root / "research_task_registry.json").write_text(json.dumps(data), encoding="utf-8")
        self.assertEqual([], registry.audit_registry(root=root))

    def test_registry_rejects_truth_or_promotion_smuggling(self):
        td, root = self.make_root()
        self.addCleanup(td.cleanup)
        path, meta = self.write_current_pass_task(root, "RS-SMUGGLE")
        entry = {
            "task_id": "RS-SMUGGLE",
            "registry_key": "RS-SMUGGLE",
            "publication_id": "TP-TEST",
            "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
            "template_version": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
            "taskbook_path": "research_tasks/RS-SMUGGLE.md",
            "taskbook_blob_sha1": registry.blob_sha1(path),
            "publisher_role": "RESEARCHER",
            "publisher_id": "EM-TEST-ABC123",
            "published_at": "2026-08-25T20:30:00+08:00",
            "parent_objective_id": "OBJ",
            "origin_kind": meta["origin_kind"],
            "kind": "RESEARCH",
            "task_lineage": meta["task_lineage"],
            "registry_state": "CLAIMABLE",
            "claimable": True,
            "effective_priority": "P2",
            "effective_leverage": "MEDIUM",
            "priority_source": "RESEARCHER_DEFAULT",
            "research_value": "valuable",
            "terminal_scope": "TASK",
            "working_truth_granted": True,
            "canonical_promotion_granted": True,
        }
        data = json.loads((root / "research_task_registry.json").read_text(encoding="utf-8"))
        data["tasks"] = [entry]
        (root / "research_task_registry.json").write_text(json.dumps(data), encoding="utf-8")
        errors = registry.audit_registry(root=root)
        self.assertTrue(any("Working Truth" in error for error in errors))
        self.assertTrue(any("canonical promotion" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
