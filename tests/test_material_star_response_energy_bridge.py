import unittest

from enterprise_math.material_star_response_energy_bridge import (
    star_equal_mass_kinetic_change_numerator,
    star_minimum_energy_spectrum,
)
from enterprise_math.material_star_response_precision_phase import (
    star_minimum_response_relation_at_precision,
)


class MaterialStarResponseEnergyBridgeTests(unittest.TestCase):
    def test_k3_q1_s3_contains_energy_neutral_and_more_dissipative_minima(self):
        report = star_minimum_energy_spectrum(3, 1, 3)
        self.assertEqual(report.quotient_baseline, 0)
        self.assertEqual(report.residue, 3)
        self.assertEqual(report.minimum_total_impulse_numerator, 3)
        self.assertEqual(report.response_relation_cardinality, 10)
        self.assertEqual(report.least_dissipative_change_numerator, 0)
        self.assertEqual(report.most_dissipative_change_numerator, -6)
        self.assertEqual(report.energy_spectrum_width, 6)
        self.assertFalse(report.energy_unique_across_minimum_relation)
        self.assertTrue(report.all_minimum_responses_passive)
        self.assertEqual(report.symmetric_minimum_energy_change_numerator, -6)
        self.assertTrue(report.symmetric_minimum_is_most_dissipative)
        self.assertEqual(
            star_equal_mass_kinetic_change_numerator((3, 0, 0), 1, 3),
            0,
        )
        self.assertEqual(
            star_equal_mass_kinetic_change_numerator((1, 1, 1), 1, 3),
            -6,
        )

    def test_zero_residue_gate_is_unique_and_strictly_dissipative(self):
        report = star_minimum_energy_spectrum(3, 1, 4)
        self.assertEqual(report.residue, 0)
        self.assertEqual(report.response_relation_cardinality, 1)
        self.assertEqual(report.energy_spectrum_width, 0)
        self.assertTrue(report.energy_unique_across_minimum_relation)
        self.assertEqual(report.energy_bins[0].kinetic_change_numerator, -12)
        self.assertEqual(report.energy_bins[0].response_count, 1)
        self.assertTrue(report.symmetric_minimum_is_most_dissipative)

    def test_residue_one_can_have_response_ambiguity_without_energy_ambiguity(self):
        # k=3,q=1,s=1: three unit-vector minima, all related by leaf permutation.
        report = star_minimum_energy_spectrum(3, 1, 1)
        self.assertEqual(report.residue, 1)
        self.assertEqual(report.response_relation_cardinality, 3)
        self.assertTrue(report.energy_unique_across_minimum_relation)
        self.assertEqual(report.energy_spectrum_width, 0)
        self.assertEqual(len(report.energy_bins), 1)
        self.assertEqual(report.energy_bins[0].kinetic_change_numerator, 0)
        self.assertEqual(report.energy_bins[0].response_count, 3)

    def test_energy_ambiguity_is_exactly_residue_r_r_minus_one(self):
        for leaf_count in range(2, 7):
            for closing_quantum in range(1, 5):
                for denominator in range(1, 10):
                    report = star_minimum_energy_spectrum(
                        leaf_count,
                        closing_quantum,
                        denominator,
                    )
                    self.assertEqual(
                        report.energy_spectrum_width,
                        report.residue * (report.residue - 1),
                    )
                    self.assertEqual(
                        report.energy_unique_across_minimum_relation,
                        report.residue in (0, 1),
                    )
                    self.assertTrue(report.all_minimum_responses_passive)
                    self.assertLessEqual(
                        report.most_dissipative_change_numerator,
                        report.least_dissipative_change_numerator,
                    )
                    self.assertLessEqual(report.least_dissipative_change_numerator, 0)

    def test_report_bins_match_independent_relation_enumeration(self):
        for leaf_count in range(2, 5):
            for q in range(1, 4):
                for denominator in range(1, 6):
                    relation = star_minimum_response_relation_at_precision(
                        leaf_count, q, denominator
                    )
                    direct = sorted(
                        star_equal_mass_kinetic_change_numerator(
                            vector, q, denominator
                        )
                        for vector in relation
                    )
                    report = star_minimum_energy_spectrum(
                        leaf_count, q, denominator
                    )
                    expanded = sorted(
                        value
                        for item in report.energy_bins
                        for value in [item.kinetic_change_numerator] * item.response_count
                    )
                    self.assertEqual(expanded, direct)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            star_minimum_energy_spectrum(1, 1, 1)
        with self.assertRaises(ValueError):
            star_minimum_energy_spectrum(3, 0, 1)
        with self.assertRaises(ValueError):
            star_minimum_energy_spectrum(3, 1, 0)
        with self.assertRaises(ValueError):
            star_equal_mass_kinetic_change_numerator((1,), 1, 1)
        with self.assertRaises(ValueError):
            star_equal_mass_kinetic_change_numerator((1, -1), 1, 1)


if __name__ == "__main__":
    unittest.main()
