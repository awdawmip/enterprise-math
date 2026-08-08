import math
import unittest

from enterprise_math.legendre import anchor_product, is_prime, primes_up_to, square_basin
from enterprise_math.mirror import (
    anchor_surviving_radius,
    mirror_basin_partition,
    mirror_center,
    mirror_pair,
    mirror_transverse_supports,
)
from enterprise_math.mirror_incidence import (
    double_composite_surviving_radii,
    mirror_counterexample_capacity,
    surviving_radii,
    transverse_incidence_count,
    transverse_incidence_count_by_prime,
)


class MirrorSeparationTests(unittest.TestCase):
    def test_centered_partition_is_exact(self) -> None:
        for k in range(2, 100):
            data = mirror_basin_partition(k)
            reconstructed = [n for pair in data["pairs"] for n in pair] + data["unpaired"]
            self.assertEqual(sorted(reconstructed), square_basin(k))
            center = mirror_center(k)
            self.assertEqual(data["unpaired"], [center, center + k])
            self.assertFalse(is_prime(center))
            self.assertFalse(is_prime(center + k))

    def test_anchor_survival_is_pairwise(self) -> None:
        for k in range(2, 100):
            A = anchor_product(k)
            for r in range(1, k):
                lower, upper = mirror_pair(k, r)
                expected = math.gcd(r, A) == 1
                self.assertEqual(anchor_surviving_radius(k, r), expected)
                self.assertEqual(math.gcd(lower, A) == 1, expected)
                self.assertEqual(math.gcd(upper, A) == 1, expected)

    def test_transverse_supports_are_disjoint(self) -> None:
        for k in range(3, 160):
            for r in surviving_radii(k):
                lower_support, upper_support = mirror_transverse_supports(k, r)
                self.assertTrue(set(lower_support).isdisjoint(upper_support))

    def test_double_composite_survivors_need_two_distinct_resources(self) -> None:
        for k in range(3, 160):
            for r in double_composite_surviving_radii(k):
                lower_support, upper_support = mirror_transverse_supports(k, r)
                self.assertGreaterEqual(len(lower_support), 1)
                self.assertGreaterEqual(len(upper_support), 1)
                self.assertTrue(set(lower_support).isdisjoint(upper_support))

    def test_incidence_double_count(self) -> None:
        for k in range(3, 120):
            self.assertEqual(transverse_incidence_count(k), transverse_incidence_count_by_prime(k))

    def test_counterexample_necessary_bound(self) -> None:
        for k in range(3, 120):
            data = mirror_counterexample_capacity(k)
            if data["all_basin_composite"]:
                self.assertTrue(data["counterexample_necessary_bound"])
                self.assertGreaterEqual(
                    data["transverse_incidence"], 2 * data["surviving_radii"]
                )

    def test_pairwise_coprime_triple_on_surviving_radii(self) -> None:
        # This stronger fact is used by the next CRT/idempotent layer.
        for k in range(3, 140):
            center = mirror_center(k)
            for r in surviving_radii(k):
                lower, upper = mirror_pair(k, r)
                self.assertEqual(math.gcd(lower, center), 1)
                self.assertEqual(math.gcd(center, upper), 1)
                self.assertEqual(math.gcd(lower, upper), 1)

    def test_transverse_prime_hits_at_most_one_side(self) -> None:
        for k in range(3, 120):
            center = mirror_center(k)
            for p in primes_up_to(k):
                if center % p == 0:
                    continue
                for r in surviving_radii(k):
                    lower, upper = mirror_pair(k, r)
                    self.assertFalse(lower % p == 0 and upper % p == 0)


if __name__ == "__main__":
    unittest.main()
