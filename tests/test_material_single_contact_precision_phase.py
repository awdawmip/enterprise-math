import unittest

from enterprise_math.material_single_contact_precision_phase import (
    ACTIVE_ARTIFACT,
    CAPACITY_DEFICIT,
    EXACT_PLASTIC,
    PASSIVE_OVERSHOOT,
    single_contact_precision_phase_report,
)


class MaterialSingleContactPrecisionPhaseTests(unittest.TestCase):
    def test_q1_k3_sequence_separates_passivity_threshold_from_plastic_sublattice(self):
        phases = [
            single_contact_precision_phase_report(1, 3, denominator, 10).phase
            for denominator in range(1, 7)
        ]
        self.assertEqual(
            phases,
            [
                ACTIVE_ARTIFACT,
                PASSIVE_OVERSHOOT,
                EXACT_PLASTIC,
                PASSIVE_OVERSHOOT,
                PASSIVE_OVERSHOOT,
                EXACT_PLASTIC,
            ],
        )
        first = single_contact_precision_phase_report(1, 3, 1, 10)
        self.assertEqual(first.minimum_passive_denominator, 2)
        self.assertEqual(first.exact_plastic_base_denominator, 3)

    def test_material_capacity_deficit_precedes_other_physical_classification(self):
        report = single_contact_precision_phase_report(
            closing_score=3,
            self_coupling=5,
            denominator=4,
            material_capacity_numerator=2,
        )
        self.assertEqual(report.minimum_required_impulse_numerator, 3)
        self.assertEqual(report.phase, CAPACITY_DEFICIT)
        self.assertFalse(report.capacity_sufficient)
        self.assertFalse(report.passive)

    def test_exact_plastic_denominators_are_exactly_one_divisibility_sublattice(self):
        for q in range(1, 12):
            for coupling in range(1, 15):
                base = coupling // __import__("math").gcd(coupling, q)
                for denominator in range(1, 30):
                    report = single_contact_precision_phase_report(
                        q,
                        coupling,
                        denominator,
                        material_capacity_numerator=1000,
                    )
                    self.assertEqual(report.exact_plastic_base_denominator, base)
                    self.assertEqual(
                        report.phase == EXACT_PLASTIC,
                        denominator % base == 0,
                    )

    def test_every_sufficiently_large_denominator_is_passive_even_between_plastic_gates(self):
        for q in range(1, 10):
            for coupling in range(1, 15):
                threshold = (coupling + 2 * q - 1) // (2 * q)
                for denominator in range(threshold, threshold + 20):
                    report = single_contact_precision_phase_report(
                        q, coupling, denominator, 1000
                    )
                    self.assertNotEqual(report.phase, ACTIVE_ARTIFACT)
                    self.assertTrue(report.passive)
                    self.assertIn(report.phase, (PASSIVE_OVERSHOOT, EXACT_PLASTIC))

    def test_energy_neutral_overshoot_can_occur_at_first_passive_gate(self):
        report = single_contact_precision_phase_report(1, 2, 1, 1)
        self.assertEqual(report.phase, PASSIVE_OVERSHOOT)
        self.assertEqual(report.kinetic_energy_change_numerator, 0)
        self.assertEqual(report.final_score_numerator, 1)
        self.assertTrue(report.passive)
        self.assertEqual(report.exact_plastic_base_denominator, 2)

    def test_invalid_capacity_is_rejected(self):
        with self.assertRaises(ValueError):
            single_contact_precision_phase_report(1, 2, 1, -1)


if __name__ == "__main__":
    unittest.main()
