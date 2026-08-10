import unittest
from itertools import product

from enterprise_math.relation_future_powerset import (
    aggregate_support_forgets_branch_survival,
    composed_relation_for_word,
    observed_support,
    relation_family_future_partition,
    relation_family_future_signature,
    relation_support_image,
    relation_word_observed_support,
    relation_word_support,
    support_compiler_matches_raw_composition,
    words_through_horizon,
)


class RelationFuturePowersetTests(unittest.TestCase):
    def test_one_relation_is_total_deterministic_on_support_sets(self):
        states = frozenset(range(4))
        relation = frozenset({(0, 1), (0, 2), (1, 3)})

        self.assertEqual(
            relation_support_image(states, relation, {0}),
            frozenset({1, 2}),
        )
        self.assertEqual(
            relation_support_image(states, relation, {0, 1}),
            frozenset({1, 2, 3}),
        )
        self.assertEqual(
            relation_support_image(states, relation, frozenset()),
            frozenset(),
        )
        self.assertEqual(
            relation_support_image(states, relation, {2, 3}),
            frozenset(),
        )

    def test_literal_relation_word_support_matches_raw_composition(self):
        states = frozenset(range(5))
        relations = {
            "a": frozenset({(0, 1), (0, 2), (1, 3), (2, 4)}),
            "b": frozenset({(1, 4), (2, 3), (3, 0), (4, 0)}),
        }
        words = words_through_horizon(("a", "b"), 4)
        for source in states:
            for word in words:
                self.assertTrue(
                    support_compiler_matches_raw_composition(
                        states,
                        relations,
                        source,
                        word,
                    )
                )
                composed = composed_relation_for_word(
                    states,
                    relations,
                    word,
                )
                direct = frozenset(
                    target
                    for current, target in composed
                    if current == source
                )
                self.assertEqual(
                    relation_word_support(
                        states,
                        relations,
                        source,
                        word,
                    ),
                    direct,
                )

    def test_exhaustive_two_state_two_action_compiler_matches_raw_words(self):
        states = frozenset({0, 1})
        pairs = ((0, 0), (0, 1), (1, 0), (1, 1))
        all_relations = tuple(
            frozenset(
                pair
                for index, pair in enumerate(pairs)
                if mask & (1 << index)
            )
            for mask in range(1 << len(pairs))
        )
        words = words_through_horizon(("a", "b"), 3)
        self.assertEqual(len(words), 1 + 2 + 4 + 8)

        for left in all_relations:
            for right in all_relations:
                family = {"a": left, "b": right}
                for source in states:
                    for word in words:
                        self.assertTrue(
                            support_compiler_matches_raw_composition(
                                states,
                                family,
                                source,
                                word,
                            )
                        )

    def test_observed_support_can_be_strictly_coarser_than_raw_support(self):
        states = frozenset(range(5))
        relations = {
            "a": frozenset({(0, 2), (0, 3)}),
        }
        raw = relation_word_support(
            states,
            relations,
            0,
            ("a",),
        )
        self.assertEqual(raw, frozenset({2, 3}))
        self.assertEqual(
            observed_support(raw, lambda value: value // 2),
            frozenset({1}),
        )
        self.assertEqual(
            relation_word_observed_support(
                states,
                relations,
                0,
                ("a",),
                lambda value: value // 2,
            ),
            frozenset({1}),
        )

    def test_multiple_witness_paths_can_collapse_to_one_support_target(self):
        states = frozenset(range(6))
        relations = {
            "a": frozenset(
                {
                    (0, 1),
                    (0, 2),
                    (4, 1),
                }
            ),
            "b": frozenset(
                {
                    (1, 3),
                    (2, 3),
                }
            ),
        }
        # Source 0 has two distinct raw a;b witness paths to target 3;
        # source 4 has only one.  The support compiler intentionally gives both
        # the same final support {3}.
        self.assertEqual(
            relation_word_support(states, relations, 0, ("a", "b")),
            frozenset({3}),
        )
        self.assertEqual(
            relation_word_support(states, relations, 4, ("a", "b")),
            frozenset({3}),
        )
        path_count_0 = sum(
            1
            for middle in states
            if (0, middle) in relations["a"]
            and (middle, 3) in relations["b"]
        )
        path_count_4 = sum(
            1
            for middle in states
            if (4, middle) in relations["a"]
            and (middle, 3) in relations["b"]
        )
        self.assertEqual((path_count_0, path_count_4), (2, 1))

    def test_aggregate_support_can_forget_that_one_branch_died(self):
        states = frozenset(range(4))
        relation = frozenset({(1, 3)})
        self.assertTrue(
            aggregate_support_forgets_branch_survival(
                states,
                relation,
                {1, 2},
                {1},
            )
        )
        self.assertEqual(
            relation_support_image(states, relation, {1, 2}),
            frozenset({3}),
        )
        self.assertEqual(
            relation_support_image(states, relation, {1}),
            frozenset({3}),
        )
        # If a future language observes whether the 2-branch died separately,
        # aggregate support is therefore too coarse despite being exact for
        # ordinary reachable-support semantics.

    def test_relation_future_language_can_generate_precision_from_constant_observation(self):
        states = frozenset({0, 1, 2})
        relations = {
            "d": frozenset({(2, 1), (1, 0)}),
        }
        observation = lambda _: 0

        horizon0 = relation_family_future_partition(
            states,
            relations,
            observation,
            0,
        )
        horizon1 = relation_family_future_partition(
            states,
            relations,
            observation,
            1,
        )
        horizon2 = relation_family_future_partition(
            states,
            relations,
            observation,
            2,
        )

        self.assertEqual(horizon0, frozenset({states}))
        self.assertEqual(
            horizon1,
            frozenset({frozenset({0}), frozenset({1, 2})}),
        )
        self.assertEqual(
            horizon2,
            frozenset(
                {
                    frozenset({0}),
                    frozenset({1}),
                    frozenset({2}),
                }
            ),
        )

        signatures = {
            source: relation_family_future_signature(
                states,
                relations,
                source,
                observation,
                2,
            )
            for source in states
        }
        self.assertEqual(len(set(signatures.values())), 3)

    def test_word_enumeration_is_exact_geometric_series(self):
        for action_count in range(1, 5):
            actions = tuple(range(action_count))
            for horizon in range(5):
                words = words_through_horizon(actions, horizon)
                expected = sum(action_count**length for length in range(horizon + 1))
                self.assertEqual(len(words), expected)
                self.assertEqual(words[0], ())
                self.assertTrue(all(len(word) <= horizon for word in words))

    def test_validation(self):
        states = frozenset({0, 1})
        relation = frozenset({(0, 1)})
        with self.assertRaises(ValueError):
            relation_support_image((), relation, {0})
        with self.assertRaises(ValueError):
            relation_support_image(states, relation, {2})
        with self.assertRaises(TypeError):
            relation_support_image(states, {(0, 1)}, {0})
        with self.assertRaises(ValueError):
            relation_word_support(
                states,
                {"a": relation},
                0,
                ("missing",),
            )
        with self.assertRaises(ValueError):
            words_through_horizon((), 1)
        with self.assertRaises(ValueError):
            words_through_horizon(("a", "a"), 1)
        with self.assertRaises(ValueError):
            words_through_horizon(("a",), -1)
        with self.assertRaises(ValueError):
            aggregate_support_forgets_branch_survival(
                states,
                relation,
                {0},
                {0},
            )


if __name__ == "__main__":
    unittest.main()
