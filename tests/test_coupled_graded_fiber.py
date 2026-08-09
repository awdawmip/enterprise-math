import unittest

from enterprise_math.coupled_graded_fiber import (
    coupled_graded_counts,
    free_graded_coupling,
    grade_shift_support,
)


class CoupledGradedFiberTests(unittest.TestCase):
    def test_free_composition_adds_total_and_grade(self):
        left = {"l0": (0, 0), "l1": (1, 1)}
        right = {"r0": (0, 0), "r1": (-1, 1)}
        coupling = free_graded_coupling(tuple(left), tuple(right))
        counts = coupled_graded_counts(left, right, coupling)
        self.assertEqual(counts[(0, 0)], 1)
        self.assertEqual(counts[(1, 1)], 1)
        self.assertEqual(counts[(-1, 1)], 1)
        self.assertEqual(counts[(0, 2)], 1)

    def test_support_removal_and_split_multiplicity_are_separate_from_grade_shift(self):
        left = {"l": (1, 1)}
        right = {"r": (-1, 1)}
        self.assertEqual(coupled_graded_counts(left, right, {("l", "r"): 0}), {})
        self.assertEqual(
            coupled_graded_counts(left, right, {("l", "r"): 3}),
            {(0, 2): 3},
        )
        self.assertEqual(
            coupled_graded_counts(
                left,
                right,
                {("l", "r"): 1},
                {("l", "r"): 5},
            ),
            {(0, 7): 1},
        )

    def test_cross_grade_can_be_negative_if_joint_grade_remains_nonnegative(self):
        left = {"l": (1, 4)}
        right = {"r": (-1, 4)}
        counts = coupled_graded_counts(
            left,
            right,
            {("l", "r"): 1},
            {("l", "r"): -3},
        )
        self.assertEqual(counts, {(0, 5): 1})

    def test_grade_budget_truncates_after_joint_interaction(self):
        left = {"l": (0, 2)}
        right = {"r": (0, 2)}
        coupling = {("l", "r"): 1}
        self.assertEqual(
            coupled_graded_counts(left, right, coupling, maximum_grade=3),
            {},
        )
        self.assertEqual(
            coupled_graded_counts(left, right, coupling, maximum_grade=4),
            {(0, 4): 1},
        )

    def test_grade_shift_support_is_typed_separately(self):
        shifts = {("a", "b"): 0, ("a", "c"): 2, ("d", "e"): -1}
        self.assertEqual(
            grade_shift_support(shifts),
            frozenset({("a", "c"), ("d", "e")}),
        )


if __name__ == "__main__":
    unittest.main()
