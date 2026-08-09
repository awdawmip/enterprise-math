import itertools
import unittest

from enterprise_math.linear_relation_quotient import (
    descended_linear_matrix,
    kernel_invariant_under_linear_matrix,
    linear_family_descends,
    linear_matrix_descends,
    partition_matrix,
    refine_partition_for_linear_family,
)


def matmul(left, right):
    return tuple(
        tuple(
            sum(left[row][k] * right[k][column] for k in range(len(right)))
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def is_refinement(fine_partition, coarse_partition):
    coarse_group_of = {}
    for group_index, group in enumerate(coarse_partition):
        for vertex in group:
            coarse_group_of[vertex] = group_index
    return all(
        len({coarse_group_of[vertex] for vertex in group}) == 1
        for group in fine_partition
    )


def set_partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first = items[0]
    for rest in set_partitions(items[1:]):
        # Add a new first block.
        yield ((first,),) + rest
        # Or insert into each existing block. Canonical tuple order prevents duplicates.
        for index in range(len(rest)):
            yield rest[:index] + ((first,) + rest[index],) + rest[index + 1 :]


class LinearRelationQuotientTests(unittest.TestCase):
    def test_descended_matrix_satisfies_exact_intertwining(self):
        # Two fine coordinates in each coarse block have identical aggregate effects.
        matrix = (
            (1, 0, 2, 0),
            (0, 1, 0, 2),
            (3, 0, 4, 0),
            (0, 3, 0, 4),
        )
        partition = ((0, 1), (2, 3))
        coarse = descended_linear_matrix(matrix, partition)
        aggregation = partition_matrix(4, partition)
        self.assertEqual(
            matmul(aggregation, matrix),
            matmul(coarse, aggregation),
        )
        self.assertTrue(linear_matrix_descends(matrix, partition))
        self.assertTrue(kernel_invariant_under_linear_matrix(matrix, partition))

    def test_hidden_to_coarse_feedback_breaks_descent_and_kernel_invariance(self):
        matrix = (
            (1, 0, 0, 0),
            (0, 0, 0, 0),
            (0, 1, 1, 0),
            (0, 0, 0, 1),
        )
        partition = ((0, 1), (2, 3))
        self.assertFalse(linear_matrix_descends(matrix, partition))
        self.assertFalse(kernel_invariant_under_linear_matrix(matrix, partition))
        with self.assertRaises(ValueError):
            descended_linear_matrix(matrix, partition)

    def test_refinement_splits_only_when_future_dynamics_requires_it(self):
        matrix = (
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (1, 0, 1, 0),
            (0, 2, 0, 1),
        )
        initial = ((0, 1), (2, 3))
        refined = refine_partition_for_linear_family((matrix,), initial)
        self.assertEqual(refined, ((0,), (1,), (2, 3)))
        self.assertTrue(linear_matrix_descends(matrix, refined))

    def test_joint_operation_family_can_require_more_refinement(self):
        first = (
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (1, 1, 1, 0),
            (0, 0, 0, 1),
        )
        second = (
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 1, 1),
            (0, 0, 0, 1),
        )
        initial = ((0, 1), (2, 3))
        refined_first = refine_partition_for_linear_family((first,), initial)
        refined_second = refine_partition_for_linear_family((second,), initial)
        refined_both = refine_partition_for_linear_family((first, second), initial)
        self.assertTrue(is_refinement(refined_both, refined_first))
        self.assertTrue(is_refinement(refined_both, refined_second))
        self.assertTrue(linear_family_descends((first, second), refined_both))

    def test_stable_refinement_is_coarsest_stable_refinement_by_bruteforce(self):
        matrices = (
            (
                (1, 0, 1, 0),
                (0, 1, 0, 1),
                (0, 0, 1, 0),
                (0, 0, 0, 1),
            ),
            (
                (0, 1, 0, 0),
                (1, 0, 0, 0),
                (0, 0, 0, 1),
                (0, 0, 1, 0),
            ),
        )
        initial = ((0, 1, 2, 3),)
        result = refine_partition_for_linear_family(matrices, initial)
        self.assertTrue(linear_family_descends(matrices, result))

        for candidate in set_partitions(range(4)):
            if not is_refinement(candidate, initial):
                continue
            if not linear_family_descends(matrices, candidate):
                continue
            # Every stable refinement must refine the algorithm's result.
            self.assertTrue(is_refinement(candidate, result), msg=candidate)

    def test_descent_equivalent_to_kernel_invariance_on_small_integer_matrices(self):
        partition = ((0, 1), (2,))
        # Exhaustive small 3x3 binary matrices.
        for entries in itertools.product((0, 1), repeat=9):
            matrix = tuple(
                tuple(entries[3 * row + column] for column in range(3))
                for row in range(3)
            )
            self.assertEqual(
                linear_matrix_descends(matrix, partition),
                kernel_invariant_under_linear_matrix(matrix, partition),
                msg=matrix,
            )

    def test_affine_offset_always_descends_after_linear_part_descends(self):
        matrix = (
            (1, 0, 2, 0),
            (0, 1, 0, 2),
            (3, 0, 4, 0),
            (0, 3, 0, 4),
        )
        partition = ((0, 1), (2, 3))
        aggregation = partition_matrix(4, partition)
        coarse = descended_linear_matrix(matrix, partition)
        offset = (2, -1, 4, 3)
        coarse_offset = tuple(
            sum(aggregation[row][column] * offset[column] for column in range(4))
            for row in range(2)
        )

        for state in itertools.product(range(-2, 3), repeat=4):
            fine_next = tuple(
                sum(matrix[row][column] * state[column] for column in range(4))
                + offset[row]
                for row in range(4)
            )
            fine_then_coarse = tuple(
                sum(aggregation[row][column] * fine_next[column] for column in range(4))
                for row in range(2)
            )
            coarse_state = tuple(
                sum(aggregation[row][column] * state[column] for column in range(4))
                for row in range(2)
            )
            coarse_next = tuple(
                sum(coarse[row][column] * coarse_state[column] for column in range(2))
                + coarse_offset[row]
                for row in range(2)
            )
            self.assertEqual(fine_then_coarse, coarse_next)


if __name__ == "__main__":
    unittest.main()
