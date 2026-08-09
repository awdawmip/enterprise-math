import unittest

from enterprise_math.material_hysteresis import (
    LOADING,
    RETURNING,
    advance_material_deformation,
    history_response_sum,
    material_state,
    trace_deformation_schedule,
)
from enterprise_math.material_response import material_curve_profile


class MaterialHysteresisTests(unittest.TestCase):
    def setUp(self):
        self.profile = material_curve_profile(
            (0, 250, 500, 750, 1000),
            amplitude=1000,
            loading_power=2,
            return_power=1,
            return_retention=500,
        )

    def test_same_deformation_index_can_retain_different_branch_state(self):
        loading = material_state(self.profile, 3, LOADING)
        returning = material_state(self.profile, 3, RETURNING)
        self.assertEqual(loading.deformation_index, returning.deformation_index)
        self.assertNotEqual(loading.response_sample, returning.response_sample)
        self.assertEqual(loading.response_sample, 562)
        self.assertEqual(returning.response_sample, 375)

    def test_direction_change_selects_loading_or_returning_branch(self):
        state = material_state(self.profile, 1, LOADING)
        loaded = advance_material_deformation(self.profile, state, 3)
        self.assertEqual(loaded.branch, LOADING)
        self.assertEqual(loaded.response_sample, 562)
        returned = advance_material_deformation(self.profile, loaded, 2)
        self.assertEqual(returned.branch, RETURNING)
        self.assertEqual(returned.response_sample, 250)
        held = advance_material_deformation(self.profile, returned, 2)
        self.assertEqual(held.branch, RETURNING)

    def test_full_load_return_schedule_is_path_dependent(self):
        schedule = (0, 1, 2, 3, 4, 3, 2, 1, 0)
        states = trace_deformation_schedule(self.profile, schedule)
        first_index_three = states[3]
        second_index_three = states[5]
        self.assertEqual(first_index_three.deformation_index, 3)
        self.assertEqual(second_index_three.deformation_index, 3)
        self.assertEqual(first_index_three.branch, LOADING)
        self.assertEqual(second_index_three.branch, RETURNING)
        self.assertEqual(first_index_three.response_sample, 562)
        self.assertEqual(second_index_three.response_sample, 375)
        self.assertGreater(history_response_sum(states), 0)

    def test_monotone_loading_never_enters_return_branch(self):
        states = trace_deformation_schedule(self.profile, (0, 1, 2, 3, 4))
        self.assertTrue(all(state.branch == LOADING for state in states))

    def test_invalid_schedule_and_index_are_rejected(self):
        with self.assertRaises(ValueError):
            trace_deformation_schedule(self.profile, ())
        with self.assertRaises(ValueError):
            material_state(self.profile, 99, LOADING)
        with self.assertRaises(ValueError):
            material_state(self.profile, 0, "UNKNOWN")


if __name__ == "__main__":
    unittest.main()
