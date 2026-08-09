import unittest

from enterprise_math.collision_trigger_policy import (
    SAMPLED_STATIC,
    TRANSITION_AWARE,
    collision_trigger_profile,
    response_triggered,
)
from enterprise_math.engineering_collision import Body2D
from enterprise_math.motion_collapse import BodyMotion2D


class CollisionTriggerPolicyTests(unittest.TestCase):
    def test_point_swap_loses_static_trigger_at_terminal_factor_but_keeps_edge_trigger(self):
        left = BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0))
        right = BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0))

        coarse = collision_trigger_profile(left, right, collapse_factor=2)
        terminal = collision_trigger_profile(left, right, collapse_factor=1)

        self.assertTrue(coarse.sampled_static_trigger)
        self.assertTrue(coarse.transition_conflict)
        self.assertTrue(response_triggered(coarse, SAMPLED_STATIC))
        self.assertTrue(response_triggered(coarse, TRANSITION_AWARE))

        self.assertFalse(terminal.sampled_static_trigger)
        self.assertTrue(terminal.transition_conflict)
        self.assertFalse(response_triggered(terminal, SAMPLED_STATIC))
        self.assertTrue(response_triggered(terminal, TRANSITION_AWARE))

    def test_static_trigger_extinction_factor_depends_on_policy(self):
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

    def test_same_endpoint_collision_is_visible_to_sampled_static_at_terminal_factor(self):
        left = BodyMotion2D(Body2D(0, -1, 0, 0), (1, 0))
        right = BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0))
        profile = collision_trigger_profile(left, right, collapse_factor=1)
        self.assertFalse(profile.start_macro_contact)
        self.assertTrue(profile.end_macro_contact)
        self.assertTrue(profile.transition_conflict)
        self.assertTrue(response_triggered(profile, SAMPLED_STATIC))

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

    def test_invalid_policy_is_rejected(self):
        left = BodyMotion2D(Body2D(0, 0, 0, 0), (0, 0))
        right = BodyMotion2D(Body2D(1, 5, 0, 0), (0, 0))
        profile = collision_trigger_profile(left, right, 1)
        with self.assertRaises(ValueError):
            response_triggered(profile, "UNKNOWN")


if __name__ == "__main__":
    unittest.main()
