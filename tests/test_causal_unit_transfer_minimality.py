import unittest

from enterprise_math.causal_unit_transfer_minimality import (
    causal_relation_dimension,
    minimum_conserved_support,
    minimum_support_conserved_events,
    minimum_support_events_are_exact_a_roots,
    primitive_direction_count,
)


class CausalUnitTransferMinimalityTests(unittest.TestCase):
    def test_nonzero_conserved_unit_event_needs_exactly_two_slots_at_minimum(self):
        for slot_count in range(2, 9):
            self.assertEqual(minimum_conserved_support(slot_count), 2)

    def test_every_minimum_support_event_is_exactly_one_receiver_one_donor(self):
        for slot_count in range(2, 8):
            events = minimum_support_conserved_events(slot_count)
            self.assertEqual(len(events), slot_count * (slot_count - 1))
            for event in events:
                self.assertEqual(event.count(1), 1)
                self.assertEqual(event.count(-1), 1)
                self.assertEqual(event.count(0), slot_count - 2)
            self.assertTrue(minimum_support_events_are_exact_a_roots(slot_count))

    def test_low_dimension_sequence_is_a1_a2_a3_without_changing_unit_value(self):
        expected = {
            2: (1, 2),   # N=2 -> p=1 -> 2 directed transfers
            3: (2, 6),   # N=3 -> p=2 -> triangular A2
            4: (3, 12),  # N=4 -> p=3 -> A3/FCC
        }
        for slots, (dimension, directions) in expected.items():
            self.assertEqual(causal_relation_dimension(slots), dimension)
            self.assertEqual(primitive_direction_count(slots), directions)

    def test_general_dimension_and_direction_counts(self):
        for slots in range(2, 15):
            p = slots - 1
            self.assertEqual(causal_relation_dimension(slots), p)
            self.assertEqual(primitive_direction_count(slots), p * (p + 1))


if __name__ == "__main__":
    unittest.main()
