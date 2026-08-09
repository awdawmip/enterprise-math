import unittest

from enterprise_math.causal_code_lattice import extended_hamming_8_code
from enterprise_math.causal_code_root_shadow import simplex_7_code
from enterprise_math.causal_local_alphabet_code import (
    binary_integer_alphabet,
    codeword_grade,
    codeword_minimum_lift_multiplicity,
    e6_primitive_shadow,
    primitive_grade_and_multiplicity,
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

    def test_binary_integer_alphabet_recovers_e7_and_e8_counts(self):
        alphabet = binary_integer_alphabet()
        self.assertEqual(primitive_grade_and_multiplicity(simplex_7_code(), alphabet), (4, 126))
        self.assertEqual(primitive_grade_and_multiplicity(extended_hamming_8_code(), alphabet), (4, 240))

    def test_code_alone_does_not_fix_geometry_without_local_alphabet(self):
        code = ternary_repetition_3_code()
        hex_grade, hex_count = primitive_grade_and_multiplicity(code, ternary_hexagonal_alphabet())
        self.assertEqual((hex_grade, hex_count), (3, 72))
        # The binary alphabet does not even contain ternary symbol 2; this is a
        # deliberate type failure rather than silently projecting code symbols.
        with self.assertRaises(ValueError):
            primitive_grade_and_multiplicity(code, binary_integer_alphabet())


if __name__ == "__main__":
    unittest.main()
