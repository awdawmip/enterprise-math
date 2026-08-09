import unittest

from enterprise_math.material_basis import (
    DIGITAL_X_PHASE,
    RECURRENCE_PHASE,
    ROTATION_PHASE,
    digital_circle_y_basis,
    recurrence_quarter_basis,
    rotation_quarter_basis,
)
from enterprise_math.material_oscillator import PythagoreanRotation


class MaterialBasisTests(unittest.TestCase):
    def setUp(self):
        self.rotation = PythagoreanRotation(399, 40, 401)

    def test_reference_rotation_quarter_has_small_peak_defect(self):
        report = rotation_quarter_basis(1000, self.rotation)
        self.assertEqual(report.phase_kind, ROTATION_PHASE)
        self.assertTrue(report.monotone_nondecreasing)
        self.assertEqual(report.sample_count, 17)
        self.assertEqual(report.peak, 991)
        self.assertEqual(report.peak_defect_from_amplitude, 9)
        self.assertEqual(
            report.samples,
            (0, 99, 197, 293, 386, 475, 560, 639, 712, 777, 835, 884, 924, 955, 977, 989, 991),
        )

    def test_reference_recurrence_quarter_is_shorter_and_lower(self):
        report = recurrence_quarter_basis(1000, self.rotation)
        self.assertEqual(report.phase_kind, RECURRENCE_PHASE)
        self.assertTrue(report.monotone_nondecreasing)
        self.assertEqual(report.sample_count, 16)
        self.assertEqual(report.peak, 960)
        self.assertEqual(report.peak_defect_from_amplitude, 40)
        self.assertEqual(report.samples[-3:], (936, 953, 960))

    def test_digital_circle_reaches_exact_peak_but_has_integer_phase_plateaus(self):
        report = digital_circle_y_basis(1000)
        self.assertEqual(report.phase_kind, DIGITAL_X_PHASE)
        self.assertTrue(report.monotone_nondecreasing)
        self.assertEqual(report.sample_count, 1001)
        self.assertEqual(report.peak, 1000)
        self.assertEqual(report.peak_defect_from_amplitude, 0)
        self.assertEqual(report.plateau_count, 414)
        self.assertEqual(report.distinct_sample_count, 587)

    def test_low_amplitude_rotation_basis_stays_finite(self):
        for amplitude in range(0, 20):
            report = rotation_quarter_basis(amplitude, self.rotation)
            self.assertTrue(report.monotone_nondecreasing)
            self.assertTrue(all(0 <= value <= amplitude for value in report.samples))

    def test_invalid_basis_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            digital_circle_y_basis(-1)
        with self.assertRaises(ValueError):
            recurrence_quarter_basis(10, self.rotation, max_samples=1)


if __name__ == "__main__":
    unittest.main()
