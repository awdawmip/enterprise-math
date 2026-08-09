import unittest

from enterprise_math.quotient_window import (
    factor_window_for_quotient_bucket,
    factor_window_meets_bucket,
    quotient_window,
    square_basin_root_factor_window,
)


class DualFactorWindowTests(unittest.TestCase):
    def test_dual_factor_window_matches_direct_existence(self) -> None:
        for a in range(0, 20):
            for b in range(a + 1, 30):
                for q_lo in range(1, 8):
                    for q_hi in range(q_lo, 9):
                        window = factor_window_for_quotient_bucket(
                            a, b, q_lo, q_hi
                        )
                        actual = [
                            d
                            for d in range(1, b + 2)
                            if any(a < d * q <= b for q in range(q_lo, q_hi + 1))
                        ]
                        if window is None:
                            self.assertEqual(actual, [])
                        else:
                            self.assertEqual(
                                actual, list(range(window.lo, window.hi + 1))
                            )

    def test_factor_and_quotient_views_are_exact_duals(self) -> None:
        for a in range(0, 20):
            for b in range(a + 1, 30):
                for d in range(1, 15):
                    q_window = quotient_window(a, b, d)
                    for q_lo in range(1, 8):
                        for q_hi in range(q_lo, 9):
                            direct = (
                                q_window is not None
                                and max(q_window.lo, q_lo) <= min(q_window.hi, q_hi)
                            )
                            self.assertEqual(
                                factor_window_meets_bucket(
                                    a, b, d, q_lo, q_hi
                                ),
                                direct,
                            )

    def test_square_root_bucket_specialization(self) -> None:
        for k in range(2, 40):
            for root in range(1, 20):
                factors = square_basin_root_factor_window(k, root)
                actual = []
                for d in range(1, k * (k + 2) + 1):
                    q_window = quotient_window(k * k, k * (k + 2), d)
                    if q_window is None:
                        continue
                    if max(q_window.lo, root * root) <= min(
                        q_window.hi, root * (root + 2)
                    ):
                        actual.append(d)
                if factors is None:
                    self.assertEqual(actual, [])
                else:
                    self.assertEqual(
                        actual, list(range(factors.lo, factors.hi + 1))
                    )


if __name__ == "__main__":
    unittest.main()
