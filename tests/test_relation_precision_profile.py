import itertools
import unittest

from enterprise_math.relation_precision_profile import (
    partition_capacities,
    partition_refines,
    relation_precision_profile,
    relation_refinement_cost,
)


class RelationPrecisionProfileTests(unittest.TestCase):
    def test_profile_on_unit_partition_chain(self):
        fine_capacities = (1,) * 8
        partitions = (
            ((0, 1, 2, 3, 4, 5, 6, 7),),
            ((0, 1, 2, 3), (4, 5, 6, 7)),
            ((0, 1), (2, 3), (4, 5), (6, 7)),
            tuple((index,) for index in range(8)),
        )
        expected = (
            (0, 8, 1),
            (1, 4, 2),
            (3, 2, 4),
            (7, 1, 8),
        )
        self.assertEqual(
            tuple(relation_precision_profile(fine_capacities, partition) for partition in partitions),
            expected,
        )

    def test_refinement_cost_tracks_rank_and_quantum_gain(self):
        fine_capacities = (1,) * 8
        initial = ((0, 1, 2, 3), (4, 5, 6, 7))
        refined = ((0, 1), (2, 3), (4,), (5,), (6,), (7,))
        rank_gain, quantum_factor, initial_quantum, refined_quantum = relation_refinement_cost(
            fine_capacities, initial, refined
        )
        self.assertEqual(rank_gain, 4)
        self.assertEqual((initial_quantum, refined_quantum), (4, 1))
        self.assertEqual(quantum_factor, 4)

    def test_refinement_can_add_rank_without_changing_quantum(self):
        fine_capacities = (2, 3, 5, 7)
        initial = ((0, 1), (2, 3))
        refined = ((0,), (1,), (2, 3))
        self.assertTrue(partition_refines(refined, initial))
        rank_gain, quantum_factor, _, _ = relation_refinement_cost(
            fine_capacities, initial, refined
        )
        self.assertEqual(rank_gain, 1)
        self.assertEqual(quantum_factor, 1)

    def test_partition_capacities(self):
        fine_capacities = (2, 1, 3, 4, 2)
        partition = ((0, 2), (1, 4), (3,))
        self.assertEqual(partition_capacities(fine_capacities, partition), (5, 3, 4))

    def test_all_small_unit_refinements_have_monotone_precision(self):
        fine_capacities = (1,) * 6
        coarse = ((0, 1, 2), (3, 4, 5))
        candidates = (
            ((0,), (1, 2), (3, 4, 5)),
            ((0, 1), (2,), (3,), (4, 5)),
            ((0,), (1,), (2,), (3,), (4,), (5,)),
        )
        coarse_rank, coarse_quantum, coarse_period = relation_precision_profile(
            fine_capacities, coarse
        )
        for refined in candidates:
            self.assertTrue(partition_refines(refined, coarse))
            rank, quantum, period = relation_precision_profile(
                fine_capacities, refined
            )
            self.assertGreaterEqual(rank, coarse_rank)
            self.assertEqual(coarse_quantum % quantum, 0)
            self.assertEqual(period % coarse_period, 0)
            rank_gain, factor, _, _ = relation_refinement_cost(
                fine_capacities, coarse, refined
            )
            self.assertEqual(rank_gain, rank - coarse_rank)
            self.assertEqual(period, coarse_period * factor)

    def test_refinement_relation_is_transitive(self):
        coarse = ((0, 1, 2, 3), (4, 5))
        middle = ((0, 1), (2, 3), (4, 5))
        fine = ((0,), (1,), (2, 3), (4,), (5,))
        self.assertTrue(partition_refines(middle, coarse))
        self.assertTrue(partition_refines(fine, middle))
        self.assertTrue(partition_refines(fine, coarse))


if __name__ == "__main__":
    unittest.main()
