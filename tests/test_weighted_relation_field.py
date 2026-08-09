import itertools
import unittest

from enterprise_math.weighted_relation_field import (
    coarsen_weighted_relation_field,
    merge_weighted_relation_field,
    recover_totals_from_weighted_field,
    split_two_block_totals_from_internal_relation,
    weighted_relation_dimension,
    weighted_relation_field,
    weighted_relation_field_is_closed,
)


class WeightedRelationFieldTests(unittest.TestCase):
    def test_unit_capacities_recover_pairwise_differences(self):
        totals = (3, -1, 4, 2)
        field = weighted_relation_field((1, 1, 1, 1), totals)
        for i in range(len(totals)):
            for j in range(len(totals)):
                self.assertEqual(field[i][j], totals[i] - totals[j])

    def test_generated_fields_are_closed(self):
        capacity_sets = ((1,), (1, 1, 1), (2, 3, 5), (4, 6, 10, 14))
        for capacities in capacity_sets:
            for totals in itertools.product(range(-2, 3), repeat=len(capacities)):
                field = weighted_relation_field(capacities, totals)
                self.assertTrue(weighted_relation_field_is_closed(capacities, field))

    def test_recover_totals_from_field_and_grand_total(self):
        capacity_sets = ((1, 1), (2, 3, 5), (4, 6, 10, 14))
        for capacities in capacity_sets:
            for totals in itertools.product(range(-2, 3), repeat=len(capacities)):
                field = weighted_relation_field(capacities, totals)
                recovered = recover_totals_from_weighted_field(
                    capacities, field, sum(totals)
                )
                self.assertEqual(recovered, totals)

    def test_partition_coarsening_matches_direct_aggregation(self):
        capacities = (2, 3, 5, 7, 11)
        totals = (4, -2, 3, 1, -6)
        field = weighted_relation_field(capacities, totals)
        partitions = (
            ((0, 1), (2, 3, 4)),
            ((0, 2, 4), (1,), (3,)),
            ((0, 1, 2, 3, 4),),
        )
        for partition in partitions:
            new_sizes, new_field = coarsen_weighted_relation_field(
                capacities, field, partition
            )
            new_totals = tuple(sum(totals[index] for index in group) for group in partition)
            self.assertEqual(new_field, weighted_relation_field(new_sizes, new_totals))

    def test_nested_partition_coarsening_is_tree_independent(self):
        capacities = (1, 2, 3, 4, 5, 6)
        totals = (3, -1, 2, 5, -4, 1)
        field = weighted_relation_field(capacities, totals)

        first_partition = ((0, 1), (2, 3), (4, 5))
        first_sizes, first_field = coarsen_weighted_relation_field(
            capacities, field, first_partition
        )
        nested_sizes, nested_field = coarsen_weighted_relation_field(
            first_sizes, first_field, ((0, 1), (2,))
        )

        direct_sizes, direct_field = coarsen_weighted_relation_field(
            capacities, field, ((0, 1, 2, 3), (4, 5))
        )
        self.assertEqual(nested_sizes, direct_sizes)
        self.assertEqual(nested_field, direct_field)

    def test_binary_merge_matches_partition_coarsening(self):
        capacities = (2, 3, 5, 7)
        totals = (4, -1, 2, 6)
        field = weighted_relation_field(capacities, totals)
        new_sizes, merged, discarded = merge_weighted_relation_field(
            capacities, field, 1, 3
        )
        expected_sizes, expected = coarsen_weighted_relation_field(
            capacities, field, ((0,), (2,), (1, 3))
        )
        self.assertEqual(new_sizes, expected_sizes)
        self.assertEqual(merged, expected)
        self.assertEqual(discarded, field[1][3])

    def test_internal_relation_recovers_binary_split(self):
        for left_size, right_size in ((1, 1), (2, 3), (4, 7)):
            for left_total in range(-5, 6):
                for right_total in range(-5, 6):
                    relation = right_size * left_total - left_size * right_total
                    recovered = split_two_block_totals_from_internal_relation(
                        left_size,
                        right_size,
                        left_total + right_total,
                        relation,
                    )
                    self.assertEqual(recovered, (left_total, right_total))

    def test_dimension_is_block_count_minus_one(self):
        for count in range(1, 10):
            self.assertEqual(weighted_relation_dimension((1,) * count), count - 1)


if __name__ == "__main__":
    unittest.main()
