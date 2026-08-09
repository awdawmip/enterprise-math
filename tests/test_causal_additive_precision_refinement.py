import unittest

from enterprise_math.causal_additive_precision_refinement import (
    continuation_type,
    continuation_type_count,
    distinguishing_future_sum,
    future_quotient_after_sum,
    minimal_future_state,
    minimal_refinement_scale,
    minimal_state_matches_refined_quotient,
    refined_quotient,
    types_are_future_distinguishable,
)


def _is_generated_sum(total: int, generators: tuple[int, ...]) -> bool:
    if total < 0:
        return False
    positive = tuple(value for value in generators if value > 0)
    reachable = [False] * (total + 1)
    reachable[0] = True
    for amount in range(total + 1):
        if not reachable[amount]:
            continue
        for generator in positive:
            if amount + generator <= total:
                reachable[amount + generator] = True
    return reachable[total]


class CausalAdditivePrecisionRefinementTests(unittest.TestCase):
    def test_scale_six_plus_two_needs_three_not_six_continuation_types(self):
        d = 6
        generators = (2,)
        self.assertEqual(minimal_refinement_scale(d, generators), 2)
        self.assertEqual(continuation_type_count(d, generators), 3)
        self.assertEqual(
            tuple(continuation_type(units, d, generators) for units in range(6)),
            (0, 0, 1, 1, 2, 2),
        )

    def test_minimal_state_is_exactly_finer_gcd_block_quotient(self):
        cases = (
            (6, (2,)),
            (6, (4, 6)),
            (12, (6, 18)),
            (10, (4, 6)),
            (8, (1,)),
        )
        for d, generators in cases:
            g = minimal_refinement_scale(d, generators)
            for units in range(80):
                self.assertTrue(minimal_state_matches_refined_quotient(units, d, generators))
                self.assertEqual(refined_quotient(units, d, generators), units // g)

    def test_no_detail_when_future_is_already_whole_block_aligned(self):
        d = 6
        generators = (6, 12, 18)
        self.assertEqual(minimal_refinement_scale(d, generators), 6)
        self.assertEqual(continuation_type_count(d, generators), 1)
        for units in range(30):
            self.assertEqual(minimal_future_state(units, d, generators)[1], 0)

    def test_full_remainder_only_when_gcd_refines_to_unit_scale(self):
        d = 6
        generators = (1,)
        self.assertEqual(minimal_refinement_scale(d, generators), 1)
        self.assertEqual(continuation_type_count(d, generators), 6)
        self.assertEqual(
            tuple(continuation_type(units, d, generators) for units in range(6)),
            tuple(range(6)),
        )

    def test_distinct_continuation_types_have_constructive_future_witnesses(self):
        cases = (
            (6, (2,)),
            (6, (4, 6)),
            (10, (4, 6)),
            (12, (8, 18)),
        )
        for d, generators in cases:
            count = continuation_type_count(d, generators)
            for left in range(count):
                for right in range(left + 1, count):
                    future_sum = distinguishing_future_sum(left, right, d, generators)
                    self.assertIsNotNone(future_sum)
                    self.assertTrue(_is_generated_sum(future_sum, generators))
                    self.assertTrue(types_are_future_distinguishable(left, right, d, generators))
                    self.assertNotEqual(
                        future_quotient_after_sum(left, future_sum, d, generators),
                        future_quotient_after_sum(right, future_sum, d, generators),
                    )

    def test_generator_larger_than_modulus_never_fabricates_residue_only_witness(self):
        d = 12
        generators = (8, 18)
        # g=2 and D=6.  The normalized generator 4 must remain the actual value
        # 4 in normalized units; it must not be replaced by a smaller residue-only
        # move when constructing a future witness.
        count = continuation_type_count(d, generators)
        for left in range(count):
            for right in range(left + 1, count):
                future_sum = distinguishing_future_sum(left, right, d, generators)
                self.assertTrue(_is_generated_sum(future_sum, generators))

    def test_equal_types_remain_future_equivalent_under_generated_sums(self):
        d = 6
        generators = (2, 4)
        pairs = ((0, 1), (2, 3), (4, 5))
        future_sums = tuple(2 * a + 4 * b for a in range(6) for b in range(6))
        for left, right in pairs:
            self.assertEqual(continuation_type(left, d, generators), continuation_type(right, d, generators))
            for future_sum in future_sums:
                self.assertEqual((left + future_sum) // d, (right + future_sum) // d)

    def test_zero_only_language_keeps_original_quotient(self):
        d = 7
        generators = (0, 0)
        self.assertEqual(minimal_refinement_scale(d, generators), 7)
        self.assertEqual(continuation_type_count(d, generators), 1)
        for units in range(30):
            self.assertEqual(refined_quotient(units, d, generators), units // 7)


if __name__ == "__main__":
    unittest.main()
