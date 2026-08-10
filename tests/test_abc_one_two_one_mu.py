import unittest
from fractions import Fraction

from enterprise_math.abc_block_value_lattice import block_value_absorption_floor
from enterprise_math.abc_one_two_one_mu import (
    exact_one_two_one_mu,
    one_two_one_coefficients,
    one_two_one_witness_at_radius,
)
from enterprise_math.abc_projective_efficiency import projective_wronskian_efficiency


class AbcOneTwoOneMuTests(unittest.TestCase):
    def test_classic_high_quality_abc_triple_has_exact_mu_601(self) -> None:
        a = 2
        b = 3**10 * 109
        c = 23**5
        self.assertEqual(a + b, c)
        self.assertEqual(
            one_two_one_coefficients(a, b, c),
            (1, 21_454_470, 59_049, 1_399_205),
        )
        self.assertIsNone(one_two_one_witness_at_radius(a, b, c, 600))
        at = one_two_one_witness_at_radius(a, b, c, 601)
        self.assertIsNotNone(at)
        if at is None:
            raise AssertionError("radius 601 must contain a witness")
        self.assertEqual(max(abs(value) for value in at.coordinates), 601)
        self.assertNotEqual(at.wronskian, 0)

        exact = exact_one_two_one_mu(a, b, c, 601)
        self.assertEqual(exact.mu, 601)
        self.assertTrue(exact.lower_radius_infeasible)

    def test_classic_triple_is_intrinsically_saturated_but_near_projective_optimum(self) -> None:
        a = 2
        b = 3**10 * 109
        c = 23**5
        self.assertEqual(block_value_absorption_floor(a, b, c), 1)
        efficiency = projective_wronskian_efficiency(a, b, c)
        self.assertEqual(efficiency.sigma_projective, Fraction(6561, 11))
        alignment = Fraction(601, 1) / efficiency.sigma_projective
        self.assertEqual(alignment, Fraction(6611, 6561))
        self.assertLess(alignment, Fraction(101, 100))

    def test_small_1_2_1_example_matches_known_mu(self) -> None:
        exact = exact_one_two_one_mu(3, 125, 128, 6)
        self.assertEqual(exact.mu, 6)
        self.assertTrue(exact.lower_radius_infeasible)


if __name__ == "__main__":
    unittest.main()
