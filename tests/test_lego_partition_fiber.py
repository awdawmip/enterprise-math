import unittest

from enterprise_math.lego_partition_fiber import (
    allocation_growth_difference_order,
    hidden_allocation_multiplicity,
    partition_fiber_multiplicity,
)


class LegoPartitionFiberTests(unittest.TestCase):
    def test_one_unit_remains_one_value_but_has_capacity_many_placements(self):
        for capacity in range(1, 8):
            self.assertEqual(hidden_allocation_multiplicity(capacity, 1), capacity)

    def test_two_slot_fiber_has_c_plus_one_lifts(self):
        for total in range(8):
            self.assertEqual(hidden_allocation_multiplicity(2, total), total + 1)

    def test_three_slot_fiber_matches_exact_integer_sequence(self):
        # C(c+2,2): 1,3,6,10,15,...
        self.assertEqual(
            tuple(hidden_allocation_multiplicity(3, total) for total in range(5)),
            (1, 3, 6, 10, 15),
        )

    def test_partition_fiber_factorizes_over_independent_coarse_blocks(self):
        capacities = (2, 3)
        totals = (4, 2)
        self.assertEqual(
            partition_fiber_multiplicity(capacities, totals),
            hidden_allocation_multiplicity(2, 4)
            * hidden_allocation_multiplicity(3, 2),
        )
        self.assertEqual(partition_fiber_multiplicity(capacities, totals), 30)

    def test_hidden_relation_count_equals_finite_difference_growth_order(self):
        for capacity in range(1, 7):
            self.assertEqual(allocation_growth_difference_order(capacity), capacity - 1)


if __name__ == "__main__":
    unittest.main()
