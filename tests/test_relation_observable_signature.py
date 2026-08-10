import unittest
from itertools import product

from enterprise_math.admissible_support import compose_relations
from enterprise_math.relation_observable_signature import (
    composed_relation_observation_signature_map,
    deterministic_observed_transition,
    observed_target_set,
    partition_refines_relation_observation_partition,
    quotient_is_relation_observation_safe,
    raw_target_set,
    relation_observable_is_deterministic,
    relation_observable_source_report,
    relation_observation_partition,
    relation_observation_signature_map,
)


class RelationObservableSignatureTests(unittest.TestCase):
    def setUp(self):
        self.states = frozenset(range(5))
        self.relation = frozenset(
            {
                (0, 3),
                (0, 4),
                (1, 3),
                (3, 3),
                (4, 4),
            }
        )
        self.observation = lambda value: "T" if value in (3, 4) else f"S{value}"

    def test_raw_branching_can_be_completely_hidden_by_declared_observation(self):
        report = relation_observable_source_report(
            self.states,
            self.relation,
            0,
            self.observation,
        )
        self.assertEqual(report.raw_targets, frozenset({3, 4}))
        self.assertEqual(report.observed_targets, frozenset({"T"}))
        self.assertTrue(report.raw_relation_branches)
        self.assertTrue(report.observable_deterministic)
        self.assertTrue(report.branching_hidden_by_observation)

    def test_undefined_is_empty_signature_not_identity(self):
        self.assertEqual(raw_target_set(self.relation, 2), frozenset())
        self.assertEqual(
            observed_target_set(self.relation, 2, self.observation),
            frozenset(),
        )
        signatures = relation_observation_signature_map(
            self.states,
            self.relation,
            self.observation,
        )
        self.assertEqual(signatures[2], frozenset())
        self.assertNotEqual(signatures[2], signatures[0])

    def test_partial_observed_transition_can_be_deterministic_without_being_total(self):
        self.assertTrue(
            relation_observable_is_deterministic(
                self.states,
                self.relation,
                self.observation,
            )
        )
        self.assertFalse(
            relation_observable_is_deterministic(
                self.states,
                self.relation,
                self.observation,
                require_defined=True,
            )
        )
        compiled = deterministic_observed_transition(
            self.states,
            self.relation,
            self.observation,
        )
        self.assertIsNone(compiled[2])
        for source in (0, 1, 3, 4):
            self.assertEqual(compiled[source], "T")

    def test_coarsest_partition_is_kernel_of_set_valued_signature(self):
        partition = relation_observation_partition(
            self.states,
            self.relation,
            self.observation,
        )
        self.assertEqual(
            partition,
            frozenset(
                {
                    frozenset({0, 1, 3, 4}),
                    frozenset({2}),
                }
            ),
        )
        self.assertTrue(
            partition_refines_relation_observation_partition(
                self.states,
                self.relation,
                self.observation,
                partition,
            )
        )
        self.assertTrue(
            partition_refines_relation_observation_partition(
                self.states,
                self.relation,
                self.observation,
                ({0, 1}, {3, 4}, {2}),
            )
        )
        self.assertFalse(
            partition_refines_relation_observation_partition(
                self.states,
                self.relation,
                self.observation,
                ({0, 2}, {1, 3, 4}),
            )
        )

    def test_source_quotient_is_safe_iff_signature_is_constant_on_each_fiber(self):
        safe_key = lambda source: 0 if source in (0, 1, 3, 4) else 1
        unsafe_key = lambda source: source % 2
        self.assertTrue(
            quotient_is_relation_observation_safe(
                self.states,
                self.relation,
                self.observation,
                safe_key,
            )
        )
        self.assertFalse(
            quotient_is_relation_observation_safe(
                self.states,
                self.relation,
                self.observation,
                unsafe_key,
            )
        )

    def test_observable_nondeterminism_is_the_size_of_observed_target_set_not_raw_target_set(self):
        relation = frozenset({(0, 2), (0, 3)})
        states = frozenset(range(4))
        identity_observation = lambda value: value
        collapsed_observation = lambda value: value % 2

        self.assertFalse(
            relation_observable_is_deterministic(
                states,
                relation,
                identity_observation,
            )
        )
        self.assertFalse(
            relation_observable_is_deterministic(
                states,
                relation,
                collapsed_observation,
            )
        )

        constant_observation = lambda _: 0
        self.assertTrue(
            relation_observable_is_deterministic(
                states,
                relation,
                constant_observation,
            )
        )

    def test_terminal_only_composition_signature_matches_explicit_composed_relation(self):
        states = frozenset(range(5))
        first = frozenset(
            {
                (0, 1),
                (0, 2),
                (3, 2),
            }
        )
        second = frozenset(
            {
                (1, 4),
                (2, 3),
                (2, 4),
            }
        )
        observation = lambda value: value % 2
        expected = relation_observation_signature_map(
            states,
            compose_relations(first, second),
            observation,
        )
        self.assertEqual(
            composed_relation_observation_signature_map(
                states,
                first,
                second,
                observation,
            ),
            expected,
        )
        self.assertEqual(expected[0], frozenset({0, 1}))
        self.assertEqual(expected[3], frozenset({0, 1}))

    def test_same_observed_target_cardinality_is_not_enough_for_safe_merge(self):
        states = frozenset(range(4))
        relation = frozenset({(0, 2), (1, 3)})
        observation = lambda value: value
        signatures = relation_observation_signature_map(
            states,
            relation,
            observation,
        )
        self.assertEqual(len(signatures[0]), len(signatures[1]))
        self.assertNotEqual(signatures[0], signatures[1])
        self.assertFalse(
            quotient_is_relation_observation_safe(
                states,
                relation,
                observation,
                lambda source: 0 if source in (0, 1) else source,
            )
        )

    def test_exhaustive_two_state_relations_match_direct_signature_kernel(self):
        states = frozenset({0, 1})
        pairs = ((0, 0), (0, 1), (1, 0), (1, 1))
        observations = (
            lambda value: value,
            lambda _: 0,
        )
        for mask in range(1 << len(pairs)):
            relation = frozenset(
                pair
                for index, pair in enumerate(pairs)
                if mask & (1 << index)
            )
            for observation in observations:
                signatures = relation_observation_signature_map(
                    states,
                    relation,
                    observation,
                )
                expected_same = signatures[0] == signatures[1]
                self.assertEqual(
                    quotient_is_relation_observation_safe(
                        states,
                        relation,
                        observation,
                        lambda _: 0,
                    ),
                    expected_same,
                )
                partition = relation_observation_partition(
                    states,
                    relation,
                    observation,
                )
                self.assertEqual(
                    len(partition),
                    1 if expected_same else 2,
                )

    def test_deterministic_helper_rejects_observed_none_collision(self):
        states = frozenset({0, 1})
        relation = frozenset({(0, 1)})
        with self.assertRaises(ValueError):
            deterministic_observed_transition(
                states,
                relation,
                lambda _: None,
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            relation_observation_signature_map(
                (),
                frozenset(),
                lambda value: value,
            )
        with self.assertRaises(TypeError):
            relation_observation_signature_map(
                {0, 1},
                {(0, 1)},
                lambda value: value,
            )
        with self.assertRaises(ValueError):
            relation_observation_signature_map(
                {0, 1},
                frozenset({(0, 2)}),
                lambda value: value,
            )
        with self.assertRaises(ValueError):
            relation_observable_source_report(
                {0, 1},
                frozenset(),
                2,
                lambda value: value,
            )
        with self.assertRaises(ValueError):
            partition_refines_relation_observation_partition(
                {0, 1},
                frozenset(),
                lambda value: value,
                ({0},),
            )


if __name__ == "__main__":
    unittest.main()
