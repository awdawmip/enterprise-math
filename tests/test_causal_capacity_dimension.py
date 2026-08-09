import unittest

from enterprise_math.causal_capacity_dimension import (
    exact_polynomial_sequence,
    product_capacity,
    sampled_polynomial_difference_degree,
)


class CausalCapacityDimensionTests(unittest.TestCase):
    def test_parity_capacity_has_growth_dimension_zero(self):
        values = (2, 2, 2, 2, 2, 2)
        self.assertEqual(sampled_polynomial_difference_degree(values), 0)
        self.assertTrue(exact_polynomial_sequence(values, 0))

    def test_integer_sum_capacity_has_growth_dimension_one(self):
        values = tuple(depth + 1 for depth in range(8))
        self.assertEqual(sampled_polynomial_difference_degree(values), 1)
        self.assertTrue(exact_polynomial_sequence(values, 1))

    def test_two_independent_sum_capacities_have_dimension_two(self):
        one = tuple(depth + 1 for depth in range(8))
        two = product_capacity(one, one)
        self.assertEqual(two, tuple((depth + 1) ** 2 for depth in range(8)))
        self.assertEqual(sampled_polynomial_difference_degree(two), 2)
        self.assertTrue(exact_polynomial_sequence(two, 2))

    def test_linear_times_quadratic_capacity_has_additive_degree_three(self):
        linear = tuple(depth + 1 for depth in range(9))
        quadratic = tuple((2 * depth + 1) * (depth + 1) for depth in range(9))
        combined = product_capacity(linear, quadratic)
        self.assertEqual(sampled_polynomial_difference_degree(combined), 3)
        self.assertTrue(exact_polynomial_sequence(combined, 3))

    def test_exponential_copy_capacity_does_not_look_like_low_degree_polynomial(self):
        values = tuple(2**depth for depth in range(10))
        degree = sampled_polynomial_difference_degree(values)
        # A finite sequence is always eventually killed by enough differences,
        # so the sampled detector must not be promoted to an all-depth theorem.
        # What matters here is that no small fixed degree (0..5) passes.
        self.assertNotIn(degree, (0, 1, 2, 3, 4, 5))
        for candidate in range(6):
            self.assertFalse(exact_polynomial_sequence(values, candidate))


if __name__ == "__main__":
    unittest.main()
