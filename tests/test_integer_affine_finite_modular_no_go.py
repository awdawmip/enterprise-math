import unittest
from math import lcm

from enterprise_math.integer_affine_finite_modular_no_go import (
    finite_modular_image_no_go_report,
    finite_modular_reachable_unreachable_pair,
)
from enterprise_math.integer_affine_fiber_diagnostic import (
    integrally_reachable,
    modular_affine_fiber_report,
)


class IntegerAffineFiniteModularNoGoTests(unittest.TestCase):
    def test_any_finite_modulus_family_has_reachable_and_unreachable_exact_targets_with_identical_modular_fibers(self):
        families = (
            (2,),
            (2, 4, 8),
            (3, 5, 7),
            (4, 6),
            (6, 10, 15),
            (8, 9, 25),
        )
        for moduli in families:
            report = finite_modular_image_no_go_report(moduli)
            depth = 1
            for modulus in moduli:
                depth = lcm(depth, modulus)
            self.assertEqual(report.lcm_depth, depth)
            self.assertEqual(report.coefficient, depth + 1)
            self.assertTrue(report.reachable_exact)
            self.assertFalse(report.unreachable_exact)
            self.assertTrue(report.modular_solution_sets_identical)

            matrix = ((report.coefficient,),)
            for modulus in moduli:
                reachable = modular_affine_fiber_report(
                    matrix,
                    (report.reachable_target,),
                    modulus,
                )
                unreachable = modular_affine_fiber_report(
                    matrix,
                    (report.unreachable_target,),
                    modulus,
                )
                self.assertEqual(reachable.solvable, unreachable.solvable)
                self.assertEqual(reachable.solution_count, unreachable.solution_count)

    def test_construction_uses_same_map_but_exact_target_status_differs(self):
        coefficient, good, bad, depth = finite_modular_reachable_unreachable_pair(
            (4, 6),
        )
        self.assertEqual(depth, 12)
        self.assertEqual(coefficient, 13)
        self.assertEqual(good, 13)
        self.assertEqual(bad, 25)
        matrix = ((13,),)
        self.assertTrue(integrally_reachable(matrix, (good,)))
        self.assertFalse(integrally_reachable(matrix, (bad,)))

    def test_one_new_modulus_not_dividing_old_lcm_breaks_equation_identity(self):
        coefficient, good, bad, depth = finite_modular_reachable_unreachable_pair(
            (4, 6),
        )
        self.assertEqual(depth, 12)
        # Mod 5 does not divide 12; the two target constants are no longer equal.
        self.assertNotEqual(good % 5, bad % 5)
        matrix = ((coefficient,),)
        good_fiber = modular_affine_fiber_report(matrix, (good,), 5)
        bad_fiber = modular_affine_fiber_report(matrix, (bad,), 5)
        # In this specific scalar construction coefficient13 is invertible mod5,
        # so both remain solvable but their actual solution residues differ.
        self.assertTrue(good_fiber.solvable)
        self.assertTrue(bad_fiber.solvable)
        good_solution = next(
            state
            for state in range(5)
            if (coefficient * state - good) % 5 == 0
        )
        bad_solution = next(
            state
            for state in range(5)
            if (coefficient * state - bad) % 5 == 0
        )
        self.assertNotEqual(good_solution, bad_solution)

    def test_single_modulus_one_is_vacuous_and_still_cannot_certify_exact_reachability(self):
        report = finite_modular_image_no_go_report((1,))
        self.assertEqual(report.lcm_depth, 1)
        self.assertEqual(report.coefficient, 2)
        self.assertTrue(report.modular_solution_sets_identical)
        self.assertTrue(report.reachable_exact)
        self.assertFalse(report.unreachable_exact)

    def test_validation(self):
        with self.assertRaises(ValueError):
            finite_modular_reachable_unreachable_pair(())
        with self.assertRaises(ValueError):
            finite_modular_image_no_go_report((0,))
        with self.assertRaises(TypeError):
            finite_modular_image_no_go_report((False,))


if __name__ == "__main__":
    unittest.main()
