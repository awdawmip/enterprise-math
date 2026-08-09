import unittest

from enterprise_math.causal_lattice_direction_link import (
    a_all_edge_contexts_uniform,
    a_direction_link_connected,
    a_direction_link_degree,
    a_direction_link_diameter,
    a_direction_link_edge_count,
    a_directions,
    a_edge_common_neighbor_graph_signature,
    a_link_induced_rectangle_count,
    a_link_triangle_count,
    a_shell_orbit_histogram,
    z_direction_count,
    z_direction_link_connected,
    z_direction_link_edge_count,
    z_shell_orbit_histogram,
)


class CausalLatticeDirectionLinkTests(unittest.TestCase):
    def test_a2_first_direction_link_is_six_cycle_data(self):
        p = 2
        self.assertEqual(len(a_directions(p)), 6)
        self.assertEqual(a_direction_link_degree(p), 2)
        self.assertEqual(a_direction_link_edge_count(p), 6)
        self.assertTrue(a_direction_link_connected(p))
        self.assertEqual(a_direction_link_diameter(p), 3)
        self.assertEqual(a_link_triangle_count(p), 0)
        self.assertEqual(a_link_induced_rectangle_count(p), 0)

    def test_a3_first_direction_link_has_cuboctahedral_counts(self):
        p = 3
        self.assertEqual(len(a_directions(p)), 12)
        self.assertEqual(a_direction_link_degree(p), 4)
        self.assertEqual(a_direction_link_edge_count(p), 24)
        self.assertTrue(a_direction_link_connected(p))
        self.assertEqual(a_direction_link_diameter(p), 3)
        self.assertEqual(a_link_triangle_count(p), 8)
        self.assertEqual(a_link_induced_rectangle_count(p), 6)

    def test_every_a3_primitive_edge_has_graph_theoretic_421_context(self):
        signatures = {
            a_edge_common_neighbor_graph_signature(3, direction)
            for direction in a_directions(3)
        }
        self.assertEqual(signatures, {(4, 2, (2, 2))})
        self.assertTrue(a_all_edge_contexts_uniform(3))

    def test_general_a_p_common_neighbor_graph_is_two_equal_cliques(self):
        for p in range(2, 7):
            expected_common = 2 * (p - 1)
            expected_edges = 2 * ((p - 1) * (p - 2) // 2)
            expected_components = (p - 1, p - 1)
            for direction in a_directions(p):
                self.assertEqual(
                    a_edge_common_neighbor_graph_signature(p, direction),
                    (expected_common, expected_edges, expected_components),
                )
            self.assertTrue(a_all_edge_contexts_uniform(p))

    def test_simple_cubic_first_direction_link_is_edgeless(self):
        for p in range(1, 7):
            self.assertEqual(z_direction_count(p), 2 * p)
            self.assertEqual(z_direction_link_edge_count(p), 0)
            self.assertFalse(z_direction_link_connected(p))

    def test_shell_orbit_count_is_not_a_valid_standalone_fcc_isotropy_score(self):
        # At graph radius 2, simple cubic Z^3 has the two types (2) and (1,1),
        # while A_3 has three positive/negative partition-pair types. Thus A_3
        # does not win by naively minimizing higher-shell orbit count.
        z_hist = z_shell_orbit_histogram(3, 2)
        a_hist = a_shell_orbit_histogram(3, 2)
        self.assertEqual(len(z_hist), 2)
        self.assertEqual(len(a_hist), 3)
        self.assertEqual(sorted(z_hist.values()), [6, 12])
        self.assertEqual(sorted(a_hist.values()), [6, 12, 24])
        self.assertEqual(sum(z_hist.values()), 18)
        self.assertEqual(sum(a_hist.values()), 42)

    def test_a3_shell_two_exact_orbit_types(self):
        histogram = a_shell_orbit_histogram(3, 2)
        self.assertEqual(
            histogram,
            {
                ((1, 1), (1, 1)): 6,
                ((1, 1), (2,)): 24,
                ((2,), (2,)): 12,
            },
        )


if __name__ == "__main__":
    unittest.main()
