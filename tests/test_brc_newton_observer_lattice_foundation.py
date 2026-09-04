from fractions import Fraction
import unittest

from enterprise_math.brc_newton_fiber_quotient import NewtonFiberCoordinate, NewtonFiberPosition
from enterprise_math.brc_newton_observer_lattice import (
    FrozenNewtonScheduleStep,
    NewtonCoordinateObserver,
    coordinate_observer_equivalent,
    coordinate_observer_kernel_dimension,
    coordinate_observer_signature,
    edge_coordinate_observer,
    frozen_horizon_edge_signature,
    frozen_horizon_kernel_profile,
    frozen_horizon_observability_analysis,
    frozen_horizon_rank_profile,
    frozen_newton_substitution,
    full_coordinate_observer,
)
from enterprise_math.brc_newton_recursion import RationalValuationScale

Q = Fraction
ONE = RationalValuationScale.one()


def s(value):
    return RationalValuationScale.from_rational(Q(value))


def layout():
    return (
        NewtonFiberPosition(s(Q(1, 4)), 0, "a"),
        NewtonFiberPosition(s(Q(1, 4)), 0, "b"),
        NewtonFiberPosition(s(Q(1, 2)), 1, "c"),
        NewtonFiberPosition(s(Q(1, 2)), 1, "d"),
        NewtonFiberPosition(ONE, 2, "e"),
        NewtonFiberPosition(s(Q(1, 8)), 0, "f"),
        NewtonFiberPosition(s(Q(1, 4)), 1, "g"),
    )


class NewtonObserverLatticeFoundationTests(unittest.TestCase):
    def setUp(self):
        self.positions = layout()
        self.theta = s(Q(1, 2))
        self.r = 2

    def test_coordinate_observer_lattice(self):
        full = full_coordinate_observer(self.positions, self.theta, self.r)
        edge = edge_coordinate_observer(self.positions, self.theta, self.r)
        self.assertEqual(full.rank, 5)
        self.assertEqual(edge.rank, 3)
        self.assertTrue(full.refines(edge))
        self.assertFalse(edge.refines(full))
        self.assertEqual(full.join(edge), full)
        self.assertEqual(full.meet(edge), edge)
        self.assertEqual(coordinate_observer_kernel_dimension(self.positions, self.theta, self.r, full), 2)
        self.assertEqual(coordinate_observer_kernel_dimension(self.positions, self.theta, self.r, edge), 4)

    def test_observer_normalization_and_signature(self):
        full = full_coordinate_observer(self.positions, self.theta, self.r)
        edge = edge_coordinate_observer(self.positions, self.theta, self.r)
        duplicate = NewtonCoordinateObserver((full.coordinates[-1], full.coordinates[0], full.coordinates[-1]))
        self.assertEqual(duplicate.rank, 2)
        self.assertEqual(duplicate.coordinates, tuple(sorted(set(duplicate.coordinates), key=lambda c: (c.residual_scale.valuations, c.taylor_degree))))

        left = (Q(1), Q(2), Q(3), Q(4), Q(5), Q(0), Q(0))
        right = (Q(1), Q(2), Q(3), Q(4), Q(5), Q(7), Q(-9))
        self.assertTrue(coordinate_observer_equivalent(self.positions, left, right, self.theta, self.r, edge))
        self.assertFalse(coordinate_observer_equivalent(self.positions, left, right, self.theta, self.r, full))
        self.assertEqual(len(coordinate_observer_signature(self.positions, left, self.theta, self.r, full)), 5)

    def test_frozen_horizon_rank_profile(self):
        coordinates = (
            NewtonFiberCoordinate(ONE, 0),
            NewtonFiberCoordinate(ONE, 1),
            NewtonFiberCoordinate(ONE, 2),
            NewtonFiberCoordinate(s(Q(1, 2)), 1),
            NewtonFiberCoordinate(s(Q(1, 4)), 0),
            NewtonFiberCoordinate(s(Q(1, 16)), 0),
        )
        schedule = (
            FrozenNewtonScheduleStep(Q(-1), 2, self.theta),
            FrozenNewtonScheduleStep(Q(-1), 2, self.theta),
        )
        self.assertEqual(frozen_horizon_rank_profile(coordinates, schedule), (3, 5, 6))
        self.assertEqual(frozen_horizon_kernel_profile(coordinates, schedule), (3, 1, 0))
        final = frozen_horizon_observability_analysis(tuple(reversed(coordinates)) + (coordinates[0],), schedule)
        self.assertEqual(final.rank, 6)
        self.assertEqual(final.kernel_dimension, 0)
        self.assertEqual(len(final.initial_coordinates), 6)

    def test_deep_coordinate_becomes_visible_later(self):
        deep = NewtonFiberCoordinate(s(Q(1, 16)), 0)
        schedule = (
            FrozenNewtonScheduleStep(Q(-1), 2, self.theta),
            FrozenNewtonScheduleStep(Q(-1), 2, self.theta),
        )
        horizon = frozen_horizon_edge_signature(((deep, Q(1)),), schedule)
        self.assertEqual(horizon[0], ())
        self.assertEqual(horizon[1], ())
        self.assertEqual(horizon[2], ((0, Q(1)),))

    def test_scheduled_substitution_is_linear(self):
        step = FrozenNewtonScheduleStep(Q(-1), 2, self.theta)
        a = NewtonFiberCoordinate(s(Q(1, 2)), 1)
        b = NewtonFiberCoordinate(s(Q(1, 4)), 0)
        left = ((a, Q(2)),)
        right = ((b, Q(3)),)
        combined = ((a, Q(2)), (b, Q(3)))
        lhs = dict(frozen_newton_substitution(combined, step))
        rhs = dict(frozen_newton_substitution(left, step))
        for coordinate, value in frozen_newton_substitution(right, step):
            rhs[coordinate] = rhs.get(coordinate, Q(0)) + value
        rhs = {coordinate: value for coordinate, value in rhs.items() if value}
        self.assertEqual(lhs, rhs)

    def test_input_guards(self):
        with self.assertRaises(TypeError):
            FrozenNewtonScheduleStep(Q(0), True, self.theta)
        with self.assertRaises(ValueError):
            FrozenNewtonScheduleStep(Q(0), 0, self.theta)
        with self.assertRaises(TypeError):
            NewtonCoordinateObserver(("bad",))
        full = full_coordinate_observer(self.positions, self.theta, self.r)
        alien = NewtonCoordinateObserver((NewtonFiberCoordinate(s(Q(1, 32)), 9),))
        with self.assertRaises(ValueError):
            coordinate_observer_signature(self.positions, (0,) * len(self.positions), self.theta, self.r, alien)
        self.assertEqual(full.rank, 5)


if __name__ == "__main__":
    unittest.main()
