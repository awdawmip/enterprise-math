import unittest

from enterprise_math.abc_absorption_repunit import (
    base3_repunit_prime_access,
    repunit_access_closed_radius,
)


class AbcAbsorptionRepunitTests(unittest.TestCase):
    def test_exponent_3(self) -> None:
        data = base3_repunit_prime_access(3)
        self.assertEqual(data["repunit_prime"], 13)
        self.assertEqual(data["eta_min"], 3)
        self.assertEqual(data["witness_2_r_3"], (3, -6, 1))
        self.assertEqual(data["nu"], 6)

    def test_exponent_7(self) -> None:
        data = base3_repunit_prime_access(7)
        self.assertEqual(data["repunit_prime"], 1093)
        self.assertEqual(data["witness_2_r_3"], (5, -181, 1))
        self.assertEqual(data["nu"], 181)
        self.assertEqual(repunit_access_closed_radius(7), 181)

    def test_exponent_13(self) -> None:
        data = base3_repunit_prime_access(13)
        self.assertEqual(data["repunit_prime"], 797161)
        self.assertEqual(data["witness_2_r_3"], (9, -132858, 1))
        self.assertEqual(data["nu"], 132858)

    def test_composite_repunit_rejected(self) -> None:
        with self.assertRaises(ValueError):
            base3_repunit_prime_access(5)


if __name__ == "__main__":
    unittest.main()
