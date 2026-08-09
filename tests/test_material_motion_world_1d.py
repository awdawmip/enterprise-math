import unittest

from enterprise_math.material_motion_world_1d import (
    MotionBudgetState1D,
    run_motion_budget_world,
)
from enterprise_math.material_response import material_curve_profile
from enterprise_math.material_collapse_world_1d import ACCEPT, REBOUND, TRANSMIT
from enterprise_math.scale_tunneling_1d import Wall1D


class MaterialMotionWorld1DTests(unittest.TestCase):
    def setUp(self):
        self.wall = Wall1D(0, 0)
        self.profile = material_curve_profile(
            (0, 250, 500, 750, 1000),
            amplitude=1000,
            loading_power=1,
            return_power=1,
            return_retention=1000,
        )

    def test_same_initial_motion_history_diverges_by_spatial_precision(self):
        initial = MotionBudgetState1D(center=-2, signed_motion_budget=4)
        coarse = run_motion_budget_world(
            initial,
            self.wall,
            radius=0,
            collapse_factor=5,
            material_profile=self.profile,
            ticks=3,
        )
        fine = run_motion_budget_world(
            initial,
            self.wall,
            radius=0,
            collapse_factor=2,
            material_profile=self.profile,
            ticks=3,
        )

        self.assertEqual(
            [transition.wall_outcome.kind for transition in coarse.transitions],
            [REBOUND, ACCEPT, ACCEPT],
        )
        self.assertEqual(coarse.transitions[0].wall_outcome.layer_material.layer_depth, 3)
        self.assertEqual(coarse.transitions[0].wall_outcome.rebound.returned_budget, 3)
        self.assertEqual(coarse.transitions[0].after, MotionBudgetState1D(-5, -3))
        self.assertEqual(coarse.final, MotionBudgetState1D(-11, -3))

        self.assertEqual(
            [transition.wall_outcome.kind for transition in fine.transitions],
            [TRANSMIT, ACCEPT, ACCEPT],
        )
        self.assertEqual(fine.transitions[0].after, MotionBudgetState1D(2, 4))
        self.assertEqual(fine.final, MotionBudgetState1D(10, 4))
        self.assertNotEqual(coarse.final, fine.final)

    def test_rebound_replaces_motion_budget_with_opposite_returned_budget(self):
        initial = MotionBudgetState1D(-2, 4)
        history = run_motion_budget_world(
            initial, self.wall, 0, 5, self.profile, ticks=1
        )
        transition = history.transitions[0]
        self.assertEqual(transition.wall_outcome.kind, REBOUND)
        self.assertEqual(transition.after.signed_motion_budget, -3)
        self.assertEqual(history.rebound_count, 1)

    def test_transmission_preserves_signed_motion_budget(self):
        initial = MotionBudgetState1D(-2, 4)
        history = run_motion_budget_world(
            initial, self.wall, 0, 2, self.profile, ticks=1
        )
        transition = history.transitions[0]
        self.assertEqual(transition.wall_outcome.kind, TRANSMIT)
        self.assertEqual(transition.after.signed_motion_budget, 4)
        self.assertEqual(history.transmission_count, 1)

    def test_zero_return_can_stop_motion_at_represented_start(self):
        zero_return = material_curve_profile(
            (0, 250, 500, 750, 1000),
            amplitude=1000,
            loading_power=1,
            return_power=1,
            return_retention=0,
        )
        history = run_motion_budget_world(
            MotionBudgetState1D(-2, 4),
            self.wall,
            0,
            5,
            zero_return,
            ticks=2,
        )
        self.assertEqual(history.transitions[0].wall_outcome.kind, REBOUND)
        self.assertEqual(history.transitions[0].after, MotionBudgetState1D(-2, 0))
        # A zero-budget second tick is just an accepted hold because gap=2 is
        # still coarse contact at d=5, so the coarse-layer helper would rebound
        # with incoming budget zero and remain at the same state.
        self.assertEqual(history.transitions[1].after, MotionBudgetState1D(-2, 0))

    def test_zero_tick_history_is_identity(self):
        initial = MotionBudgetState1D(-10, 3)
        history = run_motion_budget_world(
            initial, self.wall, 0, 2, self.profile, ticks=0
        )
        self.assertEqual(history.final, initial)
        self.assertEqual(history.transitions, ())
        self.assertEqual(history.rebound_count, 0)


if __name__ == "__main__":
    unittest.main()
