import unittest

from enterprise_math.material_impulse_tick_order import (
    DRIFT_THEN_IMPULSE,
    IMPULSE_THEN_DRIFT,
    ImpulseDriftTickState1D,
)
from enterprise_math.material_impulse_wall_world_1d import (
    DRIFT,
    LEFT,
    MATERIAL_INTERACTION,
    MATERIAL_UNDERRESOLVED,
    PRIMITIVE_CONTACT,
    RIGHT,
    TRANSMIT,
    MaterialImpulseWallState1D,
    material_impulse_wall_tick,
)
from enterprise_math.material_impulse_world_1d import (
    APPROACHING,
    OUTWARD,
    MassDriftState1D,
)
from enterprise_math.material_response import explicit_material_curve_profile
from enterprise_math.scale_tunneling_1d import Wall1D


def profile(loading, returning=None, amplitude=10):
    if returning is None:
        returning = loading
    return explicit_material_curve_profile(loading, returning, amplitude)


def body(center, momentum, mass=1, radius=0, drift_detail=0, impulse_detail=0):
    return MaterialImpulseWallState1D(
        motion=ImpulseDriftTickState1D(
            motion=MassDriftState1D(
                position=center,
                momentum=momentum,
                mass=mass,
                drift_detail=drift_detail,
            ),
            impulse_detail=impulse_detail,
        ),
        radius=radius,
    )


class MaterialImpulseWallWorld1DTests(unittest.TestCase):
    def test_same_state_coarse_turns_outward_while_fine_transmits(self):
        wall = Wall1D(0, 0)
        material = profile((0, 10), amplitude=10)
        initial = body(center=-2, momentum=4)

        coarse = material_impulse_wall_tick(
            initial,
            wall,
            collapse_factor=3,
            profile=material,
            impulse_scale_magnitude=5,
            tick_order=IMPULSE_THEN_DRIFT,
        )
        fine = material_impulse_wall_tick(
            initial,
            wall,
            collapse_factor=2,
            profile=material,
            impulse_scale_magnitude=5,
            tick_order=IMPULSE_THEN_DRIFT,
        )

        self.assertEqual(coarse.kind, MATERIAL_INTERACTION)
        self.assertEqual(coarse.start_side, LEFT)
        self.assertEqual(coarse.start_clearance, 2)
        self.assertEqual(coarse.layer_depth, 1)
        self.assertEqual(coarse.material_response_sample, 10)
        self.assertEqual(coarse.tick.impulse.impulse_quanta, -5)
        self.assertEqual(coarse.after.center, -3)
        self.assertEqual(coarse.after.motion.motion.momentum, -1)
        self.assertEqual(coarse.end_side, LEFT)
        self.assertEqual(coarse.end_momentum_status, OUTWARD)
        self.assertFalse(coarse.crossed_between_separated_sides)

        self.assertEqual(fine.kind, TRANSMIT)
        self.assertFalse(fine.macro_contact)
        self.assertIsNone(fine.material_response_sample)
        self.assertEqual(fine.after.center, 2)
        self.assertEqual(fine.after.motion.motion.momentum, 4)
        self.assertEqual(fine.end_side, RIGHT)
        self.assertEqual(fine.end_momentum_status, OUTWARD)
        self.assertTrue(fine.crossed_between_separated_sides)

    def test_tick_order_can_change_outward_turn_versus_transmit_at_same_coarse_scale(self):
        wall = Wall1D(0, 0)
        material = profile((0, 10), amplitude=10)
        initial = body(center=-2, momentum=4)

        impulse_first = material_impulse_wall_tick(
            initial, wall, 3, material, 5, IMPULSE_THEN_DRIFT
        )
        drift_first = material_impulse_wall_tick(
            initial, wall, 3, material, 5, DRIFT_THEN_IMPULSE
        )
        self.assertEqual(impulse_first.kind, MATERIAL_INTERACTION)
        self.assertFalse(impulse_first.crossed_between_separated_sides)
        self.assertEqual(impulse_first.after.center, -3)
        self.assertEqual(impulse_first.after.motion.motion.momentum, -1)
        self.assertEqual(impulse_first.end_momentum_status, OUTWARD)

        self.assertEqual(drift_first.kind, TRANSMIT)
        self.assertTrue(drift_first.crossed_between_separated_sides)
        self.assertEqual(drift_first.after.center, 2)
        self.assertEqual(drift_first.after.motion.motion.momentum, -1)
        self.assertEqual(drift_first.end_side, RIGHT)
        self.assertEqual(drift_first.end_momentum_status, APPROACHING)

    def test_macro_contact_with_zero_material_response_can_still_transmit(self):
        wall = Wall1D(0, 0)
        zero_material = profile((0, 0), amplitude=10)
        report = material_impulse_wall_tick(
            body(-2, 4),
            wall,
            3,
            zero_material,
            5,
            IMPULSE_THEN_DRIFT,
        )
        self.assertTrue(report.macro_contact)
        self.assertEqual(report.material_response_sample, 0)
        self.assertEqual(report.tick.impulse.impulse_quanta, 0)
        self.assertEqual(report.kind, TRANSMIT)
        self.assertEqual(report.after.center, 2)

    def test_retreat_inside_coarse_layer_does_not_request_new_loading_impulse(self):
        wall = Wall1D(0, 0)
        material = profile((0, 10), amplitude=10)
        report = material_impulse_wall_tick(
            body(-2, -1),
            wall,
            3,
            material,
            5,
            IMPULSE_THEN_DRIFT,
        )
        self.assertTrue(report.macro_contact)
        self.assertFalse(report.approaching)
        self.assertIsNone(report.material_response_sample)
        self.assertEqual(report.tick.impulse.impulse_quanta, 0)
        self.assertEqual(report.kind, DRIFT)
        self.assertEqual(report.after.center, -3)

    def test_unrepresented_requested_depth_stops_without_fabricated_after_state(self):
        wall = Wall1D(0, 0)
        shallow = profile((0,), amplitude=10)
        report = material_impulse_wall_tick(
            body(-2, 4),
            wall,
            3,
            shallow,
            5,
            IMPULSE_THEN_DRIFT,
        )
        self.assertEqual(report.kind, MATERIAL_UNDERRESOLVED)
        self.assertEqual(report.layer_depth, 1)
        self.assertIsNone(report.after)
        self.assertIsNone(report.tick)

    def test_primitive_contact_is_delegated_without_inventing_side_normal(self):
        wall = Wall1D(0, 0)
        material = profile((0, 10), amplitude=10)
        report = material_impulse_wall_tick(
            body(-1, 2, radius=1),
            wall,
            3,
            material,
            5,
            IMPULSE_THEN_DRIFT,
        )
        self.assertEqual(report.start_clearance, 0)
        self.assertEqual(report.kind, PRIMITIVE_CONTACT)
        self.assertIsNone(report.outward_normal)
        self.assertIsNone(report.after)


if __name__ == "__main__":
    unittest.main()
