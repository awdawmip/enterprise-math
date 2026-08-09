import unittest

from enterprise_math.causal_conservation_tomography import (
    exact_total_law,
    modular_total_law,
    unit_amplitude_events,
)
from enterprise_math.causal_dimension_revelation import (
    dimension_profile,
    dimension_revelation_spectrum,
    event_rank_through_grade,
    modular_unit_dimension_profile,
    support_grade,
)


class CausalDimensionRevelationTests(unittest.TestCase):
    def test_unconstrained_mod_one_reveals_full_rank_at_support_one(self):
        for slots in range(2, 7):
            profile = modular_unit_dimension_profile(slots, 1)
            self.assertEqual(profile[0], 0)
            self.assertEqual(profile[1], slots)
            self.assertTrue(all(rank == slots for rank in profile[1:]))

    def test_parity_mod_two_reveals_full_rank_at_support_two(self):
        for slots in range(2, 7):
            profile = modular_unit_dimension_profile(slots, 2)
            self.assertEqual(profile[0], 0)
            self.assertEqual(profile[1], 0)
            self.assertEqual(profile[2], slots)

    def test_mod_three_plus_has_a_rank_first_shell_then_one_dimension_jump(self):
        for modulus in range(3, 7):
            slots = modulus + 1
            profile = modular_unit_dimension_profile(slots, modulus)
            self.assertEqual(profile[0], 0)
            self.assertEqual(profile[1], 0)
            for budget in range(2, modulus):
                self.assertEqual(profile[budget], slots - 1)
            self.assertEqual(profile[modulus], slots)
            revelation = dimension_revelation_spectrum(profile)
            self.assertEqual(revelation[2], slots - 1)
            self.assertEqual(revelation[modulus], 1)
            self.assertEqual(sum(revelation), slots)

    def test_four_slot_mod_three_is_low_grade_a3_then_full_rank_four(self):
        profile = modular_unit_dimension_profile(4, 3)
        self.assertEqual(profile, (0, 0, 3, 4))
        self.assertEqual(dimension_revelation_spectrum(profile), (0, 0, 3, 1))

    def test_exact_total_conservation_stays_rank_n_minus_one_at_every_visible_support(self):
        for slots in range(2, 7):
            universe = unit_amplitude_events(slots)
            profile = dimension_profile(
                universe,
                exact_total_law,
                support_grade,
                slots,
            )
            self.assertEqual(profile[0], 0)
            self.assertEqual(profile[1], 0)
            self.assertTrue(all(rank == slots - 1 for rank in profile[2:]))

    def test_event_rank_is_monotone_under_grade_budget(self):
        universe = unit_amplitude_events(5)
        law = modular_total_law(4)
        ranks = tuple(
            event_rank_through_grade(universe, law, support_grade, budget)
            for budget in range(6)
        )
        self.assertTrue(all(left <= right for left, right in zip(ranks, ranks[1:])))
        self.assertEqual(ranks, (0, 0, 4, 4, 5, 5))


if __name__ == "__main__":
    unittest.main()
