import unittest

from enterprise_math.causal_conservation_geometry import (
    causal_geometry_shadow_identity,
    exact_total_conserving_minimum_events,
    parity_conserving_minimum_events,
    primitive_event_counts,
    support_size,
    unconstrained_minimum_events,
)


class CausalConservationGeometryTests(unittest.TestCase):
    def test_no_conservation_generates_axis_events(self):
        for slots in range(1, 8):
            events = unconstrained_minimum_events(slots)
            self.assertEqual({support_size(event) for event in events}, {1})
            self.assertEqual(len(events), 2 * slots)
            self.assertTrue(causal_geometry_shadow_identity(slots)["Z"])

    def test_exact_total_conservation_generates_a_transfer_events(self):
        for slots in range(2, 8):
            events = exact_total_conserving_minimum_events(slots)
            self.assertEqual({support_size(event) for event in events}, {2})
            self.assertEqual(len(events), slots * (slots - 1))
            self.assertTrue(causal_geometry_shadow_identity(slots)["A"])

    def test_parity_only_conservation_generates_d_pair_events(self):
        for slots in range(2, 8):
            events = parity_conserving_minimum_events(slots)
            self.assertEqual({support_size(event) for event in events}, {2})
            self.assertEqual(len(events), 2 * slots * (slots - 1))
            self.assertTrue(causal_geometry_shadow_identity(slots)["D"])

    def test_parity_grammar_contains_transfer_and_pair_creation_annihilation(self):
        events = set(parity_conserving_minimum_events(4))
        self.assertIn((1, -1, 0, 0), events)
        self.assertIn((1, 1, 0, 0), events)
        self.assertIn((-1, -1, 0, 0), events)
        self.assertNotIn((1, 0, 0, 0), events)

    def test_primitive_event_count_hierarchy(self):
        self.assertEqual(primitive_event_counts(3), {"Z": 6, "A": 6, "D": 12})
        self.assertEqual(primitive_event_counts(4), {"Z": 8, "A": 12, "D": 24})
        self.assertEqual(primitive_event_counts(8), {"Z": 16, "A": 56, "D": 112})


if __name__ == "__main__":
    unittest.main()
