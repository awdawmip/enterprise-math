import unittest
from itertools import product

from enterprise_math.causal_irreducible_modular_events import irreducible_modular_events
from enterprise_math.causal_quadratic_compatibility import (
    higher_modular_channel_is_quadratic_compatible,
    modular_irreducibles_all_quadratic_compatible,
    quadratic_increment_if_integer,
    quadratic_increment_is_integer_for_all_states,
    quadratic_integrality_matches_total_parity,
    quadratic_value_if_integer,
)


class CausalQuadraticCompatibilityTests(unittest.TestCase):
    def test_quadratic_value_integrality_is_exactly_even_total_parity(self):
        for state in product(range(-2, 3), repeat=4):
            self.assertTrue(quadratic_integrality_matches_total_parity(state))
            self.assertEqual(quadratic_value_if_integer(state) is not None, sum(state) % 2 == 0)

    def test_unit_event_quadratic_increment_integrality_is_exactly_even_support(self):
        for event in product((-1, 0, 1), repeat=5):
            if not any(event):
                continue
            expected = sum(value != 0 for value in event) % 2 == 0
            self.assertEqual(quadratic_increment_is_integer_for_all_states(event), expected)
            for state in ((0,) * 5, (1, -2, 3, 0, -1)):
                self.assertEqual(quadratic_increment_if_integer(state, event) is not None, expected)

    def test_mod_three_higher_irreducible_breaks_quadratic_integer_channel(self):
        self.assertFalse(higher_modular_channel_is_quadratic_compatible(3))
        self.assertFalse(modular_irreducibles_all_quadratic_compatible(5, 3))
        incompatible = [
            event
            for event in irreducible_modular_events(5, 3)
            if not quadratic_increment_is_integer_for_all_states(event)
        ]
        self.assertTrue(incompatible)
        self.assertEqual({sum(value != 0 for value in event) for event in incompatible}, {3})

    def test_mod_four_higher_irreducibles_preserve_quadratic_integrality(self):
        self.assertTrue(higher_modular_channel_is_quadratic_compatible(4))
        self.assertTrue(modular_irreducibles_all_quadratic_compatible(6, 4))

    def test_modular_higher_channel_parity_rule(self):
        for modulus in range(3, 9):
            self.assertEqual(
                higher_modular_channel_is_quadratic_compatible(modulus),
                modulus % 2 == 0,
            )


if __name__ == "__main__":
    unittest.main()
