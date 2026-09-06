from __future__ import annotations

import unittest

from enterprise_math.brc_residue_wheel_complexity import (
    canonical_difference_square_pair,
    fixed_squarehood_wheel_must_be_nonempty,
    fixed_wheel_boundary,
    legendre_symbol_reference,
    periodic_support_count,
    prime_shift_square_support_count,
)
from enterprise_math.brc_square_gap_prefilter import square_residue_table


def _contains(table: bytes, modulus: int, value: int) -> bool:
    residue = value % modulus
    return bool(table[residue >> 3] & (1 << (residue & 7)))


class BRCResidueWheelComplexityTests(unittest.TestCase):
    def test_periodic_count_exact_formula(self) -> None:
        period = 7
        offsets = (0, 2, 5)
        for limit in range(100):
            direct = sum((t % period) in offsets for t in range(limit))
            self.assertEqual(periodic_support_count(period, offsets, limit), direct)
        boundary = fixed_wheel_boundary(period, offsets, 1000)
        self.assertEqual(boundary.exact_candidates, periodic_support_count(period, offsets, 1000))
        self.assertEqual((boundary.positive_density_numerator, boundary.positive_density_denominator), (3, 7))

    def test_canonical_difference_square_pair(self) -> None:
        for value in range(1, 400):
            if value % 4 == 2:
                with self.assertRaises(ValueError):
                    canonical_difference_square_pair(value)
                continue
            pair = canonical_difference_square_pair(value)
            self.assertEqual(pair.x * pair.x - pair.y * pair.y, value)
            self.assertGreaterEqual(pair.t_from_ceiling, 0)

    def test_every_admissible_value_gives_nonempty_qr_wheel(self) -> None:
        for value in range(1, 250):
            if value % 4 == 2:
                continue
            for modulus in (8, 9, 16, 21, 63, 1008):
                self.assertTrue(fixed_squarehood_wheel_must_be_nonempty(value, modulus))
                pair = canonical_difference_square_pair(value)
                base = pair.x - pair.t_from_ceiling
                t = pair.t_from_ceiling % modulus
                gap = (base + t) * (base + t) - value
                self.assertTrue(_contains(square_residue_table(modulus), modulus, gap))

    def test_prime_local_support_formula_against_enumeration(self) -> None:
        for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
            table = square_residue_table(p)
            for c in range(p):
                direct = sum(_contains(table, p, x * x - c) for x in range(p))
                self.assertEqual(prime_shift_square_support_count(p, c), direct)

    def test_legendre_symbol_reference(self) -> None:
        self.assertEqual(legendre_symbol_reference(0, 11), 0)
        self.assertEqual(legendre_symbol_reference(3, 11), 1)
        self.assertEqual(legendre_symbol_reference(2, 11), -1)


if __name__ == "__main__":
    unittest.main()
