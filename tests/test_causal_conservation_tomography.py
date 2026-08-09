import unittest

from enterprise_math.causal_conservation_tomography import (
    accepted_support_histogram,
    exact_total_law,
    exact_vs_modular_tomography_order,
    first_distinguishing_event,
    first_distinguishing_support,
    laws_agree_through_support,
    modular_pair_tomography_order,
    modular_total_law,
    support_size,
    unconstrained_law,
)


class CausalConservationTomographyTests(unittest.TestCase):
    def test_unconstrained_and_nontrivial_modular_laws_split_at_support_one(self):
        for modulus in range(2, 7):
            self.assertEqual(
                first_distinguishing_support(
                    8, unconstrained_law, modular_total_law(modulus)
                ),
                1,
            )

    def test_mod_two_and_mod_three_plus_split_at_support_two(self):
        for modulus in range(3, 8):
            self.assertEqual(modular_pair_tomography_order(10, 2, modulus), 2)

    def test_exact_and_mod_m_are_identical_below_m_then_split_at_m(self):
        for modulus in range(3, 8):
            slots = modulus + 2
            self.assertTrue(
                laws_agree_through_support(
                    slots,
                    exact_total_law,
                    modular_total_law(modulus),
                    modulus - 1,
                )
            )
            self.assertEqual(exact_vs_modular_tomography_order(slots, modulus), modulus)
            witness = first_distinguishing_event(
                slots, exact_total_law, modular_total_law(modulus)
            )
            self.assertIsNotNone(witness)
            self.assertEqual(support_size(witness), modulus)
            self.assertNotEqual(exact_total_law(witness), modular_total_law(modulus)(witness))

    def test_distinct_moduli_first_split_at_smaller_modulus_when_slots_allow(self):
        for left, right in ((3, 4), (3, 6), (4, 7), (5, 8), (6, 9)):
            slots = max(left, right) + 1
            self.assertEqual(
                modular_pair_tomography_order(slots, left, right),
                min(left, right),
            )

    def test_support_count_shadow_is_weaker_than_exact_event_family(self):
        # Histograms are useful shadows, but tomography equality is defined by the
        # accepted event sets, not by support counts alone.
        exact_hist = accepted_support_histogram(5, exact_total_law)
        mod3_hist = accepted_support_histogram(5, modular_total_law(3))
        self.assertEqual(exact_hist[:2], mod3_hist[:2])
        self.assertNotEqual(exact_hist[2], mod3_hist[2])


if __name__ == "__main__":
    unittest.main()
