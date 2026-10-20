import unittest

from enterprise_math.prime_cubic_horizontal_cursor import (
    PSI12,
    cursor_state_cofactor_certificate,
    first_mr12_prime_after,
    is_prime_mr12,
    lower_cursor_prime_qs,
    verify_cursor_block,
)


class PrimeCubicHorizontalCursorTests(unittest.TestCase):
    def test_mr12_reference_values_and_bound(self):
        self.assertTrue(is_prime_mr12(10_000_000_019))
        self.assertFalse(is_prime_mr12(10_000_000_021))
        self.assertTrue(is_prime_mr12(100_000_000_150_000_000_499))
        with self.assertRaises(ValueError):
            is_prime_mr12(PSI12)

    def test_first_prime_search_is_interval_bounded(self):
        self.assertEqual(first_mr12_prime_after(10_000_000_018, 10_000_000_020), 10_000_000_019)
        self.assertIsNone(first_mr12_prime_after(10_000_000_019, 10_000_000_020))

    def test_first_post_database_cursor_prime_coordinates(self):
        K = 10_000_000_000
        X = 10**20
        # d=1 has only two integer cursor positions and neither is prime.
        self.assertEqual(lower_cursor_prime_qs(K + 1, X), ())
        # By d=7 the first cursor prime 10,000,000,019 is active.
        self.assertIn(10_000_000_019, lower_cursor_prime_qs(K + 7, X))

    def test_one_actual_cursor_state_has_deterministic_cofactor(self):
        K = 10_000_000_000
        X = 10**20
        k = K + 16
        q = 10_000_000_033
        r = cursor_state_cofactor_certificate(k, q, coverage_limit=X)
        self.assertEqual(r, 100_000_000_150_000_000_499)
        self.assertTrue(is_prime_mr12(r))
        self.assertGreater(q * r, k**3)
        self.assertLessEqual(q * r, (k + 1) ** 3 - 1)

    def test_small_frozen_cursor_block_summary(self):
        K = 10_000_000_000
        stats = verify_cursor_block(K + 1, K + 20, coverage_limit=10**20)
        self.assertEqual(stats["states"], 22)
        self.assertEqual(stats["max_search_offset"], 227)
        self.assertEqual(stats["min_slack"], 29_999_999_773)
        self.assertEqual(stats["max_cofactor_prime"], 100_000_000_350_000_000_331)


if __name__ == "__main__":
    unittest.main()
