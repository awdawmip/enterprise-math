import itertools
import unittest

from enterprise_math.relation_future_powerset import (
    relation_family_future_partition,
)
from enterprise_math.relation_path_count_precision import (
    count_partition_refines_support_partition,
    exact_count_partition_refines_modular_partition,
    observed_path_counts,
    path_count_future_partition,
    path_count_support_homomorphism_matches,
    relation_word_path_counts,
)


def all_relations(states):
    pairs = tuple(itertools.product(states, repeat=2))
    return tuple(
        frozenset(pair for bit, pair in zip(mask, pairs, strict=True) if bit)
        for mask in itertools.product((0, 1), repeat=len(pairs))
    )


class RelationPathCountPrecisionTests(unittest.TestCase):
    def test_two_distinct_intermediate_paths_are_counted_but_support_merges_them(self):
        states = (0, 1, 2, 3)
        relation = frozenset({
            (0, 1),
            (0, 2),
            (1, 3),
            (2, 3),
        })
        family = {"R": relation}
        self.assertEqual(
            relation_word_path_counts(
                states,
                family,
                0,
                ("R", "R"),
            ),
            (0, 0, 0, 2),
        )
        counts = dict(
            observed_path_counts(
                states,
                family,
                0,
                ("R", "R"),
                lambda _: "same",
            )
        )
        self.assertEqual(counts["same"], 2)
        self.assertTrue(
            path_count_support_homomorphism_matches(
                states,
                family,
                0,
                ("R", "R"),
                lambda _: "same",
            )
        )

    def test_same_boolean_support_can_hide_different_one_step_path_counts(self):
        states = (0, 1, 2, 3)
        relation = frozenset({
            (0, 2),
            (0, 3),
            (1, 2),
        })
        family = {"R": relation}
        observation = lambda _: 0

        support_partition = relation_family_future_partition(
            states,
            family,
            observation,
            1,
        )
        count_partition = path_count_future_partition(
            states,
            family,
            observation,
            1,
        )
        self.assertIn(frozenset({0, 1}), support_partition)
        self.assertIn(frozenset({0}), count_partition)
        self.assertIn(frozenset({1}), count_partition)
        self.assertTrue(
            count_partition_refines_support_partition(
                states,
                family,
                observation,
                1,
            )
        )

    def test_N_to_B_homomorphism_matches_every_word_for_all_two_state_relation_pairs(self):
        states = (0, 1)
        relations = all_relations(states)
        observations = (
            lambda _: 0,
            lambda state: state,
        )
        words = tuple(
            word
            for length in range(4)
            for word in itertools.product(("L", "R"), repeat=length)
        )
        for left in relations:
            for right in relations:
                family = {"L": left, "R": right}
                for observation in observations:
                    for source in states:
                        for word in words:
                            self.assertTrue(
                                path_count_support_homomorphism_matches(
                                    states,
                                    family,
                                    source,
                                    word,
                                    observation,
                                ),
                                (left, right, source, word),
                            )

    def test_count_partition_refines_support_partition_exhaustively_on_two_states(self):
        states = (0, 1)
        relations = all_relations(states)
        for left in relations:
            for right in relations:
                family = {0: left, 1: right}
                for observation in (lambda _: 0, lambda state: state):
                    for horizon in range(4):
                        self.assertTrue(
                            count_partition_refines_support_partition(
                                states,
                                family,
                                observation,
                                horizon,
                            )
                        )

    def test_exact_count_partition_refines_every_declared_modular_count_partition(self):
        states = (0, 1, 2, 3)
        relations = {
            "R": frozenset({
                (0, 1),
                (0, 2),
                (1, 3),
                (2, 3),
                (3, 3),
            }),
        }
        for modulus in range(1, 6):
            for horizon in range(4):
                self.assertTrue(
                    exact_count_partition_refines_modular_partition(
                        states,
                        relations,
                        lambda _: 0,
                        horizon,
                        modulus,
                    )
                )

    def test_validation(self):
        with self.assertRaises(ValueError):
            relation_word_path_counts((), {"R": frozenset()}, 0, ())
        with self.assertRaises(ValueError):
            relation_word_path_counts(
                (0, 1),
                {"R": frozenset({(0, 1)})},
                2,
                (),
            )
        with self.assertRaises(ValueError):
            relation_word_path_counts(
                (0, 1),
                {"R": frozenset({(0, 1)})},
                0,
                ("X",),
            )
        with self.assertRaises(ValueError):
            path_count_future_partition(
                (0, 1),
                {"R": frozenset({(0, 1)})},
                lambda _: 0,
                1,
                modulus=0,
            )


if __name__ == "__main__":
    unittest.main()
