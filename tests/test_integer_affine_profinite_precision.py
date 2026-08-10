import itertools
import unittest

from enterprise_math.integer_affine_fiber_diagnostic import (
    integrally_reachable,
    modularly_reachable,
)
from enterprise_math.integer_affine_profinite_precision import (
    finite_modulus_decides_all_target_membership,
    image_is_profinite_closed,
    image_is_profinite_open,
    least_uniform_open_modulus,
    profinite_image_precision_report,
    rational_image_subspace_has_finite_certificate,
    target_separation_modulus,
)


class IntegerAffineProfinitePrecisionTests(unittest.TestCase):
    def test_full_row_rank_image_is_clopen_with_least_smith_modulus(self):
        matrix = (
            (2, 0),
            (0, 6),
        )
        report = profinite_image_precision_report(matrix)
        self.assertTrue(report.profinitely_closed)
        self.assertTrue(report.profinitely_open)
        self.assertTrue(report.clopen)
        self.assertEqual(report.free_cokernel_rank, 0)
        self.assertEqual(report.torsion_exponent, 6)
        self.assertEqual(report.least_uniform_modulus, 6)
        self.assertEqual(least_uniform_open_modulus(matrix), 6)

        for modulus in range(1, 19):
            self.assertEqual(
                finite_modulus_decides_all_target_membership(matrix, modulus),
                modulus % 6 == 0,
            )

    def test_rank_deficient_image_is_closed_but_not_open(self):
        matrix = (
            (1,),
            (0,),
        )
        report = profinite_image_precision_report(matrix)
        self.assertTrue(report.profinitely_closed)
        self.assertFalse(report.profinitely_open)
        self.assertFalse(report.clopen)
        self.assertEqual(report.free_cokernel_rank, 1)
        self.assertIsNone(report.least_uniform_modulus)
        self.assertTrue(image_is_profinite_closed(matrix))
        self.assertFalse(image_is_profinite_open(matrix))
        for modulus in (1, 2, 3, 6, 12):
            self.assertFalse(finite_modulus_decides_all_target_membership(matrix, modulus))

    def test_closedness_gives_a_finite_separator_for_every_unreachable_target(self):
        matrix = (
            (2,),
            (0,),
        )
        targets = (
            (1, 0),
            (0, 5),
            (3, 7),
            (-1, -4),
        )
        for target in targets:
            self.assertFalse(integrally_reachable(matrix, target))
            modulus = target_separation_modulus(matrix, target)
            self.assertIsNotNone(modulus)
            assert modulus is not None
            self.assertFalse(modularly_reachable(matrix, target, modulus))

    def test_reachable_target_needs_no_separation_neighborhood(self):
        matrix = (
            (2,),
            (0,),
        )
        for target in ((0, 0), (2, 0), (-6, 0)):
            self.assertTrue(integrally_reachable(matrix, target))
            self.assertIsNone(target_separation_modulus(matrix, target))

    def test_rational_image_saturation_is_open_relative_to_its_subspace(self):
        matrix = (
            (2,),
            (0,),
        )
        for target in ((0, 0), (1, 0), (2, 0), (3, 0), (6, 0)):
            result = rational_image_subspace_has_finite_certificate(matrix, target)
            self.assertEqual(result, integrally_reachable(matrix, target))
        with self.assertRaises(ValueError):
            rational_image_subspace_has_finite_certificate(matrix, (0, 1))

    def test_surjective_image_is_whole_space_and_modulus_one_already_complete(self):
        matrix = (
            (1, 0),
            (0, 1),
        )
        report = profinite_image_precision_report(matrix)
        self.assertTrue(report.clopen)
        self.assertEqual(report.least_uniform_modulus, 1)
        self.assertTrue(finite_modulus_decides_all_target_membership(matrix, 1))
        for target in itertools.product(range(-3, 4), repeat=2):
            self.assertTrue(integrally_reachable(matrix, target))

    def test_validation(self):
        with self.assertRaises(ValueError):
            profinite_image_precision_report(())
        with self.assertRaises(ValueError):
            finite_modulus_decides_all_target_membership(((1,),), 0)
        with self.assertRaises(TypeError):
            finite_modulus_decides_all_target_membership(((1,),), True)


if __name__ == "__main__":
    unittest.main()
