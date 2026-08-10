import unittest

from enterprise_math.causal_partition_transfer_multiplicity import (
    block_capacities,
    coarse_move_multiplicity_table,
    coarse_move_witness_multiplicity,
    coarse_primitive_direction_count,
    coarse_relation_rank,
    expected_coarse_move_multiplicity_table,
    hidden_identity_move_count,
    primitive_operation_projection_identity,
)


class CausalPartitionTransferMultiplicityTests(unittest.TestCase):
    def test_every_coarse_move_keeps_unit_value_but_has_capacity_product_witnesses(self):
        partition = ((0, 3), (1,), (2, 4, 5))
        self.assertEqual(block_capacities(partition), (2, 1, 3))
        self.assertEqual(coarse_move_witness_multiplicity(0, 1, partition), 2)
        self.assertEqual(coarse_move_witness_multiplicity(2, 0, partition), 6)
        self.assertEqual(coarse_move_witness_multiplicity(1, 2, partition), 3)
        self.assertEqual(coarse_primitive_direction_count(partition), 6)
        self.assertEqual(coarse_relation_rank(partition), 2)

    def test_internal_fine_transfers_collapse_to_coarse_identity(self):
        partition = ((0, 1, 2), (3, 4))
        self.assertEqual(hidden_identity_move_count(partition), 3 * 2 + 2 * 1)
        table = coarse_move_multiplicity_table(partition)
        self.assertEqual(table[None], 8)
        self.assertEqual(table[(0, 1)], 6)
        self.assertEqual(table[(1, 0)], 6)

    def test_full_projection_table_matches_closed_capacity_formula(self):
        partitions = (
            ((0,), (1,), (2,), (3,)),
            ((0, 1), (2,), (3,)),
            ((0, 1), (2, 3)),
            ((0, 2, 4), (1, 3), (5,)),
            ((0, 1, 2, 3),),
        )
        for partition in partitions:
            self.assertTrue(primitive_operation_projection_identity(partition))
            self.assertEqual(
                coarse_move_multiplicity_table(partition),
                expected_coarse_move_multiplicity_table(partition),
            )

    def test_unit_partition_has_no_hidden_identity_and_one_witness_per_move(self):
        partition = ((0,), (1,), (2,), (3,))
        self.assertEqual(hidden_identity_move_count(partition), 0)
        table = coarse_move_multiplicity_table(partition)
        self.assertTrue(all(value == 1 for key, value in table.items() if key is not None))
        self.assertEqual(coarse_primitive_direction_count(partition), 12)
        self.assertEqual(coarse_relation_rank(partition), 3)

    def test_full_collapse_turns_every_fine_primitive_move_into_identity_witness(self):
        partition = ((0, 1, 2, 3, 4),)
        self.assertEqual(hidden_identity_move_count(partition), 20)
        self.assertEqual(coarse_move_multiplicity_table(partition), {None: 20})
        self.assertEqual(coarse_primitive_direction_count(partition), 0)
        self.assertEqual(coarse_relation_rank(partition), 0)


if __name__ == "__main__":
    unittest.main()
