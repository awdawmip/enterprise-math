from pathlib import Path
import unittest

import tools.enterprise_toolbox as toolbox


ROOT = Path(__file__).resolve().parents[1]


class ToolDiscoverySixReturnIntegrationTests(unittest.TestCase):
    def test_registry_has_t10_t11_t12(self):
        registry = toolbox.load_json(ROOT / "enterprise_toolbox_registry.json")
        ids = [tool["id"] for tool in registry["tools"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertIn("T10_LOCAL_REDISTRIBUTION_TOPPLING", ids)
        self.assertIn("T11_DISCRETE_MORSE_CHAIN_REDUCTION", ids)
        self.assertIn("T12_IDEMPOTENT_PATH_CLOSURE_BELLMAN", ids)

    def test_toppling_need_routes_to_t10(self):
        ids = [
            item["id"]
            for item in toolbox.tool_suggestions(
                "legal toppling stabilization odometer least action certificate"
            )[:4]
        ]
        self.assertIn("T10_LOCAL_REDISTRIBUTION_TOPPLING", ids)

    def test_morse_need_routes_to_t11(self):
        ids = [
            item["id"]
            for item in toolbox.tool_suggestions(
                "acyclic matching chain homotopy critical generators Morse reduction"
            )[:4]
        ]
        self.assertIn("T11_DISCRETE_MORSE_CHAIN_REDUCTION", ids)

    def test_idempotent_path_need_routes_to_t12(self):
        ids = [
            item["id"]
            for item in toolbox.tool_suggestions(
                "min-plus Kleene star Bellman all-path closure fixed point"
            )[:4]
        ]
        self.assertIn("T12_IDEMPOTENT_PATH_CLOSURE_BELLMAN", ids)

    def test_method_addendum_is_loaded(self):
        inventory = toolbox.load_method_inventory()
        self.assertIn(
            "research_method_inventory_addenda/20260823_tool_discovery_six_return.json",
            inventory["loaded_addenda"],
        )
        ids = {method["method_id"] for method in inventory["methods"]}
        expected = {
            "tool.toppling_potential",
            "tool.discrete_morse_chain_reduction",
            "tool.idempotent_path_closure_bellman",
            "specialization.weighted_incidence_energy",
            "domain.carrier_voronoi_delaunay",
            "result.discrete_conformal_admissibility",
        }
        self.assertTrue(expected <= ids)

    def test_downgraded_methods_remain_discoverable(self):
        energy = toolbox.method_suggestions("weighted incidence Dirichlet energy")
        self.assertTrue(
            any(item["method_id"] == "specialization.weighted_incidence_energy" for item in energy)
        )
        voronoi = toolbox.method_suggestions("Voronoi nearest site empty ball")
        self.assertTrue(
            any(item["method_id"] == "domain.carrier_voronoi_delaunay" for item in voronoi)
        )
        conformal = toolbox.method_suggestions("circle packing conformal curvature")
        self.assertTrue(
            any(item["method_id"] == "result.discrete_conformal_admissibility" for item in conformal)
        )

    def test_accepted_executable_modules_are_present(self):
        self.assertTrue((ROOT / "src/enterprise_math/discrete_laplacian_chip_firing.py").is_file())
        self.assertTrue((ROOT / "src/enterprise_math/discrete_morse_collapse.py").is_file())

    def test_all_six_frozen_checkers_are_preserved(self):
        names = [
            "tool_discovery_discrete_laplacian_chip_firing_potential_check.py",
            "tool_discovery_discrete_morse_acyclic_matching_check.py",
            "tool_discovery_tropical_residuation_idempotent_closure_check.py",
            "tool_discovery_weighted_incidence_energy_dirichlet_check.py",
            "tool_discovery_carrier_voronoi_delaunay_dual_cell_check.py",
            "tool_discovery_discrete_conformal_circle_pattern_admissibility_check.py",
        ]
        for name in names:
            with self.subTest(name=name):
                self.assertTrue((ROOT / "scripts" / name).is_file())


if __name__ == "__main__":
    unittest.main()
