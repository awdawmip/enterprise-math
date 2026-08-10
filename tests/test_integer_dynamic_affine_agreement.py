import itertools
import unittest

from enterprise_math.integer_dynamic_affine_agreement import (
    affine_equation_integer_solvable,
    affine_equation_modular_solvable,
    dynamic_affine_exact_agreement_report,
    dynamic_affine_modular_agreement_report,
    vector_in_integer_row_lattice,
)


def identity_affine_action():
    return ((((1,),), (0,)),)


class IntegerDynamicAffineAgreementTests(unittest.TestCase):
    def test_same_linear_kernel_but_different_offset_can_switch_zero_vs_two_mod_four_solutions(self):
        actions = identity_affine_action()

        no_solution = dynamic_affine_modular_agreement_report(
            actions,
            ((2,),),
            (1,),
            actions,
            ((0,),),
            (0,),
            4,
        )
        self.assertFalse(no_solution.solvable)
        self.assertEqual(no_solution.agreement_state_count, 0)
        self.assertEqual(no_solution.linear_smith_factors, (2,))

        two_solutions = dynamic_affine_modular_agreement_report(
            actions,
            ((2,),),
            (2,),
            actions,
            ((0,),),
            (0,),
            4,
        )
        self.assertTrue(two_solutions.solvable)
        self.assertEqual(two_solutions.agreement_state_count, 2)
        self.assertEqual(two_solutions.linear_smith_factors, (2,))

    def test_exact_integer_image_obstruction_and_solution(self):
        actions = identity_affine_action()
        no_solution = dynamic_affine_exact_agreement_report(
            actions,
            ((2,),),
            (1,),
            actions,
            ((0,),),
            (0,),
        )
        self.assertFalse(no_solution.solvable)
        self.assertIsNone(no_solution.agreement_free_rank)

        solution = dynamic_affine_exact_agreement_report(
            actions,
            ((2,),),
            (2,),
            actions,
            ((0,),),
            (0,),
        )
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.agreement_free_rank, 0)
        self.assertEqual(solution.linear_smith_factors, (2,))

    def test_pure_constant_difference_has_all_or_zero_modular_agreement_states(self):
        actions = identity_affine_action()
        for modulus in range(1, 9):
            report = dynamic_affine_modular_agreement_report(
                actions,
                ((0,),),
                (6,),
                actions,
                ((0,),),
                (0,),
                modulus,
            )
            if 6 % modulus == 0:
                self.assertTrue(report.solvable)
                self.assertEqual(report.agreement_state_count, modulus)
                self.assertTrue(report.all_states_agree)
            else:
                self.assertFalse(report.solvable)
                self.assertEqual(report.agreement_state_count, 0)

    def test_modular_affine_solver_matches_bruteforce_for_small_scalar_equations(self):
        for coefficient in range(-4, 5):
            for constant in range(-4, 5):
                for modulus in range(1, 8):
                    predicted = affine_equation_modular_solvable(
                        ((coefficient,),),
                        (constant,),
                        modulus,
                    )
                    solutions = tuple(
                        value
                        for value in range(modulus)
                        if (coefficient * value + constant) % modulus == 0
                    )
                    self.assertEqual(predicted, bool(solutions))

    def test_dynamic_affine_report_solution_count_matches_bruteforce_scalar_equations(self):
        actions = identity_affine_action()
        for coefficient in range(-3, 4):
            for constant in range(-3, 4):
                for modulus in range(1, 7):
                    report = dynamic_affine_modular_agreement_report(
                        actions,
                        ((coefficient,),),
                        (constant,),
                        actions,
                        ((0,),),
                        (0,),
                        modulus,
                    )
                    brute = sum(
                        1
                        for value in range(modulus)
                        if (coefficient * value + constant) % modulus == 0
                    )
                    self.assertEqual(report.agreement_state_count, brute)
                    self.assertEqual(report.solvable, brute > 0)

    def test_two_variable_solution_set_is_affine_coset_of_kernel_size(self):
        # x+y+1=0 mod5 has exactly five solutions, one for each x.
        actions = (
            (
                ((1, 0), (0, 1)),
                (0, 0),
            ),
        )
        report = dynamic_affine_modular_agreement_report(
            actions,
            ((1, 1),),
            (1,),
            actions,
            ((0, 0),),
            (0,),
            5,
        )
        self.assertTrue(report.solvable)
        self.assertEqual(report.agreement_state_count, 5)
        self.assertEqual(report.total_state_count, 25)

    def test_row_lattice_membership_oracle(self):
        generators = ((2, 0), (0, 3))
        self.assertTrue(vector_in_integer_row_lattice(generators, (4, 6)))
        self.assertFalse(vector_in_integer_row_lattice(generators, (1, 6)))
        self.assertTrue(vector_in_integer_row_lattice((), (0, 0)))
        self.assertFalse(vector_in_integer_row_lattice((), (0, 1)))

    def test_exactly_equivalent_affine_models_have_full_free_agreement(self):
        actions = identity_affine_action()
        report = dynamic_affine_exact_agreement_report(
            actions,
            ((1,),),
            (7,),
            actions,
            ((1,),),
            (7,),
        )
        self.assertTrue(report.solvable)
        self.assertEqual(report.agreement_free_rank, 1)
        self.assertEqual(report.augmented_difference_basis, ())

    def test_validation(self):
        with self.assertRaises(ValueError):
            affine_equation_integer_solvable(((1,),), ())
        with self.assertRaises(ValueError):
            affine_equation_modular_solvable(((1,),), (0,), 0)
        with self.assertRaises(ValueError):
            vector_in_integer_row_lattice(((1, 0),), (1,))


if __name__ == "__main__":
    unittest.main()
