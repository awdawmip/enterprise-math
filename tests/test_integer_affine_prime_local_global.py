import unittest

from enterprise_math.integer_affine_fiber_diagnostic import (
    integrally_reachable,
    modularly_reachable,
)
from enterprise_math.integer_affine_prime_local_global import (
    integer_is_squarefree,
    prime_only_false_positive_is_solvable_for_every_prime,
    prime_only_false_positive_witness,
    prime_only_local_global_complete_for_all_targets,
    prime_power_depths_required_by_torsion,
)


class IntegerAffinePrimeLocalGlobalTests(unittest.TestCase):
    def test_squarefree_torsion_exponent_requires_only_prime_depth_one(self):
        matrix = ((6,),)
        self.assertTrue(prime_only_local_global_complete_for_all_targets(matrix))
        self.assertEqual(
            prime_power_depths_required_by_torsion(matrix),
            ((2, 1), (3, 1)),
        )

    def test_repeated_prime_torsion_requires_deeper_prime_power(self):
        matrix = ((12,),)
        self.assertFalse(prime_only_local_global_complete_for_all_targets(matrix))
        self.assertEqual(
            prime_power_depths_required_by_torsion(matrix),
            ((2, 2), (3, 1)),
        )

    def test_four_x_equals_two_passes_every_prime_but_fails_exactly(self):
        coefficient = ((4,),)
        target = (2,)
        self.assertFalse(integrally_reachable(coefficient, target))
        for prime in (2, 3, 5, 7, 11, 13, 17, 19):
            self.assertTrue(modularly_reachable(coefficient, target, prime))
        self.assertFalse(modularly_reachable(coefficient, target, 4))

    def test_universal_prime_only_false_positive_witness_at_multiple_depths(self):
        for prime, depth in ((2, 2), (2, 4), (3, 2), (5, 3)):
            witness = prime_only_false_positive_witness(prime, depth)
            self.assertFalse(witness.exact_reachable)
            for tested_prime in (2, 3, 5, 7, 11, 13):
                self.assertTrue(
                    prime_only_false_positive_is_solvable_for_every_prime(
                        witness,
                        tested_prime,
                    )
                )
            self.assertFalse(
                modularly_reachable(
                    ((witness.coefficient,),),
                    (witness.target,),
                    prime ** depth,
                )
            )

    def test_free_cokernel_does_not_create_a_prime_power_depth_requirement(self):
        matrix = (
            (1,),
            (0,),
        )
        # Torsion exponent is one, so the p-adic depth list is empty even though
        # the map has one free cokernel direction.  Infinite prime breadth (or an
        # unbounded single-prime ladder) is what detects that free coordinate.
        self.assertTrue(prime_only_local_global_complete_for_all_targets(matrix))
        self.assertEqual(prime_power_depths_required_by_torsion(matrix), ())

        unreachable = (0, 6)
        self.assertFalse(integrally_reachable(matrix, unreachable))
        self.assertTrue(modularly_reachable(matrix, unreachable, 2))
        self.assertTrue(modularly_reachable(matrix, unreachable, 3))
        self.assertFalse(modularly_reachable(matrix, unreachable, 5))

    def test_squarefree_utility(self):
        for value in (1, 2, 3, 6, 30, 210):
            self.assertTrue(integer_is_squarefree(value))
        for value in (4, 8, 12, 18, 45):
            self.assertFalse(integer_is_squarefree(value))

    def test_validation(self):
        with self.assertRaises(ValueError):
            prime_only_false_positive_witness(2, 1)
        with self.assertRaises(ValueError):
            prime_only_false_positive_witness(4, 2)
        with self.assertRaises(ValueError):
            integer_is_squarefree(0)
        with self.assertRaises(TypeError):
            integer_is_squarefree(True)


if __name__ == "__main__":
    unittest.main()
