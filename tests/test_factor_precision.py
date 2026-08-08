import unittest

from enterprise_math.factor_precision import (
    COMPOSITE,
    PRIME,
    UNRESOLVED,
    factor_certificate_profile,
    factor_precision_compatibility,
    factor_precision_partition,
    factor_survivor_profile,
    factor_survivors,
    factor_witness_state,
    first_factor_shell,
    p017_p018_bridge,
    project_factor_precision,
    smallest_prime_factor,
    square_basin,
    square_basin_factor_certificate,
)
from enterprise_math.legendre import is_prime, primes_up_to


class FactorPrecisionTests(unittest.TestCase):
    def test_factor_witness_projection_is_compatible(self):
        for n in range(2, 120):
            for high in range(0, 30):
                high_state = factor_witness_state(n, high)
                for low in range(0, high + 1):
                    self.assertTrue(
                        factor_precision_compatibility(n, low, high)
                    )
                    self.assertEqual(
                        project_factor_precision(high_state, low),
                        factor_witness_state(n, low),
                    )

    def test_composite_certificate_is_permanent(self):
        n = 77
        profile = factor_certificate_profile(
            n, list(range(0, 12)), complete_horizon=11
        )
        self.assertEqual(profile[:7], [UNRESOLVED] * 7)
        self.assertTrue(all(status == COMPOSITE for status in profile[7:]))

    def test_square_basin_terminal_factor_horizon_is_complete(self):
        for k in range(2, 45):
            for n in square_basin(k):
                status = square_basin_factor_certificate(k, n, k)
                self.assertEqual(status, PRIME if is_prime(n) else COMPOSITE)

    def test_prime_can_remain_unresolved_until_terminal_horizon(self):
        # 29 lies in the k=5 square basin (25,36).  No factor witness ever
        # appears, but factor precision is not complete until cutoff k=5.
        self.assertEqual(square_basin_factor_certificate(5, 29, 2), UNRESOLVED)
        self.assertEqual(square_basin_factor_certificate(5, 29, 3), UNRESOLVED)
        self.assertEqual(square_basin_factor_certificate(5, 29, 5), PRIME)

    def test_survivors_shrink_with_factor_precision(self):
        for k in range(2, 50):
            cutoffs = list(range(0, k + 1))
            counts = factor_survivor_profile(k, cutoffs)
            self.assertEqual(counts, sorted(counts, reverse=True))
            self.assertEqual(
                factor_survivors(k, k),
                [n for n in square_basin(k) if is_prime(n)],
            )

    def test_first_factor_shell_is_exact(self):
        for k in range(2, 40):
            for p in primes_up_to(k):
                shell = first_factor_shell(k, p)
                for n in shell:
                    self.assertEqual(smallest_prime_factor(n), p)

    def test_factor_shells_partition_basin(self):
        for k in range(2, 45):
            data = factor_precision_partition(k)
            shells = data["shells"]
            shell_states = [n for states in shells.values() for n in states]
            survivors = data["final_survivors"]
            self.assertEqual(len(shell_states), len(set(shell_states)))
            self.assertEqual(
                sorted(shell_states + survivors), list(square_basin(k))
            )
            self.assertEqual(data["basin_size"], 2 * k)

    def test_p017_p018_bridge_identity(self):
        for k in range(2, 60):
            data = p017_p018_bridge(k)
            self.assertEqual(
                data["terminal_survivors"],
                data["basin_size"] - data["first_factor_shell_total"],
            )
            self.assertEqual(
                data["terminal_survivors"],
                sum(is_prime(n) for n in square_basin(k)),
            )

    def test_each_composite_exits_at_its_least_prime_factor(self):
        for k in range(2, 40):
            for n in square_basin(k):
                if is_prime(n):
                    continue
                p = smallest_prime_factor(n)
                self.assertLessEqual(p, k)
                before = factor_witness_state(n, p - 1)
                at = factor_witness_state(n, p)
                self.assertEqual(before, ())
                self.assertIn(p, at)


if __name__ == "__main__":
    unittest.main()
