import unittest

from enterprise_math.causal_bulk_capacity import (
    additive_bulk_capacity_violation,
    additive_bulk_state_bound,
    first_binary_copy_additive_bulk_violation,
    nontrivial_bulk_channel_count,
)


class CausalBulkCapacityTests(unittest.TestCase):
    def test_one_additive_bulk_channel_gives_linear_state_bound(self):
        # One structural type and one 0/1 increment channel: d+1 states.
        self.assertEqual(
            tuple(additive_bulk_state_bound(1, (1,), depth) for depth in range(6)),
            (1, 2, 3, 4, 5, 6),
        )

    def test_two_nontrivial_bulk_channels_give_quadratic_bound(self):
        for depth in range(6):
            self.assertEqual(
                additive_bulk_state_bound(3, (1, 2), depth),
                3 * (depth + 1) * (2 * depth + 1),
            )
        self.assertEqual(nontrivial_bulk_channel_count((1, 2)), 2)

    def test_zero_width_bulk_channel_does_not_raise_growth_degree(self):
        self.assertEqual(nontrivial_bulk_channel_count((1, 0, 3, 0)), 2)
        for depth in range(5):
            self.assertEqual(
                additive_bulk_state_bound(2, (1, 0), depth),
                2 * (depth + 1),
            )

    def test_copy_constraint_eventually_beats_any_fixed_tested_additive_schema(self):
        schemas = (
            (1, (1,)),
            (2, (1,)),
            (4, (1, 1)),
            (8, (2, 3)),
            (16, (1, 1, 1)),
        )
        for type_count, widths in schemas:
            violation = first_binary_copy_additive_bulk_violation(
                type_count,
                widths,
                40,
            )
            self.assertIsNotNone(violation)
            depth = violation
            self.assertTrue(
                additive_bulk_capacity_violation(
                    2**depth,
                    type_count,
                    widths,
                    depth,
                )
            )

    def test_parity_two_state_task_fits_finite_structure_without_bulk_growth(self):
        for depth in range(1, 20):
            self.assertFalse(
                additive_bulk_capacity_violation(2, 2, (), depth)
            )
            self.assertEqual(additive_bulk_state_bound(2, (), depth), 2)


if __name__ == "__main__":
    unittest.main()
