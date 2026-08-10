import unittest

from enterprise_math.relation_branching_vs_trace_cutoff import branching_trace_gap_fixture
from enterprise_math.relation_terminal_count_trace_certificate import (
    finite_trace_certificate_modulus,
)
from enterprise_math.relation_terminal_count_trace_minimal_modulus import (
    minimal_exact_terminal_trace_modulus,
)


class RelationTerminalCountTraceMinimalModulusTests(unittest.TestCase):
    def test_realized_minimum_never_exceeds_theorem_bound(self):
        states, relations, observation = branching_trace_gap_fixture()
        minimum = minimal_exact_terminal_trace_modulus(
            states,
            relations,
            observation,
        )
        guaranteed = finite_trace_certificate_modulus(
            states,
            relations,
            observation,
        )
        self.assertGreaterEqual(minimum, 2)
        self.assertLessEqual(minimum, guaranteed)

    def test_discrete_observation_needs_only_smallest_legal_modulus(self):
        states = (0, 1, 2)
        relations = {
            "a": frozenset({(0, 1), (1, 2), (2, 0)}),
        }
        observation = lambda state: state
        self.assertEqual(
            minimal_exact_terminal_trace_modulus(
                states,
                relations,
                observation,
            ),
            2,
        )

    def test_relation_specific_realized_precision_can_be_below_safe_coefficient_bound(self):
        # Current observation already separates the states, so path-count value
        # collisions cannot merge the exact state partition even with mod2.
        states = (0, 1, 2, 3)
        relations = {
            "a": frozenset(
                {
                    (0, 1),
                    (0, 2),
                    (1, 2),
                    (1, 3),
                    (2, 3),
                }
            )
        }
        observation = lambda state: state
        guaranteed = finite_trace_certificate_modulus(states, relations, observation)
        minimum = minimal_exact_terminal_trace_modulus(states, relations, observation)
        self.assertEqual(minimum, 2)
        self.assertLessEqual(minimum, guaranteed)


if __name__ == "__main__":
    unittest.main()
