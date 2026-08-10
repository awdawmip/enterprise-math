import itertools
import unittest

from enterprise_math.relation_branching_future_signature import (
    branching_signature_partition,
)
from enterprise_math.relation_count_branching_signature import (
    count_branching_refines_support_partition,
    count_branching_signature_map,
    count_branching_signature_partition,
    count_branching_terminal_trace_signature,
    count_erasure_matches_support_signature,
    terminal_count_trace_from_signature,
)
from enterprise_math.relation_future_powerset import words_through_horizon


def raw_observed_path_counts(states, relations, source, word, observation):
    counts = {source: 1}
    for action in word:
        nxt = {}
        for current, multiplicity in counts.items():
            for left, target in relations[action]:
                if left == current:
                    nxt[target] = nxt.get(target, 0) + multiplicity
        counts = nxt
    observed = {}
    for state, multiplicity in counts.items():
        label = observation(state)
        observed[label] = observed.get(label, 0) + multiplicity
    return observed


def multiplicity_fixture():
    states = ("x", "y", "u", "v")
    relations = {
        "a": frozenset({("x", "u"), ("x", "v"), ("y", "u")}),
    }
    return states, relations, lambda _state: "visible"


def count_correlation_fixture():
    states = ("p", "q", "r1", "r2", "s", "t", "z1", "z2")
    relations = {
        "a": frozenset(
            {
                ("p", "r1"),
                ("p", "r2"),
                ("q", "s"),
                ("q", "t"),
            }
        ),
        "b": frozenset(
            {
                ("r1", "z1"),
                ("r2", "z1"),
                ("s", "z1"),
                ("s", "z2"),
            }
        ),
        "c": frozenset(
            {
                ("r1", "z1"),
                ("r2", "z1"),
                ("t", "z1"),
                ("t", "z2"),
            }
        ),
    }
    return states, relations, lambda _state: "visible"


def all_two_state_relations():
    states = (0, 1)
    pairs = tuple(itertools.product(states, repeat=2))
    return tuple(
        frozenset(pair for pair, keep in zip(pairs, mask, strict=True) if keep)
        for mask in itertools.product((0, 1), repeat=4)
    )


def all_two_state_partial_relations():
    states = (0, 1)
    choices = (None, 0, 1)
    return tuple(
        frozenset(
            (source, target)
            for source, target in zip(states, outputs, strict=True)
            if target is not None
        )
        for outputs in itertools.product(choices, repeat=2)
    )


class RelationCountBranchingSignatureTests(unittest.TestCase):
    def test_N_to_B_erasure_matches_support_branching_for_all_two_state_relations(self):
        states = (0, 1)
        observations = (
            lambda _state: 0,
            lambda state: state,
        )
        for relation in all_two_state_relations():
            relations = {"a": relation}
            for observation in observations:
                for horizon in range(4):
                    self.assertTrue(
                        count_erasure_matches_support_signature(
                            states,
                            relations,
                            observation,
                            horizon,
                        )
                    )
                    self.assertTrue(
                        count_branching_refines_support_partition(
                            states,
                            relations,
                            observation,
                            horizon,
                        )
                    )

    def test_multiplicity_strictly_refines_support_branching(self):
        states, relations, observation = multiplicity_fixture()
        support = branching_signature_partition(
            states,
            relations,
            observation,
            1,
        )
        count = count_branching_signature_partition(
            states,
            relations,
            observation,
            1,
        )
        self.assertIn(frozenset({"x", "y"}), support)
        self.assertIn(frozenset({"x"}), count)
        self.assertIn(frozenset({"y"}), count)
        self.assertTrue(
            count_branching_refines_support_partition(
                states,
                relations,
                observation,
                1,
            )
        )

    def test_terminal_count_projection_matches_raw_path_counting(self):
        states, relations, observation = count_correlation_fixture()
        horizon = 4
        signatures = count_branching_signature_map(
            states,
            relations,
            observation,
            horizon,
        )
        words = words_through_horizon(tuple(relations), horizon)
        for state in states:
            for word in words:
                projected = terminal_count_trace_from_signature(
                    signatures[state],
                    word,
                )
                raw = raw_observed_path_counts(
                    states,
                    relations,
                    state,
                    word,
                    observation,
                )
                self.assertEqual(projected, raw, (state, word))

    def test_count_branching_can_be_strictly_finer_than_all_terminal_count_traces(self):
        states, relations, observation = count_correlation_fixture()
        horizon = 4
        words = words_through_horizon(tuple(relations), horizon)

        p_trace = count_branching_terminal_trace_signature(
            states,
            relations,
            observation,
            "p",
            horizon,
            words,
        )
        q_trace = count_branching_terminal_trace_signature(
            states,
            relations,
            observation,
            "q",
            horizon,
            words,
        )
        self.assertEqual(p_trace, q_trace)

        count_h1 = count_branching_signature_partition(
            states,
            relations,
            observation,
            1,
        )
        count_h2 = count_branching_signature_partition(
            states,
            relations,
            observation,
            2,
        )
        self.assertIn(frozenset({"p", "q"}), count_h1)
        self.assertIn(frozenset({"p"}), count_h2)
        self.assertIn(frozenset({"q"}), count_h2)

        # The equality is not a cutoff accident.  In this acyclic fixture every
        # word longer than two has zero count from both p and q, so horizon four
        # already includes all nonzero literal count traces.
        for word in words:
            self.assertEqual(
                raw_observed_path_counts(states, relations, "p", word, observation),
                raw_observed_path_counts(states, relations, "q", word, observation),
            )

    def test_deterministic_partial_relations_have_no_count_support_gap(self):
        states = (0, 1)
        observations = (
            lambda _state: 0,
            lambda state: state,
        )
        partials = all_two_state_partial_relations()
        for first in partials:
            for second in partials:
                relations = {"a": first, "b": second}
                for observation in observations:
                    for horizon in range(4):
                        count = count_branching_signature_partition(
                            states,
                            relations,
                            observation,
                            horizon,
                        )
                        support = branching_signature_partition(
                            states,
                            relations,
                            observation,
                            horizon,
                        )
                        self.assertEqual(count, support)

    def test_validation(self):
        states, relations, observation = multiplicity_fixture()
        with self.assertRaises(ValueError):
            count_branching_signature_partition(
                states,
                relations,
                observation,
                -1,
            )
        with self.assertRaises(ValueError):
            count_branching_terminal_trace_signature(
                states,
                relations,
                observation,
                "outside",
                1,
                ((),),
            )


if __name__ == "__main__":
    unittest.main()
