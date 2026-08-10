import unittest
from itertools import product

from enterprise_math.material_ledger_future_transfer_precision import (
    compartments_future_indistinguishable,
    future_transfer_precision_partition,
    future_transfer_precision_report,
    future_transfer_precision_signature,
    reconstruct_future_component_totals,
)
from enterprise_math.material_ledger_transfer_graph import (
    transfer_graph_components,
)


class MaterialLedgerFutureTransferPrecisionTests(unittest.TestCase):
    def test_future_edge_removal_can_make_current_connected_total_unsafe(self):
        compartments = ("P", "Q", "X")
        current = (("P", "Q"), ("Q", "X"))
        future = (
            current,
            (("P", "Q"),),
        )
        report = future_transfer_precision_report(
            compartments,
            current,
            future,
        )
        self.assertEqual(report.current_invariant_rank, 1)
        self.assertEqual(report.required_future_safe_rank, 2)
        self.assertFalse(report.current_component_totals_are_future_safe)
        self.assertEqual(
            set(report.future_meet_components),
            {frozenset({"P", "Q"}), frozenset({"X"})},
        )

        left = {"P": 1, "Q": 0, "X": 0}
        right = {"P": 0, "Q": 0, "X": 1}
        self.assertEqual(sum(left.values()), sum(right.values()))
        self.assertNotEqual(
            future_transfer_precision_signature(compartments, future, left),
            future_transfer_precision_signature(compartments, future, right),
        )

    def test_future_merging_does_not_make_finer_current_totals_unsafe(self):
        compartments = ("P", "Q", "X")
        current = (("P", "Q"),)
        future = (
            (("P", "Q"), ("Q", "X")),
        )
        report = future_transfer_precision_report(
            compartments,
            current,
            future,
        )
        self.assertEqual(report.current_invariant_rank, 2)
        self.assertEqual(report.required_future_safe_rank, 1)
        self.assertTrue(report.current_component_totals_are_future_safe)

    def test_meet_is_intersection_of_connectivity_relations_not_edge_sets(self):
        compartments = (0, 1, 2)
        first = ((0, 1), (1, 2))
        second = ((0, 2), (2, 1))
        self.assertEqual(
            transfer_graph_components(compartments, first),
            (frozenset({0, 1, 2}),),
        )
        self.assertEqual(
            transfer_graph_components(compartments, second),
            (frozenset({0, 1, 2}),),
        )
        # The literal edge intersection contains only (1,2), but every vertex
        # is connected to every other in each possible future graph.  The meet
        # of connectivity equivalences is therefore still one block.
        meet = future_transfer_precision_partition(
            compartments,
            (first, second),
        )
        self.assertEqual(meet, (frozenset({0, 1, 2}),))

    def test_totally_disconnected_possible_future_forces_full_current_ledger(self):
        compartments = (0, 1, 2, 3)
        future = (
            ((0, 1), (1, 2), (2, 3)),
            (),
        )
        meet = future_transfer_precision_partition(compartments, future)
        self.assertEqual(
            set(meet),
            {frozenset({0}), frozenset({1}), frozenset({2}), frozenset({3})},
        )
        for left in compartments:
            for right in compartments:
                self.assertEqual(
                    compartments_future_indistinguishable(
                        compartments,
                        future,
                        left,
                        right,
                    ),
                    left == right,
                )

    def test_future_component_totals_reconstruct_from_meet_block_totals(self):
        compartments = (0, 1, 2, 3, 4)
        future = (
            ((0, 1), (1, 2), (3, 4)),
            ((0, 1), (2, 3), (3, 4)),
            ((0, 4), (1, 2), (2, 3)),
        )
        for values in product(range(3), repeat=len(compartments)):
            ledger = dict(zip(compartments, values, strict=True))
            for index in range(len(future)):
                reconstructed = reconstruct_future_component_totals(
                    compartments,
                    future,
                    ledger,
                    index,
                )
                direct_components = transfer_graph_components(
                    compartments,
                    future[index],
                )
                direct = tuple(
                    sum(ledger[vertex] for vertex in component)
                    for component in direct_components
                )
                self.assertEqual(reconstructed, direct)

    def test_unit_placements_are_merged_exactly_when_future_indistinguishable(self):
        compartments = (0, 1, 2, 3)
        future = (
            ((0, 1), (2, 3)),
            ((0, 1), (1, 2), (2, 3)),
        )
        meet = future_transfer_precision_partition(compartments, future)
        self.assertEqual(
            set(meet),
            {frozenset({0, 1}), frozenset({2, 3})},
        )
        signatures = {}
        for vertex in compartments:
            ledger = {item: int(item == vertex) for item in compartments}
            signatures[vertex] = future_transfer_precision_signature(
                compartments,
                future,
                ledger,
            )
        self.assertEqual(signatures[0], signatures[1])
        self.assertEqual(signatures[2], signatures[3])
        self.assertNotEqual(signatures[0], signatures[2])

    def test_current_safety_criterion_matches_direct_partition_refinement(self):
        compartments = (0, 1, 2)
        possible_edges = ((0, 1), (1, 2), (0, 2))
        graphs = tuple(
            tuple(
                edge
                for index, edge in enumerate(possible_edges)
                if mask & (1 << index)
            )
            for mask in range(1 << len(possible_edges))
        )
        for current in graphs:
            current_components = transfer_graph_components(
                compartments,
                current,
            )
            for first in graphs:
                for second in graphs:
                    future = (first, second)
                    meet = future_transfer_precision_partition(
                        compartments,
                        future,
                    )
                    expected = all(
                        any(component.issubset(block) for block in meet)
                        for component in current_components
                    )
                    report = future_transfer_precision_report(
                        compartments,
                        current,
                        future,
                    )
                    self.assertEqual(
                        report.current_component_totals_are_future_safe,
                        expected,
                    )

    def test_validation(self):
        with self.assertRaises(ValueError):
            future_transfer_precision_partition((), ((),))
        with self.assertRaises(ValueError):
            future_transfer_precision_partition((0, 1), ())
        with self.assertRaises(ValueError):
            future_transfer_precision_signature(
                (0, 1),
                ((),),
                {0: 1},
            )
        with self.assertRaises(ValueError):
            reconstruct_future_component_totals(
                (0, 1),
                ((),),
                {0: 1, 1: 0},
                2,
            )
        with self.assertRaises(ValueError):
            compartments_future_indistinguishable(
                (0, 1),
                ((),),
                0,
                2,
            )


if __name__ == "__main__":
    unittest.main()
