import unittest

from enterprise_math.material_effective_layer_1d import effective_material_layer_1d
from enterprise_math.material_response import explicit_material_curve_profile
from enterprise_math.material_scale_phase_diagram import (
    REBOUND_PHASE,
    UNDERRESOLVED_PHASE,
    ZERO_RETURN_PHASE,
    scale_response_phase_for_gap,
)


class MaterialEffectiveLayer1DTests(unittest.TestCase):
    def setUp(self):
        self.profile = explicit_material_curve_profile(
            loading=(0, 100, 200, 300, 400),
            returning=(0, 100, 200, 300, 400),
            amplitude=400,
        )

    def test_full_five_zone_partition_has_exact_clearance_intervals(self):
        # d=7 gives geometric thickness 6, but K=4 leaves gaps 1..2
        # underresolved. B=2 gives k_B=2. Represented depths 2..4 rebound,
        # which map to gaps 3..5; depth 1 maps to zero-return gap 6.
        layer = effective_material_layer_1d(7, 2, self.profile)
        self.assertEqual(layer.geometric_shell_thickness, 6)
        self.assertEqual(layer.underresolved_thickness, 2)
        self.assertEqual(layer.rebound_thickness, 3)
        self.assertEqual(layer.zero_return_thickness, 1)
        self.assertEqual(layer.underresolved_clearances, (1, 2))
        self.assertEqual(layer.rebound_clearances, (3, 5))
        self.assertEqual(layer.zero_return_clearances, (6, 6))
        self.assertEqual(layer.resolved_exterior_min_clearance, 7)

    def test_layer_partition_matches_exact_gap_classifier(self):
        for d in range(1, 10):
            for budget in range(0, 8):
                layer = effective_material_layer_1d(d, budget, self.profile)
                counts = {
                    UNDERRESOLVED_PHASE: 0,
                    REBOUND_PHASE: 0,
                    ZERO_RETURN_PHASE: 0,
                }
                for gap in range(1, d):
                    phase = scale_response_phase_for_gap(
                        gap, d, budget, self.profile
                    ).phase
                    counts[phase] += 1
                self.assertEqual(
                    counts[UNDERRESOLVED_PHASE], layer.underresolved_thickness
                )
                self.assertEqual(counts[REBOUND_PHASE], layer.rebound_thickness)
                self.assertEqual(
                    counts[ZERO_RETURN_PHASE], layer.zero_return_thickness
                )
                self.assertEqual(
                    sum(counts.values()), layer.geometric_shell_thickness
                )

    def test_sufficient_material_depth_removes_inner_underresolution(self):
        deep = explicit_material_curve_profile(
            loading=(0, 100, 200, 300, 400, 400, 400),
            returning=(0, 100, 200, 300, 400, 400, 400),
            amplitude=400,
        )
        layer = effective_material_layer_1d(6, 2, deep)
        self.assertEqual(layer.underresolved_thickness, 0)
        self.assertIsNone(layer.underresolved_clearances)
        self.assertEqual(layer.represented_thickness, 5)

    def test_large_budget_can_remove_outer_zero_return_dead_shell(self):
        layer = effective_material_layer_1d(5, 4, self.profile)
        self.assertEqual(layer.minimum_rebound_depth, 1)
        self.assertEqual(layer.zero_return_thickness, 0)
        self.assertIsNone(layer.zero_return_clearances)
        self.assertEqual(layer.rebound_thickness, 4)

    def test_zero_budget_has_no_true_rebound_band(self):
        layer = effective_material_layer_1d(7, 0, self.profile)
        self.assertIsNone(layer.minimum_rebound_depth)
        self.assertEqual(layer.rebound_thickness, 0)
        self.assertIsNone(layer.rebound_clearances)
        self.assertEqual(layer.zero_return_thickness, 4)
        self.assertEqual(layer.underresolved_thickness, 2)

    def test_terminal_factor_has_no_positive_gap_interaction_shell(self):
        layer = effective_material_layer_1d(1, 10, self.profile)
        self.assertEqual(layer.geometric_shell_thickness, 0)
        self.assertEqual(layer.underresolved_thickness, 0)
        self.assertEqual(layer.rebound_thickness, 0)
        self.assertEqual(layer.zero_return_thickness, 0)
        self.assertIsNone(layer.underresolved_clearances)
        self.assertIsNone(layer.rebound_clearances)
        self.assertIsNone(layer.zero_return_clearances)

    def test_nonmonotone_return_branch_rejects_contiguous_layer_claim(self):
        nonmonotone = explicit_material_curve_profile(
            loading=(0, 100, 200, 300),
            returning=(0, 300, 100, 300),
            amplitude=300,
        )
        with self.assertRaises(ValueError):
            effective_material_layer_1d(5, 1, nonmonotone)


if __name__ == "__main__":
    unittest.main()
