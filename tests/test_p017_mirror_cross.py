import math
import unittest

from enterprise_math.cutoff_pairing import transverse_prime_support
from enterprise_math.legendre import anchor_product, is_prime, primes_up_to
from enterprise_math.p017_mirror import mirror_pair
from enterprise_math.p017_mirror_cross import (
    cross_side_incidence_formula,
    ordered_cross_incidence_formula,
    two_moment_certificate,
)
from enterprise_math.p017_mirror_incidence import surviving_radii


def _direct_moments(k: int) -> tuple[int, int, int]:
    center = k * (k + 1)
    anchor = anchor_product(k)
    surviving = 0
    first = 0
    cross = 0
    for r in range(1, k):
        if math.gcd(r, anchor) != 1:
            continue
        surviving += 1
        lower = center - r
        upper = center + r
        lower_support = transverse_prime_support(lower, k, anchor)
        upper_support = transverse_prime_support(upper, k, anchor)
        first += len(lower_support) + len(upper_support)
        cross += len(lower_support) * len(upper_support)
    return surviving, first, cross


class P017MirrorCrossTests(unittest.TestCase):
    def test_ordered_pair_formula_matches_direct_enumeration(self):
        for k in range(5, 60):
            center = k * (k + 1)
            trans = [p for p in primes_up_to(k) if center % p != 0]
            radii = surviving_radii(k)
            for p in trans:
                for q in trans:
                    if p == q:
                        continue
                    direct = sum(
                        1
                        for r in radii
                        if (center - r) % p == 0 and (center + r) % q == 0
                    )
                    self.assertEqual(ordered_cross_incidence_formula(k, p, q), direct)

    def test_cross_side_sum_matches_direct_support_products(self):
        for k in range(5, 90):
            surviving, _first, direct_cross = _direct_moments(k)
            data = cross_side_incidence_formula(k)
            self.assertEqual(data["surviving_radius_count"], surviving)
            self.assertEqual(data["cross_incidence"], direct_cross)
            self.assertEqual(
                data["cross_incidence"], sum(data["per_ordered_pair"].values())
            )

    def test_cross_certificate_implies_prime_on_bounded_domain(self):
        saw = False
        for k in range(5, 130):
            data = cross_side_incidence_formula(k)
            if not data["cross_prime_certificate"]:
                continue
            saw = True
            self.assertTrue(
                any(is_prime(n) for n in range(k * k + 1, (k + 1) * (k + 1)))
            )
        self.assertTrue(saw)

    def test_k46_is_cross_only_example(self):
        data = two_moment_certificate(46)
        self.assertEqual(data["surviving_radius_count"], 22)
        self.assertEqual(data["first_incidence"], 47)
        self.assertEqual(data["cross_incidence"], 18)
        self.assertFalse(data["first_certificate"])
        self.assertTrue(data["cross_certificate"])
        self.assertTrue(data["combined_certificate"])
        self.assertTrue(is_prime(2129))

    def test_k37_is_first_only_example(self):
        data = two_moment_certificate(37)
        self.assertEqual(data["surviving_radius_count"], 17)
        self.assertEqual(data["first_incidence"], 33)
        self.assertEqual(data["cross_incidence"], 18)
        self.assertTrue(data["first_certificate"])
        self.assertFalse(data["cross_certificate"])
        self.assertTrue(data["combined_certificate"])

    def test_bounded_coverage_statistics_through_1000(self):
        first = 0
        cross = 0
        both = 0
        union = 0
        for k in range(3, 1001):
            surviving, first_incidence, cross_incidence = _direct_moments(k)
            first_ok = first_incidence < 2 * surviving
            cross_ok = cross_incidence < surviving
            first += int(first_ok)
            cross += int(cross_ok)
            both += int(first_ok and cross_ok)
            union += int(first_ok or cross_ok)
        self.assertEqual(first, 273)
        self.assertEqual(cross, 323)
        self.assertEqual(both, 269)
        self.assertEqual(cross - both, 54)
        self.assertEqual(first - both, 4)
        self.assertEqual(union, 327)


if __name__ == "__main__":
    unittest.main()
