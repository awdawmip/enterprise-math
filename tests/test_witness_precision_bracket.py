import math
import unittest

from enterprise_math.abc_support import multiplicity_residual
from enterprise_math.abc_witness_precision import minimal_witness_cost
from enterprise_math.witness_precision_bracket import (
    abc_demand_floor,
    high_quality_witness_floor,
    normalized_derivative_weight,
    normalized_pair_capacity,
    sparse_two_coordinate_candidates,
    sparse_two_coordinate_upper_bound,
    witness_precision_bracket,
)


class WitnessPrecisionBracketTests(unittest.TestCase):
    def test_normalized_derivative_weight(self) -> None:
        # n=72=2^3*3^2, rad=6:
        # A/m = (6/2)*3 + (6/3)*2 = 13.
        self.assertEqual(normalized_derivative_weight(72), 13)

    def test_normalized_pair_capacity_cancels_complement_residuals(self) -> None:
        # H_(1,8)=12 and m(1)m(8)=4, so K_(1,8)=3.
        self.assertEqual(normalized_pair_capacity(1, 8), 3)
        self.assertEqual(multiplicity_residual(8), 4)

    def test_same_radical_examples_are_certified_exact(self) -> None:
        first = witness_precision_bracket(1, 2, 3, verify_exact=True)
        second = witness_precision_bracket(1, 8, 9, verify_exact=True)
        self.assertEqual((first["lambda_abc"], first["U2"], first["mu"]), (1, 1, 1))
        self.assertEqual((second["lambda_abc"], second["U2"], second["mu"]), (2, 2, 2))
        self.assertTrue(first["certified_exact"])
        self.assertTrue(second["certified_exact"])

    def test_two_coordinate_support_family_can_close_upper_side(self) -> None:
        profile = witness_precision_bracket(1, 7, 8, verify_exact=True)
        self.assertEqual(profile["lambda_abc"], 4)
        self.assertEqual(profile["mu"], 12)
        self.assertEqual(profile["U2"], 12)
        self.assertEqual(profile["upper_gap"], 0)

    def test_bracket_can_remain_nontrivial(self) -> None:
        profile = witness_precision_bracket(1, 36, 37, verify_exact=True)
        self.assertEqual(profile["lambda_abc"], 6)
        self.assertEqual(profile["mu"], 12)
        self.assertEqual(profile["U2"], 24)
        self.assertEqual(profile["width"], 18)
        self.assertFalse(profile["certified_exact"])

    def test_pluecker_minor_candidate_is_nondegenerate(self) -> None:
        candidates = sparse_two_coordinate_candidates(7, 25, 32)
        best = sparse_two_coordinate_upper_bound(7, 25, 32)
        self.assertTrue(candidates)
        self.assertNotEqual(best["best_candidate"]["minor"], 0)
        self.assertEqual(best["U2"], 8)
        self.assertEqual(minimal_witness_cost(7, 25, 32), 8)

    def test_demand_floor_is_a_lower_bound_on_exact_mu(self) -> None:
        checked = 0
        for c in range(3, 35):
            for a in range(1, c):
                b = c - a
                if math.gcd(a, b) != 1:
                    continue
                try:
                    upper = sparse_two_coordinate_upper_bound(a, b, c)["U2"]
                except ValueError:
                    continue
                if upper > 10:
                    continue
                exact = minimal_witness_cost(a, b, c, max_bound=10)
                lower = abc_demand_floor(a, b, c)["lambda_abc"]
                self.assertLessEqual(lower, exact)
                self.assertLessEqual(exact, upper)
                checked += 1
        self.assertGreater(checked, 100)

    def test_high_quality_transport_on_classical_example(self) -> None:
        a = 2
        b = 3**10 * 109
        c = 23**5
        self.assertEqual(a + b, c)
        profile = high_quality_witness_floor(a, b, c, 3, 2)
        self.assertTrue(profile["high_quality"])
        self.assertGreaterEqual(profile["witness_floor"], 1)

    def test_rejects_degenerate_one_plus_one_relation(self) -> None:
        with self.assertRaises(ValueError):
            sparse_two_coordinate_upper_bound(1, 1, 2)


if __name__ == "__main__":
    unittest.main()
