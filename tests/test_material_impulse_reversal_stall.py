import unittest

from enterprise_math.material_hysteresis import LOADING
from enterprise_math.material_impulse_world_1d import (
    MomentumMaterialState1D,
    run_impulse_material_world_1d,
)
from enterprise_math.material_response import explicit_material_curve_profile
from enterprise_math.scale_tunneling_1d import Wall1D


class MaterialImpulseReversalStallTests(unittest.TestCase):
    def test_stall_then_outward_onset_is_recorded_as_reversal_completion(self):
        # Every tick contributes only one quarter of a whole outward impulse.
        # Whole momentum stalls at zero first; retained detail then keeps
        # accumulating until a nonzero outward momentum quantum appears.
        profile = explicit_material_curve_profile(
            loading=(0, 1),
            returning=(0, 1),
            amplitude=4,
        )
        history = run_impulse_material_world_1d(
            MomentumMaterialState1D(-1, 0, branch=LOADING),
            Wall1D(0, 0),
            radius=0,
            collapse_factor=2,
            material_profile=profile,
            mass_quanta=1,
            max_impulse_per_tick=1,
            ticks=4,
            retain_impulse_detail=True,
        )
        self.assertEqual(
            [transition.after.momentum_quanta for transition in history.transitions],
            [0, 0, 0, -1],
        )
        self.assertEqual(history.first_reversal_tick, 3)
        self.assertTrue(history.transitions[3].momentum_reversed)
        self.assertEqual(history.final.center, -2)

    def test_without_retained_detail_same_subquantum_force_never_reverses(self):
        profile = explicit_material_curve_profile(
            loading=(0, 1),
            returning=(0, 1),
            amplitude=4,
        )
        history = run_impulse_material_world_1d(
            MomentumMaterialState1D(-1, 0, branch=LOADING),
            Wall1D(0, 0),
            radius=0,
            collapse_factor=2,
            material_profile=profile,
            mass_quanta=1,
            max_impulse_per_tick=1,
            ticks=8,
            retain_impulse_detail=False,
        )
        self.assertIsNone(history.first_reversal_tick)
        self.assertEqual(history.final.center, -1)
        self.assertEqual(history.final.momentum_quanta, 0)


if __name__ == "__main__":
    unittest.main()
