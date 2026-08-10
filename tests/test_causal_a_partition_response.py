import unittest
from itertools import combinations

from enterprise_math.causal_a_partition_response import (
    coarse_block_count,
    coarse_subset_to_cut,
    cut_probe_bijection_holds,
    cut_to_coarse_subset,
    expected_surviving_probe_count,
    one_dimension_contraction_probe_loss,
    probe_loss_count,
    relation_rank_after_partition,
    relation_rank_lost_by_partition,
    surviving_cut_subsets,
    surviving_extreme_probe_count,
)


class CausalAPartitionResponseTests(unittest.TestCase):
    def test_surviving_extreme_probes_are_exactly_unions_of_coarse_blocks(self):
        partitions = (
            ((0,), (1,), (2,), (3,)),
            ((0, 1), (2,), (3,)),
            ((0, 1), (2, 3)),
            ((0, 1, 2), (3,)),
            ((0, 1, 2, 3),),
        )
        for partition in partitions:
            self.assertEqual(
                surviving_extreme_probe_count(partition),
                expected_surviving_probe_count(partition),
            )
            self.assertTrue(cut_probe_bijection_holds(partition))

    def test_each_independent_dimension_contraction_removes_power_of_two_probe_family(self):
        self.assertEqual(one_dimension_contraction_probe_loss(4), 8)
        self.assertEqual(one_dimension_contraction_probe_loss(3), 4)
        self.assertEqual(one_dimension_contraction_probe_loss(2), 2)

        before = ((0,), (1,), (2,), (3,))
        after = ((0, 1), (2,), (3,))
        self.assertEqual(probe_loss_count(before), 0)
        self.assertEqual(probe_loss_count(after), 8)

    def test_relation_rank_and_probe_count_track_same_partition(self):
        partition = ((0, 1), (2, 3, 4), (5,))
        self.assertEqual(coarse_block_count(partition), 3)
        self.assertEqual(relation_rank_after_partition(partition), 2)
        self.assertEqual(relation_rank_lost_by_partition(partition), 3)
        self.assertEqual(surviving_extreme_probe_count(partition), 6)
        self.assertEqual(expected_surviving_probe_count(partition), 6)
        self.assertEqual(probe_loss_count(partition), (2 ** 6 - 2) - 6)

    def test_cut_and_coarse_subset_maps_are_inverse(self):
        partition = ((0, 3), (1,), (2, 4))
        survivors = surviving_cut_subsets(partition)
        for cut in survivors:
            coarse = cut_to_coarse_subset(cut, partition)
            self.assertEqual(coarse_subset_to_cut(coarse, partition), cut)

        for size in range(1, 3):
            for coarse in combinations(range(3), size):
                cut = coarse_subset_to_cut(coarse, partition)
                self.assertEqual(cut_to_coarse_subset(cut, partition), coarse)

    def test_full_collapse_leaves_no_nontrivial_extreme_probe(self):
        partition = ((0, 1, 2, 3, 4),)
        self.assertEqual(relation_rank_after_partition(partition), 0)
        self.assertEqual(surviving_cut_subsets(partition), ())
        self.assertEqual(surviving_extreme_probe_count(partition), 0)
        self.assertEqual(expected_surviving_probe_count(partition), 0)


if __name__ == "__main__":
    unittest.main()
