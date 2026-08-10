import unittest
from itertools import product

from enterprise_math.material_ledger_transfer_graph import (
    apply_ledger_transfer,
    component_total_signature,
    ledger_transfer_invariant_report,
    scalar_weights_transfer_invariant,
    transfer_graph_components,
    weights_constant_on_transfer_components,
)


class MaterialLedgerTransferGraphTests(unittest.TestCase):
    def test_pqx_policy_subgraphs_have_expected_invariant_ranks(self):
        compartments = ("P", "Q", "X")

        none = transfer_graph_components(compartments, ())
        scheduler = transfer_graph_components(compartments, (("Q", "P"),))
        expiry = transfer_graph_components(compartments, (("Q", "X"),))
        both = transfer_graph_components(
            compartments,
            (("Q", "P"), ("Q", "X")),
        )

        self.assertEqual(len(none), 3)
        self.assertEqual(len(scheduler), 2)
        self.assertEqual(len(expiry), 2)
        self.assertEqual(len(both), 1)
        self.assertIn(frozenset({"P", "Q"}), scheduler)
        self.assertIn(frozenset({"X"}), scheduler)
        self.assertIn(frozenset({"P"}), expiry)
        self.assertIn(frozenset({"Q", "X"}), expiry)
        self.assertEqual(both, (frozenset({"P", "Q", "X"}),))

    def test_component_totals_reproduce_applied_live_ever_boundaries(self):
        ledger = {"P": 2, "Q": 5, "X": 3}
        compartments = tuple(ledger)

        self.assertEqual(
            sorted(component_total_signature(compartments, (), ledger)),
            [2, 3, 5],
        )
        scheduler = component_total_signature(
            compartments,
            (("Q", "P"),),
            ledger,
        )
        self.assertEqual(set(scheduler), {7, 3})
        expiry = component_total_signature(
            compartments,
            (("Q", "X"),),
            ledger,
        )
        self.assertEqual(set(expiry), {2, 8})
        both = component_total_signature(
            compartments,
            (("Q", "P"), ("Q", "X")),
            ledger,
        )
        self.assertEqual(both, (10,))

    def test_edge_invariance_iff_weights_constant_on_components_exhaustively(self):
        compartments = (0, 1, 2, 3)
        possible_edges = (
            (0, 1),
            (1, 2),
            (2, 3),
            (0, 3),
        )
        edge_families = tuple(
            tuple(
                edge
                for index, edge in enumerate(possible_edges)
                if mask & (1 << index)
            )
            for mask in range(1 << len(possible_edges))
        )
        for edges in edge_families:
            for values in product(range(-1, 2), repeat=4):
                weights = dict(zip(compartments, values, strict=True))
                edge_check = scalar_weights_transfer_invariant(
                    compartments,
                    edges,
                    weights,
                )
                component_check = weights_constant_on_transfer_components(
                    compartments,
                    edges,
                    weights,
                )
                self.assertEqual(edge_check, component_check)
                report = ledger_transfer_invariant_report(
                    compartments,
                    edges,
                    weights,
                )
                self.assertEqual(
                    report.independent_linear_invariant_rank,
                    len(report.components),
                )
                self.assertEqual(report.weights_edge_invariant, edge_check)

    def test_connected_transfer_graph_allows_only_constant_small_weights(self):
        compartments = ("A", "B", "C", "D")
        edges = (("A", "B"), ("B", "C"), ("C", "D"))
        for values in product(range(-2, 3), repeat=4):
            weights = dict(zip(compartments, values, strict=True))
            self.assertEqual(
                scalar_weights_transfer_invariant(
                    compartments,
                    edges,
                    weights,
                ),
                len(set(values)) == 1,
            )

    def test_allowed_transfers_preserve_component_total_signature(self):
        compartments = ("P", "Q", "X", "Z")
        edges = (("Q", "P"), ("Q", "X"))
        ledger = {"P": 1, "Q": 6, "X": 2, "Z": 9}
        signature = component_total_signature(compartments, edges, ledger)

        after_apply = apply_ledger_transfer(
            compartments,
            edges,
            ledger,
            ("Q", "P"),
            4,
        )
        after_expire = apply_ledger_transfer(
            compartments,
            edges,
            after_apply,
            ("Q", "X"),
            2,
        )
        self.assertEqual(
            component_total_signature(compartments, edges, after_apply),
            signature,
        )
        self.assertEqual(
            component_total_signature(compartments, edges, after_expire),
            signature,
        )
        self.assertEqual(after_expire["Z"], 9)

    def test_direction_of_transfer_does_not_change_linear_invariant_space(self):
        compartments = (0, 1, 2)
        forward = ((0, 1), (1, 2))
        reversed_edges = ((1, 0), (2, 1))
        for weights_tuple in product(range(-1, 2), repeat=3):
            weights = dict(zip(compartments, weights_tuple, strict=True))
            self.assertEqual(
                scalar_weights_transfer_invariant(
                    compartments,
                    forward,
                    weights,
                ),
                scalar_weights_transfer_invariant(
                    compartments,
                    reversed_edges,
                    weights,
                ),
            )

    def test_disconnected_transfer_components_retain_one_total_each(self):
        compartments = (0, 1, 2, 3, 4)
        edges = ((0, 1), (1, 2), (3, 4))
        components = transfer_graph_components(compartments, edges)
        self.assertEqual(
            set(components),
            {frozenset({0, 1, 2}), frozenset({3, 4})},
        )
        report = ledger_transfer_invariant_report(
            compartments,
            edges,
            {0: 5, 1: 5, 2: 5, 3: -2, 4: -2},
        )
        self.assertTrue(report.weights_edge_invariant)
        self.assertEqual(report.independent_linear_invariant_rank, 2)

    def test_validation(self):
        with self.assertRaises(ValueError):
            transfer_graph_components((), ())
        with self.assertRaises(ValueError):
            transfer_graph_components((0, 0), ())
        with self.assertRaises(ValueError):
            transfer_graph_components((0, 1), ((0, 2),))
        with self.assertRaises(ValueError):
            transfer_graph_components((0, 1), ((0, 0),))
        with self.assertRaises(ValueError):
            scalar_weights_transfer_invariant(
                (0, 1),
                ((0, 1),),
                {0: 1},
            )
        with self.assertRaises(TypeError):
            scalar_weights_transfer_invariant(
                (0, 1),
                ((0, 1),),
                {0: 1, 1: False},
            )
        with self.assertRaises(ValueError):
            apply_ledger_transfer(
                (0, 1),
                ((0, 1),),
                {0: 0, 1: 0},
                (0, 1),
                1,
            )


if __name__ == "__main__":
    unittest.main()
