import itertools
import unittest

from enterprise_math.collision_interaction_basis import (
    binomial_interaction_coefficients,
    collision_spectrum_from_fiber_sizes,
    higher_interactions_nonnegative,
    merge_collision_increments,
    merge_response_defect,
    merge_response_defect_from_collisions,
    pair_interaction_strict,
    reconstruct_response_value,
    symmetric_fiber_response,
    symmetric_fiber_response_from_collisions,
)


class CollisionInteractionBasisTests(unittest.TestCase):
    def test_arbitrary_integer_response_table_reconstructs_exactly(self):
        values = (0, 3, -2, 11, 5, 19)
        coefficients = binomial_interaction_coefficients(values)
        for count, expected in enumerate(values):
            self.assertEqual(
                reconstruct_response_value(coefficients, count),
                expected,
            )

    def test_square_response_uses_first_two_collision_orders(self):
        # n^2 = n + 2*C(n,2)
        values = tuple(count * count for count in range(9))
        coefficients = binomial_interaction_coefficients(values)
        self.assertEqual(coefficients[:4], (0, 1, 2, 0))
        self.assertTrue(higher_interactions_nonnegative(values))
        self.assertTrue(pair_interaction_strict(values))

    def test_cube_response_has_integer_three_body_interaction(self):
        # n^3 = n + 6*C(n,2) + 6*C(n,3)
        values = tuple(count ** 3 for count in range(9))
        coefficients = binomial_interaction_coefficients(values)
        self.assertEqual(coefficients[:5], (0, 1, 6, 6, 0))
        self.assertTrue(higher_interactions_nonnegative(values))
        self.assertTrue(pair_interaction_strict(values))

    def test_collision_basis_matches_direct_fiber_response(self):
        fiber_sizes = (4, 3, 1, 1)
        values = (0, 2, 7, -1, 13, 4, 9, 5, 8, 6)
        self.assertEqual(
            symmetric_fiber_response(fiber_sizes, values),
            symmetric_fiber_response_from_collisions(fiber_sizes, values),
        )

    def test_many_small_partitions_and_response_tables(self):
        response_tables = (
            tuple(count for count in range(8)),
            tuple(count * count for count in range(8)),
            (0, 5, -3, 7, 2, 11, -4, 9),
        )
        partitions = (
            (1, 1, 1, 1, 1, 1, 1),
            (2, 2, 3),
            (5, 1, 1),
            (7,),
        )
        for values in response_tables:
            for fiber_sizes in partitions:
                self.assertEqual(
                    symmetric_fiber_response(fiber_sizes, values),
                    symmetric_fiber_response_from_collisions(fiber_sizes, values),
                    msg=(values, fiber_sizes),
                )

    def test_jk_coordinates_match_combinatorial_counts(self):
        fiber_sizes = (3, 2, 1)
        spectrum = collision_spectrum_from_fiber_sizes(fiber_sizes, 3)
        # J0=3 nonempty fibers, J1=6 histories, J2=4 colliding pairs,
        # J3=1 colliding triple.
        self.assertEqual(spectrum, (3, 6, 4, 1))

    def test_merge_defect_decomposes_exactly_into_collision_increments(self):
        old_sizes = (2, 3, 1)
        values = tuple(count ** 3 + 2 * count for count in range(7))
        direct = merge_response_defect(old_sizes, values)
        via_collisions = merge_response_defect_from_collisions(old_sizes, values)
        self.assertEqual(direct, via_collisions)

        increments = merge_collision_increments(old_sizes, 3)
        self.assertEqual(increments[1], 0)
        self.assertGreater(increments[2], 0)
        self.assertGreater(increments[3], 0)

    def test_nonnegative_higher_interactions_force_nonnegative_merge_defects(self):
        response_tables = (
            tuple(count * count for count in range(9)),
            tuple(count ** 3 for count in range(9)),
            tuple(count + 4 * (count * (count - 1) // 2) for count in range(9)),
        )
        merge_groups = (
            (1, 1),
            (1, 2),
            (2, 3),
            (1, 2, 4),
        )
        for values in response_tables:
            self.assertTrue(higher_interactions_nonnegative(values))
            for group in merge_groups:
                self.assertGreaterEqual(merge_response_defect(group, values), 0)

    def test_positive_pair_interaction_forces_strict_growth_on_every_genuine_merge(self):
        values = tuple(count * count for count in range(10))
        self.assertTrue(pair_interaction_strict(values))
        for left in range(1, 5):
            for right in range(1, 5):
                self.assertGreater(merge_response_defect((left, right), values), 0)


if __name__ == "__main__":
    unittest.main()
