import itertools
import unittest
from fractions import Fraction

from enterprise_math.bounded_local_law_reflection import (
    bounded_local_law_reflection_report,
    primitive_weighted_chain_collision_fixture,
    reconstruct_exact_quotient_from_modular_local_law,
    weighted_word_observation_trace,
)
from enterprise_math.linear_predictive_state import (
    compile_linear_predictive_state,
    induced_predictive_action_matrices,
    observation_decoder_matrix,
    predictive_partition_from_basis,
    predictive_state_for_raw_source,
    predictive_trace_matches_exact_quotient,
    quotient_observation_indicator_rows,
    weighted_quotient_trace_closure,
    weighted_scalar_fan_fixture,
)
from enterprise_math.relation_support_stable_refinement import normalize_partition


def count_correlation_weighted_fixture():
    states = ("p", "q", "r1", "r2", "s", "t", "z1", "z2")
    family = {
        "a": {
            ("p", "r1"): 1,
            ("p", "r2"): 1,
            ("q", "s"): 1,
            ("q", "t"): 1,
        },
        "b": {
            ("r1", "z1"): 1,
            ("r2", "z1"): 1,
            ("s", "z1"): 1,
            ("s", "z2"): 1,
        },
        "c": {
            ("r1", "z1"): 1,
            ("r2", "z1"): 1,
            ("t", "z1"): 1,
            ("t", "z2"): 1,
        },
    }
    return states, family, lambda _state: "visible"


def literal_trace_partition(states, family, observation, words):
    groups = {}
    for source in states:
        signature = tuple(
            (
                tuple(word),
                tuple(sorted(weighted_word_observation_trace(
                    states,
                    family,
                    observation,
                    source,
                    word,
                ).items(), key=lambda item: repr(item[0]))),
            )
            for word in words
        )
        groups.setdefault(signature, set()).add(source)
    return normalize_partition(tuple(groups.values()))


class LinearPredictiveStateTests(unittest.TestCase):
    def test_weighted_fan_has_eleven_discrete_classes_but_dimension_two_predictive_state(self):
        states, family, observation = weighted_scalar_fan_fixture(10)
        report = compile_linear_predictive_state(states, family, observation)
        self.assertEqual(report.raw_state_count, 11)
        self.assertEqual(report.branching_state_count, 11)
        self.assertEqual(report.predictive_dimension, 2)
        self.assertEqual(report.linear_dimension_saved_vs_branching, 9)
        self.assertEqual(report.trace_stabilization_horizon, 1)
        self.assertEqual(report.initial_observation_rank, 1)

        # The trace-equivalence partition still has eleven discrete classes:
        # predictive compression is a change of representation type, not a
        # claim that the original states become trace-equivalent.
        self.assertEqual(len(predictive_partition_from_basis(report)), 11)

    def test_weighted_fan_predictive_machine_matches_exact_outputs_for_literal_words(self):
        states, family, observation = weighted_scalar_fan_fixture(7)
        report = compile_linear_predictive_state(states, family, observation)
        for source in states:
            for word in ((), ("a",), ("a", "a"), ("a", "a", "a")):
                self.assertTrue(
                    predictive_trace_matches_exact_quotient(report, source, word)
                )

    def test_predictive_vectors_encode_weighted_fan_sources_as_two_coordinates(self):
        states, family, observation = weighted_scalar_fan_fixture(5)
        report = compile_linear_predictive_state(states, family, observation)
        vectors = {source: predictive_state_for_raw_source(report, source) for source in states}
        self.assertEqual(len(set(vectors.values())), 6)
        self.assertTrue(all(len(vector) == 2 for vector in vectors.values()))
        self.assertTrue(all(all(isinstance(value, Fraction) for value in vector) for vector in vectors.values()))

    def test_count_correlation_world_has_six_branching_classes_but_rank_four_trace_state(self):
        states, family, observation = count_correlation_weighted_fixture()
        report = compile_linear_predictive_state(states, family, observation)
        self.assertEqual(report.branching_state_count, 6)
        self.assertEqual(report.predictive_dimension, 4)
        self.assertEqual(report.linear_dimension_saved_vs_branching, 2)
        self.assertEqual(report.trace_stabilization_horizon, 1)

        predictive_partition = predictive_partition_from_basis(report)
        self.assertIn(frozenset({"p", "q"}), predictive_partition)
        self.assertIn(frozenset({"r1", "r2"}), predictive_partition)

    def test_predictive_partition_equals_literal_trace_partition_at_closure_horizon(self):
        states, family, observation = count_correlation_weighted_fixture()
        report = compile_linear_predictive_state(states, family, observation)
        actions = tuple(family)
        words = tuple(
            word
            for length in range(report.trace_stabilization_horizon + 1)
            for word in itertools.product(actions, repeat=length)
        )
        literal = literal_trace_partition(states, family, observation, words)
        self.assertEqual(predictive_partition_from_basis(report), literal)

    def test_small_modulus_reflected_machine_compiles_to_same_linear_trace_space(self):
        states, family, observation = primitive_weighted_chain_collision_fixture()
        local = bounded_local_law_reflection_report(
            states,
            family,
            observation,
            modulus=3,
        )
        reconstructed = reconstruct_exact_quotient_from_modular_local_law(
            local.exact_partition,
            family,
            3,
        )
        observation_rows = quotient_observation_indicator_rows(
            local.exact_partition,
            observation,
        )
        exact_closure = weighted_quotient_trace_closure(
            local.exact_quotient_matrices,
            observation_rows,
        )
        reconstructed_closure = weighted_quotient_trace_closure(
            reconstructed,
            observation_rows,
        )
        self.assertEqual(exact_closure, reconstructed_closure)
        self.assertEqual(
            induced_predictive_action_matrices(
                exact_closure.basis_rows,
                local.exact_quotient_matrices,
            ),
            induced_predictive_action_matrices(
                reconstructed_closure.basis_rows,
                reconstructed,
            ),
        )
        self.assertEqual(
            observation_decoder_matrix(exact_closure.basis_rows, observation_rows),
            observation_decoder_matrix(reconstructed_closure.basis_rows, observation_rows),
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            weighted_scalar_fan_fixture(1)
        with self.assertRaises(ValueError):
            weighted_quotient_trace_closure({}, ((1,),))


if __name__ == "__main__":
    unittest.main()
