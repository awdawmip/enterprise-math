import unittest
from collections import Counter
from itertools import product

from enterprise_math.material_clearance_spectrum import (
    LOADING,
    RETURNING,
    material_clearance_coverage,
    material_clearance_spectrum,
)
from enterprise_math.material_response import material_curve_profile


class MaterialClearanceSpectrumTests(unittest.TestCase):
    def test_closed_form_coverage_matches_direct_enumeration(self):
        for dimension in range(1, 5):
            for factor in range(1, 8):
                vectors = [
                    vector
                    for vector in product(range(factor), repeat=dimension)
                    if any(vector)
                ]
                for max_depth in range(0, factor + 3):
                    report = material_clearance_coverage(dimension, factor, max_depth)
                    represented = sum(
                        factor - max(vector) <= max_depth
                        for vector in vectors
                    )
                    self.assertEqual(report.coarse_only_states, len(vectors))
                    self.assertEqual(report.represented_states, represented)
                    self.assertEqual(
                        report.underresolved_states,
                        len(vectors) - represented,
                    )

    def test_full_depth_covers_every_positive_coarse_clearance_state(self):
        for dimension in range(1, 5):
            for factor in range(1, 8):
                report = material_clearance_coverage(
                    dimension,
                    factor,
                    max_material_depth=max(0, factor - 1),
                )
                self.assertEqual(report.underresolved_states, 0)
                self.assertEqual(report.represented_states, factor**dimension - 1)

    def test_response_bins_match_direct_shell_mapping(self):
        profile = material_curve_profile(
            (0, 100, 200, 300, 400),
            amplitude=400,
            loading_power=1,
            return_power=1,
            return_retention=200,
        )
        for dimension in (1, 2, 3):
            factor = 6
            report = material_clearance_spectrum(
                dimension,
                factor,
                profile,
                RETURNING,
            )
            direct = Counter()
            underresolved = 0
            max_depth = len(profile.returning) - 1
            for vector in product(range(factor), repeat=dimension):
                if not any(vector):
                    continue
                depth = factor - max(vector)
                if depth > max_depth:
                    underresolved += 1
                else:
                    direct[profile.returning[depth]] += 1
            self.assertEqual(
                {(item.response_sample, item.state_count) for item in report.bins},
                set(direct.items()),
            )
            self.assertEqual(report.coverage.underresolved_states, underresolved)

    def test_material_plateau_merges_spatial_shells_without_enumeration(self):
        profile = material_curve_profile(
            (0, 25, 50, 75, 100),
            amplitude=100,
            loading_power=1,
            return_power=1,
            return_retention=0,
        )
        report = material_clearance_spectrum(2, 5, profile, RETURNING)
        self.assertEqual(len(report.bins), 1)
        self.assertEqual(report.bins[0].response_sample, 0)
        self.assertEqual(
            report.bins[0].state_count,
            report.coverage.represented_states,
        )

    def test_loading_and_returning_can_have_different_clearance_spectra(self):
        profile = material_curve_profile(
            (0, 20, 40, 60, 80, 100),
            amplitude=100,
            loading_power=2,
            return_power=1,
            return_retention=50,
        )
        loading = material_clearance_spectrum(2, 6, profile, LOADING)
        returning = material_clearance_spectrum(2, 6, profile, RETURNING)
        self.assertEqual(loading.coverage, returning.coverage)
        self.assertNotEqual(loading.bins, returning.bins)
        self.assertEqual(
            sum(item.state_count for item in loading.bins),
            loading.coverage.represented_states,
        )
        self.assertEqual(
            sum(item.state_count for item in returning.bins),
            returning.coverage.represented_states,
        )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            material_clearance_coverage(0, 3, 1)
        with self.assertRaises(ValueError):
            material_clearance_coverage(2, 0, 1)
        with self.assertRaises(ValueError):
            material_clearance_coverage(2, 3, -1)


if __name__ == "__main__":
    unittest.main()
