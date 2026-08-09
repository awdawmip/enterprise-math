import unittest

from enterprise_math.quotient_window import (
    cross_product_separation_sufficient,
    exact_separation_criterion,
    quotient_window,
    separation_gap,
    square_basin_window,
    square_spacing_condition,
    windows_strictly_separated,
)


class QuotientWindowTransportTests(unittest.TestCase):
    def test_exact_window_matches_direct_membership(self) -> None:
        for a in range(0, 30):
            for b in range(a + 1, 40):
                for d in range(1, 16):
                    window = quotient_window(a, b, d)
                    actual = [q for q in range(0, b + 2) if a < d * q <= b]
                    if window is None:
                        self.assertEqual(actual, [])
                    else:
                        self.assertEqual(actual, list(range(window.lo, window.hi + 1)))

    def test_exact_separation_criterion_matches_realized_windows(self) -> None:
        for a in range(1, 30):
            for b in range(a + 1, 45):
                for d in range(1, 12):
                    for e in range(d + 1, 14):
                        wd = quotient_window(a, b, d)
                        we = quotient_window(a, b, e)
                        if wd is None or we is None:
                            continue
                        self.assertEqual(
                            exact_separation_criterion(a, b, d, e),
                            we.hi < wd.lo,
                        )

    def test_cross_product_condition_is_sufficient(self) -> None:
        for a in range(1, 30):
            for b in range(a + 1, 45):
                for d in range(1, 12):
                    for e in range(d + 1, 14):
                        if cross_product_separation_sufficient(a, b, d, e):
                            self.assertTrue(windows_strictly_separated(a, b, d, e))

    def test_square_spacing_gap_two_always_separates(self) -> None:
        for k in range(2, 100):
            for d in range(1, k + 1):
                for e in range(d + 2, k + 1):
                    self.assertTrue(square_spacing_condition(k, d, e))
                    self.assertTrue(
                        windows_strictly_separated(k * k, k * (k + 2), d, e)
                    )

    def test_prime_two_three_boundary_is_sharp_for_raw_windows(self) -> None:
        w2 = square_basin_window(3, 2)
        w3 = square_basin_window(3, 3)
        self.assertIsNotNone(w2)
        self.assertIsNotNone(w3)
        assert w2 is not None and w3 is not None
        self.assertEqual((w2.lo, w2.hi), (5, 7))
        self.assertEqual((w3.lo, w3.hi), (4, 5))
        self.assertFalse(windows_strictly_separated(9, 15, 2, 3))

        self.assertTrue(square_spacing_condition(4, 2, 3))
        self.assertTrue(windows_strictly_separated(16, 24, 2, 3))

    def test_separation_gap_counts_unused_quotient_states(self) -> None:
        self.assertEqual(separation_gap(16, 24, 2, 3), 0)
        self.assertEqual(separation_gap(100, 120, 2, 5), 26)


if __name__ == "__main__":
    unittest.main()
