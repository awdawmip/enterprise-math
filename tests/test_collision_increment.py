import unittest
from itertools import combinations

from enterprise_math.collision_increment import (
    collision_polynomial_from_fiber_sizes,
    merged_fiber_increment_coefficients,
    new_fiber_sizes,
    newly_colliding_pairs_count,
    partition_step_increment,
    polynomial_add,
)


class CollisionIncrementTests(unittest.TestCase):
    def test_two_fiber_increment_recovers_p011_factor_merge_coefficients(self) -> None:
        for a in range(1, 12):
            for b in range(1, 12):
                increment = merged_fiber_increment_coefficients((a, b))
                self.assertEqual(increment[0], 0)
                self.assertEqual(increment[1], a * b)

    def test_pair_coefficient_equals_new_cross_fiber_pairs(self) -> None:
        cases = [(1, 1, 1), (2, 3, 5), (4, 1, 2, 3), (7, 2)]
        for sizes in cases:
            increment = merged_fiber_increment_coefficients(sizes)
            self.assertEqual(increment[1], newly_colliding_pairs_count(sizes))
            direct = sum(a * b for a, b in combinations(sizes, 2))
            self.assertEqual(increment[1], direct)

    def test_full_increment_is_new_polynomial_minus_old_polynomial(self) -> None:
        cases = [(1, 1), (2, 3), (1, 2, 4), (3, 3, 3)]
        for sizes in cases:
            old = collision_polynomial_from_fiber_sizes(sizes)
            new = collision_polynomial_from_fiber_sizes((sum(sizes),))
            increment = merged_fiber_increment_coefficients(sizes)
            reconstructed = polynomial_add(old, increment)
            self.assertEqual(reconstructed, new)

    def test_partition_step_increment_matches_full_partition_difference(self) -> None:
        old_sizes = {"a": 2, "b": 3, "c": 1, "d": 4}
        old_to_new = {"a": "u", "b": "u", "c": "v", "d": "v"}
        increment = partition_step_increment(old_sizes, old_to_new)
        new_sizes = new_fiber_sizes(old_sizes, old_to_new)
        old_poly = collision_polynomial_from_fiber_sizes(old_sizes.values())
        new_poly = collision_polynomial_from_fiber_sizes(new_sizes.values())
        self.assertEqual(polynomial_add(old_poly, increment), new_poly)

    def test_no_merge_has_zero_increment(self) -> None:
        old_sizes = {0: 2, 1: 3, 2: 4}
        old_to_new = {0: "a", 1: "b", 2: "c"}
        increment = partition_step_increment(old_sizes, old_to_new)
        self.assertTrue(all(value == 0 for value in increment))

    def test_coefficients_are_nonnegative(self) -> None:
        for a in range(1, 7):
            for b in range(1, 7):
                for c in range(1, 5):
                    self.assertTrue(
                        all(
                            coefficient >= 0
                            for coefficient in merged_fiber_increment_coefficients((a, b, c))
                        )
                    )

    def test_temporal_increments_telescope(self) -> None:
        initial = {"a": 1, "b": 1, "c": 1, "d": 1}
        step1_map = {"a": "ab", "b": "ab", "c": "c", "d": "d"}
        step1_increment = partition_step_increment(initial, step1_map)
        step1_sizes = new_fiber_sizes(initial, step1_map)

        step2_map = {"ab": "all", "c": "all", "d": "all"}
        step2_increment = partition_step_increment(step1_sizes, step2_map)
        final_sizes = new_fiber_sizes(step1_sizes, step2_map)

        initial_poly = collision_polynomial_from_fiber_sizes(initial.values())
        final_poly = collision_polynomial_from_fiber_sizes(final_sizes.values())
        total_increment = polynomial_add(step1_increment, step2_increment)
        self.assertEqual(polynomial_add(initial_poly, total_increment), final_poly)


if __name__ == "__main__":
    unittest.main()
