import itertools
import unittest

from enterprise_math.relation_branching_future_signature import (
    branching_partition_refines_trace_partition,
    branching_partitions_match_support_refinement,
    branching_signature_partition,
    branching_trace_projection_matches_raw_words,
    deterministic_partial_branching_equals_trace,
    relation_family_is_deterministic_partial,
)
from enterprise_math.relation_future_powerset import (
    relation_family_future_partition,
)
from enterprise_math.relation_support_stable_refinement import (
    normalize_partition,
)


def choice_timing_fixture():
    states = ("p", "q", "r", "s", "t", "z")
    relations = {
        "a": frozenset({("p", "r"), ("q", "s"), ("q", "t")}),
        "b": frozenset({("r", "z"), ("s", "z")}),
        "c": frozenset({("r", "z"), ("t", "z")}),
    }
    return states, relations, lambda _state: "visible"


def all_relations(states):
    pairs = tuple(itertools.product(states, repeat=2))
    return tuple(
        frozenset(pair for pair, keep in zip(pairs, mask, strict=True) if keep)
        for mask in itertools.product((0, 1), repeat=len(pairs))
    )


def all_partial_function_relations(states):
    values = (None, *states)
    result = []
    for outputs in itertools.product(values, repeat=len(states)):
        result.append(
            frozenset(
                (source, target)
                for source, target in zip(states, outputs, strict=True)
                if target is not None
            )
        )
    return tuple(result)


class RelationBranchingFutureSignatureTests(unittest.TestCase):
    def test_recursive_signature_kernels_equal_relation_refinement_stages(self):
        states, relations, observation = choice_timing_fixture()
        self.assertTrue(
            branching_partitions_match_support_refinement(
                states,
                relations,
                observation,
            )
        )

    def test_branching_signature_projects_exactly_to_raw_terminal_word_support(self):
        states, relations, observation = choice_timing_fixture()
        for horizon in range(4):
            self.assertTrue(
                branching_trace_projection_matches_raw_words(
                    states,
                    relations,
                    observation,
                    horizon,
                )
            )
            self.assertTrue(
                branching_partition_refines_trace_partition(
                    states,
                    relations,
                    observation,
                    horizon,
                )
            )

    def test_choice_timing_witness_separates_at_branching_horizon_two_but_never_trace(self):
        states, relations, observation = choice_timing_fixture()

        branching_h1 = branching_signature_partition(
            states,
            relations,
            observation,
            1,
        )
        branching_h2 = branching_signature_partition(
            states,
            relations,
            observation,
            2,
        )
        self.assertIn(frozenset({"p", "q"}), branching_h1)
        self.assertIn(frozenset({"p"}), branching_h2)
        self.assertIn(frozenset({"q"}), branching_h2)

        for horizon in range(6):
            trace = relation_family_future_partition(
                states,
                relations,
                observation,
                horizon,
            )
            self.assertIn(frozenset({"p", "q"}), trace)

    def test_every_two_state_single_relation_branching_partition_refines_trace(self):
        states = (0, 1)
        observations = (
            lambda _state: 0,
            lambda state: state,
        )
        for relation in all_relations(states):
            relations = {"a": relation}
            for observation in observations:
                for horizon in range(4):
                    self.assertTrue(
                        branching_partition_refines_trace_partition(
                            states,
                            relations,
                            observation,
                            horizon,
                        )
                    )

    def test_deterministic_partial_relations_have_no_branching_trace_gap(self):
        states = (0, 1)
        partial_relations = all_partial_function_relations(states)
        observations = (
            lambda _state: 0,
            lambda state: state,
        )
        for first in partial_relations:
            for second in partial_relations:
                relations = {"a": first, "b": second}
                self.assertTrue(relation_family_is_deterministic_partial(states, relations))
                for observation in observations:
                    for horizon in range(4):
                        self.assertTrue(
                            deterministic_partial_branching_equals_trace(
                                states,
                                relations,
                                observation,
                                horizon,
                            )
                        )

    def test_multivalued_family_is_rejected_by_deterministic_partial_comparator(self):
        states = (0, 1)
        relations = {"a": frozenset({(0, 0), (0, 1)})}
        self.assertFalse(relation_family_is_deterministic_partial(states, relations))
        with self.assertRaises(ValueError):
            deterministic_partial_branching_equals_trace(
                states,
                relations,
                lambda _state: 0,
                1,
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            branching_signature_partition(
                (),
                {"a": frozenset()},
                lambda state: state,
                0,
            )
        with self.assertRaises(ValueError):
            branching_signature_partition(
                (0, 1),
                {},
                lambda state: state,
                1,
            )
        with self.assertRaises(ValueError):
            branching_signature_partition(
                (0, 1),
                {"a": frozenset({(0, 2)})},
                lambda state: state,
                1,
            )
        with self.assertRaises(TypeError):
            branching_signature_partition(
                (0, 1),
                {"a": frozenset()},
                lambda state: state,
                False,
            )


if __name__ == "__main__":
    unittest.main()
