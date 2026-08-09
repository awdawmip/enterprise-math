import unittest

from enterprise_math.causal_code_relaxation import (
    e8_nested_subcodes,
    e8_relaxation_profiles,
    primitive_graph_component_sizes,
    relaxation_lowers_primitive_grade,
    relaxation_preserves_primitive_shell,
)


class CausalCodeRelaxationTests(unittest.TestCase):
    def test_nested_code_chain_has_grade_four_enrichment_then_grade_two_reset(self):
        c2, c3, c4, even = e8_nested_subcodes()
        self.assertEqual(
            e8_relaxation_profiles(),
            (
                (4, 48, (8,)),
                (4, 112, (24,)),
                (4, 240, (56,)),
                (2, 112, (24,)),
            ),
        )
        self.assertTrue(relaxation_preserves_primitive_shell(c2, c3))
        self.assertTrue(relaxation_preserves_primitive_shell(c3, c4))
        self.assertTrue(relaxation_lowers_primitive_grade(c4, even))
        self.assertFalse(relaxation_preserves_primitive_shell(c4, even))

    def test_smallest_grade_four_subcode_is_two_d4_like_components(self):
        c2, c3, c4, even = e8_nested_subcodes()
        self.assertEqual(primitive_graph_component_sizes(c2), (24, 24))
        self.assertEqual(primitive_graph_component_sizes(c3), (112,))
        self.assertEqual(primitive_graph_component_sizes(c4), (240,))
        self.assertEqual(primitive_graph_component_sizes(even), (112,))

    def test_weaker_conservation_can_reduce_minimum_coordination_after_grade_drop(self):
        _, _, c4, even = e8_nested_subcodes()
        e8_grade, e8_count, _ = e8_relaxation_profiles()[2]
        d8_grade, d8_count, _ = e8_relaxation_profiles()[3]
        self.assertLess(d8_grade, e8_grade)
        self.assertLess(d8_count, e8_count)
        self.assertTrue(relaxation_lowers_primitive_grade(c4, even))


if __name__ == "__main__":
    unittest.main()
