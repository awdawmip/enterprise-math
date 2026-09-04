from fractions import Fraction
import unittest

from enterprise_math.brc_newton_schedule_strata import RationalAffineForm
from enterprise_math.brc_newton_selector_chambers import (
    AffineOrderAtom,
    SplitAffineRootBranch,
    SplitAffineRootCertificate,
    split_affine_fixed_multiplicity_holds,
    split_affine_matches_polynomial,
    split_affine_materialize_monic_polynomial,
    split_affine_smallest_positive_chamber,
    split_affine_smallest_positive_selected,
    split_affine_smallest_real_chamber,
    split_affine_smallest_real_selected,
)

Q = Fraction


def f(const=0, *linear):
    return RationalAffineForm((Q(const),) + tuple(Q(value) for value in linear))


def scale_poly(poly, scalar):
    return tuple(Q(scalar) * value for value in poly)


class NewtonSelectorChambersFoundationTests(unittest.TestCase):
    def setUp(self):
        self.u = SplitAffineRootBranch(f(0, 1, 0))
        self.v = SplitAffineRootBranch(f(0, 0, 1))
        self.real = SplitAffineRootCertificate(Q(-1), 2, (self.u, self.v), 4)
        self.positive = SplitAffineRootCertificate(Q(1), 2, (self.u, self.v), 4)

    def test_smallest_real_chamber(self):
        chamber = split_affine_smallest_real_chamber(self.real)
        self.assertEqual(chamber.selector, "SMALLEST_REAL_ROOT")
        self.assertTrue(chamber.holds((0, 2)))
        self.assertTrue(split_affine_smallest_real_selected(self.real, (0, 2)))
        self.assertFalse(chamber.holds((-2, 2)))
        self.assertFalse(split_affine_smallest_real_selected(self.real, (-2, 2)))
        self.assertFalse(split_affine_fixed_multiplicity_holds(self.real, (-1, 2)))
        self.assertFalse(split_affine_smallest_real_selected(self.real, (-1, 2)))

    def test_smallest_positive_boolean_chamber_and_zero_boundary(self):
        chamber = split_affine_smallest_positive_chamber(self.positive)
        self.assertEqual(chamber.selector, "SMALLEST_POSITIVE_REAL_ROOT")
        self.assertTrue(chamber.holds((0, Q(3, 2))))
        self.assertTrue(split_affine_smallest_positive_selected(self.positive, (0, Q(3, 2))))
        self.assertFalse(chamber.holds((Q(1, 2), Q(3, 2))))
        self.assertFalse(split_affine_smallest_positive_selected(self.positive, (Q(1, 2), Q(3, 2))))
        self.assertFalse(split_affine_fixed_multiplicity_holds(self.positive, (1, 2)))
        self.assertFalse(split_affine_smallest_positive_selected(self.positive, (1, 2)))

    def test_smallest_positive_chamber_is_not_convex(self):
        left = (Q(-1), Q(2))
        right = (Q(2), Q(-1))
        midpoint = (Q(1, 2), Q(1, 2))
        self.assertTrue(split_affine_smallest_positive_selected(self.positive, left))
        self.assertTrue(split_affine_smallest_positive_selected(self.positive, right))
        self.assertFalse(split_affine_smallest_positive_selected(self.positive, midpoint))

    def test_materialization_and_matching_up_to_scalar(self):
        params = (Q(0), Q(2))
        monic = split_affine_materialize_monic_polynomial(self.real, params)
        self.assertEqual(len(monic) - 1, 4)
        self.assertTrue(split_affine_matches_polynomial(self.real, params, monic))
        self.assertTrue(split_affine_matches_polynomial(self.real, params, scale_poly(monic, -7)))
        corrupted = list(monic)
        corrupted[0] += 1
        self.assertFalse(split_affine_matches_polynomial(self.real, params, corrupted))

    def test_branch_multiplicity_and_parameter_dimension(self):
        doubled = SplitAffineRootBranch(f(0, 1), 2)
        certificate = SplitAffineRootCertificate(Q(-1), 3, (doubled,), 5)
        poly = split_affine_materialize_monic_polynomial(certificate, (Q(2),))
        self.assertEqual(len(poly) - 1, 5)
        self.assertTrue(split_affine_smallest_real_selected(certificate, (Q(2),)))

    def test_input_guards(self):
        with self.assertRaises(ValueError):
            SplitAffineRootBranch(f(0, 1), 0)
        with self.assertRaises(ValueError):
            SplitAffineRootCertificate(Q(-1), 2, (self.u, self.v), 5)
        with self.assertRaises(ValueError):
            SplitAffineRootCertificate(Q(-1), 2, (self.u, SplitAffineRootBranch(f(0, 1))), 4)
        with self.assertRaises(ValueError):
            split_affine_smallest_positive_chamber(self.real)
        with self.assertRaises(ValueError):
            AffineOrderAtom(f(1, 1), "BAD")
        with self.assertRaises(ValueError):
            split_affine_matches_polynomial(self.real, (0, 1), (0,))


if __name__ == "__main__":
    unittest.main()
