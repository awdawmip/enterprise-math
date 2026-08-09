import itertools
import unittest

from enterprise_math.linear_relation_quotient import partition_matrix
from enterprise_math.piecewise_relation_quotient import (
    binary_threshold_piecewise_descends,
    factor_binary_threshold_piecewise,
    minimum_exact_partition_for_binary_threshold_piecewise,
)


def zero_matrix(size):
    return tuple(tuple(0 for _ in range(size)) for _ in range(size))


def aggregate(vector, partition):
    matrix = partition_matrix(len(vector), partition)
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(len(vector)))
        for row in range(len(partition))
    )


def apply_affine(branch, state):
    matrix, offset = branch
    return tuple(
        sum(matrix[row][column] * state[column] for column in range(len(state)))
        + offset[row]
        for row in range(len(state))
    )


def apply_piecewise(weights, bias, true_branch, false_branch, state):
    score = sum(weight * value for weight, value in zip(weights, state)) + bias
    return apply_affine(true_branch if score >= 0 else false_branch, state)


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
        yield ((first,),) + rest
        for index in range(len(rest)):
            yield rest[:index] + ((first,) + rest[index],) + rest[index + 1 :]


class PiecewiseRelationQuotientTests(unittest.TestCase):
    def test_hidden_guard_can_be_erased_when_coarse_branch_effects_match(self):
        partition = ((0, 1),)
        weights = (1, -1)
        false_branch = (zero_matrix(2), (0, 0))
        true_branch = (
            ((1, -1), (-1, 1)),
            (1, -1),
        )
        factor = factor_binary_threshold_piecewise(
            weights, 0, true_branch, false_branch, partition
        )
        self.assertEqual(factor.mode, "hidden_guard_erased")
        self.assertEqual(factor.common_branch, (((0,),), (0,)))

        for state in itertools.product(range(-4, 5), repeat=2):
            fine_next = apply_piecewise(weights, 0, true_branch, false_branch, state)
            self.assertEqual(aggregate(fine_next, partition), (0,))

    def test_hidden_guard_with_different_coarse_effects_is_not_exact(self):
        partition = ((0, 1, 2),)
        weights = (0, 1, -1)
        false_branch = (zero_matrix(3), (0, 0, 0))
        true_branch = (
            ((1, 1, 1), (0, 0, 0), (0, 0, 0)),
            (0, 0, 0),
        )
        self.assertFalse(
            binary_threshold_piecewise_descends(
                weights, 0, true_branch, false_branch, partition
            )
        )

    def test_coarse_guard_allows_different_coarse_branches(self):
        partition = ((0, 1), (2, 3))
        weights = (1, 1, -1, -1)
        identity = tuple(
            tuple(1 if row == column else 0 for column in range(4))
            for row in range(4)
        )
        doubled = tuple(
            tuple(2 if row == column else 0 for column in range(4))
            for row in range(4)
        )
        true_branch = (identity, (1, 1, 0, 0))
        false_branch = (doubled, (0, 0, -1, -1))
        factor = factor_binary_threshold_piecewise(
            weights, 0, true_branch, false_branch, partition
        )
        self.assertEqual(factor.mode, "coarse_guard")
        self.assertEqual(factor.coarse_guard_weights, (1, -1))
        self.assertNotEqual(factor.true_branch, factor.false_branch)

        for state in itertools.product(range(-2, 3), repeat=4):
            coarse = aggregate(state, partition)
            coarse_score = coarse[0] - coarse[1]
            branch = factor.true_branch if coarse_score >= 0 else factor.false_branch
            coarse_next = apply_affine(branch, coarse)
            fine_next = apply_piecewise(weights, 0, true_branch, false_branch, state)
            self.assertEqual(aggregate(fine_next, partition), coarse_next)

    def test_constant_guard_ignores_inactive_non_descending_branch(self):
        partition = ((0, 1), (2,))
        weights = (0, 0, 0)
        true_branch = (
            ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            (0, 0, 0),
        )
        false_branch = (
            ((1, 0, 0), (0, 0, 0), (0, 1, 1)),
            (0, 0, 0),
        )
        factor = factor_binary_threshold_piecewise(
            weights, 3, true_branch, false_branch, partition
        )
        self.assertEqual(factor.mode, "constant_true")
        self.assertTrue(
            binary_threshold_piecewise_descends(
                weights, 3, true_branch, false_branch, partition
            )
        )

    def test_exactness_need_not_be_monotone_under_partition_refinement(self):
        coarse = ((0, 1, 2),)
        intermediate = ((0,), (1, 2))
        singleton = ((0,), (1,), (2,))
        weights = (0, 1, -1)
        false_branch = (zero_matrix(3), (0, 0, 0))
        true_branch = (
            (
                (0, 1, 1),
                (0, -1, -1),
                (0, 0, 0),
            ),
            (0, 0, 0),
        )

        self.assertTrue(
            binary_threshold_piecewise_descends(
                weights, 0, true_branch, false_branch, coarse
            )
        )
        self.assertFalse(
            binary_threshold_piecewise_descends(
                weights, 0, true_branch, false_branch, intermediate
            )
        )
        self.assertTrue(
            binary_threshold_piecewise_descends(
                weights, 0, true_branch, false_branch, singleton
            )
        )

    def test_minimum_solver_keeps_hidden_guard_erased_when_possible(self):
        weights = (0, 1, -1)
        false_branch = (zero_matrix(3), (0, 0, 0))
        true_branch = (
            (
                (0, 1, 1),
                (0, -1, -1),
                (0, 0, 0),
            ),
            (0, 0, 0),
        )
        result = minimum_exact_partition_for_binary_threshold_piecewise(
            weights, 0, true_branch, false_branch
        )
        self.assertEqual(result, ((0, 1, 2),))

    def test_minimum_solver_exposes_guard_only_when_hidden_effects_differ(self):
        weights = (1, 1, -1, -1)
        identity = tuple(
            tuple(1 if row == column else 0 for column in range(4))
            for row in range(4)
        )
        doubled = tuple(
            tuple(2 if row == column else 0 for column in range(4))
            for row in range(4)
        )
        true_branch = (identity, (0, 0, 0, 0))
        false_branch = (doubled, (0, 0, 0, 0))
        result = minimum_exact_partition_for_binary_threshold_piecewise(
            weights, 0, true_branch, false_branch
        )
        self.assertEqual(result, ((0, 1), (2, 3)))
        self.assertTrue(
            binary_threshold_piecewise_descends(
                weights, 0, true_branch, false_branch, result
            )
        )

    def test_minimum_solver_is_coarsest_exact_refinement_by_bruteforce(self):
        weights = (1, 1, -1, -1)
        identity = tuple(
            tuple(1 if row == column else 0 for column in range(4))
            for row in range(4)
        )
        doubled = tuple(
            tuple(2 if row == column else 0 for column in range(4))
            for row in range(4)
        )
        true_branch = (identity, (0, 0, 0, 0))
        false_branch = (doubled, (0, 0, 0, 0))
        initial = ((0, 1, 2, 3),)
        result = minimum_exact_partition_for_binary_threshold_piecewise(
            weights, 0, true_branch, false_branch, initial
        )

        for candidate in set_partitions(range(4)):
            if not is_refinement(candidate, initial):
                continue
            if not binary_threshold_piecewise_descends(
                weights, 0, true_branch, false_branch, candidate
            ):
                continue
            self.assertTrue(is_refinement(candidate, result), msg=candidate)

    def test_globally_constant_guard_solver_stabilizes_only_active_branch(self):
        weights = (0, 0, 0)
        true_branch = (
            ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            (0, 0, 0),
        )
        false_branch = (
            ((1, 0, 0), (0, 0, 0), (0, 1, 1)),
            (0, 0, 0),
        )
        result = minimum_exact_partition_for_binary_threshold_piecewise(
            weights, 1, true_branch, false_branch
        )
        self.assertEqual(result, ((0, 1, 2),))


if __name__ == "__main__":
    unittest.main()
