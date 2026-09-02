from __future__ import annotations

import unittest
from fractions import Fraction

from enterprise_math.brc_weighted import (
    CWM_ONE,
    CWM_ZERO,
    CWMState,
    boolean_support,
    compensate_incoming_weight,
    cwm_edge,
    cwm_from_positive_weights,
    cwm_propagate,
    cwm_recoalesce,
    effective_multiplicity,
    future_cwm_equivalent,
    gauge_scale,
    is_positive_path_realizable,
    multiplicity_surplus_expr,
    one_state_recurrent_cwm,
    projective_scale,
)


class WeightedBRCFoundationToolTests(unittest.TestCase):
    def test_cwm_semiring_examples(self) -> None:
        a = cwm_edge(Fraction(2, 3))
        b = cwm_edge(Fraction(3, 5))
        c = cwm_edge(Fraction(5, 7))

        self.assertEqual(cwm_recoalesce(CWM_ZERO, a), a)
        self.assertEqual(cwm_propagate(CWM_ONE, a), a)
        self.assertEqual(
            cwm_recoalesce(a, b),
            CWMState(2, Fraction(19, 15), Fraction(2, 3)),
        )
        self.assertEqual(
            cwm_propagate(a, b),
            CWMState(1, Fraction(2, 5), Fraction(2, 5)),
        )
        self.assertEqual(
            cwm_propagate(cwm_recoalesce(a, b), c),
            cwm_recoalesce(cwm_propagate(a, c), cwm_propagate(b, c)),
        )

    def test_positive_realizability_boundary(self) -> None:
        self.assertTrue(is_positive_path_realizable(CWM_ZERO))
        self.assertTrue(is_positive_path_realizable(CWMState(1, Fraction(2), Fraction(2))))
        self.assertTrue(is_positive_path_realizable(CWMState(2, Fraction(3), Fraction(2))))
        self.assertFalse(is_positive_path_realizable(CWMState(2, Fraction(2), Fraction(2))))

    def test_equal_branch_multiplicity_and_symbolic_ln(self) -> None:
        state = cwm_from_positive_weights((Fraction(1, 6),) * 3)
        self.assertEqual(state, CWMState(3, Fraction(1, 2), Fraction(1, 6)))
        self.assertEqual(effective_multiplicity(state), 3)
        expr = multiplicity_surplus_expr(state)
        self.assertEqual(expr.argument.numerator, 3)
        self.assertEqual(expr.argument.denominator, 1)

    def test_boolean_support_and_deterministic_degeneration(self) -> None:
        self.assertFalse(boolean_support(CWM_ZERO))
        deterministic = cwm_edge(Fraction(7, 11))
        self.assertTrue(boolean_support(deterministic))
        self.assertEqual(effective_multiplicity(deterministic), 1)
        expr = multiplicity_surplus_expr(deterministic)
        self.assertEqual((expr.argument.numerator, expr.argument.denominator), (1, 1))

    def test_future_safe_and_projective_equivalence(self) -> None:
        left = {
            "t0": CWMState(2, Fraction(3), Fraction(2)),
            "t1": CWMState(1, Fraction(5, 7), Fraction(5, 7)),
        }
        exact_copy = dict(left)
        right = {key: gauge_scale(value, 3) for key, value in left.items()}

        self.assertTrue(future_cwm_equivalent(left, exact_copy))
        self.assertFalse(future_cwm_equivalent(left, right))
        self.assertEqual(projective_scale(left, right), 3)
        self.assertEqual(compensate_incoming_weight(Fraction(2, 5), 3), Fraction(6, 5))

        wrong_counts = dict(right)
        wrong_counts["t0"] = CWMState(3, wrong_counts["t0"].total, wrong_counts["t0"].dominant)
        self.assertIsNone(projective_scale(left, wrong_counts))

    def test_one_state_recurrent_phase_split(self) -> None:
        stable = one_state_recurrent_cwm((Fraction(1, 5), Fraction(1, 5)))
        self.assertEqual(stable.depth(3), CWMState(8, Fraction(8, 125), Fraction(1, 125)))
        self.assertTrue(stable.total_mass_stable)
        self.assertTrue(stable.dominant_bounded)
        self.assertEqual(stable.total_mass_closure, Fraction(5, 3))
        self.assertEqual(
            (
                stable.total_mass_closure_expr().numerator,
                stable.total_mass_closure_expr().denominator,
            ),
            (5, 3),
        )

        multiplicity_driven_divergence = one_state_recurrent_cwm(
            (Fraction(3, 5), Fraction(3, 5))
        )
        self.assertFalse(multiplicity_driven_divergence.total_mass_stable)
        self.assertTrue(multiplicity_driven_divergence.dominant_bounded)
        with self.assertRaises(ValueError):
            multiplicity_driven_divergence.total_mass_closure_expr()

    def test_positive_carrier_rejects_signed_weight(self) -> None:
        with self.assertRaises(ValueError):
            cwm_edge(-1)
        with self.assertRaises(ValueError):
            cwm_from_positive_weights((1, -1))


if __name__ == "__main__":
    unittest.main()
