import unittest
from itertools import combinations

from enterprise_math.conflict_future_signature import (
    compile_conflict_future_signature,
    conflict_future_succeeds,
    is_vertex_cover,
)


def all_edges(labels):
    return tuple(combinations(labels, 2))


def full_future_signature(labels, edges, horizon):
    return tuple(
        (removed, is_vertex_cover(edges, removed))
        for count in range(horizon + 1)
        for removed in combinations(labels, count)
    )


class ConflictFutureSignatureTests(unittest.TestCase):
    def test_antichain_signature_evaluates_every_allowed_deletion(self):
        labels = (0, 1, 2, 3)
        edges = ((0, 1), (1, 2), (2, 3))
        for horizon in range(len(labels)):
            signature = compile_conflict_future_signature(labels, edges, horizon)
            for count in range(horizon + 1):
                for removed in combinations(labels, count):
                    self.assertEqual(
                        conflict_future_succeeds(signature, removed),
                        is_vertex_cover(edges, removed),
                    )

    def test_empty_graph_has_empty_cover_as_unique_minimum_success(self):
        signature = compile_conflict_future_signature((0, 1, 2), (), 2)
        self.assertEqual(signature.minimal_successful_deletions, (frozenset(),))
        for count in range(3):
            for removed in combinations((0, 1, 2), count):
                self.assertTrue(conflict_future_succeeds(signature, removed))

    def test_horizon_below_vertex_cover_number_collapses_all_graphs_to_all_false_signature(self):
        labels = (0, 1, 2, 3)
        cycle = ((0, 1), (1, 2), (2, 3), (0, 3))
        complete = all_edges(labels)
        cycle_signature = compile_conflict_future_signature(labels, cycle, 1)
        complete_signature = compile_conflict_future_signature(labels, complete, 1)
        self.assertEqual(cycle_signature.minimal_successful_deletions, ())
        self.assertEqual(complete_signature.minimal_successful_deletions, ())
        self.assertEqual(cycle_signature, complete_signature)

    def test_path_minimal_cover_antichain_is_exact(self):
        labels = (0, 1, 2)
        edges = ((0, 1), (1, 2))
        signature = compile_conflict_future_signature(labels, edges, 2)
        self.assertEqual(
            signature.minimal_successful_deletions,
            (frozenset({1}), frozenset({0, 2})),
        )
        self.assertTrue(conflict_future_succeeds(signature, (1,)))
        self.assertTrue(conflict_future_succeeds(signature, (0, 2)))
        self.assertFalse(conflict_future_succeeds(signature, (0,)))

    def test_signature_partition_equals_complete_future_partition_on_all_small_graphs(self):
        # Fixed labels make the antichain a canonical extensional representation
        # of the horizon-bounded Boolean deletion function.
        for label_count in range(1, 6):
            labels = tuple(range(label_count))
            edge_universe = tuple(combinations(labels, 2))
            graph_count = 1 << len(edge_universe)
            for horizon in range(label_count):
                compact_to_full = {}
                full_to_compact = {}
                for mask in range(graph_count):
                    edges = tuple(
                        edge
                        for index, edge in enumerate(edge_universe)
                        if mask & (1 << index)
                    )
                    compact = compile_conflict_future_signature(
                        labels, edges, horizon
                    )
                    full = full_future_signature(labels, edges, horizon)
                    compact_to_full.setdefault(compact, set()).add(full)
                    full_to_compact.setdefault(full, set()).add(compact)
                self.assertTrue(
                    all(len(outputs) == 1 for outputs in compact_to_full.values())
                )
                self.assertTrue(
                    all(len(signatures) == 1 for signatures in full_to_compact.values())
                )

    def test_invalid_graph_or_deletion_is_rejected(self):
        with self.assertRaises(ValueError):
            compile_conflict_future_signature((0, 1), ((0, 2),), 1)
        with self.assertRaises(ValueError):
            compile_conflict_future_signature((0, 1), ((0, 0),), 1)
        signature = compile_conflict_future_signature((0, 1), ((0, 1),), 1)
        with self.assertRaises(ValueError):
            conflict_future_succeeds(signature, (0, 1))
        with self.assertRaises(ValueError):
            conflict_future_succeeds(signature, (99,))


if __name__ == "__main__":
    unittest.main()
