#!/usr/bin/env python3
"""R550: Exact cyclotomic-ratio exclusion for frozen-R462 signed BRC, k=5,6,7.

Requires Python 3.10+ and SymPy. All mathematical assertions use exact integers/rationals.
R543--R545's exact Rouché certificates are separate dependencies for the
unique dominant nonreal conjugate pair; this code proves the NEW angle claim.
"""
from fractions import Fraction
from math import comb
from sympy import Poly, Rational, Symbol, resultant, gcd, cyclotomic_poly, totient, Matrix

x, u = Symbol('x'), Symbol('u')

def cat(j):
    return comb(2*j,j)//(j+1)

def choose(n,j):
    return comb(n,j) if 0<=j<=n else 0

def H(k,t):
    r=2*k+1
    if not 2<=t<=r:
        return 0
    return comb(r+t,2*t)*sum(comb(t-1,2*q)*4**q*cat(k-q)
                   for q in range(min((t-1)//2,k)+1))

def H_raw(k,t):
    r=2*k+1
    if not 2<=t<=r:
        return 0
    return comb(r+t,2*t)*sum(comb(r-t,h)*(choose(2*t,r-2*h)-choose(2*t,r-2*h-1))
                              for h in range(r-t+1))

def charpoly(k):
    d=2*k-1
    p={t:Fraction(H(k,t),cat(k)) for t in range(2,2*k+2)}
    a=[(-1)**(j-1)*p[j+2]/p[2] for j in range(1,d+1)]
    Q=Poly(x**d-sum(Rational(v.numerator,v.denominator)*x**(d-j)
                    for j,v in enumerate(a,1)),x)
    return Q,a

def check_original(k,a):
    r=2*k+1
    assert all(H(k,t)==H_raw(k,t) for t in range(2,r+1))
    # The original matrix uses H(3+i-j), not the normalized characteristic Q.
    f=[Fraction(1)]
    for m in range(1,8):
        # actual Hessenberg coefficients for D_m / Catalan(k)^m
        orig=[(-1)**(j-1)*Fraction(H(k,j+2),cat(k))*Fraction(H(k,2),cat(k))**(j-1)
              for j in range(1,2*k)]
        f.append(sum(orig[j-1]*f[m-j] for j in range(1,min(m,len(orig))+1)))
        mat=Matrix([[H_raw(k,3+i-j) for j in range(m)] for i in range(m)])
        assert mat.det(method='berkowitz')==f[m]*cat(k)**m,(k,m)
    return r-1, 7

def ratio_polynomial(Q):
    n=Q.degree()
    # E(u)=Res_x(Q(x),u^n*Q(x/u)) = prod_ij(lambda_i-u*lambda_j).
    # Each i=j term contributes (1-u), exactly n trivial root-ratios.
    E=Poly(resultant(Q.as_expr(),u**n*Q.as_expr().subs(x,x/u),x),u)
    assert E.degree()==n*n and Q.eval(0)!=0
    R=E.exquo(Poly((u-1)**n,u))
    assert R.degree()==n*(n-1) and R.eval(1)!=0
    return R

def certify(k):
    Q,a=charpoly(k)
    raw_coeff, raw_det=check_original(k,a)
    R=ratio_polynomial(Q)
    D=R.degree()
    # Elementary universal bound phi(q)>=sqrt(q/2); hence phi(q)<=D => q<=2D^2.
    bound=2*D*D
    checked=[]
    for q in range(2,bound+1):
        if int(totient(q))>D:
            continue
        phi=Poly(cyclotomic_poly(q,u),u)
        assert gcd(R,phi).degree()==0,('ratio-root-of-unity',k,q)
        checked.append(q)
    print('k=%d degree_Q=%d degree_R=%d order_bound=%d candidates=%d largest_candidate=%d raw_H=%d raw_det=%d' %
          (k,Q.degree(),D,bound,len(checked),max(checked),raw_coeff,raw_det))
    print(' k=%d constant_Q=%s R_at_1_nonzero=%s no_cyclotomic_factors=YES' %
          (k,str(Q.eval(0)),R.eval(1)!=0))
    return len(checked)

if __name__=='__main__':
    counts=[certify(k) for k in (5,6,7)]
    assert counts==[147,215,300],counts
    print('R550_EXACT_HALF_DENSITY_CERT_PASS')
