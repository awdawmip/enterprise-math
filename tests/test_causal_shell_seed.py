import unittest

from enterprise_math.causal_code_lattice import even_parity_code, extended_hamming_8_code
from enterprise_math.causal_code_root_shadow import simplex_7_code
from enterprise_math.causal_local_alphabet_code import (
    binary_integer_alphabet,
    ternary_hamming_4_code,
    ternary_hexagonal_alphabet,
    ternary_repetition_3_code,
)
from enterprise_math.causal_shell_seed import causal_shell_seed, primitive_shell_from_seed


class CausalShellSeedTests(unittest.TestCase):
    def test_binary_e8_seed_has_240_primitive_grade_four_events(self):
        seed = causal_shell_seed(extended_hamming_8_code(), binary_integer_alphabet())
        self.assertEqual(seed, {4: 240, 8: 256})
        self.assertEqual(primitive_shell_from_seed(seed), (4, 240))

    def test_binary_e7_seed_has_126_primitive_grade_four_events(self):
        seed = causal_shell_seed(simplex_7_code(), binary_integer_alphabet())
        self.assertEqual(seed, {4: 126})
        self.assertEqual(primitive_shell_from_seed(seed), (4, 126))

    def test_binary_even_parity_seed_is_code_dominated_at_grade_two(self):
        code = even_parity_code(4)
        seed = causal_shell_seed(code, binary_integer_alphabet())
        self.assertEqual(primitive_shell_from_seed(seed), (2, 24))
        self.assertIn(4, seed)  # old local axis shell survives at higher grade

    def test_ternary_hex_e6_and_e8_have_resonant_grade_three_seeds(self):
        e6 = causal_shell_seed(ternary_repetition_3_code(), ternary_hexagonal_alphabet())
        e8 = causal_shell_seed(ternary_hamming_4_code(), ternary_hexagonal_alphabet())
        self.assertEqual(e6, {3: 72})
        self.assertEqual(e8, {3: 240})
        self.assertEqual(primitive_shell_from_seed(e6), (3, 72))
        self.assertEqual(primitive_shell_from_seed(e8), (3, 240))


if __name__ == "__main__":
    unittest.main()
