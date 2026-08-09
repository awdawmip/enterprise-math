import unittest

from enterprise_math.material_force_work import uniform_force_law
from enterprise_math.material_response import explicit_material_curve_profile
from enterprise_math.material_work_energy_oracle import loading_work_prefix_numerators2
from enterprise_math.material_work_momentum_closure import (
    QUADRATIC_ALGEBRAIC_MOMENTUM,
    RATIONAL_MOMENTUM,
    TURN_NOT_EXACTLY_REPRESENTED,
    algebraic_momentum_from_square_ratio,
    material_rebound_momentum_closure_report,
    material_return_radical_spectrum,
    momentum_square_ratio_from_returned_work,
    square_part_and_squarefree,
)


class MaterialWorkMomentumClosureTests(unittest.TestCase):
    def test_minimal_elastic_two_point_law_requires_sqrt_two_momentum(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 2), returning=(0, 2), amplitude=2
            )
        )
        energy = loading_work_prefix_numerators2(law)[1]
        self.assertEqual(energy, 2)
        report = material_rebound_momentum_closure_report(law, energy)
        self.assertEqual(report.closure_status, QUADRATIC_ALGEBRAIC_MOMENTUM)
        self.assertEqual(
            (report.momentum_square_ratio.numerator, report.momentum_square_ratio.denominator),
            (2, 1),
        )
        self.assertEqual(report.exact_momentum.coefficient_numerator, 1)
        self.assertEqual(report.exact_momentum.coefficient_denominator, 1)
        self.assertEqual(report.exact_momentum.squarefree_radicand, 2)
        self.assertFalse(report.exact_momentum.rational)

    def test_perfect_square_return_work_closes_in_whole_momentum(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 4), returning=(0, 4), amplitude=4
            )
        )
        energy = loading_work_prefix_numerators2(law)[1]
        self.assertEqual(energy, 4)
        report = material_rebound_momentum_closure_report(law, energy)
        self.assertEqual(report.closure_status, RATIONAL_MOMENTUM)
        self.assertTrue(report.exact_momentum.whole_integer)
        self.assertEqual(
            (report.exact_momentum.coefficient_numerator, report.exact_momentum.coefficient_denominator),
            (2, 1),
        )
        self.assertEqual(report.exact_momentum.squarefree_radicand, 1)

    def test_rational_but_noninteger_momentum_is_distinct_from_whole_count_closure(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1), returning=(0, 1), amplitude=1
            ),
            force_scale_factor=4,
        )
        energy = loading_work_prefix_numerators2(law)[1]
        # W2=1, physical force scale 4 => p_count^2=1/4 under unit mass/momentum scales.
        report = material_rebound_momentum_closure_report(law, energy)
        self.assertEqual(report.closure_status, RATIONAL_MOMENTUM)
        self.assertFalse(report.exact_momentum.whole_integer)
        self.assertEqual(
            (report.exact_momentum.coefficient_numerator, report.exact_momentum.coefficient_denominator),
            (1, 2),
        )

    def test_squarefree_decomposition_and_radical_representation_cross_multiply_exactly(self):
        for value in range(0, 500):
            root, squarefree = square_part_and_squarefree(value)
            self.assertEqual(root * root * squarefree, value)
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 6), returning=(0, 6), amplitude=6
            )
        )
        ratio = momentum_square_ratio_from_returned_work(law, 6, 1, 5, 3)
        momentum = algebraic_momentum_from_square_ratio(ratio)
        self.assertEqual(
            momentum.coefficient_numerator ** 2
            * momentum.squarefree_radicand
            * ratio.denominator,
            ratio.numerator * momentum.coefficient_denominator ** 2,
        )

    def test_profile_radical_spectrum_counts_distinct_exact_state_extensions(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 2, 4, 6), returning=(0, 2, 4, 6), amplitude=6
            )
        )
        spectrum = material_return_radical_spectrum(law)
        self.assertEqual(spectrum.radicands_by_depth[0], 1)
        self.assertIn(2, spectrum.distinct_radicands)
        self.assertGreaterEqual(len(spectrum.distinct_radicands), 2)
        self.assertIn(0, spectrum.rationally_closed_depths)
        self.assertTrue(spectrum.algebraic_depths)

    def test_turn_between_material_grid_levels_has_no_momentum_closure_claim(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 2, 4), returning=(0, 1, 2), amplitude=4
            )
        )
        report = material_rebound_momentum_closure_report(law, 5)
        self.assertEqual(report.closure_status, TURN_NOT_EXACTLY_REPRESENTED)
        self.assertIsNone(report.exact_momentum)

    def test_zero_return_work_is_exact_rational_zero(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 2), returning=(0, 0), amplitude=2
            )
        )
        energy = loading_work_prefix_numerators2(law)[1]
        report = material_rebound_momentum_closure_report(law, energy)
        self.assertEqual(report.closure_status, RATIONAL_MOMENTUM)
        self.assertTrue(report.exact_momentum.whole_integer)
        self.assertEqual(report.exact_momentum.coefficient_numerator, 0)


if __name__ == "__main__":
    unittest.main()
