import unittest

from enterprise_math.causal_code_lattice import even_parity_code
from enterprise_math.causal_local_alphabet_code import (
    ternary_hamming_4_code,
    ternary_repetition_3_code,
)
from enterprise_math.causal_residue_conservation import (
    binary_single_parity_check,
    minimum_nonzero_support,
    residue_kernel,
    support_histogram,
    ternary_hamming_4_checks,
    ternary_repetition_checks,
)


class CausalResidueConservationTests(unittest.TestCase):
    def test_binary_single_parity_code_is_exact_kernel_of_one_conservation_check(self):
        for length in range(2, 8):
            kernel = residue_kernel(binary_single_parity_check(length), 2)
            self.assertEqual(set(kernel), set(even_parity_code(length)))
            self.assertEqual(minimum_nonzero_support(kernel), 2)

    def test_ternary_repetition_code_is_kernel_of_equality_checks(self):
        kernel = residue_kernel(ternary_repetition_checks(), 3)
        self.assertEqual(set(kernel), set(ternary_repetition_3_code()))
        self.assertEqual(support_histogram(kernel), {0: 1, 3: 2})
        self.assertEqual(minimum_nonzero_support(kernel), 3)

    def test_ternary_hamming_code_is_kernel_of_two_conservation_checks(self):
        kernel = residue_kernel(ternary_hamming_4_checks(), 3)
        self.assertEqual(set(kernel), set(ternary_hamming_4_code()))
        self.assertEqual(support_histogram(kernel), {0: 1, 3: 8})
        self.assertEqual(minimum_nonzero_support(kernel), 3)


if __name__ == "__main__":
    unittest.main()
