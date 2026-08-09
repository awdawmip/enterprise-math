import unittest

from enterprise_math.material_oscillator import PythagoreanRotation
from enterprise_math.material_recurrence_invariant import (
    recurrence_invariant_step,
    recurrence_quadratic,
    recurrence_quadratic_trace,
)


class MaterialRecurrenceInvariantTests(unittest.TestCase):
    def test_fraction_free_lift_and_projected_defect_identity_hold_on_small_domain(self):
        rotation = PythagoreanRotation(3, 4, 5)
        for u in range(-12, 13):
            for v in range(-12, 13):
                report = recurrence_invariant_step(u, v, rotation)
                self.assertEqual(
                    report.quadratic_defect,
                    report.reconstructed_defect,
                )
                self.assertEqual(
                    report.raw_lift[0],
                    rotation.c * v,
                )

    def test_projected_recurrence_defect_has_both_signs(self):
        rotation = PythagoreanRotation(3, 4, 5)
        defects = [
            recurrence_invariant_step(u, v, rotation).quadratic_defect
            for u in range(-20, 21)
            for v in range(-20, 21)
        ]
        self.assertTrue(any(defect < 0 for defect in defects))
        self.assertTrue(any(defect > 0 for defect in defects))
        self.assertTrue(any(defect == 0 for defect in defects))

    def test_explicit_quadratic_pumping_counterexample(self):
        rotation = PythagoreanRotation(3, 4, 5)
        report = recurrence_invariant_step(-20, -19, rotation)
        self.assertEqual(report.after, (-19, -2))
        self.assertEqual(report.detail, -4)
        self.assertEqual(report.quadratic_defect, -72)
        self.assertGreater(report.quadratic_after, report.quadratic_before)

    def test_signed_local_defects_telescope(self):
        rotation = PythagoreanRotation(399, 40, 401)
        initial = (0, 99)
        trace = recurrence_quadratic_trace(initial, rotation, 300)
        total = sum(report.quadratic_defect for report in trace)
        self.assertEqual(
            total,
            recurrence_quadratic(*initial, rotation)
            - recurrence_quadratic(*trace[-1].after, rotation),
        )

    def test_nonzero_cycle_has_zero_total_quadratic_defect_over_one_period(self):
        rotation = PythagoreanRotation(3, 4, 5)
        # A=2 recurrence starts from (0,1) and has the six-state cycle:
        # (0,1)->(1,1)->(1,0)->(0,-1)->(-1,-1)->(-1,0)->(0,1).
        trace = recurrence_quadratic_trace((0, 1), rotation, 6)
        self.assertEqual(trace[-1].after, (0, 1))
        self.assertEqual(sum(report.quadratic_defect for report in trace), 0)
        self.assertTrue(any(report.quadratic_defect > 0 for report in trace))
        self.assertTrue(any(report.quadratic_defect < 0 for report in trace))


if __name__ == "__main__":
    unittest.main()
