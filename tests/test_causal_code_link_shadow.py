import unittest

from enterprise_math.causal_code_lattice import extended_hamming_8_code
from enterprise_math.causal_code_link_shadow import (
    axis_primitive_link_degree_from_code,
    coordinate_weight_four_incidence,
    coxeter_shadow_from_code_incidence,
    grade_four_root_count,
    incidence_formula_link_degree,
    uniform_weight_four_incidence,
    weight_four_incidence_is_uniform,
)
from enterprise_math.causal_code_root_shadow import simplex_7_code


class CausalCodeLinkShadowTests(unittest.TestCase):
    def test_e7_simplex_weight_four_support_incidence_is_uniform_four(self):
        code = simplex_7_code()
        self.assertEqual(coordinate_weight_four_incidence(code), (4,) * 7)
        self.assertTrue(weight_four_incidence_is_uniform(code))
        self.assertEqual(uniform_weight_four_incidence(code), 4)
        self.assertEqual(axis_primitive_link_degree_from_code(code), 32)
        self.assertEqual(incidence_formula_link_degree(code), 32)
        self.assertEqual(grade_four_root_count(code), 126)
        self.assertEqual(coxeter_shadow_from_code_incidence(code), 18)

    def test_e8_extended_hamming_support_incidence_is_uniform_seven(self):
        code = extended_hamming_8_code()
        self.assertEqual(coordinate_weight_four_incidence(code), (7,) * 8)
        self.assertTrue(weight_four_incidence_is_uniform(code))
        self.assertEqual(uniform_weight_four_incidence(code), 7)
        self.assertEqual(axis_primitive_link_degree_from_code(code), 56)
        self.assertEqual(incidence_formula_link_degree(code), 56)
        self.assertEqual(grade_four_root_count(code), 240)
        self.assertEqual(coxeter_shadow_from_code_incidence(code), 30)


if __name__ == "__main__":
    unittest.main()
