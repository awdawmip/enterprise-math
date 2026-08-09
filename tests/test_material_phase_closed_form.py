import unittest
from itertools import product

from enterprise_math.material_phase_closed_form import (
    closed_form_material_phase_mass,
    closed_form_wall_phase_mass,
    minimum_gap_range_phase_count,
)
from enterprise_math.material_phase_spectrum import material_phase_spectrum
from enterprise_math.material_response import (
    explicit_material_curve_profile,
    material_curve_profile,
)
from enterprise_math.scale_tunneling_1d import Wall1D


class MaterialPhaseClosedFormTests(unittest.TestCase):
    def setUp(self):
        self.wall = Wall1D(0, 0)
        self.profile = explicit_material_curve_profile(
            loading=(0, 0, 100, 200, 400),
            returning=(0, 0, 100, 200, 400),
            amplitude=400,
        )

    def test_minimum_gap_interval_formula_matches_direct_positive_pairs(self):
        for clearance_sum in range(2, 20):
            pairs = [
                (left, clearance_sum - left)
                for left in range(1, clearance_sum)
            ]
            for lower in range(1, 10):
                for upper in range(lower, 10):
                    direct = sum(
                        lower <= min(left, right) <= upper
                        for left, right in pairs
                    )
                    self.assertEqual(
                        minimum_gap_range_phase_count(clearance_sum, lower, upper),
                        direct,
                    )

    def test_transmission_and_interaction_have_exact_high_speed_closed_forms(self):
        full = material_curve_profile(
            tuple(range(0, 21)),
            amplitude=20,
            loading_power=1,
            return_power=1,
        )
        for clearance_sum in range(2, 30):
            for d in range(1, 10):
                report = closed_form_material_phase_mass(
                    clearance_sum, d, 20, full
                )
                self.assertEqual(
                    report.transmitting_phases,
                    max(0, clearance_sum - 2 * d + 1),
                )
                self.assertEqual(
                    report.interaction_phases,
                    min(clearance_sum - 1, 2 * (d - 1)),
                )

    def test_closed_form_four_way_mass_matches_enumerated_phase_spectrum(self):
        for displacement in range(2, 18):
            for d in range(1, 9):
                for budget in range(0, 8):
                    enumerated = material_phase_spectrum(
                        self.wall,
                        0,
                        displacement,
                        d,
                        budget,
                        self.profile,
                    )
                    closed = closed_form_wall_phase_mass(
                        self.wall,
                        0,
                        displacement,
                        d,
                        budget,
                        self.profile,
                    )
                    if enumerated.positive_clearance_phases == 0:
                        self.assertIsNone(closed)
                        continue
                    self.assertIsNotNone(closed)
                    self.assertEqual(closed.positive_clearance_phases, enumerated.positive_clearance_phases)
                    self.assertEqual(closed.transmitting_phases, enumerated.transmitting_phases)
                    self.assertEqual(closed.underresolved_phases, enumerated.underresolved_phases)
                    self.assertEqual(closed.zero_return_phases, enumerated.zero_return_phases)
                    self.assertEqual(closed.rebound_phases, enumerated.rebound_phases)

    def test_phase_mass_conservation_on_small_monotone_profiles(self):
        samples = range(0, 4)
        for returning_tail in product(samples, repeat=3):
            returning = (0,) + returning_tail
            if tuple(returning) != tuple(sorted(returning)):
                continue
            profile = explicit_material_curve_profile(
                loading=returning,
                returning=returning,
                amplitude=3,
            )
            for clearance_sum in range(2, 10):
                for d in range(1, 7):
                    for budget in range(0, 5):
                        report = closed_form_material_phase_mass(
                            clearance_sum, d, budget, profile
                        )
                        self.assertEqual(
                            report.transmitting_phases
                            + report.underresolved_phases
                            + report.zero_return_phases
                            + report.rebound_phases,
                            report.positive_clearance_phases,
                        )

    def test_nonmonotone_profile_is_rejected(self):
        nonmonotone = explicit_material_curve_profile(
            loading=(0, 2, 1),
            returning=(0, 2, 1),
            amplitude=2,
        )
        with self.assertRaises(ValueError):
            closed_form_material_phase_mass(8, 4, 4, nonmonotone)


if __name__ == "__main__":
    unittest.main()
