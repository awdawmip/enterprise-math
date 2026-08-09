import unittest
from math import isqrt

from enterprise_math.graded_lego_fiber import (
    add_one_slot,
    graded_ball_count,
    graded_fiber_counts,
    graded_shell_counts,
    one_slot_graded_counts,
    power_grade,
)


class GradedLegoFiberTests(unittest.TestCase):
    def test_two_slot_l1_zero_sum_ball_has_closed_integer_count(self):
        grade = power_grade(1)
        for budget in range(0, 12):
            # States are (a,-a), grade=2|a|.
            expected = 2 * (budget // 2) + 1
            self.assertEqual(graded_ball_count(2, 0, budget, grade), expected)

    def test_two_slot_square_zero_sum_ball_has_closed_integer_count(self):
        grade = power_grade(2)
        for budget in range(0, 30):
            # States are (a,-a), grade=2a^2.
            radius = isqrt(budget // 2)
            expected = 2 * radius + 1
            self.assertEqual(graded_ball_count(2, 0, budget, grade), expected)

    def test_dimension_raising_recurrence_matches_direct_construction(self):
        grade = power_grade(1)
        maximum_grade = 6
        one = one_slot_graded_counts(maximum_grade, grade)
        two = add_one_slot(one, maximum_grade, grade)
        three = add_one_slot(two, maximum_grade, grade)
        self.assertEqual(two, graded_fiber_counts(2, maximum_grade, grade))
        self.assertEqual(three, graded_fiber_counts(3, maximum_grade, grade))

    def test_graph_and_square_grades_share_same_lego_composition_engine(self):
        l1_shells = graded_shell_counts(3, 0, 8, power_grade(1))
        square_shells = graded_shell_counts(3, 0, 8, power_grade(2))
        self.assertNotEqual(l1_shells, square_shells)
        self.assertEqual(l1_shells[0], 1)
        self.assertEqual(square_shells[0], 1)

    def test_small_three_slot_l1_shells_match_direct_known_values(self):
        # Zero-sum triples at L1 grade 0: only (0,0,0).
        # Grade 2: permutations of (1,-1,0): 6 states.
        shells = graded_shell_counts(3, 0, 4, power_grade(1))
        self.assertEqual(shells[0], 1)
        self.assertEqual(shells[1], 0)
        self.assertEqual(shells[2], 6)


if __name__ == "__main__":
    unittest.main()
