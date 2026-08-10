import unittest

from enterprise_math.causal_direction_quotient_geometry import (
    quotient_graph_connected,
    quotient_primitive_classes,
    quotient_primitive_graph,
)
from enterprise_math.causal_primitive_link_profile import a_roots, primitive_direction_graph


class CausalDirectionQuotientGeometryTests(unittest.TestCase):
    def test_fcc_direction_quotient_is_a2_six_cycle_without_using_a3_coordinates_in_quotient(self):
        roots = a_roots(3)
        adjacency = primitive_direction_graph(roots)
        chosen = roots[0]
        classes, _ = quotient_primitive_classes(adjacency, chosen)
        quotient = quotient_primitive_graph(adjacency, chosen)
        self.assertEqual(len(classes), 6)
        self.assertEqual(len(quotient), 6)
        self.assertTrue(quotient_graph_connected(quotient))
        self.assertEqual({len(neighbors) for neighbors in quotient.values()}, {2})
        self.assertEqual(sum(len(neighbors) for neighbors in quotient.values()) // 2, 6)

    def test_general_a_p_quotient_has_a_p_minus_one_primitive_counts_and_degrees(self):
        for p in range(2, 6):
            roots = a_roots(p)
            adjacency = primitive_direction_graph(roots)
            quotient = quotient_primitive_graph(adjacency, roots[0])
            expected_count = p * (p - 1)
            expected_degree = 2 * (p - 2) if p >= 2 else 0
            self.assertEqual(len(quotient), expected_count)
            self.assertEqual({len(neighbors) for neighbors in quotient.values()}, {expected_degree})
            self.assertTrue(quotient_graph_connected(quotient) or p == 2)


if __name__ == "__main__":
    unittest.main()
