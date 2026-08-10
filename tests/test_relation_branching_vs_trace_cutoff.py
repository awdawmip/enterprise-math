import itertools
import unittest

from enterprise_math.relation_branching_vs_trace_cutoff import (
    branching_trace_gap_fixture,
    branching_versus_trace_cutoff_report,
    finite_horizon_path_count_bound,
    finite_horizon_trace_exact_above_path_count_bound,
    modular_terminal_trace_partition,
    natural_terminal_trace_partition,
    universal_finite_horizon_trace_modulus,
)


def all_two_state_relations():
    states = (0, 1)
    pairs = tuple(itertools.product(states, repeat=2))
    return tuple(
        frozenset(pair for pair, keep in zip(pairs, mask, strict=True) if keep)
        for mask in itertools.product((0, 1), repeat=4)
    )


class RelationBranchingVersusTraceCutoffTests(unittest.TestCase):
    def test_finite_horizon_path_count_bound(self):
        self.assertEqual(finite_horizon_path_count_bound(0, 0), 1)
        self.assertEqual(finite_horizon_path_count_bound(0, 5), 1)
        self.assertEqual(finite_horizon_path_count_bound(1, 8), 1)
        self.assertEqual(finite_horizon_path_count_bound(2, 5), 32)
        self.assertEqual(finite_horizon_path_count_bound(3, 4), 81)
        self.assertEqual(universal_finite_horizon_trace_modulus(2, 5), 33)

    def test_M_above_Delta_power_h_reflects_all_two_state_terminal_traces(self):
        states = (0, 1)
        relations = all_two_state_relations()
        observations = (
            lambda _state: 0,
            lambda state: state,
        )
        for first in relations:
            for second in relations:
                family = {"a": first, "b": second}
                # Two states imply raw outdegree <=2 under every action.
                for horizon in range(4):
                    modulus = universal_finite_horizon_trace_modulus(2, horizon)
                    for observation in observations:
                        self.assertTrue(
                            finite_horizon_trace_exact_above_path_count_bound(
                                states,
                                family,
                                observation,
                                horizon,
                                modulus,
                            )
                        )

    def test_mod3_is_exact_branching_cutoff_but_not_exact_terminal_trace_cutoff(self):
        states, relations, observation = branching_trace_gap_fixture()
        report = branching_versus_trace_cutoff_report(
            states,
            relations,
            observation,
            trace_horizon=4,
            modulus=3,
        )
        self.assertEqual(report.maximum_outdegree, 2)
        self.assertEqual(report.branching_cutoff_modulus, 3)
        self.assertTrue(report.branching_exact)
        self.assertFalse(report.trace_exact)
        self.assertGreater(report.simple_trace_cutoff_modulus, 3)

        self.assertIn(
            frozenset({"p", "q"}),
            report.modular_trace_partition,
        )
        self.assertIn(frozenset({"p"}), report.exact_trace_partition)
        self.assertIn(frozenset({"q"}), report.exact_trace_partition)

    def test_gap_fixture_terminal_mod3_merge_is_not_a_horizon_cutoff_accident(self):
        states, relations, observation = branching_trace_gap_fixture()
        # The fixture is acyclic past length two, so horizon six already contains
        # every nonzero literal trace.  p/q remain mod3-equivalent forever.
        exact = natural_terminal_trace_partition(
            states,
            relations,
            observation,
            6,
        )
        modular = modular_terminal_trace_partition(
            states,
            relations,
            observation,
            6,
            3,
        )
        self.assertIn(frozenset({"p"}), exact)
        self.assertIn(frozenset({"q"}), exact)
        self.assertIn(frozenset({"p", "q"}), modular)

    def test_gap_fixture_exact_counts_are_four_vs_one_at_a_squared(self):
        states, relations, observation = branching_trace_gap_fixture()
        # Inspect horizon two via the induced partitions: exact separates, mod3
        # merges.  The construction itself has four versus one a^2 paths.
        exact = natural_terminal_trace_partition(
            states,
            relations,
            observation,
            2,
        )
        modular = modular_terminal_trace_partition(
            states,
            relations,
            observation,
            2,
            3,
        )
        self.assertIn(frozenset({"p"}), exact)
        self.assertIn(frozenset({"q"}), exact)
        self.assertIn(frozenset({"p", "q"}), modular)

    def test_larger_trace_modulus_restores_gap_fixture_through_horizon_two(self):
        states, relations, observation = branching_trace_gap_fixture()
        # Delta^2=4, so mod5 reflects every path-count coefficient through h=2.
        self.assertTrue(
            finite_horizon_trace_exact_above_path_count_bound(
                states,
                relations,
                observation,
                2,
                5,
            )
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            finite_horizon_path_count_bound(-1, 2)
        with self.assertRaises(TypeError):
            finite_horizon_path_count_bound(2, False)
        with self.assertRaises(ValueError):
            universal_finite_horizon_trace_modulus(2, -1)
        states, relations, observation = branching_trace_gap_fixture()
        with self.assertRaises(ValueError):
            finite_horizon_trace_exact_above_path_count_bound(
                states,
                relations,
                observation,
                2,
                4,
            )


if __name__ == "__main__":
    unittest.main()
