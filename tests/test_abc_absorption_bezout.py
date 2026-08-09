import unittest

from enterprise_math.abc_absorption_access import absorption_optimal_radius
from enterprise_math.abc_absorption_bezout import (
    bezout_absorption_certificate,
    bezout_access_overhead,
    bezout_coefficients,
)
from enterprise_math.abc_absorption_rank2 import rank_two_absorption_optimum


class AbcAbsorptionBezoutTests(unittest.TestCase):
    def test_multi_integer_bezout_coefficients(self) -> None:
        gcd_value, coefficients = bezout_coefficients((5, -3, 2))
        self.assertEqual(gcd_value, 1)
        self.assertEqual(sum(v * z for v, z in zip((5, -3, 2), coefficients)), 1)

    def test_235_certificate_hits_floor_at_optimal_radius(self) -> None:
        certificate = bezout_absorption_certificate(2, 3, 5)
        self.assertEqual(certificate.image_generator, 1)
        self.assertEqual(certificate.absorption_redundancy, 1)
        self.assertEqual(certificate.radius, 2)
        self.assertEqual(rank_two_absorption_optimum(2, 3, 5).radius, 2)

    def test_279_certificate_hits_floor_at_optimal_radius(self) -> None:
        certificate = bezout_absorption_certificate(2, 7, 9)
        self.assertEqual(certificate.minors, (-42, 9, -12))
        self.assertEqual(certificate.image_generator, 3)
        self.assertEqual(certificate.absorption_redundancy, 1)
        self.assertEqual(certificate.witness, (1, 1, 5))
        self.assertEqual(certificate.radius, 5)
        self.assertEqual(rank_two_absorption_optimum(2, 7, 9).radius, 5)

    def test_naive_bezout_certificate_can_be_far_from_norm_optimal(self) -> None:
        certificate = bezout_absorption_certificate(1, 242, 243)
        self.assertEqual(certificate.minors, (49005, -17820))
        self.assertEqual(certificate.image_generator, 4455)
        self.assertEqual(certificate.absorption_redundancy, 5)
        self.assertEqual(certificate.witness, (-405, 11, 1215))
        self.assertEqual(certificate.radius, 1215)

        # The exact three-coordinate affine-line solver reaches the same floor at 27.
        optimal = rank_two_absorption_optimum(1, 242, 243).radius
        self.assertEqual(optimal, 27)
        overhead = bezout_access_overhead(1, 242, 243, optimal_radius=optimal)
        self.assertEqual(overhead["absolute_overhead"], 1188)

    def test_rank_one_certificate_is_necessarily_optimal(self) -> None:
        certificate = bezout_absorption_certificate(1, 8, 9)
        self.assertEqual(certificate.absorption_redundancy, 1)
        self.assertEqual(certificate.radius, 2)
        self.assertEqual(absorption_optimal_radius(1, 8, 9), 2)


if __name__ == "__main__":
    unittest.main()
