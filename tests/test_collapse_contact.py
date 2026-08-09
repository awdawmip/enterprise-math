import unittest

from enterprise_math.collapse_contact import collapse_contact_profile
from enterprise_math.common_collapse import common_collapse_collision
from enterprise_math.engineering_collision import Body2D


def moved(body, delta):
    return Body2D(body.body_id, body.x + delta[0], body.y + delta[1], body.radius)


class CollapseContactTests(unittest.TestCase):
    def test_point_contact_has_one_shared_target(self):
        left = Body2D(0, 0, 0, 1)
        right = Body2D(1, 2, 2, 1)
        profile = collapse_contact_profile(left, right)
        self.assertIsNotNone(profile)
        self.assertEqual(profile.x_count, 1)
        self.assertEqual(profile.y_count, 1)
        self.assertEqual(profile.shared_target_count, 1)
        self.assertEqual(profile.minimum_axis_separation_steps, 1)
        self.assertEqual(profile.minimum_axes, ("x", "y"))
        self.assertEqual(
            set(profile.minimum_relative_corrections),
            {(1, 0), (0, 1)},
        )
        self.assertEqual(profile.witness, (1, 1))

    def test_edge_like_contact_retains_axis_extent(self):
        left = Body2D(0, 0, 0, 1)
        right = Body2D(1, 2, 0, 1)
        profile = collapse_contact_profile(left, right)
        self.assertIsNotNone(profile)
        self.assertEqual((profile.x_count, profile.y_count), (1, 3))
        self.assertEqual(profile.shared_target_count, 3)
        self.assertEqual(profile.minimum_axis_separation_steps, 1)
        self.assertEqual(profile.minimum_axes, ("x",))
        self.assertEqual(profile.minimum_relative_corrections, ((1, 0),))

    def test_deep_overlap_has_larger_integer_separation_certificate(self):
        left = Body2D(0, 0, 0, 2)
        right = Body2D(1, 2, 1, 2)
        profile = collapse_contact_profile(left, right)
        self.assertIsNotNone(profile)
        self.assertEqual((profile.x_count, profile.y_count), (3, 4))
        self.assertEqual(profile.shared_target_count, 12)
        self.assertEqual(profile.minimum_axis_separation_steps, 3)
        self.assertEqual(profile.minimum_axes, ("x",))
        self.assertEqual(profile.minimum_relative_corrections, ((3, 0),))

    def test_containment_separates_overlap_width_from_response_distance(self):
        outer = Body2D(0, 0, 0, 5)
        inner = Body2D(1, 0, 0, 1)
        profile = collapse_contact_profile(outer, inner)
        self.assertIsNotNone(profile)
        self.assertEqual((profile.x_count, profile.y_count), (3, 3))
        self.assertEqual(profile.shared_target_count, 9)
        self.assertEqual(profile.x_signed_separations, (-7, 7))
        self.assertEqual(profile.y_signed_separations, (-7, 7))
        self.assertEqual(profile.minimum_axis_separation_steps, 7)
        self.assertEqual(profile.minimum_axes, ("x", "y"))
        self.assertEqual(
            set(profile.minimum_relative_corrections),
            {(-7, 0), (7, 0), (0, -7), (0, 7)},
        )

    def test_every_reported_minimum_correction_really_separates(self):
        bodies = [
            Body2D(body_id, x, y, radius)
            for body_id, (x, y, radius) in enumerate(
                (
                    (-3, 0, 2),
                    (0, 0, 5),
                    (1, 1, 1),
                    (4, -2, 3),
                    (8, 8, 0),
                )
            )
        ]
        for left_index, left in enumerate(bodies):
            for right in bodies[left_index + 1 :]:
                profile = collapse_contact_profile(left, right)
                if profile is None:
                    continue
                for correction in profile.minimum_relative_corrections:
                    self.assertFalse(
                        common_collapse_collision(left, moved(right, correction)),
                        (left, right, correction),
                    )

    def test_small_domain_minimum_is_globally_l1_minimal(self):
        body_id = 0
        bodies = []
        for x in range(-2, 3, 2):
            for y in range(-2, 3, 2):
                for radius in range(3):
                    bodies.append(Body2D(body_id, x, y, radius))
                    body_id += 1

        for left_index, left in enumerate(bodies):
            for right in bodies[left_index + 1 :]:
                profile = collapse_contact_profile(left, right)
                if profile is None:
                    continue
                minimum = profile.minimum_axis_separation_steps
                for dx in range(-minimum + 1, minimum):
                    for dy in range(-minimum + 1, minimum):
                        if abs(dx) + abs(dy) >= minimum:
                            continue
                        self.assertTrue(
                            common_collapse_collision(left, moved(right, (dx, dy))),
                            (left, right, minimum, dx, dy),
                        )

    def test_relative_corrections_are_swap_equivariant(self):
        left = Body2D(0, -2, 3, 4)
        right = Body2D(1, 1, 2, 1)
        forward = collapse_contact_profile(left, right)
        reverse = collapse_contact_profile(right, left)
        self.assertIsNotNone(forward)
        self.assertIsNotNone(reverse)
        self.assertEqual(
            set(reverse.minimum_relative_corrections),
            {(-dx, -dy) for dx, dy in forward.minimum_relative_corrections},
        )

    def test_translation_changes_witness_location_not_contact_cost(self):
        left = Body2D(0, -1, 2, 3)
        right = Body2D(1, 2, 3, 2)
        base = collapse_contact_profile(left, right)
        shifted = collapse_contact_profile(
            Body2D(0, left.x + 19, left.y - 11, left.radius),
            Body2D(1, right.x + 19, right.y - 11, right.radius),
        )
        self.assertIsNotNone(base)
        self.assertIsNotNone(shifted)
        self.assertEqual(base.x_count, shifted.x_count)
        self.assertEqual(base.y_count, shifted.y_count)
        self.assertEqual(base.minimum_axis_separation_steps, shifted.minimum_axis_separation_steps)
        self.assertEqual(base.minimum_relative_corrections, shifted.minimum_relative_corrections)
        self.assertEqual(
            shifted.witness,
            (base.witness[0] + 19, base.witness[1] - 11),
        )

    def test_separate_bodies_have_no_contact_profile(self):
        self.assertIsNone(
            collapse_contact_profile(Body2D(0, 0, 0, 1), Body2D(1, 5, 0, 1))
        )

    def test_same_id_is_rejected(self):
        with self.assertRaises(ValueError):
            collapse_contact_profile(Body2D(0, 0, 0, 1), Body2D(0, 1, 0, 1))


if __name__ == "__main__":
    unittest.main()
