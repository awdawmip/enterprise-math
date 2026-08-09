import unittest

from enterprise_math.engineering_collision import Body2D
from enterprise_math.motion_collapse import (
    BodyMotion2D,
    maximum_conflict_free_move_sets,
    maximum_conflict_free_outcomes,
    motion_conflict,
    motion_conflict_pairs,
    motion_conflict_witnesses,
)


class MotionCollapseTests(unittest.TestCase):
    def test_same_endpoint_is_vertex_conflict(self):
        left = BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0))
        right = BodyMotion2D(Body2D(1, 2, 0, 0), (-1, 0))
        witnesses = motion_conflict_witnesses(left, right)
        self.assertTrue(motion_conflict(left, right))
        self.assertIn(("vertex", (1, 0)), witnesses)

    def test_adjacent_point_swap_is_edge_conflict_even_with_distinct_endpoints(self):
        left = BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0))
        right = BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0))
        self.assertNotEqual(left.end_body.x, right.end_body.x)
        witnesses = motion_conflict_witnesses(left, right)
        self.assertIn(("edge", ((0, 0), (1, 0))), witnesses)
        self.assertTrue(motion_conflict(left, right))

    def test_distinct_diagonal_edges_do_not_conflict_without_extra_incidence(self):
        left = BodyMotion2D(Body2D(0, 0, 0, 0), (1, 1))
        right = BodyMotion2D(Body2D(1, 0, 1, 0), (1, -1))
        self.assertFalse(motion_conflict(left, right))
        self.assertEqual(motion_conflict_witnesses(left, right), frozenset())

    def test_following_move_uses_distinct_atomic_edges(self):
        left = BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0))
        right = BodyMotion2D(Body2D(1, 1, 0, 0), (1, 0))
        self.assertFalse(motion_conflict(left, right))

    def test_extended_support_endpoint_overlap_is_vertex_target_conflict(self):
        left = BodyMotion2D(Body2D(0, 0, 0, 1), (1, 0))
        right = BodyMotion2D(Body2D(1, 3, 0, 1), (-1, 0))
        witnesses = motion_conflict_witnesses(left, right)
        vertex_witnesses = {target for kind, target in witnesses if kind == "vertex"}
        self.assertTrue(vertex_witnesses)
        self.assertTrue(motion_conflict(left, right))

    def test_inverted_target_index_matches_pairwise_conflict_check(self):
        motions = [
            BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0)),
            BodyMotion2D(Body2D(2, 5, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(3, 8, 0, 0), (0, 0)),
        ]
        expected = set()
        for left_index, left in enumerate(motions):
            for right in motions[left_index + 1 :]:
                if motion_conflict(left, right):
                    expected.add(tuple(sorted((left.body_id, right.body_id))))
        self.assertEqual(set(motion_conflict_pairs(motions)), expected)
        self.assertEqual(
            motion_conflict_pairs(list(reversed(motions))),
            motion_conflict_pairs(motions),
        )

    def test_head_on_swap_forces_both_point_moves_to_wait(self):
        motions = [
            BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0)),
        ]
        self.assertEqual(maximum_conflict_free_move_sets(motions), (frozenset(),))
        outcomes = maximum_conflict_free_outcomes(motions)
        self.assertEqual(len(outcomes), 1)
        self.assertEqual(outcomes[0].accepted_moving_ids, frozenset())
        self.assertEqual(outcomes[0].bodies, (Body2D(0, 0, 0, 0), Body2D(1, 1, 0, 0)))

    def test_symmetric_competition_preserves_both_maximum_admission_choices(self):
        motions = [
            BodyMotion2D(Body2D(0, -1, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0)),
        ]
        self.assertEqual(
            set(maximum_conflict_free_move_sets(motions)),
            {frozenset({0}), frozenset({1})},
        )
        outcomes = maximum_conflict_free_outcomes(motions)
        self.assertEqual(
            {(outcome.accepted_moving_ids, outcome.bodies) for outcome in outcomes},
            {
                (frozenset({0}), (Body2D(0, 0, 0, 0), Body2D(1, 1, 0, 0))),
                (frozenset({1}), (Body2D(0, -1, 0, 0), Body2D(1, 0, 0, 0))),
            },
        )
        self.assertEqual(
            maximum_conflict_free_outcomes(list(reversed(motions))),
            outcomes,
        )

    def test_same_proposed_conflict_graph_can_have_different_response_capacity(self):
        head_on = [
            BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0)),
        ]
        converge = [
            BodyMotion2D(Body2D(0, -1, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0)),
        ]
        self.assertEqual(motion_conflict_pairs(head_on), ((0, 1),))
        self.assertEqual(motion_conflict_pairs(converge), ((0, 1),))
        self.assertEqual(maximum_conflict_free_move_sets(head_on), (frozenset(),))
        self.assertEqual(
            set(maximum_conflict_free_move_sets(converge)),
            {frozenset({0}), frozenset({1})},
        )

    def test_independent_moves_are_all_accepted(self):
        motions = [
            BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(1, 5, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(2, 10, 0, 0), (0, 1)),
        ]
        self.assertEqual(
            maximum_conflict_free_move_sets(motions),
            (frozenset({0, 1, 2}),),
        )

    def test_waiting_body_blocks_move_into_its_terminal_support(self):
        motions = [
            BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0)),
            BodyMotion2D(Body2D(1, 1, 0, 0), (0, 0)),
        ]
        self.assertEqual(maximum_conflict_free_move_sets(motions), (frozenset(),))

    def test_initial_overlap_is_rejected_by_admission_oracle(self):
        motions = [
            BodyMotion2D(Body2D(0, 0, 0, 1), (1, 0)),
            BodyMotion2D(Body2D(1, 1, 0, 1), (-1, 0)),
        ]
        with self.assertRaises(ValueError):
            maximum_conflict_free_move_sets(motions)

    def test_nonprimitive_or_noninteger_step_is_rejected(self):
        with self.assertRaises(ValueError):
            BodyMotion2D(Body2D(0, 0, 0, 0), (2, 0))
        with self.assertRaises(ValueError):
            BodyMotion2D(Body2D(0, 0, 0, 0), (True, 0))


if __name__ == "__main__":
    unittest.main()
