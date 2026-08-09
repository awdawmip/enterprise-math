import unittest

from enterprise_math.causal_basin_state import (
    advance_amount,
    basin_state,
    basin_widths,
    linear_growth,
    square_growth,
)
from enterprise_math.lattice_geometry import a_ball_count, a_coordinator_shell_count
from enterprise_math.lego_partition_fiber import hidden_allocation_multiplicity


class CausalBasinStateTests(unittest.TestCase):
    def test_linear_growth_recovers_fixed_block_precision(self):
        growth = linear_growth(5, 12)
        self.assertEqual(set(basin_widths(growth)), {5})
        state = basin_state(growth, 17)
        self.assertEqual((state.level, state.complete_value, state.detail), (3, 15, 2))
        self.assertEqual(state.basin_width, 5)
        self.assertEqual(state.remaining_to_next_complete, 3)

        new_state, carry = advance_amount(growth, state, 4)
        self.assertEqual(carry, 1)
        self.assertEqual(new_state.exact_value, 21)
        self.assertEqual((new_state.level, new_state.detail), (4, 1))

    def test_square_growth_has_level_dependent_odd_basin_widths(self):
        growth = square_growth(10)
        self.assertEqual(basin_widths(growth), tuple(2 * level + 1 for level in range(9)))
        state = basin_state(growth, 20)
        self.assertEqual(state.level, 4)
        self.assertEqual(state.complete_value, 16)
        self.assertEqual(state.detail, 4)
        self.assertEqual(state.basin_width, 9)

    def test_generalized_carry_can_cross_multiple_complete_levels(self):
        growth = square_growth(12)
        state = basin_state(growth, 3)  # level 1: 1+2 detail inside [1,4)
        new_state, crossed = advance_amount(growth, state, 30)  # exact 33 -> level 5
        self.assertEqual(new_state.level, 5)
        self.assertEqual(new_state.complete_value, 25)
        self.assertEqual(new_state.detail, 8)
        self.assertEqual(crossed, 4)

    def test_free_lego_growth_basin_capacity_is_lower_rank_fiber(self):
        slots = 4
        growth = tuple(hidden_allocation_multiplicity(slots, total) for total in range(10))
        widths = basin_widths(growth)
        expected = tuple(
            hidden_allocation_multiplicity(slots - 1, total + 1)
            for total in range(9)
        )
        self.assertEqual(widths, expected)

    def test_a_p_ball_growth_basin_capacity_is_next_graph_shell(self):
        for p in range(1, 5):
            growth = tuple(a_ball_count(p, radius) for radius in range(8))
            widths = basin_widths(growth)
            expected = tuple(
                a_coordinator_shell_count(p, radius)
                for radius in range(1, 8)
            )
            self.assertEqual(widths, expected)


if __name__ == "__main__":
    unittest.main()
