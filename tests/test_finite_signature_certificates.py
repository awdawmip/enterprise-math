import unittest
from fractions import Fraction

from enterprise_math.finite_signature_certificates import (
    affine_separation_certificate_holds,
    boolean_join,
    boolean_join_certificate_holds,
    convex_membership_certificate_holds,
    integer_cone_separation_certificate_holds,
    integer_dot,
    nonnegative_integer_combination,
    rational_convex_combination,
    rational_dot,
)


class FiniteSignatureCertificateTests(unittest.TestCase):
    def test_boolean_join_completion_certificate(self):
        generators = (
            (True, False, False, True),
            (False, True, False, False),
            (False, False, True, False),
        )
        target = (True, True, True, True)
        self.assertEqual(boolean_join(generators), target)
        self.assertTrue(boolean_join_certificate_holds(generators, (0, 1, 2), target))
        self.assertFalse(boolean_join_certificate_holds(generators, (0, 1), target))

    def test_exact_rational_convex_membership_certificate(self):
        vertices = ((0, 0), (1, 0), (0, 1))
        weights = (0, Fraction(1, 2), Fraction(1, 2))
        target = (Fraction(1, 2), Fraction(1, 2))
        self.assertEqual(rational_convex_combination(vertices, weights), target)
        self.assertTrue(convex_membership_certificate_holds(vertices, target, weights))

    def test_exact_affine_separator_excludes_target_from_triangle(self):
        vertices = ((0, 0), (1, 0), (0, 1))
        target = (1, 1)
        functional = (1, 1)
        self.assertTrue(
            affine_separation_certificate_holds(
                vertices, target, functional, threshold=1
            )
        )
        self.assertFalse(
            affine_separation_certificate_holds(
                vertices, (Fraction(1, 2), Fraction(1, 2)), functional, threshold=1
            )
        )

    def test_integer_cone_verifier_is_generic_r004_extraction(self):
        generators = ((-1, 0), (0, -1))
        target = (1, 1)
        functional = (1, 1)
        self.assertTrue(
            integer_cone_separation_certificate_holds(
                generators, target, functional
            )
        )
        combination = nonnegative_integer_combination(generators, (2, 3))
        self.assertEqual(combination, (-2, -3))
        self.assertLessEqual(integer_dot(functional, combination), 0)

    def test_rational_dot_is_exact(self):
        self.assertEqual(
            rational_dot((Fraction(1, 3), Fraction(2, 5)), (3, 5)),
            Fraction(3),
        )

    def test_shared_randomization_boundary_is_not_silently_weakened(self):
        vertices = ((0,), (1,))
        with self.assertRaisesRegex(ValueError, "sum exactly to one"):
            rational_convex_combination(vertices, (Fraction(1, 3), Fraction(1, 3)))
        with self.assertRaisesRegex(ValueError, "non-negative"):
            rational_convex_combination(vertices, (Fraction(3, 2), Fraction(-1, 2)))

    def test_certificate_shapes_fail_closed(self):
        with self.assertRaises(ValueError):
            boolean_join(())
        with self.assertRaises(ValueError):
            boolean_join(((True,), (False, False)))
        with self.assertRaises(ValueError):
            boolean_join_certificate_holds(((True,),), (), (True,))
        with self.assertRaises(ValueError):
            convex_membership_certificate_holds(((0, 0),), (0,), (1,))
        with self.assertRaises(ValueError):
            affine_separation_certificate_holds(((0, 0),), (1,), (1,), 0)
        with self.assertRaises(ValueError):
            integer_cone_separation_certificate_holds((), (1,), (1,))


if __name__ == "__main__":
    unittest.main()
