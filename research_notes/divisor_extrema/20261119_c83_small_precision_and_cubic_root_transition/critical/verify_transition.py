"""Exact algebra checks for the C83 finite-curvature transition model.

These identities support the explicit local formula and slice calculation.
They do not verify the analytic equidistribution or limiting theorems.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as s


def main():
    D, c, L, u, v = s.symbols('D c L u v', positive=True)
    hnn, hnt, htt = s.symbols('h_nn h_nt h_tt')
    quadratic = L*D/(2*c)*(u**2/(L**2*D**2)*hnn
                            +2*u*v/L**2*hnt
                            +D**2*v**2/L**2*htt)
    expected = D**3/(2*L*c)*htt*v**2 + D/(L*c)*hnt*u*v + hnn*u**2/(2*L*D*c)
    assert s.expand(quadratic-expected) == 0
    # z=D^-2 and lambda=L*c*D give the exact finite second-phase scale.
    assert s.cancel((L*c*D)*D**(-4) - L*c/D**3) == 0

    x=s.symbols('x',real=True)
    slices=[x**2/4,s.Rational(1,2)-(1-x)**2/4,
            s.Rational(1,2)-x**2/4,(1-x)**2/4]
    total=s.factor(sum(slices))
    squares=s.factor(sum(q*q for q in slices))
    assert total == 1
    target=s.Rational(3,8)+x**2*(1-x)**2/4
    assert s.expand(squares-target) == 0
    mean=s.integrate(squares,(x,0,1))
    assert mean == s.Rational(23,60)
    assert target.subs(x,s.Rational(1,2))-target.subs(x,0) == s.Rational(1,64)
    # The primitive-direction factor is 7/(8 zeta(2)), hence 21/(4 pi^2).
    assert F(21,4)*F(1,64) == F(21,256)
    assert F(21,4)*F(23,60) == F(161,80)
    # Coarea projection area over real second phases equals cube volume one.
    rho=s.symbols('rho',real=True)
    volume=2*(s.integrate(s.Rational(1,2)-rho**2/4,(rho,0,1))
              +s.integrate((2-rho)**2/4,(rho,1,2)))
    assert volume == 1
    A_square_integral=2*(s.integrate((s.Rational(1,2)-rho**2/4)**2,(rho,0,1))
                        +s.integrate(((2-rho)**2/4)**2,(rho,1,2)))
    assert A_square_integral == s.Rational(23,60)

    data={
        'scope':'exact algebra and rational slice checks, not analytic proof verification',
        'quadratic_expansion':'D^3*h_tt*v^2/(2*L*c) + D*h_nt*u*v/(L*c) + h_nn*u^2/(2*L*D*c)',
        'finite_second_phase_scale':'L*c/D^3',
        'slice_area_sum':'1',
        'slice_area_square_sum':'3/8 + x^2*(1-x)^2/4',
        'mean_slice_area_square_sum':str(mean),
        'conditioned_rate_difference_coefficient_over_pi_squared_a':'21/256',
        'mean_collision_coefficient_over_pi_squared_a':'161/80',
        'real_phase_slice_area_integral':str(volume),
        'real_phase_slice_square_integral':str(A_square_integral),
        'all_assertions_passed':True,
    }
    out=Path(__file__).with_name('transition_checks.json')
    out.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))


if __name__=='__main__':
    main()
