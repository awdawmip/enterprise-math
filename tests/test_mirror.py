import unittest
from math import gcd

from enterprise_math.mirror import (
    anchor_pair_survival,
    composite_surviving_pair_certificate,
    mirror_basin_partition,
    mirror_pair,
    mirror_support_separation,
)


class MirrorTests(unittest.TestCase):
    def test_mirror_partition_covers_basin(self):
        for k in range(2, 40):
            data = mirror_basin_partition(k)
            self.assertEqual(len(data["pairs"]), k - 1)
            self.assertEqual(data["center"], k * (k + 1))
            self.assertEqual(data["top"], k * (k + 2))

    def test_anchor_survival_is_all_in_or_all_out(self):
        for k in range(3, 80):
            for r in range(1, k):
                lower, upper, _center = mirror_pair(k, r)
                data = anchor_pair_survival(k, r)
                self.assertEqual(data["lower_gcd"], data["radius_gcd"])
                self.assertEqual(data["upper_gcd"], data["radius_gcd"])
                self.assertEqual(data["survives"], data["radius_gcd"] == 1)
                self.assertEqual(
                    gcd(lower, data["anchor_product"]), data["radius_gcd"]
                )
                self.assertEqual(
                    gcd(upper, data["anchor_product"]), data["radius_gcd"]
                )

    def test_transverse_supports_are_disjoint(self):
        for k in range(3, 100):
            for r in range(1, k):
                data = mirror_support_separation(k, r)
                self.assertEqual(data["shared_support"], [])
                self.assertTrue(
                    set(data["lower_support"]).isdisjoint(data["upper_support"])
                )

    def test_explicit_surviving_composite_pair(self):
        # k=20, M=420, r=17 gives 403=13*31 and 437=19*23.
        # The anchor product is 2*3*5*7=210, so both states survive it.
        data = composite_surviving_pair_certificate(20, 17)
        self.assertEqual(data["lower"], 403)
        self.assertEqual(data["upper"], 437)
        self.assertEqual(data["lower_support"], [13])
        self.assertEqual(data["upper_support"], [19])
        self.assertGreaterEqual(data["distinct_small_prime_resources"], 2)

    def test_anchor_failure_is_symmetric(self):
        # k=58 has anchor prime 29.  r=29 makes both mirror states divisible by 29.
        data = anchor_pair_survival(58, 29)
        self.assertFalse(data["survives"])
        self.assertEqual(data["radius_gcd"] % 29, 0)


if __name__ == "__main__":
    unittest.main()
