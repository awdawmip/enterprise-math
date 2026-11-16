"""Exact critical-window Jacobian factors and integrability exponents."""
import json
from fractions import Fraction as Q

import sympy as s


def main():
    a, d = s.symbols("a d")
    m = 7*a**4*d/16
    h = 4-a/(1-a)-4*m/(1+m)-5*a*m/(1+a*m)
    log_g_a = s.Rational(19,5)/a-1/(1-a)-s.diff(m,a)/(1+m)-s.diff(a*m,a)/(1+a*m)
    log_g_d = s.Rational(14,3)/d-1/(1-d)-s.diff(m,d)/(1+m)-s.diff(a*m,d)/(1+a*m)
    cleared = s.factor((log_g_a*s.diff(h,d)-log_g_d*s.diff(h,a))
                       *(1-a)**2*(1-d)**2)
    denominator = 15*d*(7*a**4*d+16)**2*(7*a**5*d+16)**2
    poly = s.Poly(s.cancel(cleared*denominator/(d-1)), a, d)
    assert poly.degree(d) == 5 and poly.degree(a) == 18
    assert poly.as_expr().subs(d,0) == -4587520
    radial = 2*Q(19,5)*Q(15,4)+Q(15,4)-2
    angular = 2*Q(14,3)-Q(4,9)
    tail = Q(4,9)/angular
    outer = 1-radial/6
    assert radial==Q(121,4) and angular==Q(80,9) and tail == Q(1,20)
    assert 1-radial*tail > -1 and Q(2)/radial>tail and outer < -1
    half, q, aa = Q(1,2), Q(21,2), Q(15,4)
    head_power=3*aa-1
    assert head_power == Q(41,4) and head_power/20 == Q(41,80)
    exact_integral=Q(20,21)/(1-head_power/20)
    assert exact_integral==Q(1600,819)
    print(json.dumps(dict(polynomial_degree_d=poly.degree(d),
                          polynomial_degree_A=poly.degree(a), constant_D0=-4587520,
                          jacobian_x_exponent=str(radial), jacobian_D_exponent=str(angular),
                          small_jacobian_exponent=str(tail), other_boundary_exponent=str(2/radial),
                          ambiguity_floor_L_exponent=str(2*tail),
                          critical_density_exponent=str(1+tail),
                          limit_model_jacobian_x_exponent=str(head_power),
                          limit_model_jacobian_Y_exponent=str(2*q-1),
                          limit_model_jacobian_factor_times_C0_squared=str(4*q*aa**2),
                          overload_coefficient_times_j0_to_1_over_20=str(exact_integral)), indent=2))


if __name__ == "__main__":
    main()
