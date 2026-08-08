import unittest

from enterprise_math.basin_aggregate import (
    exact_transverse_support_hit,
    four_support_basin_mass,
    transverse_primes,
    unique_large_modulus_hit,
)


class BasinAggregateTests(unittest.TestCase):
    def test_unique_large_modulus_hit_uses_centered_carry(self):
        hit = unique_large_modulus_hit(58, 1155)
        self.assertIsNotNone(hit)
        self.assertEqual(hit["state"], 3465)
        self.assertEqual(hit["cofactor"], 3)
        self.assertEqual(hit["half_scale"], 29)
        self.assertEqual(hit["offset"], 43)

        self.assertIsNone(unique_large_modulus_hit(58, 1000))

    def test_exact_four_support_accepts_smooth_cofactor(self):
        hit = exact_transverse_support_hit(58, [3, 5, 7, 11])
        self.assertIsNotNone(hit)
        self.assertEqual(hit["state"], 3465)
        self.assertEqual(hit["cofactor"], 3)
        self.assertEqual(hit["cofactor_prime_factors"], [3])

    def test_subset_of_five_support_is_rejected_by_extra_cofactor_prime(self):
        # 291^2 < 85085 < 292^2 and
        # 85085 = 5*7*11*13*17.  All five primes avoid 291*292.
        self.assertTrue(all(p in transverse_primes(291) for p in [5, 7, 11, 13, 17]))
        hit = exact_transverse_support_hit(291, [5, 7, 11, 13])
        self.assertIsNone(hit)

    def test_anchor_support_is_rejected(self):
        # 5 and 7 divide the anchor 70*71 through the k=70 factor.
        with self.assertRaises(ValueError):
            exact_transverse_support_hit(70, [5, 7, 11, 13])

    def test_four_support_aggregate_finds_known_negative_state(self):
        aggregate = four_support_basin_mass(58)
        matches = [
            item
            for item in aggregate["contributions"]
            if item["support"] == [3, 5, 7, 11]
        ]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["state"], 3465)
        self.assertEqual(matches[0]["cofactor"], 3)
        self.assertEqual(matches[0]["tail"], -2)
        self.assertEqual(
            aggregate["total_four_support_large_tail"],
            sum(item["tail"] for item in aggregate["contributions"]),
        )


if __name__ == "__main__":
    unittest.main()
