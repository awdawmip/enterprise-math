import unittest

from enterprise_math.lego_partition_fiber import (
    allocation_growth_difference_order,
    balanced_minimizer_multiplicity,
    composed_fiber_count,
    coupled_fiber_count_by_total_kernel,
    fiber_composition_identity,
    hidden_allocation_multiplicity,
    one_step_dimension_lowering_identity,
    partition_fiber_multiplicity,
)


class LegoPartitionFiberTests(unittest.TestCase):
    def test_one_unit_remains_one_value_but_has_capacity_many_placements(self):
        for capacity in range(1, 8):
            self.assertEqual(hidden_allocation_multiplicity(capacity, 1), capacity)
            self.assertEqual(balanced_minimizer_multiplicity(capacity, 1), capacity)

    def test_two_slot_fiber_has_c_plus_one_lifts(self):
        for total in range(8):
            self.assertEqual(hidden_allocation_multiplicity(2, total), total + 1)

    def test_three_slot_fiber_matches_exact_integer_sequence(self):
        self.assertEqual(
            tuple(hidden_allocation_multiplicity(3, total) for total in range(5)),
            (1, 3, 6, 10, 15),
        )

    def test_balanced_minimizer_count_only_depends_on_capacity_and_residue(self):
        for total in (1, 4, 7, 10):
            self.assertEqual(balanced_minimizer_multiplicity(3, total), 3)
        for total in (0, 3, 6, 9):
            self.assertEqual(balanced_minimizer_multiplicity(3, total), 1)

    def test_partition_fiber_factorizes_over_independent_coarse_blocks(self):
        capacities = (2, 3)
        totals = (4, 2)
        self.assertEqual(
            partition_fiber_multiplicity(capacities, totals),
            hidden_allocation_multiplicity(2, 4)
            * hidden_allocation_multiplicity(3, 2),
        )
        self.assertEqual(partition_fiber_multiplicity(capacities, totals), 30)

    def test_fiber_composition_generates_sum_product_convolution(self):
        for left_capacity in range(1, 5):
            for right_capacity in range(1, 5):
                for total in range(8):
                    self.assertTrue(
                        fiber_composition_identity(left_capacity, right_capacity, total)
                    )
                    self.assertEqual(
                        composed_fiber_count(left_capacity, right_capacity, total),
                        hidden_allocation_multiplicity(
                            left_capacity + right_capacity,
                            total,
                        ),
                    )

    def test_constant_one_coupling_kernel_recovers_independent_convolution(self):
        total = 5
        kernel = {(left, total - left): 1 for left in range(total + 1)}
        self.assertEqual(
            coupled_fiber_count_by_total_kernel(2, 3, total, kernel),
            composed_fiber_count(2, 3, total),
        )

    def test_zero_one_kernel_is_support_constrained_convolution(self):
        total = 4
        kernel = {
            (left, total - left): int(left % 2 == 0)
            for left in range(total + 1)
        }
        expected = sum(
            hidden_allocation_multiplicity(2, left)
            * hidden_allocation_multiplicity(2, total - left)
            for left in range(total + 1)
            if left % 2 == 0
        )
        self.assertEqual(coupled_fiber_count_by_total_kernel(2, 2, total, kernel), expected)

    def test_multiplicity_kernel_counts_multiple_joint_states_over_one_split(self):
        total = 3
        kernel = {(left, total - left): 1 for left in range(total + 1)}
        kernel[(1, 2)] = 3
        independent = composed_fiber_count(1, 1, total)
        extra = 2 * hidden_allocation_multiplicity(1, 1) * hidden_allocation_multiplicity(1, 2)
        self.assertEqual(
            coupled_fiber_count_by_total_kernel(1, 1, total, kernel),
            independent + extra,
        )

    def test_one_integer_difference_strips_one_hidden_slot_freedom(self):
        for capacity in range(2, 7):
            for total in range(8):
                self.assertTrue(one_step_dimension_lowering_identity(capacity, total))

    def test_hidden_relation_count_equals_finite_difference_growth_order(self):
        for capacity in range(1, 7):
            self.assertEqual(allocation_growth_difference_order(capacity), capacity - 1)


if __name__ == "__main__":
    unittest.main()
