#!/usr/bin/env python3
"""R4-EC20 author-side exact proof certificate: 15 highest Newton diagonals.

Scope: positive ordered binary affine auxiliary BRC palindromic kernel E.
SymPy symbolic rational manipulation + exact integer independent recurrence.
This is not a formal proof checker or native X6 implementation.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as s

D_MAX=14
J_DIRECT=48
J_HIGH=1024
z,t,j,w=s.symbols('z t j w')
Q=(1-z, -2*z+2*z**2, -z+2*z**2-z**3, -z**3)
N=s.Poly(s.expand((1+t)**6*(1-t*z)*(1-t*z*(1+t)**2)),t)

def h_diagonals():
    hs=[]; results=[]
    for d in range(D_MAX+1):
        rhs=N.nth(d)
        for k in (1,2,3):
            if d>=k: rhs -= Q[k]*hs[d-k]
        h=s.cancel(rhs/Q[0]);hs.append(h)
        numerator,denominator=map(lambda a:s.Poly(a,z),s.fraction(h))
        pole=denominator.degree(); sign=int(denominator.eval(0))
        assert s.expand(denominator.as_expr()-sign*(1-z)**pole)==0
        # For j>=d, coeff_[z^j] numerator/(1-z)^pole equals
        # sum_k numerator[k] * (j-k+1)...(j-k+pole-1)/(pole-1)!.
        exact=s.factor(sum((coeff/sign)*s.prod(j-k+l for l in range(1,pole))
             /s.factorial(pole-1) for (k,),coeff in numerator.terms()))
        shifted=s.Poly(s.expand(exact.subs(j,w+d)),w)
        nonnegative_coeff=[str(shifted.nth(k)) for k in range(shifted.degree()+1)]
        assert all(shifted.nth(k)>0 for k in range(shifted.degree()+1)),(d,shifted)
        # Check polynomial-coefficient convention at the threshold, where
        # the highest numerator degree is just beyond the coefficient index.
        for n in (d,d+1,d+2):
            assert s.simplify(s.series(h,z,0,n+1).removeO().expand().coeff(z,n)-exact.subs(j,n))==0
        results.append({"d":d,"pole_order":pole,"numerator_degree":numerator.degree(),
                        "closed_polynomial_in_j":str(exact),"polynomial_in_w_j_minus_d":str(shifted.as_expr()),
                        "positive_monomial_coefficients_ascending":nonnegative_coeff})
    return results

def e_rows(limit):
    rows=[]
    for n in range(limit+1):
        row=[0]*(n+1)
        if n==0:row[0]=1
        if n>=1:
            for k,c in enumerate(rows[n-1]):row[k]+=c;row[k+1]+=c
        if n>=4:
            for k,c in enumerate(rows[n-4]):row[k+2]-=2*c
        if n>=6:
            for k,c in enumerate(rows[n-6]):row[k+3]+=c
        if n==2:row[1]-=1
        rows.append(row)
    return rows

def difference(sequence,order):
    vals=sequence[:]
    for _ in range(order):vals=[b-a for a,b in zip(vals,vals[1:])]
    return vals[0]

def truncated_arithmetic_checks(formulae):
    # Reuses EC19's exact depth-direction recurrence; numeric code copied
    # from that trusted mathematical definition for stand-alone portability.
    rows=e_rows(3*J_DIRECT+6)
    direct=0
    for grade in range(1,J_DIRECT+1):
        b=2*grade+6
        samples=[rows[b+i][grade]-rows[b+i][grade-1] for i in range(grade+1)]
        for d in range(min(D_MAX,grade)+1):
            actual=difference(samples,grade-d)
            expected=int(s.sympify(formulae[d]["closed_polynomial_in_j"],locals={'j':j}).subs(j,grade))
            assert actual==expected and actual>0,(grade,d,actual,expected)
            direct+=1
    # Completely different *grade-direction* recurrence for the low t-part
    # of H_j(t)=(1+t)^6(X_j-t(1+t)^2 X_(j-1)).
    cutoff=D_MAX
    def poly_add(*poly):return [sum(p[k] if k<len(p) else 0 for p in poly) for k in range(cutoff+1)]
    def poly_mul(a,b):
        out=[0]*(cutoff+1)
        for r,v in enumerate(a):
            if r>cutoff:break
            for q,u in enumerate(b[:cutoff+1-r]):out[r+q]+=v*u
        return out
    const=lambda coeff:coeff+[0]*(cutoff+1-len(coeff))
    a=const([1,2,1]); minus2=const([0,-2,-2]);plus3=const([0,0,1,1]);
    one_t6=[int(s.binomial(6,k)) if k<=6 else 0 for k in range(cutoff+1)]
    x0=const([1]); x1=const([1,1,1]); previous=[x0,x1]
    high=0
    for grade in range(1,J_HIGH+1):
        if grade>=2:
            value=poly_add(poly_mul(a,previous[-1]),poly_mul(minus2,previous[-2]),
                           poly_mul(plus3,previous[-3]) if grade>=3 else const([0]))
            previous.append(value)
            if len(previous)>3:previous.pop(0)
        xcurrent=previous[-1]; xprev=previous[-2]
        ta=poly_mul(const([0,1]),a)
        h=poly_mul(one_t6,poly_add(xcurrent,[-v for v in poly_mul(ta,xprev)]))
        for d in range(min(D_MAX,grade)+1):
            expected=int(s.sympify(formulae[d]["closed_polynomial_in_j"],locals={'j':j}).subs(j,grade))
            assert h[d]==expected and h[d]>0,(grade,d,h[d],expected)
            high+=1
    return direct,high

if __name__=='__main__':
    data=h_diagonals()
    direct,high=truncated_arithmetic_checks(data)
    report={
     "schema":"EM_R4_EC20_TOP15_NEWTON_CERTIFICATE_V1",
     "theorem":"For every integer j>=1 and 0<=d<=min(14,j), Delta^(j-d) f_j(2j+6)>0",
     "model":"E(x,u)=(1-u*x^2)/(1-(1+u)*x+2*u^2*x^4-u^3*x^6), f_j(n)=E[n,j]-E[n,j-1]",
     "proof":"For each d<=14, rational H_d(z) and exact shifted-polynomial formula with every monomial coefficient positive for j>=d. Transform identity is formal and all-depth.",
     "gf_in_grade_and_shift":"sum_j H_j(t) z^j=(1+t)^6*(1-t*z)*(1-t*(1+t)^2*z)/[1-(1+t)^2*z+2*t*(1+t)*z^2-t^2*(1+t)*z^3]",
     "d_max":D_MAX,"direct_depth_recurrence_checked_j":J_DIRECT,"direct_newton_checks":direct,
     "independent_truncated_grade_checked_j":J_HIGH,"high_grade_checks":high,
     "arithmetic":"sympy exact rational coefficient identity and Python arbitrary precision integers",
     "mathematics_status":"AUTHOR_DERIVATION_WITH_SYMBOLIC_CERTIFICATE_UNREVIEWED",
     "native_X6":"NOT_RUN","full_grade_unimodality":"OPEN",
     "diagonals":data
    }
    output=Path(__file__).with_name('R4_EC20_REPORT.json')
    output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='diagonals'},indent=2))
