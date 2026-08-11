import itertools
import unittest

from enterprise_math.bounded_local_law_reflection import (
    bounded_local_law_reflection_report,
    bounded_primitive_sumset,
    decode_residue_from_local_alphabet,
    guaranteed_reflective_modulus_from_width,
    minimal_reflective_modulus,
    modulus_is_injective_on_values,
    primitive_collision_fixture,
    primitive_collision_modulus,
    primitive_weighted_chain_collision_fixture,
    quotient_word_trace_matches_raw,
    reflective_modulus_reproduces_exact_weighted_sequence,
    subset_sum_alphabet,
    weighted_local_aggregate_alphabet,
    weighted_refinement_sequence,
    weighted_word_observation_trace,
)
from enterprise_math.relation_support_stable_refinement import (
    partition_from_observation,
)


class BoundedLocalLawReflectionTests(unittest.TestCase):
    def test_subset_sum_local_alphabet_includes_signed_primitive_aggregates(self):
        self.assertEqual(
            subset_sum_alphabet((-1, 2)),
            frozenset({0, -1, 2, 1}),
        )

    def test_bounded_primitive_sumset_allows_repetition_across_distinct_edges(self):
        values = bounded_primitive_sumset((-1, 2), 2)
        self.assertEqual(
            values,
            frozenset({0, -1, 2, -2, 1, 4}),
        )
        self.assertEqual(guaranteed_reflective_modulus_from_width(values), 7)
        self.assertEqual(minimal_reflective_modulus(values), 7)

    def test_relation_specific_alphabet_can_have_smaller_reflective_modulus_than_width_bound(self):
        values = frozenset({0, 2, 4})
        self.assertEqual(guaranteed_reflective_modulus_from_width(values), 5)
        self.assertEqual(minimal_reflective_modulus(values), 3)
        self.assertTrue(modulus_is_injective_on_values(values, 3))

    def test_nonunit_primitive_weights_are_reflected_exactly_by_mod_three(self):
        states, family, observation = primitive_weighted_chain_collision_fixture()
        alphabet = weighted_local_aggregate_alphabet(states, family)
        self.assertEqual(alphabet, frozenset({0, 1, 2}))
        self.assertTrue(modulus_is_injective_on_values(alphabet, 3))
        self.assertTrue(
            reflective_modulus_reproduces_exact_weighted_sequence(
                states,
                family,
                observation,
                3,
            )
        )

        report = bounded_local_law_reflection_report(
            states,
            family,
            observation,
            modulus=3,
        )
        self.assertTrue(report.complete_sequences_equal)
        self.assertEqual(report.exact_partition, report.modular_partition)
        self.assertEqual(
            report.exact_quotient_matrices,
            report.reconstructed_quotient_matrices,
        )
        self.assertEqual(report.minimal_reflective_modulus, 3)

    def test_reflect_before_compose_recovers_four_vs_one_that_compose_then_mod_three_loses(self):
        states, family, observation = primitive_weighted_chain_collision_fixture()
        exact_p = weighted_word_observation_trace(
            states,
            family,
            observation,
            "p",
            ("a", "b"),
        )
        exact_q = weighted_word_observation_trace(
            states,
            family,
            observation,
            "q",
            ("a", "b"),
        )
        mod_p = weighted_word_observation_trace(
            states,
            family,
            observation,
            "p",
            ("a", "b"),
            modulus=3,
        )
        mod_q = weighted_word_observation_trace(
            states,
            family,
            observation,
            "q",
            ("a", "b"),
            modulus=3,
        )
        self.assertEqual(exact_p["terminal"], 4)
        self.assertEqual(exact_q["terminal"], 1)
        self.assertEqual(mod_p["terminal"], 1)
        self.assertEqual(mod_q["terminal"], 1)

        report = bounded_local_law_reflection_report(
            states,
            family,
            observation,
            modulus=3,
        )
        self.assertTrue(
            quotient_word_trace_matches_raw(
                states,
                family,
                observation,
                report.exact_partition,
                "p",
                ("a", "b"),
            )
        )
        self.assertTrue(
            quotient_word_trace_matches_raw(
                states,
                family,
                observation,
                report.exact_partition,
                "q",
                ("a", "b"),
            )
        )

    def test_unique_local_decode_can_return_negative_integer(self):
        alphabet = frozenset({-1, 0, 1, 2})
        self.assertTrue(modulus_is_injective_on_values(alphabet, 4))
        self.assertEqual(decode_residue_from_local_alphabet(3, 4, alphabet), -1)

    def test_every_primitive_sumset_collision_compiles_a_first_step_counterexample(self):
        cases = (
            ((1,), 3, 2),
            ((1, 2), 2, 3),
            ((-1, 2), 2, 5),
        )
        witnessed = 0
        for primitives, max_terms, modulus in cases:
            collision = primitive_collision_modulus(primitives, max_terms, modulus)
            if collision is None:
                continue
            witnessed += 1
            states, family, observation, values = primitive_collision_fixture(
                primitives,
                max_terms,
                modulus,
            )
            initial = partition_from_observation(states, observation)
            exact = weighted_refinement_sequence(initial, family)
            modular = weighted_refinement_sequence(initial, family, modulus=modulus)
            self.assertNotEqual(values[0], values[1])
            self.assertEqual(values[0] % modulus, values[1] % modulus)
            self.assertNotEqual(exact, modular)
        self.assertGreaterEqual(witnessed, 2)

    def test_reflective_modulus_matches_complete_sequence_on_small_weighted_worlds(self):
        states = (0, 1)
        observation = lambda _state: 0
        edge_pairs = tuple(itertools.product(states, repeat=2))
        primitive_choices = (-1, 1, 2)

        checked = 0
        # One action; enumerate small sparse weighted edge choices.  ``None``
        # means no edge, otherwise use one primitive integer weight.
        for choices in itertools.product((None, *primitive_choices), repeat=len(edge_pairs)):
            relation = {
                edge: weight
                for edge, weight in zip(edge_pairs, choices, strict=True)
                if weight is not None
            }
            family = {"a": relation}
            alphabet = weighted_local_aggregate_alphabet(states, family)
            modulus = minimal_reflective_modulus(alphabet)
            self.assertTrue(
                reflective_modulus_reproduces_exact_weighted_sequence(
                    states,
                    family,
                    observation,
                    modulus,
                )
            )
            checked += 1
        self.assertEqual(checked, 4 ** 4)

    def test_validation(self):
        with self.assertRaises(ValueError):
            bounded_primitive_sumset((), 2)
        with self.assertRaises(ValueError):
            bounded_primitive_sumset((0, 1), 2)
        with self.assertRaises(ValueError):
            modulus_is_injective_on_values((0, 1), 1)
        with self.assertRaises(ValueError):
            weighted_local_aggregate_alphabet(
                (0, 1),
                {"a": {(0, 1): 0}},
            )


if __name__ == "__main__":
    unittest.main()
