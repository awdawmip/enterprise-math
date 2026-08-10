import unittest

from enterprise_math.p017_factor_root_spectrum import (
    factor_root_relative_spectrum,
    factor_root_split_shell_primes,
    split_shell_threshold_criterion,
)


class P017FactorRootSpectrumTests(unittest.TestCase):
    def test_l067_examples(self) -> None:
        data11 = factor_root_relative_spectrum(11)
        self.assertEqual(data11["factor_shell_count"], 5)
        self.assertEqual(data11["split_shell_count"], 1)
        self.assertEqual(data11["joint_class_count"], 6)
        self.assertEqual(data11["relative_repair_spectrum"], (6, 1))

        data18 = factor_root_relative_spectrum(18)
        self.assertEqual(data18["factor_shell_count"], 5)
        self.assertEqual(data18["split_shell_primes"], (2, 7))
        self.assertEqual(data18["joint_class_count"], 7)
        self.assertEqual(data18["relative_repair_spectrum"], (7, 2))

        data1737 = factor_root_relative_spectrum(1737)
        self.assertEqual(data1737["factor_shell_count"], 157)
        self.assertEqual(data1737["split_shell_count"], 7)
        self.assertEqual(data1737["joint_class_count"], 164)
        self.assertEqual(data1737["unused_product_codes"], 150)

    def test_threshold_criterion_matches_direct_split_profile(self) -> None:
        for k in range(3, 200):
            split = set(factor_root_split_shell_primes(k))
            data = factor_root_relative_spectrum(k)
            self.assertEqual(len(split), data["split_shell_count"])
            # The executable module already checks every active shell internally.

    def test_higher_repair_spectrum_truncates_after_order_two(self) -> None:
        for k in range(3, 100):
            data = factor_root_relative_spectrum(k)
            coeffs = data["repair_polynomial_coefficients"]
            self.assertEqual(len(coeffs), 3)
            self.assertEqual(coeffs[0], 0)

    def test_unused_uniform_binary_codes_are_exactly_unsplit_shells(self) -> None:
        for k in range(3, 200):
            data = factor_root_relative_spectrum(k)
            if data["repair_factor"] == 2:
                self.assertEqual(
                    data["unused_product_codes"],
                    data["factor_shell_count"] - data["split_shell_count"],
                )
            else:
                self.assertEqual(data["unused_product_codes"], 0)


if __name__ == "__main__":
    unittest.main()
