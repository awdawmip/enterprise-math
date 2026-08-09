import unittest
from itertools import product

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
)
from enterprise_math.material_contact_passivity_precision import (
    minimum_single_contact_passivity_from_network,
)
from enterprise_math.material_weighted_path_plastic_precision import (
    exact_plastic_response_at_refinement,
    weighted_path_plastic_precision_report,
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


class MaterialWeightedPathPlasticPrecisionTests(unittest.TestCase):
    def test_three_body_fractional_consensus_has_exact_denominator_three(self):
        state = path_state((1, 1, 1), (2, 0, 0))
        report = weighted_path_plastic_precision_report(state)
        self.assertEqual(report.total_mass, 3)
        self.assertEqual(report.total_momentum, 2)
        self.assertEqual(report.prefix_mass_momentum_numerators, (4, 2))
        self.assertEqual(report.gcd_resource, 1)
        self.assertEqual(report.minimum_exact_denominator, 3)
        self.assertEqual(report.exact_impulse_numerators, (4, 2))
        self.assertEqual(report.final_momentum_numerators, (2, 2, 2))
        self.assertEqual(report.final_contact_score_numerators, (0, 0))
        self.assertEqual(report.kinetic_change_numerator, -24)
        self.assertTrue(report.passive)

    def test_passive_denominator_can_precede_exact_zero_score_plastic_denominator(self):
        state = path_state((1, 2), (-1, -3))
        plastic = weighted_path_plastic_precision_report(state)
        passive = minimum_single_contact_passivity_from_network(state, 2)
        self.assertEqual(passive.minimum_passive_denominator, 2)
        self.assertTrue(passive.passive)
        self.assertEqual(plastic.minimum_exact_denominator, 3)
        self.assertEqual(plastic.exact_impulse_numerators, (1,))
        self.assertEqual(plastic.final_momentum_numerators, (-4, -8))
        self.assertEqual(plastic.kinetic_change_numerator, -3)
        self.assertLess(
            passive.minimum_passive_denominator,
            plastic.minimum_exact_denominator,
        )

    def test_integer_closed_path_needs_no_denominator_refinement(self):
        state = path_state((1, 2, 1), (4, 4, 0))
        report = weighted_path_plastic_precision_report(state)
        self.assertEqual(report.minimum_exact_denominator, 1)
        self.assertEqual(report.gcd_resource, 4)
        self.assertEqual(report.exact_impulse_numerators, (2, 2))
        self.assertEqual(report.final_momentum_numerators, (2, 4, 2))
        self.assertEqual(report.final_contact_score_numerators, (0, 0))

    def test_true_divisibility_refinements_are_exact_scaled_copies(self):
        state = path_state((1, 1, 1), (2, 0, 0))
        base = weighted_path_plastic_precision_report(state)
        for multiplier in range(1, 8):
            denominator, impulses = exact_plastic_response_at_refinement(
                state, multiplier
            )
            self.assertEqual(
                denominator,
                base.minimum_exact_denominator * multiplier,
            )
            self.assertEqual(
                impulses,
                tuple(multiplier * value for value in base.exact_impulse_numerators),
            )
            scaled = path_state(
                state.masses,
                tuple(denominator * value for value in state.momenta),
            )
            step = apply_contact_impulse_vector(scaled, impulses)
            self.assertTrue(all(score == 0 for score in step.relative_scores_after))

    def test_no_smaller_denominator_can_make_every_exact_prefix_transfer_integral(self):
        examples = (
            path_state((1, 1, 1), (2, 0, 0)),
            path_state((1, 2), (-1, -3)),
            path_state((2, 3, 5), (5, 3, 0)),
        )
        for state in examples:
            report = weighted_path_plastic_precision_report(state)
            for denominator in range(1, report.minimum_exact_denominator):
                self.assertTrue(
                    any(
                        denominator * numerator % report.total_mass != 0
                        for numerator in report.prefix_mass_momentum_numerators
                    )
                )

    def test_already_comoving_path_has_denominator_one_and_zero_impulse(self):
        state = path_state((1, 2, 3), (2, 4, 6))
        report = weighted_path_plastic_precision_report(state)
        self.assertEqual(report.minimum_exact_denominator, 1)
        self.assertEqual(report.exact_impulse_numerators, (0, 0))
        self.assertEqual(report.kinetic_change_numerator, 0)
        self.assertEqual(report.final_momentum_numerators, state.momenta)

    def test_bounded_closing_paths_preserve_exact_gcd_and_zero_score_claim(self):
        masses = (1, 2, 1)
        contacts = (ContactChannel1D(0, 1), ContactChannel1D(1, 2))
        checked = 0
        for momenta in product(range(-3, 4), repeat=3):
            state = ContactNetworkMomentum1D(masses, momenta, contacts)
            # Closing means scaled velocities are non-increasing: 2*p0 >= p1 >= 2*p2.
            if not (2 * momenta[0] >= momenta[1] >= 2 * momenta[2]):
                continue
            report = weighted_path_plastic_precision_report(state)
            checked += 1
            self.assertTrue(all(score == 0 for score in report.final_contact_score_numerators))
            self.assertLessEqual(report.kinetic_change_numerator, 0)
            for numerator in report.prefix_mass_momentum_numerators:
                self.assertEqual(
                    report.minimum_exact_denominator * numerator
                    % report.total_mass,
                    0,
                )
        self.assertGreater(checked, 0)

    def test_separating_or_nonpath_state_is_rejected(self):
        separating = path_state((1, 1), (0, 1))
        with self.assertRaises(ValueError):
            weighted_path_plastic_precision_report(separating)

        nonpath = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(2, 1, 0),
            contacts=(ContactChannel1D(0, 2), ContactChannel1D(1, 2)),
        )
        with self.assertRaises(ValueError):
            weighted_path_plastic_precision_report(nonpath)


if __name__ == "__main__":
    unittest.main()
