import unittest
from fractions import Fraction

from enterprise_math.operation_freedom_envelope_valleys import (
    block_count_from_giant_size,
    giant_size_from_block_count,
    ideal_partial_giant_size,
    ideal_partial_upper_envelope_probability,
    ideal_total_giant_size,
    ideal_total_upper_envelope_probability,
    maximum_partial_safe_probability_by_giant_size,
    maximum_total_safe_probability_by_giant_size,
    operation_freedom_envelope_valley,
    partial_upper_envelope_candidate_giant_sizes,
    partial_upper_envelope_correction,
    total_upper_envelope_candidate_giant_sizes,
    total_upper_envelope_correction,
    true_partial_upper_envelope_giant_size,
    true_total_upper_envelope_giant_size,
)
from enterprise_math.operation_freedom_majorization import (
    maximum_safe_partial_count_fixed_blocks,
    maximum_safe_total_count_fixed_blocks,
)


class OperationFreedomEnvelopeValleysTests(unittest.TestCase):
    def test_giant_size_and_block_count_are_inverse(self):
        for state_count in range(3, 50):
            for giant_size in range(2, state_count):
                block_count = block_count_from_giant_size(
                    state_count, giant_size
                )
                self.assertEqual(
                    giant_size_from_block_count(
                        state_count, block_count
                    ),
                    giant_size,
                )

    def test_probability_formulas_match_fixed_block_maximum_counts(self):
        for state_count in range(3, 50):
            for giant_size in range(2, state_count):
                block_count = state_count - giant_size + 1
                self.assertEqual(
                    maximum_total_safe_probability_by_giant_size(
                        state_count, giant_size
                    ),
                    Fraction(
                        maximum_safe_total_count_fixed_blocks(
                            state_count, block_count
                        ),
                        state_count**state_count,
                    ),
                )
                self.assertEqual(
                    maximum_partial_safe_probability_by_giant_size(
                        state_count, giant_size
                    ),
                    Fraction(
                        maximum_safe_partial_count_fixed_blocks(
                            state_count, block_count
                        ),
                        (state_count + 1) ** state_count,
                    ),
                )

    def test_exact_multiplicative_corrections_have_closed_form(self):
        for state_count in range(3, 40):
            for giant_size in range(2, state_count):
                self.assertEqual(
                    total_upper_envelope_correction(
                        state_count, giant_size
                    ),
                    Fraction(
                        giant_size**giant_size
                        + state_count
                        - giant_size,
                        giant_size**giant_size,
                    ),
                )
                self.assertEqual(
                    partial_upper_envelope_correction(
                        state_count, giant_size
                    ),
                    Fraction(
                        giant_size**giant_size
                        + state_count
                        - giant_size
                        + 1,
                        giant_size**giant_size,
                    ),
                )

    def test_true_upper_envelope_minima_match_direct_probability_search(self):
        for state_count in range(3, 90):
            total_size = true_total_upper_envelope_giant_size(
                state_count
            )
            partial_size = true_partial_upper_envelope_giant_size(
                state_count
            )
            self.assertEqual(
                maximum_total_safe_probability_by_giant_size(
                    state_count, total_size
                ),
                min(
                    maximum_total_safe_probability_by_giant_size(
                        state_count, giant_size
                    )
                    for giant_size in range(2, state_count)
                ),
            )
            self.assertEqual(
                maximum_partial_safe_probability_by_giant_size(
                    state_count, partial_size
                ),
                min(
                    maximum_partial_safe_probability_by_giant_size(
                        state_count, giant_size
                    )
                    for giant_size in range(2, state_count)
                ),
            )

    def test_exact_ideal_candidate_windows_contain_true_minima(self):
        for state_count in range(3, 150):
            self.assertIn(
                true_total_upper_envelope_giant_size(state_count),
                total_upper_envelope_candidate_giant_sizes(
                    state_count
                ),
            )
            self.assertIn(
                true_partial_upper_envelope_giant_size(state_count),
                partial_upper_envelope_candidate_giant_sizes(
                    state_count
                ),
            )

    def test_true_and_ideal_giant_sizes_stay_close_on_broad_finite_range(self):
        # Regression evidence only.  The analytic PR argument supplies the
        # asymptotic O(1) localization without inserting floating-point e here.
        for state_count in range(6, 200):
            self.assertLessEqual(
                abs(
                    true_total_upper_envelope_giant_size(state_count)
                    - ideal_total_giant_size(state_count)
                ),
                1,
            )
            self.assertLessEqual(
                abs(
                    true_partial_upper_envelope_giant_size(state_count)
                    - ideal_partial_giant_size(state_count)
                ),
                1,
            )

    def test_report_shapes_are_maximally_imbalanced(self):
        for state_count in range(3, 80):
            report = operation_freedom_envelope_valley(state_count)
            self.assertEqual(
                report.total_shape,
                (report.total_giant_size,)
                + (1,) * (report.total_block_count - 1),
            )
            self.assertEqual(
                report.partial_shape,
                (report.partial_giant_size,)
                + (1,) * (report.partial_block_count - 1),
            )
            self.assertEqual(sum(report.total_shape), state_count)
            self.assertEqual(sum(report.partial_shape), state_count)

    def test_ideal_surrogates_have_local_integer_minima(self):
        for state_count in range(6, 100):
            total_size = ideal_total_giant_size(state_count)
            partial_size = ideal_partial_giant_size(state_count)
            total_value = ideal_total_upper_envelope_probability(
                state_count, total_size
            )
            partial_value = ideal_partial_upper_envelope_probability(
                state_count, partial_size
            )
            for neighbor in (total_size - 1, total_size + 1):
                if 2 <= neighbor < state_count:
                    self.assertLessEqual(
                        total_value,
                        ideal_total_upper_envelope_probability(
                            state_count, neighbor
                        ),
                    )
            for neighbor in (partial_size - 1, partial_size + 1):
                if 2 <= neighbor < state_count:
                    self.assertLessEqual(
                        partial_value,
                        ideal_partial_upper_envelope_probability(
                            state_count, neighbor
                        ),
                    )

    def test_validation(self):
        with self.assertRaises(ValueError):
            block_count_from_giant_size(2, 1)
        with self.assertRaises(ValueError):
            giant_size_from_block_count(5, 5)
        with self.assertRaises(TypeError):
            ideal_total_giant_size(True)
        with self.assertRaises(ValueError):
            true_partial_upper_envelope_giant_size(2)


if __name__ == "__main__":
    unittest.main()
