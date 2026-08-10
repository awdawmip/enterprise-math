import unittest
from itertools import product

from enterprise_math.precision_integer_linear_lift_compiler import (
    codimension_one_linear_lift_holds,
    compile_codimension_one_linear_lift,
    determinant_bareiss,
    integer_matrix_rank,
    linear_coordinate,
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

    def test_partition_with_full_intra_difference_rank_is_rejected(self):
        states = ((0, 0), (1, 0), (0, 1), (1, 1))
        blocks = (((0, 0), (1, 0), (0, 1)), ((1, 1),))
        self.assertFalse(codimension_one_linear_lift_holds(states, blocks))
        with self.assertRaises(ValueError):
            primitive_codimension_one_normal(states, blocks)

    def test_codimension_one_span_that_fails_to_separate_classes_is_rejected(self):
        states = ((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1))
        # Same-class differences force the normal to (0,1), but two distinct
        # classes are deliberately placed at the same y-coordinate.
        blocks = (
            ((0, 0), (1, 0)),
            ((2, 0),),
            ((0, 1), (1, 1), (2, 1)),
        )
        self.assertEqual(primitive_codimension_one_normal(states, blocks), (0, 1))
        self.assertFalse(codimension_one_linear_lift_holds(states, blocks))

    def test_invalid_partition_fails_closed(self):
        with self.assertRaises(ValueError):
            codimension_one_linear_lift_holds(((0, 0), (1, 0)), (((0, 0),),))


if __name__ == "__main__":
    unittest.main()
