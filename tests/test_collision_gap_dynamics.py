import unittest

from enterprise_math.collision_gap_dynamics import (
    contact_exit_bit,
    contact_exit_threshold_within_fiber,
    gap_separation_update,
)


class CollisionGapDynamicsTests(unittest.TestCase):
    def test_gap_update_matches_direct_projection_on_small_domain(self):
        for factor in range(1, 8):
            for gap in range(20):
                for increment in range(12):
                    update = gap_separation_update(gap, factor, increment)
                    self.assertEqual(update.coarse_before, gap // factor)
                    self.assertEqual(update.detail_before, gap % factor)
                    self.assertEqual(update.coarse_after, (gap + increment) // factor)
                    self.assertEqual(update.detail_after, (gap + increment) % factor)
                    self.assertEqual(
                        update.coarse_after,
                        update.coarse_before
                        + update.increment_coarse_part
                        + update.carry,
                    )

    def test_same_macro_contact_bit_can_have_different_next_contact(self):
        low_detail = gap_separation_update(0, 3, 1)
        boundary_detail = gap_separation_update(2, 3, 1)
        self.assertTrue(low_detail.macro_contact_before)
        self.assertTrue(boundary_detail.macro_contact_before)
        self.assertTrue(low_detail.macro_contact_after)
        self.assertFalse(boundary_detail.macro_contact_after)
        self.assertEqual(low_detail.carry, 0)
        self.assertEqual(boundary_detail.carry, 1)

    def test_unit_separation_exits_only_top_detail_of_contact_fiber(self):
        for factor in range(2, 10):
            threshold = contact_exit_threshold_within_fiber(factor, 1)
            self.assertEqual(threshold, factor - 1)
            for detail in range(factor):
                self.assertEqual(
                    contact_exit_bit(detail, factor, 1),
                    detail == factor - 1,
                )

    def test_general_subfactor_increment_has_exact_exit_threshold(self):
        for factor in range(2, 10):
            for increment in range(1, factor):
                threshold = contact_exit_threshold_within_fiber(factor, increment)
                self.assertEqual(threshold, factor - increment)
                for detail in range(factor):
                    self.assertEqual(
                        contact_exit_bit(detail, factor, increment),
                        detail >= threshold,
                    )

    def test_full_factor_increment_exits_every_contact_detail(self):
        for factor in range(1, 8):
            self.assertEqual(
                contact_exit_threshold_within_fiber(factor, factor), 0
            )
            for detail in range(factor):
                self.assertTrue(contact_exit_bit(detail, factor, factor))

    def test_zero_increment_exits_no_contact_detail(self):
        for factor in range(1, 8):
            self.assertEqual(
                contact_exit_threshold_within_fiber(factor, 0), factor
            )
            for detail in range(factor):
                self.assertFalse(contact_exit_bit(detail, factor, 0))

    def test_exit_bit_rejects_state_that_is_already_resolved_noncontact(self):
        with self.assertRaises(ValueError):
            contact_exit_bit(3, 3, 1)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            gap_separation_update(-1, 2, 1)
        with self.assertRaises(ValueError):
            gap_separation_update(1, 0, 1)
        with self.assertRaises(ValueError):
            contact_exit_threshold_within_fiber(2, -1)


if __name__ == "__main__":
    unittest.main()
