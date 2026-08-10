import unittest

from enterprise_math.precision_a3_padic_exterior_target import (
    exterior_integer_smith_profile,
    exterior_padic_profile,
    guard_image_exponent_profile,
    projective_agreement_depth,
    projective_defect_distance,
    row_defect_exponent_profile,
)


class A3PadicExteriorTargetTests(unittest.TestCase):
    def test_exterior_integer_smith_profile(self):
        self.assertEqual(exterior_integer_smith_profile((6, 10, 14)), (2, 2))
        self.assertEqual(exterior_integer_smith_profile((3, 6, 9, 12)), (3, 3, 3))

    def test_exterior_padic_profile_tracks_common_content(self):
        self.assertEqual(exterior_padic_profile((2, 6, 10), 2, 4), (3, 3))
        self.assertEqual(exterior_padic_profile((1, 3, 5), 2, 4), (4, 4))

    def test_projective_defect_distance(self):
        u = (1, 0)
        v = (1, 4)
        self.assertEqual(projective_agreement_depth(u, v, 2, 4), 2)
        self.assertEqual(projective_defect_distance(u, v, 2, 4), 2)

    def test_projective_distance_is_ultrametric_on_example(self):
        u = (1, 0)
        v = (1, 4)
        w = (1, 12)
        duv = projective_defect_distance(u, v, 2, 4)
        dvw = projective_defect_distance(v, w, 2, 4)
        duw = projective_defect_distance(u, w, 2, 4)
        self.assertLessEqual(duw, max(duv, dvw))

    def test_guard_image_and_row_defect_profiles_match(self):
        A = ((1, 1, 0),)
        W = ((0, 1, 1),)
        self.assertEqual(
            guard_image_exponent_profile(A, W, 2, 2),
            row_defect_exponent_profile(A, W, 2, 2),
        )

    def test_equal_exponent_profiles_do_not_identify_direction(self):
        u = (1, 0)
        v = (1, 2)
        self.assertEqual(exterior_padic_profile(u, 2, 3), exterior_padic_profile(v, 2, 3))
        self.assertGreater(projective_defect_distance(u, v, 2, 3), 0)


if __name__ == "__main__":
    unittest.main()
