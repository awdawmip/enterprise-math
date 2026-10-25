#!/usr/bin/env python3
"""Exact auxiliary-BRC third Newton coefficient certificate.

No physical X6 dynamics, pi, trigonometry, or floating-point inference.
The published BRC clean-source kernel is used as a *formal* generating function.
Author-side checker only; project admission/Driver review are separate.
"""
import json
from math import comb, factorial
from pathlib import Path
import sympy as sp

t, c, v, w = sp.symbols('t c v w', integer=True)
N0 = sp.expand((1+t)**6 * (1-t) * (1-t*(1+t)**2))
N1 = sp.expand((1+t)**6 * (t*(1-t*(1+t)**2) + t*(1+t)**2*(1-t)))
N2 = sp.expand(t**2 * (1+t)**8)
Q1, Q2 = 2*t-t**2, t**2


def coeff_t_times_binomial(poly, exponent, degree):
    """[t^degree] poly(t)(1-2t)^(-exponent), exact Z[c]-arithmetic."""
    total = 0
    for (i,), coefficient in sp.Poly(sp.expand(poly), t).terms():
        m = degree-i
        if m >= 0:
            total += coefficient * sp.rf(exponent, m) * 2**m / sp.factorial(m)
    return sp.factor(total)


def abc_and_third(r):
    take = coeff_t_times_binomial
    A = take(N0, c+1, r)
    B = (take(N1-3*c*N0, c+1, r)
         -(c+1)*take(N0*Q1, c+2, r)
         +take(N0, c, r+3))
    C = (take(N2-3*c*N1 + sp.Rational(3, 2)*c*(3*c-1)*N0, c+1, r)
         -(c+1)*take((N1-3*c*N0)*Q1, c+2, r)
         -(c+1)*take(N0*Q2, c+2, r)
         +sp.Rational(1, 2)*(c+1)*(c+2)*take(N0*Q1**2, c+3, r)
         +take(N1-3*(c-1)*N0, c, r+3)
         -c*take(N0*Q1, c+1, r+3)
         +take(N0, c-1, r+6))
    d = 3*c+r
    G = sp.factor(A*(sp.Rational(1, 2)*(d*d+d*(c+1))
                     +(c+1)*(3*c+2)/24) + B*(d+c/2) + C)
    return [sp.factor(x) for x in (A, B, C, G)]


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def multiply_by_one_minus_z(p, exponent):
    out = p[:]
    for _ in range(exponent):
        nxt = [0]*(len(out)+1)
        for i, x in enumerate(out):
            nxt[i] += x
            nxt[i+1] -= x
        out = nxt
    return out


def make_p(max_grade):
    """Independent exact-integer recurrence for h_d=P_d/(1-z)^(floor(d/3)+1)."""
    polys = []
    for d in range(max_grade+1):
        cc = d//3
        numer = [choose(6,d), -choose(6,d-1)-choose(8,d-1), choose(8,d-2)]
        result = [0]*(d+cc+6)
        def add(src, offset=0, scale=1):
            for i, x in enumerate(src):
                result[i+offset] += scale*x
        add(multiply_by_one_minus_z(numer, cc))
        if d>=1: add(multiply_by_one_minus_z(polys[d-1], cc-(d-1)//3), 1, 2)
        if d>=2: add(multiply_by_one_minus_z(polys[d-2], cc+1-(d-2)//3), 1)
        if d>=3: add(polys[d-3], 3)
        while len(result)>1 and result[-1]==0: result.pop()
        assert len(result)-1 <= (0 if d==0 else d+cc-1)
        polys.append(result)
    return polys


def q_at(polys, d, shift):
    cc, j = d//3, d+shift
    return sum(x*choose(j-i+cc,cc) for i,x in enumerate(polys[d]) if j>=i)


def independent_check(forms):
    polys = make_p(80)
    count = 0
    samples = []
    for cc in range(2,15):
        for r in range(3):
            d = 3*cc+r
            p = sp.Poly(sp.interpolate([(shift, q_at(polys,d,shift))
                                        for shift in range(cc+1)], w), w)
            A, B, C, G = forms[r]
            assert p.degree() == cc
            assert p.nth(cc) == A.subs(c, cc)/factorial(cc)
            assert p.nth(cc-1) == (A*(d+(c+1)/2) + B).subs(c,cc)/factorial(cc-1)
            assert p.nth(cc-2) == G.subs(c,cc)/factorial(cc-2)
            count+=1
            if cc in (2,3,14) and r in (0,1,2):
                samples.append({'c':cc,'r':r,'d':d,'third_coefficient':str(p.nth(cc-2))})
    return count,samples


def verify():
    forms = {r: abc_and_third(r) for r in range(3)}
    predicted = {
      0:(32*v**6+1056*v**5+12080*v**4+57840*v**3+114653*v**2+98499*v+52920)/360,
      1:(32*v**7+1344*v**6+20804*v**5+148680*v**4+515543*v**3+905436*v**2+932571*v+451080)/1260,
      2:(8*v**8+416*v**7+8344*v**6+82544*v**5+434707*v**4+1276814*v**3+2251556*v**2+2356701*v+960120)/1260,
    }
    positive = []
    for r in range(3):
        G = forms[r][-1]
        assert sp.cancel(G.subs(c,v+2) - predicted[r]) == 0
        numerator, denominator=sp.fraction(sp.factor(predicted[r]))
        coefficients=sp.Poly(numerator,v).all_coeffs()
        assert all(x>0 for x in coefficients), (r, coefficients)
        positive.append({'r':r,'denominator':int(denominator),
                         'positive_numerator_coefficients_desc':[int(x) for x in coefficients]})
    exact_cases,samples=independent_check(forms)
    result={
      'schema':'EM_R4_EC22_THIRD_NEWTON_EXACT_CERTIFICATE_V1',
      'scientific_status':'AUTHOR_SIDE_SYMBOLIC_PROOF_AND_EXACT_CHECK_NOT_INDEPENDENTLY_REVIEWED',
      'scope':'positive ordered binary affine auxiliary BRC; NOT P000 native X6',
      'claim':'For every c>=2 and r=0,1,2, the third-highest coefficient of q_(3c+r)(3c+r+w) is G_r(c)/(c-2)!>0',
      'source_model':'E(x,u)=(1-u*x^2)/(1-(1+u)*x+2*u^2*x^4-u^3*x^6)',
      'positive_certificate':positive,
      'independent_integer_crosschecks':exact_cases,
      'sample_coefficients':samples,
      'native_X6':'NOT_EXECUTED',
      'owner_CLAIM':'UNVERIFIED',
      'driver_review':'NOT_PERFORMED',
      'unresolved':['uniform positivity for all Newton coefficient indices','near-center f_j(2j+s) for s=0..5','native X6 bridge']
    }
    Path(__file__).with_name('R4_EC22_report.json').write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'symbolic_shifted_polynomials':'PASS',
                      'independent_integer_crosschecks':exact_cases,
                      'sample_c2':samples[:3]},ensure_ascii=False))

if __name__=='__main__':verify()
