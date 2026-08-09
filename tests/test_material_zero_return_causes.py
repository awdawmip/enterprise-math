import unittest
from itertools import product

from enterprise_math.material_response import explicit_material_curve_profile
from enterprise_math.material_zero_return_causes import (
    first_positive_return_depth,
    zero_return_decomposition_nd,
)


class MaterialZeroReturnCausesTests(unittest.TestCase):
    def setUp(self):
        self.profile = explicit_material_curve_profile(
            loading=(0, 0, 100, 200, 400),
            returning=(0, 0, 100, 200, 400),
            amplitude=400,
        )

    def test_first_positive_material_depth_is_distinct_from_kinematic_threshold(self):
        self.assertEqual(first_positive_return_depth(self.profile), 2)
        low = zero_return_decomposition_nd(1, 6, 1, self.profile)
        high = zero_return_decomposition_nd(1, 6, 4, self.profile)
        self.assertEqual(low.first_positive_material_depth, 2)
        self.assertEqual(high.first_positive_material_depth, 2)
        self.assertGreaterEqual(
            low.first_nonzero_kinematic_depth,
            low.first_positive_material_depth,
        )
        self.assertEqual(high.first_nonzero_kinematic_depth, 2)

    def test_direct_clearance_enumeration_matches_cause_split(self):
        for dimension in range(1, 4):
            for d in range(1, 8):
                for budget in range(0, 7):
                    report = zero_return_decomposition_nd(
                        dimension, d, budget, self.profile
                    )
                    material_zero = 0
                    kinematic_zero = 0
                    rebound = 0
                    underresolved = 0
                    max_depth = len(self.profile.returning) - 1
                    for clearances in product(range(d), repeat=dimension):
                        if not any(clearances):
                            continue
                        gap = max(clearances)
                        depth = d - gap
                        if depth > max_depth:
                            underresolved += 1
                            continue
                        sample = self.profile.returning[depth]
                        if sample == 0:
                            material_zero += 1
                        elif budget * sample < self.profile.amplitude:
                            kinematic_zero += 1
                        else:
                            rebound += 1
                    self.assertEqual(report.material_zero_states, material_zero)
                    self.assertEqual(
                        report.kinematic_quantization_zero_states,
                        kinematic_zero,
                    )
                    self.assertEqual(report.rebound_states, rebound)
                    self.assertEqual(report.underresolved_states, underresolved)

    def test_increasing_budget_never_erases_intrinsic_material_zero_states(self):
        reports = [
            zero_return_decomposition_nd(2, 6, budget, self.profile)
            for budget in range(0, 20)
        ]
        material_counts = {report.material_zero_states for report in reports}
        self.assertEqual(len(material_counts), 1)
        kinematic_counts = [
            report.kinematic_quantization_zero_states for report in reports
        ]
        rebound_counts = [report.rebound_states for report in reports]
        self.assertEqual(kinematic_counts, sorted(kinematic_counts, reverse=True))
        self.assertEqual(rebound_counts, sorted(rebound_counts))

    def test_large_budget_reduces_zero_return_to_only_material_dead_zone(self):
        report = zero_return_decomposition_nd(3, 6, 400, self.profile)
        self.assertEqual(report.first_positive_material_depth, 2)
        self.assertEqual(report.first_nonzero_kinematic_depth, 2)
        self.assertEqual(report.kinematic_quantization_zero_states, 0)
        self.assertGreater(report.material_zero_states, 0)
        self.assertEqual(
            report.material_zero_states
            + report.rebound_states
            + report.underresolved_states,
            report.coarse_only_states,
        )

    def test_all_zero_material_branch_has_no_kinematic_component(self):
        zero = explicit_material_curve_profile(
            loading=(0, 0, 0, 0),
            returning=(0, 0, 0, 0),
            amplitude=100,
        )
        self.assertIsNone(first_positive_return_depth(zero))
        report = zero_return_decomposition_nd(2, 5, 1000, zero)
        self.assertIsNone(report.first_positive_material_depth)
        self.assertIsNone(report.first_nonzero_kinematic_depth)
        self.assertEqual(report.kinematic_quantization_zero_states, 0)
        self.assertEqual(
            report.material_zero_states,
            report.coarse_only_states - report.underresolved_states,
        )
        self.assertEqual(report.rebound_states, 0)

    def test_nonmonotone_branch_is_rejected(self):
        nonmonotone = explicit_material_curve_profile(
            loading=(0, 0, 200, 100),
            returning=(0, 0, 200, 100),
            amplitude=200,
        )
        with self.assertRaises(ValueError):
            zero_return_decomposition_nd(2, 4, 2, nonmonotone)


if __name__ == "__main__":
    unittest.main()
