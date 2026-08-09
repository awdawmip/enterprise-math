import unittest
from math import comb

from enterprise_math.causal_basin_revelation import (
    budgeted_revelation_spectrum,
    revelation_telescopes_to_original_collision,
    unit_revelation_collision_coordinate,
    unit_revelation_increment,
    unit_revelation_increment_from_difference,
    unit_revelation_partition_sizes,
)


class CausalBasinRevelationTests(unittest.TestCase):
    def test_partition_is_one_shrinking_block_plus_revealed_singletons(self):
        width = 7
        self.assertEqual(unit_revelation_partition_sizes(width, 0), (7,))
        self.assertEqual(unit_revelation_partition_sizes(width, 1), (6, 1))
        self.assertEqual(unit_revelation_partition_sizes(width, 4), (3, 1, 1, 1, 1))
        self.assertEqual(unit_revelation_partition_sizes(width, 6), (1, 1, 1, 1, 1, 1, 1))

    def test_collision_coordinate_is_pascal_block_formula(self):
        width = 8
        for steps in range(width):
            for order in range(2, 6):
                expected = comb(width - steps, order) if width - steps >= order else 0
                self.assertEqual(
                    unit_revelation_collision_coordinate(width, steps, order),
                    expected,
                )

    def test_each_revelation_increment_is_pascal_difference(self):
        width = 9
        for step in range(1, width):
            for order in range(2, 7):
                expected = comb(width - step, order - 1) if width - step >= order - 1 else 0
                self.assertEqual(unit_revelation_increment(width, step, order), expected)
                self.assertEqual(
                    unit_revelation_increment(width, step, order),
                    unit_revelation_increment_from_difference(width, step, order),
                )

    def test_total_revelation_exactly_exhausts_original_collision_spectrum(self):
        for width in range(1, 11):
            for order in range(2, 8):
                self.assertTrue(
                    revelation_telescopes_to_original_collision(width, order)
                )

    def test_unit_cost_places_pascal_releases_at_exact_budget_multiples(self):
        width = 5
        unit_cost = 3
        spectrum = budgeted_revelation_spectrum(
            width,
            unit_cost,
            maximum_budget=15,
            maximum_order=3,
        )
        # Pair releases are w-t at budgets 3,6,9,12.
        self.assertEqual(spectrum[2][1], 4)
        self.assertEqual(spectrum[5][1], 3)
        self.assertEqual(spectrum[8][1], 2)
        self.assertEqual(spectrum[11][1], 1)
        self.assertTrue(
            all(
                row == (0, 0, 0)
                for budget, row in enumerate(spectrum, start=1)
                if budget not in (3, 6, 9, 12)
            )
        )

    def test_j1_never_reveals_because_state_count_is_conserved(self):
        spectrum = budgeted_revelation_spectrum(
            width=6,
            unit_cost=2,
            maximum_budget=12,
            maximum_order=4,
        )
        self.assertTrue(all(row[0] == 0 for row in spectrum))


if __name__ == "__main__":
    unittest.main()
