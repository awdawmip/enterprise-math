import unittest
from itertools import product

from enterprise_math.material_phase_quotient import (
    cyclic_material_phase_quotient,
    cyclic_word_primitive_period,
)


class MaterialPhaseQuotientTests(unittest.TestCase):
    def test_constant_word_collapses_any_clock_to_one_future_state(self):
        for n in range(1, 20):
            report = cyclic_material_phase_quotient((7,) * n)
            self.assertEqual(report.primitive_output_period, 1)
            self.assertEqual(report.stable_future_class_count, 1)
            self.assertEqual(report.stable_partition, (0,) * n)

    def test_primitive_word_retains_every_clock_phase(self):
        for n in range(1, 18):
            word = tuple(range(n))
            report = cyclic_material_phase_quotient(word)
            self.assertEqual(report.primitive_output_period, n)
            self.assertEqual(report.stable_future_class_count, n)

    def test_repeated_short_word_keeps_only_short_period(self):
        base = (0, 3, 1)
        word = base * 5
        report = cyclic_material_phase_quotient(word)
        self.assertEqual(report.clock_phase_count, 15)
        self.assertEqual(report.primitive_output_period, 3)
        self.assertEqual(report.stable_future_class_count, 3)
        self.assertEqual(report.stable_partition, tuple(i % 3 for i in range(15)))

    def test_closed_form_matches_bruteforce_shift_equivalence_on_small_words(self):
        for n in range(1, 9):
            for word in product(range(2), repeat=n):
                period = cyclic_word_primitive_period(word)
                signatures = {
                    i: tuple(word[(i + k) % n] for k in range(n))
                    for i in range(n)
                }
                brute_count = len(set(signatures.values()))
                self.assertEqual(period, brute_count)
                self.assertEqual(
                    cyclic_material_phase_quotient(word).stable_future_class_count,
                    brute_count,
                )

    def test_same_current_sample_can_still_require_distinct_future_phase(self):
        word = (0, 1, 0, 2)
        report = cyclic_material_phase_quotient(word)
        self.assertEqual(word[0], word[2])
        self.assertEqual(report.primitive_output_period, 4)
        self.assertNotEqual(report.stable_partition[0], report.stable_partition[2])

    def test_clock_capacity_and_future_relevant_phase_are_distinct_resources(self):
        report = cyclic_material_phase_quotient((1, 2) * 8)
        self.assertEqual(report.clock_phase_count, 16)
        self.assertEqual(report.stable_future_class_count, 2)
        self.assertEqual(
            (report.compression_factor_numerator, report.compression_factor_denominator),
            (16, 2),
        )

    def test_invalid_words_are_rejected(self):
        with self.assertRaises(ValueError):
            cyclic_material_phase_quotient(())
        with self.assertRaises(ValueError):
            cyclic_material_phase_quotient((0, True, 1))


if __name__ == "__main__":
    unittest.main()
