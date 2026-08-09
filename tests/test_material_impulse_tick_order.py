import unittest

from enterprise_math.material_impulse_tick_order import (
    DRIFT_THEN_IMPULSE,
    IMPULSE_THEN_DRIFT,
    ImpulseDriftTickState1D,
    compare_impulse_drift_orders,
    material_impulse_drift_tick,
)
from enterprise_math.material_impulse_world_1d import MassDriftState1D


class MaterialImpulseTickOrderTests(unittest.TestCase):
    def test_tick_order_can_change_immediate_position_with_same_final_momentum(self):
        state = ImpulseDriftTickState1D(
            MassDriftState1D(position=0, momentum=2, mass=3)
        )
        report = compare_impulse_drift_orders(
            state,
            outward_normal=1,
            response_sample=1,
            amplitude=1,
            impulse_scale_magnitude=1,
        )
        self.assertEqual(report.impulse_quantum, 1)
        self.assertEqual(report.impulse_then_drift.after.motion.momentum, 3)
        self.assertEqual(report.drift_then_impulse.after.motion.momentum, 3)
        self.assertEqual(report.impulse_then_drift.after.motion.position, 1)
        self.assertEqual(report.drift_then_impulse.after.motion.position, 0)
        self.assertEqual(report.displacement_difference, 1)
        self.assertEqual(report.drift_detail_difference, -2)
        self.assertEqual(3 * 1 - 2, 1)

    def test_same_immediate_position_can_hide_order_in_drift_detail(self):
        state = ImpulseDriftTickState1D(
            MassDriftState1D(position=0, momentum=-1, mass=3)
        )
        report = compare_impulse_drift_orders(
            state,
            outward_normal=1,
            response_sample=1,
            amplitude=1,
            impulse_scale_magnitude=2,
        )
        self.assertEqual(report.impulse_quantum, 2)
        self.assertEqual(report.impulse_then_drift.after.motion.position, 0)
        self.assertEqual(report.drift_then_impulse.after.motion.position, 0)
        self.assertEqual(report.impulse_then_drift.after.motion.momentum, 1)
        self.assertEqual(report.drift_then_impulse.after.motion.momentum, 1)
        self.assertEqual(report.impulse_then_drift.after.motion.drift_detail, 1)
        self.assertEqual(report.drift_then_impulse.after.motion.drift_detail, -1)
        self.assertEqual(report.drift_detail_difference, 2)

    def test_order_defect_identity_holds_on_small_integer_domain(self):
        for mass in range(1, 6):
            for momentum in range(-5, 6):
                for drift_detail in range(-(mass - 1), mass):
                    state = ImpulseDriftTickState1D(
                        MassDriftState1D(
                            position=7,
                            momentum=momentum,
                            mass=mass,
                            drift_detail=drift_detail,
                        )
                    )
                    for outward_normal in (-1, 1):
                        for response in range(4):
                            for scale in range(1, 4):
                                report = compare_impulse_drift_orders(
                                    state,
                                    outward_normal,
                                    response,
                                    amplitude=3,
                                    impulse_scale_magnitude=scale,
                                )
                                self.assertEqual(
                                    mass * report.displacement_difference
                                    + report.drift_detail_difference,
                                    report.impulse_quantum,
                                )
                                self.assertEqual(
                                    report.impulse_then_drift.after.motion.momentum,
                                    report.drift_then_impulse.after.motion.momentum,
                                )

    def test_zero_impulse_makes_both_orders_identical(self):
        state = ImpulseDriftTickState1D(
            MassDriftState1D(position=3, momentum=-4, mass=5, drift_detail=2)
        )
        report = compare_impulse_drift_orders(
            state, 1, response_sample=0, amplitude=5, impulse_scale_magnitude=3
        )
        self.assertEqual(report.impulse_quantum, 0)
        self.assertEqual(
            report.impulse_then_drift.after,
            report.drift_then_impulse.after,
        )

    def test_unknown_tick_order_is_rejected(self):
        state = ImpulseDriftTickState1D(
            MassDriftState1D(position=0, momentum=0, mass=1)
        )
        with self.assertRaises(ValueError):
            material_impulse_drift_tick(
                state, 1, 1, 1, 1, "UNKNOWN"
            )

    def test_named_orders_are_distinct_policies(self):
        self.assertNotEqual(IMPULSE_THEN_DRIFT, DRIFT_THEN_IMPULSE)


if __name__ == "__main__":
    unittest.main()
