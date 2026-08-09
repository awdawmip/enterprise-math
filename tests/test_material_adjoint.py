import unittest

from enterprise_math.material_adjoint import (
    ceil_hardening_sample,
    material_adjoint_law,
    material_adjoint_repair,
)
from enterprise_math.material_response import hardening_sample, softening_sample


class MaterialAdjointTests(unittest.TestCase):
    def test_scaled_power_root_adjunction_holds_exhaustively_on_small_chains(self):
        for amplitude in range(1, 25):
            for power in range(1, 5):
                for sample in range(amplitude + 1):
                    for target in range(amplitude + 1):
                        material_adjoint_law(sample, target, amplitude, power)

    def test_ceil_hardening_is_floor_hardening_plus_one_boundary_bit(self):
        saw_zero = False
        saw_one = False
        for amplitude in range(1, 30):
            for power in range(1, 5):
                for sample in range(amplitude + 1):
                    report = material_adjoint_repair(sample, amplitude, power)
                    self.assertIn(report.boundary_bit, (0, 1))
                    self.assertEqual(
                        report.ceil_hardening,
                        report.floor_hardening + report.boundary_bit,
                    )
                    self.assertEqual(report.boundary_bit, int(report.remainder != 0))
                    saw_zero |= report.boundary_bit == 0
                    saw_one |= report.boundary_bit == 1
        self.assertTrue(saw_zero)
        self.assertTrue(saw_one)

    def test_floor_hardening_itself_is_not_the_left_adjoint(self):
        # A=5,p=2,s=2,t=0: floor H(2)=0<=0, but 2<=G(0)=0 is false.
        self.assertEqual(hardening_sample(2, 5, 2), 0)
        self.assertEqual(softening_sample(0, 5, 2), 0)
        self.assertTrue(hardening_sample(2, 5, 2) <= 0)
        self.assertFalse(2 <= softening_sample(0, 5, 2))
        self.assertEqual(ceil_hardening_sample(2, 5, 2), 1)

    def test_adjunction_unit_and_counit_inequalities_are_explicit(self):
        for amplitude in range(1, 25):
            for power in range(1, 5):
                for sample in range(amplitude + 1):
                    k = ceil_hardening_sample(sample, amplitude, power)
                    self.assertGreaterEqual(
                        softening_sample(k, amplitude, power),
                        sample,
                    )
                for target in range(amplitude + 1):
                    g = softening_sample(target, amplitude, power)
                    self.assertLessEqual(
                        ceil_hardening_sample(g, amplitude, power),
                        target,
                    )


if __name__ == "__main__":
    unittest.main()
