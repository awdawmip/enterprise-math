import unittest
from fractions import Fraction

from enterprise_math.causal_root_two_cover import (
    a_two_cover_profile,
    d_two_cover_profile,
    e_two_cover_profile,
)


class CausalRootTwoCoverTests(unittest.TestCase):
    def test_a_family_has_trivial_loop_return(self):
        for rank in range(2, 9):
            profile = a_two_cover_profile(rank)
            self.assertEqual(profile.return_flipping_triangles, 0)
            self.assertFalse(profile.has_nontrivial_loop_return)

    def test_d_family_closed_form(self):
        expected = {
            4: (4, 0, 4, Fraction(1, 1)),
            5: (6, 8, 12, Fraction(3, 5)),
            6: (8, 32, 24, Fraction(3, 7)),
            7: (10, 80, 40, Fraction(1, 3)),
            8: (12, 160, 60, Fraction(3, 11)),
        }
        for rank, values in expected.items():
            profile = d_two_cover_profile(rank)
            self.assertEqual(
                (
                    profile.base_vertices,
                    profile.return_preserving_triangles,
                    profile.return_flipping_triangles,
                    profile.flipping_fraction,
                ),
                values,
            )
            self.assertTrue(profile.has_nontrivial_loop_return)

    def test_exceptional_family_counts(self):
        expected = {
            6: (10, 60, 60, Fraction(1, 2)),
            7: (16, 320, 240, Fraction(3, 7)),
            8: (28, 2016, 1260, Fraction(5, 13)),
        }
        for rank, values in expected.items():
            profile = e_two_cover_profile(rank)
            self.assertEqual(
                (
                    profile.base_vertices,
                    profile.return_preserving_triangles,
                    profile.return_flipping_triangles,
                    profile.flipping_fraction,
                ),
                values,
            )
            self.assertTrue(profile.has_nontrivial_loop_return)


if __name__ == "__main__":
    unittest.main()
