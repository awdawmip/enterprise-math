import unittest
from itertools import product

from enterprise_math.integer_future_observability import (
    finite_horizon_observability_matrix,
    full_rank_refinement_index_divides,
    independent_observation_rows,
    integer_future_observability_report,
    integer_matrix_rank,
    linear_future_equivalent,
    maximal_minor_gcd,
)


class IntegerFutureObservabilityTests(unittest.TestCase):
    def test_ttl_shift_total_observation_reaches_full_unimodular_state(self):
        for depth in range(1, 7):
            transition = tuple(
                tuple(
                    1 if row == column + 1 else 0
                    for column in range(depth)
                )
                for row in range(depth)
            )
            observation = (tuple(1 for _ in range(depth)),)
            for horizon in range(depth):
                matrix = finite_horizon_observability_matrix(
                    transition,
                    observation,
                    horizon,
                )
                report = integer_future_observability_report(matrix)
                self.assertEqual(report.rational_rank, horizon + 1)
                self.assertEqual(report.hidden_free_rank, depth - horizon - 1)
                self.assertEqual(report.row_lattice_saturation_index, 1)
            final = integer_future_observability_report(
                finite_horizon_observability_matrix(
                    transition,
                    observation,
                    depth - 1,
                )
            )
            self.assertTrue(final.injective_on_integer_state)
            self.assertTrue(final.integer_linear_decoder_exists)
            self.assertFalse(final.injective_but_nonunimodular)

    def test_crossing_pair_partitions_have_hidden_rank_one(self):
        matrix = (
            (1, 1, 0, 0),
            (0, 0, 1, 1),
            (1, 0, 1, 0),
            (0, 1, 0, 1),
        )
        report = integer_future_observability_report(matrix)
        self.assertEqual(report.rational_rank, 3)
        self.assertEqual(report.hidden_free_rank, 1)
        self.assertFalse(report.injective_on_integer_state)
        self.assertEqual(report.row_lattice_saturation_index, 1)

        hidden = (1, -1, -1, 1)
        zero = (0, 0, 0, 0)
        self.assertTrue(linear_future_equivalent(matrix, hidden, zero))

    def test_three_pair_partitions_are_injective_but_index_two(self):
        matrix = (
            (1, 1, 0, 0),
            (0, 0, 1, 1),
            (1, 0, 1, 0),
            (0, 1, 0, 1),
            (1, 0, 0, 1),
            (0, 1, 1, 0),
        )
        report = integer_future_observability_report(matrix)
        self.assertEqual(report.rational_rank, 4)
        self.assertEqual(report.hidden_free_rank, 0)
        self.assertTrue(report.injective_on_integer_state)
        self.assertEqual(report.row_lattice_saturation_index, 2)
        self.assertFalse(report.integer_linear_decoder_exists)
        self.assertTrue(report.injective_but_nonunimodular)

        seen = {}
        for state in product(range(3), repeat=4):
            signature = tuple(
                sum(coefficient * value for coefficient, value in zip(row, state, strict=True))
                for row in matrix
            )
            self.assertNotIn(signature, seen)
            seen[signature] = state

    def test_more_future_observation_can_improve_integer_coordinates_after_injectivity(self):
        pair_matrix = (
            (1, 1, 0, 0),
            (0, 0, 1, 1),
            (1, 0, 1, 0),
            (0, 1, 0, 1),
            (1, 0, 0, 1),
            (0, 1, 1, 0),
        )
        refined = (*pair_matrix, (1, 0, 0, 0))
        before = integer_future_observability_report(pair_matrix)
        after = integer_future_observability_report(refined)
        self.assertEqual(before.rational_rank, after.rational_rank)
        self.assertEqual(before.hidden_free_rank, after.hidden_free_rank)
        self.assertEqual(before.row_lattice_saturation_index, 2)
        self.assertEqual(after.row_lattice_saturation_index, 1)
        self.assertFalse(before.integer_linear_decoder_exists)
        self.assertTrue(after.integer_linear_decoder_exists)
        self.assertTrue(full_rank_refinement_index_divides(pair_matrix, refined))

    def test_full_rank_refinement_index_divides_for_added_rows(self):
        base = (
            (2, 0),
            (0, 2),
        )
        middle = (*base, (1, 1))
        final = (*middle, (1, 0))
        self.assertEqual(maximal_minor_gcd(base), 4)
        self.assertEqual(maximal_minor_gcd(middle), 2)
        self.assertEqual(maximal_minor_gcd(final), 1)
        self.assertTrue(full_rank_refinement_index_divides(base, middle))
        self.assertTrue(full_rank_refinement_index_divides(middle, final))

    def test_independent_rows_preserve_future_equivalence_kernel(self):
        matrix = (
            (1, 1, 0, 0),
            (0, 0, 1, 1),
            (1, 0, 1, 0),
            (0, 1, 0, 1),
        )
        rows = independent_observation_rows(matrix)
        self.assertEqual(len(rows), integer_matrix_rank(matrix))
        for left in product(range(-1, 2), repeat=4):
            for right in product(range(-1, 2), repeat=4):
                self.assertEqual(
                    linear_future_equivalent(matrix, left, right),
                    linear_future_equivalent(rows, left, right),
                )

    def test_rank_and_saturation_are_independent_diagnostics(self):
        cases = (
            (((1, 0),), (1, 1)),
            (((2, 0), (0, 2)), (2, 4)),
            (((1, 0), (0, 1)), (2, 1)),
            (((1, 1), (1, -1)), (2, 2)),
        )
        for matrix, (rank, index) in cases:
            report = integer_future_observability_report(matrix)
            self.assertEqual(report.rational_rank, rank)
            self.assertEqual(report.row_lattice_saturation_index, index)

    def test_validation(self):
        with self.assertRaises(ValueError):
            integer_future_observability_report(())
        with self.assertRaises(ValueError):
            finite_horizon_observability_matrix(
                ((1, 0),),
                ((1, 0),),
                1,
            )
        with self.assertRaises(ValueError):
            finite_horizon_observability_matrix(
                ((1, 0), (0, 1)),
                ((1,),),
                1,
            )
        with self.assertRaises(ValueError):
            full_rank_refinement_index_divides(
                ((1, 0), (0, 1)),
                ((1, 0), (1, 1)),
            )
        with self.assertRaises(TypeError):
            linear_future_equivalent(
                ((1, 0), (0, 1)),
                (0, False),
                (0, 0),
            )


if __name__ == "__main__":
    unittest.main()
