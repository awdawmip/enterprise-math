import unittest

from enterprise_math.causal_code_lattice import (
    construction_a_primitive_events,
    construction_a_primitive_grade,
    even_parity_code,
    extended_hamming_8_code,
    minimum_hamming_weight,
    primitive_event_grade_is_uniform,
    weight_histogram,
)


class CausalCodeLatticeTests(unittest.TestCase):
    def test_single_parity_check_code_has_d_n_pair_primitive_events(self):
        for length in range(3, 8):
            code = even_parity_code(length)
            self.assertEqual(minimum_hamming_weight(code), 2)
            self.assertEqual(construction_a_primitive_grade(code), 2)
            events = construction_a_primitive_events(code)
            self.assertEqual(len(events), 2 * length * (length - 1))
            self.assertTrue(primitive_event_grade_is_uniform(code))
            self.assertTrue(all(sum(value != 0 for value in event) == 2 for event in events))

    def test_extended_hamming_code_has_1_14_1_weight_spectrum(self):
        code = extended_hamming_8_code()
        self.assertEqual(len(code), 16)
        self.assertEqual(weight_histogram(code), {0: 1, 4: 14, 8: 1})
        self.assertEqual(minimum_hamming_weight(code), 4)

    def test_extended_hamming_grade_tie_generates_240_e8_primitive_events(self):
        code = extended_hamming_8_code()
        self.assertEqual(construction_a_primitive_grade(code), 4)
        events = construction_a_primitive_events(code)
        self.assertEqual(len(events), 240)
        self.assertTrue(primitive_event_grade_is_uniform(code))
        support_histogram = {}
        for event in events:
            support = sum(value != 0 for value in event)
            support_histogram[support] = support_histogram.get(support, 0) + 1
        self.assertEqual(support_histogram, {1: 16, 4: 224})

    def test_e8_count_decomposes_as_axis_plus_weight_four_code_lifts(self):
        code = extended_hamming_8_code()
        weight_four = [word for word in code if sum(word) == 4]
        self.assertEqual(len(weight_four), 14)
        self.assertEqual(16 + 14 * 16, 240)
        self.assertEqual(len(construction_a_primitive_events(code)), 240)


if __name__ == "__main__":
    unittest.main()
