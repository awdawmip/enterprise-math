import unittest

from enterprise_math.engineering_collision import Body2D
from enterprise_math.motion_action_constraints import maximum_constraint_solutions
from enterprise_math.motion_collapse import BodyMotion2D
from enterprise_math.scale_motion_constraints import (
    endpoint_clause_finest_active_factor,
    sampled_endpoint_macro_constraints,
    transition_aware_macro_constraints,
)


class ScaleMotionConstraintTests(unittest.TestCase):
    def test_approach_is_blocked_coarsely_but_both_moves_allowed_finely(self):
        motions = [
            BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(1, 3, 0, 0), (-1, 0)),
        ]
        coarse = sampled_endpoint_macro_constraints(motions, 2).constraints
        fine = sampled_endpoint_macro_constraints(motions, 1).constraints
        self.assertEqual(coarse.mutex_pairs, ((0, 1),))
        self.assertEqual(coarse.implications, ())
        self.assertEqual(
            set(maximum_constraint_solutions(coarse)),
            {frozenset({0}), frozenset({1})},
        )
        self.assertEqual(fine.mutex_pairs, ())
        self.assertEqual(fine.implications, ())
        self.assertEqual(maximum_constraint_solutions(fine), (frozenset({0, 1}),))

    def test_fine_static_only_swap_allows_pass_through_but_transition_aware_blocks(self):
        motions = [
            BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0)),
        ]
        static = sampled_endpoint_macro_constraints(motions, 1).constraints
        aware = transition_aware_macro_constraints(motions, 1).constraints
        self.assertEqual(static.mutex_pairs, ())
        self.assertEqual(set(static.implications), {(0, 1), (1, 0)})
        self.assertEqual(maximum_constraint_solutions(static), (frozenset({0, 1}),))

        self.assertEqual(aware.mutex_pairs, ((0, 1),))
        self.assertEqual(set(aware.implications), {(0, 1), (1, 0)})
        self.assertEqual(maximum_constraint_solutions(aware), (frozenset(),))

    def test_coarse_current_macro_contact_requires_repair_before_evolution(self):
        motions = [
            BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0)),
        ]
        with self.assertRaises(ValueError):
            sampled_endpoint_macro_constraints(motions, 2)
        with self.assertRaises(ValueError):
            transition_aware_macro_constraints(motions, 2)

    def test_endpoint_mutex_has_exact_single_refinement_extinction_threshold(self):
        motions = [
            BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(1, 4, 0, 0), (-1, 0)),
        ]
        # MOVE/MOVE endpoints are 1 and 3: primitive point gap = 2.
        self.assertEqual(endpoint_clause_finest_active_factor(2), 3)
        observed = []
        for factor in range(5, 0, -1):
            try:
                report = sampled_endpoint_macro_constraints(motions, factor).constraints
            except ValueError:
                observed.append((factor, "CURRENT_CONTACT"))
                continue
            observed.append((factor, (0, 1) in report.mutex_pairs))
        # Current WAIT/WAIT gap is 4, so d=5 already treats current state as macro contact.
        self.assertEqual(observed[0], (5, "CURRENT_CONTACT"))
        self.assertEqual(observed[1:], [(4, True), (3, True), (2, False), (1, False)])

    def test_persistent_terminal_endpoint_contact_never_extinguishes(self):
        motions = [
            BodyMotion2D(Body2D(0, -1, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0)),
        ]
        self.assertIsNone(endpoint_clause_finest_active_factor(0))
        for factor in (1, 2):
            report = sampled_endpoint_macro_constraints(motions, factor).constraints
            self.assertIn((0, 1), report.mutex_pairs)

    def test_refinement_only_removes_sampled_endpoint_clauses_while_current_state_valid(self):
        motions = [
            BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(1, 4, 0, 0), (-1, 0)),
            BodyMotion2D(Body2D(2, 8, 0, 0), (-1, 0)),
        ]
        previous = None
        for factor in (4, 3, 2, 1):
            report = sampled_endpoint_macro_constraints(motions, factor).constraints
            current = (
                set(report.forced_wait_ids),
                set(report.mutex_pairs),
                set(report.implications),
            )
            if previous is not None:
                self.assertTrue(current[0].issubset(previous[0]))
                self.assertTrue(current[1].issubset(previous[1]))
                self.assertTrue(current[2].issubset(previous[2]))
            previous = current

    def test_invalid_gap_is_rejected(self):
        with self.assertRaises(ValueError):
            endpoint_clause_finest_active_factor(-1)


if __name__ == "__main__":
    unittest.main()
