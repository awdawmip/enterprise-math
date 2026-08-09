import unittest

from enterprise_math.causal_d_lattice_direction_link import (
    d_all_edge_contexts_uniform,
    d_direction_link_connected,
    d_direction_link_degree,
    d_direction_link_edge_count,
    d_edge_common_neighbor_signature,
    d_expected_common_neighbor_count,
    d_expected_common_neighbor_internal_edges,
    d_root_count,
    d_roots,
)


class CausalDLatticeDirectionLinkTests(unittest.TestCase):
    def test_d3_reproduces_a3_fcc_local_counts(self):
        n = 3
        self.assertEqual(d_root_count(n), 12)
        self.assertEqual(d_direction_link_degree(n), 4)
        self.assertEqual(d_direction_link_edge_count(n), 24)
        self.assertTrue(d_direction_link_connected(n))
        signatures = {
            d_edge_common_neighbor_signature(n, root)
            for root in d_roots(n)
        }
        self.assertEqual(signatures, {(4, 2, (2, 2))})

    def test_d4_is_a_distinct_higher_dimensional_competitor(self):
        n = 4
        self.assertEqual(d_root_count(n), 24)
        self.assertEqual(d_direction_link_degree(n), 8)
        self.assertEqual(d_direction_link_edge_count(n), 96)
        self.assertTrue(d_direction_link_connected(n))
        signatures = {
            d_edge_common_neighbor_signature(n, root)
            for root in d_roots(n)
        }
        self.assertEqual(signatures, {(8, 12, (8,))})
        self.assertTrue(d_all_edge_contexts_uniform(n))

    def test_general_d_n_counts_and_uniform_edge_contexts(self):
        for n in range(3, 8):
            self.assertEqual(len(d_roots(n)), 2 * n * (n - 1))
            self.assertEqual(d_direction_link_degree(n), 4 * (n - 2))
            self.assertTrue(d_direction_link_connected(n))
            self.assertTrue(d_all_edge_contexts_uniform(n))
            for root in d_roots(n):
                common, edges, components = d_edge_common_neighbor_signature(n, root)
                self.assertEqual(common, d_expected_common_neighbor_count(n))
                self.assertEqual(edges, d_expected_common_neighbor_internal_edges(n))
                if n == 3:
                    self.assertEqual(components, (2, 2))
                else:
                    self.assertEqual(components, (common,))

    def test_d4_has_richer_first_link_than_a4_counts_without_claiming_global_optimality(self):
        # A_4 has p(p+1)=20 primitive directions and link degree 2(p-1)=6.
        # D_4 has 24 directions and degree 8, so the proposed local diagnostics
        # admit a real high-dimensional competitor rather than hard-coding A_p.
        self.assertEqual(d_root_count(4), 24)
        self.assertEqual(d_direction_link_degree(4), 8)
        self.assertGreater(d_root_count(4), 4 * 5)
        self.assertGreater(d_direction_link_degree(4), 2 * (4 - 1))


if __name__ == "__main__":
    unittest.main()
