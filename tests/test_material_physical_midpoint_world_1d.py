import unittest

from enterprise_math.material_physical_impulse_world_1d import (
    PhysicalLiftedMaterialScale1D,
)
from enterprise_math.material_physical_midpoint_world_1d import (
    CROSSING_TRANSMIT,
    FREE_MIDPOINT_DRIFT,
    MATERIAL_MIDPOINT_FORCE,
    PhysicalMidpointMaterialState1D,
    physical_midpoint_material_step_1d,
)
from enterprise_math.material_physical_projection import (
    ForceImpulseCountScale,
    MomentumDriftCountScale,
)
from enterprise_math.material_response import explicit_material_curve_profile
from enterprise_math.scale_tunneling_1d import Wall1D


def scale(*, full_force, tick=1, mass_scale=1):
    return PhysicalLiftedMaterialScale1D(
        full_scale_force_count=full_force,
        force_impulse=ForceImpulseCountScale(
            force_scale_factor=1,
            time_scale_factor=1,
            momentum_scale_factor=1,
            tick_duration_count=tick,
            force_unit="N",
            time_unit="s",
            momentum_unit="N*s",
        ),
        momentum_drift=MomentumDriftCountScale(
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
        ),
    )


class MaterialPhysicalMidpointWorldTests(unittest.TestCase):
    def setUp(self):
        self.wall = Wall1D(0, 0)

    def test_constant_opposing_force_closes_work_and_kinetic_square_exactly(self):
        profile = explicit_material_curve_profile(
            loading=(0, 1), returning=(0, 1), amplitude=1
        )
        state = PhysicalMidpointMaterialState1D(center_count=-10, momentum_count=4)
        outcome = physical_midpoint_material_step_1d(
            state,
            self.wall,
            radius=0,
            collapse_factor=11,
            material_profile=profile,
            scale=scale(full_force=2),
        )
        self.assertEqual(outcome.kind, MATERIAL_MIDPOINT_FORCE)
        self.assertEqual(outcome.raw_impulse_numerator, -2)
        self.assertEqual(outcome.whole_momentum_after, 2)
        self.assertEqual(outcome.displacement_cells, 3)
        self.assertEqual(outcome.after.center_count, -7)
        self.assertEqual(outcome.lifted_square_change, 2 * 2 - 4 * 4)
        self.assertEqual(outcome.impulse_midpoint_work_numerator, -12)
        self.assertEqual(outcome.lifted_square_change, outcome.impulse_midpoint_work_numerator)

    def test_equal_magnitude_reversal_has_zero_midpoint_displacement_and_zero_kinetic_change(self):
        profile = explicit_material_curve_profile(
            loading=(0, 1), returning=(0, 1), amplitude=1
        )
        state = PhysicalMidpointMaterialState1D(center_count=-10, momentum_count=4)
        outcome = physical_midpoint_material_step_1d(
            state,
            self.wall,
            radius=0,
            collapse_factor=11,
            material_profile=profile,
            scale=scale(full_force=8),
        )
        self.assertEqual(outcome.whole_momentum_after, -4)
        self.assertTrue(outcome.lifted_momentum_reversed)
        self.assertEqual(outcome.displacement_cells, 0)
        self.assertEqual(outcome.after.center_count, -10)
        self.assertEqual(outcome.lifted_square_change, 0)
        self.assertEqual(outcome.impulse_midpoint_work_numerator, 0)

    def test_constant_force_full_tick_matches_two_explicit_half_ticks_before_spatial_projection(self):
        profile = explicit_material_curve_profile(
            loading=(0, 1), returning=(0, 1), amplitude=1
        )
        initial = PhysicalMidpointMaterialState1D(center_count=-20, momentum_count=6)
        full = physical_midpoint_material_step_1d(
            initial,
            self.wall,
            radius=0,
            collapse_factor=21,
            material_profile=profile,
            scale=scale(full_force=2, tick=2),
        )
        self.assertEqual(full.raw_impulse_numerator, -4)
        self.assertEqual(full.whole_momentum_after, 2)
        self.assertEqual(full.displacement_cells, 8)

        half_scale = scale(full_force=2, tick=1)
        first = physical_midpoint_material_step_1d(
            initial,
            self.wall,
            0,
            21,
            profile,
            half_scale,
        )
        second = physical_midpoint_material_step_1d(
            first.after,
            self.wall,
            0,
            21,
            profile,
            half_scale,
        )
        self.assertEqual(first.whole_momentum_after, 4)
        self.assertEqual(second.whole_momentum_after, 2)
        self.assertEqual(first.displacement_cells + second.displacement_cells, 8)
        self.assertEqual(second.after.center_count, full.after.center_count)
        self.assertEqual(second.after.momentum_count, full.after.momentum_count)

    def test_free_midpoint_drift_reduces_to_constant_momentum_drift(self):
        profile = explicit_material_curve_profile(
            loading=(0, 0), returning=(0, 0), amplitude=1
        )
        state = PhysicalMidpointMaterialState1D(center_count=-10, momentum_count=3)
        outcome = physical_midpoint_material_step_1d(
            state,
            self.wall,
            0,
            2,
            profile,
            scale(full_force=0),
        )
        self.assertEqual(outcome.kind, FREE_MIDPOINT_DRIFT)
        self.assertEqual(outcome.displacement_cells, 3)
        self.assertEqual(outcome.after.center_count, -7)

    def test_coarse_saved_tick_may_still_cross_without_hidden_path(self):
        profile = explicit_material_curve_profile(
            loading=(0, 0), returning=(0, 0), amplitude=1
        )
        state = PhysicalMidpointMaterialState1D(center_count=-3, momentum_count=6)
        outcome = physical_midpoint_material_step_1d(
            state,
            self.wall,
            0,
            2,
            profile,
            scale(full_force=0),
        )
        self.assertEqual(outcome.kind, CROSSING_TRANSMIT)
        self.assertEqual(outcome.after.center_count, 3)

    def test_position_subcell_detail_accumulates_under_midpoint_projection(self):
        profile = explicit_material_curve_profile(
            loading=(0, 0), returning=(0, 0), amplitude=4
        )
        state = PhysicalMidpointMaterialState1D(
            center_count=-5,
            momentum_count=0,
            momentum_detail_numerator=1,
        )
        small = scale(full_force=0, mass_scale=1)
        positions = []
        for _ in range(4):
            outcome = physical_midpoint_material_step_1d(
                state, self.wall, 0, 1, profile, small
            )
            state = outcome.after
            positions.append((state.center_count, state.midpoint_position_detail_numerator))
        # dp=4, midpoint position divisor=8, raw midpoint numerator=2 each tick.
        self.assertEqual(positions, [(-5, 2), (-5, 4), (-5, 6), (-4, 0)])


if __name__ == "__main__":
    unittest.main()
