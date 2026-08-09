import unittest

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
)
from enterprise_math.material_contact_passivity_precision import (
    minimum_single_contact_passivity_from_network,
    minimum_single_contact_passivity_report,
)


class MaterialContactPassivityPrecisionTests(unittest.TestCase):
    def test_unequal_mass_coarse_minimum_can_inject_energy_then_refinement_restores_passivity(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 2),
            momenta=(-1, -3),
            contacts=(ContactChannel1D(0, 1),),
        )
        coarse = minimum_single_contact_passivity_from_network(state, 1)
        fine = minimum_single_contact_passivity_from_network(state, 2)
        self.assertEqual(coarse.closing_score, 1)
        self.assertEqual(coarse.self_coupling, 3)
        self.assertEqual(coarse.minimum_passive_denominator, 2)
        self.assertEqual(coarse.minimum_impulse_numerator, 1)
        self.assertEqual(coarse.final_score_numerator, 2)
        self.assertEqual(coarse.kinetic_energy_change_numerator, 1)
        self.assertFalse(coarse.passive)
        self.assertTrue(coarse.active_precision_artifact)

        self.assertEqual(fine.minimum_impulse_numerator, 1)
        self.assertEqual(fine.final_score_numerator, 1)
        self.assertEqual(fine.kinetic_energy_change_numerator, -1)
        self.assertTrue(fine.passive)

    def test_equal_mass_unit_closing_contact_is_energy_neutral_on_integer_lattice(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 1),
            momenta=(1, 0),
            contacts=(ContactChannel1D(0, 1),),
        )
        report = minimum_single_contact_passivity_from_network(state, 1)
        self.assertEqual(report.closing_score, 1)
        self.assertEqual(report.self_coupling, 2)
        self.assertEqual(report.minimum_passive_denominator, 1)
        self.assertEqual(report.kinetic_energy_change_numerator, 0)
        self.assertTrue(report.passive)

    def test_exact_threshold_matches_direct_formula_over_bounded_integer_domain(self):
        for closing_score in range(1, 20):
            for coupling in range(1, 25):
                threshold = (coupling + 2 * closing_score - 1) // (2 * closing_score)
                for denominator in range(1, 20):
                    report = minimum_single_contact_passivity_report(
                        closing_score,
                        coupling,
                        denominator,
                    )
                    expected_impulse = (
                        closing_score * denominator + coupling - 1
                    ) // coupling
                    expected_energy = expected_impulse * (
                        coupling * expected_impulse
                        - 2 * closing_score * denominator
                    )
                    self.assertEqual(report.minimum_impulse_numerator, expected_impulse)
                    self.assertEqual(report.kinetic_energy_change_numerator, expected_energy)
                    self.assertEqual(report.passive, expected_energy <= 0)
                    self.assertEqual(report.passive, denominator >= threshold)
                    self.assertEqual(report.minimum_passive_denominator, threshold)

    def test_final_score_overshoot_and_energy_identity_share_same_impulse(self):
        for q in range(1, 8):
            for coupling in range(1, 10):
                for denominator in range(1, 8):
                    report = minimum_single_contact_passivity_report(
                        q, coupling, denominator
                    )
                    impulse = report.minimum_impulse_numerator
                    self.assertEqual(
                        report.final_score_numerator,
                        -q * denominator + coupling * impulse,
                    )
                    self.assertEqual(
                        report.kinetic_energy_change_numerator,
                        impulse * (-q * denominator + report.final_score_numerator),
                    )
                    self.assertTrue(0 <= report.final_score_numerator < coupling)

    def test_invalid_or_nonclosing_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            minimum_single_contact_passivity_report(0, 2, 1)
        with self.assertRaises(ValueError):
            minimum_single_contact_passivity_report(1, 0, 1)
        with self.assertRaises(ValueError):
            minimum_single_contact_passivity_report(1, 2, 0)

        separating = ContactNetworkMomentum1D(
            masses=(1, 1),
            momenta=(0, 1),
            contacts=(ContactChannel1D(0, 1),),
        )
        with self.assertRaises(ValueError):
            minimum_single_contact_passivity_from_network(separating, 1)


if __name__ == "__main__":
    unittest.main()
