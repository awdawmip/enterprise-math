import unittest

from enterprise_math.scale_tunneling_1d import (
    BodyInterval1D,
    Wall1D,
    interval_wall_clearance,
    minimum_positive_clearance_crossing_displacement,
    sampled_wall_collision_at_factor,
    sampled_wall_transmission_at_factor,
    wall_jump_profile,
)


class ScaleTunneling1DTests(unittest.TestCase):
    def test_point_body_point_wall_has_two_cell_minimum_crossing_displacement(self):
        wall = Wall1D(0, 0)
        profile = wall_jump_profile(wall, start_center=-1, end_center=1, radius=0)
        self.assertTrue(profile.crosses_between_separated_sides)
        self.assertEqual(profile.direction, "LEFT_TO_RIGHT")
        self.assertEqual(profile.start_clearance, 1)
        self.assertEqual(profile.end_clearance, 1)
        self.assertEqual(profile.displacement, 2)
        self.assertEqual(profile.effective_minimum_crossing_displacement, 2)
        self.assertEqual(profile.finest_coarse_collision_factor, 2)
        self.assertEqual(profile.first_transmission_factor, 1)
        self.assertTrue(sampled_wall_collision_at_factor(profile, 2))
        self.assertTrue(sampled_wall_transmission_at_factor(profile, 1))

    def test_wall_thickness_plus_body_diameter_is_exact_minimum(self):
        for thickness in range(1, 6):
            wall = Wall1D(3, 3 + thickness - 1)
            for radius in range(4):
                diameter = 2 * radius + 1
                expected = thickness + diameter
                self.assertEqual(
                    minimum_positive_clearance_crossing_displacement(wall, radius),
                    expected,
                )
                start_center = wall.lo - radius - 1
                end_center = wall.hi + radius + 1
                profile = wall_jump_profile(
                    wall, start_center, end_center, radius
                )
                self.assertEqual(profile.displacement, expected)
                self.assertEqual(profile.start_clearance, 1)
                self.assertEqual(profile.end_clearance, 1)

    def test_general_clearance_identity_is_exact(self):
        wall = Wall1D(-2, 3)
        radius = 2
        minimum = minimum_positive_clearance_crossing_displacement(wall, radius)
        for start_gap in range(1, 5):
            for end_gap in range(1, 5):
                start_center = wall.lo - radius - start_gap
                end_center = wall.hi + radius + end_gap
                profile = wall_jump_profile(
                    wall, start_center, end_center, radius
                )
                self.assertEqual(
                    profile.displacement,
                    minimum + (start_gap - 1) + (end_gap - 1),
                )
                self.assertEqual(profile.start_clearance, start_gap)
                self.assertEqual(profile.end_clearance, end_gap)
                self.assertEqual(
                    profile.minimum_sampled_clearance,
                    min(start_gap, end_gap),
                )

    def test_reverse_crossing_has_same_thresholds(self):
        wall = Wall1D(0, 2)
        forward = wall_jump_profile(wall, -2, 4, radius=1)
        reverse = wall_jump_profile(wall, 4, -2, radius=1)
        self.assertEqual(forward.direction, "LEFT_TO_RIGHT")
        self.assertEqual(reverse.direction, "RIGHT_TO_LEFT")
        self.assertEqual(forward.displacement, reverse.displacement)
        self.assertEqual(
            forward.minimum_sampled_clearance,
            reverse.minimum_sampled_clearance,
        )
        self.assertEqual(
            forward.first_transmission_factor,
            reverse.first_transmission_factor,
        )

    def test_positive_endpoint_clearances_give_exact_collision_to_transmission_switch(self):
        wall = Wall1D(0, 1)
        profile = wall_jump_profile(wall, -4, 5, radius=1)
        self.assertEqual((profile.start_clearance, profile.end_clearance), (3, 3))
        for factor in range(6, 0, -1):
            self.assertEqual(
                sampled_wall_collision_at_factor(profile, factor),
                factor > 3,
            )
            self.assertEqual(
                sampled_wall_transmission_at_factor(profile, factor),
                factor <= 3,
            )

    def test_endpoint_contact_is_not_scale_controllable_tunneling(self):
        wall = Wall1D(0, 2)
        # End body overlaps wall, so refinement cannot turn this sampled state
        # into a positive-clearance separated-side endpoint.
        profile = wall_jump_profile(wall, -1, 1, radius=0)
        self.assertFalse(profile.crosses_between_separated_sides)
        self.assertEqual(profile.end_clearance, 0)
        self.assertIsNone(profile.first_transmission_factor)
        with self.assertRaises(ValueError):
            sampled_wall_collision_at_factor(profile, 2)

    def test_arbitrary_long_jump_is_accepted_as_one_saved_transition(self):
        wall = Wall1D(0, 4)
        profile = wall_jump_profile(wall, -100, 100, radius=0)
        self.assertTrue(profile.crosses_between_separated_sides)
        self.assertEqual(profile.displacement, 200)
        self.assertEqual(profile.start_clearance, 100)
        self.assertEqual(profile.end_clearance, 96)
        self.assertTrue(sampled_wall_transmission_at_factor(profile, 96))
        self.assertTrue(sampled_wall_collision_at_factor(profile, 97))

    def test_clearance_helper_uses_zero_only_for_touch_or_overlap(self):
        wall = Wall1D(0, 2)
        self.assertEqual(interval_wall_clearance(BodyInterval1D(-1, 0), wall), 1)
        self.assertEqual(interval_wall_clearance(BodyInterval1D(3, 0), wall), 1)
        self.assertEqual(interval_wall_clearance(BodyInterval1D(0, 0), wall), 0)
        self.assertEqual(interval_wall_clearance(BodyInterval1D(1, 2), wall), 0)

    def test_invalid_wall_and_radius_are_rejected(self):
        with self.assertRaises(ValueError):
            Wall1D(2, 1)
        with self.assertRaises(ValueError):
            BodyInterval1D(0, -1)
        profile = wall_jump_profile(Wall1D(0, 0), -1, 1, 0)
        with self.assertRaises(ValueError):
            sampled_wall_collision_at_factor(profile, 0)


if __name__ == "__main__":
    unittest.main()
