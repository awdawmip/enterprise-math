import itertools
import unittest

from enterprise_math.integer_affine_fiber_diagnostic import (
    integrally_reachable,
    modularly_reachable,
    rationally_reachable,
)
from enterprise_math.integer_affine_local_global_hierarchy import (
    bounded_box_certificate_holds,
    bounded_box_certificate_modulus,
    full_row_rank_certificate_modulus,
    local_global_certification_hierarchy,
    rational_image_certificate_holds,
    rational_image_certificate_modulus,
    smallest_multiple_above,
)


class IntegerAffineLocalGlobalHierarchyTests(unittest.TestCase):
    def test_full_row_rank_map_has_one_uniform_all_target_modulus(self):
        matrix = (
            (2, 0),
            (0, 6),
        )
        self.assertEqual(full_row_rank_certificate_modulus(matrix), 6)
        hierarchy = local_global_certification_hierarchy(matrix)
        self.assertTrue(hierarchy.full_row_rank)
        self.assertEqual(hierarchy.free_cokernel_rank, 0)
        self.assertEqual(hierarchy.torsion_exponent, 6)
        self.assertEqual(hierarchy.full_row_rank_certificate_modulus, 6)
        self.assertEqual(hierarchy.full_row_rank_prime_power_family, (2, 3))

        for target in itertools.product(range(-8, 9), repeat=2):
            self.assertEqual(
                integrally_reachable(matrix, target),
                modularly_reachable(matrix, target, 6),
                target,
            )

    def test_nontrivial_full_row_rank_example_uses_largest_smith_factor(self):
        matrix = (
            (2, 1),
            (0, 3),
        )
        modulus = full_row_rank_certificate_modulus(matrix)
        self.assertGreaterEqual(modulus, 1)
        for target in itertools.product(range(-5, 6), repeat=2):
            self.assertEqual(
                integrally_reachable(matrix, target),
                modularly_reachable(matrix, target, modulus),
                (target, modulus),
            )

    def test_rational_image_promise_reduces_rank_deficient_target_to_torsion_modulus(self):
        matrix = (
            (2,),
            (0,),
        )
        self.assertEqual(rational_image_certificate_modulus(matrix), 2)

        for target in ((0, 0), (1, 0), (2, 0), (3, 0), (-2, 0)):
            self.assertTrue(rationally_reachable(matrix, target))
            self.assertEqual(
                rational_image_certificate_holds(matrix, target),
                integrally_reachable(matrix, target),
            )

        with self.assertRaises(ValueError):
            rational_image_certificate_holds(matrix, (0, 1))

    def test_unimodular_full_row_rank_needs_no_nontrivial_modular_precision(self):
        matrix = (
            (1, 0),
            (0, 1),
        )
        hierarchy = local_global_certification_hierarchy(matrix)
        self.assertEqual(hierarchy.torsion_exponent, 1)
        self.assertEqual(hierarchy.full_row_rank_certificate_modulus, 1)
        self.assertEqual(hierarchy.full_row_rank_prime_power_family, ())
        for target in itertools.product(range(-3, 4), repeat=2):
            self.assertTrue(integrally_reachable(matrix, target))

    def test_smallest_multiple_above_is_exact_for_theorem_conditions(self):
        self.assertEqual(smallest_multiple_above(6, 0), 6)
        self.assertEqual(smallest_multiple_above(6, 5), 6)
        self.assertEqual(smallest_multiple_above(6, 6), 12)
        self.assertEqual(smallest_multiple_above(6, 13), 18)
        self.assertEqual(smallest_multiple_above(1, 13), 14)

    def test_bounded_box_certificate_is_uniform_for_rank_deficient_map(self):
        matrix = (
            (2,),
            (0,),
        )
        bound = 3
        modulus = bounded_box_certificate_modulus(matrix, bound)
        self.assertEqual(modulus, 4)
        for target in itertools.product(range(-bound, bound + 1), repeat=2):
            result = bounded_box_certificate_holds(matrix, target, bound)
            self.assertEqual(result, integrally_reachable(matrix, target))
            self.assertEqual(
                integrally_reachable(matrix, target),
                modularly_reachable(matrix, target, modulus),
            )

    def test_zero_map_bounded_box_certificate_requires_precision_above_target_height(self):
        matrix = (
            (0, 0),
            (0, 0),
        )
        bound = 2
        modulus = bounded_box_certificate_modulus(matrix, bound)
        # Deterministic RREF left-null basis is the standard basis, so B=H.
        self.assertEqual(modulus, 3)
        for target in itertools.product(range(-bound, bound + 1), repeat=2):
            self.assertEqual(
                integrally_reachable(matrix, target),
                modularly_reachable(matrix, target, modulus),
            )

    def test_hierarchy_marks_free_cokernel_as_requiring_bound_or_promise(self):
        matrix = (
            (1, 0),
            (0, 0),
        )
        hierarchy = local_global_certification_hierarchy(matrix)
        self.assertFalse(hierarchy.full_row_rank)
        self.assertEqual(hierarchy.free_cokernel_rank, 1)
        self.assertIsNone(hierarchy.full_row_rank_certificate_modulus)
        self.assertIsNone(hierarchy.full_row_rank_prime_power_family)

    def test_validation(self):
        with self.assertRaises(ValueError):
            full_row_rank_certificate_modulus(((1, 0), (0, 0)))
        with self.assertRaises(ValueError):
            smallest_multiple_above(0, 1)
        with self.assertRaises(ValueError):
            smallest_multiple_above(2, -1)
        with self.assertRaises(ValueError):
            bounded_box_certificate_modulus(((1,),), -1)
        with self.assertRaises(ValueError):
            bounded_box_certificate_holds(((1,),), (2,), 1)


if __name__ == "__main__":
    unittest.main()
