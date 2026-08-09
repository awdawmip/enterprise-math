import unittest

from enterprise_math.material_pair_impulse_1d import (
    PAIR_CLOSING,
    PAIR_COMOVING,
    PAIR_SEPARATING,
    PairMomentumState1D,
    apply_pair_material_impulse,
    constant_pair_response_thresholds,
    pair_motion_status,
    pair_relative_motion_numerator,
    trace_pair_material_impulses,
)


class MaterialPairImpulse1DTests(unittest.TestCase):
    def test_relative_motion_numerator_is_division_free_velocity_sign(self):
        closing = PairMomentumState1D(
            left_momentum=1,
            right_momentum=-1,
            left_mass=1,
            right_mass=1,
        )
        self.assertEqual(pair_relative_motion_numerator(closing), -2)
        self.assertEqual(pair_motion_status(closing), PAIR_CLOSING)

        comoving = PairMomentumState1D(
            left_momentum=2,
            right_momentum=3,
            left_mass=2,
            right_mass=3,
        )
        self.assertEqual(pair_relative_motion_numerator(comoving), 0)
        self.assertEqual(pair_motion_status(comoving), PAIR_COMOVING)

        separating = PairMomentumState1D(
            left_momentum=-1,
            right_momentum=2,
            left_mass=2,
            right_mass=3,
        )
        self.assertGreater(pair_relative_motion_numerator(separating), 0)
        self.assertEqual(pair_motion_status(separating), PAIR_SEPARATING)

    def test_equal_opposite_impulse_preserves_total_momentum_and_has_exact_relative_update(self):
        for left_mass in range(1, 5):
            for right_mass in range(1, 5):
                for left_momentum in range(-4, 5):
                    for right_momentum in range(-4, 5):
                        for normal in (-1, 1):
                            for amplitude in range(1, 5):
                                for response in range(amplitude + 1):
                                    for scale in range(1, 4):
                                        for detail in range(amplitude):
                                            state = PairMomentumState1D(
                                                left_momentum=left_momentum,
                                                right_momentum=right_momentum,
                                                left_mass=left_mass,
                                                right_mass=right_mass,
                                                contact_normal=normal,
                                                contact_impulse_detail=detail,
                                            )
                                            step = apply_pair_material_impulse(
                                                state,
                                                response,
                                                amplitude,
                                                scale,
                                            )
                                            self.assertEqual(
                                                step.after.total_momentum,
                                                state.total_momentum,
                                            )
                                            self.assertEqual(
                                                step.relative_numerator_after,
                                                step.relative_numerator_before
                                                + state.mass_sum
                                                * step.delivered_impulse_quanta,
                                            )
                                            self.assertGreaterEqual(
                                                step.delivered_impulse_quanta,
                                                0,
                                            )
                                            self.assertGreaterEqual(
                                                step.contact_detail_after,
                                                0,
                                            )
                                            self.assertLess(
                                                step.contact_detail_after,
                                                amplitude,
                                            )

    def test_head_on_equal_mass_pair_moves_closing_to_comoving_to_separating(self):
        initial = PairMomentumState1D(1, -1, 1, 1)
        first = apply_pair_material_impulse(initial, 1, 1, 1)
        self.assertEqual(first.status_before, PAIR_CLOSING)
        self.assertEqual(first.status_after, PAIR_COMOVING)
        self.assertEqual(first.after.left_momentum, 0)
        self.assertEqual(first.after.right_momentum, 0)
        self.assertEqual(first.after.total_momentum, 0)

        second = apply_pair_material_impulse(first.after, 1, 1, 1)
        self.assertEqual(second.status_after, PAIR_SEPARATING)
        self.assertEqual(second.after.left_momentum, -1)
        self.assertEqual(second.after.right_momentum, 1)
        self.assertEqual(second.after.total_momentum, 0)

    def test_retained_subquantum_contact_detail_can_separate_pair_while_dropped_detail_cannot(self):
        initial = PairMomentumState1D(1, -1, 1, 1)
        retained = trace_pair_material_impulses(
            initial,
            (3, 3, 3, 3),
            amplitude=10,
            impulse_scale_magnitude=2,
            retain_contact_detail=True,
        )
        dropped = trace_pair_material_impulses(
            initial,
            (3, 3, 3, 3),
            amplitude=10,
            impulse_scale_magnitude=2,
            retain_contact_detail=False,
        )
        self.assertEqual(retained.total_delivered_impulse_quanta, 2)
        self.assertEqual(retained.final.contact_impulse_detail, 4)
        self.assertEqual(pair_motion_status(retained.final), PAIR_SEPARATING)
        self.assertEqual(retained.final.total_momentum, initial.total_momentum)

        self.assertEqual(dropped.total_delivered_impulse_quanta, 0)
        self.assertEqual(dropped.final.contact_impulse_detail, 0)
        self.assertEqual(pair_motion_status(dropped.final), PAIR_CLOSING)
        self.assertEqual(dropped.final.total_momentum, initial.total_momentum)

    def test_closed_form_thresholds_match_direct_retained_and_dropped_traces(self):
        for left_mass in range(1, 4):
            for right_mass in range(1, 4):
                for left_momentum in range(-3, 4):
                    for right_momentum in range(-3, 4):
                        initial = PairMomentumState1D(
                            left_momentum,
                            right_momentum,
                            left_mass,
                            right_mass,
                        )
                        if pair_motion_status(initial) != PAIR_CLOSING:
                            continue
                        for amplitude in range(1, 6):
                            for response in range(amplitude + 1):
                                for scale in range(1, 4):
                                    thresholds = constant_pair_response_thresholds(
                                        initial,
                                        amplitude,
                                        response,
                                        scale,
                                    )
                                    for retain, nonclosing, separating in (
                                        (
                                            True,
                                            thresholds.retained_first_nonclosing_event,
                                            thresholds.retained_first_separating_event,
                                        ),
                                        (
                                            False,
                                            thresholds.dropped_first_nonclosing_event,
                                            thresholds.dropped_first_separating_event,
                                        ),
                                    ):
                                        if response == 0 or nonclosing is None:
                                            self.assertIsNone(nonclosing)
                                            self.assertIsNone(separating)
                                            continue

                                        nonclosing_trace = trace_pair_material_impulses(
                                            initial,
                                            (response,) * nonclosing,
                                            amplitude,
                                            scale,
                                            retain,
                                        )
                                        self.assertGreaterEqual(
                                            pair_relative_motion_numerator(
                                                nonclosing_trace.final
                                            ),
                                            0,
                                        )
                                        if nonclosing > 0:
                                            before = trace_pair_material_impulses(
                                                initial,
                                                (response,) * (nonclosing - 1),
                                                amplitude,
                                                scale,
                                                retain,
                                            )
                                            self.assertLess(
                                                pair_relative_motion_numerator(
                                                    before.final
                                                ),
                                                0,
                                            )

                                        separating_trace = trace_pair_material_impulses(
                                            initial,
                                            (response,) * separating,
                                            amplitude,
                                            scale,
                                            retain,
                                        )
                                        self.assertGreater(
                                            pair_relative_motion_numerator(
                                                separating_trace.final
                                            ),
                                            0,
                                        )
                                        if separating > 0:
                                            before = trace_pair_material_impulses(
                                                initial,
                                                (response,) * (separating - 1),
                                                amplitude,
                                                scale,
                                                retain,
                                            )
                                            self.assertLessEqual(
                                                pair_relative_motion_numerator(
                                                    before.final
                                                ),
                                                0,
                                            )

    def test_normal_reversal_with_swapped_bodies_preserves_physical_status(self):
        original = PairMomentumState1D(
            left_momentum=3,
            right_momentum=-2,
            left_mass=2,
            right_mass=3,
            contact_normal=1,
        )
        swapped = PairMomentumState1D(
            left_momentum=-2,
            right_momentum=3,
            left_mass=3,
            right_mass=2,
            contact_normal=-1,
        )
        self.assertEqual(
            pair_relative_motion_numerator(original),
            pair_relative_motion_numerator(swapped),
        )
        self.assertEqual(pair_motion_status(original), pair_motion_status(swapped))
        original_step = apply_pair_material_impulse(original, 2, 5, 3)
        swapped_step = apply_pair_material_impulse(swapped, 2, 5, 3)
        self.assertEqual(
            original_step.relative_numerator_after,
            swapped_step.relative_numerator_after,
        )
        self.assertEqual(original_step.after.total_momentum, swapped_step.after.total_momentum)

    def test_contact_reservoir_contract_rejects_cross_channel_style_details(self):
        with self.assertRaises(ValueError):
            PairMomentumState1D(0, 0, 1, 1, contact_impulse_detail=-1)
        oversized = PairMomentumState1D(0, 0, 1, 1, contact_impulse_detail=10)
        with self.assertRaises(ValueError):
            apply_pair_material_impulse(oversized, 0, amplitude=10, impulse_scale_magnitude=1)
        with self.assertRaises(ValueError):
            PairMomentumState1D(0, 0, 0, 1)
        with self.assertRaises(ValueError):
            PairMomentumState1D(0, 0, 1, 1, contact_normal=0)


if __name__ == "__main__":
    unittest.main()
