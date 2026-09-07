"""Exact, scope-sensitive tests for finite-carrier budgeted noise fitting."""
from fractions import Fraction as Q
import unittest
from unittest.mock import patch

from exact_feasibility import FeasibilityCertificate, verify_certificate
import noisy_recovery as noisy
from observer_certificate import Branch, all_three_axis_tables


ZERO = (0,) * 6
UNIT = (1, 0, 0, 0, 0, 0)


def zero_tables():
    return {axes: {} for axes in noisy.AXES}


def stack_distance(first, second):
    return sum((abs(first[axes].get(x, 0) - second[axes].get(x, 0))
                for axes in noisy.AXES for x in first[axes].keys() | second[axes].keys()), Q(0))


class BudgetedNoiseTests(unittest.TestCase):
    def assert_verified(self, tables, answer):
        self.assertTrue(verify_certificate(answer["compiled_matrix"], answer["compiled_rhs"], answer["certificate"]))
        branches = tuple(Branch(str(i), point, mass) for i, (point, mass) in enumerate(answer["distribution"]))
        rebuilt = all_three_axis_tables(branches)
        self.assertEqual(stack_distance(tables, rebuilt), answer["actual_stacked_l1_residual"])
        self.assertLessEqual(answer["actual_stacked_l1_residual"], answer["residual_budget"])
        self.assertFalse(answer["optimality_claimed"])
        self.assertFalse(answer["uniqueness_claimed"])

    def test_two_point_truth_with_negative_noise_and_inconsistent_totals(self):
        truth = (Branch("a", ZERO, Q(2)), Branch("b", UNIT, Q(1)))
        original = all_three_axis_tables(truth)
        tables = {axes: dict(table) for axes, table in original.items()}
        table = tables[(0, 1, 2)]
        table[(0, 0, 0)] += Q(1, 10)
        table[(1, 0, 0)] -= Q(1, 10)
        table[(9, 9, 9)] = -Q(1, 7)
        epsilon = Q(12, 35)
        self.assertEqual(stack_distance(tables, original), epsilon)
        self.assertNotEqual(sum(table.values()), sum(tables[(3, 4, 5)].values()))
        answer = noisy.fit_budgeted_noise(tables, [ZERO, UNIT], residual_budget=epsilon, truth_noise_budget=epsilon)
        self.assert_verified(tables, answer)
        truth_mass = {ZERO: Q(2), UNIT: Q(1)}
        fit_mass = dict(answer["distribution"])
        error = sum(abs(truth_mass.get(x, 0) - fit_mass.get(x, 0)) for x in truth_mass.keys() | fit_mass.keys())
        self.assertLessEqual(error, answer["conditional_l1_bound"])
        self.assertIn(((0, 1, 2), (9, 9, 9)), answer["observation_rows"])

    def test_noise_outside_carrier_is_not_dropped_and_small_budget_has_dual(self):
        tables = zero_tables()
        tables[(0, 1, 2)][(9, 9, 9)] = Q(1)
        answer = noisy.fit_budgeted_noise(tables, [], residual_budget=1)
        self.assertEqual(answer["distribution"], ())
        self.assertEqual(answer["actual_stacked_l1_residual"], 1)
        self.assert_verified(tables, answer)
        with self.assertRaises(noisy.InfeasibleNoiseBudgetError) as caught:
            noisy.fit_budgeted_noise(tables, [], residual_budget=Q(1, 2))
        error = caught.exception
        self.assertEqual(error.scope, "DECLARED_FINITE_CARRIER_AND_RESIDUAL_BUDGET_ONLY")
        self.assertEqual(error.candidates, ())
        self.assertEqual(error.residual_budget, Q(1, 2))
        self.assertEqual(error.certificate.status, "INFEASIBLE")
        self.assertTrue(verify_certificate(error.rows, error.rhs, error.certificate))

    def test_absent_data_addresses_still_compile_candidate_projection_rows(self):
        tables = zero_tables()
        answer = noisy.fit_budgeted_noise(tables, [ZERO], residual_budget=0)
        self.assertEqual(len(answer["observation_rows"]), 20)
        self.assertEqual(answer["distribution"], ())
        self.assert_verified(tables, answer)
        # Explicit zero addresses are retained in the declared row population.
        tables[(0, 1, 2)][(8, 8, 8)] = 0
        answer = noisy.fit_budgeted_noise(tables, [ZERO], residual_budget=0)
        self.assertEqual(len(answer["observation_rows"]), 21)
        self.assertIn(((0, 1, 2), (8, 8, 8)), answer["observation_rows"])

    def test_empty_zero_and_zero_noise_exact_fit(self):
        tables = zero_tables()
        answer = noisy.fit_budgeted_noise(tables, [], residual_budget=0, truth_noise_budget=0)
        self.assertEqual(answer["conditional_l1_bound"], 0)
        self.assertEqual(answer["distribution"], ())
        self.assert_verified(tables, answer)
        tables = all_three_axis_tables((Branch("a", ZERO, Q(3, 7)),))
        answer = noisy.fit_budgeted_noise(tables, [ZERO], residual_budget=0)
        self.assertEqual(answer["distribution"], ((ZERO, Q(3, 7)),))
        self.assertIsNone(answer["conditional_l1_bound"])
        self.assertIsNone(answer["conditional_l1_bound_assumptions"])
        self.assert_verified(tables, answer)

    def test_actual_residual_not_auxiliary_slack_or_declared_budget_drives_bound(self):
        tables = all_three_axis_tables((Branch("a", ZERO),))

        def valid_but_cancelling_auxiliaries(rows, rhs):
            observed = len(rows) - 1
            primal = [Q(0)] * len(rows[0])
            primal[0] = Q(1)
            primal[1] = Q(1)
            primal[1 + observed] = Q(1)
            return FeasibilityCertificate("FEASIBLE", primal=tuple(primal))

        with patch.object(noisy, "solve_nonnegative", side_effect=valid_but_cancelling_auxiliaries):
            answer = noisy.fit_budgeted_noise(tables, [ZERO], residual_budget=2, truth_noise_budget=Q(1, 3))
        self.assert_verified(tables, answer)
        self.assertEqual(answer["actual_stacked_l1_residual"], 0)
        self.assertEqual(answer["conditional_l1_bound"], Q(37, 20))

    def test_conditional_truth_premises_are_explicit_not_verified_or_carrier_restricted(self):
        # True one-point mu is outside D. Noise budget 20 is indeed sufficient,
        # and the successful zero fit still has a valid conditional bound.
        tables = zero_tables()
        answer = noisy.fit_budgeted_noise(tables, [], residual_budget=0, truth_noise_budget=20)
        truth_tables = all_three_axis_tables((Branch("outside", UNIT),))
        self.assertEqual(stack_distance(tables, truth_tables), 20)
        self.assertEqual(answer["conditional_l1_bound"], 111)
        self.assertFalse(answer["truth_premises_verified"])
        self.assertFalse(answer["truth_membership_in_carrier_required_for_bound"])
        premises = answer["conditional_l1_bound_assumptions"]
        self.assertTrue(any("SEVEN_DISTINCT_SPATIAL" in premise for premise in premises))
        self.assertTrue(any("SAME_ANCHOR" in premise for premise in premises))
        self.assertTrue(any("STACKED_L1_RESIDUAL" in premise for premise in premises))

    def test_forged_primal_or_dual_is_rejected_without_mathematical_status(self):
        tables = all_three_axis_tables((Branch("a", ZERO),))
        for status in ("FEASIBLE", "INFEASIBLE"):
            def forged(rows, rhs):
                if status == "FEASIBLE":
                    return FeasibilityCertificate(status, primal=(Q(0),) * len(rows[0]))
                return FeasibilityCertificate(status, dual=(Q(0),) * len(rows))
            with self.subTest(status=status), patch.object(noisy, "solve_nonnegative", side_effect=forged):
                with self.assertRaisesRegex(ArithmeticError, "certificate verification"):
                    noisy.fit_budgeted_noise(tables, [ZERO], residual_budget=0)

    def test_size_limits_stop_before_solver_and_execution_error_is_not_infeasible(self):
        tables = zero_tables()
        for kwargs in ({"max_candidates": 0}, {"max_observations": 19}, {"max_tableau_entries": 0}):
            with self.subTest(kwargs=kwargs), patch.object(noisy, "solve_nonnegative") as solver:
                with self.assertRaisesRegex(noisy.NoiseFitResourceLimitError, "no mathematical conclusion"):
                    noisy.fit_budgeted_noise(tables, [ZERO], residual_budget=0, **kwargs)
                solver.assert_not_called()
        failure = MemoryError("injected resource exhaustion")
        with patch.object(noisy, "solve_nonnegative", side_effect=failure):
            with self.assertRaises(MemoryError) as caught:
                noisy.fit_budgeted_noise(tables, [ZERO], residual_budget=0)
            self.assertIs(caught.exception, failure)

    def test_exact_input_contract_and_candidates_are_frozen(self):
        tables = zero_tables()
        for bad in (-1, True, 0.5):
            with self.subTest(budget=bad), self.assertRaises((ValueError, TypeError)):
                noisy.fit_budgeted_noise(tables, [], residual_budget=bad)
        for cell in ((False,) + (0,) * 5, (0,) * 5, (0.0,) + (0,) * 5):
            with self.subTest(cell=cell), self.assertRaises(ValueError):
                noisy.fit_budgeted_noise(tables, [cell], residual_budget=0)
        with self.assertRaisesRegex(ValueError, "distinct"):
            noisy.fit_budgeted_noise(tables, [ZERO, ZERO], residual_budget=0)
        for bad in (True, 0.25):
            invalid = zero_tables()
            invalid[(0, 1, 2)][(0, 0, 0)] = bad
            with self.subTest(value=bad), self.assertRaises(TypeError):
                noisy.fit_budgeted_noise(invalid, [], residual_budget=1)
        invalid = zero_tables()
        invalid[(False, 1, 2)] = invalid.pop((0, 1, 2))
        with self.assertRaisesRegex(ValueError, "axis"):
            noisy.fit_budgeted_noise(invalid, [], residual_budget=0)
        mutable = list(ZERO)
        answer = noisy.fit_budgeted_noise(tables, [mutable], residual_budget=0)
        mutable[0] = 0.5
        self.assertEqual(answer["candidate_cells"], (ZERO,))


if __name__ == "__main__":
    unittest.main(verbosity=2)
