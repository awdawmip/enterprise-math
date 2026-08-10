import unittest

from enterprise_math.abc_prime_cube_cyclotomic_congruence import (
    prime_cube_cyclotomic_congruence_signature,
)
from enterprise_math.abc_prime_cube_cyclotomic_incidence import (
    cyclotomic_signature_incidence_envelope,
    repeated_modulus_minimum,
    root_class_compression_ratio_lower_bound,
)


class PrimeCubeCyclotomicIncidenceTests(unittest.TestCase):
    def test_single_repeated_prime_square_reduces_pair_space(self) -> None:
        sig = prime_cube_cyclotomic_congruence_signature(5, 59, "sum")
        envelope = cyclotomic_signature_incidence_envelope(sig, 1000)
        self.assertEqual(envelope.repeated_modulus, 169)
        self.assertEqual(envelope.root_choice_count, 2)
        self.assertEqual(envelope.candidates_per_q_per_root, 6)
        self.assertEqual(envelope.ordered_integer_pair_bound, 12_000)
        self.assertLess(envelope.ordered_integer_pair_bound, 1_000_000)

    def test_large_modulus_enters_one_dimensional_regime(self) -> None:
        sig = prime_cube_cyclotomic_congruence_signature(13, 109, "difference")
        envelope = cyclotomic_signature_incidence_envelope(sig, 1000)
        self.assertEqual(envelope.repeated_modulus, 67**2)
        self.assertEqual(envelope.candidates_per_q_per_root, 1)
        self.assertEqual(envelope.ordered_integer_pair_bound, 2_000)

    def test_trivial_signature_recovers_ambient_pair_bound(self) -> None:
        sig = prime_cube_cyclotomic_congruence_signature(3, 7, "sum")
        envelope = cyclotomic_signature_incidence_envelope(sig, 100)
        self.assertEqual(envelope.repeated_modulus, 1)
        self.assertEqual(envelope.root_choice_count, 1)
        self.assertEqual(envelope.ordered_integer_pair_bound, 10_000)

    def test_each_repeated_prime_costs_at_least_49_over_2_in_ratio_space(self) -> None:
        for k in range(5):
            self.assertEqual(repeated_modulus_minimum(k), 49**k)
            self.assertEqual(
                root_class_compression_ratio_lower_bound(k),
                (49**k, 2**k),
            )


if __name__ == "__main__":
    unittest.main()
