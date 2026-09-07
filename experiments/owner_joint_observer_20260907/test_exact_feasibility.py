"""Independent witness tests for the exact Phase-I feasibility implementation."""
from __future__ import annotations

from dataclasses import replace
from fractions import Fraction
from itertools import combinations, product
import random
import unittest
from unittest.mock import patch

from sympy import Matrix, Rational

import exact_feasibility
from exact_feasibility import FeasibilityCertificate, solve_nonnegative, verify_certificate


def vertex_enumeration_is_feasible(rows, rhs, width):
    """Tiny independent oracle: enumerate independent nonzero-support columns.

    A nonempty standard-form polyhedron has a solution on independent columns
    (remove a support dependence in a nonnegative-preserving direction). Its
    size is at most the row count. SymPy is used only for exact linear algebra,
    never simplex or an inequality solver; this oracle is deliberately tiny.
    """
    if all(value == 0 for value in rhs):
        return True
    for count in range(1, min(len(rows), width) + 1):
        for support in combinations(range(width), count):
            submatrix = Matrix([[row[j] for j in support] for row in rows])
            if submatrix.rank() != count:
                continue
            try:
                point, parameters = submatrix.gauss_jordan_solve(Matrix(rhs))
            except ValueError:
                continue
            if parameters.rows == 0 and all(value >= 0 for value in point):
                return True
    return False


class ExactFeasibilityTests(unittest.TestCase):
    def assert_certificate(self, rows, rhs, *, feasible, n_variables=None):
        answer = solve_nonnegative(rows, rhs, n_variables=n_variables)
        self.assertEqual(answer.status, "FEASIBLE" if feasible else "INFEASIBLE")
        self.assertTrue(verify_certificate(rows, rhs, answer, n_variables=n_variables))
        # Independently express the witness conditions, without tableau data.
        width = len(rows[0]) if rows else (n_variables or 0)
        if feasible:
            self.assertEqual(len(answer.primal), width)
            self.assertTrue(all(value >= 0 for value in answer.primal))
            self.assertEqual([sum(a * x for a, x in zip(row, answer.primal)) for row in rows], rhs)
        else:
            self.assertEqual(len(answer.dual), len(rows))
            self.assertLess(sum(b * y for b, y in zip(rhs, answer.dual)), 0)
            self.assertTrue(all(sum(row[j] * y for row, y in zip(rows, answer.dual)) >= 0
                                for j in range(width)))
        return answer

    def test_three_equations_rational_solution(self):
        rows = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
        answer = self.assert_certificate(rows, [1, 1, 1], feasible=True)
        self.assertEqual(answer.primal, (Fraction(1, 2),) * 3)

    def test_empty_constraints_and_zero_variables(self):
        for width in (0, 4):
            self.assert_certificate([], [], feasible=True, n_variables=width)
        self.assert_certificate([[], []], [0, 0], feasible=True)
        self.assert_certificate([[], [], []], [0, -3, 2], feasible=False)

    def test_zero_rows_and_inconsistent_redundant_rows(self):
        self.assert_certificate([[0, 0], [0, 0]], [0, 0], feasible=True)
        self.assert_certificate([[0, 0], [0, 0]], [0, 1], feasible=False)
        self.assert_certificate([[1, 2], [2, 4], [-1, -2], [0, 0]], [3, 6, -3, 0], feasible=True)
        self.assert_certificate([[1, 2], [2, 4], [-1, -2], [0, 0]], [3, 7, -3, 0], feasible=False)

    def test_nonnegative_obstruction_with_consistent_equations(self):
        self.assert_certificate([[1, 1]], [-1], feasible=False)
        self.assert_certificate([[-1, 1], [1, 0]], [-2, 1], feasible=False)
        self.assert_certificate([[-1, 1], [1, 0]], [-2, 3], feasible=True)

    def test_degenerate_zero_basic_masses(self):
        # Several entering columns must first pivot at zero step size. Row
        # permutation and duplicate equalities must preserve the decision.
        rows = [[1, 0, 0], [1, 1, 0], [1, 1, 1], [2, 2, 0]]
        rhs = [0, 0, 1, 0]
        for order in ((0, 1, 2, 3), (3, 2, 1, 0), (2, 0, 3, 1)):
            answer = self.assert_certificate([rows[i] for i in order], [rhs[i] for i in order], feasible=True)
            self.assertEqual(answer.primal, (Fraction(0), Fraction(0), Fraction(1)))

    def test_exact_fraction_and_large_integer_inputs(self):
        huge = 10 ** 70 + 3
        rows = [[Fraction(1, huge), -1], [0, Fraction(huge, 7)]]
        expected = [Fraction(huge, 3), Fraction(2, huge)]
        rhs = [sum(a * x for a, x in zip(row, expected)) for row in rows]
        answer = self.assert_certificate(rows, rhs, feasible=True)
        self.assertEqual(answer.primal, tuple(expected))

    def test_exhaustive_signed_two_by_two_against_vertex_oracle(self):
        for entries in product((-1, 0, 1), repeat=4):
            rows = [list(entries[:2]), list(entries[2:])]
            for target in product((-1, 0, 1), repeat=2):
                rhs = list(target)
                with self.subTest(rows=rows, rhs=rhs):
                    feasible = vertex_enumeration_is_feasible(rows, rhs, 2)
                    self.assert_certificate(rows, rhs, feasible=feasible)

    def test_random_redundant_rational_systems_against_vertex_oracle(self):
        rng = random.Random(202609071103)
        for trial in range(48):
            rows = [[Rational(rng.randrange(-2, 3), rng.randrange(1, 4)) for _ in range(4)]
                    for _ in range(3)]
            rhs = [Rational(rng.randrange(-3, 4), rng.randrange(1, 4)) for _ in rows]
            # A redundant row challenges degeneracy without changing feasibility.
            if trial % 2:
                rows.append([2 * value for value in rows[0]])
                rhs.append(2 * rhs[0])
            expected = vertex_enumeration_is_feasible(rows, rhs, 4)
            self.assert_certificate([[Fraction(value) for value in row] for row in rows],
                                    [Fraction(value) for value in rhs], feasible=expected)

    def test_21_support_brc_stress_requires_verified_feasible_answer(self):
        from observer_certificate import all_three_axis_tables
        from recovery import AXES, candidate_join
        from test_recovery import FEASIBLE_SOLVER_STRESS, population

        tables = all_three_axis_tables(population(FEASIBLE_SOLVER_STRESS))
        candidates = candidate_join(tables)
        rows, rhs = [], []
        for axes in AXES:
            for address, mass in sorted(tables[axes].items()):
                rows.append([int(tuple(z[a] for a in axes) == address) for z in candidates])
                rhs.append(mass)
        answer = self.assert_certificate(rows, rhs, feasible=True)
        positive = [(z, mass) for z, mass in zip(candidates, answer.primal) if mass]
        rebuilt = population([z for z, _ in positive], [mass for _, mass in positive])
        self.assertEqual(all_three_axis_tables(rebuilt), tables)
        self.assertGreater(answer.pivots, 0)

    def test_verifier_rejects_forged_and_malformed_certificates(self):
        rows, rhs = [[1, 1, 0], [1, 0, 1], [0, 1, 1]], [1, 1, 1]
        answer = solve_nonnegative(rows, rhs)
        for forged in (
            replace(answer, primal=(Fraction(0),) * 3),
            replace(answer, primal=(Fraction(1, 2),) * 2),
            replace(answer, primal=(0.5,) * 3),
            replace(answer, primal=(True,) * 3),
            replace(answer, dual=(Fraction(1),) * 3),
            FeasibilityCertificate("UNKNOWN", primal=answer.primal),
            FeasibilityCertificate("INFEASIBLE", dual=(Fraction(0),) * 3),
            {}, None,
        ):
            self.assertFalse(verify_certificate(rows, rhs, forged))
        obstruction = solve_nonnegative([[1]], [-1])
        self.assertFalse(verify_certificate([[1]], [-1], replace(obstruction, dual=(Fraction(-1),))))
        self.assertFalse(verify_certificate([[1]], [-1], replace(obstruction, dual=())))
        self.assertTrue(verify_certificate(rows, rhs, replace(answer, pivots=-999)))
        self.assertFalse(verify_certificate(rows, [1, 1, 2], answer))

    def test_verifier_does_not_call_solver(self):
        feasible = solve_nonnegative([[2]], [1])
        infeasible = solve_nonnegative([[2]], [-1])
        with patch.object(exact_feasibility, "solve_nonnegative", side_effect=AssertionError("not independent")):
            self.assertTrue(verify_certificate([[2]], [1], feasible))
            self.assertTrue(verify_certificate([[2]], [-1], infeasible))

    def test_invalid_input_is_an_error_not_an_infeasibility_result(self):
        bad_inputs = (
            ([[1, 2], [3]], [1, 2], None), ([[1]], [], None),
            ([[0.5]], [1], None), ([[True]], [1], None),
            ([[1]], [False], None), ([[1]], [1], 2),
            ([], [], -1), ([], [], True), ([[1]], [1], 1.0),
        )
        for rows, rhs, width in bad_inputs:
            with self.subTest(rows=rows, rhs=rhs, width=width):
                with self.assertRaises((ValueError, TypeError)):
                    solve_nonnegative(rows, rhs, n_variables=width)
                self.assertFalse(verify_certificate(rows, rhs, FeasibilityCertificate("FEASIBLE", primal=()),
                                                    n_variables=width))


if __name__ == "__main__":
    unittest.main()
