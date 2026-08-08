import unittest

from enterprise_math.core import collapse


class CollapseCommutationTests(unittest.TestCase):
    def test_divisibility_gives_exact_absorption(self) -> None:
        for p in range(1, 9):
            for q in range(1, 9):
                if q % p != 0:
                    continue
                for n in range(0, 2001):
                    cq = collapse(n, q)
                    cp = collapse(n, p)
                    self.assertEqual(collapse(cq, p), cq)
                    self.assertEqual(collapse(cp, q), cq)

    def test_incomparable_exponents_have_prime_power_witness(self) -> None:
        for p in range(1, 9):
            for q in range(1, 9):
                if p == q or p % q == 0 or q % p == 0:
                    continue
                small, large = sorted((p, q))
                n = 2 ** large
                left = collapse(collapse(n, large), small)
                right = collapse(collapse(n, small), large)
                self.assertNotEqual(left, right)

    def test_small_domain_matches_divisibility_classification(self) -> None:
        for p in range(1, 7):
            for q in range(1, 7):
                globally_commuting = all(
                    collapse(collapse(n, q), p) == collapse(collapse(n, p), q)
                    for n in range(0, 1001)
                )
                self.assertEqual(globally_commuting, (p % q == 0 or q % p == 0))


if __name__ == "__main__":
    unittest.main()
