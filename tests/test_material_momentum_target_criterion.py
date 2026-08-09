import unittest
from itertools import combinations_with_replacement

from enterprise_math.material_momentum_target_criterion import (
    alternating_force_from_increments,
    momentum_target_exact_criterion,
    momentum_target_pair_criterion,
)


class MaterialMomentumTargetCriterionTests(unittest.TestCase):
    def test_alternating_formula_is_exact_recurrence_closed_form(self):
        increments = (1, 8, 27, 64)
        forces = alternating_force_from_increments(increments)
        self.assertEqual(forces, (0, 1, 7, 20, 44))
        for k in range(1, len(forces)):
            alternating_sum = sum(
                (-1) ** (k - j) * increments[j - 1]
                for j in range(1, k + 1)
            )
            self.assertEqual(forces[k], alternating_sum)

    def test_nonnegative_force_criterion_is_necessary_and_sufficient_in_bounded_targets(self):
        for length in range(2, 7):
            for tail in combinations_with_replacement(range(0, 8), length - 1):
                targets = (0,) + tuple(tail)
                report = momentum_target_exact_criterion(targets)
                direct = all(force >= 0 for force in report.recurrence_force_samples)
                self.assertEqual(report.nonnegative_force_realizable, direct)
                self.assertEqual(
                    report.alternating_force_samples,
                    report.recurrence_force_samples,
                )

    def test_hardening_margin_is_exact_local_monotonicity_condition(self):
        targets = (0, 1, 3, 6, 10)
        report = momentum_target_exact_criterion(targets)
        self.assertEqual(report.alternating_force_samples, (0, 1, 7, 20, 44))
        self.assertTrue(report.force_nondecreasing)
        self.assertTrue(all(margin >= 0 for margin in report.hardening_margins))

        plateau = momentum_target_exact_criterion((0, 1, 1, 2))
        self.assertEqual(plateau.alternating_force_samples, (0, 1, -1, 4))
        self.assertFalse(plateau.nonnegative_force_realizable)
        self.assertFalse(plateau.force_nondecreasing)

    def test_passive_work_targets_and_local_force_realizability_are_independent(self):
        pair = momentum_target_pair_criterion(
            loading_targets=(0, 2, 3, 4),
            returning_targets=(0, 1, 1, 2),
        )
        self.assertTrue(pair.cumulative_work_passive)
        self.assertFalse(pair.locally_realizable)
        self.assertIsNone(pair.pointwise_return_force_below_loading)

    def test_passive_realizable_pair_need_not_have_pointwise_return_force_below_loading(self):
        loading = (0, 0, 0, 1, 2)
        returning = (0, 0, 0, 0, 2)
        pair = momentum_target_pair_criterion(loading, returning)
        self.assertTrue(pair.cumulative_work_passive)
        self.assertTrue(pair.locally_realizable)
        self.assertEqual(pair.loading.alternating_force_samples, (0, 0, 0, 1, 2))
        self.assertEqual(pair.returning.alternating_force_samples, (0, 0, 0, 0, 4))
        self.assertFalse(pair.pointwise_return_force_below_loading)

    def test_square_slope_targets_satisfy_exact_criterion(self):
        for loading_root in range(1, 7):
            for returning_root in range(0, loading_root + 1):
                loading = tuple(loading_root * k for k in range(0, 8))
                returning = tuple(returning_root * k for k in range(0, 8))
                pair = momentum_target_pair_criterion(loading, returning)
                self.assertTrue(pair.cumulative_work_passive)
                self.assertTrue(pair.locally_realizable)
                self.assertTrue(pair.loading.force_nondecreasing)
                self.assertTrue(pair.returning.force_nondecreasing)

    def test_invalid_targets_are_rejected(self):
        with self.assertRaises(ValueError):
            momentum_target_exact_criterion((1, 2, 3))
        with self.assertRaises(ValueError):
            momentum_target_exact_criterion((0, 2, 1))
        with self.assertRaises(ValueError):
            momentum_target_pair_criterion((0, 1), (0, 1, 2))


if __name__ == "__main__":
    unittest.main()
