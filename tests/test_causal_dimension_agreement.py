import unittest

from enterprise_math.causal_dimension_agreement import (
    capacity_growth_degree,
    free_a_p_dimension_agreement,
    independent_polynomial_growth_degree_adds,
    task_growth_can_disagree_with_substrate_rank,
)


class CausalDimensionAgreementTests(unittest.TestCase):
    def test_free_a_p_model_has_three_way_dimension_agreement(self):
        for p in range(1, 6):
            certificate = free_a_p_dimension_agreement(p)
            self.assertTrue(certificate.agrees)
            self.assertEqual(certificate.fiber_growth_degree, p)
            self.assertEqual(certificate.ball_growth_degree, p)

    def test_parity_task_can_collapse_growth_dimension_below_substrate_rank(self):
        parity_capacity = (2, 2, 2, 2, 2, 2, 2)
        self.assertEqual(capacity_growth_degree(parity_capacity), 0)
        self.assertTrue(task_growth_can_disagree_with_substrate_rank(3, parity_capacity))

    def test_sum_task_has_growth_degree_one(self):
        sum_capacity = tuple(depth + 1 for depth in range(9))
        self.assertEqual(capacity_growth_degree(sum_capacity), 1)
        self.assertFalse(task_growth_can_disagree_with_substrate_rank(1, sum_capacity))

    def test_two_independent_linear_capacity_tasks_have_quadratic_growth(self):
        left = tuple(depth + 1 for depth in range(10))
        right = tuple(2 * depth + 1 for depth in range(10))
        self.assertTrue(independent_polynomial_growth_degree_adds(left, 1, right, 1))
        product = tuple(a * b for a, b in zip(left, right))
        self.assertEqual(capacity_growth_degree(product), 2)

    def test_constant_structure_count_cannot_be_confused_with_value_dimension(self):
        constant = (1, 1, 1, 1, 1, 1)
        self.assertEqual(capacity_growth_degree(constant), 0)
        # A value channel can still grow independently even when this structure-count
        # observation has zero growth degree.
        self.assertTrue(task_growth_can_disagree_with_substrate_rank(1, constant))

    def test_exponential_task_has_no_small_polynomial_growth_degree(self):
        copy_capacity = tuple(2**depth for depth in range(10))
        degree = capacity_growth_degree(copy_capacity)
        self.assertNotIn(degree, (0, 1, 2, 3, 4, 5))


if __name__ == "__main__":
    unittest.main()
