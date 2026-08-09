import unittest
from itertools import combinations

from enterprise_math.coalescence_time import first_coalescence_time
from enterprise_math.merge_time_complex import (
    collision_increment_degree,
    first_merge_count_from_subsets,
    labelled_pair_merge_times,
    merge_times_reconstruct_kernel,
    subset_first_common_time,
    subset_time_from_pair_times,
)


class MergeTimeComplexTests(unittest.TestCase):
    def test_finite_subset_time_is_max_pairwise_time(self) -> None:
        operation = lambda n: n // 2
        states = tuple(range(0, 16))
        for degree in range(1, 6):
            for subset in combinations(states, degree):
                direct = subset_first_common_time(operation, subset, max_steps=10)
                from_pairs = subset_time_from_pair_times(
                    operation, subset, max_steps=10
                )
                self.assertEqual(direct, from_pairs)

    def test_pair_merge_times_reconstruct_every_kernel_level(self) -> None:
        operations = [
            lambda n: n // 2,
            lambda n: max(n - 1, 0),
            lambda n: n if n % 2 == 0 else n - 1,
        ]
        states = tuple(range(0, 24))
        for operation in operations:
            for step in range(0, 8):
                self.assertTrue(
                    merge_times_reconstruct_kernel(
                        operation, states, step, max_steps=30
                    )
                )

    def test_degree_k_increment_is_first_merge_time_distribution(self) -> None:
        operation = lambda n: n // 2
        states = tuple(range(0, 12))
        for degree in range(2, 6):
            for step in range(1, 6):
                self.assertEqual(
                    collision_increment_degree(operation, states, degree, step),
                    first_merge_count_from_subsets(
                        operation, states, degree, step, max_steps=10
                    ),
                )

    def test_higher_subset_time_has_no_information_beyond_pair_times(self) -> None:
        operation = lambda n: n // 2
        subset = (3, 5, 8, 11)
        pair_times = [
            first_coalescence_time(operation, left, right, max_steps=10)
            for left, right in combinations(subset, 2)
        ]
        self.assertTrue(all(value is not None for value in pair_times))
        expected = max(value for value in pair_times if value is not None)
        self.assertEqual(
            subset_first_common_time(operation, subset, max_steps=10), expected
        )

    def test_same_graph_distance_can_have_different_merge_time(self) -> None:
        # Generic endomap test only: repeated quotient is not interpreted here as
        # repeated application of one typed P005 scale arrow.
        operation = lambda n: n // 2
        self.assertEqual(abs(8 - 9), abs(7 - 8))
        self.assertEqual(first_coalescence_time(operation, 8, 9), 1)
        self.assertEqual(first_coalescence_time(operation, 7, 8), 4)

    def test_graph_distance_and_merge_time_are_not_monotone(self) -> None:
        operation = lambda n: n // 2
        self.assertLess(abs(7 - 8), abs(0 - 7))
        self.assertGreater(
            first_coalescence_time(operation, 7, 8),
            first_coalescence_time(operation, 0, 7),
        )

    def test_collision_spectrum_does_not_recover_labelled_merge_pairs(self) -> None:
        # Two different deterministic maps have the same fiber-size spectrum at
        # every positive step but merge different labelled pairs.
        first = lambda n: 0 if n == 1 else n
        second = lambda n: 0 if n == 2 else n
        states = (0, 1, 2, 3)
        first_times = labelled_pair_merge_times(first, states, max_steps=3)
        second_times = labelled_pair_merge_times(second, states, max_steps=3)
        self.assertEqual(first_times[(0, 1)], 1)
        self.assertIsNone(first_times[(0, 2)])
        self.assertEqual(second_times[(0, 2)], 1)
        self.assertIsNone(second_times[(0, 1)])
        for degree in range(1, 5):
            for step in range(1, 4):
                self.assertEqual(
                    collision_increment_degree(first, states, degree, step),
                    collision_increment_degree(second, states, degree, step),
                )


if __name__ == "__main__":
    unittest.main()
