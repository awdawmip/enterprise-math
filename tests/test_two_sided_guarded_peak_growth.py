import unittest

from enterprise_math.action_language_precision import reachable_translations
from enterprise_math.two_sided_guarded_peak_growth import (
    two_sided_deficit_generators,
    two_sided_guard_peak_growth_report,
)
from enterprise_math.two_sided_guarded_peak_spectrum import (
    two_sided_guard_only_class_count,
)


def direct_nonnegative_reachable_count(actions, horizon):
    return sum(
        translation >= 0
        for translation in reachable_translations(actions, horizon)
    )


class TwoSidedGuardedPeakGrowthTests(unittest.TestCase):
    def test_deficit_generators_are_exact_and_gcd_one(self):
        expected = {
            (-2, 3): (3, 5),
            (-4, 6): (3, 5),
            (-3, 5): (5, 8),
            (-5, -2, 3, 7): (4, 7, 9, 12),
            (-2, 4, 5): (1, 5, 7),
        }
        from math import gcd

        for actions, generators in expected.items():
            actual = two_sided_deficit_generators(actions)
            self.assertEqual(actual, generators)
            common = 0
            for generator in actual:
                common = gcd(common, generator)
            self.assertEqual(common, 1)

    def test_reference_semigroup_invariants_and_exact_onsets(self):
        expected = {
            (-2, 3): (1, 3, (3, 5), 8, 4, 4, 3),
            (-4, 6): (2, 3, (3, 5), 8, 4, 4, 3),
            (-3, 5): (1, 5, (5, 8), 28, 14, 7, 6),
            (-5, -2, 3, 7): (1, 7, (4, 7, 9, 12), 11, 6, 5, 2),
            (-2, 4, 5): (1, 5, (1, 5, 7), 0, 0, 12, 4),
            (-1, 3, 5): (1, 5, (2, 5, 6), 4, 2, 9, 3),
            (-1, 2, 5): (1, 5, (3, 5, 6), 8, 4, 5, 2),
            (-2, 1, 5): (1, 5, (4, 5, 7), 7, 4, 4, 2),
        }
        for actions, target in expected.items():
            report = two_sided_guard_peak_growth_report(actions)
            self.assertEqual(
                (
                    report.action_grain,
                    report.normalized_fastest_positive,
                    report.deficit_generators,
                    report.deficit_conductor,
                    report.deficit_genus,
                    report.sufficient_prefix_horizon,
                    report.exact_prefix_affine_onset,
                ),
                target,
            )

    def test_eventual_nonnegative_reachability_formula_is_exact(self):
        action_sets = (
            (-2, 3),
            (-4, 6),
            (-3, 5),
            (-5, -2, 3, 7),
            (-2, 4, 5),
            (-1, 3, 5),
            (-1, 2, 5),
            (-2, 1, 5),
            (-3, 0, 5),
        )
        for actions in action_sets:
            report = two_sided_guard_peak_growth_report(actions)
            for horizon in range(
                report.exact_prefix_affine_onset,
                report.exact_prefix_affine_onset + 9,
            ):
                direct = direct_nonnegative_reachable_count(
                    report.normalized_actions,
                    horizon,
                )
                self.assertEqual(
                    direct,
                    report.nonnegative_reachable_count_formula(horizon),
                )

    def test_exact_onset_is_minimal_when_positive(self):
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
            report = two_sided_guard_peak_growth_report(actions)
            onset = report.exact_prefix_affine_onset
            self.assertGreater(onset, 0)
            previous = onset - 1
            direct = direct_nonnegative_reachable_count(
                report.normalized_actions,
                previous,
            )
            affine = (
                previous * report.normalized_fastest_positive
                + 1
                - report.deficit_genus
            )
            self.assertNotEqual(direct, affine)

    def test_guard_only_class_growth_matches_peak_spectrum(self):
        action_sets = (
            (-2, 3),
            (-4, 6),
            (-3, 5),
            (-5, -2, 3, 7),
            (-2, 4, 5),
            (-1, 3, 5),
        )
        for actions in action_sets:
            report = two_sided_guard_peak_growth_report(actions)
            for word_horizon in range(
                report.exact_word_affine_onset,
                report.exact_word_affine_onset + 8,
            ):
                self.assertEqual(
                    two_sided_guard_only_class_count(
                        actions,
                        word_horizon,
                    ),
                    report.guard_only_class_count_formula(word_horizon),
                )

    def test_gcd_scaling_changes_cell_width_not_normalized_growth_law(self):
        primitive = two_sided_guard_peak_growth_report((-2, 3))
        scaled = two_sided_guard_peak_growth_report((-4, 6))

        self.assertEqual(primitive.action_grain, 1)
        self.assertEqual(scaled.action_grain, 2)
        self.assertEqual(primitive.normalized_actions, scaled.normalized_actions)
        self.assertEqual(
            primitive.normalized_fastest_positive,
            scaled.normalized_fastest_positive,
        )
        self.assertEqual(primitive.deficit_generators, scaled.deficit_generators)
        self.assertEqual(primitive.deficit_genus, scaled.deficit_genus)
        self.assertEqual(
            primitive.exact_prefix_affine_onset,
            scaled.exact_prefix_affine_onset,
        )

    def test_three_resources_are_independent_in_examples(self):
        primitive = two_sided_guard_peak_growth_report((-2, 3))
        scaled = two_sided_guard_peak_growth_report((-4, 6))
        self.assertNotEqual(primitive.action_grain, scaled.action_grain)
        self.assertEqual(
            primitive.normalized_fastest_positive,
            scaled.normalized_fastest_positive,
        )
        self.assertEqual(primitive.deficit_genus, scaled.deficit_genus)

        no_gap = two_sided_guard_peak_growth_report((-2, 4, 5))
        gaps = two_sided_guard_peak_growth_report((-1, 3, 5))
        self.assertEqual(
            no_gap.normalized_fastest_positive,
            gaps.normalized_fastest_positive,
        )
        self.assertNotEqual(no_gap.deficit_genus, gaps.deficit_genus)

    def test_formula_api_rejects_pre_onset_queries(self):
        report = two_sided_guard_peak_growth_report((-2, 3))
        with self.assertRaises(ValueError):
            report.nonnegative_reachable_count_formula(
                report.exact_prefix_affine_onset - 1
            )
        with self.assertRaises(ValueError):
            report.guard_only_class_count_formula(
                report.exact_word_affine_onset - 1
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            two_sided_deficit_generators((1, 2))
        with self.assertRaises(ValueError):
            two_sided_deficit_generators((-1, -2))
        with self.assertRaises(TypeError):
            two_sided_guard_peak_growth_report((-1, True, 3))


if __name__ == "__main__":
    unittest.main()
