import itertools
import unittest

from enterprise_math.integer_affine_fiber_diagnostic import (
    integrally_reachable,
    integer_affine_fiber_report,
    modular_affine_fiber_report,
    modularly_reachable,
    rationally_reachable,
    target_class_order_in_saturation,
)


class IntegerAffineFiberDiagnosticTests(unittest.TestCase):
    def test_free_cokernel_torsion_image_and_exact_fiber_are_distinct(self):
        free = integer_affine_fiber_report(
            ((1,), (0,)),
            (0, 1),
        )
        self.assertFalse(free.rationally_reachable)
        self.assertFalse(free.integrally_reachable)
        self.assertEqual(free.obstruction_kind, "FREE_COKERNEL")
        self.assertIsNone(free.target_class_order)
        self.assertIsNone(free.exact_fiber_free_rank)

        torsion = integer_affine_fiber_report(
            ((2,),),
            (1,),
        )
        self.assertTrue(torsion.rationally_reachable)
        self.assertFalse(torsion.integrally_reachable)
        self.assertEqual(torsion.obstruction_kind, "TORSION_IMAGE")
        self.assertEqual(torsion.target_class_order, 2)
        self.assertIsNone(torsion.exact_fiber_free_rank)

        reachable = integer_affine_fiber_report(
            ((1, 0),),
            (3,),
        )
        self.assertTrue(reachable.integrally_reachable)
        self.assertEqual(reachable.obstruction_kind, "NONE")
        self.assertEqual(reachable.target_class_order, 1)
        self.assertEqual(reachable.exact_fiber_free_rank, 1)

    def test_target_class_order_matches_small_diagonal_cokernel_examples(self):
        matrix = (
            (2, 0),
            (0, 6),
        )
        self.assertEqual(target_class_order_in_saturation(matrix, (1, 0)), 2)
        self.assertEqual(target_class_order_in_saturation(matrix, (0, 1)), 6)
        self.assertEqual(target_class_order_in_saturation(matrix, (1, 3)), 2)
        self.assertEqual(target_class_order_in_saturation(matrix, (2, 6)), 1)

    def test_mod_four_image_obstruction_vs_kernel_fiber_sharp_pair(self):
        no_solution = modular_affine_fiber_report(
            ((2,),),
            (-1,),
            4,
        )
        self.assertFalse(no_solution.solvable)
        self.assertEqual(no_solution.solution_count, 0)
        self.assertEqual(no_solution.kernel_size_if_solvable, 2)

        two_solutions = modular_affine_fiber_report(
            ((2,),),
            (-2,),
            4,
        )
        self.assertTrue(two_solutions.solvable)
        self.assertEqual(two_solutions.solution_count, 2)
        self.assertEqual(two_solutions.kernel_size_if_solvable, 2)

    def test_exact_two_variable_fiber_has_expected_free_rank(self):
        report = integer_affine_fiber_report(
            ((1, 1),),
            (5,),
        )
        self.assertTrue(report.integrally_reachable)
        self.assertEqual(report.rational_rank, 1)
        self.assertEqual(report.exact_fiber_free_rank, 1)
        self.assertEqual(report.smith_factors, (1,))

    def test_modular_solution_count_matches_bruteforce_on_small_scalar_equations(self):
        for coefficient in range(-4, 5):
            for target in range(-4, 5):
                for modulus in range(1, 8):
                    report = modular_affine_fiber_report(
                        ((coefficient,),),
                        (target,),
                        modulus,
                    )
                    brute = sum(
                        1
                        for value in range(modulus)
                        if (coefficient * value - target) % modulus == 0
                    )
                    self.assertEqual(report.solution_count, brute)
                    self.assertEqual(report.solvable, brute > 0)

    def test_modular_solution_count_matches_bruteforce_on_small_two_variable_maps(self):
        matrices = (
            ((1, 1),),
            ((2, 0),),
            ((1, 0), (0, 2)),
            ((1, 1), (1, -1)),
        )
        for matrix in matrices:
            row_count = len(matrix)
            for target in itertools.product(range(-1, 2), repeat=row_count):
                for modulus in range(1, 5):
                    report = modular_affine_fiber_report(
                        matrix,
                        target,
                        modulus,
                    )
                    dimension = len(matrix[0])
                    brute = 0
                    for state in itertools.product(range(modulus), repeat=dimension):
                        image = tuple(
                            sum(coefficient * value for coefficient, value in zip(row, state, strict=True)) % modulus
                            for row in matrix
                        )
                        if image == tuple(value % modulus for value in target):
                            brute += 1
                    self.assertEqual(report.solution_count, brute, (matrix, target, modulus))

    def test_rational_reachability_and_integral_reachability_boundaries(self):
        self.assertTrue(rationally_reachable(((2,),), (1,)))
        self.assertFalse(integrally_reachable(((2,),), (1,)))
        self.assertTrue(integrally_reachable(((2,),), (2,)))
        self.assertFalse(rationally_reachable(((1,), (0,)), (0, 1)))

    def test_modular_reachability_can_differ_from_exact_integer_reachability(self):
        matrix = ((2,),)
        target = (1,)
        self.assertFalse(integrally_reachable(matrix, target))
        self.assertFalse(modularly_reachable(matrix, target, 4))
        self.assertTrue(modularly_reachable(matrix, target, 3))

    def test_validation(self):
        with self.assertRaises(ValueError):
            integer_affine_fiber_report((), ())
        with self.assertRaises(ValueError):
            integer_affine_fiber_report(((1,),), ())
        with self.assertRaises(ValueError):
            modular_affine_fiber_report(((1,),), (0,), 0)
        with self.assertRaises(TypeError):
            modular_affine_fiber_report(((1,),), (0,), False)


if __name__ == "__main__":
    unittest.main()
