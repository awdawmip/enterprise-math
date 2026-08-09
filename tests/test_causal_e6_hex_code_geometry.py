import unittest

from enterprise_math.causal_e6_hex_code_geometry import (
    e6_all_edge_contexts_uniform,
    e6_edge_context,
    e6_event_grade,
    e6_link_degree_set,
    e6_primitive_events,
    local_hex_profile,
    local_minimum_representatives,
)


class CausalE6HexCodeGeometryTests(unittest.TestCase):
    def test_local_hex_integer_alphabet_has_exact_three_to_one_grade_ratio(self):
        self.assertEqual(local_hex_profile(), {0: (3, 6), 1: (1, 3), 2: (1, 3)})
        self.assertEqual(
            set(local_minimum_representatives(0)),
            {(2, -1), (-2, 1), (-1, 2), (1, -2), (1, 1), (-1, -1)},
        )

    def test_ternary_repetition_generates_72_uniform_grade_three_events(self):
        events = e6_primitive_events()
        self.assertEqual(len(events), 72)
        self.assertEqual({e6_event_grade(event) for event in events}, {3})

    def test_e6_first_direction_link_is_uniform_degree_twenty(self):
        self.assertEqual(e6_link_degree_set(), (20,))

    def test_e6_fixed_primitive_edge_has_uniform_twenty_vertex_degree_nine_context(self):
        events = e6_primitive_events()
        self.assertEqual(
            e6_edge_context(events[0]),
            (20, 90, (20,), ((9, 20),)),
        )
        self.assertTrue(e6_all_edge_contexts_uniform())


if __name__ == "__main__":
    unittest.main()
