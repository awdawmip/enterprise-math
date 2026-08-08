import unittest
from math import gcd

from enterprise_math.core import integer_nth_root
from enterprise_math.cutoff_pairing import (
    cutoff_crossing_boundary_sum,
    cutoff_crossing_terms,
    mobius_divisor_tail,
    negative_boundary_root_bound,
    transverse_prime_support,
)
from enterprise_math.legendre import anchor_product, is_prime


class CutoffPairingTests(unittest.TestCase):
    def test_boolean_lattice_tail_pairing(self):
        prime_sets = [
            [2],
            [2, 3],
            [2, 3, 5],
            [3, 5, 7, 11],
            [2, 5, 11, 17, 23],
        ]
        for primes in prime_sets:
            for distinguished in primes:
                for threshold in range(0, 101):
                    self.assertEqual(
                        mobius_divisor_tail(primes, threshold),
                        cutoff_crossing_boundary_sum(
                            primes, distinguished, threshold
                        ),
                    )

    def test_actual_square_basin_large_tail_pairs_to_cutoff_edges(self):
        for k in range(3, 80):
            anchor = anchor_product(k)
            threshold = 2 * k
            for n in range(k * k + 1, (k + 1) * (k + 1)):
                if gcd(n, anchor) != 1 or is_prime(n):
                    continue
                support = transverse_prime_support(n, k, anchor)
                self.assertTrue(support)
                least = support[0]
                self.assertEqual(
                    mobius_divisor_tail(support, threshold),
                    cutoff_crossing_boundary_sum(support, least, threshold),
                )

    def test_negative_boundary_terms_obey_root_hierarchy(self):
        saw_depth = set()
        for k in range(8, 140):
            anchor = anchor_product(k)
            threshold = 2 * k
            for n in range(k * k + 1, (k + 1) * (k + 1)):
                if gcd(n, anchor) != 1 or is_prime(n):
                    continue
                support = transverse_prime_support(n, k, anchor)
                if not support:
                    continue
                least = support[0]
                for c, b, _mu_c, mu_b in cutoff_crossing_terms(
                    support, least, threshold
                ):
                    if mu_b >= 0:
                        continue
                    m, root_bound, reduced = negative_boundary_root_bound(
                        least, b, threshold
                    )
                    self.assertEqual(reduced, c)
                    self.assertLessEqual(least, root_bound)
                    self.assertLessEqual(least ** (2 * m), threshold)
                    self.assertEqual(
                        root_bound,
                        integer_nth_root(threshold, 2 * m),
                    )
                    saw_depth.add(2 * m + 1)
        self.assertIn(3, saw_depth)
        self.assertIn(5, saw_depth)

    def test_every_negative_crossing_has_depth_at_least_three(self):
        for k in range(3, 100):
            anchor = anchor_product(k)
            threshold = 2 * k
            for n in range(k * k + 1, (k + 1) * (k + 1)):
                if gcd(n, anchor) != 1 or is_prime(n):
                    continue
                support = transverse_prime_support(n, k, anchor)
                if not support:
                    continue
                least = support[0]
                for _c, b, _mu_c, mu_b in cutoff_crossing_terms(
                    support, least, threshold
                ):
                    if mu_b < 0:
                        # A one-prime negative edge would require least>2k,
                        # impossible because the least factor is <=k.
                        factors = [p for p in support if b % p == 0]
                        self.assertGreaterEqual(len(factors), 3)
                        self.assertLessEqual(least, integer_nth_root(threshold, 2))


if __name__ == "__main__":
    unittest.main()
