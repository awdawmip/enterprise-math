from fractions import Fraction
import unittest

from enterprise_math.brc_newton_fiber_quotient import (
    NewtonFiberPosition,
    apply_newton_fiber_transfer,
    newton_fiber_coordinate,
    newton_fiber_edge_signature,
    newton_fiber_equivalent,
    newton_fiber_quotient_analysis,
    newton_fiber_sum_signature,
)
from enterprise_math.brc_newton_recursion import RationalValuationScale

Q = Fraction


def s(value):
    return RationalValuationScale.from_rational(Q(value))


class NewtonFiberQuotientFoundationTests(unittest.TestCase):
    def setUp(self):
        self.theta = s(Q(1, 2))
        self.r = 2
        self.positions = (
            NewtonFiberPosition(s(Q(1, 2)), 1, "A1"),
            NewtonFiberPosition(s(Q(1, 2)), 1, "A2"),
            NewtonFiberPosition(s(Q(1, 4)), 0, "B1"),
            NewtonFiberPosition(s(Q(1, 4)), 0, "B2"),
            NewtonFiberPosition(s(Q(1, 8)), 0, "C"),
            NewtonFiberPosition(s(Q(1, 4)), 1, "D"),
        )

    def test_rank_kernel_and_transfer_basis(self):
        analysis = newton_fiber_quotient_analysis(self.positions, self.theta, self.r)
        self.assertEqual(analysis.observer_rank, 4)
        self.assertEqual(analysis.kernel_dimension, 2)
        self.assertEqual(len(analysis.transfer_basis), 2)

    def test_transfer_preserves_full_signature(self):
        coefficients = (Q(1), Q(1), Q(2), Q(-1), Q(3), Q(4))
        analysis = newton_fiber_quotient_analysis(self.positions, self.theta, self.r)
        moved = coefficients
        for anchor, index in analysis.transfer_basis:
            moved = apply_newton_fiber_transfer(moved, anchor, index, Q(7, 3))
        self.assertTrue(newton_fiber_equivalent(self.positions, coefficients, moved, self.theta, self.r))
        self.assertEqual(
            newton_fiber_sum_signature(self.positions, coefficients, self.theta, self.r),
            newton_fiber_sum_signature(self.positions, moved, self.theta, self.r),
        )

    def test_same_residual_scale_different_degree_does_not_merge(self):
        c = newton_fiber_coordinate(self.positions[4], self.theta, self.r)
        d = newton_fiber_coordinate(self.positions[5], self.theta, self.r)
        self.assertEqual(c.residual_scale, d.residual_scale)
        self.assertNotEqual(c.taylor_degree, d.taylor_degree)
        left = (Q(0), Q(0), Q(0), Q(0), Q(1), Q(0))
        right = (Q(0), Q(0), Q(0), Q(0), Q(0), Q(1))
        self.assertFalse(newton_fiber_equivalent(self.positions, left, right, self.theta, self.r))

    def test_edge_only_observer_is_strictly_coarser(self):
        left = (Q(1), Q(1), Q(2), Q(-1), Q(3), Q(4))
        right = list(left)
        right[4] += 9  # rho=1/2 only, edge rho=1 unchanged
        right = tuple(right)
        self.assertFalse(newton_fiber_equivalent(self.positions, left, right, self.theta, self.r))
        self.assertEqual(
            newton_fiber_edge_signature(self.positions, left, self.theta, self.r),
            newton_fiber_edge_signature(self.positions, right, self.theta, self.r),
        )

    def test_label_splitting_is_invisible(self):
        one = (NewtonFiberPosition(s(Q(1, 8)), 0, "X"),)
        split = (
            NewtonFiberPosition(s(Q(1, 8)), 0, "X1"),
            NewtonFiberPosition(s(Q(1, 8)), 0, "X2"),
        )
        self.assertEqual(
            newton_fiber_sum_signature(one, (Q(7),), self.theta, self.r),
            newton_fiber_sum_signature(split, (Q(10), Q(-3)), self.theta, self.r),
        )

    def test_input_guards(self):
        with self.assertRaises(ValueError):
            newton_fiber_quotient_analysis((), self.theta, self.r)
        with self.assertRaises(ValueError):
            apply_newton_fiber_transfer((Q(1), Q(2)), 0, 0, Q(1))
        with self.assertRaises(TypeError):
            NewtonFiberPosition(self.theta, True)


if __name__ == "__main__":
    unittest.main()
