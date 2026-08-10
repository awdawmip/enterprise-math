import unittest
from itertools import combinations

from enterprise_math.causal_relation_independence import (
    basis_exchange_witness,
    is_spanning_relation_basis,
    maximal_independent_size,
    relation_independence_profile,
    relation_nullity,
    relation_set_is_independent,
    relation_set_rank,
    spanning_relation_bases,
)
from enterprise_math.causal_transfer_graph_geometry import (
    complete_transfer_edges,
    star_transfer_edges,
)


class CausalRelationIndependenceTests(unittest.TestCase):
    def test_forest_exactly_matches_contraction_independence(self):
        slot_count = 4
        all_edges = complete_transfer_edges(slot_count)
        for size in range(len(all_edges) + 1):
            for subset in combinations(all_edges, size):
                rank = relation_set_rank(slot_count, subset)
                self.assertEqual(relation_set_is_independent(slot_count, subset), rank == size)
                self.assertEqual(relation_nullity(slot_count, subset), size - rank)

    def test_connected_geometry_dimension_is_size_of_every_spanning_relation_basis(self):
        for slots in range(2, 7):
            complete = complete_transfer_edges(slots)
            star = star_transfer_edges(slots, 0)
            self.assertEqual(maximal_independent_size(slots, complete), slots - 1)
            self.assertEqual(maximal_independent_size(slots, star), slots - 1)
            self.assertTrue(is_spanning_relation_basis(slots, complete, star))
            self.assertTrue(is_spanning_relation_basis(slots, star, star))

    def test_complete_graph_basis_count_matches_cayley_tree_count(self):
        for slots in range(2, 7):
            bases = spanning_relation_bases(slots, complete_transfer_edges(slots))
            self.assertEqual(len(bases), slots ** (slots - 2))
            profile = relation_independence_profile(slots, complete_transfer_edges(slots))
            self.assertEqual(profile.basis_count, slots ** (slots - 2))
            self.assertEqual(profile.relation_rank, slots - 1)
            self.assertEqual(
                profile.cycle_nullity,
                (slots - 1) * (slots - 2) // 2,
            )

    def test_basis_exchange_is_constructive(self):
        slots = 5
        allowed = complete_transfer_edges(slots)
        bases = spanning_relation_bases(slots, allowed)
        left = bases[0]
        right = next(basis for basis in bases if set(basis) != set(left))
        difference = sorted(set(left) - set(right))
        for removed in difference:
            candidate = basis_exchange_witness(slots, allowed, left, right, removed)
            self.assertIsNotNone(candidate)
            trial = tuple(sorted((set(left) - {removed}) | {candidate}))
            self.assertTrue(is_spanning_relation_basis(slots, allowed, trial))

    def test_simple_cubic_tree_is_one_chart_among_many_fcc_relation_bases(self):
        slots = 4
        allowed = complete_transfer_edges(slots)
        star = star_transfer_edges(slots, hub=0)
        self.assertTrue(is_spanning_relation_basis(slots, allowed, star))
        self.assertEqual(len(spanning_relation_bases(slots, allowed)), 16)
        self.assertEqual(relation_independence_profile(slots, star).basis_count, 1)
        self.assertEqual(relation_independence_profile(slots, allowed).basis_count, 16)


if __name__ == "__main__":
    unittest.main()
