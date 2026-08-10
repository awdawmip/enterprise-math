import itertools
import unittest

from enterprise_math.relation_branching_vs_trace_cutoff import (
    branching_trace_gap_fixture,
    modular_terminal_trace_partition,
    natural_terminal_trace_partition,
)
from enterprise_math.relation_terminal_count_trace_certificate import (
    exact_infinite_terminal_trace_partition,
    finite_trace_certificate_modulus,
    observation_indicator_rows,
    partition_from_row_basis,
    rational_terminal_trace_closure_report,
    relation_adjacency_matrix,
    terminal_trace_finite_certificate_report,
    universal_state_count_trace_modulus_bound,
)


def all_two_state_relations():
    states = (0, 1)
    pairs = tuple(itertools.product(states, repeat=2))
    return tuple(
        frozenset(pair for pair, keep in zip(pairs, mask, strict=True) if keep)
        for mask in itertools.product((0, 1), repeat=4)
    )


def countdown_chain(size):
    states = tuple(range(size))
    relation = {(state, state + 1) for state in range(size - 1)}
    relation.add((size - 1, size - 1))
    observation = lambda state: int(state == size - 1)
    return states, {"a": frozenset(relation)}, observation


class RelationTerminalCountTraceCertificateTests(unittest.TestCase):
    def test_adjacency_orientation_matches_source_to_target_counting(self):
        states = (0, 1, 2)
        relation = frozenset({(0, 1), (0, 2), (1, 2)})
        matrix = relation_adjacency_matrix(states, relation)
        self.assertEqual(matrix[1][0], 1)
        self.assertEqual(matrix[2][0], 1)
        self.assertEqual(matrix[2][1], 1)
        self.assertEqual(matrix[0][1], 0)

    def test_observation_indicator_rows_have_one_row_per_observation_class(self):
        states = (0, 1, 2, 3)
        rows = observation_indicator_rows(states, lambda state: state % 2)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0], (1, 0, 1, 0))
        self.assertEqual(rows[1], (0, 1, 0, 1))

    def test_all_two_state_relation_pairs_certificate_matches_literal_traces(self):
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
                    report = terminal_trace_finite_certificate_report(
                        states,
                        family,
                        observation,
                    )
                    self.assertTrue(report.finite_horizon_is_exact)
                    self.assertTrue(report.modular_certificate_is_exact)
                    self.assertLessEqual(
                        report.stabilization_horizon,
                        report.theorem_horizon_bound,
                    )
                    self.assertLessEqual(
                        report.actual_horizon_modulus,
                        report.universal_state_count_modulus_bound,
                    )

    def test_countdown_chain_attains_n_minus_c0_horizon_bound(self):
        for size in range(2, 9):
            states, relations, observation = countdown_chain(size)
            closure = rational_terminal_trace_closure_report(
                states,
                relations,
                observation,
            )
            self.assertEqual(closure.initial_observation_rank, 2)
            self.assertEqual(closure.theorem_horizon_bound, size - 2)
            self.assertEqual(closure.stabilization_horizon, size - 2)
            self.assertEqual(
                tuple(step.rank for step in closure.steps),
                tuple(range(2, size + 1)),
            )
            final_partition = partition_from_row_basis(
                states,
                closure.final_basis_rows,
            )
            self.assertEqual(len(final_partition), size)

    def test_branching_trace_gap_fixture_has_finite_exact_trace_certificate(self):
        states, relations, observation = branching_trace_gap_fixture()
        report = terminal_trace_finite_certificate_report(
            states,
            relations,
            observation,
        )
        self.assertEqual(report.maximum_outdegree, 2)
        self.assertEqual(report.stabilization_horizon, 2)
        self.assertEqual(report.actual_horizon_modulus, 5)
        self.assertTrue(report.modular_certificate_is_exact)

        exact = exact_infinite_terminal_trace_partition(
            states,
            relations,
            observation,
        )
        mod3 = modular_terminal_trace_partition(
            states,
            relations,
            observation,
            report.stabilization_horizon,
            3,
        )
        mod5 = modular_terminal_trace_partition(
            states,
            relations,
            observation,
            report.stabilization_horizon,
            5,
        )
        self.assertIn(frozenset({"p"}), exact)
        self.assertIn(frozenset({"q"}), exact)
        self.assertIn(frozenset({"p", "q"}), mod3)
        self.assertEqual(mod5, exact)

    def test_exact_finite_horizon_at_closure_equals_all_checked_longer_horizons(self):
        states, relations, observation = branching_trace_gap_fixture()
        closure = rational_terminal_trace_closure_report(
            states,
            relations,
            observation,
        )
        exact = exact_infinite_terminal_trace_partition(states, relations, observation)
        for horizon in range(closure.stabilization_horizon, 8):
            self.assertEqual(
                natural_terminal_trace_partition(
                    states,
                    relations,
                    observation,
                    horizon,
                ),
                exact,
            )

    def test_actual_horizon_modulus_can_be_much_smaller_than_state_count_bound(self):
        states, relations, observation = branching_trace_gap_fixture()
        actual = finite_trace_certificate_modulus(states, relations, observation)
        universal = universal_state_count_trace_modulus_bound(
            states,
            relations,
            observation,
        )
        self.assertEqual(actual, 5)
        self.assertGreater(universal, actual)

    def test_identity_observation_stabilizes_at_horizon_zero_and_mod2_is_enough(self):
        states = (0, 1, 2)
        relations = {
            "a": frozenset({(0, 1), (1, 2), (2, 0)}),
        }
        observation = lambda state: state
        report = terminal_trace_finite_certificate_report(
            states,
            relations,
            observation,
        )
        self.assertEqual(report.stabilization_horizon, 0)
        self.assertEqual(report.actual_horizon_modulus, 2)
        self.assertEqual(len(report.exact_infinite_partition), 3)

    def test_validation(self):
        with self.assertRaises(ValueError):
            rational_terminal_trace_closure_report(
                (),
                {"a": frozenset()},
                lambda state: state,
            )
        with self.assertRaises(TypeError):
            relation_adjacency_matrix((0, 1), {(0, 1)})
        with self.assertRaises(ValueError):
            partition_from_row_basis((0, 1), ())


if __name__ == "__main__":
    unittest.main()
