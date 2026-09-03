from fractions import Fraction
import unittest

from enterprise_math.brc_critical_degeneracy import criticality_polynomial
from enterprise_math.brc_newton_recursion import (
    RationalValuationScale,
    SelectedRootEvaluationAlgebra,
    rational_newton_step,
    selected_root_first_newton_step,
    selected_root_polynomial_vanish_order,
    selected_root_rational_newton_step,
)

Q = Fraction


def poly_add(a, b):
    n = max(len(a), len(b))
    out = [Q(0) for _ in range(n)]
    for i in range(n):
        out[i] = (a[i] if i < len(a) else Q(0)) + (b[i] if i < len(b) else Q(0))
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def poly_scale(a, c):
    return tuple(Q(c) * x for x in a)


def derivative(a):
    if len(a) <= 1:
        return (Q(0),)
    return tuple(Q(i) * a[i] for i in range(1, len(a)))


def factorial(n):
    out = 1
    for k in range(2, n + 1):
        out *= k
    return out


def shift_expansion(poly, eta=Q(1, 2), tau=Q(1, 3)):
    """Exact expansion of poly(z + eta^s + tau^s) by exponential base."""
    raw = {}
    current = poly
    for k in range(len(poly)):
        coeff = tuple(x / factorial(k) for x in current)
        for j in range(k + 1):
            base = (eta ** (k - j)) * (tau ** j)
            weight = Q(__import__('math').comb(k, j))
            raw[base] = poly_add(raw.get(base, (Q(0),)), poly_scale(coeff, weight))
        current = derivative(current)
    return tuple(sorted(raw.items(), key=lambda item: item[0], reverse=True))


class NewtonRecursionFoundationTests(unittest.TestCase):
    def test_rational_valuation_scale_exact_root_and_compare(self):
        scale = RationalValuationScale.from_rational(Q(2, 15)).root(3)
        self.assertEqual(scale.power(3), RationalValuationScale.from_rational(Q(2, 15)))
        self.assertGreater(
            RationalValuationScale.from_rational(Q(1, 3)).root(2).compare(
                RationalValuationScale.from_rational(Q(1, 2))
            ),
            0,
        )

    def test_rational_newton_step(self):
        one = RationalValuationScale.one()
        quarter = RationalValuationScale.from_rational(Q(1, 4))
        step = rational_newton_step(
            ((one, (Q(1), Q(-2), Q(1))), (quarter, (Q(-1),))),
            Q(1),
            2,
        )
        self.assertEqual(step.scale, RationalValuationScale.from_rational(Q(1, 2)))
        self.assertEqual(step.edge_polynomial, (Q(-1), Q(0), Q(1)))

    def test_selected_root_semantic_zero_and_sign(self):
        # K = diag(F,F), F=[[1,1],[1,0]], so p_K=(1-z-z^2)^2.
        F = ((1, 1), (1, 0))
        K = (
            (1, 1, 0, 0),
            (1, 0, 0, 0),
            (0, 0, 1, 1),
            (0, 0, 1, 0),
        )
        p0 = criticality_polynomial(K)
        algebra = SelectedRootEvaluationAlgebra.from_polynomial(p0)
        self.assertFalse(algebra.selector.is_rational)
        self.assertTrue(algebra.zero(algebra.polynomial))
        x = (Q(0), Q(1))
        self.assertGreater(algebra.sign(x), 0)
        self.assertGreater(algebra.sign((Q(1), Q(-1))), 0)
        self.assertLess(algebra.sign((Q(-1), Q(1))), 0)

    def test_algebraic_base_two_rational_newton_steps(self):
        K = (
            (1, 1, 0, 0),
            (1, 0, 0, 0),
            (0, 0, 1, 1),
            (0, 0, 1, 0),
        )
        p0 = criticality_polynomial(K)
        algebra = SelectedRootEvaluationAlgebra.from_polynomial(p0)
        expansion = shift_expansion(tuple(Q(value) for value in p0))
        first = selected_root_first_newton_step(expansion, algebra, 2)
        self.assertEqual(first.scale, RationalValuationScale.from_rational(Q(1, 2)))
        self.assertEqual(selected_root_polynomial_vanish_order(first.edge_polynomial, Q(-1), algebra), 2)
        second = selected_root_rational_newton_step(first.jet, Q(-1), 2, algebra)
        self.assertEqual(second.scale, RationalValuationScale.from_rational(Q(2, 3)))
        self.assertEqual(selected_root_polynomial_vanish_order(second.edge_polynomial, Q(-1), algebra), 2)

    def test_typed_guards(self):
        with self.assertRaises(TypeError):
            RationalValuationScale.from_rational(True)
        with self.assertRaises(ValueError):
            RationalValuationScale.from_rational(0)
        with self.assertRaises(ValueError):
            RationalValuationScale.from_rational(Q(1, 2)).root(0)


if __name__ == "__main__":
    unittest.main()
