import unittest
from itertools import product

from enterprise_math.precision_integer_linear_lift_compiler import (
    codimension_one_linear_lift_holds,
    compile_codimension_one_linear_lift,
    compile_linear_lift_state,
    determinant_bareiss,
    determinant_relation_token,
    integer_matrix_rank,
    linear_coordinate,
    linear_lift_difference_basis,
    linear_lift_partition_is_exact,
    linear_lift_span_gate_holds,
    primitive_codimension_one_normal,
)
from enterprise_math.precision_product_language_factorization import (
    BIT_STATES,
    coupled_and_observable,
    signature_partition,
)


def partition_to_blocks(partition):
    return tuple(tuple(sorted(block)) for block in sorted(partition, key=lambda block: sorted(block)))


class PrecisionIntegerLinearLiftCompilerTests(unittest.TestCase):
    def test_bareiss_determinant_and_fractionless_rank(self):
        self.assertEqual(determinant_bareiss(((1, 2), (3, 4))), -2)
        self.assertEqual(determinant_bareiss(((2, 4), (1, 2))), 0)
        self.assertEqual(integer_matrix_rank(((1, -1),)), 1)
        self.assertEqual(integer_matrix_rank(((1, 1, 0), (0, 1, 1))), 2)
        self.assertEqual(integer_matrix_rank(((1, 1), (2, 2))), 1)

    def test_diagonal_and_language_recovers_integer_sum_coordinate(self):
        actions = ((0, 0), (1, 1))
        partition = signature_partition(actions, coupled_and_observable)
        blocks = partition_to_blocks(partition)
        normal = primitive_codimension_one_normal(BIT_STATES, blocks)
        self.assertEqual(normal, (1, 1))
        self.assertTrue(codimension_one_linear_lift_holds(BIT_STATES, blocks))
        self.assertTrue(linear_lift_partition_is_exact(BIT_STATES, blocks))
        values = {
            state: compile_codimension_one_linear_lift(state, BIT_STATES, blocks)
            for state in BIT_STATES
        }
        self.assertEqual(values, {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 2})

    def test_cross_and_language_recovers_a3_unit_difference_coordinate(self):
        actions = ((0, 1), (1, 0))
        partition = signature_partition(actions, coupled_and_observable)
        blocks = partition_to_blocks(partition)
        normal = primitive_codimension_one_normal(BIT_STATES, blocks)
        self.assertEqual(normal, (1, -1))
        self.assertTrue(codimension_one_linear_lift_holds(BIT_STATES, blocks))
        self.assertTrue(linear_lift_partition_is_exact(BIT_STATES, blocks))
        values = {
            state: compile_codimension_one_linear_lift(state, BIT_STATES, blocks)
            for state in BIT_STATES
        }
        self.assertEqual(values, {(0, 0): 0, (0, 1): -1, (1, 0): 1, (1, 1): 0})

    def test_three_dimensional_plane_partition_recovers_primitive_normal(self):
        states = tuple(product(range(3), repeat=3))
        blocks_by_value = {}
        normal = (1, -2, 1)
        for state in states:
            blocks_by_value.setdefault(linear_coordinate(state, normal), []).append(state)
        blocks = tuple(tuple(block) for block in blocks_by_value.values())
        recovered = primitive_codimension_one_normal(states, blocks)
        self.assertEqual(recovered, normal)
        self.assertTrue(codimension_one_linear_lift_holds(states, blocks))
        self.assertTrue(linear_lift_partition_is_exact(states, blocks))

    def test_arbitrary_codimension_linear_lift_uses_determinant_token(self):
        # Fibers are parallel lines in Z^3 with direction (1,1,1); the
        # intra-class span has rank 1, so the quotient has codimension 2.
        states = tuple(product(range(3), repeat=3))
        direction = (1, 1, 1)
        # Use two independent difference coordinates orthogonal to the line.
        blocks_by_value = {}
        for state in states:
            key = (state[0] - state[1], state[1] - state[2])
            blocks_by_value.setdefault(key, []).append(state)
        blocks = tuple(tuple(block) for block in blocks_by_value.values())
        basis = linear_lift_difference_basis(states, blocks)
        self.assertEqual(len(basis), 1)
        self.assertEqual(integer_matrix_rank(basis), 1)
        self.assertTrue(linear_lift_span_gate_holds(states, blocks))
        self.assertTrue(linear_lift_partition_is_exact(states, blocks))
        tokens = {state: compile_linear_lift_state(state, states, blocks) for state in states}
        for left in states:
            for right in states:
                same_class = (
                    left[0] - left[1], left[1] - left[2]
                ) == (
                    right[0] - right[1], right[1] - right[2]
                )
                self.assertEqual(tokens[left] == tokens[right], same_class)
        # The selected basis may be +/- the primitive direction; either way the
        # determinant token is exact on fibers.
        self.assertEqual(len(determinant_relation_token((0, 0, 0), basis)), 3)

    def test_singleton_partition_is_exact_state_special_case(self):
        states = tuple(product((0, 1), repeat=3))
        blocks = tuple((state,) for state in states)
        self.assertTrue(linear_lift_partition_is_exact(states, blocks))
        tokens = {compile_linear_lift_state(state, states, blocks) for state in states}
        self.assertEqual(len(tokens), len(states))

    def test_one_block_partition_is_constant_special_case(self):
        states = tuple(product((0, 1), repeat=3))
        blocks = (states,)
        self.assertTrue(linear_lift_partition_is_exact(states, blocks))
        self.assertEqual(
            {compile_linear_lift_state(state, states, blocks) for state in states},
            {()},
        )

    def test_partition_with_full_intra_difference_rank_is_rejected(self):
        states = ((0, 0), (1, 0), (0, 1), (1, 1))
        blocks = (((0, 0), (1, 0), (0, 1)), ((1, 1),))
        self.assertFalse(codimension_one_linear_lift_holds(states, blocks))
        self.assertFalse(linear_lift_partition_is_exact(states, blocks))
        with self.assertRaises(ValueError):
            primitive_codimension_one_normal(states, blocks)

    def test_codimension_one_span_that_fails_to_separate_classes_is_rejected(self):
        states = ((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1))
        blocks = (
            ((0, 0), (1, 0)),
            ((2, 0),),
            ((0, 1), (1, 1), (2, 1)),
        )
        self.assertEqual(primitive_codimension_one_normal(states, blocks), (0, 1))
        self.assertFalse(codimension_one_linear_lift_holds(states, blocks))
        self.assertFalse(linear_lift_partition_is_exact(states, blocks))

    def test_invalid_partition_fails_closed(self):
        with self.assertRaises(ValueError):
            codimension_one_linear_lift_holds(((0, 0), (1, 0)), (((0, 0),),))


if __name__ == "__main__":
    unittest.main()
