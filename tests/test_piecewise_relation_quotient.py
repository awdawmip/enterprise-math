import itertools
import unittest

from enterprise_math.linear_relation_quotient import partition_matrix
from enterprise_math.piecewise_relation_quotient import (
    binary_threshold_piecewise_descends,
    factor_binary_threshold_piecewise,
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
        # Coarsest partition erases the hidden guard because both branches have
        # the same total effect.  An intermediate refinement exposes a branch
        # difference while the guard is still hidden.  Singleton precision is
        # exact again because the guard itself becomes visible.
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


if __name__ == "__main__":
    unittest.main()
