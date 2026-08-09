import unittest

from enterprise_math.material_hysteresis import MaterialHistoryState, RETURNING
from enterprise_math.material_world_1d import (
    ACCEPT,
    REBOUND,
    TRANSMIT,
    material_wall_step,
)
from enterprise_math.scale_tunneling_1d import Wall1D


class MaterialWorld1DTests(unittest.TestCase):
    def setUp(self):
        self.wall = Wall1D(0, 0)
        self.half_return = MaterialHistoryState(
            deformation_index=1,
            branch=RETURNING,
            response_sample=500,
        )
        self.full_return = MaterialHistoryState(
            deformation_index=1,
            branch=RETURNING,
            response_sample=1000,
        )

    def test_same_jump_rebounds_coarse_and_transmits_fine(self):
        # Point body: start/end clearances are both 2.  d=3 collapses them to
        # macro contact, while d=2 resolves both and accepts the same long jump.
        coarse = material_wall_step(
            self.wall,
            start_center=-2,
            proposed_end_center=2,
            radius=0,
            collapse_factor=3,
            material_state=self.half_return,
            material_amplitude=1000,
        )
        fine = material_wall_step(
            self.wall,
            start_center=-2,
            proposed_end_center=2,
            radius=0,
            collapse_factor=2,
            material_state=self.half_return,
            material_amplitude=1000,
        )
        self.assertEqual(coarse.kind, REBOUND)
        self.assertEqual(coarse.incoming_budget, 4)
        self.assertEqual(coarse.rebound.returned_budget, 2)
        self.assertEqual(coarse.after_center, -4)
        self.assertEqual(fine.kind, TRANSMIT)
        self.assertEqual(fine.after_center, 2)
        self.assertIsNone(fine.rebound)

    def test_full_return_reverses_full_incoming_budget_from_start(self):
        outcome = material_wall_step(
            self.wall,
            -2,
            2,
            0,
            3,
            self.full_return,
            1000,
        )
        self.assertEqual(outcome.kind, REBOUND)
        self.assertEqual(outcome.rebound.returned_budget, 4)
        self.assertEqual(outcome.after_center, -6)

    def test_zero_return_sample_rejects_forward_motion_without_reverse_travel(self):
        zero = MaterialHistoryState(1, RETURNING, 0)
        outcome = material_wall_step(
            self.wall,
            -2,
            2,
            0,
            3,
            zero,
            1000,
        )
        self.assertEqual(outcome.kind, REBOUND)
        self.assertEqual(outcome.rebound.returned_budget, 0)
        self.assertEqual(outcome.after_center, -2)

    def test_primitive_overlap_at_proposed_end_triggers_at_every_factor(self):
        for factor in (1, 2, 10):
            outcome = material_wall_step(
                self.wall,
                -2,
                0,
                0,
                factor,
                self.half_return,
                1000,
            )
            self.assertEqual(outcome.kind, REBOUND)
            self.assertEqual(outcome.proposed_end_clearance, 0)

    def test_same_side_contact_free_motion_is_plain_accept_not_transmission(self):
        outcome = material_wall_step(
            self.wall,
            -5,
            -4,
            0,
            2,
            self.half_return,
            1000,
        )
        self.assertEqual(outcome.kind, ACCEPT)
        self.assertEqual(outcome.after_center, -4)
        self.assertFalse(outcome.crosses_between_separated_sides)

    def test_right_to_left_rebound_uses_opposite_direction(self):
        outcome = material_wall_step(
            self.wall,
            2,
            -2,
            0,
            3,
            self.half_return,
            1000,
        )
        self.assertEqual(outcome.kind, REBOUND)
        self.assertEqual(outcome.incoming_direction, -1)
        self.assertEqual(outcome.after_center, 4)

    def test_primitive_contact_start_is_rejected_as_invalid_pre_state(self):
        with self.assertRaises(ValueError):
            material_wall_step(
                self.wall,
                0,
                2,
                0,
                1,
                self.half_return,
                1000,
            )


if __name__ == "__main__":
    unittest.main()
