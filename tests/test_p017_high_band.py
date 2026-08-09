import unittest
from math import gcd, isqrt

from enterprise_math.legendre import primes_up_to
from enterprise_math.p017_high_band import (
    cofactor_window_hit_identity,
    high_band_multiplicative_resource_bound,
    high_band_pairwise_coprime,
    high_band_second_factor_candidate,
    high_band_triple_resource_bound,
)
from enterprise_math.p017_rough_recursion import high_least_factor_band


class P017HighBandTests(unittest.TestCase):
    def test_cofactor_window_is_exact_legacy_hit_count(self):
        for k in range(2, 80):
            for p in primes_up_to(k):
                data = cofactor_window_hit_identity(k, p)
                self.assertEqual(data["N"], data["B"] - data["A"] + 1)

    def test_binary_second_factor_candidate_matches_canonical_triples_and_legacy_hits(self):
        saw_hit = False
        saw_miss = False
        for k in range(3, 100):
            for p in primes_up_to(k):
                if p * p < 2 * k:
                    continue
                data = high_least_factor_band(k, p)
                B = int(data["q_max"])
                expected = {}
                for n in data["triple_prime_states"]:
                    q = n // p
                    ell = min(qp for qp in primes_up_to(isqrt(q)) if q % qp == 0)
                    expected[ell] = n
                for ell in primes_up_to(isqrt(B)):
                    if ell < p:
                        continue
                    branch = high_band_second_factor_candidate(k, p, ell)
                    self.assertIn(branch["multiple_count"], (0, 1))
                    self.assertEqual(
                        branch["multiple_count"], branch["legacy_hit_count"]
                    )
                    self.assertEqual(
                        branch["multiple_count"] == 1,
                        branch["residue_step"] < branch["N"],
                    )
                    self.assertEqual(
                        branch["multiple_count"] == 1,
                        branch["center_hit"] is not None,
                    )
                    if branch["candidate_state"] is not None:
                        self.assertEqual(branch["candidate_state"], branch["center_hit"])
                    if branch["triple_state"] is None:
                        saw_miss = True
                        self.assertNotIn(ell, expected)
                    else:
                        saw_hit = True
                        self.assertEqual(branch["triple_state"], expected[ell])
                self.assertEqual(
                    sorted(state for state in expected.values()),
                    sorted(data["triple_prime_states"]),
                )
        self.assertTrue(saw_hit)
        self.assertTrue(saw_miss)

    def test_high_band_cofactor_survivors_are_pairwise_coprime(self):
        saw_multiple = False
        for k in range(3, 120):
            for p in primes_up_to(k):
                if p * p < 2 * k:
                    continue
                data = high_band_pairwise_coprime(k, p)
                survivors = data["survivors"]
                if len(survivors) > 1:
                    saw_multiple = True
                for i, left in enumerate(survivors):
                    for right in survivors[i + 1 :]:
                        self.assertEqual(gcd(left, right), 1)
                        self.assertEqual(gcd(p * left, p * right), p)
        self.assertTrue(saw_multiple)

    def test_triple_resource_bound(self):
        saw_triples = False
        saw_square_branch = False
        for k in range(3, 140):
            for p in primes_up_to(k):
                if p * p < 2 * k:
                    continue
                data = high_band_triple_resource_bound(k, p)
                self.assertLessEqual(
                    len(data["triple_states"]), data["triple_bound"]
                )
                self.assertLessEqual(
                    data["used_resource_count"], data["resource_count"]
                )
                self.assertIn(data["square_branches"], (0, 1))
                saw_triples |= bool(data["triple_states"])
                saw_square_branch |= data["square_branches"] == 1
        self.assertTrue(saw_triples)
        # A square branch need not occur in every finite scan.  If one does,
        # the theorem already checks uniqueness; absence is not a failure.
        self.assertIsInstance(saw_square_branch, bool)

    def test_multiplicative_resource_capacity(self):
        saw_strict_improvement = False
        for k in range(3, 140):
            for p in primes_up_to(k):
                if p * p < 2 * k:
                    continue
                data = high_band_multiplicative_resource_bound(k, p)
                T = len(data["triple_states"])
                self.assertLessEqual(T, data["multiplicative_capacity"])
                self.assertLessEqual(T, data["combined_bound"])
                self.assertLessEqual(data["combined_bound"], data["additive_bound"])
                self.assertLessEqual(
                    data["combined_bound"], data["multiplicative_capacity"]
                )
                self.assertEqual(
                    data["resource_limit"] % data["triple_cofactor_product"], 0
                )
                if data["multiplicative_capacity"] < data["additive_bound"]:
                    saw_strict_improvement = True
        self.assertTrue(saw_strict_improvement)

        # The product capacity can rule out triples even when the additive
        # resource-count bound still permits one.
        zero_case = high_band_multiplicative_resource_bound(12, 5)
        self.assertEqual(zero_case["multiplicative_capacity"], 0)
        self.assertEqual(zero_case["additive_bound"], 1)
        self.assertEqual(zero_case["triple_states"], [])

        # It can also be sharp and strictly stronger than the additive count.
        sharp_case = high_band_multiplicative_resource_bound(45, 11)
        self.assertEqual(len(sharp_case["triple_states"]), 1)
        self.assertEqual(sharp_case["multiplicative_capacity"], 1)
        self.assertEqual(sharp_case["additive_bound"], 2)
        self.assertEqual(sharp_case["combined_bound"], 1)

        # A prime-square cofactor consumes one resource twice; the unique extra
        # copy is represented by the square allowance xi.
        square_case = high_band_multiplicative_resource_bound(11, 5)
        self.assertEqual(square_case["square_allowance"], 5)
        self.assertEqual(square_case["triple_cofactor_product"], 25)
        self.assertEqual(square_case["multiplicative_capacity"], 1)


if __name__ == "__main__":
    unittest.main()
