import unittest

from enterprise_math.integer_future_observability import (
    finite_horizon_observability_matrix,
)
from enterprise_math.integer_future_smith_precision import (
    determinantal_divisor,
    determinantal_divisors,
    integer_smith_precision_profile,
    row_extension_determinantal_refinement,
    smith_invariant_factors_from_minors,
)


class IntegerFutureSmithPrecisionTests(unittest.TestCase):
    def test_diagonal_reference_smith_profile(self):
        matrix = ((2, 0), (0, 6))
        self.assertEqual(determinantal_divisors(matrix), (2, 12))
        self.assertEqual(smith_invariant_factors_from_minors(matrix), (2, 6))
        profile = integer_smith_precision_profile(matrix)
        self.assertEqual(profile.rational_rank, 2)
        self.assertEqual(profile.hidden_free_rank, 0)
        self.assertEqual(profile.maximal_nonzero_determinantal_divisor, 12)
        self.assertFalse(profile.integer_unimodular)

    def test_crossing_pair_partitions_have_free_hidden_direction_but_no_smith_torsion(self):
        matrix = (
            (1, 1, 0, 0),
            (0, 0, 1, 1),
            (1, 0, 1, 0),
            (0, 1, 0, 1),
        )
        profile = integer_smith_precision_profile(matrix)
        self.assertEqual(profile.rational_rank, 3)
        self.assertEqual(profile.hidden_free_rank, 1)
        self.assertEqual(profile.smith_invariant_factors, (1, 1, 1))
        self.assertEqual(profile.determinantal_divisors, (1, 1, 1, 0))

    def test_three_pair_partitions_have_exact_one_index_two_factor(self):
        matrix = (
            (1, 1, 0, 0),
            (0, 0, 1, 1),
            (1, 0, 1, 0),
            (0, 1, 0, 1),
            (1, 0, 0, 1),
            (0, 1, 1, 0),
        )
        profile = integer_smith_precision_profile(matrix)
        self.assertEqual(profile.rational_rank, 4)
        self.assertEqual(profile.hidden_free_rank, 0)
        self.assertEqual(profile.determinantal_divisors, (1, 1, 1, 2))
        self.assertEqual(profile.smith_invariant_factors, (1, 1, 1, 2))
        self.assertFalse(profile.integer_unimodular)

    def test_singleton_future_row_removes_final_index_two_factor_without_rank_change(self):
        base = (
            (1, 1, 0, 0),
            (0, 0, 1, 1),
            (1, 0, 1, 0),
            (0, 1, 0, 1),
            (1, 0, 0, 1),
            (0, 1, 1, 0),
        )
        refined = (*base, (1, 0, 0, 0))
        before = integer_smith_precision_profile(base)
        after = integer_smith_precision_profile(refined)
        self.assertEqual(before.rational_rank, after.rational_rank)
        self.assertEqual(before.hidden_free_rank, after.hidden_free_rank)
        self.assertEqual(before.smith_invariant_factors, (1, 1, 1, 2))
        self.assertEqual(after.smith_invariant_factors, (1, 1, 1, 1))
        self.assertTrue(after.integer_unimodular)
        self.assertEqual(
            row_extension_determinantal_refinement(base, refined),
            (True, True, True, True),
        )

    def test_full_rank_future_rows_can_refine_multiple_determinantal_orders(self):
        base = (
            (2, 0),
            (0, 2),
        )
        middle = (*base, (1, 1))
        final = (*middle, (1, 0))
        self.assertEqual(determinantal_divisors(base), (2, 4))
        self.assertEqual(determinantal_divisors(middle), (1, 2))
        self.assertEqual(determinantal_divisors(final), (1, 1))
        self.assertEqual(smith_invariant_factors_from_minors(base), (2, 2))
        self.assertEqual(smith_invariant_factors_from_minors(middle), (1, 2))
        self.assertEqual(smith_invariant_factors_from_minors(final), (1, 1))
        self.assertEqual(
            row_extension_determinantal_refinement(base, middle),
            (True, True),
        )
        self.assertEqual(
            row_extension_determinantal_refinement(middle, final),
            (True, True),
        )

    def test_ttl_age_observability_has_all_unit_smith_factors_at_every_visible_rank(self):
        for depth in range(1, 7):
            transition = tuple(
                tuple(
                    1 if row == column + 1 else 0
                    for column in range(depth)
                )
                for row in range(depth)
            )
            observation = (tuple(1 for _ in range(depth)),)
            for horizon in range(depth):
                matrix = finite_horizon_observability_matrix(
                    transition,
                    observation,
                    horizon,
                )
                profile = integer_smith_precision_profile(matrix)
                self.assertEqual(profile.rational_rank, horizon + 1)
                self.assertEqual(
                    profile.smith_invariant_factors,
                    (1,) * (horizon + 1),
                )
                self.assertEqual(
                    profile.determinantal_divisors[: horizon + 1],
                    (1,) * (horizon + 1),
                )
            final = integer_smith_precision_profile(
                finite_horizon_observability_matrix(
                    transition,
                    observation,
                    depth - 1,
                )
            )
            self.assertTrue(final.integer_unimodular)

    def test_rank_growth_appears_as_previous_zero_divisor_becoming_nonzero(self):
        early = ((1, 1, 1),)
        later = (*early, (1, 1, 0))
        final = (*later, (1, 0, 0))
        self.assertEqual(determinantal_divisors(early), (1, 0, 0))
        self.assertEqual(determinantal_divisors(later), (1, 1, 0))
        self.assertEqual(determinantal_divisors(final), (1, 1, 1))
        self.assertEqual(integer_smith_precision_profile(early).hidden_free_rank, 2)
        self.assertEqual(integer_smith_precision_profile(later).hidden_free_rank, 1)
        self.assertEqual(integer_smith_precision_profile(final).hidden_free_rank, 0)

    def test_validation(self):
        with self.assertRaises(ValueError):
            determinantal_divisor((), 1)
        with self.assertRaises(ValueError):
            determinantal_divisor(((1, 2),), -1)
        with self.assertRaises(TypeError):
            determinantal_divisor(((1, 2),), False)
        with self.assertRaises(ValueError):
            row_extension_determinantal_refinement(
                ((1, 0),),
                ((0, 1), (1, 0)),
            )


if __name__ == "__main__":
    unittest.main()
