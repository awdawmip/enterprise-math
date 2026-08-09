import unittest

from enterprise_math.material_phase_saturation import (
    saturated_interaction_phase_spectrum,
    saturation_clearance_sum_threshold,
    verify_saturated_wall_phase_spectrum,
)
from enterprise_math.material_response import explicit_material_curve_profile
from enterprise_math.scale_tunneling_1d import Wall1D


class MaterialPhaseSaturationTests(unittest.TestCase):
    def setUp(self):
        self.wall = Wall1D(0, 0)
        self.profile = explicit_material_curve_profile(
            loading=(0, 0, 2, 5),
            returning=(0, 0, 2, 5),
            amplitude=5,
        )

    def test_threshold_is_exactly_two_d_minus_one(self):
        for d in range(1, 12):
            self.assertEqual(saturation_clearance_sum_threshold(d), 2 * d - 1)

    def test_factorized_spectrum_conserves_exactly_two_phases_per_depth(self):
        for d in range(1, 9):
            for budget in range(0, 10):
                report = saturated_interaction_phase_spectrum(
                    d, budget, self.profile
                )
                self.assertEqual(report.interaction_phases, 2 * (d - 1))
                self.assertEqual(
                    report.underresolved_phases
                    + report.zero_return_phases
                    + report.rebound_phases,
                    report.interaction_phases,
                )
                self.assertEqual(report.underresolved_phases % 2, 0)
                self.assertEqual(report.zero_return_phases % 2, 0)
                self.assertEqual(report.rebound_phases % 2, 0)
                self.assertTrue(
                    all(item.phase_count % 2 == 0 for item in report.rebound_bins)
                )

    def test_full_phase_spectrum_matches_factorization_at_and_beyond_threshold(self):
        # Point wall/body has effective crossing displacement H=2 and C=s.
        for d in range(1, 8):
            threshold = saturation_clearance_sum_threshold(d)
            for clearance_sum in range(threshold, threshold + 8):
                displacement = clearance_sum
                for budget in range(0, 8):
                    self.assertTrue(
                        verify_saturated_wall_phase_spectrum(
                            self.wall,
                            radius=0,
                            displacement=displacement,
                            collapse_factor=d,
                            incoming_budget=budget,
                            profile=self.profile,
                        )
                    )

    def test_further_displacement_adds_only_transmission_phase_mass(self):
        d = 5
        threshold = saturation_clearance_sum_threshold(d)
        interaction_reports = []
        transmitting = []
        from enterprise_math.material_phase_spectrum import material_phase_spectrum

        for clearance_sum in range(threshold, threshold + 8):
            full = material_phase_spectrum(
                self.wall,
                0,
                clearance_sum,
                d,
                incoming_budget=7,
                material_profile=self.profile,
            )
            interaction_reports.append(
                (
                    full.underresolved_phases,
                    full.zero_return_phases,
                    full.rebound_phases,
                    tuple(
                        (item.returned_budget, item.phase_count)
                        for item in full.rebound_bins
                    ),
                )
            )
            transmitting.append(full.transmitting_phases)
        self.assertEqual(len(set(interaction_reports)), 1)
        self.assertEqual(
            transmitting,
            list(range(transmitting[0], transmitting[0] + len(transmitting))),
        )

    def test_nonmonotone_material_branch_still_factorizes_by_depth(self):
        nonmonotone = explicit_material_curve_profile(
            loading=(0, 5, 1, 4),
            returning=(0, 5, 1, 4),
            amplitude=5,
        )
        for d in range(2, 7):
            threshold = saturation_clearance_sum_threshold(d)
            self.assertTrue(
                verify_saturated_wall_phase_spectrum(
                    self.wall,
                    0,
                    threshold,
                    d,
                    3,
                    nonmonotone,
                )
            )

    def test_below_threshold_verifier_rejects_unsaturated_geometry(self):
        with self.assertRaises(ValueError):
            verify_saturated_wall_phase_spectrum(
                self.wall,
                0,
                displacement=6,
                collapse_factor=4,
                incoming_budget=6,
                profile=self.profile,
            )


if __name__ == "__main__":
    unittest.main()
