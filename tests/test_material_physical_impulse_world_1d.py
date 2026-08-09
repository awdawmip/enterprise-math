import unittest

from enterprise_math.material_hysteresis import LOADING, RETURNING
from enterprise_math.material_physical_impulse_world_1d import (
    CROSSING_TRANSMIT,
    FREE_LIFTED_DRIFT,
    MATERIAL_FORCE_LIFT,
    MATERIAL_ZERO_FORCE,
    PhysicalLiftedMaterialScale1D,
    PhysicalLiftedMaterialState1D,
    physical_lifted_material_step_1d,
)
from enterprise_math.material_physical_projection import (
    ForceImpulseCountScale,
    MomentumDriftCountScale,
)
from enterprise_math.material_response import explicit_material_curve_profile
from enterprise_math.scale_tunneling_1d import Wall1D


def force_scale(tick=1):
    return ForceImpulseCountScale(
        force_scale_factor=1,
        time_scale_factor=1,
        momentum_scale_factor=1,
        tick_duration_count=tick,
        force_unit="N",
        time_unit="s",
        momentum_unit="N*s",
    )


def drift_scale(mass_scale=1, tick=1):
    return MomentumDriftCountScale(
        momentum_scale_factor=1,
        mass_scale_factor=mass_scale,
        time_scale_factor=1,
        position_scale_factor=1,
        tick_duration_count=tick,
        mass_count=1,
        momentum_unit="N*s",
        mass_unit="kg",
        time_unit="s",
        position_unit="m",
    )


class MaterialPhysicalImpulseWorldTests(unittest.TestCase):
    def setUp(self):
        self.wall = Wall1D(0, 0)
        self.profile = explicit_material_curve_profile(
            loading=(0, 2, 4, 4, 4),
            returning=(0, 2, 4, 4, 4),
            amplitude=4,
        )
        self.unit_scale = PhysicalLiftedMaterialScale1D(
            full_scale_force_count=4,
            force_impulse=force_scale(),
            momentum_drift=drift_scale(),
        )

    def test_unit_calibration_reproduces_reference_emergent_reversal(self):
        state = PhysicalLiftedMaterialState1D(-3, 5)
        first = physical_lifted_material_step_1d(
            state, self.wall, 0, 5, self.profile, self.unit_scale
        )
        self.assertEqual(first.kind, MATERIAL_FORCE_LIFT)
        self.assertEqual(first.layer_depth, 2)
        self.assertEqual(first.raw_material_impulse_numerator, -16)
        self.assertEqual(first.momentum_lift_before, 20)
        self.assertEqual(first.momentum_lift_after_force, 4)
        self.assertEqual(first.after.center_count, -2)
        self.assertEqual(first.after.momentum_count, 1)
        self.assertFalse(first.lifted_momentum_reversed)

        second = physical_lifted_material_step_1d(
            first.after, self.wall, 0, 5, self.profile, self.unit_scale
        )
        self.assertEqual(second.momentum_lift_before, 4)
        self.assertEqual(second.momentum_lift_after_force, -12)
        self.assertTrue(second.lifted_momentum_reversed)
        self.assertTrue(second.whole_momentum_reversed)
        self.assertEqual(second.after.center_count, -5)
        self.assertEqual(second.after.momentum_count, -3)
        self.assertEqual(second.after.branch, RETURNING)

    def test_same_state_at_fine_spatial_precision_transmits_without_force(self):
        state = PhysicalLiftedMaterialState1D(-3, 5)
        outcome = physical_lifted_material_step_1d(
            state, self.wall, 0, 2, self.profile, self.unit_scale
        )
        self.assertEqual(outcome.kind, CROSSING_TRANSMIT)
        self.assertIsNone(outcome.response_sample)
        self.assertEqual(outcome.raw_material_impulse_numerator, 0)
        self.assertEqual(outcome.after.center_count, 2)
        self.assertEqual(outcome.after.momentum_count, 5)

    def test_subwhole_momentum_can_drive_position_when_lift_is_consumed(self):
        tiny = explicit_material_curve_profile(
            loading=(0, 1), returning=(0, 1), amplitude=4
        )
        fast_spatial_scale = PhysicalLiftedMaterialScale1D(
            full_scale_force_count=1,
            force_impulse=force_scale(),
            momentum_drift=drift_scale(mass_scale=4),
        )
        initial = PhysicalLiftedMaterialState1D(-1, 0, branch=LOADING)
        retained = physical_lifted_material_step_1d(
            initial,
            self.wall,
            0,
            2,
            tiny,
            fast_spatial_scale,
            retain_momentum_detail=True,
        )
        dropped = physical_lifted_material_step_1d(
            initial,
            self.wall,
            0,
            2,
            tiny,
            fast_spatial_scale,
            retain_momentum_detail=False,
        )
        self.assertEqual(retained.momentum_lift_after_force, -1)
        self.assertEqual(retained.after.momentum_count, 0)
        self.assertEqual(retained.after.momentum_detail_numerator, -1)
        self.assertEqual(retained.displacement_cells, -1)
        self.assertEqual(retained.after.center_count, -2)
        self.assertEqual(retained.after.branch, RETURNING)

        self.assertEqual(dropped.after.momentum_count, 0)
        self.assertEqual(dropped.after.momentum_detail_numerator, 0)
        self.assertEqual(dropped.displacement_cells, 0)
        self.assertEqual(dropped.after.center_count, -1)

    def test_position_detail_accumulates_without_hidden_geometry_sweep(self):
        # Whole momentum is zero but a positive lifted detail produces one quarter
        # position cell per tick under this scale.  Geometry remains at whole cells
        # until the retained position numerator reaches a full cell.
        zero_force = explicit_material_curve_profile(
            loading=(0, 0), returning=(0, 0), amplitude=4
        )
        scale = PhysicalLiftedMaterialScale1D(
            full_scale_force_count=0,
            force_impulse=force_scale(),
            momentum_drift=drift_scale(),
        )
        state = PhysicalLiftedMaterialState1D(
            center_count=-3,
            momentum_count=0,
            branch=LOADING,
            momentum_detail_numerator=1,
        )
        positions = []
        for _ in range(4):
            transition = physical_lifted_material_step_1d(
                state, self.wall, 0, 1, zero_force, scale
            )
            self.assertEqual(transition.kind, FREE_LIFTED_DRIFT)
            state = transition.after
            positions.append((state.center_count, state.position_detail_numerator))
        self.assertEqual(positions, [(-3, 1), (-3, 2), (-3, 3), (-2, 0)])

    def test_zero_material_sample_is_distinct_from_free_outside_layer(self):
        zero = explicit_material_curve_profile(
            loading=(0, 0), returning=(0, 0), amplitude=1
        )
        scale = PhysicalLiftedMaterialScale1D(1, force_scale(), drift_scale())
        inside = physical_lifted_material_step_1d(
            PhysicalLiftedMaterialState1D(-1, 0),
            self.wall,
            0,
            2,
            zero,
            scale,
        )
        outside = physical_lifted_material_step_1d(
            PhysicalLiftedMaterialState1D(-3, 0),
            self.wall,
            0,
            2,
            zero,
            scale,
        )
        self.assertEqual(inside.kind, MATERIAL_ZERO_FORCE)
        self.assertEqual(outside.kind, FREE_LIFTED_DRIFT)

    def test_scale_layers_must_share_time_and_momentum_count_coordinates(self):
        bad_force = ForceImpulseCountScale(
            force_scale_factor=1,
            time_scale_factor=2,
            momentum_scale_factor=1,
            tick_duration_count=1,
            force_unit="N",
            time_unit="s",
            momentum_unit="N*s",
        )
        with self.assertRaises(ValueError):
            PhysicalLiftedMaterialScale1D(1, bad_force, drift_scale())


if __name__ == "__main__":
    unittest.main()
