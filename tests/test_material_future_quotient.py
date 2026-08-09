import unittest

from enterprise_math.material_future_quotient import (
    branch_bit_future_equivalent,
    material_future_signature,
)
from enterprise_math.material_hysteresis import LOADING, RETURNING
from enterprise_math.material_response import material_curve_profile


class MaterialFutureQuotientTests(unittest.TestCase):
    def setUp(self):
        self.profile = material_curve_profile(
            (0, 250, 500, 750, 1000),
            amplitude=1000,
            loading_power=2,
            return_power=1,
            return_retention=500,
        )

    def test_immediate_index_change_erases_current_branch_for_terminal_response(self):
        schedules = ((3, 2), (3, 4), (3, 1), (3, 4, 2))
        self.assertTrue(
            branch_bit_future_equivalent(self.profile, 3, schedules)
        )
        loading = material_future_signature(self.profile, 3, LOADING, schedules)
        returning = material_future_signature(self.profile, 3, RETURNING, schedules)
        self.assertEqual(loading.terminal_responses, returning.terminal_responses)
        self.assertEqual(loading.terminal_branches, returning.terminal_branches)

    def test_hold_action_can_make_current_branch_future_relevant(self):
        schedules = ((3, 3), (3, 2), (3, 4))
        self.assertFalse(
            branch_bit_future_equivalent(self.profile, 3, schedules)
        )
        loading = material_future_signature(self.profile, 3, LOADING, schedules)
        returning = material_future_signature(self.profile, 3, RETURNING, schedules)
        self.assertNotEqual(
            loading.terminal_responses[0],
            returning.terminal_responses[0],
        )
        self.assertEqual(
            loading.terminal_responses[1:],
            returning.terminal_responses[1:],
        )

    def test_branch_can_be_value_irrelevant_but_still_relevant_if_terminal_branch_is_observed(self):
        symmetric_profile = material_curve_profile(
            (0, 250, 500, 750, 1000),
            amplitude=1000,
            loading_power=1,
            return_power=1,
            return_retention=1000,
        )
        schedules = ((3, 3),)
        self.assertTrue(
            branch_bit_future_equivalent(
                symmetric_profile, 3, schedules, include_terminal_branch=False
            )
        )
        self.assertFalse(
            branch_bit_future_equivalent(
                symmetric_profile, 3, schedules, include_terminal_branch=True
            )
        )

    def test_empty_language_makes_branch_vacuously_value_equivalent(self):
        self.assertTrue(branch_bit_future_equivalent(self.profile, 3, ()))

    def test_schedule_must_start_at_declared_initial_index(self):
        with self.assertRaises(ValueError):
            material_future_signature(self.profile, 3, LOADING, ((2, 3),))


if __name__ == "__main__":
    unittest.main()
