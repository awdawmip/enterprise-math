import unittest

from enterprise_math.action_language_precision import reachable_translations
from enterprise_math.two_sided_guarded_peak_defects import (
    two_sided_guard_peak_defect_report,
    two_sided_guard_peak_defect_sequence,
    unique_positive_speed_has_no_packing_defect,
)


def direct_nonnegative_reachable_count(actions, horizon):
    return sum(
        translation >= 0
        for translation in reachable_translations(actions, horizon)
    )


class TwoSidedGuardedPeakDefectTests(unittest.TestCase):
    def test_exact_all_horizon_defect_decomposition_matches_direct_reachability(self):
        action_sets = (
            (-2, 3),
            (-4, 6),
            (-3, 5),
            (-5, -2, 3, 7),
            (-2, 4, 5),
            (-1, 3, 5),
            (-1, 2, 5),
            (-2, 1, 5),
            (-5, 2, 5),
            (-5, 3, 5),
            (-3, 0, 5),
        )
        for actions in action_sets:
            for horizon in range(0, 8):
                report = two_sided_guard_peak_defect_report(
                    actions,
                    horizon,
                )
                direct = direct_nonnegative_reachable_count(
                    report.normalized_actions,
                    horizon,
                )
                self.assertEqual(
                    report.nonnegative_reachable_count,
                    direct,
                )
                self.assertEqual(
                    direct,
                    horizon * report.normalized_fastest_positive
                    + 1
                    - report.arithmetic_gap_count
                    - report.packing_defect_count,
                )
                self.assertEqual(
                    report.guard_only_class_count,
                    direct + 1,
                )

    def test_pure_arithmetic_gap_example_has_no_packing_defect(self):
        sequence = two_sided_guard_peak_defect_sequence(
            (-2, 3),
            7,
        )
        self.assertEqual(
            tuple(report.arithmetic_gap_count for report in sequence),
            (0, 2, 3, 4, 4, 4, 4, 4),
        )
        self.assertEqual(
            tuple(report.packing_defect_count for report in sequence),
            (0, 0, 0, 0, 0, 0, 0, 0),
        )
        self.assertEqual(sequence[-1].deficit_genus, 4)
        self.assertEqual(
            sequence[-1].gap_saturation_prefix_horizon,
            3,
        )

    def test_hole_free_semigroup_can_still_be_finitely_underresolved(self):
        sequence = two_sided_guard_peak_defect_sequence(
            (-2, 4, 5),
            5,
        )
        self.assertEqual(
            tuple(report.arithmetic_gap_count for report in sequence),
            (0, 0, 0, 0, 0, 0),
        )
        self.assertEqual(
            tuple(report.packing_defect_count for report in sequence),
            (0, 3, 3, 1, 0, 0),
        )
        self.assertEqual(sequence[0].deficit_genus, 0)
        self.assertEqual(sequence[0].deficit_conductor, 0)
        self.assertEqual(sequence[0].gap_saturation_prefix_horizon, 0)
        self.assertEqual(sequence[0].exact_prefix_affine_onset, 4)

    def test_mixed_arithmetic_and_packing_defects_are_separate(self):
        sequence = two_sided_guard_peak_defect_sequence(
            (-1, 3, 5),
            5,
        )
        self.assertEqual(
            tuple(report.arithmetic_gap_count for report in sequence),
            (0, 2, 2, 2, 2, 2),
        )
        self.assertEqual(
            tuple(report.packing_defect_count for report in sequence),
            (0, 1, 1, 0, 0, 0),
        )
        self.assertEqual(sequence[-1].deficit_genus, 2)
        self.assertEqual(
            sequence[-1].gap_saturation_prefix_horizon,
            1,
        )
        self.assertEqual(
            sequence[-1].exact_prefix_affine_onset,
            3,
        )

    def test_packing_underresolution_need_not_be_monotone(self):
        first = two_sided_guard_peak_defect_sequence(
            (-5, 2, 5),
            6,
        )
        second = two_sided_guard_peak_defect_sequence(
            (-5, 3, 5),
            7,
        )
        self.assertEqual(
            tuple(report.packing_defect_count for report in first),
            (0, 0, 1, 2, 1, 0, 0),
        )
        self.assertEqual(
            tuple(report.packing_defect_count for report in second),
            (0, 1, 3, 3, 2, 1, 0, 0),
        )

    def test_affine_onset_is_exactly_when_total_defect_reaches_genus_forever(self):
        action_sets = (
            (-2, 3),
            (-3, 5),
            (-5, -2, 3, 7),
            (-2, 4, 5),
            (-1, 3, 5),
            (-1, 2, 5),
            (-2, 1, 5),
        )
        for actions in action_sets:
            sequence = two_sided_guard_peak_defect_sequence(
                actions,
                10,
            )
            onset = sequence[0].exact_prefix_affine_onset
            genus = sequence[0].deficit_genus
            for report in sequence:
                if report.prefix_horizon >= onset:
                    self.assertEqual(report.total_missing_count, genus)
            if onset > 0:
                self.assertNotEqual(
                    sequence[onset - 1].total_missing_count,
                    genus,
                )

    def test_unique_positive_action_value_precludes_packing_defects(self):
        action_sets = (
            (-2, 3),
            (-4, 6),
            (-3, 5),
            (-5, -2, 7),
            (-3, 0, 5),
        )
        for actions in action_sets:
            for horizon in range(0, 10):
                self.assertTrue(
                    unique_positive_speed_has_no_packing_defect(
                        actions,
                        horizon,
                    )
                )
                self.assertEqual(
                    two_sided_guard_peak_defect_report(
                        actions,
                        horizon,
                    ).packing_defect_count,
                    0,
                )

    def test_unique_positive_helper_rejects_multiple_positive_speeds(self):
        with self.assertRaises(ValueError):
            unique_positive_speed_has_no_packing_defect(
                (-2, 4, 5),
                3,
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            two_sided_guard_peak_defect_report((1, 2), 3)
        with self.assertRaises(ValueError):
            two_sided_guard_peak_defect_report((-1, -2), 3)
        with self.assertRaises(ValueError):
            two_sided_guard_peak_defect_report((-1, 1), -1)
        with self.assertRaises(TypeError):
            two_sided_guard_peak_defect_report((-1, True, 3), 2)


if __name__ == "__main__":
    unittest.main()
