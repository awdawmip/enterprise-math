import unittest
from itertools import combinations_with_replacement

from enterprise_math.material_momentum_target_synthesis import (
    force_samples_from_momentum_targets,
    momentum_target_branch_realizability,
    momentum_target_material_family,
    squared_work_increments_nondecreasing,
)


class MaterialMomentumTargetSynthesisTests(unittest.TestCase):
    def test_linear_integer_momentum_targets_recover_hooke_force(self):
        targets = tuple(range(0, 11))
        forces = force_samples_from_momentum_targets(targets)
        self.assertEqual(forces, targets)
        report = momentum_target_branch_realizability(targets)
        self.assertTrue(report.nonnegative_force_realizable)
        self.assertTrue(report.sufficient_convexity_condition)
        self.assertTrue(report.force_nondecreasing)

    def test_nonlinear_convex_square_targets_generate_nonnegative_hardening_force(self):
        targets = tuple(k * k for k in range(0, 7))
        report = momentum_target_branch_realizability(targets)
        self.assertTrue(report.sufficient_convexity_condition)
        self.assertTrue(report.nonnegative_force_realizable)
        self.assertEqual(report.force_samples[:5], (0, 1, 14, 51, 124))

    def test_passive_cumulative_return_targets_can_fail_local_nonnegative_force_realizability(self):
        targets = (0, 1, 1, 2)
        report = momentum_target_branch_realizability(targets)
        self.assertEqual(report.force_samples, (0, 1, -1, 4))
        self.assertFalse(report.nonnegative_force_realizable)
        self.assertEqual(report.first_negative_force_depth, 2)
        with self.assertRaises(ValueError):
            momentum_target_material_family((0, 2, 3, 4), targets)

    def test_nondecreasing_squared_work_increments_are_sufficient_in_bounded_search(self):
        for length in range(2, 7):
            for tail in combinations_with_replacement(range(0, 7), length - 1):
                targets = (0,) + tuple(tail)
                if squared_work_increments_nondecreasing(targets):
                    report = momentum_target_branch_realizability(targets)
                    self.assertTrue(report.nonnegative_force_realizable)
                    self.assertTrue(all(force >= 0 for force in report.force_samples))

    def test_synthesized_nonlinear_material_hits_every_target_square_work_exactly(self):
        loading = (0, 1, 3, 6, 10)
        returning = (0, 1, 2, 4, 7)
        family = momentum_target_material_family(loading, returning)
        self.assertTrue(family.passive_work_targets)
        self.assertEqual(family.loading_realizability.force_samples, (0, 1, 7, 20, 44))
        self.assertEqual(family.returning_realizability.force_samples, (0, 1, 2, 10, 23))
        # The constructor itself verifies every prefix square; here keep one visible reference.
        self.assertEqual(family.law.profile.loading[-1], 44)
        self.assertEqual(family.law.profile.returning[-1], 23)

    def test_square_slope_family_is_recovered_as_linear_momentum_targets(self):
        loading_targets = tuple(5 * k for k in range(0, 8))
        returning_targets = tuple(3 * k for k in range(0, 8))
        family = momentum_target_material_family(loading_targets, returning_targets)
        self.assertEqual(
            family.law.profile.loading,
            tuple(25 * k for k in range(0, 8)),
        )
        self.assertEqual(
            family.law.profile.returning,
            tuple(9 * k for k in range(0, 8)),
        )

    def test_passivity_is_a_work_prefix_condition_not_a_local_force_order_requirement(self):
        # Search for a realizable pair with Q<=P but some local return force above loading force.
        found = None
        candidates = []
        for tail in combinations_with_replacement(range(0, 8), 4):
            targets = (0,) + tuple(tail)
            report = momentum_target_branch_realizability(targets)
            if report.nonnegative_force_realizable:
                candidates.append((targets, report.force_samples))
        for loading, l_force in candidates:
            for returning, r_force in candidates:
                if all(q <= p for p, q in zip(loading, returning)) and any(
                    r > l for l, r in zip(l_force, r_force)
                ):
                    found = (loading, returning)
                    break
            if found:
                break
        self.assertIsNotNone(found)
        family = momentum_target_material_family(*found)
        self.assertTrue(family.passive_work_targets)
        self.assertTrue(
            any(r > l for l, r in zip(family.law.profile.loading, family.law.profile.returning))
        )

    def test_invalid_targets_are_rejected(self):
        with self.assertRaises(ValueError):
            momentum_target_branch_realizability((1, 2, 3))
        with self.assertRaises(ValueError):
            momentum_target_branch_realizability((0, 2, 1))
        with self.assertRaises(ValueError):
            momentum_target_material_family((0, 1, 2), (0, 1))
        with self.assertRaises(ValueError):
            momentum_target_material_family((0, 1, 2), (0, 1, 3))


if __name__ == "__main__":
    unittest.main()
