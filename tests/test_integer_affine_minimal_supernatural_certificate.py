import itertools
import unittest

from enterprise_math.integer_affine_fiber_diagnostic import (
    integrally_reachable,
    modularly_reachable,
)
from enterprise_math.integer_affine_minimal_supernatural_certificate import (
    free_cokernel_rank,
    minimal_single_prime_ladder_modulus,
    minimal_supernatural_certificate,
)


class IntegerAffineMinimalSupernaturalCertificateTests(unittest.TestCase):
    def test_full_row_rank_has_unique_finite_least_certificate(self):
        matrix = (
            (2, 0),
            (0, 6),
        )
        certificate = minimal_supernatural_certificate(matrix)
        self.assertTrue(certificate.finite)
        self.assertEqual(certificate.torsion_exponent, 6)
        self.assertEqual(certificate.free_cokernel_rank, 0)
        self.assertIsNone(certificate.infinite_prime)
        self.assertEqual(
            certificate.finite_required_prime_depths,
            ((2, 1), (3, 1)),
        )
        with self.assertRaises(ValueError):
            minimal_supernatural_certificate(matrix, infinite_prime=2)

    def test_free_cokernel_requires_one_chosen_infinite_prime(self):
        matrix = (
            (12,),
            (0,),
        )
        self.assertEqual(free_cokernel_rank(matrix), 1)

        at_two = minimal_supernatural_certificate(matrix, infinite_prime=2)
        self.assertFalse(at_two.finite)
        self.assertEqual(at_two.torsion_exponent, 12)
        self.assertEqual(at_two.infinite_prime, 2)
        self.assertEqual(at_two.finite_required_prime_depths, ((3, 1),))

        at_five = minimal_supernatural_certificate(matrix, infinite_prime=5)
        self.assertEqual(at_five.infinite_prime, 5)
        self.assertEqual(
            at_five.finite_required_prime_depths,
            ((2, 2), (3, 1)),
        )

        with self.assertRaises(ValueError):
            minimal_supernatural_certificate(matrix)

    def test_E_times_one_prime_ladder_detects_torsion_immediately_and_free_eventually(self):
        matrix = (
            (12,),
            (0,),
        )
        prime = 5

        # Pure torsion obstruction: not divisible by 12 in the rational-image
        # coordinate, so it already fails at level zero (mod E).
        torsion_target = (6, 0)
        self.assertFalse(integrally_reachable(matrix, torsion_target))
        modulus0 = minimal_single_prime_ladder_modulus(matrix, prime, 0)
        self.assertEqual(modulus0, 12)
        self.assertFalse(modularly_reachable(matrix, torsion_target, modulus0))

        # Free obstruction chosen to pass levels 0,1,2 and fail at 3.
        free_target = (0, 12 * (prime ** 2))
        self.assertFalse(integrally_reachable(matrix, free_target))
        flags = tuple(
            modularly_reachable(
                matrix,
                free_target,
                minimal_single_prime_ladder_modulus(matrix, prime, level),
            )
            for level in range(5)
        )
        self.assertEqual(flags, (True, True, True, False, False))

    def test_any_chosen_prime_direction_is_uniformly_separating_on_bounded_sample(self):
        matrix = (
            (6,),
            (0,),
        )
        targets = tuple(itertools.product(range(-8, 9), repeat=2))
        for prime in (2, 3, 5, 7):
            minimal_supernatural_certificate(matrix, infinite_prime=prime)
            for target in targets:
                exact = integrally_reachable(matrix, target)
                # A finite sample only needs finitely many ladder levels; search a
                # conservative range sufficient for these bounded targets.
                passes_all_checked = all(
                    modularly_reachable(
                        matrix,
                        target,
                        minimal_single_prime_ladder_modulus(matrix, prime, level),
                    )
                    for level in range(0, 8)
                )
                self.assertEqual(
                    passes_all_checked,
                    exact,
                    (prime, target),
                )

    def test_validation(self):
        with self.assertRaises(ValueError):
            minimal_supernatural_certificate(((1,), (0,)), infinite_prime=4)
        with self.assertRaises(ValueError):
            minimal_single_prime_ladder_modulus(((1,), (0,)), 2, -1)
        with self.assertRaises(TypeError):
            minimal_single_prime_ladder_modulus(((1,), (0,)), True, 1)


if __name__ == "__main__":
    unittest.main()
