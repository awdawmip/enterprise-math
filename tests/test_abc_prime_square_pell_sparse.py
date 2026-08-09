import unittest

from enterprise_math.abc_prime_square_pell_sparse import (
    pell_coefficient_upper_bound,
    prime_square_failure_pell_witness,
    prime_square_pcc_failure_count_bound,
    uniform_negative_pell_solution_count_bound,
)


class AbcPrimeSquarePellSparseTests(unittest.TestCase):
    def test_239_square_failure_maps_to_negative_pell(self) -> None:
        data = prime_square_failure_pell_witness(239, 3, 5)
        self.assertIsNotNone(data)
        if data is None:
            raise AssertionError("stored prime-square PCC failure disappeared")
        self.assertEqual(data.successor, 57122)
        self.assertEqual(data.square_divisor_root, 169)
        self.assertEqual(data.pell_coefficient, 2)
        self.assertEqual(data.pell_identity, -1)

    def test_nonfailure_has_no_pell_failure_witness(self) -> None:
        self.assertIsNone(prime_square_failure_pell_witness(17, 3, 5))

    def test_exact_coefficient_power_bound(self) -> None:
        X = 10**12
        bound = pell_coefficient_upper_bound(X, 3, 5)
        self.assertLessEqual((2 * bound) ** 5, X**2)
        self.assertGreater((2 * (bound + 1)) ** 5, X**2)

    def test_pell_count_beats_ambient_square_root_for_eta_above_half(self) -> None:
        X = 10**12
        per_k = uniform_negative_pell_solution_count_bound(X)
        self.assertGreater(per_k, 0)
        bound = prime_square_pcc_failure_count_bound(X, 3, 5)
        self.assertLess(bound, 10**6)

    def test_stronger_eta_improves_pell_union_bound(self) -> None:
        X = 10**16
        half_plus = prime_square_pcc_failure_count_bound(X, 3, 5)
        two_thirds = prime_square_pcc_failure_count_bound(X, 2, 3)
        self.assertLessEqual(two_thirds, half_plus)


if __name__ == "__main__":
    unittest.main()
