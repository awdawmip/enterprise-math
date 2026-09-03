import inspect
import unittest
from fractions import Fraction

from enterprise_math import euler_cayley_spinor as ecs


class EulerCayleySpinorTests(unittest.TestCase):
    def test_pythagorean_character(self):
        for pair in ((1, 0), (1, 1), (2, 1), (5, 2), (12, 5), (70, 1), (99, 1)):
            x, y, r = ecs.rotation_triple(pair)
            self.assertEqual(x * x + y * y, r * r)
            self.assertEqual(ecs.character_norm_squared(ecs.rotation_character(pair)), 1)

    def test_projective_invariance(self):
        self.assertEqual(ecs.rotation_character((5, 2)), ecs.rotation_character((15, 6)))
        self.assertEqual(ecs.rotation_character((5, 2)), ecs.rotation_character((-5, -2)))

    def test_exact_composition(self):
        samples = ((2, 1), (3, -1), (5, 2), (7, 3))
        for left in samples:
            for right in samples:
                self.assertEqual(*ecs.compose_certificate(left, right))

    def test_rational_unit_circle_inverse(self):
        for pair in ((1, 0), (1, 1), (2, 1), (3, 2), (0, 1), (5, -3)):
            point = ecs.rotation_character(pair)
            recovered = ecs.spinor_from_rational_character(*point)
            self.assertEqual(ecs.rotation_character(recovered), point)

    def test_identity_quarter_half_turn(self):
        self.assertEqual(ecs.rotation_character((1, 0)), (Fraction(1), Fraction(0)))
        self.assertEqual(ecs.rotation_character((1, 1)), (Fraction(0), Fraction(1)))
        self.assertEqual(ecs.rotation_character((0, 1)), (Fraction(-1), Fraction(0)))
        self.assertTrue(ecs.verify_quarter_turn_certificate())

    def test_cayley_composition_law(self):
        values = (Fraction(0), Fraction(1, 5), Fraction(-1, 7), Fraction(2, 3), None)
        for left in values:
            for right in values:
                composed = ecs.cayley_compose(left, right)
                self.assertEqual(
                    ecs.cayley_character(composed),
                    ecs.character_product(
                        ecs.cayley_character(left), ecs.cayley_character(right)
                    ),
                )

    def test_negative_pell_segments(self):
        for p, q, d in ((1, 1, 2), (70, 13, 29), (99, 13, 58)):
            certificate = ecs.pell_cayley_certificate(p, q, d)
            self.assertTrue(certificate.valid)
            defect = ecs.pell_defect_decimal(p, q, d, precision=80)
            self.assertGreater(defect, 0)
            self.assertLess(defect, 1)

    def test_machin_is_integer_spinor_composition(self):
        self.assertEqual(*ecs.machin_spinor_certificate())

    def test_exact_cayley_euler_approximants_stay_on_unit_circle(self):
        for theta in (Fraction(1), Fraction(3, 2), Fraction(-7, 5)):
            for steps in (1, 2, 5, 16):
                point = ecs.cayley_euler_approximant(theta, steps)
                self.assertEqual(ecs.character_norm_squared(point), 1)

    def test_core_has_no_pi_or_trigonometric_dependency(self):
        source = inspect.getsource(ecs)
        self.assertNotIn("math.pi", source)
        self.assertNotIn("sin(", source)
        self.assertNotIn("cos(", source)


if __name__ == "__main__":
    unittest.main()
