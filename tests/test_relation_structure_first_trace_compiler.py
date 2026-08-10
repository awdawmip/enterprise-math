import itertools
import unittest

from enterprise_math.relation_branching_vs_trace_cutoff import branching_trace_gap_fixture
from enterprise_math.relation_structure_first_trace_compiler import (
    exact_count_branching_partition,
    exact_weighted_quotient_matrices,
    lift_modular_weight,
    lifted_modular_weighted_quotient_matrices,
    observation_labels_for_blocks,
    quotient_observation_indicator_rows,
    quotient_trace_closure_report,
    structure_first_trace_compiler_report,
)
from enterprise_math.relation_terminal_count_trace_certificate import (
    exact_infinite_terminal_trace_partition,
)


def all_two_state_relations():
    states = (0, 1)
    pairs = tuple(itertools.product(states, repeat=2))
    return tuple(
        frozenset(pair for pair, keep in zip(pairs, mask, strict=True) if keep)
        for mask in itertools.product((0, 1), repeat=4)
    )


def repeated_behaviour_fixture(group_size=10):
    a_states = tuple(f"a{index}" for index in range(group_size))
    b_states = tuple(f"b{index}" for index in range(group_size))
    states = a_states + b_states
    relation = frozenset((source, b_states[0]) for source in a_states)
    return states, {"step": relation}, lambda _state: "visible"


def weighted_word_total(matrix, source, length):
    vector = [0 for _ in range(len(matrix))]
    vector[source] = 1
    for _ in range(length):
        nxt = [0 for _ in range(len(matrix))]
        for target in range(len(matrix)):
            nxt[target] = sum(
                matrix[target][current] * vector[current]
                for current in range(len(matrix))
            )
        vector = nxt
    return sum(vector)


class RelationStructureFirstTraceCompilerTests(unittest.TestCase):
    def test_all_two_state_relation_pairs_compile_exact_infinite_trace_partition(self):
        states = (0, 1)
        relations = all_two_state_relations()
        observations = (
            lambda _state: 0,
            lambda state: state,
        )
        for first in relations:
            for second in relations:
                family = {"a": first, "b": second}
                for observation in observations:
                    report = structure_first_trace_compiler_report(
                        states,
                        family,
                        observation,
                    )
                    self.assertTrue(report.structure_first_exact)
                    self.assertEqual(
                        report.exact_trace_partition_from_quotient,
                        exact_infinite_terminal_trace_partition(
                            states,
                            family,
                            observation,
                        ),
                    )

    def test_small_modulus_lifts_exact_weighted_quotient(self):
        states, relations, observation = branching_trace_gap_fixture()
        exact_partition = exact_count_branching_partition(
            states,
            relations,
            observation,
        )
        exact_matrices = exact_weighted_quotient_matrices(
            states,
            relations,
            exact_partition,
        )
        modular_partition, lifted = lifted_modular_weighted_quotient_matrices(
            states,
            relations,
            observation,
            3,
        )
        self.assertEqual(modular_partition, exact_partition)
        self.assertEqual(lifted, exact_matrices)

    def test_branching_trace_gap_world_uses_mod3_structure_to_compile_exact_traces(self):
        states, relations, observation = branching_trace_gap_fixture()
        report = structure_first_trace_compiler_report(
            states,
            relations,
            observation,
            modulus=3,
        )
        self.assertEqual(report.maximum_outdegree, 2)
        self.assertEqual(report.local_exact_modulus, 3)
        self.assertTrue(report.structure_first_exact)
        self.assertLessEqual(
            report.quotient_trace_horizon_bound,
            report.raw_trace_horizon_bound,
        )

    def test_repeated_behaviour_collapses_twenty_raw_states_to_two_weighted_states(self):
        states, relations, observation = repeated_behaviour_fixture(10)
        report = structure_first_trace_compiler_report(
            states,
            relations,
            observation,
        )
        self.assertEqual(report.raw_state_count, 20)
        self.assertEqual(report.maximum_outdegree, 1)
        self.assertEqual(report.local_exact_modulus, 2)
        self.assertEqual(report.branching_state_count, 2)
        self.assertEqual(report.dimension_reduction, 18)
        self.assertEqual(report.raw_trace_horizon_bound, 19)
        self.assertEqual(report.quotient_trace_horizon_bound, 1)
        self.assertEqual(report.quotient_trace_stabilization_horizon, 1)
        self.assertTrue(report.structure_first_exact)

    def test_exact_weighted_quotient_preserves_path_totals_on_repeated_fixture(self):
        states, relations, observation = repeated_behaviour_fixture(6)
        partition = exact_count_branching_partition(
            states,
            relations,
            observation,
        )
        matrices = exact_weighted_quotient_matrices(
            states,
            relations,
            partition,
        )
        matrix = matrices["step"]
        labels = observation_labels_for_blocks(partition, observation)
        self.assertEqual(labels, ("visible", "visible"))

        source_block = next(
            index
            for index, block in enumerate(partition)
            if "a0" in block
        )
        terminal_block = next(
            index
            for index, block in enumerate(partition)
            if "b0" in block
        )
        self.assertEqual(matrix[terminal_block][source_block], 1)
        self.assertEqual(weighted_word_total(matrix, source_block, 0), 1)
        self.assertEqual(weighted_word_total(matrix, source_block, 1), 1)
        self.assertEqual(weighted_word_total(matrix, source_block, 2), 0)

    def test_quotient_observation_rows_preserve_observation_rank(self):
        states = (0, 1, 2, 3)
        relations = {
            "a": frozenset({(0, 2), (1, 2), (2, 3), (3, 3)}),
        }
        observation = lambda state: state % 2
        partition = exact_count_branching_partition(states, relations, observation)
        rows = quotient_observation_indicator_rows(partition, observation)
        self.assertEqual(len(rows), 2)
        self.assertTrue(all(len(row) == len(partition) for row in rows))
        matrices = exact_weighted_quotient_matrices(states, relations, partition)
        closure = quotient_trace_closure_report(matrices, rows)
        self.assertLessEqual(
            closure.stabilization_horizon,
            closure.theorem_horizon_bound,
        )

    def test_local_weight_lift_validation(self):
        self.assertEqual(lift_modular_weight(0, 3, 2), 0)
        self.assertEqual(lift_modular_weight(2, 3, 2), 2)
        with self.assertRaises(ValueError):
            lift_modular_weight(0, 2, 2)
        with self.assertRaises(ValueError):
            lift_modular_weight(3, 5, 2)

    def test_modulus_below_outdegree_is_rejected(self):
        states, relations, observation = branching_trace_gap_fixture()
        with self.assertRaises(ValueError):
            lifted_modular_weighted_quotient_matrices(
                states,
                relations,
                observation,
                2,
            )


if __name__ == "__main__":
    unittest.main()
