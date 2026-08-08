import unittest

from enterprise_math.division import (
    division_gap,
    euclidean_state,
    integer_quotient,
    multiple_collapse,
    reconstruct_euclidean,
)


class TestP007DiscreteDivision(unittest.TestCase):
    def test_quotient_characterization(self):
        for divisor in range(1, 13):
            for n in range(0, 241):
                q = integer_quotient(n, divisor)
                self.assertLessEqual(divisor * q, n)
                self.assertLess(n, divisor * (q + 1))

    def test_multiplication_quotient_adjunction(self):
        for divisor in range(1, 10):
            for n in range(0, 80):
                for q in range(0, 20):
                    self.assertEqual(
                        divisor * q <= n,
                        q <= integer_quotient(n, divisor),
                    )

    def test_multiple_collapse_laws(self):
        for divisor in range(1, 13):
            for n in range(0, 241):
                value = multiple_collapse(n, divisor)
                self.assertLessEqual(value, n)
                self.assertEqual(multiple_collapse(value, divisor), value)
                self.assertEqual(value == n, n % divisor == 0)
                self.assertGreaterEqual(division_gap(n, divisor), 0)
                self.assertLess(division_gap(n, divisor), divisor)

    def test_every_multiple_basin_has_divisor_states(self):
        for divisor in range(1, 13):
            for q in range(0, 20):
                basin = [
                    n
                    for n in range(divisor * q, divisor * q + divisor)
                    if multiple_collapse(n, divisor) == divisor * q
                ]
                self.assertEqual(len(basin), divisor)

    def test_quotient_composition_is_multiplicative_and_commutative(self):
        for d in range(1, 10):
            for e in range(1, 10):
                for n in range(0, 241):
                    self.assertEqual(
                        integer_quotient(integer_quotient(n, e), d),
                        integer_quotient(n, d * e),
                    )
                    self.assertEqual(
                        integer_quotient(integer_quotient(n, e), d),
                        integer_quotient(integer_quotient(n, d), e),
                    )

    def test_multiple_projection_commutes_exactly_for_comparable_divisors(self):
        for d in range(1, 13):
            for e in range(1, 13):
                commutes = all(
                    multiple_collapse(multiple_collapse(n, e), d)
                    == multiple_collapse(multiple_collapse(n, d), e)
                    for n in range(0, 4 * d * e + 1)
                )
                comparable = d % e == 0 or e % d == 0
                self.assertEqual(commutes, comparable)

    def test_incomparable_divisors_have_the_universal_larger_divisor_witness(self):
        for d in range(1, 13):
            for e in range(1, 13):
                if d == e or d % e == 0 or e % d == 0:
                    continue
                small, large = sorted((d, e))
                left = multiple_collapse(multiple_collapse(large, large), small)
                right = multiple_collapse(multiple_collapse(large, small), large)
                self.assertGreater(left, 0)
                self.assertEqual(right, 0)
                self.assertNotEqual(left, right)

    def test_euclidean_state_is_lossless_when_remainder_is_explicit(self):
        for divisor in range(1, 13):
            for n in range(0, 241):
                quotient, remainder = euclidean_state(n, divisor)
                self.assertGreaterEqual(remainder, 0)
                self.assertLess(remainder, divisor)
                self.assertEqual(
                    reconstruct_euclidean(quotient, remainder, divisor),
                    n,
                )

    def test_invalid_remainder_is_rejected(self):
        with self.assertRaises(ValueError):
            reconstruct_euclidean(2, 5, 5)


if __name__ == "__main__":
    unittest.main()
