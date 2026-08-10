import itertools
import unittest

from enterprise_math.integer_affine_fiber_diagnostic import (
    integrally_reachable,
    modularly_reachable,
)
from enterprise_math.integer_affine_uniform_all_target_local_global import (
    finite_uniform_all_target_certificate_exists,
    free_cokernel_finite_family_false_positive,
    least_uniform_all_target_certificate_modulus,
)


class IntegerAffineUniformAllTargetLocalGlobalTests(unittest.TestCase):
    def test_full_row_rank_is_exact_positive_boundary(self):
        matrices = (
            ((1,),),
            ((6,),),
            ((2, 0), (0, 6)),
            ((2, 1), (0, 3)),
        )
        for matrix in matrices:
            self.assertTrue(finite_uniform_all_target_certificate_exists(matrix))
            modulus = least_uniform_all_target_certificate_modulus(matrix)
            self.assertIsNotNone(modulus)
            assert modulus is not None
            row_count = len(matrix)
            for target in itertools.product(range(-5, 6), repeat=row_count):
                self.assertEqual(
                    integrally_reachable(matrix, target),
                    modularly_reachable(matrix, target, modulus),
                    (matrix, target, modulus),
                )

    def test_rank_deficient_maps_have_no_finite_uniform_all_target_certificate(self):
        matrices = (
            ((0,),),
            ((1,), (0,)),
            ((1, 0), (0, 0)),
            ((1, 2), (2, 4), (0, 0)),
        )
        for matrix in matrices:
            self.assertFalse(finite_uniform_all_target_certificate_exists(matrix))
            self.assertIsNone(least_uniform_all_target_certificate_modulus(matrix))

    def test_every_finite_modulus_family_is_defeated_by_constructed_free_target(self):
        matrices = (
            ((0,),),
            ((1,), (0,)),
            ((1, 0), (0, 0)),
            ((1, 2), (2, 4), (0, 0)),
        )
        families = (
            (2,),
            (4, 6),
            (3, 5, 8),
            (7, 9, 10, 12),
        )
        for matrix in matrices:
            for family in families:
                witness = free_cokernel_finite_family_false_positive(matrix, family)
                self.assertFalse(witness.rationally_reachable)
                self.assertFalse(witness.integrally_reachable)
                self.assertTrue(witness.modularly_reachable_all_tests)
                self.assertTrue(all(
                    value % modulus == 0
                    for value in witness.target
                    for modulus in family
                    if value
                ))

    def test_false_positive_uses_lcm_ceiling_exactly(self):
        matrix = (
            (1,),
            (0,),
        )
        witness = free_cokernel_finite_family_false_positive(matrix, (4, 6))
        self.assertEqual(witness.lcm_ceiling, 12)
        self.assertEqual(witness.left_null_witness, (0, 1))
        self.assertEqual(witness.witness_coordinate, 1)
        self.assertEqual(witness.target, (0, 12))
        self.assertFalse(integrally_reachable(matrix, witness.target))
        self.assertTrue(modularly_reachable(matrix, witness.target, 4))
        self.assertTrue(modularly_reachable(matrix, witness.target, 6))

    def test_full_row_rank_rejects_free_cokernel_no_go_constructor(self):
        with self.assertRaises(ValueError):
            free_cokernel_finite_family_false_positive(((2,),), (2, 3))

    def test_validation(self):
        with self.assertRaises(ValueError):
            free_cokernel_finite_family_false_positive(((1,), (0,)), ())
        with self.assertRaises(ValueError):
            free_cokernel_finite_family_false_positive(((1,), (0,)), (0,))
        with self.assertRaises(TypeError):
            free_cokernel_finite_family_false_positive(((1,), (0,)), (True,))


if __name__ == "__main__":
    unittest.main()
