from __future__ import annotations

import random
import unittest
from fractions import Fraction
from math import isqrt
from types import SimpleNamespace

from enterprise_math.brc_error_linearization_pell import (
    brc_gap_after_crossings,
    pell_linear_recurrence_next,
    pell_pade_pair,
    pell_two_correction_certificate,
    post_truncation_derivative_ratio,
    transport_pell_tail,
)


class BRCErrorLinearizationPellTests(unittest.TestCase):
    def test_post_truncation_derivative_ratio_is_affine(self) -> None:
        for degree in (2, 4, 8, 16):
            for order in range(degree + 1, degree + 7):
                self.assertEqual(
                    post_truncation_derivative_ratio(degree, order),
                    Fraction(1, 2) - order,
                )

    def test_recursive_brc_gap_has_constant_second_difference(self) -> None:
        a = 37
        g0 = 10000
        values = [brc_gap_after_crossings(a, g0, q) for q in range(8)]
        first = [b - a0 for a0, b in zip(values, values[1:])]
        second = [b - a0 for a0, b in zip(first, first[1:])]
        third = [b - a0 for a0, b in zip(second, second[1:])]
        self.assertTrue(all(value == -2 for value in second))
        self.assertTrue(all(value == 0 for value in third))

    def test_pell_identity_and_linear_order_recurrence(self) -> None:
        for m in range(2, 40):
            for h in (1, 2):
                if m < h:
                    continue
                pairs = [pell_pade_pair(m, h, n) for n in range(1, 8)]
                for n, (a, b) in enumerate(pairs, start=1):
                    self.assertEqual((m + h) * b * b - m * a * a, h ** (2 * n + 1))
                    self.assertLess(m * a * a, (m + h) * b * b)
                a0, b0 = 1, 1
                a1, b1 = pairs[0]
                self.assertEqual(a1, 4 * m + 3 * h)
                self.assertEqual(b1, 4 * m + h)
                prev_a, cur_a = a0, a1
                prev_b, cur_b = b0, b1
                for index in range(2, 8):
                    next_a = pell_linear_recurrence_next(prev_a, cur_a, m, h)
                    next_b = pell_linear_recurrence_next(prev_b, cur_b, m, h)
                    self.assertEqual((next_a, next_b), pairs[index - 1])
                    prev_a, cur_a = cur_a, next_a
                    prev_b, cur_b = cur_b, next_b

    def test_certified_transport_matches_direct_roots_small(self) -> None:
        for n_value in range(3, 500, 2):
            for m in range(2, 40):
                j = isqrt(m * n_value)
                r = m * n_value - j * j
                source = SimpleNamespace(n=n_value, multiplier=m, root=j, remainder=r)
                for h in (1, 2):
                    for order in (1, 2, 4, 8, 16):
                        if not pell_two_correction_certificate(j, m, h, order):
                            continue
                        state = transport_pell_tail(source, m + h, order=order)
                        expected = isqrt((m + h) * n_value)
                        self.assertEqual(state.root, expected)
                        self.assertEqual(
                            state.remainder,
                            (m + h) * n_value - expected * expected,
                        )
                        self.assertLessEqual(state.correction_steps, 2)
                        break

    def test_random_large_certified_transport(self) -> None:
        rng = random.Random(20260907)
        cases = (
            (512, 7, 2, 32),
            (1024, 124, 2, 32),
            (2048, 126, 2, 64),
            (2048, 8, 2, 128),
            (4096, 127, 2, 128),
        )
        for bits, m, h, order in cases:
            for _ in range(8):
                n_value = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
                j = isqrt(m * n_value)
                r = m * n_value - j * j
                source = SimpleNamespace(n=n_value, multiplier=m, root=j, remainder=r)
                self.assertTrue(pell_two_correction_certificate(j, m, h, order))
                state = transport_pell_tail(source, m + h, order=order)
                expected = isqrt((m + h) * n_value)
                self.assertEqual(state.root, expected)
                self.assertLessEqual(state.correction_steps, 2)


if __name__ == "__main__":
    unittest.main()
