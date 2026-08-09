import unittest

from enterprise_math.material_dynamic_passivity import (
    chord_branch_work_over_saved_schedule_numerator2,
    current_hold_branch_work_numerator2,
    sampled_cycle_passivity_report,
)
from enterprise_math.material_force_work import uniform_force_law
from enterprise_math.material_hysteresis import LOADING, RETURNING
from enterprise_math.material_response import explicit_material_curve_profile


class MaterialDynamicPassivityTests(unittest.TestCase):
    def test_two_state_elastic_curve_is_static_passive_but_current_sampling_is_superelastic(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 10), returning=(0, 10), amplitude=10
            )
        )
        report = sampled_cycle_passivity_report(law, (0, 1), (1, 0))
        self.assertEqual(report.static_chord_loss_numerator2, 0)
        self.assertTrue(report.static_chord_passive)
        self.assertEqual(report.current_loading_work_numerator2, 0)
        self.assertEqual(report.current_returning_work_numerator2, 20)
        self.assertEqual(report.current_sampled_loss_numerator2, -20)
        self.assertFalse(report.current_sampled_passive)
        self.assertTrue(report.force_sampling_changes_passivity)

    def test_chord_branch_work_telescopes_independent_of_saved_schedule(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1, 4, 9, 16), returning=(0, 1, 3, 6, 10), amplitude=16
            )
        )
        load_coarse = chord_branch_work_over_saved_schedule_numerator2(law, (0, 4), LOADING)
        load_fine = chord_branch_work_over_saved_schedule_numerator2(law, (0, 1, 2, 3, 4), LOADING)
        ret_coarse = chord_branch_work_over_saved_schedule_numerator2(law, (4, 0), RETURNING)
        ret_fine = chord_branch_work_over_saved_schedule_numerator2(law, (4, 3, 2, 1, 0), RETURNING)
        self.assertEqual(load_coarse, load_fine)
        self.assertEqual(ret_coarse, ret_fine)

    def test_current_hold_cycle_depends_on_saved_schedule_even_for_same_material_curve(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 2, 5, 9), returning=(0, 1, 3, 6), amplitude=9
            )
        )
        coarse = sampled_cycle_passivity_report(law, (0, 3), (3, 0))
        fine = sampled_cycle_passivity_report(law, (0, 1, 2, 3), (3, 2, 1, 0))
        self.assertEqual(coarse.static_chord_loss_numerator2, fine.static_chord_loss_numerator2)
        self.assertNotEqual(coarse.current_sampled_loss_numerator2, fine.current_sampled_loss_numerator2)

    def test_pointwise_return_below_loading_does_not_rescue_arbitrary_current_sampling(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 5, 10), returning=(0, 4, 9), amplitude=10
            )
        )
        self.assertTrue(all(r <= l for l, r in zip(law.profile.loading, law.profile.returning)))
        report = sampled_cycle_passivity_report(law, (0, 2), (2, 0))
        self.assertTrue(report.static_chord_passive)
        self.assertFalse(report.current_sampled_passive)

    def test_constant_force_is_sampling_passivity_neutral(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(4, 4, 4, 4), returning=(4, 4, 4, 4), amplitude=4
            )
        )
        for load, ret in (
            ((0, 3), (3, 0)),
            ((0, 1, 3), (3, 2, 0)),
            ((0, 1, 2, 3), (3, 2, 1, 0)),
        ):
            report = sampled_cycle_passivity_report(law, load, ret)
            self.assertEqual(report.current_sampled_loss_numerator2, 0)
            self.assertEqual(report.static_chord_loss_numerator2, 0)
            self.assertTrue(report.current_sampled_passive)

    def test_current_hold_branch_work_matches_manual_orientation(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 2, 5), returning=(0, 1, 3), amplitude=5
            )
        )
        self.assertEqual(
            current_hold_branch_work_numerator2(law, (0, 1, 2), LOADING),
            2 * 0 + 2 * 2,
        )
        self.assertEqual(
            current_hold_branch_work_numerator2(law, (2, 1, 0), RETURNING),
            2 * 3 + 2 * 1,
        )

    def test_invalid_cycle_schedules_are_rejected(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1, 2), returning=(0, 1, 2), amplitude=2
            )
        )
        with self.assertRaises(ValueError):
            sampled_cycle_passivity_report(law, (0, 2), (1, 0))
        with self.assertRaises(ValueError):
            current_hold_branch_work_numerator2(law, (0, 2, 1), LOADING)
        with self.assertRaises(ValueError):
            current_hold_branch_work_numerator2(law, (2, 0, 1), RETURNING)


if __name__ == "__main__":
    unittest.main()
