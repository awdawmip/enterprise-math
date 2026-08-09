import unittest

from enterprise_math.p018_root_state_decomposition import (
    naive_positive_quotient_root_states,
    quotient_root_state_decomposition,
    state_coalescence_horizon,
    state_coalescence_multiplicity_cap,
)
from enterprise_math.p018_power_coalescence import exact_root_fiber_capacity


class P018RootStateDecompositionTests(unittest.TestCase):
    def test_compressed_decomposition_matches_naive_state_set(self):
        for root_exp in range(1, 6):
            for n in range(1, 1200):
                data = quotient_root_state_decomposition(n, root_exp)
                naive = naive_positive_quotient_root_states(n, root_exp)
                self.assertEqual(data["distinct_roots"], naive)
                self.assertEqual(data["distinct_root_count"], len(naive))
                self.assertLessEqual(
                    data["state_count_lower_bound"],
                    data["distinct_root_count"],
                )
                self.assertLessEqual(
                    data["distinct_root_count"],
                    data["state_count_upper_bound"],
                )

    def test_high_branch_is_strictly_decreasing_and_singleton(self):
        saw_nontrivial = False
        for root_exp in range(1, 6):
            for n in (10, 100, 1000, 10_000, 10**6):
                data = quotient_root_state_decomposition(n, root_exp)
                roots = data["high_roots"]
                for left, right in zip(roots, roots[1:]):
                    self.assertGreater(left, right)
                for root in roots:
                    cap = state_coalescence_multiplicity_cap(
                        n, root_exp, root
                    )
                    self.assertEqual(cap, 1)
                    self.assertEqual(
                        exact_root_fiber_capacity(n, root_exp, root), 1
                    )
                saw_nontrivial |= len(roots) > 1
        self.assertTrue(saw_nontrivial)

    def test_low_branch_is_exact_nonempty_fiber_set(self):
        for root_exp in range(1, 5):
            for n in range(10, 400):
                data = quotient_root_state_decomposition(n, root_exp)
                expected = tuple(
                    target
                    for target in range(1, data["horizon"] + 1)
                    if exact_root_fiber_capacity(n, root_exp, target) > 0
                )
                self.assertEqual(data["low_roots"], expected)

    def test_r1_recovers_classical_sqrt_scale(self):
        # The state-specific collision horizon is floor(sqrt(n-1)); the full
        # distinct-quotient decomposition has at most H + floor(n/(H+1)).
        for n in (10, 100, 1000, 10_000, 10**6):
            data = quotient_root_state_decomposition(n, 1)
            self.assertEqual(data["horizon"], state_coalescence_horizon(n, 1))
            self.assertLessEqual(
                data["distinct_root_count"],
                2 * int(n**0.5) + 2,
            )

    def test_state_specific_multiplicity_cap_beats_uniform_basin_cap(self):
        for root_exp in range(1, 5):
            for n in (100, 999, 10_000):
                horizon = state_coalescence_horizon(n, root_exp)
                for target in range(1, horizon + 2):
                    cap = state_coalescence_multiplicity_cap(
                        n, root_exp, target
                    )
                    self.assertIsNotNone(cap)
                    exact = exact_root_fiber_capacity(n, root_exp, target)
                    self.assertLessEqual(exact, cap)

    def test_large_n_uses_small_exact_frontier(self):
        # The implementation enumerates only D high labels plus H low roots;
        # both live on the n^(1/(r+1)) scale.
        for root_exp in (1, 2, 3, 5):
            data = quotient_root_state_decomposition(10**18, root_exp)
            frontier = data["horizon"] + data["high_denominator_max"]
            self.assertEqual(frontier, data["state_count_upper_bound"])
            self.assertLess(frontier, 10**10)

    def test_validation(self):
        with self.assertRaises(ValueError):
            state_coalescence_horizon(0, 2)
        with self.assertRaises(ValueError):
            state_coalescence_multiplicity_cap(10, 0, 1)
        with self.assertRaises(ValueError):
            quotient_root_state_decomposition(0, 2)
        with self.assertRaises(ValueError):
            naive_positive_quotient_root_states(10, 0)


if __name__ == "__main__":
    unittest.main()
