import unittest
from fractions import Fraction

from enterprise_math.rotation_cayley_pell import (
    biquadratic_mul,
    cayley_compose,
    cayley_double,
    certificate,
    n58_cayley_pell_certificate,
    quadratic_conjugate,
    quadratic_mul,
    quadratic_norm,
    quadratic_pow,
)


class RotationCayleyPellTests(unittest.TestCase):
    def test_rational_cayley_composition(self):
        self.assertEqual(cayley_compose(Fraction(1, 2), Fraction(1, 3)), 1)
        self.assertEqual(cayley_double(Fraction(1, 3)), Fraction(3, 4))
        with self.assertRaises(ZeroDivisionError):
            cayley_compose(1, 1)

    def test_quadratic_pair_arithmetic(self):
        self.assertEqual(quadratic_mul((1, 1), (1, 1), 2), (3, 2))
        self.assertEqual(quadratic_pow((1, 1), 6, 2), (99, 70))
        self.assertEqual(quadratic_conjugate((99, 70)), (99, -70))
        self.assertEqual(quadratic_norm((99, 70), 2), 1)
        self.assertEqual(quadratic_norm((99, 13), 58), -1)

    def test_first_post_gate_defect_doubles_to_quarter_turn(self):
        defect = (-1, 1)  # sqrt(2)-1
        defect_square = quadratic_mul(defect, defect, 2)
        one_minus_square = (1 - defect_square[0], -defect_square[1])
        twice_defect = (2 * defect[0], 2 * defect[1])
        self.assertEqual(one_minus_square, twice_defect)
        self.assertEqual(quadratic_pow(defect, 6, 2), (99, -70))

    def test_n58_inverse_units(self):
        self.assertEqual(quadratic_mul((99, -70), (99, 70), 2), (1, 0))
        self.assertEqual(quadratic_mul((-99, 13), (99, 13), 58), (1, 0))

    def test_biquadratic_lambda_star_inverse_product(self):
        small = biquadratic_mul((99, -70, 0, 0), (-99, 0, 13, 0), 2, 58)
        large = biquadratic_mul((99, 70, 0, 0), (99, 0, 13, 0), 2, 58)
        self.assertEqual(small, (-9801, 6930, 1287, -910))
        self.assertEqual(large, (9801, 6930, 1287, 910))
        self.assertEqual(biquadratic_mul(small, large, 2, 58), (1, 0, 0, 0))

    def test_full_n58_cayley_pell_certificate(self):
        result = n58_cayley_pell_certificate()
        self.assertTrue(result.valid)
        self.assertEqual(result.paired_pell.P, 99)
        self.assertEqual(result.first_post_gate_defect_sixth_sqrt2, (99, -70))
        self.assertEqual(result.negative_pell_inverse_sqrt58, (-99, 13))

    def test_serializable_certificate(self):
        payload = certificate()
        self.assertTrue(payload["valid"])
        self.assertEqual(payload["cayley_rational_example"], "1")
        self.assertIn("external analytic input", payload["boundary"])


if __name__ == "__main__":
    unittest.main()
