import itertools
import unittest

from enterprise_math.integer_action_language_observability import (
    action_language_observation_rows,
)
from enterprise_math.integer_action_module_closure import (
    action_module_closure_report,
    action_module_closure_step,
    integer_row_hermite_basis,
)


class IntegerActionModuleClosureTests(unittest.TestCase):
    def test_row_hermite_basis_is_generator_order_invariant(self):
        rows = (
            (2, 0, 2),
            (0, 4, 2),
            (2, 4, 4),
            (1, 2, 1),
        )
        expected = integer_row_hermite_basis(rows)
        for permutation in itertools.permutations(rows):
            self.assertEqual(
                integer_row_hermite_basis(permutation),
                expected,
            )

    def test_basis_iteration_matches_literal_word_lattice_exhaustively_on_small_binary_actions(self):
        actions = tuple(
            (
                (entries[0], entries[1]),
                (entries[2], entries[3]),
            )
            for entries in itertools.product((0, 1), repeat=4)
        )
        observation = ((1, 0),)

        for left in actions:
            for right in actions:
                family = (left, right)
                basis = integer_row_hermite_basis(observation)
                for horizon in range(4):
                    literal = action_language_observation_rows(
                        family,
                        observation,
                        horizon,
                    )
                    self.assertEqual(
                        basis,
                        integer_row_hermite_basis(literal),
                        (family, horizon),
                    )
                    basis = action_module_closure_step(basis, family)

    def test_rank_full_then_index_two_to_one_noncommutative_witness(self):
        action_a = (
            (0, 1, 0),
            (0, 0, 0),
            (0, 0, 0),
        )
        action_b = (
            (0, 0, 2),
            (0, 0, 1),
            (0, 0, 0),
        )
        report = action_module_closure_report(
            (action_a, action_b),
            ((1, 0, 0),),
        )
        by_horizon = {step.horizon: step for step in report.steps}
        self.assertEqual(by_horizon[1].rational_rank, 3)
        self.assertEqual(by_horizon[1].saturation_index, 2)
        self.assertEqual(by_horizon[2].rational_rank, 3)
        self.assertEqual(by_horizon[2].saturation_index, 1)
        self.assertEqual(report.rational_stabilization_horizon, 1)
        self.assertEqual(report.exact_stabilization_horizon, 2)
        self.assertEqual(report.theorem_attainment_bound, 2)
        self.assertTrue(report.delayed_integer_refinement_after_rational_stability)
        self.assertEqual(
            report.final_basis,
            ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
        )

    def test_index_four_has_two_strict_post_rank_refinements_and_meets_omega_bound(self):
        # Horizon 1 reaches full rational rank with basis e1,e2,2e3,2e4
        # (index 4).  Word A;C contributes e3 at horizon 2, and A;C;D
        # contributes e4 at horizon 3.  Thus 4 -> 2 -> 1 uses exactly
        # Omega(4)=2 strict arithmetic refinements after rational stabilization.
        action_a = (
            (0, 1, 0, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
        )
        action_b = (
            (0, 0, 2, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
        )
        action_c = (
            (0, 0, 0, 2),
            (0, 0, 1, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
        )
        action_d = (
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 1),
            (0, 0, 0, 0),
        )
        report = action_module_closure_report(
            (action_a, action_b, action_c, action_d),
            ((1, 0, 0, 0),),
        )
        by_horizon = {step.horizon: step for step in report.steps}
        self.assertEqual(
            tuple(by_horizon[h].rational_rank for h in (1, 2, 3)),
            (4, 4, 4),
        )
        self.assertEqual(
            tuple(by_horizon[h].saturation_index for h in (1, 2, 3)),
            (4, 2, 1),
        )
        self.assertEqual(report.rational_stabilization_horizon, 1)
        self.assertEqual(report.arithmetic_refinement_budget, 2)
        self.assertEqual(report.theorem_attainment_bound, 3)
        self.assertEqual(report.exact_stabilization_horizon, 3)

    def test_zero_observation_lattice_is_valid_and_stable_at_horizon_zero(self):
        actions = (
            ((1, 1), (0, 1)),
            ((0, 1), (1, 0)),
        )
        report = action_module_closure_report(
            actions,
            ((0, 0),),
        )
        self.assertEqual(report.initial_basis, ())
        self.assertEqual(report.final_basis, ())
        self.assertEqual(report.rational_stabilization_horizon, 0)
        self.assertEqual(report.exact_stabilization_horizon, 0)
        self.assertEqual(report.theorem_attainment_bound, 0)
        self.assertEqual(report.steps[0].hidden_free_rank, 2)
        self.assertEqual(action_module_closure_step(((0, 0),), actions), ())

    def test_one_equal_basis_step_is_a_permanent_stop_certificate(self):
        actions = (
            ((1, 1), (0, 1)),
            ((1, 0), (0, 1)),
        )
        observation = ((1, 0), (0, 1))
        report = action_module_closure_report(actions, observation)
        self.assertEqual(report.exact_stabilization_horizon, 0)
        self.assertEqual(report.final_basis, ((1, 0), (0, 1)))
        for horizon in range(5):
            literal = action_language_observation_rows(
                actions,
                observation,
                horizon,
            )
            self.assertEqual(
                integer_row_hermite_basis(literal),
                report.final_basis,
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            action_module_closure_report((), ((1,),))
        with self.assertRaises(ValueError):
            action_module_closure_report((((1, 0),),), ((1,),))
        with self.assertRaises(TypeError):
            integer_row_hermite_basis(((1, False),))


if __name__ == "__main__":
    unittest.main()
