import unittest
from fractions import Fraction

from enterprise_math.abc_projective_tail_moment import (
    dyadic_fractional_moment_tail_envelope,
    projective_dyadic_tail_union_bound,
    projective_tail_power_envelope,
)


class AbcProjectiveTailMomentTests(unittest.TestCase):
    def test_exact_tail_union_bound_decreases_with_threshold(self) -> None:
        X = 10**6
        first = projective_dyadic_tail_union_bound(X, 100)
        second = projective_dyadic_tail_union_bound(X, 10_000)
        self.assertGreater(first.component_union_bound, second.component_union_bound)
        self.assertGreater(first.triple_union_bound, second.triple_union_bound)
        self.assertEqual(first.square_root_threshold, 10)
        self.assertEqual(second.square_root_threshold, 100)

    def test_exact_union_bound_below_simple_power_envelope(self) -> None:
        for X, threshold in ((10**4, 7), (10**6, 100), (10**8, 10_001)):
            exact = projective_dyadic_tail_union_bound(X, threshold)
            envelope = projective_tail_power_envelope(X, threshold)
            self.assertLessEqual(exact.triple_union_bound, envelope)

    def test_fractional_moment_envelope_is_uniform_quadratic_below_half(self) -> None:
        X = 10**5
        quarter = dyadic_fractional_moment_tail_envelope(X, 1, 4)
        two_fifths = dyadic_fractional_moment_tail_envelope(X, 2, 5)
        self.assertEqual(quarter, Fraction(7, 1) * X * X)
        self.assertGreater(two_fifths, quarter)
        self.assertEqual(two_fifths.denominator, 1)

    def test_half_moment_is_deliberately_outside_bounded_envelope(self) -> None:
        with self.assertRaises(ValueError):
            dyadic_fractional_moment_tail_envelope(10**5, 1, 2)


if __name__ == "__main__":
    unittest.main()
