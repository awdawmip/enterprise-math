import unittest

from enterprise_math.causal_code_lattice import extended_hamming_8_code
from enterprise_math.causal_code_root_shadow import simplex_7_code
from enterprise_math.causal_support_uniformity import (
    codeword_supports,
    incidence_histogram,
    nontrivial_uniformity_depth,
    uniform_incidence_value,
)


class CausalSupportUniformityTests(unittest.TestCase):
    def test_e7_weight_four_supports_are_uniform_through_pairs_but_not_triples(self):
        supports = codeword_supports(simplex_7_code(), 4)
        self.assertEqual(len(supports), 7)
        self.assertEqual(incidence_histogram(7, supports, 1), {4: 7})
        self.assertEqual(incidence_histogram(7, supports, 2), {2: 21})
        self.assertEqual(incidence_histogram(7, supports, 3), {0: 7, 1: 28})
        self.assertEqual(nontrivial_uniformity_depth(7, supports), 2)

    def test_e8_weight_four_supports_have_uniform_triple_incidence_one(self):
        supports = codeword_supports(extended_hamming_8_code(), 4)
        self.assertEqual(len(supports), 14)
        self.assertEqual(incidence_histogram(8, supports, 1), {7: 8})
        self.assertEqual(incidence_histogram(8, supports, 2), {3: 28})
        self.assertEqual(incidence_histogram(8, supports, 3), {1: 56})
        self.assertEqual(uniform_incidence_value(8, supports, 3), 1)
        self.assertEqual(nontrivial_uniformity_depth(8, supports), 3)

    def test_uniformity_breaks_at_full_weight_four_context_for_e8(self):
        supports = codeword_supports(extended_hamming_8_code(), 4)
        self.assertEqual(incidence_histogram(8, supports, 4), {0: 56, 1: 14})


if __name__ == "__main__":
    unittest.main()
