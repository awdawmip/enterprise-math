import unittest
from fractions import Fraction

from enterprise_math.precision_threshold_record import (
    overlap_count_by_enumeration,
    pedalino_representative_region_excluded,
    representative_visibility_region_excluded,
    threshold_record_overlap,
)


class PrecisionThresholdRecordTests(unittest.TestCase):
    def test_closed_form_overlap_matches_exhaustive_integer_records(self):
        for resolution in range(1, 21):
            for separation in range(0, 26):
                self.assertEqual(
                    threshold_record_overlap(separation, resolution),
                    Fraction(overlap_count_by_enumeration(separation, resolution), resolution),
                )

    def test_overlap_has_exact_triangular_threshold_form(self):
        self.assertEqual(threshold_record_overlap(0, 10), 1)
        self.assertEqual(threshold_record_overlap(1, 10), Fraction(9, 10))
        self.assertEqual(threshold_record_overlap(9, 10), Fraction(1, 10))
        self.assertEqual(threshold_record_overlap(10, 10), 0)
        self.assertEqual(threshold_record_overlap(15, 10), 0)

    def test_pedalino_representative_exclusion_is_exact_integer_cross_product(self):
        for resolution in range(1, 121):
            for separation in range(0, resolution + 3):
                self.assertEqual(
                    pedalino_representative_region_excluded(separation, resolution),
                    representative_visibility_region_excluded(
                        separation, resolution, Fraction(9, 100)
                    ),
                )
        self.assertFalse(pedalino_representative_region_excluded(91, 100))
        self.assertTrue(pedalino_representative_region_excluded(92, 100))

    def test_invalid_inputs_fail_closed(self):
        with self.assertRaises(ValueError):
            threshold_record_overlap(-1, 10)
        with self.assertRaises(ValueError):
            threshold_record_overlap(1, 0)
        with self.assertRaises(ValueError):
            representative_visibility_region_excluded(1, 10, Fraction(11, 10))


if __name__ == "__main__":
    unittest.main()
