import itertools
import unittest

from enterprise_math.collision_interaction_basis import (
    binomial_interaction_coefficients,
    collision_spectrum_from_fiber_sizes,
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
        values = tuple(count * count for count in range(7))
        coefficients = binomial_interaction_coefficients(values)
        self.assertEqual(coefficients[:4], (0, 1, 2, 0))

    def test_cube_response_has_integer_three_body_interaction(self):
        # n^3 = n + 6*C(n,2) + 6*C(n,3)
        values = tuple(count ** 3 for count in range(7))
        coefficients = binomial_interaction_coefficients(values)
        self.assertEqual(coefficients[:5], (0, 1, 6, 6, 0))

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


if __name__ == "__main__":
    unittest.main()
