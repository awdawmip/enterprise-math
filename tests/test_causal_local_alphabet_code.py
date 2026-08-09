import unittest

from enterprise_math.causal_code_lattice import extended_hamming_8_code, even_parity_code
from enterprise_math.causal_code_root_shadow import simplex_7_code
from enterprise_math.causal_local_alphabet_code import (
    binary_integer_alphabet,
    codeword_grade,
    codeword_minimum_lift_multiplicity,
    e6_primitive_shadow,
    primitive_grade_and_multiplicity,
    primitive_grade_regime,
    ternary_e8_primitive_shadow,
    ternary_hamming_4_code,
    ternary_hexagonal_alphabet,
    ternary_repetition_3_code,
)


class CausalLocalAlphabetCodeTests(unittest.TestCase):
    def test_e6_ternary_hexagonal_shadow_is_grade_three_with_72_primitives(self):
        grade, multiplicity = e6_primitive_shadow()
        self.assertEqual(grade, 3)
        self.assertEqual(multiplicity, 72)
        alphabet = ternary_hexagonal_alphabet()
        code = ternary_repetition_3_code()
        self.assertEqual(codeword_grade(code[1], alphabet), 3)
        self.assertEqual(codeword_minimum_lift_multiplicity(code[1], alphabet), 27)
        self.assertEqual(codeword_minimum_lift_multiplicity(code[2], alphabet), 27)
        self.assertEqual(3 * 6 + 2 * 27, 72)
        self.assertEqual(primitive_grade_regime(code, alphabet), "resonant")

    def test_binary_integer_alphabet_recovers_e7_and_e8_counts(self):
        alphabet = binary_integer_alphabet()
        self.assertEqual(primitive_grade_and_multiplicity(simplex_7_code(), alphabet), (4, 126))
        self.assertEqual(primitive_grade_and_multiplicity(extended_hamming_8_code(), alphabet), (4, 240))
        self.assertEqual(primitive_grade_regime(simplex_7_code(), alphabet), "resonant")
        self.assertEqual(primitive_grade_regime(extended_hamming_8_code(), alphabet), "resonant")

    def test_binary_single_parity_code_is_code_dominated_d_regime(self):
        alphabet = binary_integer_alphabet()
        code = even_parity_code(6)
        self.assertEqual(primitive_grade_regime(code, alphabet), "code_dominated")
        self.assertEqual(primitive_grade_and_multiplicity(code, alphabet)[0], 2)

    def test_ternary_hamming_four_code_has_eight_weight_three_words_and_e8_shadow(self):
        code = ternary_hamming_4_code()
        weights = sorted(sum(symbol != 0 for symbol in word) for word in code)
        self.assertEqual(weights, [0] + [3] * 8)
        self.assertEqual(primitive_grade_regime(code, ternary_hexagonal_alphabet()), "resonant")
        self.assertEqual(ternary_e8_primitive_shadow(), (3, 240))
        self.assertEqual(4 * 6 + 8 * 27, 240)

    def test_same_e8_primitive_count_can_have_binary_or_ternary_causal_origin(self):
        binary = primitive_grade_and_multiplicity(
            extended_hamming_8_code(), binary_integer_alphabet()
        )
        ternary = ternary_e8_primitive_shadow()
        self.assertEqual(binary[1], 240)
        self.assertEqual(ternary[1], 240)
        self.assertNotEqual(binary[0], ternary[0])  # local grade normalization/alphabet differs

    def test_code_alone_does_not_fix_geometry_without_local_alphabet(self):
        code = ternary_repetition_3_code()
        hex_grade, hex_count = primitive_grade_and_multiplicity(code, ternary_hexagonal_alphabet())
        self.assertEqual((hex_grade, hex_count), (3, 72))
        with self.assertRaises(ValueError):
            primitive_grade_and_multiplicity(code, binary_integer_alphabet())


if __name__ == "__main__":
    unittest.main()
