import unittest

from enterprise_math.abc_low_capacity_rigidity import (
    classify_low_capacity_integer,
    low_capacity_finite_universe_bound,
    low_capacity_rigidity_holds,
)


class AbcLowCapacityRigidityTests(unittest.TestCase):
    def test_prime_power_capacity_equals_exponent(self) -> None:
        for prime, exponent in ((239, 2), (13, 4), (3, 5), (2, 9)):
            n = prime**exponent
            data = classify_low_capacity_integer(n, max(exponent, 5))
            self.assertTrue(data.prime_power)
            self.assertEqual(data.prime_power_base, prime)
            self.assertEqual(data.prime_power_exponent, exponent)
            self.assertEqual(data.capacity, exponent)

    def test_capacity_below_five_forces_prime_power(self) -> None:
        for n in range(2, 500):
            data = classify_low_capacity_integer(n, 4)
            if data.capacity <= 4:
                self.assertTrue(data.prime_power)
                self.assertEqual(data.capacity, data.prime_power_exponent)

    def test_non_prime_power_low_capacity_lives_in_finite_universe(self) -> None:
        H = 15
        universe = low_capacity_finite_universe_bound(H)
        for n in (6, 10, 12, 18, 22, 30, 242):
            data = classify_low_capacity_integer(n, H)
            if data.capacity <= H and not data.prime_power:
                self.assertEqual(universe % n, 0)
                self.assertTrue(data.all_support_primes_bounded)
                self.assertTrue(data.all_exponents_bounded)

    def test_large_prime_support_cannot_hide_under_small_capacity_horizon(self) -> None:
        data = classify_low_capacity_integer(2 * 101, 20)
        self.assertGreater(data.capacity, 20)
        self.assertFalse(data.all_support_primes_bounded)
        self.assertTrue(low_capacity_rigidity_holds(2 * 101, 20))

    def test_unit_hard_examples_fit_prime_power_or_finite_core_dichotomy(self) -> None:
        first = classify_low_capacity_integer(57121, 2)
        self.assertTrue(first.prime_power)
        self.assertEqual((first.prime_power_base, first.prime_power_exponent), (239, 2))

        second = classify_low_capacity_integer(57122, 21)
        self.assertFalse(second.prime_power)
        self.assertEqual(second.capacity, 21)
        self.assertTrue(low_capacity_rigidity_holds(57122, 21))


if __name__ == "__main__":
    unittest.main()
