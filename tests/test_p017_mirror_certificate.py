import math
import unittest

from enterprise_math.legendre import anchor_product, is_prime, primes_up_to
from enterprise_math.p017_mirror_certificate import (
    mirror_incidence_formula,
    residue_class_count,
    surviving_radius_count_formula,
    transverse_prime_incidence_formula,
)
from enterprise_math.p017_mirror_incidence import (
    surviving_radii,
    transverse_incidence_by_prime,
    transverse_incidence_count,
)


class P017MirrorCertificateTests(unittest.TestCase):
    def test_residue_counter(self):
        self.assertEqual(residue_class_count(20, 7, 3), 3)  # 3,10,17
        self.assertEqual(residue_class_count(2, 7, 3), 0)
        self.assertEqual(residue_class_count(3, 7, 3), 1)

    def test_surviving_radius_formula_matches_gcd_enumeration(self):
        for k in range(2, 130):
            anchor = anchor_product(k)
            direct = sum(1 for r in range(1, k) if math.gcd(r, anchor) == 1)
            self.assertEqual(surviving_radius_count_formula(k), direct)
            self.assertEqual(direct, len(surviving_radii(k)))

    def test_each_transverse_prime_formula_matches_direct_count(self):
        for k in range(3, 100):
            center = k * (k + 1)
            direct = transverse_incidence_by_prime(k)
            for p in primes_up_to(k):
                if center % p == 0:
                    continue
                self.assertEqual(
                    transverse_prime_incidence_formula(k, p), direct.get(p, 0)
                )

    def test_total_formula_matches_l045_state_count(self):
        for k in range(3, 130):
            data = mirror_incidence_formula(k)
            self.assertEqual(data["incidence"], transverse_incidence_count(k))
            self.assertEqual(
                data["incidence"], sum(data["per_prime_incidence"].values())
            )
            self.assertEqual(
                data["surviving_radius_count"], len(surviving_radii(k))
            )

    def test_certificate_implies_a_basin_prime_on_bounded_domain(self):
        saw_certificate = False
        for k in range(3, 180):
            data = mirror_incidence_formula(k)
            if not data["prime_certificate"]:
                continue
            saw_certificate = True
            self.assertTrue(
                any(is_prime(n) for n in range(k * k + 1, (k + 1) * (k + 1)))
            )
        self.assertTrue(saw_certificate)

    def test_k31_is_sufficient_not_necessary_boundary(self):
        data = mirror_incidence_formula(31)
        self.assertEqual(data["surviving_radius_count"], 15)
        self.assertEqual(data["incidence"], 30)
        self.assertFalse(data["prime_certificate"])
        self.assertTrue(is_prime(967))
        self.assertTrue(31 * 31 < 967 < 32 * 32)

    def test_computational_coverage_count_through_1000(self):
        certified = sum(
            1 for k in range(3, 1001) if mirror_incidence_formula(k)["prime_certificate"]
        )
        self.assertEqual(certified, 273)


if __name__ == "__main__":
    unittest.main()
