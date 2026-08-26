import unittest

from enterprise_math.p018_p023_prime_four_horizon import (
    binary_prime_four_formula_matches_direct,
    binary_prime_four_required_horizon,
    minimal_boundary_for_prime_four_length,
    prime_four_required_horizon,
    prime_four_shortest_word_length,
)
from enterprise_math.p018_p023_quotient_word_basis import (
    prime_generator_required_horizon,
)


class P018P023PrimeFourHorizonTests(unittest.TestCase):
    def test_weighted_shell_minimum_matches_direct_shortest_lengths(self):
        for length in range(1, 7):
            boundary = minimal_boundary_for_prime_four_length(length)
            self.assertEqual(prime_four_shortest_word_length(boundary), length)
            for smaller in range(2, boundary):
                self.assertLess(prime_four_shortest_word_length(smaller), length)

    def test_binary_closed_form_matches_independent_packing_oracle(self):
        for max_state in range(2, 160):
            root_exp = max_state.bit_length()
            self.assertLess(max_state, 2**root_exp)
            self.assertTrue(
                binary_prime_four_formula_matches_direct(max_state, root_exp)
            )

    def test_single_macro_changes_logarithmic_depth_scale(self):
        cases = (
            (16, 4, 2),
            (32, 5, 3),
            (64, 6, 4),
            (128, 7, 4),
            (1024, 10, 6),
        )
        for max_state, prime_depth, prime_four_depth in cases:
            root_exp = max_state.bit_length()
            self.assertEqual(
                prime_generator_required_horizon(max_state, root_exp),
                prime_depth,
            )
            self.assertEqual(
                binary_prime_four_required_horizon(max_state, root_exp),
                prime_four_depth,
            )
            self.assertEqual(
                prime_four_required_horizon(max_state, root_exp),
                prime_four_depth,
            )


if __name__ == "__main__":
    unittest.main()
