import unittest
from collections import Counter
from itertools import product

from enterprise_math.material_hysteresis import LOADING, RETURNING
from enterprise_math.material_kinematic_response_spectrum import (
    directional_kinematic_spectrum_2d,
    scalar_kinematic_spectrum,
)
from enterprise_math.material_kinematic_coupling import rebound_budget
from enterprise_math.material_kinematic_coupling_2d import direction_budget_report_2d
from enterprise_math.material_response import (
    explicit_material_curve_profile,
    material_curve_profile,
)


class MaterialKinematicResponseSpectrumTests(unittest.TestCase):
    def test_scalar_spectrum_matches_direct_clearance_enumeration(self):
        profile = material_curve_profile(
            (0, 20, 40, 60, 80, 100),
            amplitude=100,
            loading_power=2,
            return_power=1,
            return_retention=60,
        )
        for dimension in (1, 2, 3):
            for factor in range(2, 7):
                for budget in (0, 1, 7, 31):
                    report = scalar_kinematic_spectrum(
                        dimension,
                        factor,
                        profile,
                        budget,
                        RETURNING,
                    )
                    direct = Counter()
                    max_depth = len(profile.returning) - 1
                    for vector in product(range(factor), repeat=dimension):
                        if not any(vector):
                            continue
                        depth = factor - max(vector)
                        if depth > max_depth:
                            continue
                        returned = rebound_budget(
                            budget,
                            profile.returning[depth],
                            profile.amplitude,
                        ).returned_budget
                        direct[returned] += 1
                    self.assertEqual(
                        {(item.returned_budget, item.state_count) for item in report.bins},
                        set(direct.items()),
                    )
                    self.assertEqual(
                        sum(item.state_count for item in report.bins),
                        report.coverage.represented_states,
                    )

    def test_loading_and_returning_can_induce_different_kinematic_spectra(self):
        profile = material_curve_profile(
            (0, 25, 50, 75, 100),
            amplitude=100,
            loading_power=2,
            return_power=1,
            return_retention=50,
        )
        loading = scalar_kinematic_spectrum(2, 5, profile, 37, LOADING)
        returning = scalar_kinematic_spectrum(2, 5, profile, 37, RETURNING)
        self.assertEqual(loading.coverage, returning.coverage)
        self.assertNotEqual(loading.bins, returning.bins)

    def test_axis_direction_has_no_direction_conflict_states(self):
        profile = material_curve_profile(
            (0, 1, 2, 3, 4),
            amplitude=4,
        )
        report = directional_kinematic_spectrum_2d(5, profile, (9, 0))
        self.assertEqual(report.direction_conflict_states, 0)
        self.assertEqual(
            report.direction_preserved_states,
            report.coverage.represented_states,
        )

    def test_general_slope_conflict_count_matches_exact_shell_multiplicity(self):
        profile = explicit_material_curve_profile(
            loading=(0, 2, 4),
            returning=(0, 2, 4),
            amplitude=4,
        )
        report = directional_kinematic_spectrum_2d(
            collapse_factor=3,
            profile=profile,
            incoming_vector=(2, 3),
        )
        # depth 1 has shell multiplicity 3^2-2^2=5 and response 2/4,
        # which exposes the direction-budget conflict for primitive ray (2,3).
        # depth 2 has multiplicity 2^2-1^2=3 and full response 4/4, hence locked.
        self.assertEqual(report.coverage.represented_states, 8)
        self.assertEqual(report.direction_conflict_states, 5)
        self.assertEqual(report.direction_preserved_states, 3)

    def test_directional_spectrum_matches_direct_shell_to_coupling_map(self):
        profile = material_curve_profile(
            (0, 20, 40, 60, 80, 100),
            amplitude=100,
            loading_power=1,
            return_power=1,
            return_retention=75,
        )
        incoming = (4, -6)
        factor = 6
        report = directional_kinematic_spectrum_2d(
            factor,
            profile,
            incoming,
            RETURNING,
        )
        direct = Counter()
        max_depth = len(profile.returning) - 1
        for vector in product(range(factor), repeat=2):
            if not any(vector):
                continue
            depth = factor - max(vector)
            if depth > max_depth:
                continue
            coupling = direction_budget_report_2d(
                incoming,
                profile.returning[depth],
                profile.amplitude,
            )
            direct[
                (
                    coupling.componentwise_linf_budget,
                    coupling.primitive_ray_locked_linf_budget,
                    coupling.componentwise_preserves_primitive_ray,
                )
            ] += 1
        self.assertEqual(
            {
                (
                    item.componentwise_linf_budget,
                    item.primitive_ray_locked_linf_budget,
                    item.direction_preserved,
                    item.state_count,
                )
                for item in report.bins
            },
            {(key[0], key[1], key[2], count) for key, count in direct.items()},
        )

    def test_zero_scalar_budget_is_valid_and_collapses_all_bins_to_zero(self):
        profile = material_curve_profile((0, 25, 50, 75, 100), amplitude=100)
        report = scalar_kinematic_spectrum(3, 5, profile, 0)
        self.assertEqual(len(report.bins), 1)
        self.assertEqual(report.bins[0].returned_budget, 0)
        self.assertEqual(report.bins[0].state_count, report.coverage.represented_states)

    def test_invalid_inputs_are_rejected(self):
        profile = material_curve_profile((0, 1), amplitude=1)
        with self.assertRaises(ValueError):
            scalar_kinematic_spectrum(1, 2, profile, -1)
        with self.assertRaises(ValueError):
            scalar_kinematic_spectrum(1, 2, profile, 1, "UNKNOWN")
        with self.assertRaises(ValueError):
            directional_kinematic_spectrum_2d(2, profile, (0, 0))


if __name__ == "__main__":
    unittest.main()
