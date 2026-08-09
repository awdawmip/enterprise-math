import unittest
from math import gcd

from enterprise_math.abc_support import (
    abc_support_state,
    exceptional_below_support_power,
    multiplicity_residual,
    radical,
    radical_addition_counterexample,
    rational_abc_bound_holds,
    rational_abc_defect,
    residual_pressure,
    witness_capacity_elimination,
)


class AbcSupportTests(unittest.TestCase):
    def test_radical_and_residual(self) -> None:
        self.assertEqual(radical(1), 1)
        self.assertEqual(radical(72), 6)
        self.assertEqual(multiplicity_residual(72), 12)
        self.assertEqual(radical(72) * multiplicity_residual(72), 72)

    def test_primitive_supports_are_disjoint(self) -> None:
        data = abc_support_state(5, 27, 32)
        supports = [set(s) for s in data["supports"]]
        self.assertFalse(supports[0] & supports[1])
        self.assertFalse(supports[0] & supports[2])
        self.assertFalse(supports[1] & supports[2])
        self.assertEqual(
            data["radical_product"] * data["residual_product"], 5 * 27 * 32
        )

    def test_radical_is_not_addition_congruence(self) -> None:
        data = radical_addition_counterexample()
        self.assertEqual(data["coarse_input"], (2, 1))
        self.assertEqual(data["coarse_outputs"], (5, 3))

    def test_exact_rational_defect_on_classic_triple(self) -> None:
        a = 2
        b = 3**10 * 109
        c = 23**5
        self.assertEqual(a + b, c)
        self.assertEqual(gcd(a, b), 1)
        self.assertEqual(radical(a * b * c), 2 * 3 * 109 * 23)
        self.assertEqual(rational_abc_defect(a, b, c, 3, 2), 13)
        self.assertFalse(rational_abc_bound_holds(a, b, c, 3, 2, 12))
        self.assertTrue(rational_abc_bound_holds(a, b, c, 3, 2, 13))

    def test_exceptional_integer_power_test(self) -> None:
        a = 2
        b = 3**10 * 109
        c = 23**5
        self.assertTrue(exceptional_below_support_power(a, b, c, 1, 4))
        self.assertFalse(exceptional_below_support_power(a, b, c, 1, 2))

    def test_residual_pressure_exhaustive_small(self) -> None:
        for c in range(3, 120):
            for a in range(1, c):
                b = c - a
                if gcd(a, b) != 1:
                    continue
                for u, v in ((2, 1), (3, 2), (4, 3)):
                    data = residual_pressure(a, b, c, u, v)
                    if data["high_quality"]:
                        self.assertGreater(
                            data["residual_product_power"], data["threshold"]
                        )
                        self.assertGreater(
                            data["max_residual"] ** (3 * u), data["threshold"]
                        )

    def test_witness_capacity_elimination(self) -> None:
        # D=(4+3+5)-7=5, and 5<=6=4+3-1; hence 5+1<=7.
        self.assertTrue(witness_capacity_elimination(4, 3, 5, 7, 5))
        # If the supplied witness is too small, the schema correctly does not fire.
        self.assertFalse(witness_capacity_elimination(4, 3, 5, 7, 4))

    def test_invalid_abc_input(self) -> None:
        with self.assertRaises(ValueError):
            abc_support_state(2, 2, 4)


if __name__ == "__main__":
    unittest.main()
