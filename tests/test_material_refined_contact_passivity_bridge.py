import unittest
from itertools import product

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
)
from enterprise_math.material_refined_contact_passivity_bridge import (
    refined_contact_passivity_report,
)
from enterprise_math.material_star_response_energy_bridge import (
    star_minimum_energy_spectrum,
)
from enterprise_math.material_star_response_precision_phase import (
    star_symmetric_minimum_numerators,
)


def path_state(momentum):
    return ContactNetworkMomentum1D(
        masses=(1, 1, 1),
        momenta=tuple(momentum),
        contacts=(ContactChannel1D(0, 1), ContactChannel1D(1, 2)),
    )


class RefinedContactPassivityBridgeTests(unittest.TestCase):
    def test_nonclosing_multi_contact_response_can_still_inject_energy(self):
        state = path_state((-1, -2, -3))
        report = refined_contact_passivity_report(
            state,
            momentum_denominator=1,
            momentum_detail_numerators=(0, 0, 0),
            impulse_numerators=(2, 3),
            impulse_denominators=(1, 1),
        )
        self.assertEqual(report.bridge.contact_score_numerators_before, (-1, -1))
        self.assertEqual(report.bridge.contact_score_numerators_after, (0, 3))
        self.assertTrue(report.all_contacts_nonclosing)
        self.assertEqual(report.kinetic_change_numerator, 4)
        self.assertFalse(report.globally_passive)
        self.assertFalse(report.contactwise_passive_envelope)

    def test_local_overshoot_can_be_offset_by_dissipation_elsewhere(self):
        state = path_state((0, -2, -3))
        report = refined_contact_passivity_report(
            state, 1, (0, 0, 0), (3, 3), (1, 1)
        )
        self.assertEqual(report.bridge.contact_score_numerators_before, (-2, -1))
        self.assertEqual(report.bridge.contact_score_numerators_after, (1, 2))
        self.assertTrue(report.all_contacts_nonclosing)
        self.assertEqual(report.kinetic_change_numerator, 0)
        self.assertTrue(report.globally_passive)
        self.assertFalse(report.contactwise_passive_envelope)

    def test_contactwise_overshoot_bound_is_a_sufficient_global_certificate(self):
        state = path_state((2, 0, -2))
        report = refined_contact_passivity_report(
            state, 1, (0, 0, 0), (2, 2), (1, 1)
        )
        self.assertEqual(report.bridge.contact_score_numerators_before, (-2, -2))
        self.assertEqual(report.bridge.contact_score_numerators_after, (0, 0))
        self.assertTrue(report.contactwise_passive_envelope)
        self.assertTrue(report.globally_passive)
        self.assertEqual(report.kinetic_change_numerator, -8)

    def test_refined_symmetric_star_energy_matches_star_energy_spectrum(self):
        contacts = tuple(ContactChannel1D(0, leaf) for leaf in (1, 2, 3))
        state = ContactNetworkMomentum1D(
            masses=(1, 1, 1, 1),
            momenta=(1, 0, 0, 0),
            contacts=contacts,
        )
        impulse = star_symmetric_minimum_numerators(3, 1, 3)
        self.assertEqual(impulse, (1, 1, 1))
        report = refined_contact_passivity_report(
            state, 1, (0, 0, 0, 0), impulse, (3, 3, 3)
        )
        spectrum = star_minimum_energy_spectrum(3, 1, 3)
        self.assertEqual(report.kinetic_change_numerator, -6)
        self.assertEqual(
            report.kinetic_change_numerator,
            spectrum.symmetric_minimum_energy_change_numerator,
        )
        self.assertTrue(report.globally_passive)
        self.assertTrue(report.all_contacts_nonclosing)

    def test_three_exact_energy_forms_agree_over_bounded_path_states(self):
        contacts = (ContactChannel1D(0, 1), ContactChannel1D(1, 2))
        for momentum in product(range(-2, 3), repeat=3):
            state = ContactNetworkMomentum1D(
                masses=(1, 1, 1),
                momenta=momentum,
                contacts=contacts,
            )
            for impulses in product(range(3), repeat=2):
                report = refined_contact_passivity_report(
                    state,
                    momentum_denominator=2,
                    momentum_detail_numerators=(0, 0, 0),
                    impulse_numerators=impulses,
                    impulse_denominators=(2, 2),
                )
                self.assertEqual(
                    report.kinetic_change_numerator,
                    report.linear_plus_quadratic_change_numerator,
                )
                self.assertEqual(
                    report.kinetic_change_numerator,
                    report.score_pairing_change_numerator,
                )
                if report.contactwise_passive_envelope:
                    self.assertTrue(report.globally_passive)


if __name__ == "__main__":
    unittest.main()
