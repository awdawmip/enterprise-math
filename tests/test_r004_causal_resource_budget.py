import unittest

from enterprise_math.r004_causal_resource_budget import (
    causal_history_capacity_profile,
    finite_horizon_static_compilation_bound,
    first_budget_violation_step,
    history_support_profile_fits_budget,
    prestored_prefix_then_online_schedule,
    static_uniform_history_atom_requirement,
    uniform_full_support_history_profile,
    uniform_history_budget_holds,
)


class R004CausalResourceBudgetTests(unittest.TestCase):
    def test_capacity_profile_is_prefix_product(self):
        self.assertEqual(
            causal_history_capacity_profile(3, (2, 5, 7)),
            (3, 6, 30, 210),
        )
        self.assertEqual(finite_horizon_static_compilation_bound(3, (2, 5, 7)), 210)

    def test_full_uniform_history_support_profile_is_exact_power_tree(self):
        self.assertEqual(uniform_full_support_history_profile(2, 5), (1, 2, 4, 8, 16, 32))
        self.assertEqual(uniform_full_support_history_profile(3, 3), (1, 3, 9, 27))
        self.assertEqual(static_uniform_history_atom_requirement(2, 5), 32)
        self.assertEqual(static_uniform_history_atom_requirement(3, 3), 27)

    def test_static_presampling_requires_full_history_support(self):
        horizon = 6
        support = uniform_full_support_history_profile(2, horizon)
        self.assertTrue(
            history_support_profile_fits_budget(support, 2**horizon, (1,) * horizon)
        )
        self.assertFalse(
            history_support_profile_fits_budget(support, 2**horizon - 1, (1,) * horizon)
        )
        self.assertEqual(
            first_budget_violation_step(support, 2**horizon - 1, (1,) * horizon),
            horizon,
        )

    def test_pure_online_uniform_innovation_hits_every_prefix_bound_exactly(self):
        horizon = 7
        self.assertTrue(uniform_history_budget_holds(2, horizon, 1, (2,) * horizon))
        self.assertEqual(
            causal_history_capacity_profile(1, (2,) * horizon),
            uniform_full_support_history_profile(2, horizon),
        )

    def test_prestorage_runtime_tradeoff_schedules_all_meet_the_same_target(self):
        r = 3
        horizon = 5
        final_target = r**horizon
        for prestored in range(horizon + 1):
            initial, innovations = prestored_prefix_then_online_schedule(r, horizon, prestored)
            self.assertTrue(uniform_history_budget_holds(r, horizon, initial, innovations))
            self.assertEqual(
                finite_horizon_static_compilation_bound(initial, innovations),
                final_target,
            )
            self.assertEqual(initial, r**prestored)
            self.assertEqual(innovations[:prestored], (1,) * prestored)
            self.assertEqual(innovations[prestored:], (r,) * (horizon - prestored))

    def test_insufficient_runtime_innovation_is_detected_at_first_prefix(self):
        support = uniform_full_support_history_profile(3, 4)
        innovations = (3, 2, 3, 3)
        self.assertFalse(history_support_profile_fits_budget(support, 1, innovations))
        self.assertEqual(first_budget_violation_step(support, 1, innovations), 2)

    def test_more_initial_storage_can_delay_fresh_innovation_requirement(self):
        support = uniform_full_support_history_profile(2, 6)
        initial = 8
        innovations = (1, 1, 1, 2, 2, 2)
        self.assertTrue(history_support_profile_fits_budget(support, initial, innovations))
        self.assertEqual(causal_history_capacity_profile(initial, innovations), (8, 8, 8, 8, 16, 32, 64))

    def test_invalid_inputs_fail_closed(self):
        with self.assertRaises(ValueError):
            causal_history_capacity_profile(0, (2,))
        with self.assertRaises(ValueError):
            causal_history_capacity_profile(1, (2, 0))
        with self.assertRaises(ValueError):
            history_support_profile_fits_budget((1, 2), 1, (2, 2))
        with self.assertRaises(ValueError):
            history_support_profile_fits_budget((1, 0), 1, (1,))
        with self.assertRaises(ValueError):
            uniform_full_support_history_profile(0, 2)
        with self.assertRaises(ValueError):
            uniform_full_support_history_profile(2, -1)
        with self.assertRaises(ValueError):
            uniform_history_budget_holds(2, 2, 1, (2,))
        with self.assertRaises(ValueError):
            prestored_prefix_then_online_schedule(2, 3, 4)


if __name__ == "__main__":
    unittest.main()
