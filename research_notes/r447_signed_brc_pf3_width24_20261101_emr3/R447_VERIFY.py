#!/usr/bin/env python3
"""R447: exact common-denominator certificate for signed-BRC scalar Toeplitz PF3.

This is an author-side computer-assisted finite-width lemma, not native X6 dynamics.
Requires Python 3.10+ and SymPy; no floating-point decisions.
"""
import hashlib
import json
from itertools import combinations
from math import comb
from pathlib import Path
import sympy as sp

R_LOWER = 99
L = 24
r = sp.Symbol('r')


def falling(x, n):
    value = sp.Integer(1)
    for k in range(n):
        value *= x-k
    return value


def rho(h):
    """Exact ratio H(r,r-h)/Catalan(r); valid at all odd r>=99, h<=24."""
    terms = sum(
        sp.binomial(h,q) * falling(r,2*q) * falling(r,2*h-2*q)
        * (4*q-2*h+1) / (r-2*h+2*q+1)
        for q in range(h+1)
    )
    return sp.cancel(
        (r+1)*falling(2*r-h,h)*terms
        / (sp.factorial(h)*falling(2*r,2*h))
    )


def original_H(R,h):
    """Independent signed convolution at fixed odd R."""
    def c(n,k):
        return comb(n,k) if 0 <= k <= n else 0
    s=R-h
    return c(R+s,2*s)*sum(
        c(h,q)*(c(2*s,R-2*q)-c(2*s,R-2*q-1))
        for q in range(h+1)
    )


def shifted_coefficients(P,lower):
    """Evaluate P(lower+u) exactly, ascending integral coefficients."""
    a=[int(z) for z in reversed(P.all_coeffs())]
    return [sum(a[j]*comb(j,i)*lower**(j-i) for j in range(i,len(a)))
            for i in range(len(a))]


def multiply(a,b):
    if not a or not b: return []
    result=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b): result[i+j]+=x*y
    return result


def plus(*terms):
    N=max(map(len,terms))
    return [sum(t[i] if i<len(t) else 0 for t in terms) for i in range(N)]


def opposite(a): return [-z for z in a]


def determinant_coefs(cols,qa,pair_cache):
    m=len(cols)
    if m==1: return qa[cols[0]]
    def pair(a,b):
        if a<0 or b<0: return []
        key=tuple(sorted((a,b)))
        if key not in pair_cache:
            pair_cache[key]=multiply(qa[key[0]],qa[key[1]])
        return pair_cache[key]
    if m==2:
        a,b=cols
        return plus(pair(a,b-1),opposite(pair(b,a-1)))
    a,b,c=cols
    def tri(x,y,z):
        return multiply(pair(x,y),qa[z]) if min(x,y,z)>=0 else []
    return plus(
        tri(a,b-1,c-2),tri(b,c-1,a-2),tri(c,a-1,b-2),
        opposite(tri(c,b-1,a-2)),opposite(tri(b,a-1,c-2)),
        opposite(tri(a,c-1,b-2))
    )


def numeric_det(vals,cols):
    m=len(cols)
    at=lambda row,j: vals[j-row] if j>=row else 0
    if m==1:return at(0,cols[0])
    if m==2:
        a,b=cols
        return at(0,a)*at(1,b)-at(0,b)*at(1,a)
    a,b,c=cols
    return (at(0,a)*at(1,b)*at(2,c)+at(0,b)*at(1,c)*at(2,a)
            +at(0,c)*at(1,a)*at(2,b)-at(0,c)*at(1,b)*at(2,a)
            -at(0,b)*at(1,a)*at(2,c)-at(0,a)*at(1,c)*at(2,b))


def main():
    ratios=[rho(h) for h in range(L+1)]
    fractions=[]
    common=sp.Poly(1,r,domain=sp.QQ)
    for ratio in ratios:
        nu,de=sp.fraction(ratio)
        num,den=sp.Poly(nu,r,domain=sp.QQ),sp.Poly(de,r,domain=sp.QQ)
        common=sp.lcm(common,den)
        fractions.append((num,den))
    if common.eval(R_LOWER)<0: common=-common
    numerators=[sp.Poly(sp.cancel(num.as_expr()*common.as_expr()/den.as_expr()),r,domain=sp.QQ)
                for num,den in fractions]
    scale=sp.ilcm(*[int(c.q) for p in [common]+numerators for c in p.all_coeffs()])
    den=common*scale
    q_polys=[p*scale for p in numerators]
    assert all(z.q==1 for p in [den]+q_polys for z in p.all_coeffs())
    assert all(sp.cancel(q.as_expr()/den.as_expr()-target)==0
               for q,target in zip(q_polys,ratios))
    da=shifted_coefficients(den,R_LOWER)
    assert all(c>0 for c in da)
    qa=[shifted_coefficients(p,R_LOWER) for p in q_polys]
    # Independently reconstruct signed raw BRC coefficients, not only rational functions.
    raw={}
    checks=0
    for R in (99,343):
        C=comb(2*R,R)//(R+1)
        values=[original_H(R,h) for h in range(L+1)]
        for h,value in enumerate(values):
            assert sp.Rational(value,C)==ratios[h].subs(r,R), (R,h)
            checks+=1
        raw[R]=values
    # Every coefficient strictly positive is a certificate for all u=r-99>=0.
    grouped={}; pair_cache={}; bad=[]
    serialized=hashlib.sha256()
    maxdeg=0
    numeric_checks={R:0 for R in raw}
    for m in (1,2,3):
        grouped[m]=0
        for columns in combinations(range(L+1),m):
            coeff=determinant_coefs(columns,qa,pair_cache)
            if not coeff or not all(z>0 for z in coeff):
                bad.append({'order':m,'columns':columns})
            maxdeg=max(maxdeg,len(coeff)-1)
            serialized.update(json.dumps([m,columns,list(map(str,coeff))],separators=(',',':')).encode()+b'\n')
            # Independent direct raw convolution and integer Leibniz determinant check.
            for R,values in raw.items():
                actual=numeric_det(values,columns)
                assert actual>0,(R,m,columns,actual)
                # det Q = (D / C)^m * det H; exact integer identity
                Dv=int(den.eval(R));Cv=comb(2*R,R)//(R+1)
                poly_value=sum(x*(R-R_LOWER)**i for i,x in enumerate(coeff))
                assert poly_value*Cv**m==actual*Dv**m,(R,m,columns)
                numeric_checks[R]+=1
            grouped[m]+=1
    assert not bad,bad[:10]
    assert grouped=={1:25,2:300,3:2300}
    summary={
        'schema':'R447_SIGNED_BRC_PF3_WIDTH24_EXACT_CERTIFICATE_V1',
        'scope':'odd integer r>=99, signed BRC auxiliary scalar Toeplitz only',
        'width':L,'lower_r':R_LOWER,
        'certificate_method':'all coefficients of D(99+u) and every det[Q_(j-i)(99+u)] strictly positive integers',
        'common_denominator_degree':den.degree(),
        'denominator_shift_coefficients_positive':True,
        'orders_checked':grouped,'total':sum(grouped.values()),
        'raw_signed_convolution_identity_checks':checks,
        'direct_exact_determinants':numeric_checks,
        'max_certificate_numerator_degree':maxdeg,
        'unverified_claims':['uniform width proportional to r','whole half-infinite PF3','native X6 transfer'],
        'all_coefficient_checks_passed':True,
        'full_coefficient_stream_sha256':serialized.hexdigest(),
        'status':'AUTHOR_SIDE_EXACT_SYMBOLIC; UNREVIEWED; NOT_ADMITTED',
    }
    path=Path(__file__).with_name('R447_EVIDENCE.json')
    path.write_text(json.dumps(summary,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('R447_PASS',json.dumps(summary,sort_keys=True,ensure_ascii=False))


if __name__=='__main__':main()
