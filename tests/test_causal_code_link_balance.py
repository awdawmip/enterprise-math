import unittest

from enterprise_math.causal_code_lattice import extended_hamming_8_code
from enterprise_math.causal_code_link_balance import (
    axis_link_degrees,
    coordinate_incidence,
    glue_link_degrees,
    homogeneity_balance_identity,
    intersection_two_counts,
    provenance_degree_is_uniform,
    support_intersection_histogram,
)
from enterprise_math.causal_code_root_shadow import simplex_7_code


class CausalCodeLinkBalanceTests(unittest.TestCase):
    def test_e7_support_system_satisfies_axis_glue_balance(self):
        code = simplex_7_code()
        self.assertEqual(coordinate_incidence(code), (4,) * 7)
        self.assertEqual(intersection_two_counts(code), (6,) * 7)
        self.assertEqual(axis_link_degrees(code), (32,) * 7)
        self.assertEqual(glue_link_degrees(code), (32,) * 7)
        self.assertTrue(homogeneity_balance_identity(code))
        self.assertTrue(provenance_degree_is_uniform(code))
        self.assertEqual(support_intersection_histogram(code), {2: 21})

    def test_e8_support_system_satisfies_axis_glue_balance(self):
        code = extended_hamming_8_code()
        self.assertEqual(coordinate_incidence(code), (7,) * 8)
        self.assertEqual(intersection_two_counts(code), (12,) * 14)
        self.assertEqual(axis_link_degrees(code), (56,) * 8)
        self.assertEqual(glue_link_degrees(code), (56,) * 14)
        self.assertTrue(homogeneity_balance_identity(code))
        self.assertTrue(provenance_degree_is_uniform(code))
        self.assertEqual(support_intersection_histogram(code), {0: 7, 2: 84})


if __name__ == "__main__":
    unittest.main()
