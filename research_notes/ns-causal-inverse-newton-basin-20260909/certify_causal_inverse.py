#!/usr/bin/env python3
"""Result-specific exact checks for a causal inverse / Newton convergence certificate.

Analytic infinite-dimensional proof: RESEARCH_NOTE.md.
This executable checks finite Fourier identities and rational enclosures only.
It does not simulate or numerically solve the full PDE Newton iteration.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import hashlib
import json
import sys
import sympy as s

ROOT = Path(__file__).resolve().parent
DEP = ROOT / 'inherited'
if not DEP.is_dir():
    DEP = ROOT
sys.path.insert(0, str(DEP))
import inherited_fourier as old

EXPECTED = 'ac6a0a34994c85832bde55e38e195e9552df308906f1a4c4460d3dbdafb1db59'
assert hashlib.sha256((DEP/'inherited_fourier.py').read_bytes()).hexdigest() == EXPECTED
ZERO = s.zeros(3, 1)


def root_bounds(x: F, digits: int = 16) -> tuple[F, F]:
    if x < 0:
        raise ValueError('negative square-root argument')
    scale = 10**digits
    n = isqrt(x.numerator*scale*scale//x.denominator)
    lo, hi = F(n, scale), F(n+1, scale)
    assert lo*lo <= x < hi*hi
    return lo, hi


def exp_bounds(x: F, degree: int = 32) -> tuple[F, F]:
    if x < 0 or x >= degree + 2:
        raise ValueError('nonnegative x < degree+2 required')
    lo = sum((x**j/F(factorial(j)) for j in range(degree+1)), F())
    rem = x**(degree+1)/F(factorial(degree+1))/(1-x/F(degree+2))
    return lo, lo+rem


def rational_radical_bounds(expr: s.Expr) -> tuple[F, F]:
    """Exact enclosures for the positive rational/radical sums used here."""
    lo = hi = F()
    for term in s.Add.make_args(s.expand(expr)):
        coeff, rest = term.as_coeff_Mul()
        c = F(int(s.numer(coeff)), int(s.denom(coeff)))
        assert c >= 0
        if rest == 1:
            a = b = F(1)
        else:
            assert rest.is_Pow and rest.exp == s.Rational(1, 2)
            a, b = root_bounds(F(int(rest.base)))
        lo += c*a
        hi += c*b
    return lo, hi


def unit_plus(k):
    kv = s.Matrix(k)
    e = ZERO.copy()
    e[list(k).index(0)] = 1
    z = old.clean((e+s.I*kv.cross(e)/s.sqrt(old.sq(k)))/s.sqrt(2))
    assert old.clean(s.I*kv.cross(z)-s.sqrt(old.sq(k))*z) == ZERO
    assert s.simplify((s.conjugate(z).T*z)[0]) == 1
    assert kv.dot(z) == 0
    return z


def exact_gram(A, B, radial_power=-1):
    by = defaultdict(list)
    for (k, rate, degree), vec in B.items():
        by[k].append((rate, degree, vec))
    coeff = defaultdict(lambda: s.S.Zero)
    for (k, ra, ma), a in A.items():
        for rb, mb, b in by[k]:
            inner = s.expand(s.re((s.conjugate(a).T*b)[0]))
            if inner:
                coeff[old.sq(k)] += inner*s.Rational(factorial(ma+mb), (ra+rb)**(ma+mb+1))
    return s.simplify(sum(s.Integer(k)**s.Rational(radial_power, 2)*s.expand(z)
                          for k, z in coeff.items()))


def algebra_checks():
    e, c, q = s.symbols('e c q', positive=True)
    # A running energy bound X(t)+c*integral_0^t Q <= e^2 yields this exact primitive.
    primitive = e**2*q-c*q*q/2
    assert s.diff(primitive, q) == e**2-c*q
    assert s.simplify(e**4/(2*c)-primitive-(c*q-e**2)**2/(2*c)) == 0
    a, eta, t, h = s.symbols('a eta t h', real=True)
    phi = eta-t+a*t*t
    assert s.expand(phi.subs(t,t+h)-phi-s.diff(phi,t)*h) == a*h*h
    return {'running_energy_integral_bound': 'integral XQ <= ||w||_X^4/(2c)',
            'trajectory_bilinear_constant': 'C_star/sqrt(2c)',
            'quadratic_Newton_remainder_identity': True}


def main():
    ks = [(1,1,0),(1,0,1),(0,1,1),(2,-2,0)]
    modes = {}
    for k in ks:
        modes[k] = unit_plus(k)
        modes[tuple(-x for x in k)] = s.conjugate(modes[k])
    assert s.Matrix(ks).rank() == 3
    v1 = {(k, old.sq(k), 0): z for k,z in modes.items()}
    n2 = old.ntime(v1, v1)
    v2 = old.solve_heat(n2)
    old.check_equation(v2, n2)
    n3 = old.plus(old.ntime(v1, v2), old.ntime(v2, v1))
    assert (len(v1),len(n2),len(v2),len(n3)) == (8,12,20,130)
    cR = exact_gram(n2,n2)
    c3 = exact_gram(n3,n3)
    targetR = 3*s.sqrt(14)/245+7*s.sqrt(10)/250+s.sqrt(6)/20
    target3 = (17*s.sqrt(42)/202836480+13*s.sqrt(34)/84272400+s.sqrt(26)/346112
               +s.Rational(11,43200)+9449*s.sqrt(10)/17280000
               +757223*s.sqrt(14)/1452124800+321119*s.sqrt(6)/316108800
               +325286597*s.sqrt(2)/46942156800)
    assert s.simplify(cR-targetR) == 0 and s.simplify(c3-target3) == 0
    rlo,rhi = rational_radical_bounds(cR)
    glo,ghi = rational_radical_bounds(c3)
    assert rhi < F(257,1000) < F(507,1000)**2
    assert rlo > F(506,1000)**2
    assert ghi < F(163,10000) < F(16,125)**2
    # Time-integrated all-frequency Hermitian majorant for v=.1*S(t)(a+b).
    l2,u2 = root_bounds(F(2))
    lnest1,_ = root_bounds(1+l2)
    _,unest1 = root_bounds(1+u2)
    lnest2,_ = root_bounds(1+2*l2)
    _,unest2 = root_bounds(1+2*u2)
    mAl,mAu = 6*l2*(F(1,2)+lnest1),6*u2*(F(1,2)+unest1)
    mBl,mBu = 4*l2*(F(1,2)+lnest2),4*u2*(F(1,2)+unest2)
    amp = F(1,10)
    blo,bhi = amp*(mAl/2+mBl/8),amp*(mAu/2+mBu/8)
    assert F(1045,1000) < blo < bhi < F(1046,1000)
    exp_lo,_ = exp_bounds(F(1045,1000))
    _,exp_hi = exp_bounds(F(1046,1000))
    assert exp_lo > F(71,25) and exp_hi < F(57,20)
    nu, c, C = F(1), F(3,4), F(9503,1000)
    L, alpha, eta, radius = F(33,10), F(128,5), F(11,2000), F(7,1000)
    assert L*L*c > F(57,20)**2
    assert alpha*alpha*2*c*c > C*C*F(57,20)**2
    linear_defect_radius = L*amp**3*F(16,125)
    eta_constructive = amp**2*F(507,1000)+linear_defect_radius
    assert eta_constructive < eta
    qcert = 4*alpha*eta
    map_margin = radius-eta-alpha*radius*radius
    lipschitz = 2*alpha*radius
    assert qcert == F(352,625) < 1
    assert map_margin == F(307,1250000) > 0
    assert lipschitz == F(224,625) < 1
    # The raw-norm-only bound for THIS same inverse estimate does not pass.
    assert F(71,25)**2 > F(327,100)**2*c
    assert C*C*F(71,25)**2 > F(25)**2*2*c*c
    raw_q_lower = 4*F(25)*F(327,100)*amp**2*F(506,1000)
    assert raw_q_lower > 1
    # Exact scalar Newton majorant. These are not full PDE Newton solves.
    t = F()
    scalar_steps = []
    for n in range(1,7):
        step = (eta-t+alpha*t*t)/(1-2*alpha*t)
        assert step > 0 and 0 <= t < t+step < radius
        t += step
        scalar_steps.append({'n':n,'majorant_radius_decimal':float(t)})
    data = {
        'status':'PASS',
        'scope':'ordinary analytic theorem plus exact finite Fourier/rational verification; not PDE simulation',
        'inherited_fourier_sha256':EXPECTED,
        'algebra':algebra_checks(),
        'example':{
          'viscosity':'1','amplitude':'1/10','wavevectors':ks,'initial_rank':3,
          'initial_helicity':'+','initial_modes':8,'first_source_packets':12,
          'first_response_packets':20,'linear_defect_packets':130,
          'cR_exact':str(cR),'c3_exact':str(c3),'cR_decimal':float(cR),'c3_decimal':float(c3),
          'growth_integral_upper':'523/500','exp_growth_upper':'57/20',
          'inverse_norm_upper':str(L),'quadratic_feedback_bound':str(alpha),
          'first_Newton_response_norm_upper':str(eta),
          'finite_response_to_exact_inverse_error_upper':str(linear_defect_radius),
          'four_alpha_eta':str(qcert),'certified_global_trajectory_radius':str(radius),
          'ball_inclusion_margin':str(map_margin),'contraction_factor_upper':str(lipschitz),
          'raw_inverse_test_q_lower':str(raw_q_lower),
          'scalar_Newton_majorant_steps':scalar_steps,
          'compared_with':'raw residual norm times this inverse bound only, not all previous criteria'
        },
        'limits':[
          'No arbitrary-data regularity or historical novelty claim.',
          'The causal inverse existence and infinite-tail control are analytic, not finite-mode extrapolation.',
          'Newton convergence is proved in the note; no infinite-dimensional Newton simulation was executed.',
          'Only the specified smooth periodic A3 input and its proved neighborhood are certified.',
          'C_star=9.503 depends on the inherited lattice proof, rerun separately unchanged.'
        ]}
    (ROOT/'verification.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(data,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
