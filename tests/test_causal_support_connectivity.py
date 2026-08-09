import unittest

from enterprise_math.causal_code_lattice import construction_a_primitive_events
from enterprise_math.causal_code_relaxation import (
    e8_nested_subcodes,
    primitive_graph_component_sizes,
)
from enterprise_math.causal_support_connectivity import (
    every_slot_is_glued,
    minimum_weight_supports,
    support_hypergraph_components,
    support_hypergraph_connected,
)


class CausalSupportConnectivityTests(unittest.TestCase):
    def test_c2_support_hypergraph_has_two_four_cell_components_matching_root_graph(self):
        c2, _, _, _ = e8_nested_subcodes()
        supports = minimum_weight_supports(c2)
        self.assertTrue(every_slot_is_glued(8, supports))
        self.assertEqual(
            tuple(sorted(map(len, support_hypergraph_components(8, supports)), reverse=True)),
            (4, 4),
        )
        self.assertFalse(support_hypergraph_connected(8, supports))
        self.assertEqual(primitive_graph_component_sizes(c2), (24, 24))

    def test_c3_and_full_hamming_support_hypergraphs_are_connected(self):
        _, c3, c4, _ = e8_nested_subcodes()
        for code in (c3, c4):
            supports = minimum_weight_supports(code)
            self.assertTrue(every_slot_is_glued(8, supports))
            self.assertTrue(support_hypergraph_connected(8, supports))
            self.assertEqual(
                primitive_graph_component_sizes(code),
                (len(construction_a_primitive_events(code)),),
            )


if __name__ == "__main__":
    unittest.main()
