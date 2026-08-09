import unittest

from enterprise_math.causal_locality_capacity import (
    capacity_violation,
    first_binary_copy_violation,
    fixed_local_grade_state_bound,
)


class CausalLocalityCapacityTests(unittest.TestCase):
    def test_bound_counts_bulk_range_times_suffix_memory(self):
        # Binary alphabet, q=3, depth=6: four completed windows, grade range width 5,
        # four suffix states -> 4*(4*5+1)=84 raw states suffice.
        self.assertEqual(fixed_local_grade_state_bound(2, 3, 6, -2, 3), 84)

    def test_before_first_complete_window_only_prefix_memory_is_needed(self):
        self.assertEqual(fixed_local_grade_state_bound(3, 5, 0, 0, 7), 1)
        self.assertEqual(fixed_local_grade_state_bound(3, 5, 2, 0, 7), 9)
        self.assertEqual(fixed_local_grade_state_bound(3, 5, 3, 0, 7), 27)

    def test_copy_constraint_eventually_beats_any_fixed_small_local_grade_schema(self):
        for window, grade_min, grade_max in (
            (2, 0, 1),
            (3, -1, 2),
            (5, -3, 4),
        ):
            violation = first_binary_copy_violation(
                window,
                grade_min,
                grade_max,
                30,
            )
            self.assertIsNotNone(violation)
            n = violation
            self.assertTrue(
                capacity_violation(
                    2**n,
                    2,
                    window,
                    n,
                    grade_min,
                    grade_max,
                )
            )

    def test_parity_two_state_requirement_stays_below_local_capacity(self):
        for depth in range(1, 12):
            self.assertFalse(
                capacity_violation(
                    2,
                    2,
                    2,
                    depth,
                    0,
                    1,
                )
            )

    def test_zero_width_grade_does_not_create_fake_bulk_capacity(self):
        # If every local grade is identical, accumulated grade has only one value;
        # only suffix memory remains.
        self.assertEqual(fixed_local_grade_state_bound(2, 4, 10, 7, 7), 8)


if __name__ == "__main__":
    unittest.main()
