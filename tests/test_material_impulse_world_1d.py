import unittest

from enterprise_math.material_impulse_world_1d import (
    APPROACHING,
    REBOUND,
    STOPPED,
    MassDriftState1D,
    accumulate_material_impulses,
    apply_material_impulse_to_momentum,
    mass_drift_step,
    material_impulse_quantization,
    momentum_contact_status,
    trace_constant_momentum_drift,
)


class MaterialImpulseWorld1DTests(unittest.TestCase):
    def test_signed_impulse_quantization_reconstructs_raw_numerator(self):
        for amplitude in range(1, 8):
            for response in range(amplitude + 1):
                for scale in range(-5, 6):
                    for detail in range(-(amplitude - 1), amplitude):
                        report = material_impulse_quantization(
                            response, amplitude, scale, detail
                        )
                        self.assertEqual(
                            amplitude * report.impulse_quanta + report.detail_after,
                            report.raw_signed_numerator,
                        )
                        self.assertLess(abs(report.detail_after), amplitude)

    def test_impulse_quantization_is_odd_under_signed_reversal(self):
        for amplitude in range(1, 10):
            for response in range(amplitude + 1):
                for scale in range(1, 6):
                    for detail in range(-(amplitude - 1), amplitude):
                        positive = material_impulse_quantization(
                            response, amplitude, scale, detail
                        )
                        negative = material_impulse_quantization(
                            response, amplitude, -scale, -detail
                        )
                        self.assertEqual(
                            negative.impulse_quanta, -positive.impulse_quanta
                        )
                        self.assertEqual(negative.detail_after, -positive.detail_after)

    def test_retained_subquantum_impulse_can_accumulate_while_dropped_detail_cannot(self):
        retained = accumulate_material_impulses(
            (3, 3, 3, 3), amplitude=10, signed_impulse_scale=2, retain_detail=True
        )
        dropped = accumulate_material_impulses(
            (3, 3, 3, 3), amplitude=10, signed_impulse_scale=2, retain_detail=False
        )
        self.assertEqual(retained.impulse_quanta, (0, 1, 0, 1))
        self.assertEqual(retained.total_impulse_quanta, 2)
        self.assertEqual(retained.final_detail, 4)
        self.assertEqual(dropped.impulse_quanta, (0, 0, 0, 0))
        self.assertEqual(dropped.total_impulse_quanta, 0)
        self.assertEqual(dropped.final_detail, 0)

    def test_rebound_emerges_from_momentum_sign_change_not_reverse_command(self):
        momentum = -1
        detail = 0
        statuses = []
        for _ in range(4):
            step = apply_material_impulse_to_momentum(
                momentum=momentum,
                outward_normal=1,
                response_sample=3,
                amplitude=10,
                impulse_scale_magnitude=2,
                impulse_detail=detail,
            )
            momentum = step.momentum_after
            detail = step.impulse.detail_after
            statuses.append(step.status_after)
        self.assertEqual(statuses, (APPROACHING, STOPPED, STOPPED, REBOUND))
        self.assertEqual(momentum, 1)

        dropped_momentum = -1
        for _ in range(4):
            step = apply_material_impulse_to_momentum(
                momentum=dropped_momentum,
                outward_normal=1,
                response_sample=3,
                amplitude=10,
                impulse_scale_magnitude=2,
                impulse_detail=0,
            )
            dropped_momentum = step.momentum_after
        self.assertEqual(dropped_momentum, -1)
        self.assertEqual(momentum_contact_status(dropped_momentum, 1), APPROACHING)

    def test_mass_drift_retains_exact_signed_remainder(self):
        positive = MassDriftState1D(position=0, momentum=2, mass=3)
        steps = trace_constant_momentum_drift(positive, 5)
        self.assertEqual(steps[-1].after.position, 3)
        self.assertEqual(steps[-1].after.drift_detail, 1)
        self.assertEqual(3 * 3 + 1, 5 * 2)

        negative = MassDriftState1D(position=0, momentum=-2, mass=3)
        negative_steps = trace_constant_momentum_drift(negative, 5)
        self.assertEqual(negative_steps[-1].after.position, -3)
        self.assertEqual(negative_steps[-1].after.drift_detail, -1)

    def test_one_mass_drift_step_has_exact_local_identity(self):
        state = MassDriftState1D(position=7, momentum=-5, mass=3, drift_detail=1)
        report = mass_drift_step(state)
        self.assertEqual(
            state.mass * report.displacement + report.after.drift_detail,
            state.drift_detail + state.momentum,
        )

    def test_contact_status_uses_explicit_outward_normal(self):
        self.assertEqual(momentum_contact_status(-2, 1), APPROACHING)
        self.assertEqual(momentum_contact_status(0, 1), STOPPED)
        self.assertEqual(momentum_contact_status(2, 1), REBOUND)
        self.assertEqual(momentum_contact_status(2, -1), APPROACHING)
        with self.assertRaises(ValueError):
            momentum_contact_status(1, 0)


if __name__ == "__main__":
    unittest.main()
