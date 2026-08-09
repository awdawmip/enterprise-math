import unittest

from enterprise_math.scale_tunneling_1d import Wall1D
from enterprise_math.tunneling_phase_diagram import (
    enumerate_positive_clearance_phases,
    tunneling_phase_diagram,
)


class TunnelingPhaseDiagramTests(unittest.TestCase):
    def test_phase_count_matches_explicit_clearance_pairs(self):
        for thickness in range(1, 5):
            wall = Wall1D(0, thickness - 1)
            for radius in range(3):
                effective = thickness + (2 * radius + 1)
                for displacement in range(0, effective + 9):
                    phases = enumerate_positive_clearance_phases(
                        wall, radius, displacement
                    )
                    for factor in range(1, 6):
                        report = tunneling_phase_diagram(
                            wall, radius, displacement, factor
                        )
                        transmitting = [
                            pair
                            for pair in phases
                            if pair[0] >= factor and pair[1] >= factor
                        ]
                        self.assertEqual(
                            report.positive_clearance_crossing_phases,
                            len(phases),
                        )
                        self.assertEqual(report.transmitting_phases, len(transmitting))
                        self.assertEqual(
                            report.macro_contact_phases,
                            len(phases) - len(transmitting),
                        )
                        if transmitting:
                            self.assertEqual(
                                report.transmission_start_clearance_range,
                                (transmitting[0][0], transmitting[-1][0]),
                            )
                        else:
                            self.assertIsNone(
                                report.transmission_start_clearance_range
                            )

    def test_minimum_displacement_for_any_transmission_is_exact(self):
        for thickness in range(1, 6):
            wall = Wall1D(-2, -2 + thickness - 1)
            for radius in range(4):
                effective = thickness + (2 * radius + 1)
                for factor in range(1, 6):
                    threshold = effective + 2 * (factor - 1)
                    below = tunneling_phase_diagram(
                        wall, radius, max(0, threshold - 1), factor
                    )
                    at = tunneling_phase_diagram(
                        wall, radius, threshold, factor
                    )
                    self.assertEqual(
                        at.minimum_displacement_for_any_transmission,
                        threshold,
                    )
                    self.assertEqual(below.transmitting_phases, 0)
                    self.assertEqual(at.transmitting_phases, 1)
                    self.assertEqual(
                        at.transmission_start_clearance_range,
                        (factor, factor),
                    )

    def test_point_wall_phase_diagram(self):
        wall = Wall1D(0, 0)
        # H=T+D=2.  At d=2, displacement 4 is the first one with a
        # transmitting phase: g_pre=g_post=2.
        d2_s3 = tunneling_phase_diagram(wall, 0, 3, 2)
        d2_s4 = tunneling_phase_diagram(wall, 0, 4, 2)
        self.assertEqual(d2_s3.positive_clearance_crossing_phases, 2)
        self.assertEqual(d2_s3.transmitting_phases, 0)
        self.assertEqual(d2_s3.macro_contact_phases, 2)
        self.assertEqual(d2_s4.transmitting_phases, 1)
        self.assertEqual(d2_s4.transmission_start_clearance_range, (2, 2))

    def test_terminal_factor_transmits_every_positive_clearance_crossing_phase(self):
        wall = Wall1D(0, 3)
        for radius in range(3):
            effective = wall.thickness_cells + (2 * radius + 1)
            for displacement in range(effective, effective + 10):
                report = tunneling_phase_diagram(wall, radius, displacement, 1)
                self.assertEqual(
                    report.transmitting_phases,
                    report.positive_clearance_crossing_phases,
                )
                self.assertEqual(report.macro_contact_phases, 0)

    def test_refinement_monotonically_increases_transmitting_phase_count(self):
        wall = Wall1D(0, 2)
        radius = 1
        displacement = 14
        counts = [
            tunneling_phase_diagram(wall, radius, displacement, factor).transmitting_phases
            for factor in range(6, 0, -1)
        ]
        self.assertEqual(counts, sorted(counts))

    def test_coarsening_removes_two_transmitting_phases_per_factor_until_zero(self):
        wall = Wall1D(0, 0)
        radius = 0
        displacement = 10
        reports = [
            tunneling_phase_diagram(wall, radius, displacement, factor)
            for factor in range(1, 6)
        ]
        positive = reports[0].positive_clearance_crossing_phases
        for report in reports:
            self.assertEqual(
                report.transmitting_phases,
                max(0, positive - 2 * (report.collapse_factor - 1)),
            )

    def test_invalid_inputs_are_rejected(self):
        wall = Wall1D(0, 0)
        with self.assertRaises(ValueError):
            tunneling_phase_diagram(wall, -1, 2, 1)
        with self.assertRaises(ValueError):
            tunneling_phase_diagram(wall, 0, -1, 1)
        with self.assertRaises(ValueError):
            tunneling_phase_diagram(wall, 0, 2, 0)


if __name__ == "__main__":
    unittest.main()
