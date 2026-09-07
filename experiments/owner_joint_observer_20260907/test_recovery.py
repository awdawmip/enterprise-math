"""Independent bounded regression of the noncanonical raw X6 recovery adapter.

No finite test below substitutes for the support-bound induction proof. The
known feasible 21-point case records a SymPy 1.14.0 limitation: refusing an
unverified answer is acceptable; issuing an incorrect certificate is not.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
import random
import unittest
from unittest.mock import patch

import recovery
from observer_certificate import Branch, all_three_axis_tables, parity_branches
from sympy.solvers.simplex import InfeasibleLPError


# Seed 2026090709, trial 13 in the audit's expanding binary-six population probe.
FEASIBLE_SOLVER_STRESS = (
    (1, 1, 1, 0, 0, 1), (1, 0, 0, 0, 0, 1), (0, 1, 1, 1, 0, 1),
    (1, 1, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1), (1, 1, 0, 0, 0, 0),
    (1, 1, 1, 1, 1, 0), (1, 0, 1, 0, 0, 0), (1, 1, 0, 0, 1, 0),
    (0, 0, 1, 1, 1, 0), (0, 1, 1, 1, 1, 1), (0, 1, 0, 0, 1, 1),
    (0, 1, 0, 0, 0, 1), (1, 0, 0, 0, 1, 1), (1, 0, 0, 1, 0, 1),
    (0, 1, 1, 0, 1, 0), (1, 1, 0, 1, 1, 0), (1, 1, 1, 0, 1, 0),
    (0, 0, 1, 1, 1, 1), (0, 0, 0, 1, 1, 0), (0, 0, 0, 1, 0, 0),
)


def population(points, weights=None):
    if weights is None:
        weights = [Fraction(1)] * len(points)
    return tuple(Branch(str(i), point, weight) for i, (point, weight) in enumerate(zip(points, weights)))


class RecoveryAudit(unittest.TestCase):
    def assert_verified(self, tables, answer):
        self.assertTrue(all(mass > 0 for _, mass in answer["distribution"]))
        recovered = population([z for z, _ in answer["distribution"]], [w for _, w in answer["distribution"]])
        self.assertEqual(all_three_axis_tables(recovered), tables)

    def test_56_signed_nonuniform_sparse_populations(self):
        rng = random.Random(2026090717)
        carrier = list(product((0, 1), repeat=6))
        for size in range(1, 8):
            for trial in range(8):
                with self.subTest(size=size, trial=trial):
                    points = [tuple((axis + 2) * bit - 4 - trial for axis, bit in enumerate(point))
                              for point in rng.sample(carrier, size)]
                    weights = [Fraction(rng.randrange(1, 10), rng.randrange(1, 10)) for _ in points]
                    source = population(points, weights)
                    tables = all_three_axis_tables(source)
                    answer = recovery.recover(tables)
                    self.assertEqual(answer["status"], "UNIQUE_BY_SUPPORT_BOUND")
                    self.assertEqual(dict(answer["distribution"]), dict(zip(points, weights)))
                    self.assertLessEqual(answer["candidate_count"], answer["prefilter_join_count"])
                    self.assertLessEqual(answer["prefilter_join_count"], size * size)
                    self.assert_verified(tables, answer)

    def test_120_deleted_parity_points_across_all_active_axes(self):
        bits = [p for p in product((0, 1), repeat=4) if sum(p) % 2 == 0]
        for active in combinations(range(6), 4):
            for omitted in range(8):
                with self.subTest(active=active, omitted=omitted):
                    points = []
                    for index, point in enumerate(bits):
                        if index == omitted:
                            continue
                        coordinate = [-3] * 6
                        for axis, bit in zip(active, point):
                            coordinate[axis] += bit * (axis + 2)
                        points.append(tuple(coordinate))
                    source = population(points)
                    answer = recovery.recover(all_three_axis_tables(source))
                    self.assertEqual(answer["status"], "UNIQUE_BY_SUPPORT_BOUND")
                    self.assertEqual(dict(answer["distribution"]), {point: Fraction(1) for point in points})

    def test_eight_point_collision_never_certified_unique(self):
        even, odd = parity_branches(0), parity_branches(1)
        tables = all_three_axis_tables(even)
        self.assertEqual(tables, all_three_axis_tables(odd))
        answer = recovery.recover(tables)
        self.assertEqual(answer["status"], "FEASIBLE_UNIQUENESS_UNCLASSIFIED")
        self.assertEqual((answer["candidate_count"], answer["equation_rank"]), (16, 15))
        self.assert_verified(tables, answer)

    def test_raw_depth_is_required_even_for_one_cell(self):
        origin, diagonal = (0,) * 6, (1,) * 6
        raw0 = all_three_axis_tables(population([origin]))
        raw1 = all_three_axis_tables(population([diagonal]))
        self.assertNotEqual(raw0, raw1)
        for axes in recovery.AXES:
            canonical = lambda point: tuple(point[a] - min(point[b] for b in axes) for a in axes)
            self.assertEqual(canonical(origin), canonical(diagonal))
        self.assertEqual(dict(recovery.recover(raw1)["distribution"]), {diagonal: Fraction(1)})

    def test_branch_count_is_not_spatial_support_count(self):
        source = population([(0,) * 6, (0,) * 6], [Fraction(2, 3), Fraction(5, 7)])
        answer = recovery.recover(all_three_axis_tables(source))
        self.assertEqual(answer["support_count"], 1)
        self.assertEqual(dict(answer["distribution"]), {(0,) * 6: Fraction(29, 21)})

    def test_empty_and_explicit_zero_tables(self):
        tables = {axes: {(0, 0, 0): Fraction(0)} for axes in recovery.AXES}
        answer = recovery.recover(tables)
        self.assertEqual(answer["status"], "UNIQUE_ZERO")
        self.assertEqual(answer["distribution"], ())

    def test_reject_invalid_marginal_contract(self):
        valid = all_three_axis_tables(population([(0,) * 6]))
        missing = dict(valid)
        missing.pop(recovery.AXES[0])
        with self.assertRaises(ValueError):
            recovery.recover(missing)
        bool_axis = dict(valid)
        first_table = bool_axis.pop((0, 1, 2))
        bool_axis[(False, 1, 2)] = first_table
        with self.assertRaisesRegex(ValueError, "axis"):
            recovery.recover(bool_axis)
        for bad_mass in (-1, True, 0.5):
            bad = {axes: dict(table) for axes, table in valid.items()}
            bad[recovery.AXES[0]][(0, 0, 0)] = bad_mass
            with self.subTest(mass=bad_mass), self.assertRaises((ValueError, TypeError)):
                recovery.recover(bad)
        for bad_address in ((True, 0, 0), (0, 0), (0.0, 0, 0)):
            bad = {axes: dict(table) for axes, table in valid.items()}
            bad[recovery.AXES[0]] = {bad_address: Fraction(1)}
            with self.subTest(address=bad_address), self.assertRaises(ValueError):
                recovery.recover(bad)

    def test_equal_total_inconsistent_equations_are_rejected(self):
        tables = all_three_axis_tables(parity_branches(0))
        first = tables[(0, 1, 2)]
        first[(0, 0, 0)] += Fraction(1, 2)
        first[(0, 0, 1)] -= Fraction(1, 2)
        with self.assertRaisesRegex(ValueError, "inconsistent marginal equations"):
            recovery.recover(tables)

    def test_budget_rejection_is_not_an_infeasibility_claim(self):
        tables = all_three_axis_tables(parity_branches(0)[:-1])
        with self.assertRaisesRegex(ValueError, "no mathematical conclusion"):
            recovery.recover(tables, max_candidates=1)

    def test_coordinates_are_frozen_after_construction(self):
        coordinate = [0] * 6
        branch = Branch("mutable-input", coordinate)
        coordinate[0] = 0.25
        self.assertEqual(branch.coordinate, (0,) * 6)
        self.assertIsInstance(branch.coordinate, tuple)

    def test_malicious_solver_parameters_cannot_escape_validation(self):
        tables = all_three_axis_tables(population(FEASIBLE_SOLVER_STRESS))
        with patch.object(recovery, "linprog", side_effect=lambda objective, *a, **kw: (0, [0] * len(objective))) as solver:
            with self.assertRaisesRegex(ArithmeticError, "negative mass"):
                recovery.recover(tables)
            self.assertEqual(solver.call_count, 1)

    def test_solver_infeasible_report_is_not_mathematical_certificate(self):
        tables = all_three_axis_tables(population(FEASIBLE_SOLVER_STRESS))
        with patch.object(recovery, "linprog", side_effect=InfeasibleLPError("injected failure")):
            with self.assertRaisesRegex(ArithmeticError, "no verified infeasibility certificate"):
                recovery.recover(tables)

    def test_known_feasible_solver_stress_is_verified_or_refused(self):
        tables = all_three_axis_tables(population(FEASIBLE_SOLVER_STRESS))
        try:
            answer = recovery.recover(tables)
        except ArithmeticError:
            # A dependency failure is a supported incomplete outcome. ValueError
            # would be a false mathematical infeasibility claim for this input.
            return
        self.assert_verified(tables, answer)
        self.assertEqual(answer["status"], "FEASIBLE_UNIQUENESS_UNCLASSIFIED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
