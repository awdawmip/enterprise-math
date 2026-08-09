import unittest

from enterprise_math.collision_trigger_policy import (
    SAMPLED_STATIC,
    TRANSITION_AWARE,
    collision_trigger_profile,
    policy_spatial_extinction_factor,
    response_triggered,
    sampled_static_trigger_first_resolving_factor,
)
from enterprise_math.engineering_collision import Body2D
from enterprise_math.motion_collapse import BodyMotion2D


class CollisionTriggerPolicyTests(unittest.TestCase):
    def test_point_swap_loses_static_trigger_at_terminal_factor_but_keeps_edge_trigger(self):
        left = BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0))
        right = BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0))

        coarse = collision_trigger_profile(left, right, collapse_factor=2)
        terminal = collision_trigger_profile(left, right, collapse_factor=1)

        self.assertEqual(coarse.sampled_static_primitive_gap, 1)
        self.assertTrue(coarse.sampled_static_trigger)
        self.assertTrue(coarse.transition_conflict)
        self.assertTrue(response_triggered(coarse, SAMPLED_STATIC))
        self.assertTrue(response_triggered(coarse, TRANSITION_AWARE))

        self.assertFalse(terminal.sampled_static_trigger)
        self.assertTrue(terminal.transition_conflict)
        self.assertFalse(response_triggered(terminal, SAMPLED_STATIC))
        self.assertTrue(response_triggered(terminal, TRANSITION_AWARE))
        self.assertEqual(sampled_static_trigger_first_resolving_factor(left, right), 1)
        self.assertEqual(policy_spatial_extinction_factor(left, right, SAMPLED_STATIC), 1)
        self.assertIsNone(policy_spatial_extinction_factor(left, right, TRANSITION_AWARE))

    def test_static_trigger_extinction_factor_matches_direct_factor_sweep(self):
        motions = (
            (
                BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0)),
                BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0)),
            ),
            (
                BodyMotion2D(Body2D(0, 0, 0, 0), (0, 0)),
                BodyMotion2D(Body2D(1, 3, 0, 0), (-1, 0)),
            ),
            (
                BodyMotion2D(Body2D(0, -5, 0, 1), (1, 0)),
                BodyMotion2D(Body2D(1, 1, 0, 1), (-1, 0)),
            ),
        )
        for left, right in motions:
            gap = min(
                collision_trigger_profile(left, right, 1).start_primitive_gap,
                collision_trigger_profile(left, right, 1).end_primitive_gap,
            )
            threshold = sampled_static_trigger_first_resolving_factor(left, right)
            self.assertEqual(threshold, None if gap == 0 else gap)
            for factor in range(1, max(6, gap + 3)):
                profile = collision_trigger_profile(left, right, factor)
                self.assertEqual(profile.sampled_static_trigger, gap < factor)

    def test_policy_threshold_depends_on_transition_subscription(self):
        left = BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0))
        right = BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0))
        sampled = []
        aware = []
        for factor in range(4, 0, -1):
            profile = collision_trigger_profile(left, right, factor)
            sampled.append((factor, response_triggered(profile, SAMPLED_STATIC)))
            aware.append((factor, response_triggered(profile, TRANSITION_AWARE)))
        self.assertEqual(sampled, [(4, True), (3, True), (2, True), (1, False)])
        self.assertTrue(all(triggered for _factor, triggered in aware))

    def test_no_transition_conflict_gives_same_extinction_for_both_policies(self):
        left = BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0))
        right = BodyMotion2D(Body2D(1, 4, 0, 0), (-1, 0))
        self.assertFalse(collision_trigger_profile(left, right, 1).transition_conflict)
        self.assertEqual(
            policy_spatial_extinction_factor(left, right, SAMPLED_STATIC),
            policy_spatial_extinction_factor(left, right, TRANSITION_AWARE),
        )

    def test_same_endpoint_collision_has_no_spatial_extinction(self):
        left = BodyMotion2D(Body2D(0, -1, 0, 0), (1, 0))
        right = BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0))
        profile = collision_trigger_profile(left, right, collapse_factor=1)
        self.assertFalse(profile.start_macro_contact)
        self.assertTrue(profile.end_macro_contact)
        self.assertTrue(profile.transition_conflict)
        self.assertTrue(response_triggered(profile, SAMPLED_STATIC))
        self.assertIsNone(sampled_static_trigger_first_resolving_factor(left, right))
        self.assertIsNone(policy_spatial_extinction_factor(left, right, SAMPLED_STATIC))
        self.assertIsNone(policy_spatial_extinction_factor(left, right, TRANSITION_AWARE))

    def test_distinct_diagonal_graph_edges_do_not_gain_hidden_continuum_trigger(self):
        left = BodyMotion2D(Body2D(0, 0, 0, 0), (1, 1))
        right = BodyMotion2D(Body2D(1, 0, 1, 0), (1, -1))
        profile = collision_trigger_profile(left, right, collapse_factor=1)
        self.assertFalse(profile.sampled_static_trigger)
        self.assertFalse(profile.transition_conflict)
        self.assertFalse(response_triggered(profile, TRANSITION_AWARE))

    def test_separated_parallel_motion_has_no_trigger(self):
        left = BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0))
        right = BodyMotion2D(Body2D(1, 5, 0, 0), (1, 0))
        for factor in (1, 2):
            profile = collision_trigger_profile(left, right, factor)
            self.assertFalse(profile.sampled_static_trigger)
            self.assertFalse(profile.transition_conflict)
            self.assertFalse(response_triggered(profile, SAMPLED_STATIC))
            self.assertFalse(response_triggered(profile, TRANSITION_AWARE))

    def test_invalid_policy_and_factor_are_rejected(self):
        left = BodyMotion2D(Body2D(0, 0, 0, 0), (0, 0))
        right = BodyMotion2D(Body2D(1, 5, 0, 0), (0, 0))
        profile = collision_trigger_profile(left, right, 1)
        with self.assertRaises(ValueError):
            response_triggered(profile, "UNKNOWN")
        with self.assertRaises(ValueError):
            collision_trigger_profile(left, right, 0)
        with self.assertRaises(ValueError):
            policy_spatial_extinction_factor(left, right, "UNKNOWN")


if __name__ == "__main__":
    unittest.main()
