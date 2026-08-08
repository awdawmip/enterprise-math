import unittest
from math import gcd

from enterprise_math.core import integer_nth_root
from enterprise_math.cutoff_pairing import (
    cutoff_crossing_boundary_sum,
    cutoff_crossing_terms,
    mobius_divisor_tail,
    negative_boundary_root_bound,
    shell_dimension_root_bound,
    threshold_shell_betti,
    threshold_shell_faces,
    threshold_shell_reduced_euler,
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

    def test_threshold_shell_euler_equals_mobius_tail(self):
        prime_sets = [
            [2, 3],
            [2, 3, 5],
            [3, 5, 7, 11],
            [2, 5, 11, 17, 23],
        ]
        for primes in prime_sets:
            for threshold in range(min(primes), 121):
                self.assertEqual(
                    threshold_shell_reduced_euler(primes, threshold),
                    mobius_divisor_tail(primes, threshold),
                )
                betti = threshold_shell_betti(primes, threshold)
                self.assertEqual(
                    sum(
                        (1 if dim % 2 == 0 else -1) * rank
                        for dim, rank in betti.items()
                    ),
                    mobius_divisor_tail(primes, threshold),
                )

    def test_every_shell_dimension_obeys_integer_root_bound(self):
        prime_sets = [
            [2, 3, 5, 7, 11],
            [3, 5, 7, 11, 13, 17],
            [5, 7, 11, 13, 17, 19],
        ]
        saw_dimensions = set()
        for primes in prime_sets:
            least = min(primes)
            for threshold in range(least, 250):
                for c, dimension, _sign in threshold_shell_faces(
                    primes, threshold
                ):
                    bound = shell_dimension_root_bound(
                        least, dimension, threshold
                    )
                    self.assertLessEqual(least, bound)
                    self.assertLessEqual(least ** (dimension + 1), c)
                    self.assertLessEqual(c, threshold)
                    saw_dimensions.add(dimension)
        self.assertIn(0, saw_dimensions)
        self.assertIn(1, saw_dimensions)
        self.assertIn(2, saw_dimensions)

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
                    cutoff_crossing_boundary_sum(
                        support, least, threshold
                    ),
                )
                self.assertEqual(
                    mobius_divisor_tail(support, threshold),
                    threshold_shell_reduced_euler(support, threshold),
                )

    def test_actual_negative_boundary_terms_obey_root_hierarchy(self):
        saw_depth_three = False
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
                    if 2 * m + 1 == 3:
                        saw_depth_three = True
        self.assertTrue(saw_depth_three)

    def test_constructed_depth_five_boundary_obeys_root_hierarchy(self):
        # Generic L011 does not assert that every depth must occur in a tiny
        # consecutive-square sample.  This explicit square-free boundary gives
        # a depth-five negative edge: c=5*7*11*13<=6000<3*c.
        least = 3
        c = 5 * 7 * 11 * 13
        boundary = least * c
        threshold = 6000
        m, root_bound, reduced = negative_boundary_root_bound(
            least, boundary, threshold
        )
        self.assertEqual(m, 2)
        self.assertEqual(reduced, c)
        self.assertLessEqual(least, root_bound)
        self.assertEqual(root_bound, integer_nth_root(threshold, 4))

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
                        self.assertLessEqual(
                            least, integer_nth_root(threshold, 2)
                        )


if __name__ == "__main__":
    unittest.main()
