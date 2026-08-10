import unittest
from fractions import Fraction

from enterprise_math.precision_geometric_record import (
    grid_geometric_record_overlap,
    grid_representative_visibility_region_excluded,
    overlap_from_distance,
    path_geometric_record_overlap,
    path_positive_overlap_pair_count,
    path_representative_visibility_region_excluded,
    path_zero_overlap_fraction_monotone_step,
    path_zero_overlap_pair_count,
    path_zero_overlap_pair_fraction,
    unordered_pair_count,
)


class PrecisionGeometricRecordTests(unittest.TestCase):
    def test_path_overlap_is_derived_from_intrinsic_integer_distance(self):
        scales = (1, 2, 4, 8)
        self.assertEqual(path_geometric_record_overlap(1, 4, scales, 10), Fraction(7, 10))
        self.assertEqual(path_geometric_record_overlap(0, 7, scales, 10), Fraction(3, 10))
        self.assertEqual(path_geometric_record_overlap(2, 5, scales, 3), 0)

    def test_grid_overlap_is_derived_from_l1_distance(self):
        axes = ((1, 2, 4), (1, 2, 4))
        self.assertEqual(grid_geometric_record_overlap((0, 0), (3, 3), axes, 10), Fraction(2, 5))
        self.assertEqual(grid_geometric_record_overlap((1, 1), (2, 3), axes, 10), Fraction(7, 10))

    def test_equal_graph_distance_forces_equal_toy_overlap(self):
        self.assertEqual(overlap_from_distance(4, 10), Fraction(3, 5))
        self.assertEqual(
            path_geometric_record_overlap(0, 4, (1, 2, 4, 8), 10),
            overlap_from_distance(4, 10),
        )
        cube_axes = ((1, 2),) * 4
        self.assertEqual(
            grid_geometric_record_overlap((0, 0, 0, 0), (1, 1, 1, 1), cube_axes, 10),
            overlap_from_distance(4, 10),
        )

    def test_same_capacity_different_geometry_gives_different_record_prediction(self):
        # All three examples have 16 fine states but different intrinsic diameters.
        path_eta = path_geometric_record_overlap(0, 15, (1, 2, 4, 8, 16), 10)
        square_eta = grid_geometric_record_overlap(
            (0, 0), (3, 3), ((1, 2, 4), (1, 2, 4)), 10
        )
        cube_eta = grid_geometric_record_overlap(
            (0, 0, 0, 0), (1, 1, 1, 1), ((1, 2),) * 4, 10
        )
        self.assertEqual((path_eta, square_eta, cube_eta), (0, Fraction(2, 5), Fraction(3, 5)))

    def test_visibility_exclusion_is_now_geometric_cross_product(self):
        self.assertFalse(path_representative_visibility_region_excluded(0, 9, (1, 2, 5, 10), 10))
        self.assertTrue(path_representative_visibility_region_excluded(0, 10, (1, 2, 5, 10, 20), 10))
        axes = ((1, 2, 4), (1, 2, 4))
        self.assertFalse(grid_representative_visibility_region_excluded((0, 0), (3, 3), axes, 10))

    def test_path_zero_overlap_pair_count_has_exact_triangular_formula(self):
        self.assertEqual(unordered_pair_count(8), 28)
        self.assertEqual(path_zero_overlap_pair_count(8, 3), 15)
        self.assertEqual(path_positive_overlap_pair_count(8, 3), 13)
        self.assertEqual(path_zero_overlap_pair_fraction(8, 3), Fraction(15, 28))
        self.assertEqual(path_zero_overlap_pair_count(3, 3), 0)
        self.assertEqual(path_zero_overlap_pair_count(2, 5), 0)
        self.assertEqual(path_zero_overlap_pair_count(8, 1), 28)

    def test_fixed_record_resolution_gives_monotone_finite_macro_crossover(self):
        for record_resolution in range(1, 8):
            fractions = tuple(
                path_zero_overlap_pair_fraction(size, record_resolution)
                for size in range(1, 25)
            )
            self.assertEqual(tuple(sorted(fractions)), fractions)
            for size in range(1, 24):
                self.assertTrue(
                    path_zero_overlap_fraction_monotone_step(size, record_resolution)
                )

        self.assertEqual(
            tuple(path_zero_overlap_pair_fraction(size, 3) for size in (3, 4, 5, 8, 16)),
            (Fraction(0, 1), Fraction(1, 6), Fraction(3, 10), Fraction(15, 28), Fraction(91, 120)),
        )


if __name__ == "__main__":
    unittest.main()
