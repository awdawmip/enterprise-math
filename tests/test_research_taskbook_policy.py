import json
from pathlib import Path
import tempfile
import unittest

import tools.research_taskbook as rt


class ResearchTaskbookPolicyTests(unittest.TestCase):
    def make_root(self):
        td = tempfile.TemporaryDirectory()
        root = Path(td.name)
        (root / "docs").mkdir()
        (root / "research_tasks").mkdir()
        policy = {
            "schema": "ENTERPRISE_MATH_TASKBOOK_POLICY_SET_V1",
            "status": "ACTIVE",
            "policy_inputs": [
                "AGENTS.md",
                "docs/GITHUB_INTERACTION_BUDGET.md",
                "docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md",
                "research_role_policy.json",
                "research_identity_state_machine.json",
                "research_taskbook_contract.json",
            ],
            "conflict_checks": [
                {
                    "id": "TB-REMOTE-RUNTIME",
                    "severity": "ERROR",
                    "patterns": ["github actions", "\\bremote validation\\b"],
                }
            ],
            "restatement_checks": [
                {
                    "id": "TB-RESTATE-REMOTE",
                    "severity": "ERROR",
                    "patterns": ["ci_not_required_for_research"],
                }
            ],
            "override_required_fields": [
                "conflict_id",
                "scope",
                "reason",
                "replacement_behavior",
                "expires_when",
            ],
        }
        (root / "research_taskbook_policy.json").write_text(json.dumps(policy))
        contract = {
            "schema": "ENTERPRISE_MATH_RESEARCH_TASKBOOK_CONTRACT_V2",
            "status": "ACTIVE",
            "new_dispatchable_taskbook_required_metadata": {
                "created_by_role": "RESEARCH_DRIVER",
                "task_authority": "DRIVER_APPROVED",
                "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
                "policy_review": {},
            },
            "forbidden_fixed_runtime_metadata": ["researcher_id"],
        }
        (root / "research_taskbook_contract.json").write_text(json.dumps(contract))
        for rel in [
            "AGENTS.md",
            "docs/GITHUB_INTERACTION_BUDGET.md",
            "docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md",
            "research_role_policy.json",
            "research_identity_state_machine.json",
        ]:
            p = root / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(rel)
        return td, root

    def write_task(self, root, body="## Work\nDo mathematics.\n", overrides=None, digest=None):
        meta = {
            "task_id": "RS-TEST",
            "title": "Test",
            "kind": "RESEARCH",
            "owner": "taskbook/unassigned",
            "base_state": "READY",
            "priority": "P1",
            "leverage": "HIGH",
            "created_by_role": "RESEARCH_DRIVER",
            "task_authority": "DRIVER_APPROVED",
            "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
            "origin_kind": "DIRECT_USER_DIRECTION",
            "task_lineage": "NEW_DIRECTION",
            "policy_review": {
                "policy_set": "research_taskbook_policy.json",
                "policy_digest": digest or rt.policy_digest(root),
                "review_state": "PASS",
                "temporary_overrides": overrides or [],
            },
        }
        path = root / "research_tasks" / "TEST.md"
        path.write_text(rt.render_taskbook(meta, body))
        return path

    def codes(self, findings):
        return {f["code"] for f in findings}

    def test_clean_dispatch_passes(self):
        td, root = self.make_root()
        self.addCleanup(td.cleanup)
        path = self.write_task(root)
        self.assertEqual(rt.audit_taskbook(path, root=root, dispatch=True), [])

    def test_policy_change_makes_stamp_stale(self):
        td, root = self.make_root()
        self.addCleanup(td.cleanup)
        path = self.write_task(root)
        (root / "AGENTS.md").write_text("changed")
        self.assertIn("TB-POLICY-STALE", self.codes(rt.audit_taskbook(path, root=root, dispatch=True)))

    def test_remote_directive_requires_explicit_override(self):
        td, root = self.make_root()
        self.addCleanup(td.cleanup)
        path = self.write_task(root, body="Use GitHub Actions for remote validation.\n")
        self.assertIn("TB-REMOTE-RUNTIME", self.codes(rt.audit_taskbook(path, root=root, dispatch=True)))

    def test_complete_override_allows_policy_sensitive_directive(self):
        td, root = self.make_root()
        self.addCleanup(td.cleanup)
        override = {
            "conflict_id": "TB-REMOTE-RUNTIME",
            "scope": "one final validation after a complete proof candidate",
            "reason": "pinned environment is unavailable locally",
            "replacement_behavior": "one batched remote validation; no iterative remote proof loop",
            "expires_when": "the validation result is captured or the task ends",
        }
        path = self.write_task(root, body="Use GitHub Actions for one remote validation.\n", overrides=[override])
        self.assertNotIn("TB-REMOTE-RUNTIME", self.codes(rt.audit_taskbook(path, root=root, dispatch=True)))

    def test_generic_policy_restatement_is_rejected(self):
        td, root = self.make_root()
        self.addCleanup(td.cleanup)
        path = self.write_task(root, body="CI_NOT_REQUIRED_FOR_RESEARCH.\n")
        self.assertIn("TB-RESTATE-REMOTE", self.codes(rt.audit_taskbook(path, root=root, dispatch=True)))

    def test_unstamped_legacy_warns_but_cannot_dispatch(self):
        td, root = self.make_root()
        self.addCleanup(td.cleanup)
        meta = {
            "task_id": "RS-OLD",
            "title": "Old",
            "created_by_role": "RESEARCH_DRIVER",
            "task_authority": "DRIVER_APPROVED",
            "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
        }
        path = root / "research_tasks" / "OLD.md"
        path.write_text(rt.render_taskbook(meta, "# Old\n"))
        non_dispatch = rt.audit_taskbook(path, root=root, dispatch=False)
        dispatch = rt.audit_taskbook(path, root=root, dispatch=True)
        self.assertEqual(next(f["severity"] for f in non_dispatch if f["code"] == "TB-POLICY-UNSTAMPED"), "WARN")
        self.assertEqual(next(f["severity"] for f in dispatch if f["code"] == "TB-POLICY-UNSTAMPED"), "ERROR")


if __name__ == "__main__":
    unittest.main()
