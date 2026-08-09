import unittest

from enterprise_math.material_collapse_layer import (
    BOTH,
    END,
    sampled_wall_layer_material,
)
from enterprise_math.material_hysteresis import RETURNING
from enterprise_math.material_response import material_curve_profile
from enterprise_math.scale_tunneling_1d import Wall1D


class MaterialCollapseLayerTests(unittest.TestCase):
    def setUp(self):
        self.wall = Wall1D(0, 0)
        self.profile = material_curve_profile(
            (0, 200, 400, 600, 800, 1000),
            amplitude=1000,
            loading_power=2,
            return_power=1,
            return_retention=500,
        )

    def test_symmetric_coarse_contact_maps_gap_to_canonical_layer_depth(self):
        # start=-2, end=2 around point wall: both primitive clearances are 2.
        # d=5 gives kappa=3, so returning sample is branch index 3 = 300.
        observation = sampled_wall_layer_material(
            self.wall, -2, 2, 0, 5, self.profile, RETURNING
        )
        self.assertIsNotNone(observation)
        self.assertEqual(observation.controlling_clearance, 2)
        self.assertEqual(observation.layer_depth, 3)
        self.assertEqual(observation.trigger_sample, BOTH)
        self.assertEqual(observation.material_state.response_sample, 300)

    def test_refinement_reduces_layer_depth_then_extinguishes_material_entry(self):
        depths = []
        for factor in (6, 5, 4, 3, 2, 1):
            observation = sampled_wall_layer_material(
                self.wall, -2, 2, 0, factor, self.profile, RETURNING
            )
            depths.append(None if observation is None else observation.layer_depth)
        self.assertEqual(depths, [4, 3, 2, 1, None, None])

    def test_nearer_end_sample_controls_asymmetric_coarse_contact(self):
        observation = sampled_wall_layer_material(
            self.wall, -5, -2, 0, 4, self.profile, RETURNING
        )
        self.assertIsNotNone(observation)
        self.assertEqual(observation.start_clearance, 5)
        self.assertEqual(observation.end_clearance, 2)
        self.assertEqual(observation.controlling_clearance, 2)
        self.assertEqual(observation.layer_depth, 2)
        self.assertEqual(observation.trigger_sample, END)

    def test_resolved_positive_gaps_do_not_enter_material_layer(self):
        observation = sampled_wall_layer_material(
            self.wall, -2, 2, 0, 2, self.profile, RETURNING
        )
        self.assertIsNone(observation)

    def test_primitive_overlap_is_rejected_from_coarse_layer_semantics(self):
        with self.assertRaises(ValueError):
            sampled_wall_layer_material(
                self.wall, -2, 0, 0, 5, self.profile, RETURNING
            )

    def test_unrepresented_layer_depth_is_rejected(self):
        short = material_curve_profile(
            (0, 100),
            amplitude=100,
            loading_power=1,
            return_power=1,
        )
        with self.assertRaises(ValueError):
            sampled_wall_layer_material(
                self.wall, -2, 2, 0, 5, short, RETURNING
            )


if __name__ == "__main__":
    unittest.main()
