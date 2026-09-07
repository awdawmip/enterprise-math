from __future__ import annotations

import unittest
from math import gcd, isqrt

from enterprise_math.brc_multiplier_priority_jump import direct_multiplier_jump_from_one
from enterprise_math.brc_multiplier_square_content import (
    jump_state_square_content_reduction,
    odd_n_square_content_scan_reduction,
)


def _gap_witness(n: int, m: int) -> tuple[int, int] | None:
    target = m * n
    x = isqrt(target)
    if x * x < target:
        x += 1
    gap = x * x - target
    y = isqrt(gap)
    return (x, y) if y * y == gap else None


class BRCMultiplierSquareContentTests(unittest.TestCase):
    def test_prime_square_reduction_examples(self) -> None:
        # 9*35 = 18^2-3^2 reduces by 3 to 35 = 6^2-1^2.
        r = odd_n_square_content_scan_reduction(35, 9, 18)
        self.assertEqual(r.square_content_root, 3)
        self.assertEqual(r.common_scale, 3)
        self.assertEqual((r.reduced_multiplier, r.reduced_ceiling_root), (1, 6))
        self.assertEqual(r.scan_representative, 1)
        self.assertEqual(r.status, "REDUCED")

        # 45*203 = 96^2-9^2 reduces by 3 to 5*203 = 32^2-3^2.
        r = odd_n_square_content_scan_reduction(203, 45, 96)
        self.assertEqual(r.common_scale, 3)
        self.assertEqual((r.reduced_multiplier, r.reduced_ceiling_root), (5, 32))
        self.assertEqual(r.scan_representative, 5)

    def test_two_adic_reduction_is_special_case(self) -> None:
        r = odd_n_square_content_scan_reduction(15, 16, 16)
        self.assertEqual(r.square_content_root, 4)
        self.assertEqual(r.common_scale, 4)
        self.assertEqual((r.reduced_multiplier, r.reduced_ceiling_root), (1, 4))
        self.assertEqual(r.scan_representative, 1)

    def test_squareful_multiplier_can_be_irredundant(self) -> None:
        # 9*19=14^2-5^2 with gcd(19,9)=gcd(14,3)=1, so this valid
        # square-gap state cannot strip the square content of multiplier 9.
        state = direct_multiplier_jump_from_one(19, 9)
        self.assertEqual(state.ceiling_root, 14)
        self.assertEqual(gcd(state.n, state.multiplier), 1)
        self.assertEqual(9 * 19, state.ceiling_root**2 - 5**2)
        r = jump_state_square_content_reduction(state)
        self.assertEqual(r.square_content_root, 3)
        self.assertEqual(r.common_scale, 1)
        self.assertEqual(r.scan_representative, 9)
        self.assertTrue(r.gap_test_is_irredundant)

    def test_coprimality_boundary(self) -> None:
        # The former irredundant fixture has gcd(111,9)=3 and is outside
        # the same-gcd transport contract, despite having a square gap.
        state = direct_multiplier_jump_from_one(111, 9)
        self.assertEqual(state.ceiling_root, 32)
        self.assertEqual(gcd(state.n, state.multiplier), 3)
        with self.assertRaisesRegex(ValueError, "reduction requires coprimality"):
            jump_state_square_content_reduction(state)
        with self.assertRaises(ValueError):
            odd_n_square_content_scan_reduction(21, 9, 14)
        with self.assertRaises(ValueError):
            odd_n_square_content_scan_reduction(14, 9, 12)

    def test_bounded_square_gap_witness_transport(self) -> None:
        # For every bounded square-gap witness with gcd(n,m)=1, square-content
        # reduction must preserve the immediate ceiling identity and the gcd
        # factor whenever it actually strips a nontrivial common scale.
        checked = 0
        reduced = 0
        for n in range(3, 1000, 2):
            for m in range(1, 101):
                if gcd(n, m) != 1:
                    continue
                witness = _gap_witness(n, m)
                if witness is None:
                    continue
                checked += 1
                x, y = witness
                r = odd_n_square_content_scan_reduction(n, m, x)
                if r.common_scale == 1:
                    continue
                reduced += 1
                g = r.common_scale
                self.assertEqual(y % g, 0)
                reduced_y = y // g
                self.assertEqual(
                    r.reduced_ceiling_root * r.reduced_ceiling_root
                    - r.reduced_multiplier * n,
                    reduced_y * reduced_y,
                )
                target = r.reduced_multiplier * n
                expected = isqrt(target)
                if expected * expected < target:
                    expected += 1
                self.assertEqual(r.reduced_ceiling_root, expected)
                self.assertEqual(gcd(x - y, n), gcd(r.reduced_ceiling_root - reduced_y, n))
        self.assertGreater(checked, 0)
        self.assertGreater(reduced, 0)


if __name__ == "__main__":
    unittest.main()
