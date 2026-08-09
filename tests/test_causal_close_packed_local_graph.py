import unittest

from enterprise_math.causal_close_packed_local_graph import (
    close_packed_neighbors,
    fcc_hcp_edge_contexts_distinguish,
    fcc_hcp_first_link_indistinguishable_by_coarse_counts,
    origin_bond_context_by_layer_offset,
    origin_bond_context_histogram,
    origin_direction_link_signature,
)


class CausalClosePackedLocalGraphTests(unittest.TestCase):
    def test_fcc_and_hcp_both_have_twelve_primitive_neighbors(self):
        origin = (0, 0, 0)
        self.assertEqual(len(close_packed_neighbors(origin, "fcc")), 12)
        self.assertEqual(len(close_packed_neighbors(origin, "hcp")), 12)

    def test_first_direction_link_coarse_graph_counts_do_not_separate_fcc_hcp(self):
        expected = (12, 24, ((4, 12),), 8, (12,))
        self.assertEqual(origin_direction_link_signature("fcc"), expected)
        self.assertEqual(origin_direction_link_signature("hcp"), expected)
        self.assertTrue(fcc_hcp_first_link_indistinguishable_by_coarse_counts())

    def test_second_local_bond_context_separates_fcc_hcp_exactly(self):
        context_421 = (4, 2, (2, 2))
        context_422 = (4, 2, (3, 1))
        self.assertEqual(
            origin_bond_context_histogram("fcc"),
            {context_421: 12},
        )
        self.assertEqual(
            origin_bond_context_histogram("hcp"),
            {context_421: 6, context_422: 6},
        )
        self.assertTrue(fcc_hcp_edge_contexts_distinguish())

    def test_hcp_context_split_is_layer_orientation_split(self):
        context_421 = (4, 2, (2, 2))
        context_422 = (4, 2, (3, 1))
        by_layer = origin_bond_context_by_layer_offset("hcp")
        self.assertEqual(by_layer[(0, context_422)], 6)
        self.assertEqual(by_layer[(1, context_421)], 3)
        self.assertEqual(by_layer[(-1, context_421)], 3)
        self.assertEqual(sum(by_layer.values()), 12)

    def test_fcc_context_is_uniform_across_in_plane_and_interlayer_bonds(self):
        context_421 = (4, 2, (2, 2))
        by_layer = origin_bond_context_by_layer_offset("fcc")
        self.assertEqual(by_layer[(0, context_421)], 6)
        self.assertEqual(by_layer[(1, context_421)], 3)
        self.assertEqual(by_layer[(-1, context_421)], 3)
        self.assertEqual(sum(by_layer.values()), 12)


if __name__ == "__main__":
    unittest.main()
