import itertools
import unittest
from math import lcm

from enterprise_math.integer_affine_fiber_diagnostic import modularly_reachable
from enterprise_math.integer_affine_modular_solvability_lattice import (
    INFINITE,
    affine_solvability_is_downward,
    affine_solvability_is_lcm_closed,
    bounded_affine_solvability_lattice_report,
    scalar_modulus_solvable_from_prime_thresholds,
    scalar_prime_power_solvability_threshold,
)


class IntegerAffineModularSolvabilityLatticeTests(unittest.TestCase):
    def test_2x_equals_1_is_solvable_exactly_for_odd_moduli(self):
        matrix = ((2,),)
        target = (1,)
        report = bounded_affine_solvability_lattice_report(
            matrix,
            target,
            40,
        )
        self.assertEqual(
            report.solvable_moduli,
            tuple(modulus for modulus in range(1, 41) if modulus % 2 == 1),
        )
        self.assertTrue(report.downward_closed)
        self.assertTrue(report.lcm_closed_within_bound)
        self.assertEqual(
            scalar_prime_power_solvability_threshold(2, 1, 2),
            0,
        )
        for prime in (3, 5, 7):
            self.assertEqual(
                scalar_prime_power_solvability_threshold(2, 1, prime),
                INFINITE,
            )

    def test_zero_linear_map_has_finite_prime_thresholds_from_target_content(self):
        # 0*x=12 mod M is solvable iff M divides 12.
        report = bounded_affine_solvability_lattice_report(
            ((0,),),
            (12,),
            24,
        )
        self.assertEqual(report.solvable_moduli, (1, 2, 3, 4, 6, 12))
        self.assertEqual(
            scalar_prime_power_solvability_threshold(0, 12, 2),
            2,
        )
        self.assertEqual(
            scalar_prime_power_solvability_threshold(0, 12, 3),
            1,
        )
        self.assertEqual(
            scalar_prime_power_solvability_threshold(0, 12, 5),
            0,
        )

    def test_scalar_prime_threshold_compiler_matches_direct_modular_reachability(self):
        for coefficient in range(-6, 7):
            for target in range(-6, 7):
                for modulus in range(1, 25):
                    expected = modularly_reachable(
                        ((coefficient,),),
                        (target,),
                        modulus,
                    )
                    actual = scalar_modulus_solvable_from_prime_thresholds(
                        coefficient,
                        target,
                        modulus,
                    )
                    self.assertEqual(
                        actual,
                        expected,
                        (coefficient, target, modulus),
                    )

    def test_downward_and_lcm_closure_on_small_matrix_targets(self):
        matrices = (
            ((2, 0), (0, 3)),
            ((1, 1),),
            ((1, 0), (0, 0)),
        )
        targets = (
            (1, 1),
            (2,),
            (0, 2),
        )
        for matrix, target in zip(matrices, targets, strict=True):
            solvable = tuple(
                modulus
                for modulus in range(1, 13)
                if modularly_reachable(matrix, target, modulus)
            )
            for finer in solvable:
                for coarser in range(1, finer + 1):
                    if finer % coarser == 0:
                        self.assertTrue(
                            affine_solvability_is_downward(
                                matrix,
                                target,
                                finer,
                                coarser,
                            )
                        )
            for left in solvable:
                for right in solvable:
                    self.assertTrue(
                        affine_solvability_is_lcm_closed(
                            matrix,
                            target,
                            left,
                            right,
                        )
                    )
                    joined = lcm(left, right)
                    self.assertTrue(
                        modularly_reachable(matrix, target, joined)
                    )

    def test_exact_reachable_target_is_solvable_at_every_modulus(self):
        matrix = ((1, 1),)
        target = (7,)
        report = bounded_affine_solvability_lattice_report(
            matrix,
            target,
            30,
        )
        self.assertEqual(report.solvable_moduli, tuple(range(1, 31)))

    def test_numeric_modulus_size_is_not_the_solvability_order(self):
        # 2x=1 is solvable mod 9 but not mod 2, even though 9>2; the natural
        # order remains divisibility, not numerical magnitude.
        self.assertTrue(modularly_reachable(((2,),), (1,), 9))
        self.assertFalse(modularly_reachable(((2,),), (1,), 2))

    def test_validation(self):
        with self.assertRaises(ValueError):
            bounded_affine_solvability_lattice_report(((1,),), (0,), 0)
        with self.assertRaises(ValueError):
            affine_solvability_is_downward(((1,),), (0,), 3, 2)
        with self.assertRaises(ValueError):
            scalar_prime_power_solvability_threshold(1, 1, 4)
        with self.assertRaises(TypeError):
            scalar_modulus_solvable_from_prime_thresholds(1, 1, False)


if __name__ == "__main__":
    unittest.main()
