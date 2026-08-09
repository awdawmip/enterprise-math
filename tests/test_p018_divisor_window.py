import unittest

from enterprise_math.p018_divisor_window import (
    divisor_quotient_window,
    divisor_window_separation,
    same_parity_divisor_windows,
)


class P018DivisorWindowTests(unittest.TestCase):
    def test_exact_window_endpoints(self):
        for k in range(3, 80):
            for d in range(2, k + 1):
                lo, hi = divisor_quotient_window(k, d)
                values = {n // d for n in range(k * k + 1, (k + 1) * (k + 1))}
                self.assertEqual(min(values), lo)
                self.assertEqual(max(values), hi)

    def test_sufficient_criterion_implies_strict_separation(self):
        for k in range(3, 160):
            for d in range(2, k):
                for e in range(d + 1, k + 1):
                    if 2 * d <= k * (e - d):
                        data = divisor_window_separation(k, d, e)
                        self.assertLess(data["right_window"][1], data["left_window"][0])
                        self.assertGreaterEqual(data["criterion_margin"], 0)
                        self.assertGreaterEqual(data["integer_gap"], 0)

    def test_all_same_parity_pairs_satisfy_criterion(self):
        for k in range(3, 250):
            data = same_parity_divisor_windows(k)
            for d, e in data["checked_pairs"]:
                self.assertEqual((e - d) % 2, 0)
                self.assertGreaterEqual(k * (e - d), 2 * d)

    def test_adjacent_opposite_parity_can_overlap(self):
        self.assertEqual(divisor_quotient_window(3, 2), (5, 7))
        self.assertEqual(divisor_quotient_window(3, 3), (4, 5))
        self.assertEqual(
            set(range(5, 8)).intersection(range(4, 6)),
            {5},
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            divisor_quotient_window(5, 1)
        with self.assertRaises(ValueError):
            divisor_window_separation(10, 6, 7)


if __name__ == "__main__":
    unittest.main()
