import unittest

from enterprise_math.prime_cubic_certificate_resources import (
    combined_resource_k_max,
    coverage_required_to_match_delta,
    effective_delta_required_for_k,
    horizontal_coverage_required_for_k,
    horizontal_database_k_max,
    vertical_effective_k_max,
)


class PrimeCubicCertificateResourceTests(unittest.TestCase):
    def test_vertical_endpoint_is_exact(self):
        for delta in range(2, 200):
            k = vertical_effective_k_max(delta)
            self.assertGreater(3 * (k + 1) * (delta - 1) - k * k, 0)
            self.assertEqual(3 * (k + 2) * (delta - 1) - (k + 1) ** 2, -1)

    def test_horizontal_endpoint_is_exact(self):
        for x in range(1, 5000):
            k = horizontal_database_k_max(x)
            self.assertLess(k * k - k, x)
            self.assertGreaterEqual((k + 1) ** 2 - (k + 1), x)

    def test_inverse_resource_compilers(self):
        for k in range(1, 500):
            x = horizontal_coverage_required_for_k(k)
            self.assertGreaterEqual(horizontal_database_k_max(x), k)
            if x > 1:
                self.assertLess(horizontal_database_k_max(x - 1), k)

            delta = effective_delta_required_for_k(k)
            self.assertGreaterEqual(vertical_effective_k_max(delta), k)
            if delta > 2:
                self.assertLess(vertical_effective_k_max(delta - 1), k)

    def test_current_corrected_chl_resource_is_horizontal_limited(self):
        delta = 76_918_400_000
        x = 10**20
        self.assertEqual(vertical_effective_k_max(delta), 230_755_199_997)
        self.assertEqual(horizontal_database_k_max(x), 10_000_000_000)
        self.assertEqual(combined_resource_k_max(delta, x), 10_000_000_000)
        self.assertEqual(
            coverage_required_to_match_delta(delta),
            53_247_962_325_424_713_600_013,
        )
        self.assertEqual(effective_delta_required_for_k(10_000_000_000), 3_333_333_335)


if __name__ == "__main__":
    unittest.main()
