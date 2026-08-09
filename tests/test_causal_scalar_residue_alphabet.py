import unittest

from enterprise_math.causal_local_alphabet_code import (
    binary_integer_alphabet,
    primitive_grade_and_multiplicity,
    ternary_hexagonal_alphabet,
    ternary_repetition_3_code,
)
from enterprise_math.causal_scalar_residue_alphabet import (
    nearest_residue_magnitude,
    scalar_integer_residue_alphabet,
    scalar_residue_minimum_multiplicity,
    ternary_repetition_scalar_shadow,
)


class CausalScalarResidueAlphabetTests(unittest.TestCase):
    def test_binary_scalar_alphabet_matches_existing_binary_integer_profile(self):
        self.assertEqual(scalar_integer_residue_alphabet(2), binary_integer_alphabet())

    def test_nearest_residue_magnitudes_generate_square_lee_weights(self):
        self.assertEqual(
            tuple(nearest_residue_magnitude(residue, 7) for residue in range(7)),
            (0, 1, 2, 3, 3, 2, 1),
        )
        alphabet = scalar_integer_residue_alphabet(7)
        self.assertEqual(alphabet.residue_grade, {0: 0, 1: 1, 2: 4, 3: 9, 4: 9, 5: 4, 6: 1})

    def test_even_half_residue_has_two_equal_minimum_signed_representatives(self):
        self.assertEqual(scalar_residue_minimum_multiplicity(3, 6), 2)
        self.assertEqual(scalar_residue_minimum_multiplicity(1, 6), 1)
        self.assertEqual(scalar_residue_minimum_multiplicity(2, 5), 1)

    def test_ternary_scalar_repetition_is_code_dominated_and_not_e6(self):
        regime, grade, multiplicity = ternary_repetition_scalar_shadow()
        self.assertEqual((regime, grade, multiplicity), ("code_dominated", 3, 2))

    def test_same_ternary_code_becomes_e6_only_after_hex_local_alphabet_change(self):
        code = ternary_repetition_3_code()
        scalar = primitive_grade_and_multiplicity(code, scalar_integer_residue_alphabet(3))
        hexagonal = primitive_grade_and_multiplicity(code, ternary_hexagonal_alphabet())
        self.assertEqual(scalar, (3, 2))
        self.assertEqual(hexagonal, (3, 72))


if __name__ == "__main__":
    unittest.main()
