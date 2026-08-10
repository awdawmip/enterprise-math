import unittest

from enterprise_math.causal_global_relation_geometry import (
    causal_ball_growth,
    causal_word_ball_count,
    causal_word_shell_count,
)
from enterprise_math.causal_primitive_link_profile import a_roots, primitive_direction_graph
from enterprise_math.lattice_geometry import a_ball_count, a_coordinator_shell_count


class CausalGlobalRelationGeometryTests(unittest.TestCase):
    def test_fcc_global_ball_growth_is_generated_from_only_the_local_direction_graph(self):
        adjacency = primitive_direction_graph(a_roots(3))
        reconstructed = causal_ball_growth(adjacency, 4)
        expected = tuple(a_ball_count(3, radius) for radius in range(5))
        self.assertEqual(reconstructed, expected)
        self.assertEqual(reconstructed, (1, 13, 55, 147, 309))

    def test_a2_and_a4_global_relation_balls_match_coordinate_reference_counts(self):
        for p, maximum_radius in ((2, 4), (4, 3)):
            adjacency = primitive_direction_graph(a_roots(p))
            for radius in range(maximum_radius + 1):
                self.assertEqual(
                    causal_word_ball_count(adjacency, radius),
                    a_ball_count(p, radius),
                )
                self.assertEqual(
                    causal_word_shell_count(adjacency, radius),
                    a_coordinator_shell_count(p, radius),
                )


if __name__ == "__main__":
    unittest.main()
