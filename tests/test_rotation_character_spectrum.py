import unittest
from decimal import Decimal
from fractions import Fraction

from enterprise_math.rotation_character_spectrum import (
    certificate,
    rotation_spectrum_data,
    verify_rotation_spectrum,
)


class RotationCharacterSpectrumTests(unittest.TestCase):
    def test_first_phase_step(self):
        first = rotation_spectrum_data(1, precision=100)[0]
        self.assertEqual(first.level, 1)
        self.assertEqual(first.phase_step, Fraction(1, 4))
        self.assertEqual(first.precision_readout, Decimal(2))
        self.assertEqual(first.skew_eigenvalue_magnitude, Decimal(4))

    def test_skew_eigenvalue_is_twice_precision_readout(self):
        for item in rotation_spectrum_data(20, precision=120):
            self.assertEqual(
                item.skew_eigenvalue_magnitude,
                Decimal(2) * item.precision_readout,
            )

    def test_laplacian_eigenvalue_is_next_precision_square(self):
        tolerance = Decimal("1e-90")
        for item in rotation_spectrum_data(20, precision=120):
            expected = Decimal(4) * item.next_precision_readout**2
            self.assertLess(abs(item.positive_laplacian_eigenvalue - expected), tolerance)

    def test_first_second_spectrum_relation(self):
        tolerance = Decimal("1e-90")
        for item in rotation_spectrum_data(20, precision=120):
            left = item.skew_eigenvalue_magnitude**2
            right = (
                (Decimal(1) + item.half_trace)
                / Decimal(2)
                * item.positive_laplacian_eigenvalue
            )
            self.assertLess(abs(left - right), tolerance)

    def test_verified_certificate(self):
        self.assertTrue(verify_rotation_spectrum(24, precision=120))
        payload = certificate(12, precision=100)
        self.assertTrue(payload["verified"])
        self.assertEqual(len(payload["levels"]), 12)


if __name__ == "__main__":
    unittest.main()
