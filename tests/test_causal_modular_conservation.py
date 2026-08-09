import unittest

from enterprise_math.causal_modular_conservation import (
    exact_and_modular_agree_below_support,
    first_exact_total_changing_support,
    minimum_modular_events,
    primitive_geometry_family,
    support_size,
)


class CausalModularConservationTests(unittest.TestCase):
    def test_modulus_one_two_and_three_plus_give_z_d_a_primitive_families(self):
        self.assertEqual(primitive_geometry_family(1), "Z")
        self.assertEqual(primitive_geometry_family(2), "D")
        for modulus in range(3, 10):
            self.assertEqual(primitive_geometry_family(modulus), "A")

    def test_minimum_event_support_and_counts_follow_z_d_a_split(self):
        slots = 6
        m1 = minimum_modular_events(slots, 1)
        m2 = minimum_modular_events(slots, 2)
        m5 = minimum_modular_events(slots, 5)
        self.assertEqual({support_size(event) for event in m1}, {1})
        self.assertEqual({support_size(event) for event in m2}, {2})
        self.assertEqual({support_size(event) for event in m5}, {2})
        self.assertEqual(len(m1), 2 * slots)
        self.assertEqual(len(m2), 2 * slots * (slots - 1))
        self.assertEqual(len(m5), slots * (slots - 1))

    def test_mod_m_and_exact_conservation_agree_at_all_supports_below_m(self):
        for modulus in range(3, 8):
            slots = modulus + 2
            self.assertTrue(
                exact_and_modular_agree_below_support(
                    slots,
                    modulus,
                    support_bound=modulus,
                )
            )

    def test_first_modular_event_that_changes_exact_total_has_support_m(self):
        for modulus in range(3, 8):
            slots = modulus + 1
            self.assertEqual(
                first_exact_total_changing_support(slots, modulus),
                modulus,
            )

    def test_when_slots_are_too_few_modular_and_exact_unit_languages_can_be_identical(self):
        self.assertIsNone(first_exact_total_changing_support(3, 5))
        self.assertTrue(exact_and_modular_agree_below_support(3, 5, 4))


if __name__ == "__main__":
    unittest.main()
