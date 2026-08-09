import unittest
from itertools import combinations

from enterprise_math.p017_support_closure import (
    common_center_large_hit,
    large_support_closure,
    transverse_primes,
)


class P017SupportClosureTests(unittest.TestCase):
    def test_l039_hit_matches_direct_basin_enumeration(self):
        for k in range(3, 42):
            primes = transverse_primes(k)
            for size in (2, 3):
                for support in combinations(primes, size):
                    modulus = 1
                    for p in support:
                        modulus *= p
                    if modulus <= 2 * k:
                        continue
                    data = common_center_large_hit(k, modulus)
                    direct = [
                        n
                        for n in range(k * k + 1, (k + 1) * (k + 1))
                        if n % modulus == 0
                    ]
                    self.assertLessEqual(len(direct), 1)
                    if data is None:
                        self.assertEqual(direct, [])
                    else:
                        self.assertEqual(direct, [data["state"]])
                        self.assertLessEqual(data["cofactor"], (k + 1) // 2)

    def test_l040_on_bounded_anchor_surviving_hits(self):
        saw_applicable = False
        saw_smooth = False
        saw_nonsmooth = False
        for k in range(3, 55):
            primes = transverse_primes(k)
            for size in (2, 3):
                for support in combinations(primes, size):
                    product = 1
                    for p in support:
                        product *= p
                    if product <= 2 * k:
                        continue
                    data = large_support_closure(k, list(support))
                    if data is None or not data["anchor_survives"]:
                        continue
                    saw_applicable = True
                    self.assertEqual(
                        data["exact_transverse_support"], data["p_smooth"]
                    )
                    saw_smooth |= bool(data["p_smooth"])
                    saw_nonsmooth |= not bool(data["p_smooth"])
        self.assertTrue(saw_applicable)
        self.assertTrue(saw_smooth)
        self.assertTrue(saw_nonsmooth)

    def test_positive_smooth_closure_example(self):
        data = large_support_closure(16, [5, 11])
        self.assertIsNotNone(data)
        self.assertEqual(data["support_product"], 55)
        self.assertEqual(data["state"], 275)
        self.assertEqual(data["cofactor"], 5)
        self.assertTrue(data["anchor_survives"])
        self.assertTrue(data["p_smooth"])
        self.assertTrue(data["exact_transverse_support"])
        self.assertEqual(data["full_transverse_support"], [5, 11])

    def test_anchor_qualifier_is_logically_necessary(self):
        data = large_support_closure(10, [3, 7])
        self.assertIsNotNone(data)
        self.assertEqual(data["support_product"], 21)
        self.assertEqual(data["state"], 105)
        self.assertEqual(data["cofactor"], 5)
        self.assertFalse(data["anchor_survives"])
        self.assertFalse(data["p_smooth"])
        self.assertTrue(data["exact_transverse_support"])
        self.assertEqual(data["full_transverse_support"], [3, 7])
        self.assertFalse(data["closure_equivalence_applies"])

    def test_invalid_supports_are_rejected(self):
        with self.assertRaises(ValueError):
            large_support_closure(10, [])
        with self.assertRaises(ValueError):
            large_support_closure(10, [3, 3])
        # 5 divides the center 10*11 and is therefore not transverse.
        with self.assertRaises(ValueError):
            large_support_closure(10, [3, 5, 7])
        # A transverse support is valid only in the strict large-modulus regime.
        with self.assertRaises(ValueError):
            large_support_closure(16, [5])


if __name__ == "__main__":
    unittest.main()
