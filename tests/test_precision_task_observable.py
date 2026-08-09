import itertools
import unittest

from enterprise_math.precision_task_observable import (
    all_crossed_signature,
    any_crossed_signature,
    any_or_all_class_count,
    crossing_bucket,
    full_vector_class_count,
    linear_two_coordinate_class_count,
    linear_two_coordinate_signature,
    symmetric_sum_class_count,
    symmetric_sum_signature,
    two_coordinate_equality_class_count,
    two_coordinate_equality_signature,
)


class CrossingBucketTests(unittest.TestCase):
    def test_crossing_bucket_matches_direct_unit_translation(self) -> None:
        for width in range(1, 16, 2):
            for horizon in range(width):
                for detail in range(width):
                    bucket = crossing_bucket(detail, width, horizon)
                    direct = horizon + 1
                    for sample in range(1, horizon + 1):
                        if (detail + sample) // width > 0:
                            direct = sample
                            break
                    self.assertEqual(bucket, direct)

    def test_full_vector_count_is_ordered_bucket_product(self) -> None:
        for dimension in range(1, 6):
            for horizon in range(7):
                self.assertEqual(
                    full_vector_class_count(dimension, horizon),
                    (horizon + 1) ** dimension,
                )


class LinearObservableTests(unittest.TestCase):
    def test_complete_two_coefficient_classification(self) -> None:
        for width in range(1, 14, 2):
            for horizon in range(width):
                for alpha in range(-3, 4):
                    for beta in range(-3, 4):
                        signatures = {
                            linear_two_coordinate_signature(
                                left,
                                right,
                                width,
                                horizon,
                                alpha,
                                beta,
                            )
                            for left in range(width)
                            for right in range(width)
                        }
                        self.assertEqual(
                            len(signatures),
                            linear_two_coordinate_class_count(alpha, beta, horizon),
                        )

    def test_generic_linear_scalar_can_retain_full_ordered_pair_burden(self) -> None:
        horizon = 4
        self.assertEqual(linear_two_coordinate_class_count(1, 2, horizon), 25)
        self.assertEqual(full_vector_class_count(2, horizon), 25)

    def test_symmetric_and_antisymmetric_specializations(self) -> None:
        horizon = 4
        buckets = horizon + 1
        self.assertEqual(
            linear_two_coordinate_class_count(1, 1, horizon),
            buckets * (buckets + 1) // 2,
        )
        self.assertEqual(
            linear_two_coordinate_class_count(1, -1, horizon),
            buckets * (buckets - 1) + 1,
        )
        self.assertEqual(linear_two_coordinate_class_count(0, 1, horizon), buckets)
        self.assertEqual(linear_two_coordinate_class_count(0, 0, horizon), 1)


class SymmetricSumTests(unittest.TestCase):
    def test_sum_signature_count_matches_multiset_formula(self) -> None:
        for width in (1, 3, 5, 7):
            for horizon in range(width):
                for dimension in range(1, 5):
                    signatures = {
                        symmetric_sum_signature(details, width, horizon)
                        for details in itertools.product(range(width), repeat=dimension)
                    }
                    self.assertEqual(
                        len(signatures),
                        symmetric_sum_class_count(dimension, horizon),
                    )

    def test_three_dimensional_sum_is_far_coarser_than_full_vector(self) -> None:
        horizon = 4
        self.assertEqual(full_vector_class_count(3, horizon), 125)
        self.assertEqual(symmetric_sum_class_count(3, horizon), 35)


class BooleanObservableTests(unittest.TestCase):
    def test_any_and_all_crossing_need_only_one_bucket(self) -> None:
        for width in (1, 3, 5, 7):
            for horizon in range(width):
                for dimension in range(1, 5):
                    any_signatures = {
                        any_crossed_signature(details, width, horizon)
                        for details in itertools.product(range(width), repeat=dimension)
                    }
                    all_signatures = {
                        all_crossed_signature(details, width, horizon)
                        for details in itertools.product(range(width), repeat=dimension)
                    }
                    expected = any_or_all_class_count(horizon)
                    self.assertEqual(len(any_signatures), expected)
                    self.assertEqual(len(all_signatures), expected)

    def test_boolean_task_collapses_dimension_power_to_linear(self) -> None:
        horizon = 4
        dimension = 5
        self.assertEqual(full_vector_class_count(dimension, horizon), 3125)
        self.assertEqual(any_or_all_class_count(horizon), 5)

    def test_two_coordinate_equality_formula(self) -> None:
        for width in range(1, 14, 2):
            for horizon in range(width):
                signatures = {
                    two_coordinate_equality_signature(left, right, width, horizon)
                    for left in range(width)
                    for right in range(width)
                }
                self.assertEqual(
                    len(signatures),
                    two_coordinate_equality_class_count(horizon),
                )


if __name__ == "__main__":
    unittest.main()
