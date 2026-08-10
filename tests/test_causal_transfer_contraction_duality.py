import unittest
from fractions import Fraction
from itertools import combinations, product

from enterprise_math.causal_relation_independence import relation_set_is_independent
from enterprise_math.causal_transfer_boundary_contraction import contract_transfer_graph
from enterprise_math.causal_transfer_contraction_duality import (
    contraction_annihilator_condition,
    descend_potential_to_contraction,
    edge_contraction_response_section_identity,
    forest_contraction_probe_rank,
    independent_contraction_rank_drop,
    potential_is_constant_on_forest_components,
    pullback_contracted_potential,
    response_potential_is_valid,
)
from enterprise_math.causal_transfer_graph_geometry import (
    complete_transfer_edges,
    star_transfer_edges,
    transfer_components,
)


def _connected_graphs(slot_count):
    possible = tuple(combinations(range(slot_count), 2))
    for mask in range(1, 1 << len(possible)):
        edges = tuple(edge for index, edge in enumerate(possible) if mask & (1 << index))
        if len(transfer_components(slot_count, edges)) == 1:
            yield edges


class CausalTransferContractionDualityTests(unittest.TestCase):
    def test_every_four_slot_graph_edge_has_exact_response_section_pullback(self):
        for edges in _connected_graphs(4):
            for edge in edges:
                new_n, new_edges, old_to_new = contract_transfer_graph(4, edges, edge)
                for values in product(range(-2, 3), repeat=new_n):
                    psi = tuple(Fraction(value) for value in values)
                    self.assertTrue(
                        edge_contraction_response_section_identity(4, edges, edge, psi)
                    )
                    phi = pullback_contracted_potential(psi, old_to_new)
                    self.assertTrue(contraction_annihilator_condition(phi, edge))
                    self.assertEqual(descend_potential_to_contraction(phi, old_to_new), psi)
                    self.assertEqual(
                        response_potential_is_valid(phi, edges),
                        response_potential_is_valid(psi, new_edges),
                    )

    def test_potential_that_distinguishes_contracted_slots_cannot_descend(self):
        edges = complete_transfer_edges(4)
        edge = (0, 1)
        _, _, old_to_new = contract_transfer_graph(4, edges, edge)
        bad = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
        self.assertFalse(contraction_annihilator_condition(bad, edge))
        with self.assertRaises(ValueError):
            descend_potential_to_contraction(bad, old_to_new)

    def test_each_independent_relation_contraction_removes_one_primal_and_dual_freedom(self):
        for slots in range(2, 7):
            tree = star_transfer_edges(slots, 0)
            for size in range(len(tree) + 1):
                forest = tree[:size]
                self.assertTrue(relation_set_is_independent(slots, forest))
                self.assertEqual(independent_contraction_rank_drop(slots, forest), size)
                self.assertEqual(forest_contraction_probe_rank(slots, forest), slots - size - 1)

    def test_forest_surviving_probes_are_exactly_component_constant(self):
        forest = ((0, 1), (2, 3))
        good = (Fraction(4), Fraction(4), Fraction(-1), Fraction(-1), Fraction(7))
        bad = (Fraction(4), Fraction(3), Fraction(-1), Fraction(-1), Fraction(7))
        self.assertTrue(potential_is_constant_on_forest_components(good, forest))
        self.assertFalse(potential_is_constant_on_forest_components(bad, forest))
        self.assertEqual(forest_contraction_probe_rank(5, forest), 2)
        self.assertEqual(independent_contraction_rank_drop(5, forest), 2)

    def test_complete_and_tree_transfer_laws_share_same_contraction_duality_rule(self):
        for edges in (complete_transfer_edges(4), star_transfer_edges(4, 0)):
            for edge in edges:
                new_n, _, old_to_new = contract_transfer_graph(4, edges, edge)
                psi = tuple(Fraction(index - 1) for index in range(new_n))
                phi = pullback_contracted_potential(psi, old_to_new)
                self.assertEqual(descend_potential_to_contraction(phi, old_to_new), psi)


if __name__ == "__main__":
    unittest.main()
