import unittest

from enterprise_math.weighted_relation_field import (
    coarsen_weighted_relation_field,
    weighted_relation_field,
)


class RelationErasureTests(unittest.TestCase):
    def test_deleted_internal_relation_is_invisible_to_all_future_coarsenings(self):
        block_sizes = (1, 1, 1, 1)
        left_fine = (1, -1, 2, -2)
        right_fine = (2, -2, 2, -2)
        left_field = weighted_relation_field(block_sizes, left_fine)
        right_field = weighted_relation_field(block_sizes, right_fine)
        self.assertNotEqual(left_field[0][1], right_field[0][1])

        current_partition = ((0, 1), (2,), (3,))
        left_sizes, left_coarse = coarsen_weighted_relation_field(
            block_sizes, left_field, current_partition
        )
        right_sizes, right_coarse = coarsen_weighted_relation_field(
            block_sizes, right_field, current_partition
        )
        self.assertEqual(left_sizes, right_sizes)
        self.assertEqual(left_coarse, right_coarse)

        # Every tested future operation is a further partition coarsening.
        future_partitions = (
            ((0, 1), (2,)),
            ((0,), (1, 2)),
            ((0, 1, 2),),
        )
        for future_partition in future_partitions:
            self.assertEqual(
                coarsen_weighted_relation_field(
                    left_sizes, left_coarse, future_partition
                ),
                coarsen_weighted_relation_field(
                    right_sizes, right_coarse, future_partition
                ),
            )

    def test_refinement_can_reveal_the_deleted_relation_immediately(self):
        block_sizes = (1, 1, 1)
        left_fine = (1, -1, 0)
        right_fine = (2, -2, 0)
        left_field = weighted_relation_field(block_sizes, left_fine)
        right_field = weighted_relation_field(block_sizes, right_fine)

        current_partition = ((0, 1), (2,))
        _, left_coarse = coarsen_weighted_relation_field(
            block_sizes, left_field, current_partition
        )
        _, right_coarse = coarsen_weighted_relation_field(
            block_sizes, right_field, current_partition
        )
        self.assertEqual(left_coarse, right_coarse)

        # Refining the first coarse block back to unit slots reveals Z_01.
        self.assertNotEqual(left_field[0][1], right_field[0][1])
        self.assertEqual(left_field[0][1], 2)
        self.assertEqual(right_field[0][1], 4)


if __name__ == "__main__":
    unittest.main()
