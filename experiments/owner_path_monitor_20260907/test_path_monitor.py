"""Independent finite enumeration and existing WBRC cross-checks."""
from dataclasses import replace
from fractions import Fraction
import unittest

from path_monitor import (
    ALPHABET, HIT, MONITOR_STATES, ONE, START, Edge, NativeGraph, Node,
    coefficient, compose_port_series, enumerate_port_walks, port_excursion_series, reverse_step_monitor,
    verify_port_series,
)
from examples import blind_pair, branching_hidden_cycle_graph, suffix_context_graph
from enterprise_math.brc_histogram import WeightHistogram
from enterprise_math.brc_moment_transfer import (
    moment_port_kernel_at_z, moment_transition_matrix, moment_walk_series_coefficients,
)


def indexed_edges(graph):
    indices = {node.label: i for i, node in enumerate(graph.nodes)}
    return indices, tuple((indices[edge.source], indices[edge.target], edge.weight) for edge in graph.edges)


class NativePathMonitorTests(unittest.TestCase):
    def assert_matches_enumeration(self, graph, ports, horizon):
        excursion = port_excursion_series(graph, ports, horizon)
        walks = compose_port_series(excursion)
        enumerated = enumerate_port_walks(graph, ports, horizon)
        self.assertTrue(excursion.complete and walks.complete and enumerated.complete)
        self.assertEqual(walks.coefficients, enumerated.coefficients)
        return excursion, walks, enumerated

    def test_t6_minimal_monitor_and_all_signed_directions(self):
        monitor = reverse_step_monitor()
        self.assertEqual(monitor.partition_sizes, (2, 14))
        self.assertEqual(len(monitor.states), 14)
        for step in ALPHABET:
            self.assertEqual(monitor.advance(START, step), step)
            self.assertEqual(monitor.advance(step, -step), HIT)
            self.assertEqual(monitor.advance(HIT, step), HIT)
        with self.assertRaises(TypeError):
            monitor.operations[1][START] = HIT
        for state in (True, 1.0, "START"):
            with self.assertRaises(ValueError):
                monitor.advance(state, 1)

    def test_blind_pair_equal_endpoint_length_histogram_but_different_hit(self):
        left_graph, right_graph = blind_pair()
        left_e, left, left_enum = self.assert_matches_enumeration(left_graph, ("P",), 8)
        right_e, right, right_enum = self.assert_matches_enumeration(right_graph, ("P",), 8)
        same = WeightHistogram.from_weights([Fraction(2, 11)])
        self.assertEqual(coefficient(left, "P", "P", 4), same)
        self.assertEqual(coefficient(right, "P", "P", 4), same)
        self.assertEqual(coefficient(left, "P", "P", 4, final=HIT), same)
        self.assertTrue(coefficient(right, "P", "P", 4, final=HIT).is_zero)
        self.assertEqual(coefficient(right, "P", "P", 4, final=-2), same)
        self.assertTrue(all(key[2] == 4 for key in left_e.coefficients))
        self.assertTrue(all(key[2] == 4 for key in right_e.coefficients))
        left_word = next(w.word for w in left_enum.witnesses if len(w.word) == 4)
        right_word = next(w.word for w in right_enum.witnesses if len(w.word) == 4)
        self.assertEqual(left_word, (1, -1, 2, -2))
        self.assertEqual(right_word, (1, 2, -1, -2))
        self.assertNotEqual(left_word, right_word)

    def test_future_suffix_matches_monitor_boundary_at_port(self):
        graph = suffix_context_graph()
        excursions, walks, _ = self.assert_matches_enumeration(graph, ("P", "Q", "R"), 2)
        self.assertEqual(coefficient(excursions, "P", "Q", 1, final=1).total_mass, Fraction(2, 3))
        self.assertEqual(coefficient(excursions, "Q", "R", 1, initial=1, final=HIT).total_mass, Fraction(3, 5))
        self.assertTrue(coefficient(excursions, "Q", "R", 1, initial=START, final=HIT).is_zero)
        self.assertEqual(coefficient(walks, "P", "R", 2, final=HIT).total_mass, Fraction(2, 5))
        # Reclassifying Q as internal gives the same P/R transfer; labels with
        # equal raw coordinates P and R remain distinct routing states.
        _, fewer_ports, _ = self.assert_matches_enumeration(graph, ("P", "R"), 2)
        for initial in MONITOR_STATES:
            for final in MONITOR_STATES:
                self.assertEqual(coefficient(walks, "P", "R", 2, initial, final),
                                 coefficient(fewer_ports, "P", "R", 2, initial, final))

    def test_hidden_cycle_parallel_branches_and_repeated_port_returns(self):
        graph = branching_hidden_cycle_graph()
        excursions, walks, enumerated = self.assert_matches_enumeration(graph, ("P",), 8)
        self.assertEqual(coefficient(excursions, "P", "P", 2).count, 2)
        self.assertEqual(coefficient(excursions, "P", "P", 4).count, 2)
        self.assertEqual(coefficient(walks, "P", "P", 4).count, 6)
        self.assertEqual(len({w.edge_labels for w in enumerated.witnesses}), len(enumerated.witnesses))
        for length in (1, 3, 5, 7):
            self.assertTrue(coefficient(walks, "P", "P", length).is_zero)

    def test_existing_t33_moment_series_matches_monitor_forgetful_readout(self):
        graph = branching_hidden_cycle_graph()
        _, walks, _ = self.assert_matches_enumeration(graph, ("P", "B"), 6)
        indices, edges = indexed_edges(graph)
        for order in (0, 1, 2):
            matrices = moment_walk_series_coefficients(len(graph.nodes), edges, order, 6)
            for source in walks.ports:
                for target in walks.ports:
                    for length in range(7):
                        for initial in (START, HIT, -1):
                            observed = coefficient(walks, source, target, length, initial)
                            self.assertEqual(observed.moment(order), matrices[length][indices[source]][indices[target]])

    def test_existing_t35_port_kernel_matches_acyclic_hidden_excursions(self):
        z = Fraction(2, 3)
        for graph in blind_pair():
            excursions = port_excursion_series(graph, ("P",), 4)
            _, edges = indexed_edges(graph)
            for order in (0, 1, 2):
                matrix = moment_transition_matrix(len(graph.nodes), edges, order)
                existing = moment_port_kernel_at_z(matrix, (1, 2, 3), z)
                finite_value = sum((coefficient(excursions, "P", "P", length).moment(order) * z ** length
                                    for length in range(1, 5)), Fraction(0))
                # Internal block is a DAG: its first-return polynomial ends at
                # degree four. No extrapolation from finite recurrent prefixes.
                self.assertEqual(existing, ((finite_value,),))

    def test_zero_horizon_has_walk_identity_but_no_empty_excursion(self):
        graph = blind_pair()[0]
        excursions = port_excursion_series(graph, ("P",), 0, budget=0)
        self.assertTrue(excursions.complete)
        self.assertEqual(dict(excursions.coefficients), {})
        walks = compose_port_series(excursions, budget=0)
        self.assertEqual(len(walks.coefficients), 14)
        self.assertEqual(coefficient(walks, "P", "P", 0), ONE)
        self.assertEqual(walks.coefficients, enumerate_port_walks(graph, ("P",), 0, budget=0).coefficients)
        bad = replace(excursions, coefficients={("P", "P", 0, START, START): ONE})
        with self.assertRaisesRegex(ValueError, "strictly positive"):
            compose_port_series(bad)

    def test_truncation_does_not_change_earlier_exact_coefficients(self):
        graph = branching_hidden_cycle_graph()
        short = compose_port_series(port_excursion_series(graph, ("P",), 4))
        long = compose_port_series(port_excursion_series(graph, ("P",), 8))
        self.assertEqual(short.coefficients, {key: value for key, value in long.coefficients.items() if key[2] <= 4})
        with self.assertRaises(ValueError):
            coefficient(short, "P", "P", 5)

    def test_budget_exhaustion_is_not_an_empty_zero_transfer(self):
        graph = blind_pair()[0]
        empty_partial = port_excursion_series(graph, ("P",), 4, budget=0)
        self.assertEqual(empty_partial.status, "INCOMPLETE")
        self.assertEqual(dict(empty_partial.coefficients), {})
        with self.assertRaisesRegex(ValueError, "INCOMPLETE"):
            coefficient(empty_partial, "P", "P", 4)
        with self.assertRaisesRegex(ValueError, "COMPLETE"):
            compose_port_series(empty_partial)
        complete_excursion = port_excursion_series(graph, ("P",), 4)
        partial_walks = compose_port_series(complete_excursion, budget=0)
        self.assertEqual(partial_walks.status, "INCOMPLETE")
        self.assertEqual(partial_walks.complete_through, 3)
        self.assertEqual(len(partial_walks.coefficients), 14)  # only identities
        partial_enum = enumerate_port_walks(graph, ("P",), 4, budget=0)
        self.assertEqual(partial_enum.status, "INCOMPLETE")
        self.assertEqual(partial_enum.complete_through, 0)

    def test_partial_coefficients_are_explicitly_uncertified(self):
        graph = suffix_context_graph()
        partial = port_excursion_series(graph, ("P", "Q", "R"), 2, budget=1)
        self.assertEqual(partial.status, "INCOMPLETE")
        self.assertGreater(len(partial.coefficients), 0)
        self.assertEqual(partial.complete_through, 0)
        with self.assertRaises(ValueError):
            coefficient(partial, "P", "Q", 1)

    def test_input_coordinate_weight_step_and_label_contracts(self):
        with self.assertRaises(ValueError):
            Node("P", (False, 0, 0, 0, 0, 0))
        for weight in (True, 0.5):
            with self.assertRaises(TypeError):
                Edge("bad", "P", "Q", 1, weight)
        for step in (True, 0, 7, 1.0):
            with self.assertRaises(ValueError):
                Edge("bad", "P", "Q", step)
        with self.assertRaises(ValueError):
            Edge("bad", "P", "Q", 1, 0)
        nodes = (Node("P", (0,) * 6), Node("Q", (1, 1, 0, 0, 0, 0)))
        with self.assertRaisesRegex(ValueError, "coordinate difference"):
            NativeGraph(nodes, (Edge("diagonal", "P", "Q", 1),))
        with self.assertRaisesRegex(ValueError, "missing"):
            NativeGraph((nodes[0],), (Edge("missing", "P", "Q", 1),))
        with self.assertRaisesRegex(ValueError, "unique"):
            NativeGraph((nodes[0], nodes[0]), ())
        graph = suffix_context_graph()
        with self.assertRaisesRegex(ValueError, "unique"):
            NativeGraph(graph.nodes, (graph.edges[0], graph.edges[0]))

    def test_freezing_and_ports_do_not_erase_routing_identity(self):
        coordinate = [0] * 6
        node = Node("P", coordinate)
        coordinate[0] = 8
        self.assertEqual(node.coordinate, (0,) * 6)
        graph = suffix_context_graph()
        self.assertEqual(graph.nodes[0].coordinate, graph.nodes[2].coordinate)
        self.assertNotEqual(graph.nodes[0].label, graph.nodes[2].label)
        for ports in ((), ("missing",), ("P", "P")):
            with self.assertRaises(ValueError):
                port_excursion_series(graph, ports, 2)
        for horizon in (-1, True, 1.0):
            with self.assertRaises(ValueError):
                port_excursion_series(graph, ("P",), horizon)
        for budget in (-1, True):
            with self.assertRaises(ValueError):
                port_excursion_series(graph, ("P",), 2, budget=budget)
        walks = compose_port_series(port_excursion_series(graph, ("P", "R"), 2))
        with self.assertRaises(TypeError):
            walks.coefficients[("P", "P", 0, START, START)] = ONE
        with self.assertRaises(ValueError):
            coefficient(walks, "P", "R", 2, initial=1.0)

    def test_independent_verifier_accepts_computed_walks_and_enumerated_walks(self):
        graph = branching_hidden_cycle_graph()
        _, walks, enumerated = self.assert_matches_enumeration(graph, ("P",), 6)
        for series in (walks, enumerated):
            report = verify_port_series(graph, ("P",), 6, series)
            self.assertEqual(report["status"], "VERIFIED")
            self.assertEqual(report["verified_series"].coefficients, series.coefficients)
            self.assertFalse(report["provided_runtime_metadata_and_witnesses_verified"])

    def test_independent_verifier_rejects_forged_histogram_and_deleted_coefficient(self):
        graph = blind_pair()[0]
        walks = compose_port_series(port_excursion_series(graph, ("P",), 4))
        key = ("P", "P", 4, START, HIT)
        wrong = dict(walks.coefficients)
        wrong[key] = WeightHistogram.from_weights([Fraction(4, 11)])
        forged = replace(walks, coefficients=wrong)
        # The convenience readout intentionally cannot authenticate its public
        # container. Only the independent verifier rejects this forged value.
        self.assertEqual(coefficient(forged, "P", "P", 4, final=HIT).total_mass, Fraction(4, 11))
        self.assertEqual(verify_port_series(graph, ("P",), 4, forged)["status"], "REJECTED")
        deleted = dict(walks.coefficients)
        del deleted[key]
        self.assertEqual(verify_port_series(graph, ("P",), 4, replace(walks, coefficients=deleted))["status"], "REJECTED")
        false_complete = replace(walks, coefficients={}, status="COMPLETE", complete_through=4)
        self.assertEqual(verify_port_series(graph, ("P",), 4, false_complete)["status"], "REJECTED")

    def test_independent_verifier_binds_graph_frame_ports_and_horizon(self):
        graph = blind_pair()[0]
        walks = compose_port_series(port_excursion_series(graph, ("P",), 4))
        translated = NativeGraph(tuple(Node(node.label, tuple(value + 10 for value in node.coordinate))
                                       for node in graph.nodes), graph.edges)
        for changes in ({"graph": translated}, {"graph": blind_pair()[1]},
                        {"ports": ("internal:1",)}, {"horizon": 5}, {"horizon": 4.0}):
            with self.subTest(changes=tuple(changes)):
                self.assertEqual(verify_port_series(graph, ("P",), 4, replace(walks, **changes))["status"], "REJECTED")
        extended_label = replace(walks, horizon=8, complete_through=8)
        self.assertEqual(verify_port_series(graph, ("P",), 8, extended_label)["status"], "REJECTED")

    def test_verifier_budget_exhaustion_and_excursions_never_pass(self):
        graph = blind_pair()[0]
        excursions = port_excursion_series(graph, ("P",), 4)
        walks = compose_port_series(excursions)
        report = verify_port_series(graph, ("P",), 4, walks, enumeration_budget=0)
        self.assertEqual(report["status"], "UNVERIFIED")
        self.assertEqual(report["enumeration_status"], "INCOMPLETE")
        empty_forged = replace(walks, coefficients={})
        self.assertEqual(verify_port_series(graph, ("P",), 4, empty_forged, enumeration_budget=0)["status"], "UNVERIFIED")
        self.assertEqual(verify_port_series(graph, ("P",), 4, excursions)["status"], "UNVERIFIED")
        self.assertEqual(verify_port_series(graph, ("P",), 4, replace(walks, status="INCOMPLETE"))["status"], "UNVERIFIED")

    def test_verifier_rejects_malformed_histogram_without_numeric_coercion(self):
        class UncheckedHistogram(WeightHistogram):
            def __post_init__(self):
                pass

        graph = blind_pair()[0]
        walks = compose_port_series(port_excursion_series(graph, ("P",), 4))
        key = ("P", "P", 4, START, HIT)
        for value in (Fraction(2, 11), UncheckedHistogram([[Fraction(2, 11), True]]),
                      UncheckedHistogram([[float(Fraction(2, 11)), 1]])):
            forged = dict(walks.coefficients)
            forged[key] = value
            self.assertEqual(verify_port_series(graph, ("P",), 4, replace(walks, coefficients=forged))["status"], "REJECTED")


if __name__ == "__main__":
    unittest.main()
