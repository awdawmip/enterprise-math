from fractions import Fraction
import unittest

from enterprise_math.brc_newton_recursion import RationalValuationScale, rational_newton_step
from enterprise_math.brc_newton_schedule_strata import (
    AffineNewtonLayer,
    AffinePolynomial,
    RationalAffineForm,
    affine_contact_order,
    affine_edge_polynomial,
    affine_first_newton_residual,
    affine_root_multiplicity_constraints,
    affine_scheduled_newton_substitution,
    affine_selected_newton_scale,
    affine_taylor_form,
    evaluate_affine_layers,
    evaluate_affine_state,
)

Q = Fraction
ONE = RationalValuationScale.one()


def s(value):
    return RationalValuationScale.from_rational(Q(value))


def f(c=0, u=0, v=0, w=0):
    return RationalAffineForm((Q(c), Q(u), Q(v), Q(w)))


def layers():
    return (
        AffineNewtonLayer(ONE, AffinePolynomial((f(1), f(-2), f(1)))),
        AffineNewtonLayer(s(Q(1, 2)), AffinePolynomial((f(-2, u=1), f(2)))),
        AffineNewtonLayer(s(Q(1, 4)), AffinePolynomial((f(-2, v=1), f(2)))),
        AffineNewtonLayer(s(Q(1, 8)), AffinePolynomial((f(2),))),
        AffineNewtonLayer(s(Q(1, 16)), AffinePolynomial((f(0, w=1),))),
    )


def production_state(step):
    out = {}
    for scale, poly in step.jet:
        for degree, value in enumerate(poly):
            if value:
                out[(scale, degree)] = value
    return out


def affine_state_values(state, params):
    return {(coordinate.residual_scale, coordinate.taylor_degree): value for coordinate, value in evaluate_affine_state(state, params)}


class NewtonScheduleStrataFoundationTests(unittest.TestCase):
    def setUp(self):
        self.layers = layers()
        self.half = s(Q(1, 2))

    def test_affine_taylor_contact_and_scale_strata(self):
        a = self.layers[1].polynomial
        self.assertEqual(affine_taylor_form(a, Q(1), 0), f(0, u=1))
        self.assertEqual(affine_taylor_form(a, Q(1), 1), f(2))
        self.assertEqual(affine_contact_order(a, Q(1), 2, (0, 1, 1)), 1)
        self.assertEqual(affine_contact_order(a, Q(1), 2, (1, 1, 1)), 0)
        self.assertEqual(affine_selected_newton_scale(self.layers, Q(1), 2, (0, 1, 1)), self.half)
        self.assertEqual(affine_selected_newton_scale(self.layers, Q(1), 2, (1, 1, 1)), self.half.root(2))

    def test_affine_edge_and_root_constraints(self):
        edge = affine_edge_polynomial(self.layers, Q(1), 2, self.half)
        self.assertEqual(edge.coefficients, (f(0, v=1), f(2), f(1)))
        constraints = affine_root_multiplicity_constraints(edge, Q(-1), 2)
        self.assertEqual(constraints.zero_forms[0], f(-1, v=1))
        self.assertTrue(constraints.zero_forms[1].is_identically_zero)
        self.assertEqual(constraints.nonzero_form, f(1))
        self.assertTrue(constraints.holds((0, 1, 7)))
        self.assertFalse(constraints.holds((0, 0, 7)))

    def test_first_affine_residual_matches_production_on_contact_stratum(self):
        formal = affine_first_newton_residual(self.layers, Q(1), 2, self.half)
        for v in (-1, 0, 1, 2):
            for w in (-1, 0, 1, 2):
                params = (Q(0), Q(v), Q(w))
                step = rational_newton_step(evaluate_affine_layers(self.layers, params), Q(1), 2)
                self.assertEqual(step.scale, self.half)
                self.assertEqual(production_state(step), affine_state_values(formal, params))

    def test_two_step_affine_schedule_matches_production(self):
        formal1 = affine_first_newton_residual(self.layers, Q(1), 2, self.half)
        formal2 = affine_scheduled_newton_substitution(formal1, Q(-1), 2, self.half)
        for w in (-2, -1, 0, 1, 2):
            params = (Q(0), Q(1), Q(w))
            step1 = rational_newton_step(evaluate_affine_layers(self.layers, params), Q(1), 2)
            self.assertEqual(step1.edge_polynomial, (Q(1), Q(2), Q(1)))
            step2 = rational_newton_step(step1.jet, Q(-1), 2)
            self.assertEqual(step2.scale, self.half)
            self.assertEqual(step2.edge_polynomial, (Q(w), Q(2), Q(1)))
            self.assertEqual(production_state(step2), affine_state_values(formal2, params))

    def test_non_open_witness(self):
        base = rational_newton_step(evaluate_affine_layers(self.layers, (0, 1, 1)), Q(1), 2)
        self.assertEqual(base.scale, self.half)
        for denominator in range(2, 18):
            perturbed = rational_newton_step(
                evaluate_affine_layers(self.layers, (Q(1, denominator), 1, 1)),
                Q(1),
                2,
            )
            self.assertEqual(perturbed.scale, self.half.root(2))

    def test_type_and_dimension_guards(self):
        with self.assertRaises(ValueError):
            RationalAffineForm(())
        with self.assertRaises(ValueError):
            f(1).evaluate((1, 2))
        with self.assertRaises(ValueError):
            AffinePolynomial((RationalAffineForm((Q(1), Q(0))), f(2)))
        with self.assertRaises(TypeError):
            affine_contact_order(self.layers[1].polynomial, 1, True, (0, 0, 0))
        with self.assertRaises(ValueError):
            affine_root_multiplicity_constraints(
                affine_edge_polynomial(self.layers, Q(1), 2, self.half), Q(-1), 0
            )


if __name__ == "__main__":
    unittest.main()
