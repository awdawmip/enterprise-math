import unittest
from itertools import product

from enterprise_math.multitype_lego_interaction import multitype_interaction_spectrum
from enterprise_math.saturation_interaction import (
    min_has_nonzero_interaction_at_total_order,
    min_interaction_coefficient,
    min_requires_unbounded_interaction_order,
)


class SaturationInteractionTests(unittest.TestCase):
    def test_closed_form_matches_direct_multitype_interaction_coefficients(self):
        maximum = 6
        response = {
            (n, m): min(n, m)
            for n, m in product(range(maximum + 1), range(maximum + 1))
        }
        coefficients = multitype_interaction_spectrum(response, (maximum, maximum))
        for k in range(maximum + 1):
            for l in range(maximum + 1):
                self.assertEqual(coefficients[(k, l)], min_interaction_coefficient(k, l))

    def test_every_total_order_at_least_two_has_nonzero_interaction(self):
        for order in range(2, 20):
            self.assertTrue(min_has_nonzero_interaction_at_total_order(order))
        self.assertTrue(min_requires_unbounded_interaction_order(40))

    def test_small_closed_form_values(self):
        self.assertEqual(min_interaction_coefficient(1, 1), 1)
        self.assertEqual(min_interaction_coefficient(1, 2), -1)
        self.assertEqual(min_interaction_coefficient(2, 2), 2)
        self.assertEqual(min_interaction_coefficient(3, 3), 6)
        self.assertEqual(min_interaction_coefficient(4, 4), 20)


if __name__ == "__main__":
    unittest.main()
