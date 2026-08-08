import unittest
from math import gcd

from enterprise_math.alexander_descent import (
    alexander_dual_dimension,
    alexander_dual_tail_identity,
    cutoff_edge_cofactor_window,
    large_divisor_cofactor_descent,
    legendre_one_dimensional_root_squeeze,
    square_basin_dual_threshold,
    square_basin_half_scale_bound,
    squarefree_product,
    two_sided_root_bounds,
)
from enterprise_math.cutoff_pairing import (
    cutoff_crossing_terms,
    threshold_shell_betti,
    transverse_prime_support,
)
from enterprise_math.legendre import anchor_product, is_prime


class AlexanderDescentTests(unittest.TestCase):
    def test_alexander_dual_tail_identity(self):
        prime_sets = [
            [2, 3],
            [2, 3, 5],
            [3, 5, 7, 11],
            [2, 5, 11, 17, 23],
            [3, 5, 7, 11, 13],
        ]
        for primes in prime_sets:
            product = squarefree_product(primes)
            for threshold in range(min(primes), min(product, 180)):
                tail, dual_threshold, dual_tail, signed_dual = (
                    alexander_dual_tail_identity(primes, threshold)
                )
                self.assertEqual(tail, signed_dual)
                self.assertEqual(
                    dual_threshold, (product - 1) // threshold
                )
                self.assertIsInstance(dual_tail, int)

    def test_shell_betti_obey_combinatorial_alexander_duality(self):
        prime_sets = [
            [2, 3, 5],
            [3, 5, 7, 11],
            [2, 5, 11, 17, 23],
            [3, 5, 7, 11, 13, 17],
        ]
        for primes in prime_sets:
            product = squarefree_product(primes)
            r = len(primes)
            for threshold in range(min(primes), min(product, 220)):
                betti = threshold_shell_betti(primes, threshold)
                if not betti:
                    continue
                dual_threshold = (product - 1) // threshold
                for dimension, rank in betti.items():
                    dual_dimension = alexander_dual_dimension(r, dimension)
                    if dual_dimension < 0:
                        # The dual S^-1 case is represented by the empty-face
                        # convention rather than threshold_shell_betti.
                        self.assertEqual(dual_dimension, -1)
                        self.assertLess(dual_threshold, min(primes))
                        self.assertEqual(rank, 1)
                        continue
                    self.assertGreaterEqual(dual_threshold, min(primes))
                    dual_betti = threshold_shell_betti(
                        primes, dual_threshold
                    )
                    self.assertEqual(dual_betti.get(dual_dimension, 0), rank)

    def test_square_basin_dual_threshold_descends_to_half_scale(self):
        saw_nontrivial = False
        for k in range(3, 100):
            anchor = anchor_product(k)
            for n in range(k * k + 1, (k + 1) * (k + 1)):
                if gcd(n, anchor) != 1 or is_prime(n):
                    continue
                support = transverse_prime_support(n, k, anchor)
                if not support or squarefree_product(support) <= 2 * k:
                    continue
                dual_threshold, upper = square_basin_dual_threshold(
                    k, n, support
                )
                self.assertLessEqual(dual_threshold, upper)
                self.assertEqual(upper, square_basin_half_scale_bound(k))
                saw_nontrivial = True
        self.assertTrue(saw_nontrivial)

    def test_large_divisor_cofactor_descends_to_half_scale(self):
        saw_edge = False
        for k in range(3, 100):
            anchor = anchor_product(k)
            for n in range(k * k + 1, (k + 1) * (k + 1)):
                if gcd(n, anchor) != 1 or is_prime(n):
                    continue
                support = transverse_prime_support(n, k, anchor)
                if not support:
                    continue
                least = support[0]
                for c, b, _mu_c, _mu_b in cutoff_crossing_terms(
                    support, least, 2 * k
                ):
                    cofactor, upper = large_divisor_cofactor_descent(
                        k, n, b
                    )
                    self.assertLessEqual(cofactor, upper)
                    edge_cofactor, edge_upper = cutoff_edge_cofactor_window(
                        k, n, least, c
                    )
                    self.assertEqual(edge_cofactor, cofactor)
                    self.assertEqual(edge_upper, upper)
                    self.assertGreaterEqual(
                        2 * least * edge_cofactor, k + 1
                    )
                    saw_edge = True
        self.assertTrue(saw_edge)

    def test_two_sided_root_squeeze_for_nonzero_shell_homology(self):
        prime_sets = [
            [3, 5, 7, 11],
            [3, 5, 7, 11, 13],
            [3, 5, 7, 11, 13, 17],
        ]
        for primes in prime_sets:
            product = squarefree_product(primes)
            least = min(primes)
            for threshold in range(least, min(product, 300)):
                betti = threshold_shell_betti(primes, threshold)
                for dimension, rank in betti.items():
                    self.assertGreater(rank, 0)
                    original, dual, dual_threshold = two_sided_root_bounds(
                        primes, threshold, dimension
                    )
                    self.assertLessEqual(least, original)
                    dual_dimension = alexander_dual_dimension(
                        len(primes), dimension
                    )
                    if dual_dimension >= 0:
                        self.assertIsNotNone(dual)
                        self.assertLessEqual(least, dual)
                        self.assertGreaterEqual(dual_threshold, least)

    def test_actual_one_dimensional_shell_gets_support_size_squeeze(self):
        saw_support_five = False
        for k in range(20, 180):
            anchor = anchor_product(k)
            for n in range(k * k + 1, (k + 1) * (k + 1)):
                if gcd(n, anchor) != 1 or is_prime(n):
                    continue
                support = transverse_prime_support(n, k, anchor)
                if len(support) < 3 or squarefree_product(support) <= 2 * k:
                    continue
                betti = threshold_shell_betti(support, 2 * k)
                if betti.get(1, 0) == 0:
                    continue
                original, dual, dual_threshold, half_scale = (
                    legendre_one_dimensional_root_squeeze(k, n, support)
                )
                least = min(support)
                self.assertLessEqual(least, original)
                self.assertLessEqual(dual_threshold, half_scale)
                if len(support) >= 4:
                    self.assertIsNotNone(dual)
                    self.assertLessEqual(least, dual)
                if len(support) >= 5:
                    saw_support_five = True
        self.assertTrue(saw_support_five)


if __name__ == "__main__":
    unittest.main()
