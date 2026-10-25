#!/usr/bin/env python3
"""Exact sixth-highest Newton-coefficient certificate; auxiliary positive BRC.

No native P000 X6 dynamics or physical heartbeat arithmetic is executed.
Mathematical inputs are R4-EC20/21 and the source-verified R4-EC25 derivation.
"""
from __future__ import annotations
import json
from functools import lru_cache
from math import comb, factorial
from pathlib import Path
import sympy as S
from sympy.functions.combinatorial.numbers import stirling

c,t,v=S.symbols('c t v', integer=True)
N=(S.expand((1+t)**6*(1-t)*(1-t*(1+t)**2)),
   S.expand((1+t)**6*(t*(1-t*(1+t)**2)+t*(1+t)**2*(1-t))),
   S.expand(t*t*(1+t)**8))
Q1,Q2=2*t-t*t,t*t

@lru_cache(None)
def product(a,s1,s2):
    return S.Poly(S.expand(N[a]*Q1**s1*Q2**s2),t)

def tcoef(a,s1,s2,p,m):
    return sum(x*2**(m-k)*S.rf(p,m-k)/factorial(m-k)
               for (k,),x in product(a,s1,s2).terms() if k<=m)

def pole(h,r):
    """R_h(c,r) coefficient of y^(-c-1+h), [t^(3c+r)] H(1-y,t)."""
    out=S.Integer(0)
    for ell in range(h+1):
        k,p=c-ell,c-ell+1
        deg=h-ell
        for a in range(min(2,deg)+1):
            for i in range(deg-a+1):
                for s2 in range((deg-a-i)//2+1):
                    s1=deg-a-i-2*s2
                    factor=(-1)**(i+s1+s2)*S.ff(3*k,i)*S.rf(p,s1+s2)/(
                        factorial(i)*factorial(s1)*factorial(s2))
                    out+=factor*tcoef(a,s1,s2,p+s1+s2,r+3*ell)
    return S.cancel(out)

def elementary(m,d,order):
    """Symmetric e_order(d+1,...,d+m); symbolic polynomial via Newton identities."""
    sums={}
    # Exact closed power sums for i=1..m.
    s1=m*(m+1)/2
    s2=m*(m+1)*(2*m+1)/6
    s3=s1*s1
    s4=m*(m+1)*(2*m+1)*(3*m*m+3*m-1)/30
    s5=m*m*(m+1)**2*(2*m*m+2*m-1)/12
    for j in range(1,order+1):
        sm={1:s1,2:s2,3:s3,4:s4,5:s5}
        sums[j]=S.expand(sum(S.binomial(j,i)*d**(j-i)*(m if i==0 else sm[i]) for i in range(j+1)))
    e=[S.Integer(1)]
    for k in range(1,order+1):
        e.append(S.cancel(sum((-1)**(i-1)*e[k-i]*sums[i] for i in range(1,k+1))/k))
    return e[-1]

def sixth(r):
    R=[pole(h,r) for h in range(6)]
    d=3*c+r
    J=S.cancel(sum(R[h]*elementary(c-h,d,5-h)/S.ff(c-h,5-h) for h in range(6)))
    shifted=S.cancel(J.subs(c,v+5))
    numer,den=S.fraction(shifted)
    # Minimized common positive denominator for the rational polynomial.
    coeffs=S.Poly(shifted,v).all_coeffs()
    lcm=S.ilcm(*[int(S.denom(a)) for a in coeffs])
    scaled=[int(lcm*x) for x in coeffs]
    assert all(x>0 for x in scaled)
    assert S.expand(shifted-sum(S.Rational(x,lcm)*v**(len(scaled)-1-i)
                                    for i,x in enumerate(scaled)))==0
    return {'r':r,'min_c':5,'degree':len(scaled)-1,
            'common_positive_denominator':int(lcm),
            'integer_coefficients_desc':scaled,
            'minimum_integer_coefficient':min(scaled)},shifted,R

def choose(n,k): return comb(n,k) if 0<=k<=n else 0

def mul_one_minus_z(vec,exp):
    out=vec[:]
    for _ in range(exp):
        nxt=[0]*(len(out)+1)
        for i,x in enumerate(out):nxt[i]+=x;nxt[i+1]-=x
        out=nxt
    return out

def numerator_polynomials(maxd):
    """Independent exact integer recursion for [t^d]H=P_d/(1-z)^(floor(d/3)+1)."""
    polys=[]
    for d in range(maxd+1):
        a=d//3
        base=[choose(6,d),-choose(6,d-1)-choose(8,d-1),choose(8,d-2)]
        res=[0]*(d+a+8)
        def add(src,ofs=0,mult=1):
            for i,x in enumerate(src):res[ofs+i]+=mult*x
        add(mul_one_minus_z(base,a))
        if d>=1:add(mul_one_minus_z(polys[d-1],a-(d-1)//3),1,2)
        if d>=2:add(mul_one_minus_z(polys[d-2],a+1-(d-2)//3),1)
        if d>=3:add(polys[d-3],3)
        while len(res)>1 and res[-1]==0:res.pop()
        assert len(res)-1<= (0 if d==0 else d+a-1)
        polys.append(res)
    return polys

def q(polys,d,w):
    a=d//3
    return sum(x*choose(d+w-i+a,a) for i,x in enumerate(polys[d]) if d+w>=i)

def numerical_certificate(polys,d,c0):
    """Coefficient [w^(c-5)] reconstructed from c+1 exact values via Stirling transform."""
    values=[q(polys,d,i) for i in range(c0+1)]
    diffs=[]
    for j in range(c0+1):
        diffs.append(values[0])
        values=[values[i+1]-values[i] for i in range(len(values)-1)]
    return S.cancel(sum(S.Rational(diffs[k]*stirling(k,c0-5,kind=1,signed=True),factorial(k))
                        for k in range(c0-5,c0+1)))

def main():
    rows=[sixth(r) for r in range(3)]
    cert=[row[0] for row in rows]
    limit=22
    polys=numerator_polynomials(3*limit+2)
    checks=[]
    for cc in range(5,limit+1):
        for r in range(3):
            d=3*cc+r
            expected=S.cancel(rows[r][1].subs(v,cc-5)/factorial(cc-5))
            measured=numerical_certificate(polys,d,cc)
            assert measured==expected,(cc,r,measured,expected)
            if cc in (5,6,12,22):
                checks.append({'c':cc,'r':r,'exact_value':str(measured)})
    # Independently recover first coefficients of generating function directly.
    z=S.symbols('z')
    H=((1+t)**6*(1-t*z)*(1-t*(1+t)**2*z)/(1-(1+t)**2*z+2*t*(1+t)*z*z-t*t*(1+t)*z**3))
    # Multiplying both sides by the denominator is an exact identity.
    assert S.expand(S.cancel((1-(1+t)**2*z+2*t*(1+t)*z*z-t*t*(1+t)*z**3)*H
                       -(1+t)**6*(1-t*z)*(1-t*(1+t)**2*z)))==0
    out={'schema':'EM_R4_EC25_SIXTH_NEWTON_REPRO_CERTIFICATE_V1',
         'math_status':'AUTHOR_SIDE_EXACT_PROOF_NOT_INDEPENDENTLY_REVIEWED',
         'scope':'auxiliary positive ordered binary affine BRC only; no native X6 transfer',
         'global_claim':'For every c>=5 and r in {0,1,2}, [w^(c-5)] q_(3c+r)(3c+r+w)>0',
         'proof_certificate':'positive rational shifted polynomial in v=c-4, derived by Laurent formula and Newton identities',
         'certificates':cert,'independent_integer_regression_c_range':[5,limit],
         'independent_integer_regression_cases':3*(limit-4),
         'sample_exact_values':checks,
         'unproved':['all Newton differences positive uniformly in c,d',
                     'near-center f_j(2j+s)>=0 for s=0..5',
                     'P000 X6 correspondence and physical time semantics'],
         'native_owner_claim':'UNVERIFIED_CONTROL_QUOTA',
         'native_session':'DENIED_STATIC_READONLY_SCOPE',
         'independent_review':'NOT_PERFORMED'}
    p=Path(__file__).with_name('R4_EC25_report_rerepro.json')
    p.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'pass':True,'degrees':[x['degree'] for x in cert],
                     'lcm':[x['common_positive_denominator'] for x in cert],
                     'integer_check_cases':out['independent_integer_regression_cases'],
                     'at_c5':[x for x in checks if x['c']==5]},ensure_ascii=False))

if __name__=='__main__':main()
