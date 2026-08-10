import itertools
import unittest

from enterprise_math.integer_affine_fiber_diagnostic import (
    integrally_reachable,
    modularly_reachable,
)
from enterprise_math.integer_affine_local_global import (
    affine_finite_local_global_report,
    bounded_target_certificate_modulus,
    cokernel_torsion_exponent,
    integer_left_nullspace_rows,
    left_nullspace_target_values,
    local_global_countermodulus,
    local_global_prime_power_counterexample,
    prime_power_components,
    target_specific_certificate_modulus,
)


class IntegerAffineLocalGlobalTests(unittest.TestCase):
    def test_left_nullspace_detects_rational_free_obstruction(self):
        matrix = (
            (2, 0),
            (0, 0),
        )
        rows = integer_left_nullspace_rows(matrix)
        self.assertEqual(rows, ((0, 1),))
        self.assertEqual(left_nullspace_target_values(matrix, (1, 0)), (0,))
        self.assertEqual(left_nullspace_target_values(matrix, (0, 5)), (5,))

    def test_torsion_only_scalar_certificate_is_smith_exponent(self):
        matrix = ((6,),)
        self.assertEqual(cokernel_torsion_exponent(matrix), 6)

        reachable = affine_finite_local_global_report(matrix, (12,))
        self.assertTrue(reachable.exact_reachable)
        self.assertEqual(reachable.certificate_modulus, 6)
        self.assertTrue(reachable.certificate_modulus_solvable)

        obstructed = affine_finite_local_global_report(matrix, (4,))
        self.assertFalse(obstructed.exact_reachable)
        self.assertEqual(obstructed.certificate_modulus, 6)
        self.assertFalse(obstructed.certificate_modulus_solvable)
        self.assertIn(
            local_global_prime_power_counterexample(matrix, (4,)),
            (2, 3),
        )

    def test_free_cokernel_bound_forces_rational_image_before_torsion_test(self):
        matrix = (
            (2,),
            (0,),
        )
        report = affine_finite_local_global_report(matrix, (0, 5))
        self.assertFalse(report.exact_reachable)
        self.assertEqual(report.left_nullspace_target_values, (5,))
        self.assertEqual(report.free_obstruction_bound, 5)
        self.assertEqual(report.torsion_exponent, 2)
        self.assertGreater(report.certificate_modulus, 5)
        self.assertEqual(report.certificate_modulus % 2, 0)
        self.assertFalse(report.certificate_modulus_solvable)

    def test_rational_but_nonintegral_target_is_detected_after_free_part_vanishes(self):
        matrix = (
            (2, 0),
            (0, 6),
        )
        report = affine_finite_local_global_report(matrix, (1, 3))
        self.assertEqual(report.left_nullspace_rows, ())
        self.assertEqual(report.free_obstruction_bound, 0)
        self.assertEqual(report.torsion_exponent, 6)
        self.assertEqual(report.certificate_modulus, 6)
        self.assertFalse(report.exact_reachable)
        self.assertFalse(report.certificate_modulus_solvable)

    def test_target_specific_certificate_matches_exact_reachability_on_small_matrices(self):
        matrices = tuple(
            (
                (entries[0], entries[1]),
                (entries[2], entries[3]),
            )
            for entries in itertools.product((-1, 0, 1), repeat=4)
        )
        targets = tuple(itertools.product(range(-2, 3), repeat=2))
        for matrix in matrices:
            for target in targets:
                modulus = target_specific_certificate_modulus(matrix, target)
                self.assertGreaterEqual(modulus, 1)
                self.assertEqual(
                    integrally_reachable(matrix, target),
                    modularly_reachable(matrix, target, modulus),
                    (matrix, target, modulus),
                )

    def test_one_uniform_modulus_certifies_every_target_in_a_bounded_box(self):
        matrices = (
            ((2, 0), (0, 0)),
            ((2, 0), (0, 6)),
            ((1, 1), (0, 0)),
            ((0, 0), (0, 0)),
        )
        bound = 3
        targets = tuple(itertools.product(range(-bound, bound + 1), repeat=2))
        for matrix in matrices:
            modulus = bounded_target_certificate_modulus(matrix, bound)
            for target in targets:
                self.assertEqual(
                    integrally_reachable(matrix, target),
                    modularly_reachable(matrix, target, modulus),
                    (matrix, target, modulus),
                )

    def test_prime_power_family_is_equivalent_to_certificate_modulus_by_crt(self):
        matrix = (
            (6, 0),
            (0, 0),
        )
        target = (3, 5)
        report = affine_finite_local_global_report(matrix, target)
        self.assertEqual(
            report.prime_power_certificate_moduli,
            prime_power_components(report.certificate_modulus),
        )
        self.assertEqual(
            report.certificate_modulus_solvable,
            report.prime_power_family_solvable,
        )

    def test_exact_unreachability_always_has_a_finite_and_prime_power_counterexample(self):
        examples = (
            (((2,),), (1,)),
            ((((2,), (0,))), (0, 1)),
            ((((2, 0), (0, 6))), (1, 3)),
            ((((1, 0), (0, 0))), (0, 7)),
        )
        for matrix, target in examples:
            self.assertFalse(integrally_reachable(matrix, target))
            modulus = local_global_countermodulus(matrix, target)
            self.assertIsNotNone(modulus)
            assert modulus is not None
            self.assertFalse(modularly_reachable(matrix, target, modulus))
            prime_power = local_global_prime_power_counterexample(matrix, target)
            self.assertIsNotNone(prime_power)
            assert prime_power is not None
            self.assertFalse(modularly_reachable(matrix, target, prime_power))

    def test_reachable_targets_have_no_local_counterexample(self):
        examples = (
            (((2,),), (4,)),
            ((((2,), (0,))), (6, 0)),
            ((((2, 0), (0, 6))), (2, 12)),
        )
        for matrix, target in examples:
            self.assertTrue(integrally_reachable(matrix, target))
            self.assertIsNone(local_global_countermodulus(matrix, target))
            self.assertIsNone(local_global_prime_power_counterexample(matrix, target))

    def test_validation(self):
        with self.assertRaises(ValueError):
            integer_left_nullspace_rows(())
        with self.assertRaises(ValueError):
            bounded_target_certificate_modulus(((1,),), -1)
        with self.assertRaises(ValueError):
            prime_power_components(0)
        with self.assertRaises(TypeError):
            prime_power_components(True)


if __name__ == "__main__":
    unittest.main()
