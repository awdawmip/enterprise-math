import itertools
import unittest

from enterprise_math.weighted_relation_field import (
    merge_weighted_relation_field,
    recover_totals_from_weighted_field,
    split_two_block_totals_from_internal_relation,
    weighted_relation_dimension,
    weighted_relation_field,
    weighted_relation_field_is_closed,
)


class WeightedRelationFieldTests(unittest.TestCase):
    def test_weighted_field_closure_and_recovery(self):
        size_sets = ((1,), (1, 1), (2, 1, 3), (2, 2, 1, 4))
        for block_sizes in size_sets:
            for totals in itertools.product(range(-3, 4), repeat=len(block_sizes)):
                field = weighted_relation_field(block_sizes, totals)
                self.assertTrue(weighted_relation_field_is_closed(block_sizes, field))
                self.assertEqual(
                    recover_totals_from_weighted_field(
                        block_sizes, field, sum(totals)
                    ),
                    totals,
                )
                self.assertEqual(
                    weighted_relation_dimension(block_sizes),
                    len(block_sizes) - 1,
                )

    def test_unit_capacity_field_is_ordinary_difference_field(self):
        for size in range(1, 7):
            block_sizes = (1,) * size
            for totals in itertools.product(range(-2, 3), repeat=size):
                field = weighted_relation_field(block_sizes, totals)
                expected = tuple(
                    tuple(totals[i] - totals[j] for j in range(size))
                    for i in range(size)
                )
                self.assertEqual(field, expected)

    def test_merge_adds_external_relation_rows_and_discards_internal_relation(self):
        block_sizes = (2, 1, 3, 2)
        for totals in itertools.product(range(-3, 4), repeat=4):
            field = weighted_relation_field(block_sizes, totals)
            new_sizes, new_field, discarded = merge_weighted_relation_field(
                block_sizes, field, 0, 2
            )
            new_totals = (totals[1], totals[3], totals[0] + totals[2])
            self.assertEqual(new_sizes, (1, 2, 5))
            self.assertEqual(new_field, weighted_relation_field(new_sizes, new_totals))
            self.assertEqual(discarded, field[0][2])
            self.assertEqual(new_field[2][0], field[0][1] + field[2][1])
            self.assertEqual(new_field[2][1], field[0][3] + field[2][3])

    def test_internal_relation_exactly_reverses_two_block_total_merge(self):
        for left_size in range(1, 6):
            for right_size in range(1, 6):
                for left_total in range(-8, 9):
                    for right_total in range(-8, 9):
                        internal = (
                            right_size * left_total
                            - left_size * right_total
                        )
                        recovered = split_two_block_totals_from_internal_relation(
                            left_size,
                            right_size,
                            left_total + right_total,
                            internal,
                        )
                        self.assertEqual(recovered, (left_total, right_total))

    def test_each_merge_reduces_relation_dimension_by_one(self):
        block_sizes = (1, 1, 1, 1, 1)
        totals = (3, -1, 4, -2, -4)
        field = weighted_relation_field(block_sizes, totals)
        dimension = weighted_relation_dimension(block_sizes)
        while len(block_sizes) > 1:
            block_sizes, field, _ = merge_weighted_relation_field(
                block_sizes, field, 0, 1
            )
            self.assertEqual(
                weighted_relation_dimension(block_sizes),
                dimension - 1,
            )
            dimension -= 1


if __name__ == "__main__":
    unittest.main()
