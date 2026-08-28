import unittest
from math import comb

from enterprise_math.nonly_valuation_wall_gcd import (
    activation_wall_synchronization_certificate,
    factor_nonly_valuation_wall,
    local_valuation_wall_certificate,
    valuation_wall_step_mod,
    valuation_wall_threshold,
    verify_nonly_valuation_wall_certificate,
)


class NOnlyValuationWallGCDTests(unittest.TestCase):
    def test_exact_local_wall(self):
        self.assertEqual(valuation_wall_threshold(5), 2)
        self.assertEqual(valuation_wall_threshold(7), 3)
        self.assertEqual(valuation_wall_threshold(11), 4)

        before = local_valuation_wall_certificate(1, 5)
        at_wall = local_valuation_wall_certificate(2, 5)
        self.assertEqual(before["valuation_exponent"], 0)
        self.assertFalse(before["divides"])
        self.assertEqual(at_wall["valuation_exponent"], 1)
        self.assertTrue(at_wall["divides"])

    def test_generic_activation_wall_sync_certificate(self):
        cert = activation_wall_synchronization_certificate(4, 8, coefficient=3)
        self.assertEqual(cert["p_lower_exclusive"], 12)
        self.assertEqual(cert["q_upper_inclusive"], 24)
        self.assertEqual(cert["strict_ratio_law"], "q/p < current_seed/previous_seed")
        self.assertTrue(cert["pcf4r_q_lt_2p"])

        non_dyadic = activation_wall_synchronization_certificate(5, 8, coefficient=3)
        self.assertFalse(non_dyadic["pcf4r_q_lt_2p"])

    def test_modular_recurrence_matches_exact_observable(self):
        N = 101 * 103
        residue = 1
        for s in range(1, 25):
            residue, denominator_gcd = valuation_wall_step_mod(residue, s, N)
            self.assertEqual(denominator_gcd, 1)
            self.assertIsNotNone(residue)
            exact = comb(2 * s, s) ** 2 * comb(3 * s, s)
            self.assertEqual(residue, exact % N)

    def test_dyadic_extraction(self):
        cert = factor_nonly_valuation_wall(5 * 7)
        self.assertEqual(cert.factor, 5)
        self.assertEqual(cert.cofactor, 7)
        self.assertEqual(cert.mode, "DYADIC")
        self.assertEqual(cert.first_nonunit_seed, 2)
        self.assertEqual(cert.factor_seed, 2)
        self.assertTrue(verify_nonly_valuation_wall_certificate(cert, replay=True))

    def test_synchronized_fallback_extraction(self):
        cert = factor_nonly_valuation_wall(7 * 11)
        self.assertEqual(cert.factor, 7)
        self.assertEqual(cert.cofactor, 11)
        self.assertEqual(cert.mode, "FALLBACK_T1")
        self.assertEqual(cert.first_nonunit_seed, 4)
        self.assertEqual(cert.fallback_t, 2)
        self.assertEqual(cert.factor_seed, 3)
        self.assertEqual(cert.dyadic_trace[-1], (4, 77))
        self.assertTrue(verify_nonly_valuation_wall_certificate(cert, replay=True))

    def test_small_promised_domain_census(self):
        primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
        modes = set()
        for i, p in enumerate(primes):
            for q in primes[i + 1 :]:
                cert = factor_nonly_valuation_wall(p * q)
                self.assertIn(cert.factor, (p, q))
                self.assertTrue(verify_nonly_valuation_wall_certificate(cert))
                modes.add(cert.mode)
        self.assertIn("DYADIC", modes)
        self.assertTrue({"FALLBACK_T", "FALLBACK_T1"} & modes)

    def test_public_shape_and_local_guards(self):
        with self.assertRaises(ValueError):
            factor_nonly_valuation_wall(2 * 5)
        with self.assertRaises(ValueError):
            factor_nonly_valuation_wall(3 * 5)
        with self.assertRaises(ValueError):
            valuation_wall_threshold(9)
        with self.assertRaises(ValueError):
            local_valuation_wall_certificate(5, 5)
        with self.assertRaises(ValueError):
            activation_wall_synchronization_certificate(4, 4)


if __name__ == "__main__":
    unittest.main()
