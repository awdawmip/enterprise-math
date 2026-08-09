import unittest

from enterprise_math.causal_code_lattice import (
    construction_a_primitive_events,
    extended_hamming_8_code,
    weight_histogram,
)
from enterprise_math.causal_code_root_shadow import (
    coxeter_shadow_from_root_count,
    e7_causal_root_count,
    e8_causal_root_count,
    grade_four_primitive_count_from_weight_spectrum,
    simplex_7_code,
)


class CausalCodeRootShadowTests(unittest.TestCase):
    def test_simplex_7_code_has_seven_weight_four_nonzero_words(self):
        code = simplex_7_code()
        self.assertEqual(len(code), 8)
        self.assertEqual(weight_histogram(code), {0: 1, 4: 7})
        self.assertEqual(len(construction_a_primitive_events(code)), 126)

    def test_e7_and_e8_root_counts_are_generated_by_code_weight_four_spectrum(self):
        self.assertEqual(e7_causal_root_count(), 126)
        self.assertEqual(e8_causal_root_count(), 240)
        self.assertEqual(
            grade_four_primitive_count_from_weight_spectrum(simplex_7_code()),
            126,
        )
        self.assertEqual(
            grade_four_primitive_count_from_weight_spectrum(extended_hamming_8_code()),
            240,
        )

    def test_coxeter_numbers_are_root_count_per_rank_shadows_here(self):
        self.assertEqual(coxeter_shadow_from_root_count(7, 126), 18)
        self.assertEqual(coxeter_shadow_from_root_count(8, 240), 30)


if __name__ == "__main__":
    unittest.main()
