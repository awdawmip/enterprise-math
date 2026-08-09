import unittest

from enterprise_math.material_response import explicit_material_curve_profile
from enterprise_math.material_scale_phase_diagram import (
    REBOUND_PHASE,
    RESOLVED_PHASE,
    UNDERRESOLVED_PHASE,
    ZERO_RETURN_PHASE,
    minimum_rebound_depth,
    monotone_scale_phase_thresholds,
    scale_response_phase_for_gap,
)


class MaterialScalePhaseDiagramTests(unittest.TestCase):
    def setUp(self):
        self.profile = explicit_material_curve_profile(
            loading=(0, 100, 200, 300, 400),
            returning=(0, 100, 200, 300, 400),
            amplitude=400,
        )

    def test_reference_four_phase_sequence_has_exact_boundaries(self):
        # B=2 requires response >=200, so first nonzero return occurs at depth 2.
        gap = 3
        budget = 2
        phases = [
            scale_response_phase_for_gap(gap, d, budget, self.profile).phase
            for d in range(1, 10)
        ]
        self.assertEqual(
            phases,
            [
                RESOLVED_PHASE,
                RESOLVED_PHASE,
                RESOLVED_PHASE,
                ZERO_RETURN_PHASE,
                REBOUND_PHASE,
                REBOUND_PHASE,
                REBOUND_PHASE,
                UNDERRESOLVED_PHASE,
                UNDERRESOLVED_PHASE,
            ],
        )
        thresholds = monotone_scale_phase_thresholds(gap, budget, self.profile)
        self.assertEqual(thresholds.minimum_rebound_depth, 2)
        self.assertEqual(thresholds.resolved_max_factor, 3)
        self.assertEqual(thresholds.zero_return_factor_range, (4, 4))
        self.assertEqual(thresholds.rebound_factor_range, (5, 7))
        self.assertEqual(thresholds.underresolved_min_factor, 8)

    def test_no_nonzero_return_leaves_entire_represented_segment_zero_return(self):
        thresholds = monotone_scale_phase_thresholds(2, 0, self.profile)
        self.assertIsNone(thresholds.minimum_rebound_depth)
        self.assertEqual(thresholds.zero_return_factor_range, (3, 6))
        self.assertIsNone(thresholds.rebound_factor_range)
        self.assertEqual(thresholds.underresolved_min_factor, 7)

    def test_full_response_starts_rebound_at_first_represented_depth(self):
        full = explicit_material_curve_profile(
            loading=(0, 400, 400),
            returning=(0, 400, 400),
            amplitude=400,
        )
        thresholds = monotone_scale_phase_thresholds(5, 1, full)
        self.assertEqual(thresholds.minimum_rebound_depth, 1)
        self.assertIsNone(thresholds.zero_return_factor_range)
        self.assertEqual(thresholds.rebound_factor_range, (6, 7))
        self.assertEqual(thresholds.underresolved_min_factor, 8)

    def test_minimum_rebound_depth_matches_direct_integer_threshold(self):
        for budget in range(0, 9):
            expected = next(
                (
                    depth
                    for depth, sample in enumerate(self.profile.returning[1:], start=1)
                    if budget * sample >= self.profile.amplitude
                ),
                None,
            )
            self.assertEqual(minimum_rebound_depth(budget, self.profile), expected)

    def test_exact_classifier_matches_threshold_ranges_for_many_gaps_and_budgets(self):
        for gap in range(1, 7):
            for budget in range(0, 8):
                thresholds = monotone_scale_phase_thresholds(gap, budget, self.profile)
                for d in range(1, gap + len(self.profile.returning) + 3):
                    phase = scale_response_phase_for_gap(
                        gap, d, budget, self.profile
                    ).phase
                    if d <= thresholds.resolved_max_factor:
                        expected = RESOLVED_PHASE
                    elif d >= thresholds.underresolved_min_factor:
                        expected = UNDERRESOLVED_PHASE
                    elif (
                        thresholds.rebound_factor_range is not None
                        and thresholds.rebound_factor_range[0]
                        <= d
                        <= thresholds.rebound_factor_range[1]
                    ):
                        expected = REBOUND_PHASE
                    else:
                        expected = ZERO_RETURN_PHASE
                    self.assertEqual(phase, expected)

    def test_nonmonotone_branch_rejects_interval_theorem_but_exact_classifier_still_works(self):
        nonmonotone = explicit_material_curve_profile(
            loading=(0, 100, 200, 300),
            returning=(0, 300, 100, 300),
            amplitude=300,
        )
        with self.assertRaises(ValueError):
            monotone_scale_phase_thresholds(2, 1, nonmonotone)
        self.assertEqual(
            scale_response_phase_for_gap(2, 3, 1, nonmonotone).phase,
            REBOUND_PHASE,
        )
        self.assertEqual(
            scale_response_phase_for_gap(2, 4, 1, nonmonotone).phase,
            ZERO_RETURN_PHASE,
        )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            scale_response_phase_for_gap(0, 2, 1, self.profile)
        with self.assertRaises(ValueError):
            scale_response_phase_for_gap(1, 0, 1, self.profile)
        with self.assertRaises(ValueError):
            scale_response_phase_for_gap(1, 2, -1, self.profile)


if __name__ == "__main__":
    unittest.main()
