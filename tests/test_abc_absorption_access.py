import unittest

from enterprise_math.abc_absorption_access import (
    absorption_access_delay,
    absorption_optimal_radius,
    genuine_tradeoff_requires_three_prime_coordinates,
    rank_one_witness_ray,
    scalar_witness_cost_is_complete_for_two_cost_frontier,
)
from enterprise_math.abc_witness_absorption import certified_absorption_pareto_frontier
from enterprise_math.abc_witness_precision import minimal_witness_cost


class AbcAbsorptionAccessTests(unittest.TestCase):
    def test_rank_one_witness_rays_have_singleton_frontier(self) -> None:
        first = rank_one_witness_ray(1, 8, 9)
        self.assertEqual(first["minimum_witness_radius"], 2)
        self.assertEqual(first["minimum_absorption_redundancy"], 1)
        self.assertEqual(first["absorption_access_delay"], 0)
        self.assertEqual(first["pareto_frontier"], ((2, 1),))

        second = rank_one_witness_ray(1, 3, 4)
        self.assertEqual(second["minimum_witness_radius"], 4)
        self.assertEqual(second["minimum_absorption_redundancy"], 2)
        self.assertEqual(second["absorption_access_delay"], 0)
        self.assertEqual(second["pareto_frontier"], ((4, 2),))

    def test_two_cost_tradeoff_has_positive_access_delay(self) -> None:
        self.assertEqual(minimal_witness_cost(2, 3, 5), 1)
        self.assertEqual(absorption_optimal_radius(2, 3, 5), 2)
        self.assertEqual(absorption_access_delay(2, 3, 5), 1)
        self.assertFalse(scalar_witness_cost_is_complete_for_two_cost_frontier(2, 3, 5))

        self.assertEqual(minimal_witness_cost(2, 7, 9), 1)
        self.assertEqual(absorption_optimal_radius(2, 7, 9, max_bound=6), 5)
        self.assertEqual(absorption_access_delay(2, 7, 9, max_bound=6), 4)
        self.assertEqual(
            certified_absorption_pareto_frontier(2, 7, 9, max_bound=6),
            ((1, 3), (4, 2), (5, 1)),
        )

    def test_three_prime_coordinates_do_not_force_tradeoff(self) -> None:
        self.assertEqual(
            certified_absorption_pareto_frontier(1, 242, 243, max_bound=30),
            ((27, 5),),
        )
        self.assertEqual(absorption_access_delay(1, 242, 243, max_bound=30), 0)
        self.assertTrue(
            scalar_witness_cost_is_complete_for_two_cost_frontier(
                1, 242, 243, max_bound=30
            )
        )

    def test_tradeoff_requires_at_least_three_prime_coordinates(self) -> None:
        self.assertTrue(genuine_tradeoff_requires_three_prime_coordinates(1, 8, 9))
        self.assertTrue(genuine_tradeoff_requires_three_prime_coordinates(1, 3, 4))
        self.assertTrue(genuine_tradeoff_requires_three_prime_coordinates(2, 3, 5))
        self.assertTrue(genuine_tradeoff_requires_three_prime_coordinates(2, 7, 9, max_bound=6))


if __name__ == "__main__":
    unittest.main()
