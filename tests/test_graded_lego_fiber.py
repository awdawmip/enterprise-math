import unittest
from math import isqrt

from enterprise_math.dimension_contraction import balanced_power_energy
from enterprise_math.graded_lego_fiber import (
    add_one_slot,
    exact_grade_count,
    graded_ball_count,
    graded_fiber_counts,
    graded_shell_counts,
    minimum_grade_multiplicity,
    minimum_reachable_grade,
    one_slot_graded_counts,
    power_grade,
)
from enterprise_math.lattice_geometry import (
    a_ball_count,
    a_quadratic_shell_count,
)
from enterprise_math.lego_partition_fiber import balanced_minimizer_multiplicity


class GradedLegoFiberTests(unittest.TestCase):
    def test_two_slot_l1_zero_sum_ball_has_closed_integer_count(self):
        grade = power_grade(1)
        for budget in range(0, 12):
            expected = 2 * (budget // 2) + 1
            self.assertEqual(graded_ball_count(2, 0, budget, grade), expected)

    def test_two_slot_square_zero_sum_ball_has_closed_integer_count(self):
        grade = power_grade(2)
        for budget in range(0, 30):
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
        shells = graded_shell_counts(3, 0, 4, power_grade(1))
        self.assertEqual(shells[0], 1)
        self.assertEqual(shells[1], 0)
        self.assertEqual(shells[2], 6)

    def test_a_p_graph_balls_are_zero_sum_l1_graded_lego_balls(self):
        for p in range(1, 5):
            slots = p + 1
            for radius in range(0, 5):
                self.assertEqual(
                    graded_ball_count(slots, 0, 2 * radius, power_grade(1)),
                    a_ball_count(p, radius),
                )

    def test_a_p_quadratic_shells_are_zero_sum_square_grade_shells(self):
        for p in range(1, 5):
            slots = p + 1
            for q in range(0, 8):
                self.assertEqual(
                    exact_grade_count(slots, 0, 2 * q, power_grade(2)),
                    a_quadratic_shell_count(p, q),
                )

    def test_p019_balanced_power_energy_is_lowest_occupied_grade(self):
        for slots in range(1, 6):
            for power in (2, 3, 4):
                grade = power_grade(power)
                for total in range(0, 9):
                    budget = total ** power
                    expected = balanced_power_energy(slots, power, total)
                    self.assertEqual(
                        minimum_reachable_grade(slots, total, budget, grade),
                        expected,
                    )

    def test_balanced_minimizer_multiplicity_is_minimum_grade_shell_count(self):
        for slots in range(1, 6):
            for power in (2, 3):
                grade = power_grade(power)
                for total in range(0, 9):
                    budget = total ** power
                    minimum, multiplicity = minimum_grade_multiplicity(
                        slots, total, budget, grade
                    )
                    self.assertEqual(minimum, balanced_power_energy(slots, power, total))
                    self.assertEqual(
                        multiplicity,
                        balanced_minimizer_multiplicity(slots, total),
                    )


if __name__ == "__main__":
    unittest.main()
