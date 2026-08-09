import unittest

from enterprise_math.material_star_shape_observables import (
    finite_difference_shape_alias,
    response_shape_fits_zero_baseline_star_shell,
    response_shape_from_histogram,
    response_shape_histogram,
    response_shape_power_signature,
)


class MaterialStarShapeObservableTests(unittest.TestCase):
    def test_histogram_is_exact_identity_free_shape_state(self):
        shapes = (
            (4, 3, 1),
            (5, 3, 3, 3, 1),
            (7, 7, 4, 2, 2, 1),
            (1,),
        )
        for shape in shapes:
            histogram = response_shape_histogram(shape)
            self.assertEqual(response_shape_from_histogram(histogram), shape)

    def test_first_finite_difference_aliases_match_explicit_small_examples(self):
        first = finite_difference_shape_alias(1)
        self.assertEqual(first.left_shape, (4, 3, 1))
        self.assertEqual(first.right_shape, (4, 2, 2))
        self.assertEqual(first.common_total, 8)
        self.assertEqual(first.common_power_sums, (8,))

        second = finite_difference_shape_alias(2)
        self.assertEqual(second.left_shape, (5, 3, 3, 3, 1))
        self.assertEqual(second.right_shape, (5, 4, 2, 2, 2))
        self.assertEqual(second.common_total, 15)
        self.assertEqual(second.common_power_sums, (15, 53))

    def test_alias_construction_matches_all_declared_statistics_through_degree_eight(self):
        for degree in range(1, 9):
            alias = finite_difference_shape_alias(degree)
            self.assertNotEqual(alias.left_shape, alias.right_shape)
            self.assertEqual(len(alias.left_shape), len(alias.right_shape))
            self.assertEqual(max(alias.left_shape), max(alias.right_shape))
            self.assertEqual(sum(alias.left_shape), sum(alias.right_shape))
            self.assertEqual(
                response_shape_power_signature(alias.left_shape, degree),
                response_shape_power_signature(alias.right_shape, degree),
            )
            self.assertEqual(
                alias.common_power_sums,
                tuple(
                    sum(value**power for value in alias.left_shape)
                    for power in range(1, degree + 1)
                ),
            )

    def test_alias_pairs_live_inside_actual_zero_baseline_star_response_shell(self):
        for degree in range(1, 8):
            alias = finite_difference_shape_alias(degree)
            for shape in (alias.left_shape, alias.right_shape):
                self.assertTrue(
                    response_shape_fits_zero_baseline_star_shell(
                        shape,
                        alias.star_leaf_count,
                        alias.star_closing_score,
                    )
                )

    def test_fixed_low_order_moments_do_not_recover_exact_shape(self):
        for degree in range(1, 7):
            alias = finite_difference_shape_alias(degree)
            signature = response_shape_power_signature(alias.left_shape, degree)
            self.assertEqual(
                signature,
                response_shape_power_signature(alias.right_shape, degree),
            )
            self.assertNotEqual(
                response_shape_histogram(alias.left_shape),
                response_shape_histogram(alias.right_shape),
            )

    def test_higher_moment_can_separate_the_constructed_degree_d_alias(self):
        # The finite-difference construction only guarantees equality through d;
        # the next power provides an explicit witness that the exact shape still
        # contains additional information.
        for degree in range(1, 7):
            alias = finite_difference_shape_alias(degree)
            left_next = sum(value ** (degree + 1) for value in alias.left_shape)
            right_next = sum(value ** (degree + 1) for value in alias.right_shape)
            self.assertNotEqual(left_next, right_next)

    def test_task_signature_can_be_validly_coarser_than_shape_histogram(self):
        alias = finite_difference_shape_alias(3)
        self.assertEqual(
            response_shape_power_signature(alias.left_shape, 3),
            response_shape_power_signature(alias.right_shape, 3),
        )
        self.assertNotEqual(
            response_shape_histogram(alias.left_shape),
            response_shape_histogram(alias.right_shape),
        )

    def test_invalid_shapes_and_observables_are_rejected(self):
        with self.assertRaises(ValueError):
            response_shape_histogram(())
        with self.assertRaises(ValueError):
            response_shape_histogram((1, 2))
        with self.assertRaises(ValueError):
            response_shape_histogram((2, 0))
        with self.assertRaises(ValueError):
            response_shape_power_signature((2, 1), -1)
        with self.assertRaises(ValueError):
            finite_difference_shape_alias(0)
        with self.assertRaises(ValueError):
            response_shape_from_histogram(((2, 1), (2, 1)))
        with self.assertRaises(ValueError):
            response_shape_fits_zero_baseline_star_shell((2, 1), 1, 3)


if __name__ == "__main__":
    unittest.main()
