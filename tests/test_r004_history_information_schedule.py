import unittest

from enterprise_math.r004_causal_resource_budget import (
    catalan_number,
    uniform_r_adic_minimal_schedule_count,
    uniform_r_adic_storage_advance_area,
)
from enterprise_math.r004_history_information_schedule import (
    history_support_information_levels,
    integer_information_level,
    just_in_time_r_adic_exponents,
    minimum_r_adic_schedule_count,
    minimum_schedule_storage_advance_area,
    minimum_total_r_adic_exponent,
    r_adic_exponent_schedule_fits_history_profile,
)


def weak_compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for suffix in weak_compositions(total - first, parts - 1):
            yield (first,) + suffix


class R004HistoryInformationScheduleTests(unittest.TestCase):
    def test_integer_information_level_matches_canonical_ceiling_power_definition(self):
        self.assertEqual(
            tuple(integer_information_level(10, mass) for mass in (1, 2, 10, 11, 99, 100, 101)),
            (0, 1, 1, 2, 2, 2, 3),
        )
        self.assertEqual(
            tuple(integer_information_level(2, mass) for mass in range(1, 10)),
            (0, 1, 2, 2, 3, 3, 3, 3, 4),
        )

    def test_support_profile_maps_to_integer_demand_profile(self):
        support = (1, 2, 3, 5, 9)
        self.assertEqual(history_support_information_levels(2, support), (0, 1, 2, 3, 4))
        self.assertEqual(minimum_total_r_adic_exponent(2, support), 4)
        self.assertEqual(just_in_time_r_adic_exponents(2, support), (0, 1, 1, 1, 1))

    def test_slow_support_growth_produces_sparse_just_in_time_innovations(self):
        support = (1, 2, 2, 3, 3)
        self.assertEqual(history_support_information_levels(2, support), (0, 1, 1, 2, 2))
        self.assertEqual(just_in_time_r_adic_exponents(2, support), (0, 1, 0, 1, 0))
        self.assertTrue(
            r_adic_exponent_schedule_fits_history_profile(
                2, support, (0, 1, 0, 1, 0)
            )
        )
        self.assertEqual(minimum_schedule_storage_advance_area(2, support, (0, 1, 0, 1, 0)), 0)

    def test_dynamic_program_counts_all_minimum_schedules_above_general_boundary(self):
        profiles = (
            (1,),
            (1, 2, 2),
            (1, 2, 3, 3),
            (1, 2, 2, 3, 5),
            (1, 3, 4, 9),
        )
        for support in profiles:
            base = 2 if support != (1, 3, 4, 9) else 3
            total = minimum_total_r_adic_exponent(base, support)
            brute = [
                row
                for row in weak_compositions(total, len(support))
                if r_adic_exponent_schedule_fits_history_profile(base, support, row)
            ]
            self.assertEqual(minimum_r_adic_schedule_count(base, support), len(brute))

    def test_full_power_history_profile_recovers_catalan_frontier_exactly(self):
        for horizon in range(0, 7):
            support = tuple(2**step for step in range(horizon + 1))
            self.assertEqual(
                history_support_information_levels(2, support),
                tuple(range(horizon + 1)),
            )
            self.assertEqual(
                minimum_r_adic_schedule_count(2, support),
                catalan_number(horizon + 1),
            )
            self.assertEqual(
                minimum_r_adic_schedule_count(2, support),
                uniform_r_adic_minimal_schedule_count(horizon),
            )

    def test_general_area_reduces_to_catalan_storage_area_on_full_tree(self):
        for horizon in range(0, 6):
            support = tuple(2**step for step in range(horizon + 1))
            total = horizon
            for row in weak_compositions(total, horizon + 1):
                if not r_adic_exponent_schedule_fits_history_profile(2, support, row):
                    continue
                self.assertEqual(
                    minimum_schedule_storage_advance_area(2, support, row),
                    uniform_r_adic_storage_advance_area(row),
                )

    def test_coarser_history_support_needs_no_more_integer_information(self):
        fine = (1, 2, 4, 8, 16)
        coarse = (1, 2, 3, 5, 9)
        fine_levels = history_support_information_levels(2, fine)
        coarse_levels = history_support_information_levels(2, coarse)
        self.assertTrue(all(c <= f for c, f in zip(coarse_levels, fine_levels, strict=True)))
        self.assertLessEqual(
            minimum_total_r_adic_exponent(2, coarse),
            minimum_total_r_adic_exponent(2, fine),
        )

    def test_invalid_inputs_fail_closed(self):
        with self.assertRaises(ValueError):
            integer_information_level(1, 2)
        with self.assertRaises(ValueError):
            integer_information_level(2, 0)
        with self.assertRaises(ValueError):
            history_support_information_levels(2, ())
        with self.assertRaises(ValueError):
            history_support_information_levels(2, (1, 3, 2))
        with self.assertRaises(ValueError):
            r_adic_exponent_schedule_fits_history_profile(2, (1, 2), (1,))
        with self.assertRaises(ValueError):
            r_adic_exponent_schedule_fits_history_profile(2, (1, 2), (0, -1))
        with self.assertRaises(ValueError):
            minimum_schedule_storage_advance_area(2, (1, 2, 4), (0, 1, 0))


if __name__ == "__main__":
    unittest.main()
