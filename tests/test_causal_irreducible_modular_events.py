import unittest
from math import comb

from enterprise_math.causal_irreducible_modular_events import (
    conformally_decomposable,
    irreducible_closed_form_identity,
    irreducible_modular_events,
    irreducible_support_histogram,
    modular_allowed,
    support_size,
)


class CausalIrreducibleModularEventsTests(unittest.TestCase):
    def test_closed_form_matches_direct_conformal_decomposition_small_systems(self):
        for slots in range(2, 7):
            for modulus in range(1, 6):
                self.assertTrue(irreducible_closed_form_identity(slots, modulus))

    def test_mod_one_has_only_single_slot_irreducibles(self):
        slots = 5
        self.assertEqual(irreducible_support_histogram(slots, 1), {1: 2 * slots})

    def test_mod_two_has_exact_d_n_support_two_irreducibles(self):
        slots = 5
        self.assertEqual(
            irreducible_support_histogram(slots, 2),
            {2: 2 * slots * (slots - 1)},
        )

    def test_mod_three_plus_has_transfer_shell_and_m_body_creation_annihilation(self):
        for modulus in range(3, 6):
            slots = 6
            expected = {2: slots * (slots - 1)}
            if slots >= modulus:
                expected[modulus] = 2 * comb(slots, modulus)
            self.assertEqual(irreducible_support_histogram(slots, modulus), expected)

    def test_m_body_all_plus_event_is_allowed_irreducible_and_distinguishes_exact_law(self):
        modulus = 4
        event = (1, 1, 1, 1, 0)
        self.assertTrue(modular_allowed(event, modulus))
        self.assertFalse(conformally_decomposable(event, modulus))
        self.assertEqual(support_size(event), modulus)
        self.assertNotEqual(sum(event), 0)

    def test_larger_mixed_modular_events_decompose_into_m_body_and_transfers(self):
        event = (1, 1, 1, 1, -1, 1)  # sum=4 mod 4, support 6
        self.assertTrue(modular_allowed(event, 4))
        self.assertTrue(conformally_decomposable(event, 4))
        self.assertNotIn(event, irreducible_modular_events(6, 4))


if __name__ == "__main__":
    unittest.main()
