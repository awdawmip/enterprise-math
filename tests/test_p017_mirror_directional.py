import unittest

from enterprise_math.p017_mirror_cross import aggregate_mirror_certificate
from enterprise_math.p017_mirror_directional import (
    directional_first_moments,
    directional_mirror_certificate,
    directional_prime_incidence_formula,
)


class P017MirrorDirectionalTests(unittest.TestCase):
    def test_directional_moments_sum_to_canonical_first_moment(self):
        for k in range(3, 120):
            directional = directional_first_moments(k)
            canonical = aggregate_mirror_certificate(k)
            self.assertEqual(directional["total_incidence"], canonical["first_incidence"])

    def test_per_prime_directional_counts_are_nonnegative(self):
        for k in (11, 31, 47, 83):
            center = k * (k + 1)
            for p in range(2, k + 1):
                try:
                    data = directional_prime_incidence_formula(k, p)
                except ValueError:
                    continue
                self.assertNotEqual(center % p, 0)
                self.assertGreaterEqual(data["lower"], 0)
                self.assertGreaterEqual(data["upper"], 0)

    def test_directional_certificate_subsumes_mc06_on_bounded_range(self):
        for k in range(3, 120):
            data = directional_mirror_certificate(k)
            if data["mc06_certificate"]:
                self.assertTrue(data["directional_certificate"], msg=f"k={k}")

    def test_fixed_directional_only_witnesses(self):
        witnesses = (137, 171, 233, 293, 336, 470, 570)
        for k in witnesses:
            data = directional_mirror_certificate(k)
            self.assertTrue(data["directional_certificate"], msg=f"k={k}")
            self.assertFalse(data["mc06_certificate"], msg=f"k={k}")

    def test_side_deficit_example(self):
        data = directional_mirror_certificate(137)
        self.assertEqual(data["surviving_radius_count"], 43)
        self.assertEqual((data["lower_incidence"], data["upper_incidence"]), (45, 41))
        self.assertTrue(data["upper_channel_certificate"])

    def test_product_only_example(self):
        data = directional_mirror_certificate(233)
        self.assertEqual((data["lower_slack"], data["upper_slack"]), (0, 4))
        self.assertEqual(data["simultaneous_excess_slack"], 1)
        self.assertTrue(data["product_violation_certificate"])
        self.assertFalse(data["mc06_certificate"])

    def test_non_witness_boundary(self):
        data = directional_mirror_certificate(31)
        self.assertEqual((data["lower_slack"], data["upper_slack"]), (0, 0))
        self.assertEqual(data["simultaneous_excess_slack"], 0)
        self.assertFalse(data["directional_certificate"])

    def test_validation(self):
        with self.assertRaises(ValueError):
            directional_mirror_certificate(1)
        with self.assertRaises(ValueError):
            directional_prime_incidence_formula(11, 4)


if __name__ == "__main__":
    unittest.main()
