import itertools
import unittest

from enterprise_math.relation_branching_semiring import words_through_horizon
from enterprise_math.relation_branching_vs_trace_cutoff import branching_trace_gap_fixture
from enterprise_math.relation_structure_first_trace_compiler import (
    exact_count_branching_partition,
    exact_weighted_quotient_matrices,
)
from enterprise_math.relation_weighted_quotient_trace_oracle import (
    raw_and_weighted_quotient_traces_agree,
    weighted_quotient_word_trace,
)


def all_two_state_relations():
    states = (0, 1)
    pairs = tuple(itertools.product(states, repeat=2))
    return tuple(
        frozenset(pair for pair, keep in zip(pairs, mask, strict=True) if keep)
        for mask in itertools.product((0, 1), repeat=4)
    )


class RelationWeightedQuotientTraceOracleTests(unittest.TestCase):
    def test_all_two_state_relation_pairs_factor_all_words_through_horizon_four(self):
        states = (0, 1)
        relations = all_two_state_relations()
        observations = (
            lambda _state: 0,
            lambda state: state,
        )
        for first in relations:
            for second in relations:
                family = {"a": first, "b": second}
                words = words_through_horizon(tuple(family), 4)
                for observation in observations:
                    for source in states:
                        for word in words:
                            self.assertTrue(
                                raw_and_weighted_quotient_traces_agree(
                                    states,
                                    family,
                                    observation,
                                    source,
                                    word,
                                )
                            )

    def test_branching_trace_gap_fixture_factorization_includes_four_vs_one(self):
        states, relations, observation = branching_trace_gap_fixture()
        partition = exact_count_branching_partition(states, relations, observation)
        matrices = exact_weighted_quotient_matrices(states, relations, partition)
        p = weighted_quotient_word_trace(
            partition,
            matrices,
            observation,
            "p",
            ("a", "a"),
        )
        q = weighted_quotient_word_trace(
            partition,
            matrices,
            observation,
            "q",
            ("a", "a"),
        )
        self.assertEqual(p, {"visible": 4})
        self.assertEqual(q, {"visible": 1})

    def test_validation(self):
        states, relations, observation = branching_trace_gap_fixture()
        partition = exact_count_branching_partition(states, relations, observation)
        matrices = exact_weighted_quotient_matrices(states, relations, partition)
        with self.assertRaises(ValueError):
            weighted_quotient_word_trace(
                partition,
                matrices,
                observation,
                "outside",
                (),
            )
        with self.assertRaises(ValueError):
            weighted_quotient_word_trace(
                partition,
                matrices,
                observation,
                "p",
                ("missing",),
            )


if __name__ == "__main__":
    unittest.main()
