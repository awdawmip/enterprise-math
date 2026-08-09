import unittest

from enterprise_math.material_collapse_world_1d import (
    ACCEPT,
    REBOUND,
    TRANSMIT,
    collapse_material_wall_step,
)
from enterprise_math.material_response import material_curve_profile
from enterprise_math.scale_tunneling_1d import Wall1D


class MaterialCollapseWorld1DTests(unittest.TestCase):
    def setUp(self):
        self.wall = Wall1D(0, 0)
        self.profile = material_curve_profile(
            (0, 200, 400, 600, 800, 1000),
            amplitude=1000,
            loading_power=2,
            return_power=1,
            return_retention=500,
        )

    def test_same_jump_changes_rebound_depth_then_transmits_under_refinement(self):
        # start/end gaps both 2; incoming budget is 4.
        outcomes = [
            collapse_material_wall_step(
                self.wall, -2, 2, 0, factor, self.profile
            )
            for factor in (6, 5, 4, 3, 2, 1)
        ]
        self.assertEqual(
            [outcome.kind for outcome in outcomes],
            [REBOUND, REBOUND, REBOUND, REBOUND, TRANSMIT, TRANSMIT],
        )
        self.assertEqual(
            [
                None if outcome.layer_material is None else outcome.layer_material.layer_depth
                for outcome in outcomes
            ],
            [4, 3, 2, 1, None, None],
        )
        # Return branch samples at depths 4,3,2,1 are 400,300,200,100.
        self.assertEqual(
            [None if outcome.rebound is None else outcome.rebound.returned_budget for outcome in outcomes],
            [1, 1, 0, 0, None, None],
        )
        self.assertEqual(outcomes[-1].after_center, 2)

    def test_coarser_factor_can_create_deeper_material_layer_and_stronger_rebound(self):
        # A full-return linear curve makes the layer-depth effect transparent.
        profile = material_curve_profile(
            (0, 200, 400, 600, 800, 1000),
            amplitude=1000,
            loading_power=1,
            return_power=1,
            return_retention=1000,
        )
        d6 = collapse_material_wall_step(self.wall, -2, 2, 0, 6, profile)
        d3 = collapse_material_wall_step(self.wall, -2, 2, 0, 3, profile)
        self.assertEqual(d6.layer_material.layer_depth, 4)
        self.assertEqual(d3.layer_material.layer_depth, 1)
        self.assertEqual(d6.layer_material.material_state.response_sample, 800)
        self.assertEqual(d3.layer_material.material_state.response_sample, 200)
        self.assertEqual(d6.rebound.returned_budget, 3)
        self.assertEqual(d3.rebound.returned_budget, 0)
        self.assertLess(d6.after_center, d3.after_center)

    def test_resolved_same_side_move_is_plain_accept(self):
        outcome = collapse_material_wall_step(
            self.wall, -5, -4, 0, 2, self.profile
        )
        self.assertEqual(outcome.kind, ACCEPT)
        self.assertEqual(outcome.after_center, -4)
        self.assertIsNone(outcome.layer_material)

    def test_primitive_endpoint_contact_is_outside_coarse_layer_helper(self):
        with self.assertRaises(ValueError):
            collapse_material_wall_step(
                self.wall, -2, 0, 0, 5, self.profile
            )

    def test_material_domain_must_cover_generated_layer_depth(self):
        short = material_curve_profile(
            (0, 100),
            amplitude=100,
            loading_power=1,
            return_power=1,
        )
        with self.assertRaises(ValueError):
            collapse_material_wall_step(self.wall, -2, 2, 0, 6, short)


if __name__ == "__main__":
    unittest.main()
