import unittest
from fractions import Fraction

from enterprise_math.precision_grid_distance_spectrum import (
    axis_ordered_distance_spectrum,
    grid_ordered_distance_spectrum,
    grid_unordered_distance_spectrum,
    grid_unordered_pair_count,
    grid_vertex_count,
    grid_zero_overlap_pair_count,
    grid_zero_overlap_pair_fraction,
    uniform_cube_zero_overlap_fraction,
)


class PrecisionGridDistanceSpectrumTests(unittest.TestCase):
    def test_one_axis_spectrum_recovers_path_pair_counts(self):
        self.assertEqual(axis_ordered_distance_spectrum(4), (4, 6, 4, 2))
        self.assertEqual(grid_unordered_distance_spectrum((4,)), (0, 3, 2, 1))
        self.assertEqual(grid_unordered_pair_count((4,)), 6)

    def test_two_by_two_grid_spectrum_is_exact_polynomial_square(self):
        self.assertEqual(grid_ordered_distance_spectrum((2, 2)), (4, 8, 4))
        self.assertEqual(grid_unordered_distance_spectrum((2, 2)), (0, 4, 2))
        self.assertEqual(grid_vertex_count((2, 2)), 4)
        self.assertEqual(grid_unordered_pair_count((2, 2)), 6)

    def test_binary_cube_spectrum_is_exact(self):
        self.assertEqual(grid_ordered_distance_spectrum((2, 2, 2)), (8, 24, 24, 8))
        self.assertEqual(grid_unordered_distance_spectrum((2, 2, 2)), (0, 12, 12, 4))
        self.assertEqual(grid_zero_overlap_pair_count((2, 2, 2), 2), 16)
        self.assertEqual(grid_zero_overlap_pair_fraction((2, 2, 2), 2), Fraction(4, 7))

    def test_three_dimensional_isotropic_grid_macro_fraction_grows_at_fixed_resolution(self):
        fractions = tuple(
            uniform_cube_zero_overlap_fraction(side, 3, 2)
            for side in (1, 2, 3, 4, 5)
        )
        self.assertEqual(
            fractions,
            (
                Fraction(0, 1),
                Fraction(4, 7),
                Fraction(11, 13),
                Fraction(13, 14),
                Fraction(149, 155),
            ),
        )
        self.assertEqual(tuple(sorted(fractions)), fractions)

    def test_distance_spectrum_counts_all_ordered_pairs(self):
        for sides in ((3,), (2, 3), (2, 3, 4), (3, 3, 3)):
            ordered = grid_ordered_distance_spectrum(sides)
            vertices = grid_vertex_count(sides)
            self.assertEqual(sum(ordered), vertices * vertices)
            self.assertEqual(ordered[0], vertices)
            self.assertEqual(
                sum(grid_unordered_distance_spectrum(sides)),
                vertices * (vertices - 1) // 2,
            )

    def test_record_resolution_beyond_diameter_has_no_zero_overlap_pairs(self):
        self.assertEqual(grid_zero_overlap_pair_count((3, 3), 5), 0)
        self.assertEqual(grid_zero_overlap_pair_fraction((1,), 1), 0)

    def test_invalid_inputs_fail_closed(self):
        with self.assertRaises(ValueError):
            grid_ordered_distance_spectrum(())
        with self.assertRaises(ValueError):
            grid_zero_overlap_pair_count((2, 2), 0)
        with self.assertRaises(ValueError):
            uniform_cube_zero_overlap_fraction(2, 0, 1)


if __name__ == "__main__":
    unittest.main()
