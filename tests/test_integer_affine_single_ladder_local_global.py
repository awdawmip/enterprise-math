import unittest

from enterprise_math.integer_affine_fiber_diagnostic import integrally_reachable
from enterprise_math.integer_affine_single_ladder_local_global import (
    INFINITE,
    canonical_complete_ladder_base,
    finite_single_ladder_spectrum,
    free_cokernel_rank,
    integer_radical,
    ladder_base_is_uniformly_complete,
)


class IntegerAffineSingleLadderLocalGlobalTests(unittest.TestCase):
    def test_torsion_free_free_cokernel_uses_binary_ladder(self):
        matrix = (
            (1,),
            (0,),
        )
        self.assertEqual(free_cokernel_rank(matrix), 1)
        self.assertEqual(canonical_complete_ladder_base(matrix), 2)
        self.assertTrue(ladder_base_is_uniformly_complete(matrix, 2))
        self.assertTrue(ladder_base_is_uniformly_complete(matrix, 3))
        self.assertFalse(ladder_base_is_uniformly_complete(matrix, 1))

        # Target second coordinate 8 is invisible through 2,4,8 and fails at16.
        target = (0, 8)
        report = finite_single_ladder_spectrum(
            matrix,
            target,
            4,
            resolve_exact_height=True,
        )
        self.assertEqual(report.solvable_flags, (True, True, True, False))
        self.assertEqual(report.first_unsolvable_exponent, 4)
        self.assertEqual(report.exact_height, 3)
        self.assertFalse(report.exact_reachable)

    def test_canonical_base_equal_torsion_exponent_kills_torsion_at_first_level(self):
        matrix = (
            (6,),
            (0,),
        )
        self.assertEqual(canonical_complete_ladder_base(matrix), 6)

        torsion_target = (3, 0)
        report = finite_single_ladder_spectrum(
            matrix,
            torsion_target,
            3,
            resolve_exact_height=True,
        )
        self.assertEqual(report.solvable_flags, (False, False, False))
        self.assertEqual(report.first_unsolvable_exponent, 1)
        self.assertEqual(report.exact_height, 0)

        free_target = (0, 36)
        report = finite_single_ladder_spectrum(
            matrix,
            free_target,
            3,
            resolve_exact_height=True,
        )
        self.assertEqual(report.solvable_flags, (True, True, False))
        self.assertEqual(report.first_unsolvable_exponent, 3)
        self.assertEqual(report.exact_height, 2)

    def test_full_row_rank_needs_only_first_canonical_level(self):
        matrix = (
            (2, 0),
            (0, 6),
        )
        self.assertEqual(free_cokernel_rank(matrix), 0)
        self.assertEqual(canonical_complete_ladder_base(matrix), 6)

        unreachable = finite_single_ladder_spectrum(
            matrix,
            (1, 3),
            3,
            resolve_exact_height=True,
        )
        self.assertFalse(unreachable.solvable_flags[0])
        self.assertEqual(unreachable.exact_height, 0)

        reachable = finite_single_ladder_spectrum(
            matrix,
            (2, 12),
            3,
            resolve_exact_height=True,
        )
        self.assertEqual(reachable.solvable_flags, (True, True, True))
        self.assertEqual(reachable.exact_height, INFINITE)
        self.assertTrue(reachable.exact_reachable)

    def test_surjective_integer_map_needs_no_nontrivial_modular_test(self):
        matrix = (
            (1, 0),
            (0, 1),
        )
        self.assertEqual(canonical_complete_ladder_base(matrix), 1)
        report = finite_single_ladder_spectrum(
            matrix,
            (7, -9),
            3,
            resolve_exact_height=True,
        )
        self.assertEqual(report.moduli, (1, 1, 1))
        self.assertEqual(report.solvable_flags, (True, True, True))
        self.assertEqual(report.exact_height, INFINITE)
        self.assertTrue(integrally_reachable(matrix, (7, -9)))

    def test_base_must_contain_every_torsion_prime(self):
        matrix = ((12,),)
        self.assertEqual(integer_radical(12), 6)
        self.assertTrue(ladder_base_is_uniformly_complete(matrix, 6))
        self.assertTrue(ladder_base_is_uniformly_complete(matrix, 12))
        self.assertTrue(ladder_base_is_uniformly_complete(matrix, 30))
        self.assertFalse(ladder_base_is_uniformly_complete(matrix, 2))
        self.assertFalse(ladder_base_is_uniformly_complete(matrix, 3))
        with self.assertRaises(ValueError):
            finite_single_ladder_spectrum(matrix, (6,), 3, base=2)

    def test_validation(self):
        with self.assertRaises(ValueError):
            integer_radical(0)
        with self.assertRaises(TypeError):
            integer_radical(True)
        with self.assertRaises(ValueError):
            ladder_base_is_uniformly_complete(((1,), (0,)), 0)
        with self.assertRaises(ValueError):
            finite_single_ladder_spectrum(((1,),), (1,), 0)


if __name__ == "__main__":
    unittest.main()
