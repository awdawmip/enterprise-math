import unittest

from enterprise_math.p017_cofactor_separation import (
    all_cofactor_windows_separated,
    cofactor_window_pair_separation,
    least_factor_strip_injection,
    raw_cofactor_interval,
)


class P017CofactorSeparationTests(unittest.TestCase):
    def test_pairwise_windows_are_strictly_ordered(self):
        saw_touching = False
        saw_positive_gap = False
        for k in range(4, 180):
            data = all_cofactor_windows_separated(k)
            primes = data["primes"]
            windows = data["windows"]
            for left, right in zip(primes, primes[1:]):
                left_min, _ = windows[left]
                _, right_max = windows[right]
                self.assertLess(right_max, left_min)
                gap = left_min - right_max - 1
                saw_touching |= gap == 0
                saw_positive_gap |= gap > 0
        self.assertTrue(saw_touching)
        self.assertTrue(saw_positive_gap)

    def test_spacing_margin_is_nonnegative(self):
        for k in range(4, 150):
            primes = all_cofactor_windows_separated(k)["primes"]
            for left, right in zip(primes, primes[1:]):
                data = cofactor_window_pair_separation(k, left, right)
                self.assertGreaterEqual(data["spacing_margin"], 0)
                self.assertGreaterEqual(data["integer_gap"], 0)

    def test_least_factor_stripping_is_injective(self):
        saw_nontrivial = False
        for k in range(4, 100):
            data = least_factor_strip_injection(k)
            self.assertEqual(len(data["cofactor_owner"]), data["composite_state_count"])
            saw_nontrivial |= data["composite_state_count"] > 1
        self.assertTrue(saw_nontrivial)

    def test_k3_is_the_sharp_small_exception(self):
        self.assertEqual(raw_cofactor_interval(3, 2), (5, 7))
        self.assertEqual(raw_cofactor_interval(3, 3), (4, 5))
        self.assertEqual(set(range(5, 8)) & set(range(4, 6)), {5})
        with self.assertRaises(ValueError):
            cofactor_window_pair_separation(3, 2, 3)
        with self.assertRaises(ValueError):
            least_factor_strip_injection(3)

    def test_validation(self):
        with self.assertRaises(ValueError):
            raw_cofactor_interval(5, 4)
        with self.assertRaises(ValueError):
            cofactor_window_pair_separation(5, 3, 2)


if __name__ == "__main__":
    unittest.main()
