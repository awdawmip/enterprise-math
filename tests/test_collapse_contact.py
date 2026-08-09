import unittest

from enterprise_math.collapse_contact import collapse_contact_profile
from enterprise_math.engineering_collision import Body2D


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

    def test_deep_overlap_has_larger_integer_separation_certificate(self):
        left = Body2D(0, 0, 0, 2)
        right = Body2D(1, 2, 1, 2)
        profile = collapse_contact_profile(left, right)
        self.assertIsNotNone(profile)
        self.assertEqual((profile.x_count, profile.y_count), (3, 4))
        self.assertEqual(profile.shared_target_count, 12)
        self.assertEqual(profile.minimum_axis_separation_steps, 3)
        self.assertEqual(profile.minimum_axes, ("x",))

    def test_separate_bodies_have_no_contact_profile(self):
        self.assertIsNone(
            collapse_contact_profile(Body2D(0, 0, 0, 1), Body2D(1, 5, 0, 1))
        )

    def test_same_id_is_rejected(self):
        with self.assertRaises(ValueError):
            collapse_contact_profile(Body2D(0, 0, 0, 1), Body2D(0, 1, 0, 1))


if __name__ == "__main__":
    unittest.main()
