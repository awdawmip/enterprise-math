import math
import unittest

from enterprise_math.abc_witness_precision import minimal_witness_cost, witness_coordinates
from enterprise_math.witness_precision_layers import minimal_additive_radius, witness_precision_layer_profile
from enterprise_math.witness_support_dimension import two_coordinate_witness_radius


class WitnessSupportDimensionTests(unittest.TestCase):
    def test_one_plus_seven_is_pure_additive_lattice_cost(self) -> None:
        profile = two_coordinate_witness_radius(1, 7, 8)
        self.assertEqual(profile["coordinates"], (2, 7))
        self.assertEqual(profile["alpha"], (12, -1))
        self.assertEqual((profile["rho"], profile["mu"], profile["U2"]), (12, 12, 12))
        self.assertEqual(profile["nondegeneracy_overhead_over_rho"], 0)

    def test_one_plus_two(self) -> None:
        profile = two_coordinate_witness_radius(1, 2, 3)
        self.assertEqual((profile["rho"], profile["mu"], profile["U2"]), (1, 1, 1))

    def test_two_coordinate_formula_matches_exact_oracles(self) -> None:
        checked = 0
        for c in range(3, 80):
            for a in range(1, c):
                b = c - a
                if math.gcd(a, b) != 1:
                    continue
                if len(witness_coordinates(a, b, c)) != 2:
                    continue
                try:
                    profile = two_coordinate_witness_radius(a, b, c)
                except ValueError:
                    continue
                if profile["mu"] > 16:
                    continue
                self.assertEqual(minimal_additive_radius(a, b, c, max_bound=16), profile["rho"])
                self.assertEqual(minimal_witness_cost(a, b, c, max_bound=16), profile["mu"])
                checked += 1
        self.assertGreater(checked, 50)

    def test_positive_degeneracy_overhead_first_appears_beyond_two_coordinates(self) -> None:
        profile = witness_precision_layer_profile(1, 53, 54, max_bound=27)
        self.assertEqual(len(witness_coordinates(1, 53, 54)), 3)
        self.assertEqual(profile["rho"], 2)
        self.assertEqual(profile["mu"], 27)
        self.assertGreater(profile["nondegeneracy_overhead"], 0)

    def test_rejects_wrong_support_dimension(self) -> None:
        with self.assertRaises(ValueError):
            two_coordinate_witness_radius(1, 53, 54)


if __name__ == "__main__":
    unittest.main()
