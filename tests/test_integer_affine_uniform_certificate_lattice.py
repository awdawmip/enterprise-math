import itertools
import unittest

from enterprise_math.integer_affine_fiber_diagnostic import (
    integrally_reachable,
    modularly_reachable,
    rationally_reachable,
)
from enterprise_math.integer_affine_uniform_certificate_lattice import (
    full_row_rank_uniform_certificate_modulus,
    modulus_is_uniform_rational_image_certificate,
    uniform_certificate_lattice_report,
    uniform_rational_image_certificate_modulus,
)


class IntegerAffineUniformCertificateLatticeTests(unittest.TestCase):
    def test_diagonal_map_certificate_upset_is_multiples_of_six(self):
        matrix = (
            (2, 0),
            (0, 6),
        )
        self.assertEqual(uniform_rational_image_certificate_modulus(matrix), 6)
        self.assertEqual(full_row_rank_uniform_certificate_modulus(matrix), 6)
        for modulus in range(1, 25):
            self.assertEqual(
                modulus_is_uniform_rational_image_certificate(matrix, modulus),
                modulus % 6 == 0,
            )

    def test_every_multiple_of_exponent_decides_all_targets_for_full_row_rank(self):
        matrix = (
            (2, 0),
            (0, 6),
        )
        for modulus in (6, 12, 18):
            for target in itertools.product(range(-8, 9), repeat=2):
                self.assertEqual(
                    integrally_reachable(matrix, target),
                    modularly_reachable(matrix, target, modulus),
                    (modulus, target),
                )

    def test_smaller_incomplete_modulus_has_explicit_false_positive(self):
        matrix = (
            (2, 0),
            (0, 6),
        )
        # M=3 is not a multiple of exponent 6.  Target (0,3) is rationally
        # reachable, is not integrally reachable, but becomes zero in the second
        # congruence modulo 3.
        target = (0, 3)
        self.assertTrue(rationally_reachable(matrix, target))
        self.assertFalse(integrally_reachable(matrix, target))
        self.assertTrue(modularly_reachable(matrix, target, 3))
        self.assertFalse(modulus_is_uniform_rational_image_certificate(matrix, 3))

    def test_rank_deficient_map_has_same_torsion_upset_under_rational_image_promise(self):
        matrix = (
            (2,),
            (0,),
        )
        report = uniform_certificate_lattice_report(matrix)
        self.assertFalse(report.full_row_rank)
        self.assertEqual(report.free_cokernel_rank, 1)
        self.assertEqual(report.torsion_exponent, 2)
        self.assertTrue(report.modulus_is_complete(2))
        self.assertTrue(report.modulus_is_complete(6))
        self.assertFalse(report.modulus_is_complete(3))

        rational_targets = ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0))
        for target in rational_targets:
            self.assertTrue(rationally_reachable(matrix, target))
            self.assertEqual(
                integrally_reachable(matrix, target),
                modularly_reachable(matrix, target, 2),
            )

    def test_saturated_image_has_exponent_one_and_no_nontrivial_modular_test_needed(self):
        matrix = (
            (1,),
            (0,),
        )
        report = uniform_certificate_lattice_report(matrix)
        self.assertEqual(report.torsion_exponent, 1)
        self.assertTrue(report.modulus_is_complete(1))
        self.assertTrue(report.modulus_is_complete(7))
        for target in ((-3, 0), (0, 0), (4, 0)):
            self.assertTrue(rationally_reachable(matrix, target))
            self.assertTrue(integrally_reachable(matrix, target))

    def test_validation(self):
        with self.assertRaises(ValueError):
            full_row_rank_uniform_certificate_modulus(((1, 0), (0, 0)))
        report = uniform_certificate_lattice_report(((2,),))
        with self.assertRaises(ValueError):
            report.modulus_is_complete(0)
        with self.assertRaises(TypeError):
            report.modulus_is_complete(True)
        with self.assertRaises(ValueError):
            modulus_is_uniform_rational_image_certificate(((2,),), 0)


if __name__ == "__main__":
    unittest.main()
