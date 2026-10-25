#!/usr/bin/env python3
"""Exact fourth-highest Newton coefficient proof certificate for auxiliary BRC.

Inputs: R4-EC17--EC22 formal clean-source kernel and Newton transform.
This is not a native Enterprise Math X6 physical calculation, and not independent review.
Requires SymPy; uses exact rational/integer arithmetic only.
"""
from __future__ import annotations

import json
from functools import lru_cache
from math import comb, factorial
from pathlib import Path

import sympy as sp

c, t, v, w = sp.symbols('c t v w', integer=True)
N = (
    sp.expand((1+t)**6 * (1-t) * (1-t*(1+t)**2)),
    sp.expand((1+t)**6 * (t*(1-t*(1+t)**2) + t*(1+t)**2*(1-t))),
    sp.expand(t*t * (1+t)**8),
)
Q1, Q2 = 2*t-t*t, t*t


@lru_cache(None)
def product_polynomial(a: int, s1: int, s2: int):
    return sp.Poly(sp.expand(N[a] * Q1**s1 * Q2**s2), t)


def tcoefficient(a: int, s1: int, s2: int, p, m: int):
    """[t^m] N_a Q1^s1 Q2^s2 (1-2t)^(-p), using rising factorial."""
    return sum(
        coeff * 2**(m-i) * sp.rf(p, m-i) / sp.factorial(m-i)
        for (i,), coeff in product_polynomial(a, s1, s2).terms() if i <= m
    )


def laurent_pole_coefficient(h: int, r: int):
    """Coefficient of (1-z)^(-c-1+h) in [t^(3c+r)] H(z,t)."""
    terms = []
    for ell in range(h+1):
        k = c-ell
        p = k+1
        target_t = r+3*ell
        y_degree = h-ell
        for a in range(min(2, y_degree)+1):
            for i in range(y_degree-a+1):
                rest = y_degree-a-i
                for s2 in range(rest//2+1):
                    s1 = rest-2*s2
                    scale = (
                        (-1)**(i+s1+s2) * sp.ff(3*k,i)/sp.factorial(i)
                        * sp.rf(p,s1+s2)/(sp.factorial(s1)*sp.factorial(s2))
                    )
                    terms.append(scale * tcoefficient(a,s1,s2,p+s1+s2,target_t))
    return sp.factor(sp.expand(sum(terms)))


def symmetric_sums(m,d):
    """e1,e2,e3 of d+1,...,d+m; exact polynomial in m,d."""
    S1 = m*d + m*(m+1)/2
    S2 = m*d*d+d*m*(m+1)+m*(m+1)*(2*m+1)/6
    S3 = (m*d**3+sp.Rational(3,2)*d*d*m*(m+1)
          +sp.Rational(1,2)*d*m*(m+1)*(2*m+1)
          +(m*(m+1)/2)**2)
    return (sp.factor(S1),
            sp.factor((S1**2-S2)/2),
            sp.factor((S1**3-3*S1*S2+2*S3)/6))


def fourth_coefficient(r: int):
    A,B,C,D=[laurent_pole_coefficient(h,r) for h in range(4)]
    d=3*c+r
    e3=symmetric_sums(c,d)[2]
    e2=symmetric_sums(c-1,d)[1]
    e1=symmetric_sums(c-2,d)[0]
    L=sp.factor(A*e3/(c*(c-1)*(c-2))
                +B*e2/((c-1)*(c-2))
                +C*e1/(c-2)+D)
    shifted=sp.factor(L.subs(c,v+3))
    numerator,denominator=sp.fraction(shifted)
    coefficients=sp.Poly(numerator,v).all_coeffs()
    assert sp.expand(shifted-sp.Poly(numerator,v).as_expr()/denominator)==0
    assert all(x.is_Integer and x>0 for x in coefficients)
    return (A,B,C,D,L,shifted,coefficients,denominator)


def choose(n:int,k:int)->int:
    return comb(n,k) if 0<=k<=n else 0


def multiply_one_minus_z(p:list[int], power:int)->list[int]:
    out=p[:]
    for _ in range(power):
        nxt=[0]*(len(out)+1)
        for idx,a in enumerate(out):
            nxt[idx]+=a
            nxt[idx+1]-=a
        out=nxt
    return out


def numerator_polynomials(max_d:int):
    """Independent Z[z] recurrence: h_d=P_d/(1-z)^(floor(d/3)+1)."""
    polys=[]
    for d in range(max_d+1):
        a=d//3
        num=[choose(6,d),-choose(6,d-1)-choose(8,d-1),choose(8,d-2)]
        res=[0]*(d+a+6)
        def add(src, offset=0,scale=1):
            for idx,val in enumerate(src): res[offset+idx]+=scale*val
        add(multiply_one_minus_z(num,a))
        if d>=1: add(multiply_one_minus_z(polys[d-1],a-(d-1)//3),1,2)
        if d>=2: add(multiply_one_minus_z(polys[d-2],a+1-(d-2)//3),1)
        if d>=3: add(polys[d-3],3)
        while len(res)>1 and res[-1]==0: res.pop()
        assert len(res)-1 <= (0 if d==0 else d+a-1)
        polys.append(res)
    return polys


def q_at(polys, d:int, shift:int):
    a=d//3
    j=d+shift
    return sum(val*choose(j-idx+a,a) for idx,val in enumerate(polys[d]) if j>=idx)


def independent_integer_checks(derived):
    max_c=14
    polys=numerator_polynomials(3*max_c+2)
    cases=0
    sample=[]
    for cc in range(3,max_c+1):
        for r in range(3):
            d=3*cc+r
            values=[(k,q_at(polys,d,k)) for k in range(cc+1)]
            poly=sp.Poly(sp.interpolate(values,w),w)
            A,B,C,D,L,*_=derived[r]
            assert poly.degree()==cc
            assert poly.nth(cc)==A.subs(c,cc)/factorial(cc)
            assert poly.nth(cc-3)==L.subs(c,cc)/factorial(cc-3)
            assert poly.eval(0)==q_at(polys,d,0)
            cases+=1
            if cc in (3,4,14):
                sample.append({'c':cc,'r':r,'d':d,
                               'fourth_coefficient':str(poly.nth(cc-3)),
                               'q_at_w0':str(q_at(polys,d,0))})
    return cases,sample


def verify():
    derived={r:fourth_coefficient(r) for r in range(3)}
    cases,sample=independent_integer_checks(derived)
    cert=[]
    for r in range(3):
        A,B,C,D,L,shifted,coeff,den=derived[r]
        cert.append({'r':r,'polynomial_degree':len(coeff)-1,
                     'denominator':int(den),
                     'positive_numerator_coefficients_desc':[int(x) for x in coeff]})
    report={
      'schema':'EM_R4_EC23_FOURTH_NEWTON_EXACT_CERTIFICATE_V1',
      'scientific_status':'AUTHOR_SIDE_SYMBOLIC_PROOF_AND_EXACT_INTEGER_CROSSCHECK_NOT_INDEPENDENTLY_REVIEWED',
      'scope':'positive ordered binary affine auxiliary BRC; not native P000 X6',
      'claim':'For every c>=3 and r in {0,1,2}, [w^(c-3)]q_(3c+r)(3c+r+w) is strictly positive',
      'source_kernel':'E(x,u)=(1-u*x^2)/(1-(1+u)*x+2*u^2*x^4-u^3*x^6)',
      'formal_identity':'H(z,t)=(1+t)^6(1-t*z)(1-t*(1+t)^2*z)/(1-(1+t)^2*z+2*t*(1+t)*z^2-t^2*(1+t)*z^3)',
      'positive_polynomial_certificates':cert,
      'independent_exact_integer_crosschecks':cases,
      'independent_exact_integer_samples':sample,
      'native_x6':'NOT_EXECUTED','owner_claim':'UNVERIFIED','driver_review':'NOT_PERFORMED',
      'unresolved':['fifth and lower Newton coefficients all-grade positivity',
                    'full near-center f_j(2j+s)>=0, s=0..5',
                    'native X6 correspondence','independent formal review']
    }
    path=Path(__file__).with_name('R4_EC23_report.json')
    path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'exact_symbolic_positive_polynomials':3,
        'independent_integer_crosschecks':cases,'sample_first_three':sample[:3],
        'all_pass':True},ensure_ascii=False))

if __name__=='__main__': verify()
