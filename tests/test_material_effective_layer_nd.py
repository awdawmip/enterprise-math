import unittest
from itertools import product

from enterprise_math.material_effective_layer_nd import (
    effective_material_state_mass_nd,
)
from enterprise_math.material_effective_layer_1d import effective_material_layer_1d
from enterprise_math.material_response import explicit_material_curve_profile
from enterprise_math.material_scale_phase_diagram import scale_response_phase_for_gap


class MaterialEffectiveLayerNDTests(unittest.TestCase):
    def setUp(self):
        self.profile = explicit_material_curve_profile(
            loading=(0, 100, 200, 300, 400),
            returning=(0, 100, 200, 300, 400),
            amplitude=400,
        )

    def test_closed_form_matches_direct_clearance_vector_classification(self):
        for dimension in range(1, 5):
            for d in range(1, 8):
                for budget in range(0, 7):
                    report = effective_material_state_mass_nd(
                        dimension, d, budget, self.profile
                    )
                    direct = {"UNDERRESOLVED": 0, "ZERO_RETURN": 0, "REBOUND": 0}
                    for clearances in product(range(d), repeat=dimension):
                        if not any(clearances):
                            continue
                        controlling_gap = max(clearances)
                        phase = scale_response_phase_for_gap(
                            controlling_gap,
                            d,
                            budget,
                            self.profile,
                        ).phase
                        direct[phase] += 1
                    self.assertEqual(
                        report.underresolved_states, direct["UNDERRESOLVED"]
                    )
                    self.assertEqual(report.zero_return_states, direct["ZERO_RETURN"])
                    self.assertEqual(report.rebound_states, direct["REBOUND"])
                    self.assertEqual(report.coarse_only_states, d**dimension - 1)

    def test_one_dimensional_counts_equal_effective_layer_thicknesses(self):
        for d in range(1, 10):
            for budget in range(0, 8):
                nd = effective_material_state_mass_nd(1, d, budget, self.profile)
                one = effective_material_layer_1d(d, budget, self.profile)
                self.assertEqual(nd.underresolved_states, one.underresolved_thickness)
                self.assertEqual(nd.zero_return_states, one.zero_return_thickness)
                self.assertEqual(nd.rebound_states, one.rebound_thickness)

    def test_reference_2d_telescoping_counts(self):
        report = effective_material_state_mass_nd(2, 7, 2, self.profile)
        self.assertEqual(report.coarse_only_states, 48)
        self.assertEqual(report.underresolved_states, 8)
        self.assertEqual(report.rebound_states, 27)
        self.assertEqual(report.zero_return_states, 13)
        self.assertEqual(8 + 27 + 13, 48)

    def test_zero_budget_has_no_true_rebound_states(self):
        for dimension in (1, 2, 3, 4):
            report = effective_material_state_mass_nd(
                dimension, 7, 0, self.profile
            )
            self.assertEqual(report.rebound_states, 0)
            self.assertEqual(
                report.zero_return_states + report.underresolved_states,
                report.coarse_only_states,
            )

    def test_sufficient_depth_and_budget_can_fill_entire_coarse_box_with_rebound_states(self):
        full = explicit_material_curve_profile(
            loading=(0, 400, 400, 400, 400, 400),
            returning=(0, 400, 400, 400, 400, 400),
            amplitude=400,
        )
        for dimension in (1, 2, 3):
            report = effective_material_state_mass_nd(dimension, 6, 1, full)
            self.assertEqual(report.underresolved_states, 0)
            self.assertEqual(report.zero_return_states, 0)
            self.assertEqual(report.rebound_states, 6**dimension - 1)

    def test_invalid_inputs_and_nonmonotone_branch_are_rejected(self):
        with self.assertRaises(ValueError):
            effective_material_state_mass_nd(0, 3, 1, self.profile)
        with self.assertRaises(ValueError):
            effective_material_state_mass_nd(2, 0, 1, self.profile)
        with self.assertRaises(ValueError):
            effective_material_state_mass_nd(2, 3, -1, self.profile)
        nonmonotone = explicit_material_curve_profile(
            loading=(0, 100, 200, 300),
            returning=(0, 300, 100, 300),
            amplitude=300,
        )
        with self.assertRaises(ValueError):
            effective_material_state_mass_nd(2, 4, 1, nonmonotone)


if __name__ == "__main__":
    unittest.main()
