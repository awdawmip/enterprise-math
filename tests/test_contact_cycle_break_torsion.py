import itertools
import unittest

from enterprise_math.contact_cycle_break_torsion import (
    cycle_break_torsion_report,
    cycle_degree_zero_target_is_reachable,
    cycle_finite_torsion_order,
    cycle_principal_minor_after_break,
    lift_reduced_degree_zero_target,
    reduced_degree_zero_target,
    solve_cycle_degree_zero_target,
    surviving_tree_edges,
    weighted_cycle_contact_gram,
)
from enterprise_math.contact_forest_reachability import (
    apply_integer_matrix,
)
from enterprise_math.contact_weighted_forest_reachability import (
    solve_weighted_forest_contact_target,
    weighted_forest_contact_gram,
    weighted_tree_determinant,
)


class ContactCycleBreakTorsionTests(unittest.TestCase):
    def test_weighted_cycle_has_zero_row_sum_and_all_ones_kernel(self):
        for weights in (
            (1, 1, 1),
            (2, 3, 5),
            (1, 2, 3, 4),
            (2, 1, 4, 3, 5),
        ):
            gram = weighted_cycle_contact_gram(weights)
            self.assertEqual(
                apply_integer_matrix(gram, (1,) * len(weights)),
                (0,) * len(weights),
            )
            self.assertTrue(all(sum(row) == 0 for row in gram))

    def test_break_principal_minor_is_exact_surviving_tree_gram(self):
        for weights in (
            (1, 1, 1),
            (2, 3, 5),
            (1, 2, 3, 4),
        ):
            n = len(weights)
            for removed in range(n):
                self.assertEqual(
                    cycle_principal_minor_after_break(weights, removed),
                    weighted_forest_contact_gram(
                        n,
                        surviving_tree_edges(n, removed),
                        weights,
                    ),
                )

    def test_degree_zero_reduction_and_lift_are_inverse(self):
        for n in range(3, 8):
            for removed in range(n):
                for reduced in itertools.product(range(-2, 3), repeat=n - 1):
                    full = lift_reduced_degree_zero_target(reduced, removed)
                    self.assertEqual(sum(full), 0)
                    self.assertEqual(
                        reduced_degree_zero_target(full, removed),
                        reduced,
                    )

    def test_full_cycle_reachability_equals_reduced_tree_reachability(self):
        cases = (
            (1, 1, 1),
            (2, 3, 5),
            (1, 2, 3, 4),
        )
        checked = 0
        for weights in cases:
            n = len(weights)
            for removed in range(n):
                tree_edges = surviving_tree_edges(n, removed)
                for reduced in itertools.product(range(-2, 3), repeat=n - 1):
                    full_target = lift_reduced_degree_zero_target(
                        reduced,
                        removed,
                    )
                    tree_impulse = solve_weighted_forest_contact_target(
                        n,
                        tree_edges,
                        weights,
                        reduced,
                    )
                    cycle_impulse = solve_cycle_degree_zero_target(
                        weights,
                        full_target,
                        removed,
                    )
                    self.assertEqual(
                        tree_impulse is not None,
                        cycle_impulse is not None,
                    )
                    self.assertEqual(
                        cycle_degree_zero_target_is_reachable(
                            weights,
                            full_target,
                            removed,
                        ),
                        tree_impulse is not None,
                    )
                    if cycle_impulse is not None:
                        self.assertEqual(
                            apply_integer_matrix(
                                weighted_cycle_contact_gram(weights),
                                cycle_impulse,
                            ),
                            full_target,
                        )
                    checked += 1
        self.assertGreater(checked, 1000)

    def test_cycle_solutions_are_unique_only_modulo_all_ones_kernel(self):
        weights = (2, 3, 5)
        target = (1, 1, -2)
        impulse = solve_cycle_degree_zero_target(
            weights,
            target,
            0,
        )
        if impulse is None:
            # Pick a guaranteed reachable target from one explicit impulse.
            gram = weighted_cycle_contact_gram(weights)
            seed = (2, -1, 0)
            target = apply_integer_matrix(gram, seed)
            impulse = solve_cycle_degree_zero_target(weights, target, 0)
        assert impulse is not None
        gram = weighted_cycle_contact_gram(weights)
        for shift in range(-5, 6):
            candidate = tuple(value + shift for value in impulse)
            self.assertEqual(
                apply_integer_matrix(gram, candidate),
                target,
            )

    def test_first_nonbridge_break_preserves_finite_torsion_order(self):
        for weights in (
            (1, 1, 1),
            (2, 3, 5),
            (1, 2, 3, 4),
            (2, 1, 4, 3, 5),
        ):
            expected = weighted_tree_determinant(weights)
            self.assertEqual(cycle_finite_torsion_order(weights), expected)
            for removed in range(len(weights)):
                report = cycle_break_torsion_report(weights, removed)
                self.assertEqual(report.before_free_rank, 1)
                self.assertEqual(report.after_free_rank, 0)
                self.assertEqual(report.free_rank_drop, 1)
                self.assertEqual(
                    report.finite_torsion_order_before,
                    expected,
                )
                self.assertEqual(
                    report.finite_cokernel_order_after,
                    expected,
                )
                self.assertTrue(report.finite_torsion_order_preserved)

    def test_common_weight_break_removes_only_free_z_part(self):
        for n in range(3, 9):
            for weight in range(1, 5):
                report = cycle_break_torsion_report(
                    (weight,) * n,
                    n // 2,
                )
                self.assertEqual(
                    report.common_weight_torsion_invariant_factors,
                    (weight,) * (n - 2) + (n * weight,),
                )

    def test_triangle_unequal_weight_reference_keeps_order_31(self):
        weights = (2, 3, 5)
        self.assertEqual(cycle_finite_torsion_order(weights), 31)
        for removed in range(3):
            report = cycle_break_torsion_report(weights, removed)
            self.assertEqual(report.finite_torsion_order_before, 31)
            self.assertEqual(report.finite_cokernel_order_after, 31)

    def test_non_degree_zero_target_is_free_cokernel_obstruction(self):
        with self.assertRaises(ValueError):
            solve_cycle_degree_zero_target(
                (1, 1, 1),
                (1, 0, 0),
                0,
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            weighted_cycle_contact_gram((1, 1))
        with self.assertRaises(ValueError):
            cycle_principal_minor_after_break((1, 1, 1), 3)
        with self.assertRaises(ValueError):
            reduced_degree_zero_target((1, -1, 0), -1)


if __name__ == "__main__":
    unittest.main()
