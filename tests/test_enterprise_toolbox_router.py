import json
from pathlib import Path
import unittest
from unittest.mock import patch

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

    def test_chinese_queries_find_relevant_existing_families(self):
        cases = [
            ("残差 观察 保持", "T0_BRC"),
            ("分支计数", "T1_SCALE_ENUMERATION_VALUATION"),
            ("碰撞 纤维", "T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA"),
            ("碰撞纖維", "T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA"),
            ("軌道穩定子等變對稱", "T7_FINITE_SYMMETRY_EQUIVARIANCE"),
        ]
        for query, expected in cases:
            with self.subTest(query=query):
                ids = [item["id"] for item in toolbox.tool_suggestions(query)[:4]]
                self.assertIn(expected, ids)

    def test_mixed_query_keeps_the_chinese_condition(self):
        registry = {"tools": [
            {"id": "A_PLAIN", "name": "BRC ordinary"},
            {"id": "Z_RESIDUAL", "name": "BRC residual"},
        ]}
        self.assertEqual(toolbox.tool_suggestions("BRC", registry=registry)[0]["id"], "A_PLAIN")
        mixed = toolbox.tool_suggestions("BRC 残差", registry=registry)
        self.assertEqual(mixed[0]["id"], "Z_RESIDUAL")
        self.assertGreater(mixed[0]["score"], mixed[1]["score"])

    def test_unknown_chinese_is_retained_without_character_ngram_matches(self):
        registry = {"tools": [{"id": "LOCAL_TERM", "name": "未编目算子"}]}
        self.assertEqual(toolbox.tool_suggestions("未编目算子", registry=registry)[0]["id"], "LOCAL_TERM")
        self.assertEqual(toolbox.tool_suggestions("未编目外衣", registry=registry), [])
        self.assertEqual(toolbox.tool_suggestions("量子巧克力"), [])
        self.assertEqual(toolbox.tool_suggestions("！？"), [])

    def test_explicit_record_alias_is_searchable(self):
        registry = {"tools": [{"id": "LOCAL_ALIAS", "name": "A local construction", "aliases": ["透明折叠"]}]}
        self.assertEqual(toolbox.tool_suggestions("透明折叠", registry=registry)[0]["id"], "LOCAL_ALIAS")

    def test_longest_alias_and_ascii_identifiers_are_preserved(self):
        self.assertIn("observable", toolbox._tokens("观察量"))
        self.assertNotIn("observer", toolbox._tokens("观察量"))
        self.assertNotIn("quotient", toolbox._tokens("商品"))
        self.assertIn("quotient", toolbox._tokens("商空间"))
        self.assertEqual(toolbox._tokens("x_y v1.2 p+q min-plus"), {"x_y", "v1.2", "p+q", "min-plus"})

    def test_chinese_method_query_reaches_existing_inventory(self):
        suggestions = toolbox.method_suggestions("对称 等变 轨道")
        ids = [item["method_id"] for item in suggestions]
        self.assertIn("recent.r064.s3_equivariant_map_census", ids)

    def test_coverage_distinguishes_search_outcome_from_method_choice(self):
        for matches in ([], [{"id": "EXISTING_IMPLEMENTATION"}]):
            with self.subTest(matches=bool(matches)):
                with patch.object(toolbox, "tool_suggestions", return_value=matches), \
                     patch.object(toolbox, "method_suggestions", return_value=[]), \
                     patch.object(toolbox, "module_suggestions", return_value=[]):
                    result = toolbox.coverage("independent implementation")
                self.assertEqual(result["verdict"], "REUSE_CANDIDATE_FOUND" if matches else "NO_CATALOG_MATCH")
                self.assertIn("ALTERNATIVE_APPROACH_CHOSEN", result["next_rule"])
                self.assertIn("no capability gap is required", result["next_rule"])
                self.assertIn("before novelty claims or shared-tool acceptance", result["next_rule"])
                self.assertEqual(result["tool_families"], matches)
                if not matches:
                    self.assertIn("does not establish a mathematical capability gap", result["next_rule"])


if __name__ == "__main__":
    unittest.main()
