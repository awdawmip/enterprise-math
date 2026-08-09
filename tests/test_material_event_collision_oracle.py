import unittest

from enterprise_math.material_event_collision_oracle import (
    EXACT_MATERIAL_BOUNCE,
    MATERIAL_DEPTH_EXHAUSTED,
    NO_POSITIVE_INTERACTION_LAYER,
    SPATIAL_AND_MATERIAL_EXHAUSTED,
    SPATIAL_LAYER_EXHAUSTED,
    TURN_UNDERRESOLVED,
    material_event_collision_report,
)
from enterprise_math.material_force_work import uniform_force_law
from enterprise_math.material_response import explicit_material_curve_profile
from enterprise_math.material_turn_return_witness import RETURN_MOMENTUM_UNDERRESOLVED


class MaterialEventCollisionOracleTests(unittest.TestCase):
    def test_hooke_integer_momentum_turns_exactly_when_spatial_layer_is_deep_enough(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=tuple(k for k in range(9)),
                returning=tuple(k for k in range(9)),
                amplitude=8,
            )
        )
        for momentum in range(1, 8):
            insufficient = material_event_collision_report(
                law, collapse_factor=momentum, incoming_momentum=momentum
            )
            self.assertEqual(insufficient.status, SPATIAL_LAYER_EXHAUSTED)
            sufficient = material_event_collision_report(
                law, collapse_factor=momentum + 1, incoming_momentum=momentum
            )
            self.assertEqual(sufficient.status, EXACT_MATERIAL_BOUNCE)
            self.assertEqual(sufficient.exact_turn_depth, momentum)
            self.assertEqual(sufficient.outgoing_momentum, momentum)

    def test_square_slope_b_requires_momentum_multiple_of_b_for_exact_current_grid_turn(self):
        b = 3
        a = 2
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=tuple(b * b * k for k in range(10)),
                returning=tuple(a * a * k for k in range(10)),
                amplitude=b * b * 9,
            )
        )
        for depth in range(1, 9):
            exact = material_event_collision_report(
                law,
                collapse_factor=depth + 1,
                incoming_momentum=b * depth,
            )
            self.assertEqual(exact.status, EXACT_MATERIAL_BOUNCE)
            self.assertEqual(exact.exact_turn_depth, depth)
            self.assertEqual(exact.outgoing_momentum, a * depth)

        # p=4 lies between work squares (3*1)^2=9 and (3*2)^2=36.
        under = material_event_collision_report(law, collapse_factor=4, incoming_momentum=4)
        self.assertEqual(under.status, TURN_UNDERRESOLVED)
        self.assertEqual((under.lower_turn_depth, under.upper_turn_depth), (1, 2))

    def test_spatial_capacity_and_material_capacity_are_distinguished(self):
        long_law = uniform_force_law(
            explicit_material_curve_profile(
                loading=tuple(k for k in range(11)),
                returning=tuple(k for k in range(11)),
                amplitude=10,
            )
        )
        spatial = material_event_collision_report(long_law, 3, 5)
        self.assertEqual(spatial.status, SPATIAL_LAYER_EXHAUSTED)

        short_law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1, 2), returning=(0, 1, 2), amplitude=2
            )
        )
        material = material_event_collision_report(short_law, 10, 5)
        self.assertEqual(material.status, MATERIAL_DEPTH_EXHAUSTED)

        both = material_event_collision_report(short_law, 3, 5)
        self.assertEqual(both.status, SPATIAL_AND_MATERIAL_EXHAUSTED)

    def test_d_equal_one_has_no_positive_gap_material_capacity(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1, 2), returning=(0, 1, 2), amplitude=2
            )
        )
        report = material_event_collision_report(law, 1, 1)
        self.assertEqual(report.status, NO_POSITIVE_INTERACTION_LAYER)
        self.assertEqual(report.represented_max_depth, 0)

    def test_exact_loading_turn_can_still_fail_return_momentum_language(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 4), returning=(0, 2), amplitude=4
            )
        )
        report = material_event_collision_report(law, 2, 2)
        self.assertEqual(report.exact_turn_depth, 1)
        self.assertEqual(report.status, RETURN_MOMENTUM_UNDERRESOLVED)
        self.assertIsNone(report.outgoing_momentum)

    def test_increasing_spatial_precision_capacity_can_change_exhausted_to_exact_bounce(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=tuple(k for k in range(8)),
                returning=tuple(k for k in range(8)),
                amplitude=7,
            )
        )
        momentum = 5
        statuses = [
            material_event_collision_report(law, d, momentum).status
            for d in range(1, 7)
        ]
        self.assertEqual(statuses[-1], EXACT_MATERIAL_BOUNCE)
        self.assertIn(SPATIAL_LAYER_EXHAUSTED, statuses[:-1])

    def test_invalid_inputs_are_rejected(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1), returning=(0, 1), amplitude=1
            )
        )
        with self.assertRaises(ValueError):
            material_event_collision_report(law, 0, 1)
        with self.assertRaises(ValueError):
            material_event_collision_report(law, 2, 0)


if __name__ == "__main__":
    unittest.main()
