import unittest

from enterprise_math.causal_primitive_link_profile import (
    a_roots,
    d_roots,
    e6_scaled_roots,
    primitive_direction_graph,
)
from enterprise_math.causal_root_lattice_reconstruction import (
    causal_translation_module_summary,
    primitive_difference_target,
)


class CausalRootLatticeReconstructionTests(unittest.TestCase):
    def test_fcc_local_direction_graph_generates_rank_three_translation_module(self):
        adjacency = primitive_direction_graph(a_roots(3))
        summary = causal_translation_module_summary(adjacency)
        self.assertEqual(summary.primitive_generator_count, 12)
        self.assertEqual(summary.translation_rank, 3)
        self.assertEqual(summary.invisible_relation_rank, 9)
        self.assertTrue(summary.antipode_relations_verified)
        self.assertTrue(summary.primitive_difference_relations_verified)

    def test_a_d_e_global_translation_rank_is_recovered_from_local_relation_graph(self):
        cases = (
            (a_roots(2), 2),
            (a_roots(5), 5),
            (d_roots(4), 4),
            (d_roots(6), 6),
            (e6_scaled_roots(), 6),
        )
        for roots, expected_rank in cases:
            summary = causal_translation_module_summary(primitive_direction_graph(roots))
            self.assertEqual(summary.translation_rank, expected_rank)
            self.assertTrue(summary.antipode_relations_verified)
            self.assertTrue(summary.primitive_difference_relations_verified)

    def test_fcc_adjacent_direction_difference_is_another_primitive_direction_without_coordinates_in_rule(self):
        roots = a_roots(3)
        adjacency = primitive_direction_graph(roots)
        left = (1, -1, 0, 0)
        right = (1, 0, -1, 0)
        target = primitive_difference_target(adjacency, left, right)
        # Coordinate equality below is only an audit of the causal column relation.
        self.assertEqual(target, (0, 1, -1, 0))


if __name__ == "__main__":
    unittest.main()
