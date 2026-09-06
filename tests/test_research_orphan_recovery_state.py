import json
import re
import unittest
from pathlib import Path


class ResearchOrphanRecoveryStateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = json.loads(Path("control_plane/research_orphan_recovery_contract.json").read_text())
        cls.state = json.loads(Path(cls.contract["current_state_path"]).read_text())

    def test_state_is_non_dispatch_authority(self):
        self.assertEqual("ENTERPRISE_MATH_RESEARCH_ORPHAN_RECOVERY_STATE_V1", self.state["schema"])
        self.assertIn("NOT_TASK_AVAILABILITY", self.state["status"])
        self.assertIn("NO_CLAIM_AUTHORITY", self.state["status"])
        self.assertRegex(self.state["source_main_sha"], r"^[0-9a-f]{40}$")

    def test_task_orphans_are_fail_closed(self):
        for row in self.state["task_recovery"]:
            self.assertEqual("TASK_RESEARCH_RUNTIME", row["state_machine"])
            self.assertEqual("BLOCKED", row["state"])
            self.assertEqual("BLOCKED", row["dispatch_state"])
            self.assertFalse(row["ordinary_dispatch_eligible"])
            self.assertTrue(row["hard_block"]["code"].startswith("ORPHAN_"))

    def test_free_orphans_stay_in_free_candidate_machine(self):
        for row in self.state["free_recovery"]:
            self.assertEqual("research_axiom_candidate_state_machine.json", row["state_machine"])
            self.assertEqual("DISCOVERY_IN_PROGRESS", row["state"])
            self.assertFalse(row["ordinary_dispatch_eligible"])
            self.assertEqual("NOT_PERFORMED", row["promotion"])
            self.assertTrue(row["free_lane_evidence"])

    def test_recovery_ids_and_source_frontiers_are_unique(self):
        rows = self.state["task_recovery"] + self.state["free_recovery"]
        self.assertEqual(len(rows), len({r["recovery_id"] for r in rows}))
        self.assertEqual(len(rows), len({r["source_tip_sha"] for r in rows}))
        self.assertEqual(len(rows), self.state["summary"]["total_recovery_capsules"])

    def test_recovery_never_synthesizes_claim_identity(self):
        text = json.dumps(self.state)
        self.assertNotIn('"claim_id"', text)
        self.assertNotIn('"researcher_id"', text)
        self.assertIn("NO_RESEARCHER_ID_SYNTHESIS_DURING_RECOVERY", self.contract["freeze"])

    def test_inventory_reads_canonical_main_not_generated_state(self):
        source = Path("tools/research_orphan_inventory.py").read_text()
        self.assertIn('git("ls-tree","-r","--name-only","origin/main")', source)
        self.assertIn('git("show",f"origin/main:{rel}"', source)
        self.assertIn('"research_orphan_recovery" in rel', source)


if __name__ == "__main__":
    unittest.main()
