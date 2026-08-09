import itertools
import unittest

from enterprise_math.dimension_contraction import balanced_power_energy
from enterprise_math.discrete_fiber_convexity import (
    balanced_power_increment,
    exchange_energy_increment,
    exchange_minimize,
    exchange_minimum_identity,
    has_decreasing_exchange,
)


class DiscreteFiberConvexityTests(unittest.TestCase):
    def test_forward_increment_matches_direct_energy_difference(self):
        for block_size in range(1, 8):
            for power in range(1, 6):
                for total in range(-20, 21):
                    self.assertEqual(
                        balanced_power_increment(block_size, power, total),
                        balanced_power_energy(block_size, power, total + 1)
                        - balanced_power_energy(block_size, power, total),
                    )

    def test_forward_increment_is_monotone(self):
        for block_size in range(1, 8):
            for power in range(1, 6):
                slopes = [
                    balanced_power_increment(block_size, power, total)
                    for total in range(-30, 31)
                ]
                self.assertEqual(slopes, sorted(slopes))

    def test_exchange_increment_matches_direct_cost_change(self):
        block_sizes = (2, 1, 3, 2)
        for power in range(1, 5):
            for totals in itertools.product(range(-3, 4), repeat=4):
                base = sum(
                    balanced_power_energy(size, power, total)
                    for size, total in zip(block_sizes, totals)
                )
                for receiver in range(4):
                    for donor in range(4):
                        if receiver == donor:
                            continue
                        moved = list(totals)
                        moved[receiver] += 1
                        moved[donor] -= 1
                        moved_cost = sum(
                            balanced_power_energy(size, power, total)
                            for size, total in zip(block_sizes, moved)
                        )
                        self.assertEqual(
                            exchange_energy_increment(
                                block_sizes, power, totals, receiver, donor
                            ),
                            moved_cost - base,
                        )

    def test_exchange_descent_reaches_closed_global_minimum(self):
        capacity_sets = ((1, 1), (2, 1, 3), (2, 2, 1, 3))
        for block_sizes in capacity_sets:
            for power in range(1, 6):
                for totals in itertools.product(range(-3, 4), repeat=len(block_sizes)):
                    actual, expected = exchange_minimum_identity(
                        block_sizes, power, totals
                    )
                    self.assertEqual(actual, expected)
                    minimizer = exchange_minimize(block_sizes, power, totals)
                    self.assertFalse(
                        has_decreasing_exchange(block_sizes, power, minimizer)
                    )

    def test_power_two_or_higher_minimizers_have_unit_slot_balance(self):
        block_sizes = (2, 3, 1)
        for power in range(2, 6):
            for total in range(-12, 13):
                start = (total, 0, 0)
                minimizer = exchange_minimize(block_sizes, power, start)
                self.assertEqual(
                    sum(
                        balanced_power_energy(size, power, value)
                        for size, value in zip(block_sizes, minimizer)
                    ),
                    balanced_power_energy(sum(block_sizes), power, total),
                )


if __name__ == "__main__":
    unittest.main()
