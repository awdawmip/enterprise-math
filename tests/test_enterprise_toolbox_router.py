import json
from pathlib import Path
import unittest

import tools.enterprise_toolbox as toolbox


ROOT = Path(__file__).resolve().parents[1]


class EnterpriseToolboxRouterTests(unittest.TestCase):
    def test_registry_has_unique_t0_through_t9(self):
        registry = toolbox.load_json(ROOT / "enterprise_toolbox_registry.json")
        ids = [tool["id"] for tool in registry["tools"]]
        self.assertEqual(len(ids), len(set(ids)))
        for index in range(10):
            self.assertTrue(any(tool_id.startswith(f"T{index}_") for tool_id in ids))

    def test_predictive_quotient_need_routes_to_t6(self):
        suggestions = toolbox.tool_suggestions(
            "coarsest quotient preserving future observations under an operation family"
        )
        ids = [item["id"] for item in suggestions[:4]]
        self.assertIn("T6_OPERATION_SAFE_QUOTIENT", ids)

    def test_symmetry_need_routes_to_t7(self):
        suggestions = toolbox.tool_suggestions(
            "orbit stabilizer equivariant relabeling canonical choice"
        )
        self.assertEqual(suggestions[0]["id"], "T7_FINITE_SYMMETRY_EQUIVARIANCE")

    def test_current_source_scan_finds_precision_module(self):
        suggestions = toolbox.module_suggestions("precision carry borrow projection")
        refs = [item["source_ref"] for item in suggestions]
        self.assertIn("src/enterprise_math/precision.py", refs)

    def test_recent_harvest_contains_r064_and_lsr_boundary(self):
        inventory = toolbox.load_json(ROOT / "research_method_inventory.json")
        ids = {method["method_id"] for method in inventory["methods"]}
        self.assertIn("recent.r064.s3_equivariant_map_census", ids)
        self.assertIn("recent.lsr_n2.kernel_readout", ids)
        lsr = next(method for method in inventory["methods"] if method["method_id"] == "recent.lsr_n2.kernel_readout")
        self.assertEqual(lsr["classification"], "CANDIDATE_NOT_TOOL")

    def test_invocation_policy_preserves_discovery_firewalls(self):
        policy = json.loads((ROOT / "tool_invocation_policy.json").read_text(encoding="utf-8"))
        phase_a = policy["role_timing"]["FREE_AXIOM_DISCOVERY_PHASE_A"]
        phase_b = policy["role_timing"]["FREE_AXIOM_DISCOVERY_PHASE_B"]
        task_firewall = policy["role_timing"]["TASK_RESEARCH_DISCOVERY_FIREWALL"]
        self.assertEqual(phase_a["tool_catalog_visibility"], "HIDDEN_AS_DISCOVERY_PRIOR")
        self.assertTrue(phase_a["forbidden_as_question_prior"])
        self.assertTrue(phase_b["mandatory"])
        self.assertFalse(task_firewall["mandatory_before_declared_freeze"])
        self.assertTrue(task_firewall["mandatory_after_declared_freeze"])
        self.assertIn("taskbook", task_firewall["scope_rule"])


if __name__ == "__main__":
    unittest.main()
