import unittest
from itertools import product

from enterprise_math.multitype_lego_interaction import (
    additive_inventory_response_table,
    higher_interaction_support,
    multitype_interaction_coefficient,
    multitype_interaction_spectrum,
    reconstruct_multitype_response,
)


class MultitypeLegoInteractionTests(unittest.TestCase):
    def test_additive_response_has_no_higher_interactions(self):
        maxima = (3, 3)
        response = additive_inventory_response_table(maxima, (5, -2), base=7)
        coefficients = multitype_interaction_spectrum(response, maxima)
        self.assertEqual(coefficients[(0, 0)], 7)
        self.assertEqual(coefficients[(1, 0)], 5)
        self.assertEqual(coefficients[(0, 1)], -2)
        self.assertEqual(higher_interaction_support(coefficients), {})

    def test_pure_cross_pair_response_is_one_one_interaction(self):
        maxima = (3, 3)
        response = {
            (n, m): n * m
            for n, m in product(range(4), range(4))
        }
        coefficients = multitype_interaction_spectrum(response, maxima)
        self.assertEqual(coefficients[(1, 1)], 1)
        higher = higher_interaction_support(coefficients)
        self.assertEqual(higher, {(1, 1): 1})

    def test_same_type_pair_and_cross_type_interactions_are_distinct(self):
        maxima = (4, 4)
        response = {
            (n, m): 2 * (n * (n - 1) // 2) + 3 * n * m
            for n, m in product(range(5), range(5))
        }
        coefficients = multitype_interaction_spectrum(response, maxima)
        self.assertEqual(coefficients[(2, 0)], 2)
        self.assertEqual(coefficients[(1, 1)], 3)
        self.assertEqual(
            higher_interaction_support(coefficients),
            {(1, 1): 3, (2, 0): 2},
        )

    def test_reconstructs_arbitrary_small_integer_table_exactly(self):
        maxima = (2, 2)
        response = {
            (0, 0): 4,
            (0, 1): -1,
            (0, 2): 7,
            (1, 0): 3,
            (1, 1): 9,
            (1, 2): -5,
            (2, 0): 8,
            (2, 1): 1,
            (2, 2): 12,
        }
        coefficients = multitype_interaction_spectrum(response, maxima)
        for state, expected in response.items():
            self.assertEqual(reconstruct_multitype_response(coefficients, state), expected)

    def test_one_type_reduces_to_ordinary_binomial_interaction(self):
        response = {(n,): n ** 3 for n in range(6)}
        self.assertEqual(multitype_interaction_coefficient(response, (1,)), 1)
        self.assertEqual(multitype_interaction_coefficient(response, (2,)), 6)
        self.assertEqual(multitype_interaction_coefficient(response, (3,)), 6)
        self.assertEqual(multitype_interaction_coefficient(response, (4,)), 0)


if __name__ == "__main__":
    unittest.main()
