import unittest

from enterprise_math.material_hysteresis import LOADING, RETURNING
from enterprise_math.material_peak_memory import (
    advance_peak_history_material,
    branch_bit_is_sufficient_for_family,
    peak_conditioned_material_family,
    peak_history_material_state,
    trace_peak_history_schedule,
)
from enterprise_math.material_response import explicit_material_curve_profile


def profile(loading, returning, amplitude=100):
    return explicit_material_curve_profile(loading, returning, amplitude)


class MaterialPeakMemoryTests(unittest.TestCase):
    def setUp(self):
        self.family = peak_conditioned_material_family(
            {
                2: profile(
                    (0, 30, 60, 80, 100),
                    (0, 20, 40, 60, 80),
                ),
                4: profile(
                    (0, 20, 40, 60, 80),
                    (0, 10, 25, 45, 65),
                ),
            }
        )

    def test_same_index_and_branch_can_require_historical_peak(self):
        low_peak = peak_history_material_state(self.family, 1, RETURNING, 2)
        high_peak = peak_history_material_state(self.family, 1, RETURNING, 4)
        self.assertEqual(low_peak.deformation_index, high_peak.deformation_index)
        self.assertEqual(low_peak.branch, high_peak.branch)
        self.assertNotEqual(low_peak.response_sample, high_peak.response_sample)
        self.assertFalse(branch_bit_is_sufficient_for_family(self.family))

    def test_peak_memory_updates_only_when_new_maximum_is_reached(self):
        state = peak_history_material_state(self.family, 1, LOADING, 2)
        down = advance_peak_history_material(self.family, state, 0)
        self.assertEqual(down.branch, RETURNING)
        self.assertEqual(down.historical_peak, 2)
        up_below_peak = advance_peak_history_material(self.family, down, 1)
        self.assertEqual(up_below_peak.branch, LOADING)
        self.assertEqual(up_below_peak.historical_peak, 2)
        with self.assertRaises(ValueError):
            advance_peak_history_material(self.family, up_below_peak, 3)
        high = advance_peak_history_material(self.family, up_below_peak, 4)
        self.assertEqual(high.historical_peak, 4)
        self.assertEqual(high.branch, LOADING)
        returned = advance_peak_history_material(self.family, high, 1)
        self.assertEqual(returned.historical_peak, 4)
        self.assertEqual(returned.branch, RETURNING)
        self.assertEqual(returned.response_sample, 10)

    def test_trace_keeps_peak_after_unloading_and_reloading(self):
        trace = trace_peak_history_schedule(
            self.family,
            (4, 3, 2, 1, 0, 1, 2),
            initial_peak=4,
        )
        self.assertTrue(all(state.historical_peak == 4 for state in trace))
        self.assertEqual(
            [state.branch for state in trace],
            [LOADING, RETURNING, RETURNING, RETURNING, RETURNING, LOADING, LOADING],
        )

    def test_branch_bit_can_be_sufficient_when_all_peak_profiles_are_identical(self):
        common = profile(
            (0, 20, 40, 60, 80),
            (0, 10, 20, 30, 40),
        )
        family = peak_conditioned_material_family({2: common, 4: common})
        self.assertTrue(branch_bit_is_sufficient_for_family(family))

    def test_peak_must_be_explicit_and_not_below_current_index(self):
        with self.assertRaises(ValueError):
            peak_history_material_state(self.family, 3, LOADING, 2)
        with self.assertRaises(ValueError):
            peak_history_material_state(self.family, 1, LOADING, 3)

    def test_family_rejects_duplicate_peak_records_before_mapping(self):
        common = profile(
            (0, 20, 40, 60, 80),
            (0, 10, 20, 30, 40),
        )
        with self.assertRaises(ValueError):
            peak_conditioned_material_family([(2, common), (2, common)])

    def test_family_requires_common_scale_and_domain(self):
        with self.assertRaises(ValueError):
            peak_conditioned_material_family(
                {
                    2: profile((0, 30, 60), (0, 20, 40), 100),
                    4: profile((0, 50, 100), (0, 40, 80), 200),
                }
            )
        with self.assertRaises(ValueError):
            peak_conditioned_material_family(
                {
                    2: profile((0, 30, 60), (0, 20, 40), 100),
                    4: profile((0, 25, 50, 75, 100), (0, 20, 40, 60, 80), 100),
                }
            )


if __name__ == "__main__":
    unittest.main()
