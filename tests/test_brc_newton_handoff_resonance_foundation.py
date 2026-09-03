from fractions import Fraction
import unittest

from enterprise_math.brc_newton_recursion import RationalValuationScale, SelectedRootEvaluationAlgebra
from enterprise_math.brc_newton_handoff import (
    RealRootEvaluationAlgebra,
    RealRootSelector,
    newton_atoms_resonate,
    rational_newton_pushforward,
    real_root_handoff_step,
    real_root_polynomial_vanish_order,
    real_root_rational_newton_step,
    verify_absorbed_root_zero,
)

Q = Fraction


def mul(a, b):
    out = [Q(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def scale(poly, c):
    return tuple(Q(c) * x for x in poly)


class NewtonHandoffResonanceFoundationTests(unittest.TestCase):
    def test_negative_irrational_real_root_selector_and_algebra(self):
        f = (Q(-1), Q(1), Q(1))  # x^2+x-1
        selector = RealRootSelector.from_interval(f, Q(-2), Q(-1))
        algebra = RealRootEvaluationAlgebra(selector)
        self.assertFalse(selector.is_rational)
        self.assertTrue(algebra.zero(f))
        self.assertLess(algebra.sign((Q(0), Q(1))), 0)
        self.assertGreater(algebra.sign((Q(2), Q(1))), 0)  # beta+2 > 0

    def test_irrational_handoff_then_rational_continuation(self):
        f = (Q(-1), Q(1), Q(1))
        fp = (Q(1), Q(2))
        f2 = mul(f, f)
        a = mul(fp, fp)
        linear = scale(mul(f, fp), 2)  # zero at beta, derivative 2*(f')^2
        selector = RealRootSelector.from_interval(f, Q(-2), Q(-1))
        algebra = RealRootEvaluationAlgebra(selector)
        one = RationalValuationScale.one()
        half = RationalValuationScale.from_rational(Q(1, 2))
        quarter = RationalValuationScale.from_rational(Q(1, 4))
        ninth = RationalValuationScale.from_rational(Q(1, 9))
        jet = (
            (one, f2),
            (half, linear),
            (quarter, a),
            (ninth, (Q(1),)),
        )
        first = real_root_handoff_step(jet, algebra, 2)
        self.assertEqual(first.scale, half)
        self.assertEqual(real_root_polynomial_vanish_order(first.edge_polynomial, Q(-1), algebra), 2)
        second = real_root_rational_newton_step(first.jet, Q(-1), 2, algebra)
        self.assertEqual(second.scale, RationalValuationScale.from_rational(Q(2, 3)))

    def test_absorption_zero_certificate(self):
        algebra = SelectedRootEvaluationAlgebra.from_polynomial((1, -1, -1))
        candidate = (Q(-1), Q(-1))  # beta=-(alpha+1)
        edge = ((Q(-1),), (Q(1),), (Q(1),))  # y^2+y-1
        self.assertTrue(verify_absorbed_root_zero(edge, candidate, algebra))

    def test_resonance_pushforward_matches_edge(self):
        one = RationalValuationScale.one()
        half = RationalValuationScale.from_rational(Q(1, 2))
        quarter = RationalValuationScale.from_rational(Q(1, 4))
        jet = (
            (one, (Q(1), Q(-2), Q(1))),
            (half, (Q(-1), Q(1))),
            (quarter, (Q(-1),)),
        )
        analysis = rational_newton_pushforward(jet, Q(1), 2)
        self.assertEqual(analysis.step.scale, half)
        self.assertEqual(analysis.edge_fiber.polynomial, (Q(-1), Q(1), Q(1)))
        self.assertTrue(analysis.edge_fiber.resonant)
        atoms = analysis.edge_fiber.atoms
        self.assertEqual(len(atoms), 3)
        for i in range(len(atoms)):
            for j in range(i + 1, len(atoms)):
                self.assertTrue(newton_atoms_resonate(atoms[i], atoms[j], analysis.step.scale))

    def test_aggregation_cancellation_is_visible(self):
        one = RationalValuationScale.one()
        quarter = RationalValuationScale.from_rational(Q(1, 4))
        analysis = rational_newton_pushforward(
            (
                (one, (Q(1), Q(-2), Q(1))),
                (quarter, (Q(1),)),
                (quarter, (Q(-1),)),
            ),
            Q(1),
            2,
        )
        self.assertEqual(analysis.edge_fiber.polynomial, (Q(0), Q(0), Q(1)))
        self.assertTrue(analysis.edge_fiber.resonant)

    def test_selector_rejects_nonisolating_interval(self):
        with self.assertRaises(ValueError):
            RealRootSelector.from_interval((Q(-1), Q(0), Q(1)), Q(-2), Q(2))


if __name__ == "__main__":
    unittest.main()
