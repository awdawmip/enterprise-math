import unittest

from enterprise_math.causal_e8_direction_link import (
    e8_all_edge_contexts_uniform,
    e8_direction_link_connected,
    e8_direction_link_degree,
    e8_direction_link_edge_count,
    e8_edge_common_neighbor_signature,
    e8_root_count,
    e8_scaled_roots,
)


class CausalE8DirectionLinkTests(unittest.TestCase):
    def test_scaled_integer_root_construction_has_240_unique_roots(self):
        roots = e8_scaled_roots()
        self.assertEqual(len(roots), 240)
        self.assertEqual(len(set(roots)), 240)
        self.assertEqual(e8_root_count(), 240)
        self.assertTrue(
            all(
                all(isinstance(value, int) for value in root)
                for root in roots
            )
        )

    def test_e8_direction_link_exact_counts(self):
        self.assertEqual(e8_direction_link_degree(), 56)
        self.assertEqual(e8_direction_link_edge_count(), 6720)
        self.assertTrue(e8_direction_link_connected())

    def test_fixed_e8_edge_common_neighbor_graph_is_connected_27_regular(self):
        signature = e8_edge_common_neighbor_signature()
        self.assertEqual(signature[0], 56)
        self.assertEqual(signature[1], 756)
        self.assertEqual(signature[2], (56,))
        self.assertEqual(signature[3], ((27, 56),))

    def test_all_e8_primitive_edges_have_same_context(self):
        self.assertTrue(e8_all_edge_contexts_uniform())

    def test_e8_is_a_real_competitor_not_an_a_family_relabel(self):
        # A_8 would have 8*9=72 primitive directions and link degree 14.
        # E8 instead has 240 roots and degree 56; the local causal diagnostics
        # therefore leave room for dimension-specific exceptional candidates.
        self.assertGreater(e8_root_count(), 8 * 9)
        self.assertGreater(e8_direction_link_degree(), 2 * (8 - 1))


if __name__ == "__main__":
    unittest.main()
