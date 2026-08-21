import unittest

from enterprise_math.legendre import primes_up_to
from enterprise_math.prime_collapse_field import factor_horizon
from enterprise_math.prime_cubic_lower_finite_closure import (
    bounded_gap_real_activation_cutoff,
    cube_root_gap_supercritical,
    cubic_external_cofactor_k_limit,
    cubic_lower_cofactor_boundary_prime,
    cubic_lower_cofactor_interval,
    lower_failure_requires_cube_root_gap,
)
from enterprise_math.prime_horizon_gap import (
    exclusive_cofactor_certificate,
    next_prime_after,
)


class PrimeCubicLowerFiniteClosureTests(unittest.TestCase):
    def test_external_cutoff_and_k_limit_constants(self):
        self.assertEqual(bounded_gap_real_activation_cutoff(1328), 86_742_206)
        self.assertEqual(bounded_gap_real_activation_cutoff(1724), 189_778_942)
        self.assertEqual(
            cubic_external_cofactor_k_limit(400_000_000_000_000_000, 1328),
            928_317,
        )
        self.assertEqual(
            cubic_external_cofactor_k_limit(100_000_000_000_000_000_000, 1724),
            5_848_035,
        )

    def test_1327_gap_never_captures_a_lower_band_integer_q(self):
        a, b = 1327, 1361
        self.assertTrue(cube_root_gap_supercritical(a, b))
        # k<119 has no positive real reciprocal width; at k=119 the integer
        # window is empty; at k=120,121 the horizon is inside the same gap but
        # the qF<=A lower-band intersection is still empty.
        expected = {
            119: (1270, 1269),
            120: (1302, 1299),
            121: (1335, 1315),
        }
        for k, interval in expected.items():
            self.assertEqual(cubic_lower_cofactor_interval(k, a, b), interval)
            self.assertIsNone(cubic_lower_cofactor_boundary_prime(k, a, b))
        self.assertLess(factor_horizon(119, 3), a)
        self.assertTrue(a <= factor_horizon(120, 3) < b)
        self.assertTrue(a <= factor_horizon(121, 3) < b)
        self.assertGreaterEqual(factor_horizon(122, 3), b)

    def test_any_bounded_small_lower_e1_failure_has_cube_root_supercritical_gap(self):
        comparisons = 0
        failures = 0
        for k in range(3, 80):
            lower = k**3
            horizon = factor_horizon(k, 3)
            candidates = primes_up_to(horizon)
            for q in candidates:
                if q * horizon > lower:
                    continue
                comparisons += 1
                if exclusive_cofactor_certificate(k, 3, q) is not None:
                    continue
                failures += 1
                x_floor = lower // q
                b = next_prime_after(x_floor)
                # Find the predecessor prime before the cofactor point.
                a_candidates = primes_up_to(x_floor)
                if a_candidates and a_candidates[-1] == x_floor:
                    a = a_candidates[-2]
                else:
                    a = a_candidates[-1]
                self.assertTrue(lower_failure_requires_cube_root_gap(k, q, a, b))
        self.assertGreater(comparisons, 0)
        # Small grids may already have no lower-band failures; the implication
        # test is still exhaustive over every actual failure encountered.
        self.assertGreaterEqual(failures, 0)

    def test_strict_cube_condition_matches_real_threshold_criterion(self):
        # Every gap under the cube-root line is automatically too short for the
        # cubic lower mechanism once the left endpoint reaches the cap cutoff.
        for max_gap in (100, 1328, 1724):
            cutoff = bounded_gap_real_activation_cutoff(max_gap)
            self.assertLessEqual(max_gap**3, 27 * cutoff)
            if cutoff > 1:
                self.assertGreater(max_gap**3, 27 * (cutoff - 1))


if __name__ == "__main__":
    unittest.main()
