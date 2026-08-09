import unittest

from enterprise_math.causal_basin_dimension import (
    a_p_ball_basin_width,
    basin_growth_degree,
    basin_widths,
    expected_dimension_lowering,
    free_lego_basin_width,
)
from enterprise_math.lattice_geometry import a_ball_count, a_coordinator_shell_count
from enterprise_math.lego_partition_fiber import hidden_allocation_multiplicity


class CausalBasinDimensionTests(unittest.TestCase):
    def test_square_completion_basins_have_linear_width(self):
        growth = tuple(level * level for level in range(10))
        self.assertEqual(basin_widths(growth), tuple(2 * level + 1 for level in range(9)))
        self.assertEqual(basin_growth_degree(growth), 1)
        self.assertTrue(expected_dimension_lowering(growth, 2))

    def test_free_lego_basin_is_exact_lower_slot_fiber(self):
        for slots in range(2, 7):
            for total in range(8):
                width = free_lego_basin_width(slots, total)
                self.assertEqual(
                    width,
                    hidden_allocation_multiplicity(slots - 1, total + 1),
                )

    def test_a_p_complete_ball_basin_is_exact_shell(self):
        for p in range(1, 5):
            for radius in range(1, 6):
                self.assertEqual(
                    a_p_ball_basin_width(p, radius),
                    a_coordinator_shell_count(p, radius),
                )
                self.assertEqual(
                    a_ball_count(p, radius) - a_ball_count(p, radius - 1),
                    a_coordinator_shell_count(p, radius),
                )

    def test_a_p_ball_growth_lowers_from_degree_p_to_p_minus_one(self):
        for p in range(1, 5):
            growth = tuple(a_ball_count(p, radius) for radius in range(2 * p + 7))
            self.assertTrue(expected_dimension_lowering(growth, p))

    def test_plateau_growth_is_not_a_valid_exact_level_scale_for_this_theorem(self):
        with self.assertRaises(ValueError):
            basin_widths((1, 2, 2, 5))


if __name__ == "__main__":
    unittest.main()
