import unittest
from fractions import Fraction

from enterprise_math.abc_projective_efficiency import (
    effective_overhead_decomposition,
    projective_wronskian_efficiency,
)


class AbcProjectiveEfficiencyTests(unittest.TestCase):
    def test_2_plus_7_first_witness_is_projectively_optimal_but_absorption_high(self) -> None:
        efficiency = projective_wronskian_efficiency(2, 7, 9)
        self.assertEqual(efficiency.pair_capacities, (9, 21, 51))
        self.assertEqual(efficiency.sigma_projective, Fraction(1, 3))

        data = effective_overhead_decomposition(2, 7, 9)
        self.assertEqual(data.mu, 1)
        self.assertEqual(data.eta_at_mu, 3)
        self.assertEqual(data.eta_min, 1)
        self.assertEqual(data.first_witness_projective_ratio, Fraction(1, 3))
        self.assertEqual(data.projective_alignment_factor, 1)
        self.assertEqual(data.absorption_level_factor, 3)
        self.assertEqual(data.total_effective_overhead_factor, 3)

    def test_1_plus_242_saturates_both_projective_and_absorption_layers(self) -> None:
        data = effective_overhead_decomposition(1, 242, 243)
        self.assertEqual(data.sigma_projective, Fraction(27, 5))
        self.assertEqual(data.effective_mu, Fraction(27, 5))
        self.assertEqual(data.projective_alignment_factor, 1)
        self.assertEqual(data.absorption_level_factor, 1)
        self.assertEqual(data.total_effective_overhead_factor, 1)

    def test_1_plus_512_has_small_projective_alignment_loss_only(self) -> None:
        data = effective_overhead_decomposition(1, 512, 513)
        self.assertEqual(data.sigma_projective, Fraction(64, 15))
        self.assertEqual(data.first_witness_projective_ratio, Fraction(13, 3))
        self.assertEqual(data.eta_at_mu, 3)
        self.assertEqual(data.eta_min, 3)
        self.assertEqual(data.projective_alignment_factor, Fraction(65, 64))
        self.assertEqual(data.absorption_level_factor, 1)
        self.assertEqual(data.total_effective_overhead_factor, Fraction(65, 64))

    def test_3_plus_125_eta_one_hard_case_is_pure_alignment_loss(self) -> None:
        data = effective_overhead_decomposition(3, 125, 128)
        self.assertEqual(data.sigma_projective, Fraction(32, 7))
        self.assertEqual(data.mu, 6)
        self.assertEqual(data.eta_at_mu, 1)
        self.assertEqual(data.eta_min, 1)
        self.assertEqual(data.projective_alignment_factor, Fraction(21, 16))
        self.assertEqual(data.absorption_level_factor, 1)


if __name__ == "__main__":
    unittest.main()
