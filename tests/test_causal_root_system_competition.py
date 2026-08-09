import unittest

from enterprise_math.causal_root_system_competition import (
    all_primitive_edge_contexts_uniform,
    d_direction_count,
    d_direction_link_degree,
    d_edge_context_closed,
    d_roots,
    e8_local_context_closed,
    e8_roots_scaled,
    primitive_edge_context,
    primitive_link_degree_set,
    root_system_local_profile,
)


class CausalRootSystemCompetitionTests(unittest.TestCase):
    def test_d3_recovers_a3_fcc_local_edge_context(self):
        roots = d_roots(3)
        self.assertEqual(len(roots), 12)
        self.assertEqual(primitive_link_degree_set(roots), (4,))
        self.assertEqual(primitive_edge_context(roots, roots[0]), (4, 2, (2, 2), ((1, 4),)))
        self.assertEqual(d_edge_context_closed(3), (4, 2, (2, 2), ((1, 4),)))
        self.assertTrue(all_primitive_edge_contexts_uniform(roots))

    def test_d_n_closed_local_formulas_match_integer_enumeration(self):
        for n in range(3, 8):
            roots = d_roots(n)
            self.assertEqual(len(roots), d_direction_count(n))
            self.assertEqual(primitive_link_degree_set(roots), (d_direction_link_degree(n),))
            expected = d_edge_context_closed(n)
            self.assertEqual(primitive_edge_context(roots, roots[0]), expected)
            self.assertTrue(all_primitive_edge_contexts_uniform(roots))

    def test_d4_has_richer_first_relation_context_than_a3_fcc(self):
        profile = root_system_local_profile(d_roots(4))
        self.assertEqual(profile[0], 24)
        self.assertEqual(profile[1], 8)
        self.assertEqual(profile[2], (8, 12, (8,), ((3, 8),)))
        self.assertTrue(profile[3])

    def test_scaled_e8_has_uniform_240_root_local_context(self):
        roots = e8_roots_scaled()
        self.assertEqual(len(roots), 240)
        self.assertEqual(primitive_link_degree_set(roots), (56,))
        self.assertEqual(primitive_edge_context(roots, roots[0]), e8_local_context_closed())
        self.assertTrue(all_primitive_edge_contexts_uniform(roots))
        self.assertEqual(
            root_system_local_profile(roots),
            (240, 56, (56, 756, (56,), ((27, 56),)), True),
        )

    def test_local_uniformity_does_not_select_one_universal_root_family(self):
        self.assertTrue(all_primitive_edge_contexts_uniform(d_roots(4)))
        self.assertTrue(all_primitive_edge_contexts_uniform(d_roots(5)))
        self.assertTrue(all_primitive_edge_contexts_uniform(e8_roots_scaled()))


if __name__ == "__main__":
    unittest.main()
