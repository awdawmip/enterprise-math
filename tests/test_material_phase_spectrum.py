import unittest

from enterprise_math.material_phase_spectrum import (
    controlling_gap_phase_multiplicity,
    material_phase_spectrum,
)
from enterprise_math.material_response import material_curve_profile
from enterprise_math.scale_tunneling_1d import Wall1D


class MaterialPhaseSpectrumTests(unittest.TestCase):
    def setUp(self):
        self.wall = Wall1D(0, 0)
        self.profile = material_curve_profile(
            (0, 200, 400, 600, 800, 1000),
            amplitude=1000,
            loading_power=1,
            return_power=1,
            return_retention=1000,
        )

    def test_controlling_gap_multiplicity_has_center_singleton_only_when_even_sum(self):
        self.assertEqual(
            [controlling_gap_phase_multiplicity(6, gap) for gap in range(1, 4)],
            [2, 2, 1],
        )
        self.assertEqual(
            [controlling_gap_phase_multiplicity(5, gap) for gap in range(1, 3)],
            [2, 2],
        )

    def test_reference_spectrum_conserves_all_positive_clearance_phases(self):
        # Point wall/body gives H=2.  s=8 -> C=8 and 7 phases.
        # d=4: gaps 1,2,3 rebound with depths 3,2,1; gap4 transmits.
        report = material_phase_spectrum(
            self.wall,
            radius=0,
            displacement=8,
            collapse_factor=4,
            incoming_budget=8,
            material_profile=self.profile,
        )
        self.assertEqual(report.positive_clearance_phases, 7)
        self.assertEqual(report.transmitting_phases, 1)
        self.assertEqual(report.zero_return_phases, 0)
        self.assertEqual(report.rebound_phases, 6)
        self.assertEqual(report.interaction_phases, 6)
        self.assertEqual(
            tuple((item.returned_budget, item.phase_count) for item in report.rebound_bins),
            ((1, 2), (3, 2), (4, 2)),
        )
        self.assertEqual(report.total_returned_budget_over_phases, 16)

    def test_refinement_moves_interaction_phase_mass_and_returned_budget_downward(self):
        reports = [
            material_phase_spectrum(
                self.wall,
                radius=0,
                displacement=8,
                collapse_factor=factor,
                incoming_budget=8,
                material_profile=self.profile,
            )
            for factor in (5, 4, 3, 2, 1)
        ]
        transmitting = [report.transmitting_phases for report in reports]
        interaction = [report.interaction_phases for report in reports]
        returned_totals = [
            report.total_returned_budget_over_phases for report in reports
        ]
        self.assertEqual(transmitting, sorted(transmitting))
        self.assertEqual(interaction, sorted(interaction, reverse=True))
        self.assertEqual(returned_totals, sorted(returned_totals, reverse=True))
        for report in reports:
            self.assertEqual(
                report.transmitting_phases
                + report.zero_return_phases
                + report.rebound_phases,
                report.positive_clearance_phases,
            )

    def test_zero_return_material_creates_interaction_without_true_rebound(self):
        zero_return = material_curve_profile(
            (0, 200, 400, 600, 800, 1000),
            amplitude=1000,
            loading_power=1,
            return_power=1,
            return_retention=0,
        )
        report = material_phase_spectrum(
            self.wall,
            radius=0,
            displacement=8,
            collapse_factor=4,
            incoming_budget=8,
            material_profile=zero_return,
        )
        self.assertEqual(report.transmitting_phases, 1)
        self.assertEqual(report.zero_return_phases, 6)
        self.assertEqual(report.rebound_phases, 0)
        self.assertEqual(report.interaction_phases, 6)
        self.assertEqual(report.rebound_bins, ())
        self.assertEqual(report.total_returned_budget_over_phases, 0)

    def test_small_incoming_budget_can_quantize_positive_material_response_to_zero(self):
        report = material_phase_spectrum(
            self.wall,
            radius=0,
            displacement=8,
            collapse_factor=4,
            incoming_budget=1,
            material_profile=self.profile,
        )
        self.assertGreater(report.zero_return_phases, 0)
        self.assertGreater(report.interaction_phases, report.rebound_phases)
        self.assertEqual(
            report.transmitting_phases
            + report.zero_return_phases
            + report.rebound_phases,
            report.positive_clearance_phases,
        )

    def test_terminal_factor_transmits_every_positive_clearance_phase(self):
        for displacement in range(2, 12):
            report = material_phase_spectrum(
                self.wall,
                0,
                displacement,
                1,
                incoming_budget=displacement,
                material_profile=self.profile,
            )
            self.assertEqual(report.zero_return_phases, 0)
            self.assertEqual(report.rebound_phases, 0)
            self.assertEqual(report.total_returned_budget_over_phases, 0)
            self.assertEqual(
                report.transmitting_phases,
                report.positive_clearance_phases,
            )

    def test_no_separated_crossing_phase_below_effective_thickness(self):
        report = material_phase_spectrum(
            self.wall,
            radius=1,
            displacement=3,
            collapse_factor=2,
            incoming_budget=3,
            material_profile=self.profile,
        )
        # H=T+D=1+3=4, so s=3 cannot have both endpoints separated on opposite sides.
        self.assertEqual(report.positive_clearance_phases, 0)
        self.assertEqual(report.zero_return_phases, 0)
        self.assertEqual(report.rebound_bins, ())
        self.assertEqual(report.total_returned_budget_over_phases, 0)

    def test_material_curve_must_cover_possible_layer_depths(self):
        short = material_curve_profile(
            (0, 100),
            amplitude=100,
            loading_power=1,
            return_power=1,
        )
        with self.assertRaises(ValueError):
            material_phase_spectrum(
                self.wall,
                0,
                8,
                4,
                8,
                short,
            )


if __name__ == "__main__":
    unittest.main()
