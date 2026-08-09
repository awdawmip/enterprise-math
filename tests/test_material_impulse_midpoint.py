import unittest

from enterprise_math.material_impulse_midpoint import (
    constant_rate_integrator_report,
    impulse_work_pairing_report,
)


class MaterialImpulseMidpointTests(unittest.TestCase):
    def test_midpoint_constant_rate_endpoint_is_partition_exact(self):
        schedules = (
            (1,),
            (1, 1),
            (2, 1),
            (1, 3, 2),
            (0, 2, 1),
            (4, 0, 0, 3),
        )
        for initial in range(-8, 9):
            for rate in range(-5, 6):
                for schedule in schedules:
                    report = constant_rate_integrator_report(initial, rate, schedule)
                    self.assertTrue(report.midpoint_partition_exact)
                    self.assertEqual(
                        report.final_lifted_momentum,
                        initial + rate * sum(schedule),
                    )

    def test_one_sided_schedule_defects_are_exact_square_duration_resource(self):
        for initial in range(-5, 6):
            for rate in range(-4, 5):
                for schedule in ((1,), (1, 1), (2, 3), (1, 2, 4)):
                    report = constant_rate_integrator_report(initial, rate, schedule)
                    expected = rate * sum(dt * dt for dt in schedule)
                    self.assertEqual(report.postkick_midpoint_defect, expected)
                    self.assertEqual(report.midpoint_prekick_defect, expected)

    def test_refining_positive_duration_reduces_postkick_cadence_defect_for_positive_rate(self):
        coarse = constant_rate_integrator_report(7, 3, (6,))
        refined = constant_rate_integrator_report(7, 3, (1, 1, 1, 1, 1, 1))
        self.assertEqual(
            coarse.midpoint_doubled_displacement_numerator,
            refined.midpoint_doubled_displacement_numerator,
        )
        self.assertGreater(
            coarse.postkick_midpoint_defect,
            refined.postkick_midpoint_defect,
        )
        self.assertEqual(coarse.postkick_midpoint_defect, 3 * 36)
        self.assertEqual(refined.postkick_midpoint_defect, 3 * 6)

    def test_midpoint_impulse_work_matches_kinetic_square_change_for_all_small_integers(self):
        for before in range(-20, 21):
            for impulse in range(-10, 11):
                report = impulse_work_pairing_report(before, impulse)
                self.assertEqual(
                    report.midpoint_work_numerator,
                    report.kinetic_square_change,
                )
                self.assertEqual(report.post_defect, impulse * impulse)
                self.assertEqual(report.pre_defect, -(impulse * impulse))

    def test_reference_kick_exposes_pre_post_defects_but_midpoint_closes_exactly(self):
        report = impulse_work_pairing_report(before_lifted_momentum=20, impulse_numerator=-8)
        self.assertEqual(report.after_lifted_momentum, 12)
        self.assertEqual(report.kinetic_square_change, 12 * 12 - 20 * 20)
        self.assertEqual(report.midpoint_work_numerator, report.kinetic_square_change)
        self.assertEqual(report.post_defect, 64)
        self.assertEqual(report.pre_defect, -64)

    def test_invalid_duration_schedules_are_rejected(self):
        with self.assertRaises(ValueError):
            constant_rate_integrator_report(0, 1, ())
        with self.assertRaises(ValueError):
            constant_rate_integrator_report(0, 1, (0, 0))
        with self.assertRaises(ValueError):
            constant_rate_integrator_report(0, 1, (1, -1))


if __name__ == "__main__":
    unittest.main()
