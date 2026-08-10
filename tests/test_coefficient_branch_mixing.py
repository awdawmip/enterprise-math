import unittest

from enterprise_math.coefficient_branch_mixing import (
    CONSTANTS,
    branch_blocker_moduli,
    composite_zero_divisor_witness,
    labelled_branch_has_root_modulus,
    local_branch_choice,
    mod15_branch_mixing_witness,
    modular_ring_is_integral_domain,
    no_single_label_is_locally_solvable_everywhere,
    product_zero_without_labelled_branch,
)


class CoefficientBranchMixingTests(unittest.TestCase):
    def test_mod15_product_solution_has_no_labelled_mod15_branch(self):
        witness = mod15_branch_mixing_witness()
        self.assertEqual(witness.residue, 1)
        self.assertEqual(witness.modulus, 15)
        self.assertTrue(witness.product_zero_mod15)
        self.assertTrue(witness.no_global_mod15_branch)
        self.assertFalse(any(witness.factor_zero_mod15))

        # At p=3 the 13-branch vanishes; at p=5 the 221-branch vanishes.
        self.assertTrue(witness.factor_zero_mod3[0])
        self.assertTrue(witness.factor_zero_mod5[2])
        self.assertNotEqual(
            witness.factor_zero_mod3,
            witness.factor_zero_mod5,
        )
        self.assertTrue(product_zero_without_labelled_branch(1, 15))

    def test_prime_moduli_are_domains_composites_have_zero_divisors(self):
        primes = (2, 3, 5, 7, 11, 13, 17, 19)
        composites = (4, 6, 8, 9, 10, 12, 15, 16, 21, 25)
        for modulus in primes:
            self.assertTrue(modular_ring_is_integral_domain(modulus))
            self.assertIsNone(composite_zero_divisor_witness(modulus))
        for modulus in composites:
            self.assertFalse(modular_ring_is_integral_domain(modulus))
            pair = composite_zero_divisor_witness(modulus)
            self.assertIsNotNone(pair)
            assert pair is not None
            left, right = pair
            self.assertNotEqual(left % modulus, 0)
            self.assertNotEqual(right % modulus, 0)
            self.assertEqual((left * right) % modulus, 0)

    def test_each_labelled_branch_is_blocked_by_some_finite_precision(self):
        blockers = dict(branch_blocker_moduli())
        self.assertEqual(blockers, {13: 5, 17: 3, 221: 3})
        self.assertTrue(no_single_label_is_locally_solvable_everywhere())
        for constant in CONSTANTS:
            self.assertFalse(
                labelled_branch_has_root_modulus(
                    constant,
                    blockers[constant],
                )
            )

    def test_local_branch_choice_changes_across_prime_components(self):
        # Special primes deliberately choose different simple Hensel branches.
        self.assertEqual(local_branch_choice(13), 17)
        self.assertEqual(local_branch_choice(17), 13)

        choices = {
            prime: local_branch_choice(prime)
            for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
        }
        self.assertGreaterEqual(len(set(choices.values())), 2)
        self.assertTrue(set(choices.values()).issubset(set(CONSTANTS)))

    def test_prime_fields_preserve_product_zero_implies_one_factor_zero_for_reference_polynomial(self):
        for prime in (2, 3, 5, 7, 11, 13, 17, 19):
            for value in range(prime):
                mixed = product_zero_without_labelled_branch(value, prime)
                self.assertFalse(mixed, (prime, value))

    def test_modulus_one_is_trivial_precision_boundary(self):
        self.assertEqual(composite_zero_divisor_witness(1), (0, 0))
        self.assertFalse(modular_ring_is_integral_domain(1))

    def test_validation(self):
        with self.assertRaises(ValueError):
            modular_ring_is_integral_domain(0)
        with self.assertRaises(TypeError):
            modular_ring_is_integral_domain(True)
        with self.assertRaises(ValueError):
            labelled_branch_has_root_modulus(19, 5)


if __name__ == "__main__":
    unittest.main()
