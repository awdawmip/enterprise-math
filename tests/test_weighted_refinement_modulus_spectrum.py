import itertools
import unittest

from enterprise_math.bounded_local_law_reflection import (
    modulus_is_injective_on_values,
    primitive_weighted_chain_collision_fixture,
    weighted_local_aggregate_alphabet,
)
from enterprise_math.weighted_refinement_modulus_spectrum import (
    exact_bad_moduli_for_weighted_refinement,
    exact_moduli_are_upward_closed_sample,
    exact_weighted_split_content_events,
    least_numeric_exact_modulus_from_contents,
    modulus_reproduces_exact_weighted_sequence_by_contents,
)


class WeightedRefinementModulusSpectrumTests(unittest.TestCase):
    def test_primitive_chain_has_exactly_one_bad_modulus(self):
        states, family, observation = primitive_weighted_chain_collision_fixture()
        events = exact_weighted_split_content_events(states, family, observation)
        self.assertTrue(events)
        self.assertEqual(exact_bad_moduli_for_weighted_refinement(states, family, observation), frozenset({2}))
        self.assertEqual(
            least_numeric_exact_modulus_from_contents(states, family, observation),
            3,
        )
        self.assertFalse(
            modulus_reproduces_exact_weighted_sequence_by_contents(
                states, family, observation, 2
            )
        )
        for modulus in range(3, 10):
            self.assertTrue(
                modulus_reproduces_exact_weighted_sequence_by_contents(
                    states, family, observation, modulus
                )
            )

    def test_realized_world_can_be_exact_even_when_global_local_alphabet_code_is_not_injective(self):
        states = (0, 1)
        family = {"a": {(0, 1): 2}}
        observation = lambda state: state  # initial state is already discrete
        alphabet = weighted_local_aggregate_alphabet(states, family)
        self.assertEqual(alphabet, frozenset({0, 2}))
        self.assertFalse(modulus_is_injective_on_values(alphabet, 2))
        self.assertEqual(
            exact_bad_moduli_for_weighted_refinement(states, family, observation),
            frozenset(),
        )
        self.assertTrue(
            modulus_reproduces_exact_weighted_sequence_by_contents(
                states, family, observation, 2
            )
        )
        self.assertEqual(
            least_numeric_exact_modulus_from_contents(states, family, observation),
            2,
        )

    def test_bad_moduli_can_be_a_nonprincipal_finite_downset(self):
        states = ("x0", "x2", "x3", "t")
        family = {
            "a": {
                ("x2", "t"): 2,
                ("x3", "t"): 3,
            }
        }
        observation = lambda _state: 0
        bad = exact_bad_moduli_for_weighted_refinement(states, family, observation)
        self.assertEqual(bad, frozenset({2, 3}))
        self.assertEqual(
            least_numeric_exact_modulus_from_contents(states, family, observation),
            4,
        )
        self.assertTrue(
            modulus_reproduces_exact_weighted_sequence_by_contents(
                states, family, observation, 6
            )
        )

    def test_exact_moduli_are_upward_closed_under_divisibility_on_samples(self):
        states, family, observation = primitive_weighted_chain_collision_fixture()
        self.assertTrue(
            exact_moduli_are_upward_closed_sample(
                states,
                family,
                observation,
                30,
            )
        )

    def test_split_content_prediction_matches_actual_modular_refinement_exhaustively_on_two_states(self):
        states = (0, 1)
        edge_pairs = tuple(itertools.product(states, repeat=2))
        weight_choices = (None, -1, 1, 2)
        observations = (
            lambda _state: 0,
            lambda state: state,
        )
        checked = 0
        for choices in itertools.product(weight_choices, repeat=len(edge_pairs)):
            relation = {
                edge: weight
                for edge, weight in zip(edge_pairs, choices, strict=True)
                if weight is not None
            }
            family = {"a": relation}
            for observation in observations:
                for modulus in range(2, 7):
                    # The helper internally compares the split-content theorem
                    # with the literal modular refinement sequence.
                    modulus_reproduces_exact_weighted_sequence_by_contents(
                        states,
                        family,
                        observation,
                        modulus,
                    )
                    checked += 1
        self.assertEqual(checked, (4 ** 4) * 2 * 5)

    def test_event_contents_are_positive_on_strict_splits(self):
        states = ("x0", "x2", "x3", "t")
        family = {
            "a": {
                ("x2", "t"): 2,
                ("x3", "t"): 3,
            }
        }
        events = exact_weighted_split_content_events(
            states,
            family,
            lambda _state: 0,
        )
        self.assertTrue(events)
        self.assertTrue(all(event.gcd_content > 0 for event in events))


if __name__ == "__main__":
    unittest.main()
