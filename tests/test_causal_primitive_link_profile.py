import unittest

from enterprise_math.causal_primitive_link_profile import (
    a_roots,
    d_roots,
    e6_scaled_roots,
    e7_scaled_roots,
    e8_scaled_roots,
    flag_extension_histograms,
    neighborhood_signature,
    pair_context_histogram,
    primitive_direction_graph,
    primitive_link_profile,
)


class CausalPrimitiveLinkProfileTests(unittest.TestCase):
    def test_a3_fcc_profile_is_uniform_but_not_distance_context_uniform(self):
        profile = primitive_link_profile(a_roots(3))
        self.assertEqual(profile.primitive_count, 12)
        self.assertEqual(profile.link_degree_histogram, ((4, 12),))
        self.assertEqual(profile.link_edge_count, 24)
        self.assertEqual(profile.link_component_sizes, (12,))
        self.assertEqual(profile.link_diameter, 3)
        self.assertEqual(len(profile.edge_context_histogram), 1)
        signature, multiplicity = profile.edge_context_histogram[0]
        self.assertEqual(multiplicity, 12)
        self.assertEqual(signature[:4], (4, 2, ((1, 4),), (2, 2)))
        self.assertEqual(
            dict(profile.pair_context_histogram),
            {(1, 1): 24, (2, 1): 24, (2, 2): 12, (3, 0): 6},
        )
        self.assertEqual(
            tuple(dict(hist) for hist in profile.flag_extension_histograms),
            ({4: 12}, {1: 24}, {0: 8}),
        )
        self.assertIsNone(profile.first_flag_split_order)

    def test_a4_and_d4_are_both_locally_uniform_but_have_different_flag_laws(self):
        a4 = primitive_link_profile(a_roots(4))
        d4 = primitive_link_profile(d_roots(4))
        self.assertEqual(a4.link_degree_histogram, ((6, 20),))
        self.assertEqual(d4.link_degree_histogram, ((8, 24),))
        self.assertEqual(len(a4.edge_context_histogram), 1)
        self.assertEqual(len(d4.edge_context_histogram), 1)
        self.assertEqual(
            tuple(dict(hist) for hist in a4.flag_extension_histograms),
            ({6: 20}, {2: 60}, {1: 40}, {0: 10}),
        )
        self.assertEqual(
            tuple(dict(hist) for hist in d4.flag_extension_histograms),
            ({8: 24}, {3: 96}, {0: 96}),
        )

    def test_d5_first_higher_order_flag_split_occurs_at_triangles(self):
        profile = primitive_link_profile(d_roots(5), maximum_flag_size=4)
        self.assertEqual(profile.primitive_count, 40)
        self.assertEqual(profile.link_degree_histogram, ((12, 40),))
        self.assertEqual(
            tuple(dict(hist) for hist in profile.flag_extension_histograms),
            ({12: 40}, {5: 240}, {0: 80, 2: 320}, {0: 160}),
        )
        self.assertEqual(profile.first_flag_split_order, 3)

    def test_e6_is_flag_uniform_through_its_maximal_compatible_flags(self):
        profile = primitive_link_profile(e6_scaled_roots())
        self.assertEqual(profile.primitive_count, 72)
        self.assertEqual(profile.link_degree_histogram, ((20, 72),))
        self.assertEqual(len(profile.edge_context_histogram), 1)
        self.assertEqual(
            tuple(dict(hist) for hist in profile.flag_extension_histograms),
            ({20: 72}, {9: 720}, {4: 2160}, {1: 2160}, {0: 432}),
        )
        self.assertIsNone(profile.first_flag_split_order)

    def test_exceptional_root_counts_and_low_order_contexts(self):
        self.assertEqual(len(e6_scaled_roots()), 72)
        self.assertEqual(len(e7_scaled_roots()), 126)
        self.assertEqual(len(e8_scaled_roots()), 240)

        expected = {
            "E6": (e6_scaled_roots(), 20, (20, 90, ((9, 20),), (20,), 3)),
            "E7": (e7_scaled_roots(), 32, (32, 240, ((15, 32),), (32,), 3)),
            "E8": (e8_scaled_roots(), 56, (56, 756, ((27, 56),), (56,), 3)),
        }
        for _, (roots, degree, local_signature) in expected.items():
            adjacency = primitive_direction_graph(roots)
            self.assertEqual({len(adjacency[root]) for root in roots}, {degree})
            self.assertEqual(
                {neighborhood_signature(adjacency, root) for root in roots},
                {local_signature},
            )

    def test_pair_context_histogram_detects_second_horizon_splits(self):
        self.assertEqual(
            pair_context_histogram(primitive_direction_graph(d_roots(5))),
            {(1, 5): 240, (2, 1): 240, (2, 4): 240, (2, 6): 40, (3, 0): 20},
        )
        self.assertEqual(
            pair_context_histogram(primitive_direction_graph(e6_scaled_roots())),
            {(1, 9): 720, (2, 1): 720, (2, 6): 1080, (3, 0): 36},
        )

    def test_bounded_flag_enumeration_keeps_e8_ci_cost_controlled(self):
        adjacency = primitive_direction_graph(e8_scaled_roots())
        histograms = flag_extension_histograms(adjacency, maximum_size=2)
        self.assertEqual(histograms, ({56: 240}, {27: 6720}))


if __name__ == "__main__":
    unittest.main()
