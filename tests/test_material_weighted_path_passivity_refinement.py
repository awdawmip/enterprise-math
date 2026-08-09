import unittest
from itertools import product

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
)
from enterprise_math.material_weighted_path_passivity_refinement import (
    weighted_path_passivity_refinement_report,
)


def path_state(masses, momenta):
    return ContactNetworkMomentum1D(
        masses=tuple(masses),
        momenta=tuple(momenta),
        contacts=tuple(
            ContactChannel1D(index, index + 1)
            for index in range(len(masses) - 1)
        ),
    )


class MaterialWeightedPathPassivityRefinementTests(unittest.TestCase):
    def test_true_refinement_can_remove_a_coarse_active_artifact(self):
        state = path_state((1, 1, 2), (-1, -1, -3))
        report = weighted_path_passivity_refinement_report(state, 1, 2)
        self.assertEqual(report.coarse_impulse_numerators, (1, 1))
        self.assertEqual(report.coarse_kinetic_change_numerator, 1)
        self.assertFalse(report.coarse_passive)
        self.assertEqual(report.fine_impulse_numerators, (1, 2))
        self.assertEqual(report.fine_kinetic_change_numerator, 0)
        self.assertTrue(report.fine_passive)
        self.assertTrue(report.normalized_change_cross_inequality_holds)

    def test_once_passive_a_path_cannot_become_active_on_a_divisibility_refinement(self):
        state = path_state((1, 2), (-1, -3))
        for coarse_denominator in (2, 3, 4, 6):
            for multiplier in (2, 3, 5):
                report = weighted_path_passivity_refinement_report(
                    state, coarse_denominator, multiplier
                )
                self.assertTrue(report.coarse_passive)
                self.assertTrue(report.fine_passive)
                self.assertLessEqual(
                    report.fine_kinetic_change_numerator,
                    multiplier * multiplier * report.coarse_kinetic_change_numerator,
                )

    def test_exact_plastic_refinement_preserves_normalized_kinetic_change_exactly(self):
        state = path_state((1, 1, 1), (2, 0, 0))
        report = weighted_path_passivity_refinement_report(state, 3, 4)
        self.assertEqual(report.coarse_final_score_numerators, (0, 0))
        self.assertEqual(report.fine_final_score_numerators, (0, 0))
        self.assertEqual(
            report.fine_impulse_numerators,
            tuple(4 * value for value in report.coarse_impulse_numerators),
        )
        self.assertEqual(
            report.fine_kinetic_change_numerator,
            16 * report.coarse_kinetic_change_numerator,
        )

    def test_fine_least_response_is_componentwise_below_scaled_coarse_witness(self):
        state = path_state((1, 2, 1), (4, 4, 0))
        for coarse_denominator in range(1, 5):
            for multiplier in (2, 3):
                report = weighted_path_passivity_refinement_report(
                    state, coarse_denominator, multiplier
                )
                self.assertTrue(
                    all(
                        fine <= scaled
                        for fine, scaled in zip(
                            report.fine_impulse_numerators,
                            report.scaled_coarse_impulse_numerators,
                        )
                    )
                )

    def test_bounded_weighted_paths_show_no_passivity_regression_on_true_refinement(self):
        checked = 0
        mass_sets = ((1, 1, 1), (1, 2, 1), (1, 1, 2), (2, 3, 1))
        for masses in mass_sets:
            # Closing path condition is checked by the owner solver; skip states
            # rejected for having a separating contact.
            for momenta in product(range(-2, 3), repeat=3):
                state = path_state(masses, momenta)
                for coarse_denominator in (1, 2, 3):
                    for multiplier in (2, 3):
                        try:
                            report = weighted_path_passivity_refinement_report(
                                state,
                                coarse_denominator,
                                multiplier,
                            )
                        except ValueError:
                            continue
                        checked += 1
                        self.assertTrue(report.normalized_change_cross_inequality_holds)
                        if report.coarse_passive:
                            self.assertTrue(report.fine_passive)
        self.assertGreater(checked, 100)

    def test_invalid_refinement_arguments_are_rejected(self):
        state = path_state((1, 1), (1, 0))
        with self.assertRaises(ValueError):
            weighted_path_passivity_refinement_report(state, 0, 2)
        with self.assertRaises(ValueError):
            weighted_path_passivity_refinement_report(state, 1, 0)


if __name__ == "__main__":
    unittest.main()
