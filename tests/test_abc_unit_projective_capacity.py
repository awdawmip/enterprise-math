import unittest
from fractions import Fraction

from enterprise_math.abc_unit_projective_capacity import (
    capacity_support_lower_bound_holds,
    minimum_capacity_for_support_count,
    unit_projective_capacity_state,
    unit_sqrt_bound_counterexamples,
)


class AbcUnitProjectiveCapacityTests(unittest.TestCase):
    def test_capacity_support_shell_minima(self) -> None:
        self.assertEqual(minimum_capacity_for_support_count(0), 0)
        self.assertEqual(minimum_capacity_for_support_count(1), 1)
        self.assertEqual(minimum_capacity_for_support_count(2), 5)
        self.assertEqual(minimum_capacity_for_support_count(3), 31)
        self.assertEqual(minimum_capacity_for_support_count(4), 247)

    def test_capacity_shell_bound_on_working_examples(self) -> None:
        for n in (242, 243, 288, 289, 57121, 57122, 3**10 * 109):
            self.assertTrue(capacity_support_lower_bound_holds(n))

    def test_1_plus_242_cross_capacity(self) -> None:
        data = unit_projective_capacity_state(242, 243)
        self.assertEqual(data.capacities, (15, 5))
        self.assertEqual(data.residuals, (11, 81))
        self.assertEqual(data.cross_ratios, (Fraction(27, 5), Fraction(11, 5)))
        self.assertEqual(data.sigma_projective, Fraction(27, 5))
        self.assertEqual(data.dominant_side, "c_residual_over_b_capacity")

    def test_1_plus_512_cross_capacity(self) -> None:
        data = unit_projective_capacity_state(512, 513)
        self.assertEqual(data.capacities, (9, 60))
        self.assertEqual(data.residuals, (256, 9))
        self.assertEqual(data.cross_ratios, (Fraction(1, 1), Fraction(64, 15)))
        self.assertEqual(data.sigma_projective, Fraction(64, 15))
        self.assertEqual(data.dominant_side, "b_residual_over_c_capacity")

    def test_sqrt_conjecture_is_false(self) -> None:
        first, second = unit_sqrt_bound_counterexamples()
        self.assertEqual((first.b, first.c, first.sigma_projective), (288, 289, Fraction(24, 1)))
        self.assertEqual(
            (second.b, second.c, second.capacities, second.residuals, second.sigma_projective),
            (57121, 57122, (2, 21), (239, 2197), Fraction(2197, 2)),
        )


if __name__ == "__main__":
    unittest.main()
