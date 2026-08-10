import unittest

from enterprise_math.relation_natural_count_semimodule import (
    booleanized_count_row,
    natural_count_generators_through_horizon,
    new_row_not_in_previous_natural_span,
    triangular_count_coefficient_comparison,
    triangular_count_future_row,
)


class RelationNaturalCountSemimoduleTests(unittest.TestCase):
    def test_exact_count_rows_follow_one_h_formula(self):
        self.assertEqual(
            tuple(triangular_count_future_row(h) for h in range(8)),
            tuple((1, h + 1) for h in range(8)),
        )

    def test_natural_semimodule_chain_is_strict_at_every_checked_horizon(self):
        for horizon in range(1, 30):
            self.assertTrue(new_row_not_in_previous_natural_span(horizon))
            generators = natural_count_generators_through_horizon(horizon)
            self.assertEqual(generators[-1], (1, horizon + 1))
            self.assertNotIn(generators[-1], generators[:-1])

    def test_boolean_support_collapses_all_positive_count_rows(self):
        for horizon in range(12):
            self.assertEqual(
                booleanized_count_row(triangular_count_future_row(horizon)),
                (1, 1),
            )
        report = triangular_count_coefficient_comparison(12)
        self.assertFalse(report.boolean_distinguishes_states)
        self.assertEqual(set(report.boolean_rows), {(1, 1)})

    def test_integer_group_completion_closes_at_horizon_one(self):
        for horizon in range(1, 20):
            report = triangular_count_coefficient_comparison(horizon)
            self.assertTrue(report.natural_chain_strict)
            self.assertTrue(report.integer_envelope_closed_from_horizon_one)
            self.assertEqual(
                report.integer_envelope_basis,
                ((1, 0), (0, 1)),
            )

    def test_count_state_equality_finishes_at_horizon_one_while_N_reconstruction_keeps_growing(self):
        # Current row (1,1) merges the two states.  Horizon-one row (1,2)
        # separates them.  Later exact-count rows add no new state distinction
        # but do remain new irreducible N-semimodule generators.
        current = triangular_count_future_row(0)
        first_future = triangular_count_future_row(1)
        self.assertEqual(current[0], current[1])
        self.assertNotEqual(first_future[0], first_future[1])
        for horizon in range(2, 15):
            self.assertTrue(new_row_not_in_previous_natural_span(horizon))

    def test_validation(self):
        with self.assertRaises(ValueError):
            triangular_count_future_row(-1)
        with self.assertRaises(TypeError):
            triangular_count_future_row(False)
        with self.assertRaises(ValueError):
            new_row_not_in_previous_natural_span(0)
        with self.assertRaises(ValueError):
            booleanized_count_row((1, -1))
        with self.assertRaises(ValueError):
            triangular_count_coefficient_comparison(0)


if __name__ == "__main__":
    unittest.main()
