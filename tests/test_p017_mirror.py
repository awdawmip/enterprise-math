import math
import unittest

from enterprise_math.legendre import anchor_product, is_prime
from enterprise_math.p017_mirror import (
    anchor_pair_gcds,
    anchor_surviving_radius,
    mirror_basin_partition,
    mirror_center,
    mirror_pair,
    mirror_transverse_supports,
    surviving_mirror_triple,
)
from enterprise_math.p017_mirror_incidence import (
    double_composite_resource_certificate,
    double_composite_surviving_radii,
    mirror_counterexample_capacity,
    surviving_radii,
    transverse_incidence_by_prime,
    transverse_incidence_count,
)


class P017MirrorSeparationTests(unittest.TestCase):
    def test_centered_partition_is_exact(self):
        for k in range(2, 70):
            data = mirror_basin_partition(k)
            self.assertEqual(len(data["pairs"]), k - 1)
            self.assertEqual(data["unpaired"], [k * (k + 1), k * (k + 2)])
            self.assertFalse(is_prime(data["unpaired"][0]))
            self.assertFalse(is_prime(data["unpaired"][1]))

    def test_l042_anchor_survival_is_pairwise(self):
        for k in range(2, 80):
            anchor = anchor_product(k)
            for r in range(1, k):
                lower, upper = mirror_pair(k, r)
                data = anchor_pair_gcds(k, r)
                self.assertEqual(data["radius_gcd"], math.gcd(r, anchor))
                self.assertEqual(data["lower_gcd"], math.gcd(lower, anchor))
                self.assertEqual(data["upper_gcd"], math.gcd(upper, anchor))
                self.assertEqual(data["survives"], math.gcd(r, anchor) == 1)
                self.assertEqual(anchor_surviving_radius(k, r), data["survives"])

    def test_l043_transverse_supports_are_disjoint(self):
        for k in range(3, 100):
            for r in range(1, k):
                lower_support, upper_support = mirror_transverse_supports(k, r)
                self.assertTrue(set(lower_support).isdisjoint(upper_support))

    def test_surviving_mirror_triples_are_pairwise_coprime(self):
        for k in range(3, 90):
            for r in surviving_radii(k):
                triple = surviving_mirror_triple(k, r)
                self.assertEqual(math.gcd(triple["lower"], triple["center"]), 1)
                self.assertEqual(math.gcd(triple["center"], triple["upper"]), 1)
                self.assertEqual(math.gcd(triple["lower"], triple["upper"]), 1)

    def test_l044_double_composite_pairs_use_two_resources(self):
        saw_example = False
        for k in range(3, 90):
            for r in double_composite_surviving_radii(k):
                data = double_composite_resource_certificate(k, r)
                self.assertTrue(data["lower_support"])
                self.assertTrue(data["upper_support"])
                self.assertTrue(
                    set(data["lower_support"]).isdisjoint(data["upper_support"])
                )
                self.assertGreaterEqual(data["distinct_resources"], 2)
                if k == 20 and r == 17:
                    saw_example = True
                    self.assertEqual(data["lower"], 403)
                    self.assertEqual(data["upper"], 437)
                    self.assertEqual(data["lower_support"], [13])
                    self.assertEqual(data["upper_support"], [19])
        self.assertTrue(saw_example)

    def test_l045_state_and_prime_incidence_counts_agree(self):
        for k in range(3, 80):
            state_total = transverse_incidence_count(k)
            prime_total = sum(transverse_incidence_by_prime(k).values())
            self.assertEqual(state_total, prime_total)

    def test_l045_hypothetical_failure_bound(self):
        for k in range(3, 80):
            data = mirror_counterexample_capacity(k)
            if data["all_mirror_composite"]:
                self.assertTrue(data["necessary_bound_holds"])
                self.assertGreaterEqual(
                    data["transverse_incidence"], data["hypothetical_required_minimum"]
                )

    def test_known_pair(self):
        self.assertEqual(mirror_center(20), 420)
        self.assertEqual(mirror_pair(20, 17), (403, 437))
        self.assertTrue(anchor_surviving_radius(20, 17))
        self.assertEqual(mirror_transverse_supports(20, 17), ([13], [19]))


if __name__ == "__main__":
    unittest.main()
