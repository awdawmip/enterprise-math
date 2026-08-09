import unittest

from enterprise_math.abc_witness_absorption import (
    absorption_tradeoff_examples,
    arithmetic_derivative_value,
    arithmetic_wronskian_value,
    certified_absorption_pareto_frontier,
    mason_degree_slack,
    minimum_absorption_redundancy,
    multiplicity_residual_product,
    raw_wronskian_vector,
    scaled_wronskian_signature,
    witness_absorption_redundancy,
)


class AbcWitnessAbsorptionTests(unittest.TestCase):
    def test_actual_wronskian_scale_for_189(self) -> None:
        self.assertEqual(raw_wronskian_vector(1, 8, 9), (12, 0))
        self.assertEqual(arithmetic_derivative_value(1, 8, 9, 8, (1, 2)), 12)
        self.assertEqual(arithmetic_derivative_value(1, 8, 9, 9, (1, 2)), 12)
        self.assertEqual(arithmetic_wronskian_value(1, 8, 9, (1, 2)), 12)
        self.assertEqual(multiplicity_residual_product(1, 8, 9), 12)
        self.assertEqual(witness_absorption_redundancy(1, 8, 9, (1, 2)), 1)
        self.assertEqual(minimum_absorption_redundancy(1, 8, 9), 1)

    def test_absorption_step_can_exceed_one(self) -> None:
        self.assertEqual(multiplicity_residual_product(1, 3, 4), 2)
        self.assertEqual(minimum_absorption_redundancy(1, 3, 4), 2)
        self.assertEqual(minimum_absorption_redundancy(5, 27, 32), 3)

    def test_scaled_signature_retains_wronskian_image_content(self) -> None:
        self.assertEqual(scaled_wronskian_signature(1, 8, 9), (12,))
        self.assertEqual(scaled_wronskian_signature(1, 3, 4), (4,))

    def test_scalar_radius_is_not_complete_for_absorption_language(self) -> None:
        self.assertEqual(
            certified_absorption_pareto_frontier(2, 3, 5, max_bound=3),
            ((1, 2), (2, 1)),
        )
        self.assertEqual(
            certified_absorption_pareto_frontier(5, 7, 12, max_bound=3),
            ((1, 6), (2, 2)),
        )
        examples = absorption_tradeoff_examples()
        self.assertEqual(
            examples["perfect_absorption_tradeoff"]["minimum_absorption_redundancy"],
            1,
        )
        self.assertEqual(
            examples["irreducible_absorption_overhead"]["minimum_absorption_redundancy"],
            2,
        )

    def test_three_level_tradeoff_frontier(self) -> None:
        self.assertEqual(
            certified_absorption_pareto_frontier(2, 7, 9, max_bound=6),
            ((1, 3), (4, 2), (5, 1)),
        )

    def test_mason_slack_decomposition(self) -> None:
        equality = mason_degree_slack(5, 0, 5, 6, 4)
        self.assertEqual(equality["theorem_margin"], 0)
        self.assertEqual(equality["absorption_slack"], 0)
        self.assertEqual(equality["capacity_slack"], 0)

        absorption_only = mason_degree_slack(2, 1, 2, 5, 2)
        self.assertEqual(absorption_only["theorem_margin"], 2)
        self.assertEqual(absorption_only["absorption_slack"], 2)
        self.assertEqual(absorption_only["capacity_slack"], 0)

        capacity_only = mason_degree_slack(2, 2, 2, 5, 1)
        self.assertEqual(capacity_only["theorem_margin"], 2)
        self.assertEqual(capacity_only["absorption_slack"], 0)
        self.assertEqual(capacity_only["capacity_slack"], 2)

    def test_invalid_absorption_request(self) -> None:
        with self.assertRaises(ValueError):
            witness_absorption_redundancy(2, 3, 5, (0, 0, 0))


if __name__ == "__main__":
    unittest.main()
