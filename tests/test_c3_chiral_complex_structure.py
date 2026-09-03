import unittest
from fractions import Fraction

from enterprise_math.c3_chiral_complex_structure import (
    IDENTITY,
    ZERO,
    c3_chiral_certificate,
    effective_scalar_compatibility,
    matrix_add,
    matrix_mul,
    matrix_pow,
    matrix_scale,
    required_normalizer_square,
)


class C3ChiralComplexStructureTests(unittest.TestCase):
    def test_exact_integer_matrix_certificate(self):
        cert = c3_chiral_certificate()
        self.assertEqual(cert.right_turn_cube, IDENTITY)
        self.assertEqual(cert.cyclotomic_sum, ZERO)
        self.assertEqual(cert.chiral_square, matrix_scale(-3, IDENTITY))
        self.assertEqual(cert.cell_radius_squared, Fraction(1, 3))
        self.assertEqual(cert.normalized_square_coefficient, Fraction(-1, 1))

    def test_turn_inverse_and_cyclotomic_relation(self):
        cert = c3_chiral_certificate()
        self.assertEqual(matrix_mul(cert.right_turn, cert.inverse_turn), IDENTITY)
        self.assertEqual(
            matrix_add(matrix_add(IDENTITY, cert.right_turn), cert.inverse_turn),
            ZERO,
        )
        self.assertEqual(matrix_pow(cert.right_turn, 6), IDENTITY)

    def test_unique_required_scale_square(self):
        self.assertEqual(required_normalizer_square(), Fraction(1, 3))

    def test_refined_quarter_turn_realizes_coarse_chiral_operator(self):
        omega, derived_i, quarter_turn = effective_scalar_compatibility()
        self.assertAlmostEqual(derived_i.real, 0.0, places=14)
        self.assertAlmostEqual(derived_i.imag, 1.0, places=14)
        self.assertAlmostEqual(quarter_turn.real, derived_i.real, places=14)
        self.assertAlmostEqual(quarter_turn.imag, derived_i.imag, places=14)
        self.assertAlmostEqual((omega**3).real, 1.0, places=14)
        self.assertAlmostEqual((omega**3).imag, 0.0, places=14)


if __name__ == "__main__":
    unittest.main()
