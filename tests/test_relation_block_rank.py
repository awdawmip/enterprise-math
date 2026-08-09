import unittest

from enterprise_math.relation_block_rank import (
    certificate_rank_ceiling,
    derivative_value_state_is_admissible,
    rational_matrix_rank,
    relation_block_system,
)


class RelationBlockRankTests(unittest.TestCase):
    def test_abc_is_three_blocks_minus_one_relation(self) -> None:
        system = relation_block_system((2, 3, 5), ((1, 1, -1),))
        self.assertEqual(system.active_indices, (0, 1, 2))
        self.assertEqual(system.block_image_generators, (1, 1, 1))
        self.assertEqual(system.relation_rank, 1)
        self.assertEqual(system.compressed_rank, 2)
        self.assertTrue(derivative_value_state_is_admissible(system, (1, 1, 2)))
        self.assertFalse(derivative_value_state_is_admissible(system, (1, 1, 1)))

    def test_unit_abc_boundary_has_rank_one(self) -> None:
        system = relation_block_system((1, 8, 9), ((1, 1, -1),))
        self.assertEqual(system.active_indices, (1, 2))
        self.assertEqual(system.block_image_generators, (0, 12, 6))
        self.assertEqual(system.active_relation_rows, ((1, -1),))
        self.assertEqual(system.relation_rank, 1)
        self.assertEqual(system.compressed_rank, 1)
        self.assertTrue(derivative_value_state_is_admissible(system, (0, 12, 12)))
        self.assertFalse(derivative_value_state_is_admissible(system, (1, 12, 12)))

    def test_many_prime_coordinates_still_reduce_to_two_block_directions(self) -> None:
        # 6,35,41 are pairwise coprime and satisfy 6+35=41.  Their fine prime
        # supports contain five coordinates: 2,3,5,7,41.
        system = relation_block_system((6, 35, 41), ((1, 1, -1),))
        self.assertEqual(system.block_image_generators, (1, 1, 1))
        self.assertEqual(system.compressed_rank, 2)
        self.assertTrue(derivative_value_state_is_admissible(system, (3, -1, 2)))

    def test_two_independent_relations_leave_one_direction(self) -> None:
        blocks = (1, 2, 3, 5)
        relations = (
            (1, 1, -1, 0),   # 1+2=3
            (0, 1, 1, -1),   # 2+3=5
        )
        system = relation_block_system(blocks, relations)
        self.assertEqual(system.active_indices, (1, 2, 3))
        self.assertEqual(system.active_relation_rows, ((1, -1, 0), (1, 1, -1)))
        self.assertEqual(system.relation_rank, 2)
        self.assertEqual(system.compressed_rank, 1)
        self.assertTrue(derivative_value_state_is_admissible(system, (0, 1, 1, 2)))

    def test_one_relation_on_four_active_blocks_leaves_rank_three(self) -> None:
        system = relation_block_system(
            (2, 3, 5, 7),
            ((1, 1, -1, 0),),
        )
        self.assertEqual(system.relation_rank, 1)
        self.assertEqual(system.compressed_rank, 3)
        self.assertEqual(
            certificate_rank_ceiling(
                system,
                (
                    (1, 0, 0, 0),
                    (0, 1, 0, 0),
                    (0, 0, 0, 1),
                    (1, 1, 1, 1),
                ),
            ),
            3,
        )

    def test_exact_rational_rank(self) -> None:
        self.assertEqual(rational_matrix_rank(((1, 2, 3), (2, 4, 6))), 1)
        self.assertEqual(rational_matrix_rank(((1, 2, 3), (0, 1, 1))), 2)
        self.assertEqual(rational_matrix_rank(((0, 0), (0, 0))), 0)

    def test_invalid_nonrelation_or_overlapping_blocks_rejected(self) -> None:
        with self.assertRaises(ValueError):
            relation_block_system((2, 4, 6), ((1, 1, -1),))
        with self.assertRaises(ValueError):
            relation_block_system((2, 3, 5), ((1, 1, 1),))


if __name__ == "__main__":
    unittest.main()
