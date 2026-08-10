import unittest

from enterprise_math.precision_prime_axes import (
    divisor_exponent_coordinates,
    divisor_from_exponent_coordinates,
    divisor_lattice_shape,
    divisor_lattice_size,
    prime_axis_rank,
    prime_axis_rank_sequence,
    prime_axis_rank_stabilized_after,
    prime_axis_support,
    prime_factorization,
    prime_power_axis_scale_chains,
    prime_power_axis_sizes,
    prime_support_stable,
    refinement_rank_monotone,
)


class PrecisionPrimeAxesTests(unittest.TestCase):
    def test_unique_factorization_gives_canonical_axis_rank(self):
        self.assertEqual(prime_factorization(1), ())
        self.assertEqual(prime_factorization(60), ((2, 2), (3, 1), (5, 1)))
        self.assertEqual(prime_axis_rank(1), 0)
        self.assertEqual(prime_axis_rank(60), 3)
        self.assertEqual(prime_axis_support(180), (2, 3, 5))

    def test_divisor_lattice_is_product_of_prime_exponent_chains(self):
        self.assertEqual(divisor_lattice_shape(60), (3, 2, 2))
        self.assertEqual(divisor_lattice_size(60), 12)
        self.assertEqual(divisor_lattice_size(1), 1)
        for divisor in (1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60):
            coordinates = divisor_exponent_coordinates(divisor, 60)
            self.assertEqual(divisor_from_exponent_coordinates(coordinates, 60), divisor)

    def test_prime_power_axis_sizes_multiply_to_scalar_scale(self):
        self.assertEqual(prime_power_axis_sizes(60), (4, 3, 5))
        self.assertEqual(prime_power_axis_scale_chains(60), ((1, 2, 4), (1, 3), (1, 5)))
        product = 1
        for size in prime_power_axis_sizes(180):
            product *= size
        self.assertEqual(product, 180)

    def test_axis_rank_is_monotone_along_divisibility_refinement(self):
        chain = (1, 2, 6, 30, 60, 180, 900)
        self.assertEqual(prime_axis_rank_sequence(chain), (0, 1, 2, 3, 3, 3, 3))
        for coarse, fine in zip(chain, chain[1:]):
            self.assertTrue(refinement_rank_monotone(coarse, fine))
        self.assertTrue(prime_axis_rank_stabilized_after(chain, 3))
        self.assertFalse(prime_axis_rank_stabilized_after(chain, 2))

    def test_precision_can_grow_after_prime_support_stabilizes(self):
        self.assertTrue(prime_support_stable(30, 60))
        self.assertTrue(prime_support_stable(60, 180))
        self.assertEqual(prime_axis_support(30), (2, 3, 5))
        self.assertEqual(prime_axis_rank(30), prime_axis_rank(180))

    def test_new_prime_factor_is_exact_rank_increase_event(self):
        self.assertFalse(prime_support_stable(6, 30))
        self.assertEqual(prime_axis_rank(6) + 1, prime_axis_rank(30))

    def test_invalid_inputs_fail_closed(self):
        with self.assertRaises(ValueError):
            prime_factorization(0)
        with self.assertRaises(ValueError):
            divisor_exponent_coordinates(7, 60)
        with self.assertRaises(ValueError):
            refinement_rank_monotone(6, 20)
        with self.assertRaises(ValueError):
            prime_axis_rank_sequence((1, 6, 10))


if __name__ == "__main__":
    unittest.main()
