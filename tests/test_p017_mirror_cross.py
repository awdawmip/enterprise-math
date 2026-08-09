import math
import unittest

from enterprise_math.cutoff_pairing import transverse_prime_support
from enterprise_math.legendre import anchor_product, is_prime, primes_up_to
from enterprise_math.p017_mirror_cross import (
    cross_side_incidence_formula,
    ordered_cross_incidence_formula,
    two_slack_certificate,
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
        lower_support = transverse_prime_support(center - r, k, anchor)
        upper_support = transverse_prime_support(center + r, k, anchor)
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

    def test_cross_sum_and_factorized_slacks_are_exact(self):
        for k in range(5, 100):
            surviving, first, cross = _direct_moments(k)
            data = cross_side_incidence_formula(k)
            self.assertEqual(data["surviving_radius_count"], surviving)
            self.assertEqual(data["first_incidence"], first)
            self.assertEqual(data["cross_incidence"], cross)
            self.assertEqual(
                data["cross_incidence"], sum(data["per_ordered_pair"].values())
            )
            self.assertEqual(data["first_slack"], first - 2 * surviving)
            self.assertEqual(
                data["simultaneous_excess_slack"], cross - first + surviving
            )
            self.assertEqual(data["raw_cross_slack"], cross - surviving)
            self.assertEqual(
                data["raw_cross_slack"],
                data["first_slack"] + data["simultaneous_excess_slack"],
            )

    def test_factorized_certificate_implies_prime_on_bounded_domain(self):
        saw = False
        for k in range(5, 160):
            data = two_slack_certificate(k)
            if not data["factorized_certificate"]:
                continue
            saw = True
            self.assertTrue(
                any(is_prime(n) for n in range(k * k + 1, (k + 1) * (k + 1)))
            )
        self.assertTrue(saw)

    def test_k37_is_first_slack_only_example(self):
        data = two_slack_certificate(37)
        self.assertEqual(data["surviving_radius_count"], 17)
        self.assertEqual(data["first_incidence"], 33)
        self.assertEqual(data["cross_incidence"], 18)
        self.assertEqual(data["first_slack"], -1)
        self.assertEqual(data["simultaneous_excess_slack"], 2)
        self.assertTrue(data["first_channel_certificate"])
        self.assertFalse(data["simultaneous_excess_certificate"])

    def test_k46_is_simultaneous_excess_only_example(self):
        data = two_slack_certificate(46)
        self.assertEqual(data["surviving_radius_count"], 22)
        self.assertEqual(data["first_incidence"], 47)
        self.assertEqual(data["cross_incidence"], 18)
        self.assertEqual(data["first_slack"], 3)
        self.assertEqual(data["simultaneous_excess_slack"], -7)
        self.assertFalse(data["first_channel_certificate"])
        self.assertTrue(data["simultaneous_excess_certificate"])
        self.assertTrue(is_prime(2129))

    def test_k31_is_noncharacterization_boundary(self):
        data = two_slack_certificate(31)
        self.assertEqual(data["surviving_radius_count"], 15)
        self.assertEqual(data["first_incidence"], 30)
        self.assertEqual(data["cross_incidence"], 15)
        self.assertEqual(data["first_slack"], 0)
        self.assertEqual(data["simultaneous_excess_slack"], 0)
        self.assertFalse(data["factorized_certificate"])
        self.assertTrue(is_prime(967))

    def test_factorized_certificate_strictly_dominates_raw_cross_certificate(self):
        for k in range(3, 400):
            data = two_slack_certificate(k)
            raw_cross = data["raw_cross_slack"] < 0
            if raw_cross:
                self.assertTrue(data["factorized_certificate"])

    def test_bounded_coverage_statistics_through_1000(self):
        u_negative = 0
        v_negative = 0
        both_negative = 0
        factorized_union = 0
        raw_cross = 0
        for k in range(3, 1001):
            surviving, first, cross = _direct_moments(k)
            u = first - 2 * surviving
            v = cross - first + surviving
            u_negative += int(u < 0)
            v_negative += int(v < 0)
            both_negative += int(u < 0 and v < 0)
            factorized_union += int(u < 0 or v < 0)
            raw_cross += int(cross < surviving)
        self.assertEqual(u_negative, 273)
        self.assertEqual(v_negative, 594)
        self.assertEqual(both_negative, 140)
        self.assertEqual(factorized_union, 727)
        self.assertEqual(raw_cross, 323)


if __name__ == "__main__":
    unittest.main()
