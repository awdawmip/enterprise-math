import unittest

from enterprise_math.causal_close_packed_contact import (
    bond_common_neighbor_signature,
    close_packed_point,
    fcc_bond_signature_histogram,
    fcc_bonds_are_single_context,
    fcc_registry,
    hcp_bond_signature_histogram,
    hcp_bonds_split_into_two_contexts,
    hcp_registry,
    local_close_packed_points,
    point_neighbors,
)


class CausalClosePackedContactTests(unittest.TestCase):
    def test_fcc_and_hcp_both_have_twelve_primitive_contacts(self):
        for registry in (fcc_registry, hcp_registry):
            points = local_close_packed_points(registry, 4, 4)
            center = close_packed_point(0, 0, 0, registry)
            self.assertEqual(len(point_neighbors(center, points)), 12)

    def test_fcc_every_primitive_bond_has_the_same_421_graph_context(self):
        self.assertEqual(
            fcc_bond_signature_histogram(),
            {(4, 2, (2, 2), (1, 1, 1, 1)): 12},
        )
        self.assertTrue(fcc_bonds_are_single_context())

    def test_hcp_splits_six_421_and_six_422_graph_contexts(self):
        self.assertEqual(
            hcp_bond_signature_histogram(),
            {
                (4, 2, (2, 2), (1, 1, 1, 1)): 6,
                (4, 2, (3, 1), (0, 1, 1, 2)): 6,
            },
        )
        self.assertTrue(hcp_bonds_split_into_two_contexts())

    def test_hcp_context_split_is_not_coordination_or_common_neighbor_count(self):
        points = local_close_packed_points(hcp_registry, 4, 4)
        center = close_packed_point(0, 0, 0, hcp_registry)
        signatures = [
            bond_common_neighbor_signature(center, neighbor, points)
            for neighbor in point_neighbors(center, points)
        ]
        self.assertEqual({signature[0] for signature in signatures}, {4})
        self.assertEqual({signature[1] for signature in signatures}, {2})
        self.assertEqual(
            {signature[2] for signature in signatures},
            {(2, 2), (3, 1)},
        )


if __name__ == "__main__":
    unittest.main()
