from fractions import Fraction
import unittest

from enterprise_math.brc_critical_degeneracy import (
    critical_degeneracy_analysis,
    critical_graph_shaped,
    critical_log_bounds,
    critical_log_correction_from_branches,
    critical_log_correction_state,
    critical_log_less_than_rational,
    critical_log_threshold_analysis,
    critical_log_zero,
    criticality_polynomial,
    smallest_positive_root_selector,
)


Q = Fraction


class CriticalDegeneracyFoundationTests(unittest.TestCase):
    def test_branching_critical_graph_from_explicit_branches(self):
        branches = (
            (0, 0, Q(1, 2)),
            (0, 0, Q(1, 5)),
            (0, 1, Q(1, 2)),
            (0, 1, Q(1, 4)),
            (1, 0, Q(1, 2)),
            (1, 0, Q(1, 6)),
            (1, 1, Q(1, 2)),
            (1, 1, Q(1, 7)),
        )
        analysis = critical_degeneracy_analysis(2, branches)
        self.assertEqual(analysis.reference_cycle_product, Q(1, 2))
        self.assertEqual(analysis.critical_matrix, ((1, 1), (1, 1)))
        self.assertEqual(set(analysis.critical_cycles), {(0,), (1,), (0, 1)})
        state = critical_log_correction_state(analysis.critical_matrix)
        self.assertEqual(state.polynomial, (1, -2))
        self.assertEqual(state.root.exact_root, Q(1, 2))

    def test_unique_cycle_tie_product(self):
        branches = tuple(
            [(0, 1, Q(1, 2))] * 2
            + [(1, 2, Q(1, 2))] * 3
            + [(2, 0, Q(1, 2))] * 4
        )
        analysis, state = critical_log_correction_from_branches(3, branches)
        self.assertEqual(analysis.critical_matrix, ((0, 2, 0), (0, 0, 3), (4, 0, 0)))
        self.assertEqual(state.polynomial, (1, 0, 0, -24))
        self.assertFalse(state.root.is_rational)
        self.assertGreater(state.root.lower, 0)
        self.assertLess(state.root.upper, 1)

    def test_golden_selector(self):
        state = critical_log_correction_state(((1, 1), (1, 0)))
        self.assertEqual(state.polynomial, (1, -1, -1))
        self.assertFalse(state.root.is_rational)
        self.assertLess(Q(3, 5), state.root.lower)
        self.assertLess(state.root.upper, Q(5, 8))
        lower, upper = critical_log_bounds(state.root)
        lower_arg = Q(lower.argument.numerator, lower.argument.denominator)
        upper_arg = Q(upper.argument.numerator, upper.argument.denominator)
        self.assertLess(lower_arg, upper_arg)
        self.assertGreater(lower_arg, 1)

    def test_rational_log_bounds_collapse(self):
        state = critical_log_correction_state(((1, 1), (1, 1)))
        self.assertEqual(state.root.exact_root, Q(1, 2))
        lower, upper = critical_log_bounds(state.root)
        self.assertEqual((lower.argument.numerator, lower.argument.denominator), (2, 1))
        self.assertEqual((upper.argument.numerator, upper.argument.denominator), (2, 1))

    def test_zero_correction_structure(self):
        unit_cycle = ((0, 1, 0), (0, 0, 1), (1, 0, 0))
        self.assertTrue(critical_graph_shaped(unit_cycle))
        self.assertTrue(critical_log_zero(unit_cycle))
        self.assertEqual(critical_log_correction_state(unit_cycle).root.exact_root, 1)
        self.assertFalse(critical_log_zero(((1, 1), (1, 1))))

    def test_threshold_reuses_finite_recurrent_stability(self):
        k = ((1, 1), (1, 1))  # rho(K)=2
        self.assertTrue(critical_log_less_than_rational(k, 3))
        self.assertFalse(critical_log_less_than_rational(k, 2))
        self.assertFalse(critical_log_less_than_rational(k, Q(3, 2)))
        analysis = critical_log_threshold_analysis(k, 3)
        self.assertTrue(analysis.stable)
        self.assertIsNotNone(analysis.canonical_potential)

    def test_criticality_polynomials(self):
        self.assertEqual(criticality_polynomial(((1, 1), (1, 0))), (1, -1, -1))
        self.assertEqual(criticality_polynomial(((0, 2, 0), (0, 0, 3), (4, 0, 0))), (1, 0, 0, -24))
        self.assertEqual(smallest_positive_root_selector((1, -2)).exact_root, Q(1, 2))

    def test_typed_guards(self):
        with self.assertRaises(TypeError):
            critical_degeneracy_analysis(2, ((0, 1, True),))
        with self.assertRaises(ValueError):
            critical_degeneracy_analysis(2, ((0, 1, Q(-1, 2)),))
        with self.assertRaises(ValueError):
            critical_degeneracy_analysis(2, ((0, 1, Q(1, 2)),))
        with self.assertRaises(TypeError):
            criticality_polynomial(((True,),))
        with self.assertRaises(ValueError):
            critical_log_zero(((0, 1), (0, 0)))
        with self.assertRaises(ValueError):
            critical_log_less_than_rational(((1,),), 0)


if __name__ == "__main__":
    unittest.main()
