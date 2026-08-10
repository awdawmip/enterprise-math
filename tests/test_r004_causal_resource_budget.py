import unittest
from collections import Counter

from enterprise_math.r004_causal_resource_budget import (
    catalan_number,
    causal_history_capacity_profile,
    finite_horizon_static_compilation_bound,
    first_budget_violation_step,
    history_support_profile_fits_budget,
    prestored_prefix_then_online_schedule,
    static_uniform_history_atom_requirement,
    uniform_full_support_history_profile,
    uniform_history_budget_holds,
    uniform_r_adic_minimal_schedule_count,
    uniform_r_adic_minimal_schedule_holds,
    uniform_r_adic_storage_advance_area,
    uniform_r_adic_storage_advance_area_bounds,
)


def weak_compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for suffix in weak_compositions(total - first, parts - 1):
            yield (first,) + suffix


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

    def test_minimum_r_adic_schedule_predicate(self):
        self.assertTrue(uniform_r_adic_minimal_schedule_holds((0, 1, 1, 1)))
        self.assertTrue(uniform_r_adic_minimal_schedule_holds((3, 0, 0, 0)))
        self.assertTrue(uniform_r_adic_minimal_schedule_holds((0, 2, 1, 0)))
        self.assertFalse(uniform_r_adic_minimal_schedule_holds((0, 0, 3, 0)))
        self.assertFalse(uniform_r_adic_minimal_schedule_holds((1, 1, 1, 1)))

    def test_minimum_r_adic_frontier_is_catalan(self):
        expected = (1, 1, 2, 5, 14, 42, 132, 429)
        self.assertEqual(tuple(catalan_number(index) for index in range(8)), expected)
        for horizon in range(0, 7):
            schedules = [
                row
                for row in weak_compositions(horizon, horizon + 1)
                if uniform_r_adic_minimal_schedule_holds(row)
            ]
            self.assertEqual(
                len(schedules),
                uniform_r_adic_minimal_schedule_count(horizon),
            )
            self.assertEqual(len(schedules), catalan_number(horizon + 1))

    def test_storage_advance_area_has_online_and_static_extremes(self):
        for horizon in range(0, 7):
            online = (0,) + (1,) * horizon
            static = (horizon,) + (0,) * horizon
            minimum, maximum = uniform_r_adic_storage_advance_area_bounds(horizon)
            self.assertEqual(minimum, 0)
            self.assertEqual(maximum, horizon * (horizon + 1) // 2)
            self.assertEqual(uniform_r_adic_storage_advance_area(online), minimum)
            self.assertEqual(uniform_r_adic_storage_advance_area(static), maximum)

    def test_storage_advance_area_refines_catalan_frontier(self):
        expected_distributions = {
            1: {0: 1, 1: 1},
            2: {0: 1, 1: 2, 2: 1, 3: 1},
            3: {0: 1, 1: 3, 2: 3, 3: 3, 4: 2, 5: 1, 6: 1},
            4: {0: 1, 1: 4, 2: 6, 3: 7, 4: 7, 5: 5, 6: 5, 7: 3, 8: 2, 9: 1, 10: 1},
        }
        for horizon, expected in expected_distributions.items():
            distribution = Counter(
                uniform_r_adic_storage_advance_area(row)
                for row in weak_compositions(horizon, horizon + 1)
                if uniform_r_adic_minimal_schedule_holds(row)
            )
            self.assertEqual(dict(distribution), expected)
            self.assertEqual(sum(distribution.values()), catalan_number(horizon + 1))

    def test_every_minimum_r_adic_schedule_meets_uniform_prefix_capacity(self):
        r = 2
        for horizon in range(0, 6):
            target = uniform_full_support_history_profile(r, horizon)
            for exponents in weak_compositions(horizon, horizon + 1):
                if not uniform_r_adic_minimal_schedule_holds(exponents):
                    continue
                initial = r ** exponents[0]
                innovations = tuple(r**value for value in exponents[1:])
                self.assertTrue(
                    history_support_profile_fits_budget(target, initial, innovations)
                )
                self.assertEqual(
                    finite_horizon_static_compilation_bound(initial, innovations),
                    r**horizon,
                )

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
        with self.assertRaises(ValueError):
            uniform_r_adic_minimal_schedule_holds(())
        with self.assertRaises(ValueError):
            uniform_r_adic_minimal_schedule_holds((0, -1))
        with self.assertRaises(ValueError):
            uniform_r_adic_storage_advance_area((0, 0, 2))
        with self.assertRaises(ValueError):
            uniform_r_adic_storage_advance_area_bounds(-1)
        with self.assertRaises(ValueError):
            catalan_number(-1)


if __name__ == "__main__":
    unittest.main()
