import unittest

from enterprise_math.material_force_activation_sampling import (
    ALREADY_ACTIVE,
    NO_POSITIVE_FORCE_REPRESENTED,
    SAMPLED_AFTER_ZERO_PREFIX,
    SKIPPED_POSITIVE_FORCE_WINDOW,
    ZERO_DRIFT_STALL,
    engagement_then_reversal_certificate,
    force_activation_sampling_report,
)
from enterprise_math.material_impulse_world_1d import (
    MATERIAL_KICK,
    MATERIAL_ZERO_FORCE,
    TERMINAL_CONTACT,
    MomentumMaterialState1D,
    run_impulse_material_world_1d,
)
from enterprise_math.material_response import explicit_material_curve_profile
from enterprise_math.scale_tunneling_1d import Wall1D


class MaterialForceActivationSamplingTests(unittest.TestCase):
    def setUp(self):
        self.profile = explicit_material_curve_profile(
            loading=(0, 0, 0, 4, 4, 4),
            returning=(0, 0, 0, 4, 4, 4),
            amplitude=4,
        )

    def test_saved_depth_arithmetic_progression_can_hit_positive_force_layer(self):
        report = force_activation_sampling_report(
            collapse_factor=6,
            current_depth=1,
            inward_lifted_momentum_numerator=20,
            profile=self.profile,
            mass_quanta=2,
        )
        self.assertEqual(report.zero_force_saved_drift_cells, 2)
        self.assertEqual(report.first_positive_sample_tick, 1)
        self.assertEqual(report.first_positive_sample_depth, 3)
        self.assertEqual(report.first_positive_sample_gap, 3)
        self.assertEqual(report.status, SAMPLED_AFTER_ZERO_PREFIX)
        self.assertTrue(report.force_layer_sampled)

    def test_fast_saved_drift_can_skip_every_positive_force_state(self):
        report = force_activation_sampling_report(
            6, 1, 20, self.profile, mass_quanta=1
        )
        self.assertEqual(report.zero_force_saved_drift_cells, 5)
        self.assertEqual(report.status, SKIPPED_POSITIVE_FORCE_WINDOW)
        self.assertFalse(report.force_layer_sampled)

        # The causal world samples a represented zero-force material state, then
        # drifts straight to terminal geometry before any positive-force state.
        history = run_impulse_material_world_1d(
            MomentumMaterialState1D(-5, 5),
            Wall1D(0, 0),
            0,
            6,
            self.profile,
            1,
            2,
            ticks=1,
        )
        transition = history.transitions[0]
        self.assertEqual(history.halted_kind, TERMINAL_CONTACT)
        self.assertEqual(transition.response_sample, 0)
        self.assertEqual(transition.layer_depth, 1)
        self.assertIsNone(transition.impulse)
        # Terminal geometry owns the final kind, but the retained response/depth
        # witnesses prove that the pre-drift material sample was exactly zero.

    def test_zero_force_nonterminal_tick_is_distinct_from_free_drift(self):
        history = run_impulse_material_world_1d(
            MomentumMaterialState1D(-5, 2),
            Wall1D(0, 0),
            0,
            6,
            self.profile,
            2,
            2,
            ticks=1,
        )
        transition = history.transitions[0]
        self.assertEqual(transition.kind, MATERIAL_ZERO_FORCE)
        self.assertEqual(transition.response_sample, 0)
        self.assertEqual(transition.layer_depth, 1)
        self.assertIsNone(transition.impulse)
        self.assertEqual(transition.after.momentum_quanta, 2)
        self.assertEqual(transition.after.impulse_detail_numerator, 0)

    def test_jump_may_skip_first_positive_depth_but_still_sample_a_deeper_positive_depth(self):
        report = force_activation_sampling_report(
            7, 1, 28, self.profile, mass_quanta=2
        )
        # A=4,M=2 => q=3; depths 1 -> 4, skipping k0=3 but landing
        # inside the positive-force interval.
        self.assertEqual(report.zero_force_saved_drift_cells, 3)
        self.assertEqual(report.first_positive_sample_depth, 4)
        self.assertEqual(report.status, SAMPLED_AFTER_ZERO_PREFIX)

    def test_zero_whole_drift_inside_zero_force_prefix_is_a_true_stall(self):
        report = force_activation_sampling_report(
            6, 1, 4, self.profile, mass_quanta=2
        )
        self.assertEqual(report.zero_force_saved_drift_cells, 0)
        self.assertEqual(report.status, ZERO_DRIFT_STALL)
        self.assertFalse(report.force_layer_sampled)

    def test_positive_force_outside_spatially_represented_depth_is_not_invented(self):
        report = force_activation_sampling_report(
            collapse_factor=3,
            current_depth=1,
            inward_lifted_momentum_numerator=8,
            profile=self.profile,
            mass_quanta=1,
        )
        self.assertEqual(report.represented_max_depth, 2)
        self.assertEqual(report.status, NO_POSITIVE_FORCE_REPRESENTED)

    def test_current_positive_force_is_sampled_at_tick_zero(self):
        report = force_activation_sampling_report(
            6, 3, 20, self.profile, mass_quanta=1
        )
        self.assertEqual(report.status, ALREADY_ACTIVE)
        self.assertEqual(report.first_positive_sample_tick, 0)
        self.assertEqual(report.first_positive_sample_depth, 3)

    def test_engagement_then_reversal_certificate_chains_without_hidden_substeps(self):
        certificate = engagement_then_reversal_certificate(
            collapse_factor=6,
            current_depth=1,
            inward_lifted_momentum_numerator=20,
            profile=self.profile,
            mass_quanta=2,
            max_impulse_per_tick=2,
        )
        engagement = certificate.engagement
        reversal = certificate.reversal
        self.assertEqual(engagement.status, SAMPLED_AFTER_ZERO_PREFIX)
        self.assertEqual(engagement.first_positive_sample_tick, 1)
        self.assertEqual(engagement.first_positive_sample_depth, 3)
        self.assertEqual(engagement.first_positive_sample_gap, 3)
        self.assertIsNotNone(reversal)
        self.assertEqual(reversal.current_depth, 3)
        self.assertEqual(reversal.primitive_clearance, 3)
        self.assertEqual(reversal.current_loading_sample, 4)
        self.assertEqual(reversal.minimum_impulse_numerator_per_tick, 8)
        self.assertEqual(reversal.comparison_positive_drift_ticks, 2)
        self.assertEqual(reversal.maximum_inward_drift_cells, 1)
        self.assertEqual(reversal.maximum_reached_depth_before_noninward, 4)
        self.assertTrue(reversal.clearance_sufficient)
        self.assertTrue(reversal.material_depth_sufficient)
        self.assertTrue(reversal.guaranteed_precontact_reversal)
        self.assertTrue(certificate.guaranteed_precontact_reversal)

        history = run_impulse_material_world_1d(
            MomentumMaterialState1D(-5, 5),
            Wall1D(0, 0),
            0,
            6,
            self.profile,
            2,
            2,
            ticks=5,
        )
        self.assertIsNone(history.halted_kind)
        self.assertIsNotNone(history.first_reversal_tick)
        first_kick = next(
            transition
            for transition in history.transitions
            if transition.kind == MATERIAL_KICK
        )
        self.assertEqual(first_kick.layer_depth, 3)


if __name__ == "__main__":
    unittest.main()
