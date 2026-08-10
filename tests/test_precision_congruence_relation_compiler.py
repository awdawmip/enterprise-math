import unittest
from itertools import product

from enterprise_math.precision_congruence_relation_compiler import (
    additive_subgroup_holds,
    all_product_states,
    coset_partition,
    exact_prime_power_exponent,
    partition_is_translation_congruence,
    quotient_exponent_codimension,
    quotient_exponent_mass,
    quotient_invariant_exponents,
    quotient_torsion_counts,
)
from enterprise_math.precision_product_language_factorization import (
    coupled_and_observable,
    signature_partition,
)
from enterprise_math.precision_relation_rank_compiler import relation_vector


class PrecisionCongruenceRelationCompilerTests(unittest.TestCase):
    def test_exact_state_partition_has_full_ambient_exponent_profile(self):
        prime = 2
        cap = 3
        dimension = 2
        subgroup = ((0, 0),)
        partition = coset_partition(subgroup, prime, cap, dimension)
        self.assertTrue(partition_is_translation_congruence(partition, prime, cap, dimension))
        self.assertEqual(quotient_invariant_exponents(partition, prime, cap, dimension), (3, 3))
        self.assertEqual(quotient_exponent_mass(partition, prime, cap, dimension), 6)
        self.assertEqual(quotient_exponent_codimension(partition, prime, cap, dimension), 0)

    def test_killing_one_full_axis_leaves_one_relation_axis(self):
        prime = 2
        cap = 3
        modulus = prime**cap
        dimension = 2
        subgroup = tuple((value, 0) for value in range(modulus))
        self.assertTrue(additive_subgroup_holds(subgroup, prime, cap, dimension))
        partition = coset_partition(subgroup, prime, cap, dimension)
        self.assertEqual(quotient_invariant_exponents(partition, prime, cap, dimension), (3,))
        self.assertEqual(quotient_exponent_codimension(partition, prime, cap, dimension), 3)

    def test_mixed_depth_quotient_recovers_nonuniform_exponent_profile(self):
        prime = 2
        cap = 3
        dimension = 2
        # H = 2Z/8 on first axis, leaving Z/2 on axis 1 and full Z/8 on axis 2.
        subgroup = tuple((value, 0) for value in (0, 2, 4, 6))
        partition = coset_partition(subgroup, prime, cap, dimension)
        self.assertEqual(quotient_invariant_exponents(partition, prime, cap, dimension), (3, 1))
        self.assertEqual(quotient_torsion_counts(partition, prime, cap, dimension), (1, 4, 8, 16))
        self.assertEqual(quotient_exponent_mass(partition, prime, cap, dimension), 4)
        self.assertEqual(quotient_exponent_codimension(partition, prime, cap, dimension), 2)

    def test_relation_matrix_kernel_recovers_rank_profile(self):
        prime = 2
        cap = 2
        modulus = prime**cap
        matrix = ((1, 0, 1), (0, 1, 1))
        dimension = 3
        subgroup = tuple(
            state
            for state in product(range(modulus), repeat=dimension)
            if relation_vector(state, matrix, prime, cap) == (0, 0)
        )
        partition = coset_partition(subgroup, prime, cap, dimension)
        self.assertEqual(quotient_invariant_exponents(partition, prime, cap, dimension), (2, 2))
        self.assertEqual(quotient_exponent_codimension(partition, prime, cap, dimension), 2)

    def test_nonuniform_relation_depths_are_visible_without_smith_normal_form(self):
        prime = 3
        cap = 3
        dimension = 2
        # H = 3Z/27 x 9Z/27. Quotient is Z/3 x Z/9 -> profile (2,1).
        subgroup = tuple(
            (left, right)
            for left in range(0, 27, 3)
            for right in range(0, 27, 9)
        )
        partition = coset_partition(subgroup, prime, cap, dimension)
        self.assertEqual(quotient_invariant_exponents(partition, prime, cap, dimension), (2, 1))
        self.assertEqual(quotient_exponent_mass(partition, prime, cap, dimension), 3)
        self.assertEqual(quotient_exponent_codimension(partition, prime, cap, dimension), 3)

    def test_coupled_and_safe_partition_is_not_translation_congruence(self):
        diagonal = ((0, 0), (1, 1))
        cross = ((0, 1), (1, 0))
        diagonal_partition = signature_partition(diagonal, coupled_and_observable)
        cross_partition = signature_partition(cross, coupled_and_observable)
        self.assertFalse(partition_is_translation_congruence(diagonal_partition, 2, 1, 2))
        self.assertFalse(partition_is_translation_congruence(cross_partition, 2, 1, 2))
        with self.assertRaises(ValueError):
            quotient_invariant_exponents(diagonal_partition, 2, 1, 2)

    def test_exact_prime_power_exponent_rejects_non_power(self):
        self.assertEqual(exact_prime_power_exponent(1, 2), 0)
        self.assertEqual(exact_prime_power_exponent(27, 3), 3)
        with self.assertRaises(ValueError):
            exact_prime_power_exponent(12, 2)

    def test_coset_partition_covers_all_states(self):
        partition = coset_partition(((0, 0), (1, 0)), 2, 1, 2)
        union = set().union(*partition)
        self.assertEqual(union, set(all_product_states(2, 1, 2)))


if __name__ == "__main__":
    unittest.main()
