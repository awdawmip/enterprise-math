import itertools
import math
import unittest

from enterprise_math.arithmetic_witness_budget import (
    arithmetic_derivative,
    arithmetic_wronskian,
    is_relation_adapted,
    pair_budget_profile,
    relation_budget_profile,
    residual_derivative_divisibility,
    support_primes,
)


class ArithmeticWitnessBudgetTests(unittest.TestCase):
    def test_local_residual_divides_arithmetic_derivative(self) -> None:
        psi = {2: 3, 3: -2, 5: 7}
        for n in range(1, 500):
            self.assertTrue(residual_derivative_divisibility(n, psi), n)

    def test_same_radical_witness_examples_have_different_norm_slack(self) -> None:
        first = pair_budget_profile(1, 2, 3, {2: 1, 3: 1}, (1, 2))
        second = pair_budget_profile(1, 8, 9, {2: 1, 3: 2}, (1, 8))

        self.assertEqual(first["residual_demand"], 1)
        self.assertEqual(first["witness_size"], 1)
        self.assertEqual(first["absolute_budget"], 1)
        self.assertEqual(first["norm_budget"], 1)
        self.assertEqual(first["norm_projection_gap"], 0)

        self.assertEqual(second["residual_demand"], 12)
        self.assertEqual(second["witness_size"], 12)
        self.assertEqual(second["absolute_budget"], 12)
        self.assertEqual(second["norm_budget"], 24)
        self.assertEqual(second["norm_projection_gap"], 12)

    def test_cancellation_and_norm_projection_slacks_can_both_be_positive(self) -> None:
        profile = pair_budget_profile(2, 3, 5, {2: 1, 3: 1, 5: 2}, (2, 3))
        self.assertEqual(profile["residual_demand"], 1)
        self.assertEqual(profile["witness_size"], 1)
        self.assertEqual(profile["absolute_budget"], 5)
        self.assertEqual(profile["norm_budget"], 10)
        self.assertEqual(profile["absorption_gap"], 0)
        self.assertEqual(profile["cancellation_gap"], 4)
        self.assertEqual(profile["norm_projection_gap"], 5)
        self.assertEqual(profile["total_gap"], 9)

    def test_same_triple_different_witnesses_change_budget_provenance(self) -> None:
        first = pair_budget_profile(2, 3, 5, {2: 1, 3: 1, 5: 2}, (2, 3))
        second = pair_budget_profile(2, 3, 5, {2: 0, 3: 1, 5: 1}, (2, 3))
        self.assertEqual(first["residual_demand"], second["residual_demand"])
        self.assertNotEqual(
            (first["absorption_gap"], first["cancellation_gap"], first["norm_projection_gap"]),
            (second["absorption_gap"], second["cancellation_gap"], second["norm_projection_gap"]),
        )

    def test_cyclic_wronskians_have_common_absolute_level(self) -> None:
        profile = relation_budget_profile(2, 3, 5, {2: 1, 3: 1, 5: 2})
        sizes = {item["witness_size"] for item in profile["profiles"]}
        self.assertEqual(sizes, {1})

    def test_exact_chain_exhaustively_on_small_adapted_witnesses(self) -> None:
        checked = 0
        for c in range(3, 25):
            for a in range(1, c):
                b = c - a
                if math.gcd(a, b) != 1:
                    continue
                coordinates = support_primes(a, b, c)
                if len(coordinates) > 4:
                    continue
                for vector in itertools.product(range(-2, 3), repeat=len(coordinates)):
                    if all(value == 0 for value in vector):
                        continue
                    psi = dict(zip(coordinates, vector, strict=True))
                    if not is_relation_adapted(a, b, c, psi):
                        continue
                    witness = arithmetic_wronskian(a, b, psi)
                    if witness == 0:
                        continue
                    relation = relation_budget_profile(a, b, c, psi)
                    for pair_profile in relation["profiles"]:
                        self.assertLessEqual(
                            pair_profile["residual_demand"], pair_profile["witness_size"]
                        )
                        self.assertLessEqual(
                            pair_profile["witness_size"], pair_profile["absolute_budget"]
                        )
                        self.assertLessEqual(
                            pair_profile["absolute_budget"], pair_profile["norm_budget"]
                        )
                        self.assertEqual(
                            pair_profile["total_gap"],
                            pair_profile["absorption_gap"]
                            + pair_profile["cancellation_gap"]
                            + pair_profile["norm_projection_gap"],
                        )
                    checked += 1
        self.assertGreater(checked, 100)

    def test_rejects_nonadapted_and_degenerate_witnesses(self) -> None:
        with self.assertRaises(ValueError):
            pair_budget_profile(2, 3, 5, {2: 1, 3: 1, 5: 1}, (2, 3))
        with self.assertRaises(ValueError):
            pair_budget_profile(2, 3, 5, {2: 1, 3: 2, 5: 3}, (2, 3))

    def test_arithmetic_derivative_formula(self) -> None:
        psi = {2: 1, 3: 2}
        self.assertEqual(arithmetic_derivative(8, psi), 12)
        self.assertEqual(arithmetic_derivative(9, psi), 12)


if __name__ == "__main__":
    unittest.main()
