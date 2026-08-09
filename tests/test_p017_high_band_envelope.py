import unittest

from enterprise_math.p017_high_band_envelope import (
    ceil_integer_sqrt,
    high_band_composite_envelope,
    high_band_hit_count_envelope,
    high_band_resource_interval,
)


class P017HighBandEnvelopeTests(unittest.TestCase):
    def test_ceil_integer_sqrt(self):
        for n in range(1, 200):
            root = ceil_integer_sqrt(n)
            self.assertGreaterEqual(root * root, n)
            if root > 1:
                self.assertLess((root - 1) * (root - 1), n)

    def test_universal_resource_interval(self):
        self.assertEqual(high_band_resource_interval(110), (15, 56))
        self.assertEqual(high_band_resource_interval(500), (32, 251))

    def test_all_high_band_composites_lie_below_raw_shell_envelope(self):
        for k in (2, 3, 5, 11, 12, 20, 45, 58, 80, 110, 500):
            data = high_band_composite_envelope(k)
            self.assertLessEqual(
                data["exact_composite_count"], data["raw_hit_sum"]
            )
            self.assertTrue(
                all(prime >= data["least_prime_lower"] for prime in data["least_primes"])
            )

    def test_finite_envelope_dominates_exact_l049_capacity(self):
        for k in (2, 3, 5, 11, 12, 20, 45, 58, 80, 110, 500):
            data = high_band_hit_count_envelope(k)
            self.assertLessEqual(
                data["exact_support_capacity"], data["hit_count_sum"]
            )
            self.assertLessEqual(
                data["square_branch_count"], data["cube_root_bound"]
            )
            self.assertLessEqual(
                data["exact_global_triple_bound"], data["finite_triple_envelope"]
            )
            self.assertTrue(
                all(
                    data["resource_lower"] <= prime <= data["resource_upper"]
                    for prime in data["resource_primes"]
                )
            )

    def test_fixed_regression_envelopes(self):
        all110 = high_band_composite_envelope(110)
        self.assertEqual(all110["raw_hit_sum"], 106)
        self.assertEqual(all110["exact_composite_count"], 19)

        k110 = high_band_hit_count_envelope(110)
        self.assertEqual(k110["hit_count_sum"], 72)
        self.assertEqual(k110["cube_root_bound"], 23)
        self.assertEqual(k110["finite_triple_envelope"], 47)
        self.assertEqual(k110["exact_global_triple_bound"], 4)

        all500 = high_band_composite_envelope(500)
        self.assertEqual(all500["raw_hit_sum"], 534)
        self.assertEqual(all500["exact_composite_count"], 77)

        k500 = high_band_hit_count_envelope(500)
        self.assertEqual(k500["hit_count_sum"], 418)
        self.assertEqual(k500["cube_root_bound"], 63)
        self.assertEqual(k500["finite_triple_envelope"], 240)
        self.assertEqual(k500["exact_global_triple_bound"], 17)


if __name__ == "__main__":
    unittest.main()
