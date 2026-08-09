import unittest

from enterprise_math.abc_block_value_quotient import (
    block_derivative_access_value,
    block_value_lattice_membership,
    block_value_witness_state,
    bounded_block_value_pareto_frontier,
    fine_and_block_pareto_agree_on_reference_examples,
)


class AbcBlockValueQuotientTests(unittest.TestCase):
    def test_single_block_access_reduces_to_primitive_row(self) -> None:
        value = block_derivative_access_value(9, 6)
        self.assertEqual(value.image_generator, 6)
        self.assertEqual(value.primitive_row, (1,))
        self.assertEqual(value.reduced_target, 1)
        self.assertEqual(value.radius, 1)

        with self.assertRaises(ValueError):
            block_derivative_access_value(9, 1)

    def test_235_frontier_states_live_entirely_in_block_values(self) -> None:
        first = block_value_witness_state(2, 3, 5, 0, 1)
        self.assertEqual(first.derivative_values, (0, 1, 1))
        self.assertEqual(first.global_radius, 1)
        self.assertEqual(first.wronskian, 2)
        self.assertEqual(first.absorption_redundancy, 2)

        second = block_value_witness_state(2, 3, 5, 1, 1)
        self.assertEqual(second.derivative_values, (1, 1, 2))
        self.assertEqual(second.global_radius, 2)
        self.assertEqual(second.wronskian, -1)
        self.assertEqual(second.absorption_redundancy, 1)

        self.assertEqual(
            bounded_block_value_pareto_frontier(2, 3, 5, 3),
            ((1, 2), (2, 1)),
        )

    def test_same_radical_189_state_compresses_to_one_scalar_value(self) -> None:
        self.assertTrue(block_value_lattice_membership(1, 8, 9, 0, 12))
        state = block_value_witness_state(1, 8, 9, 0, 12)
        self.assertEqual(state.derivative_values, (0, 12, 12))
        self.assertEqual(state.block_radii, (0, 1, 2))
        self.assertEqual(state.global_radius, 2)
        self.assertEqual(state.wronskian, 12)
        self.assertEqual(state.residual_product, 12)
        self.assertEqual(state.absorption_redundancy, 1)

        self.assertFalse(block_value_lattice_membership(1, 8, 9, 0, 6))

    def test_unit_relation_floor_access_is_block_value_state(self) -> None:
        state = block_value_witness_state(1, 242, 243, 0, 4455)
        self.assertEqual(state.derivative_values, (0, 4455, 4455))
        self.assertEqual(state.block_radii, (0, 27, 11))
        self.assertEqual(state.global_radius, 27)
        self.assertEqual(state.wronskian, 4455)
        self.assertEqual(state.residual_product, 891)
        self.assertEqual(state.absorption_redundancy, 5)

    def test_reference_fine_and_block_pareto_frontiers_agree(self) -> None:
        self.assertTrue(fine_and_block_pareto_agree_on_reference_examples())
        self.assertEqual(
            bounded_block_value_pareto_frontier(2, 7, 9, 6),
            ((1, 3), (4, 2), (5, 1)),
        )
        self.assertEqual(
            bounded_block_value_pareto_frontier(5, 7, 12, 3),
            ((1, 6), (2, 2)),
        )

    def test_degenerate_block_state_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            block_value_witness_state(2, 3, 5, 0, 0)


if __name__ == "__main__":
    unittest.main()
