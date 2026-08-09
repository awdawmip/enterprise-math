import unittest
from itertools import combinations, product

from enterprise_math.engineering_collision import Body2D
from enterprise_math.motion_action_constraints import (
    accepted_set_satisfies_constraints,
    binary_motion_constraints,
    maximum_constraint_solutions,
)
from enterprise_math.motion_collapse import BodyMotion2D, maximum_conflict_free_move_sets


class MotionActionConstraintTests(unittest.TestCase):
    def test_head_on_swap_becomes_mutex_plus_mutual_implication(self):
        motions = [
            BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0)),
        ]
        report = binary_motion_constraints(motions)
        self.assertEqual(report.mutex_pairs, ((0, 1),))
        self.assertEqual(set(report.implications), {(0, 1), (1, 0)})
        self.assertEqual(report.forced_wait_ids, ())
        self.assertEqual(maximum_constraint_solutions(report), (frozenset(),))

    def test_convergence_has_mutex_without_move_dependencies(self):
        motions = [
            BodyMotion2D(Body2D(0, -1, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0)),
        ]
        report = binary_motion_constraints(motions)
        self.assertEqual(report.mutex_pairs, ((0, 1),))
        self.assertEqual(report.implications, ())
        self.assertEqual(
            set(maximum_constraint_solutions(report)),
            {frozenset({0}), frozenset({1})},
        )

    def test_following_move_produces_forward_dependency(self):
        motions = [
            BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(1, 1, 0, 0), (1, 0)),
        ]
        report = binary_motion_constraints(motions)
        self.assertEqual(report.mutex_pairs, ())
        self.assertEqual(report.implications, ((0, 1),))
        self.assertTrue(accepted_set_satisfies_constraints(report, frozenset({0, 1})))
        self.assertFalse(accepted_set_satisfies_constraints(report, frozenset({0})))
        self.assertTrue(accepted_set_satisfies_constraints(report, frozenset({1})))
        self.assertEqual(maximum_constraint_solutions(report), (frozenset({0, 1}),))

    def test_explicit_waiting_body_can_force_proposed_move_to_wait(self):
        motions = [
            BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(1, 1, 0, 0), (0, 0)),
        ]
        report = binary_motion_constraints(motions)
        self.assertEqual(report.moving_ids, (0,))
        self.assertEqual(report.forced_wait_ids, (0,))
        self.assertEqual(maximum_constraint_solutions(report), (frozenset(),))

    def test_constraint_factorization_matches_target_oracle_on_small_1d_domain(self):
        positions = [-2, -1, 0, 1, 2]
        steps = [(-1, 0), (0, 0), (1, 0)]
        for points in combinations(positions, 3):
            bodies = [Body2D(body_id, x, 0, 0) for body_id, x in enumerate(points)]
            for proposed in product(steps, repeat=3):
                motions = [
                    BodyMotion2D(body, step)
                    for body, step in zip(bodies, proposed, strict=True)
                ]
                report = binary_motion_constraints(motions)
                self.assertEqual(
                    maximum_constraint_solutions(report),
                    maximum_conflict_free_move_sets(motions),
                    (points, proposed, report),
                )

    def test_initial_overlap_is_rejected(self):
        motions = [
            BodyMotion2D(Body2D(0, 0, 0, 1), (0, 0)),
            BodyMotion2D(Body2D(1, 1, 0, 1), (0, 0)),
        ]
        with self.assertRaises(ValueError):
            binary_motion_constraints(motions)


if __name__ == "__main__":
    unittest.main()
