from fractions import Fraction
import unittest

from enterprise_math import (
    rational_critical_scale_lower_bound,
    recurrent_critical_susceptibility,
    recurrent_criticality_polynomial,
    recurrent_edge_responses,
    recurrent_loop_surplus_expr,
    recurrent_loop_zeta_ratio,
    recurrent_response_hessian,
    recurrent_total_susceptibility,
)
from enterprise_math.brc_logarithm import LnExpr
from enterprise_math.brc_weighted_recurrent import finite_recurrent_mass_analysis

Q = Fraction


class RecurrentLoopToolTest(unittest.TestCase):
    def test_zeta_and_susceptibility(self) -> None:
        matrix = [[Q(0), Q(1, 2)], [Q(1, 2), Q(2, 3)]]
        self.assertEqual(recurrent_loop_zeta_ratio(matrix), Q(12))
        self.assertEqual(recurrent_total_susceptibility(matrix), Q(14))
        self.assertIsInstance(recurrent_loop_surplus_expr(matrix), LnExpr)

    def test_edge_response_and_hessian(self) -> None:
        edges = [
            (0, 0, Q(1, 5)),
            (0, 1, Q(1, 4)),
            (1, 0, Q(1, 3)),
        ]
        responses = recurrent_edge_responses(2, edges)
        hessian = recurrent_response_hessian(2, edges)
        self.assertEqual(len(responses), 3)
        self.assertEqual(hessian, tuple(zip(*hessian)))
        for i, response in enumerate(responses):
            self.assertGreater(response, 0)
            self.assertEqual(hessian[i][i], response * (1 + response))
        self.assertTrue(all(value >= 0 for row in hessian for value in row))

    def test_feedforward_edge_response_is_zero(self) -> None:
        edges = [
            (0, 1, Q(1, 5)),
            (1, 0, Q(1, 6)),
            (1, 2, Q(3, 2)),
            (2, 2, Q(1, 7)),
        ]
        responses = recurrent_edge_responses(3, edges)
        hessian = recurrent_response_hessian(3, edges)
        self.assertEqual(responses[2], 0)
        self.assertEqual(hessian[2], (Q(0), Q(0), Q(0), Q(0)))
        self.assertEqual(tuple(row[2] for row in hessian), (Q(0), Q(0), Q(0), Q(0)))

    def test_criticality_polynomials(self) -> None:
        one = recurrent_criticality_polynomial([[Q(3, 5)]])
        self.assertEqual(one.common_denominator, 5)
        self.assertEqual(one.coefficients, (5, -3))
        self.assertEqual(one.evaluate(Q(5, 3)), 0)

        two_matrix = [[Q(0), Q(1, 2)], [Q(1, 2), Q(2, 3)]]
        two = recurrent_criticality_polynomial(two_matrix)
        self.assertEqual(two.common_denominator, 6)
        self.assertEqual(two.coefficients, (36, -24, -9))
        self.assertGreater(two.evaluate(1), 0)
        self.assertLess(two.evaluate(Q(6, 5)), 0)
        self.assertEqual(
            recurrent_critical_susceptibility(two_matrix, Q(1)),
            recurrent_total_susceptibility(two_matrix),
        )

        dag = recurrent_criticality_polynomial(
            [[Q(0), Q(2), Q(0)], [Q(0), Q(0), Q(3)], [Q(0), Q(0), Q(0)]]
        )
        self.assertEqual(dag.coefficients, (1, 0, 0, 0))

    def test_rational_critical_lower_bound(self) -> None:
        matrix = [[Q(0), Q(1, 2)], [Q(1, 2), Q(2, 3)]]
        analysis = finite_recurrent_mass_analysis(matrix)
        self.assertTrue(analysis.stable)
        assert analysis.canonical_potential is not None
        self.assertEqual(
            rational_critical_scale_lower_bound(matrix, analysis.canonical_potential),
            Q(18, 17),
        )

        nil = [[Q(0), Q(1)], [Q(0), Q(0)]]
        self.assertIsNone(rational_critical_scale_lower_bound(nil, [1, 1]))

    def test_unstable_readouts_reject(self) -> None:
        unstable = [[Q(6, 5)]]
        with self.assertRaises(ValueError):
            recurrent_loop_zeta_ratio(unstable)
        with self.assertRaises(ValueError):
            recurrent_total_susceptibility(unstable)
        with self.assertRaises(ValueError):
            recurrent_edge_responses(1, [(0, 0, Q(6, 5))])


if __name__ == "__main__":
    unittest.main()
