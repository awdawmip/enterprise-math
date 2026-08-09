import unittest

from enterprise_math.material_oscillator import PythagoreanRotation
from enterprise_math.material_projection_schedule import (
    batched_rotation_projection,
    compare_projection_schedules,
    sequential_rotation_projection,
)


class MaterialProjectionScheduleTests(unittest.TestCase):
    def test_one_step_schedules_are_identical(self):
        rotation = PythagoreanRotation(3, 4, 5)
        for x in range(-8, 9):
            for y in range(-8, 9):
                self.assertEqual(
                    sequential_rotation_projection((x, y), rotation, 1),
                    batched_rotation_projection((x, y), rotation, 1),
                )

    def test_sequential_projection_can_preserve_more_radius_than_batched(self):
        rotation = PythagoreanRotation(3, 4, 5)
        report = compare_projection_schedules((-20, -16), rotation, 2)
        self.assertEqual(report.sequential_state, (20, -15))
        self.assertEqual(report.batched_state, (20, -14))
        self.assertEqual(report.sequential_norm_sq, 625)
        self.assertEqual(report.batched_norm_sq, 596)
        self.assertGreater(report.norm_sq_difference, 0)

    def test_batched_projection_can_preserve_more_radius_than_sequential(self):
        rotation = PythagoreanRotation(3, 4, 5)
        report = compare_projection_schedules((-20, -14), rotation, 2)
        self.assertEqual(report.sequential_state, (19, -14))
        self.assertEqual(report.batched_state, (19, -15))
        self.assertEqual(report.sequential_norm_sq, 557)
        self.assertEqual(report.batched_norm_sq, 586)
        self.assertLess(report.norm_sq_difference, 0)

    def test_small_domain_contains_both_cadence_orderings_and_equalities(self):
        rotation = PythagoreanRotation(3, 4, 5)
        saw_sequential_larger = False
        saw_batched_larger = False
        saw_equal = False
        for x in range(-12, 13):
            for y in range(-12, 13):
                report = compare_projection_schedules((x, y), rotation, 2)
                saw_sequential_larger |= report.norm_sq_difference > 0
                saw_batched_larger |= report.norm_sq_difference < 0
                saw_equal |= report.norm_sq_difference == 0
        self.assertTrue(saw_sequential_larger)
        self.assertTrue(saw_batched_larger)
        self.assertTrue(saw_equal)

    def test_zero_step_is_identity_for_both_schedules(self):
        rotation = PythagoreanRotation(5, 12, 13)
        state = (-7, 11)
        self.assertEqual(sequential_rotation_projection(state, rotation, 0), state)
        self.assertEqual(batched_rotation_projection(state, rotation, 0), state)


if __name__ == "__main__":
    unittest.main()
