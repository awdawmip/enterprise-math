"""Exact checks for C85 CUSP_POSITION_THEOREM.md; no floating evidence."""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as sp


def run():
    checks = {}
    q = F(1, 10)
    aa = 1 / ((q + 1) * (q + 2))
    bb = 1 / ((q + 2) * (q + 3))

    def primitive(r):
        return aa * (F(3, 2) * r * r - r) - bb * (r ** 3 - r * r / 2)

    hstar = primitive(F(1)) - primitive(F(1, 3))
    checks['angular_polynomial_integral'] = hstar == F(40400, 193347)
    checks['Kq_lower_bound'] = F(15, 14) ** 10 < 2
    checks['five_tenth_root_lower_bound'] = F(7, 6) ** 10 < 5
    checks['atan_lower_bound'] = F(1, 3) - F(1, 3) ** 3 / 3 > F(3, 10)
    q_upper = F(57, 20) + F(13, 16) * F(22, 7) - F(3, 4) * F(3, 10)
    checks['Q_upper_bound'] = q_upper == F(145, 28) and q_upper < F(26, 5)
    bracket = (3 * F(16, 15) * hstar / (2 * (2 - q)) * F(175, 6)
               - 12 * F(26, 5) / ((q + 2) * (q + 6)))
    checks['positive_bracket'] = bracket == F(175414240, 672267519) and bracket > 0
    ratio = (F(16, 15) * (q + 2) * (q + 6) * hstar
             / (8 * (2 - q) * F(26, 5)) * 25 * F(7, 6))
    checks['principal_to_error_ratio'] = ratio == F(21563500, 20467161) and ratio > 1
    coefficient = q * F(7, 22) ** 2 * bracket
    checks['concrete_coefficient'] = coefficient == F(30697492, 11620624257)
    checks['five_power_bound'] = 5 ** 61 < 150 ** 20
    checks['concrete_cusp_gap'] = coefficient / 150 > F(1, 60000)
    checks['untruncated_phase_range'] = 8 < 9  # 2 sqrt(2)/3 < 1.

    z, a, b, m = sp.symbols('z a b m')
    e2 = a*b + a*m + b*m
    e3 = a*b*m
    product = (1-z*a)*(1-z*b)*(1-z*m)
    checks['phase_tail_polynomial'] = sp.expand(
        1-2*product+product.subs(z,2*z)-2*e2*z*z+6*e3*z**3) == 0
    qq, rr = sp.symbols('q r', positive=True)
    checks['middle_linear_coefficient'] = sp.factor(
        1/(qq+1)-(1+rr)/(qq+2)+rr/(qq+3)
        -(1/((qq+1)*(qq+2))-rr/((qq+2)*(qq+3)))) == 0

    angle = sp.symbols('angle')
    full = 1 + 3*sp.pi/8
    partial = sp.Rational(2,25) + 3*angle/2
    mpart = sp.Rational(39,100) + sp.Rational(3,2)*full - partial/2
    angular = 1+sp.pi/4+mpart
    checks['Q_angular_identity'] = sp.expand(
        angular-(sp.Rational(57,20)+13*sp.pi/16-3*angle/4)) == 0

    result = {
        'status': 'exact_arithmetic_checks',
        'all_passed': all(checks.values()),
        'checks': checks,
        'scope': 'Algebra and inequalities in the stated hand proof; not a formal proof checker.',
        'cusp_cutoff': 5,
        'moment_exponent': '1/10',
        'strict_signed_gap_at_cutoff': 'I_quarter_cusp(5)-I_mid_cusp(5)<-1/60000',
        'exact_positive_bracket': str(bracket),
        'exact_principal_to_error_ratio_lower_bound': str(ratio),
    }
    return result


if __name__ == '__main__':
    result = run()
    Path(__file__).with_name('cusp_checks.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['all_passed'] else 1)
