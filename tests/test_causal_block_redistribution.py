import unittest

from enterprise_math.causal_block_redistribution import (
    cross_block_redistribution_rank,
    direct_slot_hidden_rank,
    grand_total_hidden_rank,
    internal_hidden_rank,
    new_cross_freedom_when_two_blocks_merge,
    rank_decomposition_identity,
)


class CausalBlockRedistributionTests(unittest.TestCase):
    def test_two_blocks_gain_exactly_one_cross_redistribution_freedom(self):
        for left in range(1, 6):
            for right in range(1, 6):
                self.assertEqual(new_cross_freedom_when_two_blocks_merge(left, right), 1)

    def test_k_blocks_gain_k_minus_one_freedoms_when_only_grand_total_remains(self):
        block_sizes = (2, 3, 1, 4)
        self.assertEqual(internal_hidden_rank(block_sizes), (2 - 1) + (3 - 1) + (1 - 1) + (4 - 1))
        self.assertEqual(cross_block_redistribution_rank(len(block_sizes)), 3)
        self.assertEqual(grand_total_hidden_rank(block_sizes), 9)
        self.assertEqual(direct_slot_hidden_rank(block_sizes), 9)
        self.assertTrue(rank_decomposition_identity(block_sizes))

    def test_rank_decomposition_is_partition_shape_independent(self):
        partitions = (
            (6,),
            (1, 5),
            (2, 4),
            (1, 2, 3),
            (1, 1, 1, 1, 1, 1),
        )
        for block_sizes in partitions:
            self.assertTrue(rank_decomposition_identity(block_sizes))
            self.assertEqual(grand_total_hidden_rank(block_sizes), 5)

    def test_preserving_all_block_totals_has_smaller_hidden_rank_than_grand_total_only(self):
        block_sizes = (3, 2, 4)
        self.assertEqual(grand_total_hidden_rank(block_sizes) - internal_hidden_rank(block_sizes), 2)


if __name__ == "__main__":
    unittest.main()
