import unittest

from enterprise_math.core import collapse


class CollapseCommutationTests(unittest.TestCase):
    def test_absorption_when_exponents_are_divisibility_comparable(self) -> None:
        for p in range(1, 7):
            for q in range(1, 7):
                if q % p != 0:
                    continue
                for n in range(0, 2001):
                    self.assertEqual(collapse(collapse(n, q), p), collapse(n, q))
                    self.assertEqual(collapse(collapse(n, p), q), collapse(n, q))

    def test_prime_power_witness_for_incomparable_exponents(self) -> None:
        for p in range(1, 8):
            for q in range(p + 1, 8):
                if q % p == 0:
                    continue
                n = 2**q
                left = collapse(collapse(n, q), p)
                right = collapse(collapse(n, p), q)
                self.assertGreater(left, 1)
                self.assertEqual(right, 1)
                self.assertNotEqual(left, right)

    def test_global_commutation_matches_divisibility_comparability(self) -> None:
        for p in range(1, 7):
            for q in range(1, 7):
                comparable = q % p == 0 or p % q == 0
                if comparable:
                    commutes = all(
                        collapse(collapse(n, q), p) == collapse(collapse(n, p), q)
                        for n in range(0, 1001)
                    )
                else:
                    exponent = max(p, q)
                    witness = 2**exponent
                    commutes = (
                        collapse(collapse(witness, q), p)
                        == collapse(collapse(witness, p), q)
                    )
                self.assertEqual(commutes, comparable)


if __name__ == "__main__":
    unittest.main()
