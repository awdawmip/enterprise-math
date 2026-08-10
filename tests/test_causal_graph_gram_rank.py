import unittest

from enterprise_math.causal_graph_gram_rank import (
    causal_graph_dimension,
    causal_simply_laced_gram,
    graph_antipodes,
)
from enterprise_math.causal_primitive_link_profile import (
    a_roots,
    d_roots,
    e6_scaled_roots,
    primitive_direction_graph,
)
from enterprise_math.causal_root_inner_product_shadow import actual_scaled_inner_product_class


class CausalGraphGramRankTests(unittest.TestCase):
    def test_fcc_unlabeled_primitive_graph_recovers_dimension_three(self):
        roots = a_roots(3)
        adjacency = primitive_direction_graph(roots)
        self.assertEqual(causal_graph_dimension(adjacency), 3)
        antipodes = graph_antipodes(adjacency)
        self.assertTrue(all(antipodes[antipodes[root]] == root for root in roots))

    def test_a_d_e_relation_graph_rank_recovers_root_rank(self):
        cases = (
            (a_roots(2), 2),
            (a_roots(5), 5),
            (d_roots(4), 4),
            (d_roots(6), 6),
            (e6_scaled_roots(), 6),
        )
        for roots, expected_rank in cases:
            self.assertEqual(
                causal_graph_dimension(primitive_direction_graph(roots)),
                expected_rank,
            )

    def test_graph_reconstructed_gram_matches_coordinate_audit_without_using_coordinates_in_reconstruction(self):
        roots = a_roots(4)
        adjacency = primitive_direction_graph(roots)
        reconstructed = causal_simply_laced_gram(adjacency)
        vertices = tuple(adjacency)
        audited = tuple(
            tuple(actual_scaled_inner_product_class(left, right) for right in vertices)
            for left in vertices
        )
        self.assertEqual(reconstructed, audited)


if __name__ == "__main__":
    unittest.main()
