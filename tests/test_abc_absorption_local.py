import math
import unittest

from enterprise_math.abc_absorption_formula import (
    minimum_absorption_redundancy_support_formula,
)
from enterprise_math.abc_absorption_local import (
    absorption_obstruction_spectrum,
    high_quality_absorption_counterexample,
    local_absorption_valuation,
    perfect_absorption_local_criterion,
)
from enterprise_math.abc_support import radical


class AbcAbsorptionLocalTests(unittest.TestCase):
    def test_known_local_spectra(self) -> None:
        self.assertEqual(absorption_obstruction_spectrum(1, 8, 9), ())
        self.assertEqual(absorption_obstruction_spectrum(1, 3, 4), ((2, 1),))
        self.assertEqual(absorption_obstruction_spectrum(1, 512, 513), ((3, 1),))
        self.assertEqual(absorption_obstruction_spectrum(25, 704, 729), ((2, 1), (3, 1)))

    def test_local_valuations_reconstruct_eta(self) -> None:
        for triple in ((1, 7, 8), (1, 15, 16), (5, 27, 32), (5, 7, 12), (2, 7, 9)):
            eta = minimum_absorption_redundancy_support_formula(*triple)
            reconstructed = 1
            for prime, exponent in absorption_obstruction_spectrum(*triple):
                reconstructed *= prime**exponent
            self.assertEqual(reconstructed, eta)

    def test_perfect_absorption_local_criterion(self) -> None:
        self.assertTrue(perfect_absorption_local_criterion(2, 3, 5))
        self.assertTrue(perfect_absorption_local_criterion(1, 4374, 4375))
        self.assertFalse(perfect_absorption_local_criterion(1, 3, 4))
        self.assertFalse(perfect_absorption_local_criterion(1, 512, 513))

    def test_high_quality_counterexample(self) -> None:
        data = high_quality_absorption_counterexample()
        self.assertEqual((data["a"], data["b"], data["c"]), (1, 512, 513))
        self.assertEqual(data["radical"], 114)
        self.assertEqual(data["eta_min"], 3)
        self.assertTrue(data["quality_gt_5_over_4"])
        self.assertEqual(data["obstruction_spectrum"], ((3, 1),))
        self.assertGreater(513**4, 114**5)

    def test_exponent_only_high_quality_obstruction(self) -> None:
        self.assertEqual(radical(1 * 242 * 243), 66)
        self.assertEqual(minimum_absorption_redundancy_support_formula(1, 242, 243), 5)
        self.assertEqual(absorption_obstruction_spectrum(1, 242, 243), ((5, 1),))
        self.assertGreater(243**10, 66**13)

    def test_small_falsification_scan_finds_quality_obstructions(self) -> None:
        found = []
        for c in range(3, 100):
            for a in range(1, c // 2 + 1):
                b = c - a
                if math.gcd(a, b) != 1:
                    continue
                try:
                    eta = minimum_absorption_redundancy_support_formula(a, b, c)
                except ValueError:
                    continue
                R = radical(a * b * c)
                if c > R and eta > 1:
                    found.append((a, b, c, R, eta))
        self.assertIn((1, 80, 81, 30, 2), found)
        self.assertIn((5, 27, 32, 30, 3), found)

    def test_single_local_valuation(self) -> None:
        self.assertEqual(local_absorption_valuation(1, 512, 513, 3), 1)
        self.assertEqual(local_absorption_valuation(1, 512, 513, 19), 0)
        self.assertEqual(local_absorption_valuation(1, 242, 243, 5), 1)


if __name__ == "__main__":
    unittest.main()
