import unittest
from itertools import product
from math import comb

from enterprise_math.interaction_type_collapse import (
    induced_coarse_interaction_spectrum,
    interaction_spectrum_descends,
)
from enterprise_math.multitype_lego_interaction import multitype_interaction_spectrum


class InteractionTypeCollapseTests(unittest.TestCase):
    def test_total_count_descends_when_two_fine_types_are_merged(self):
        maxima = (3, 3)
        response = {(n, m): n + m for n, m in product(range(4), range(4))}
        coefficients = multitype_interaction_spectrum(response, maxima)
        self.assertTrue(interaction_spectrum_descends(coefficients, (0, 0), 1))
        coarse = induced_coarse_interaction_spectrum(coefficients, (0, 0), 1)
        self.assertEqual(coarse[(1,)], 1)
        self.assertEqual(coarse[(2,)], 0)

    def test_choose_two_from_total_descends_by_vandermonde(self):
        maxima = (3, 3)
        response = {
            (n, m): comb(n + m, 2)
            for n, m in product(range(4), range(4))
        }
        coefficients = multitype_interaction_spectrum(response, maxima)
        # Fine orders (2,0), (1,1), (0,2) all carry the same coefficient 1.
        self.assertEqual(coefficients[(2, 0)], 1)
        self.assertEqual(coefficients[(1, 1)], 1)
        self.assertEqual(coefficients[(0, 2)], 1)
        self.assertTrue(interaction_spectrum_descends(coefficients, (0, 0), 1))
        coarse = induced_coarse_interaction_spectrum(coefficients, (0, 0), 1)
        self.assertEqual(coarse[(2,)], 1)

    def test_cross_only_interaction_does_not_descend_to_total_count(self):
        maxima = (3, 3)
        response = {(n, m): n * m for n, m in product(range(4), range(4))}
        coefficients = multitype_interaction_spectrum(response, maxima)
        self.assertEqual(coefficients[(1, 1)], 1)
        self.assertEqual(coefficients[(2, 0)], 0)
        self.assertEqual(coefficients[(0, 2)], 0)
        self.assertFalse(interaction_spectrum_descends(coefficients, (0, 0), 1))
        with self.assertRaises(ValueError):
            induced_coarse_interaction_spectrum(coefficients, (0, 0), 1)

    def test_partial_type_merge_checks_only_blockwise_selected_counts(self):
        maxima = (2, 2, 2)
        # Response depends on total of types 0+1 and separately on type 2.
        response = {
            (a, b, c): 3 * (a + b) + 5 * c + comb(a + b, 2) * c
            for a, b, c in product(range(3), range(3), range(3))
        }
        coefficients = multitype_interaction_spectrum(response, maxima)
        self.assertTrue(interaction_spectrum_descends(coefficients, (0, 0, 1), 2))


if __name__ == "__main__":
    unittest.main()
