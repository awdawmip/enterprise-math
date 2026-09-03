import unittest

from enterprise_math.finite_symmetry import (
    canonical_choice_obstruction,
    orbit_partition,
)
from enterprise_math.operation_quotient import operation_descends
from enterprise_math.rotation_phase_refinement import quarter_turn_roots


class EulerOrientationTorsorTests(unittest.TestCase):
    def test_quarter_turn_roots_form_one_reflection_orbit(self):
        roots = quarter_turn_roots(12)
        self.assertEqual(roots, (3, 9))
        actions = {
            "identity": {3: 3, 9: 9},
            "reflection": {3: 9, 9: 3},
        }
        self.assertEqual(orbit_partition(roots, actions), (frozenset({3, 9}),))
        self.assertTrue(canonical_choice_obstruction(roots, actions))

    def test_reflection_conjugates_successor_to_inverse(self):
        order = 12
        successor = lambda state: (state + 1) % order
        inverse_successor = lambda state: (state - 1) % order
        reflection = lambda state: (-state) % order
        for state in range(order):
            self.assertEqual(
                reflection(successor(reflection(state))),
                inverse_successor(state),
            )

    def test_half_turn_is_reflection_fixed(self):
        order = 12
        half_turn = order // 2
        self.assertEqual((-half_turn) % order, half_turn)

    def test_constant_turn_orientation_observation_descends(self):
        domain = tuple((phase, hidden) for phase in range(6) for hidden in (0, 1))
        observation = {state: state[0] for state in domain}
        operation = {
            state: ((state[0] + 1) % 6, state[1])
            for state in domain
        }
        self.assertTrue(operation_descends(domain, operation, observation))

    def test_hidden_dependent_turn_fails_to_descend(self):
        domain = tuple((phase, hidden) for phase in range(6) for hidden in (0, 1))
        observation = {state: state[0] for state in domain}
        operation = {
            state: ((state[0] + state[1]) % 6, state[1])
            for state in domain
        }
        self.assertFalse(operation_descends(domain, operation, observation))


if __name__ == "__main__":
    unittest.main()
