import unittest

from enterprise_math.relation_block_rank import relation_block_system
from enterprise_math.relation_certificate_rank import (
    abc_wronskian_row,
    certificate_rank_gain,
    exact_certificate_equivalence_rank,
)


class RelationCertificateRankTests(unittest.TestCase):
    def test_one_wronskian_adds_one_dimension_in_abc(self) -> None:
        system = relation_block_system((2, 3, 5), ((1, 1, -1),))
        result = certificate_rank_gain(system, (abc_wronskian_row(2, 3, 5),))
        self.assertEqual(result.relation_rank, 1)
        self.assertEqual(result.compressed_rank, 2)
        self.assertEqual(result.rank_gain, 1)
        self.assertEqual(result.residual_kernel_rank, 1)
        self.assertFalse(result.relation_redundant)
        self.assertFalse(result.block_value_complete)

    def test_dependent_many_wronskians_still_gain_one(self) -> None:
        system = relation_block_system((2, 3, 5), ((1, 1, -1),))
        w = abc_wronskian_row(2, 3, 5)
        rows = (w, tuple(2 * value for value in w), tuple(-7 * value for value in w))
        result = certificate_rank_gain(system, rows)
        self.assertEqual(result.certificate_row_count, 3)
        self.assertEqual(result.rank_gain, 1)
        self.assertEqual(result.residual_kernel_rank, 1)

    def test_one_additional_independent_certificate_completes_abc_state(self) -> None:
        system = relation_block_system((2, 3, 5), ((1, 1, -1),))
        rows = (
            abc_wronskian_row(2, 3, 5),
            (1, 0, 0),
        )
        result = certificate_rank_gain(system, rows)
        self.assertEqual(result.rank_gain, 2)
        self.assertEqual(result.residual_kernel_rank, 0)
        self.assertTrue(result.block_value_complete)
        self.assertEqual(exact_certificate_equivalence_rank(system, rows), 0)

    def test_relation_row_itself_is_certificate_redundant(self) -> None:
        relation = (1, 1, -1)
        system = relation_block_system((2, 3, 5), (relation,))
        result = certificate_rank_gain(system, (relation, tuple(3 * x for x in relation)))
        self.assertEqual(result.rank_gain, 0)
        self.assertTrue(result.relation_redundant)
        self.assertEqual(result.residual_kernel_rank, 2)

    def test_unit_abc_one_nonzero_certificate_is_complete(self) -> None:
        system = relation_block_system((1, 8, 9), ((1, 1, -1),))
        result = certificate_rank_gain(system, ((0, 1, 0),))
        self.assertEqual(system.compressed_rank, 1)
        self.assertEqual(result.rank_gain, 1)
        self.assertTrue(result.block_value_complete)

    def test_two_relation_system_has_only_one_remaining_precision_dimension(self) -> None:
        system = relation_block_system(
            (1, 2, 3, 5),
            (
                (1, 1, -1, 0),
                (0, 1, 1, -1),
            ),
        )
        self.assertEqual(system.compressed_rank, 1)
        result = certificate_rank_gain(system, ((0, 1, 0, 0), (0, 0, 0, 1)))
        self.assertEqual(result.rank_gain, 1)
        self.assertTrue(result.block_value_complete)

    def test_four_active_blocks_one_relation_can_gain_at_most_three(self) -> None:
        system = relation_block_system((2, 3, 5, 7), ((1, 1, -1, 0),))
        result = certificate_rank_gain(
            system,
            (
                (1, 0, 0, 0),
                (0, 1, 0, 0),
                (0, 0, 0, 1),
                (1, 1, 1, 1),
                (2, 2, 2, 2),
            ),
        )
        self.assertEqual(system.compressed_rank, 3)
        self.assertEqual(result.rank_gain, 3)
        self.assertTrue(result.block_value_complete)


if __name__ == "__main__":
    unittest.main()
