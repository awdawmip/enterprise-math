#!/usr/bin/env python3
"""R449 exact symbolic certificates for signed BRC Poisson-edge expansions.

Uses exact rational polynomial algebra; no floating point and no external data.
Symbolic coefficient identities hold for an indeterminate h, not a list of h samples.
"""
import json
from itertools import combinations
from math import comb, factorial, prod
from pathlib import Path
import sympy as sp

h, q = sp.symbols('h q', integer=True, nonnegative=True)

def S1(n):
    return n*(n-1)/2

def S2(n):
    return n*(n-1)*(2*n-1)/6

# Coefficients of log F_hq(1/x)=U*x+V*x*x+O_h(x**3),
# from the exact R448 factorial product F_hq.
U = sp.expand(2*(h-q) - (h*h+S1(h))/2
              -S1(2*q)-S1(2*h-2*q)+S1(2*h)/2)
V = sp.expand((sp.expand((1-2*h+2*q)**2)-1)/2
              -(h**3+2*h*S1(h)+S2(h))/8
              -(S2(2*q)+S2(2*h-2*q))/2+S2(2*h)/8)
F2 = sp.expand(V+U**2/2)

def binomial_mean(poly):
    # E[Q**k] = sum_{j=0}^k S(k,j)*(h)_j/2**j for Q~Binomial(h,1/2).
    P = sp.Poly(sp.expand(poly), q)
    def moment(k):
        return sum(sp.functions.combinatorial.numbers.stirling(k, j, kind=2)
                   * sp.prod(h-i for i in range(j))/2**j
                   for j in range(k+1))
    return sp.factor(sum(c*moment(power[0]) for power,c in P.terms()))

W = 4*q-2*h+1
A = sp.factor(binomial_mean(W*U))
B = sp.factor(binomial_mean(W*F2))
A_expected = -h*(3*h+5)/4
B_expected = h*(h-1)*(27*h*h+89*h+254)/96
assert sp.simplify(A-A_expected)==0
assert sp.simplify(B-B_expected)==0

def signed_h(r,k):
    s=r-k
    def bc(n,a):return comb(n,a) if 0<=a<=n else 0
    return bc(r+s,2*s)*sum(bc(k,j)*(bc(2*s,r-2*j)-bc(2*s,r-2*j-1))
                         for j in range(k+1))

def falling(n,k):return prod(n-i for i in range(k))

def rho_r448(r,k):
    if k==0:return sp.Rational(1)
    summand = sum(sp.Rational(comb(k,j)*falling(r,2*j)*falling(r,2*k-2*j)
                   *(4*j-2*k+1),r-2*k+2*j+1) for j in range(k+1))
    return sp.Rational((r+1)*falling(2*r-k,k),
                       factorial(k)*falling(2*r,2*k))*summand

# Independent fixed-h Laurent/Taylor extraction from the exact rational rho formula.
# This bypasses the log-F/binomial-moment coefficient derivation.
R, x = sp.symbols('R x', positive=True)
fixed_h_series_checks=0
for k in range(0,8):
    if k==0:
        e=sp.Integer(1)
    else:
        total=sum(sp.binomial(k,j)*sp.prod(R-i for i in range(2*j))
                  *sp.prod(R-i for i in range(2*k-2*j))
                  *(4*j-2*k+1)/(R-2*k+2*j+1) for j in range(k+1))
        e=sp.cancel((R+1)*sp.prod(2*R-k-i for i in range(k))
                    /sp.prod(2*R-i for i in range(2*k))
                    *total/R**k)
    terms=sp.series(e.subs(R,1/x),x,0,3).removeO().expand()
    assert sp.simplify(terms-(1+A_expected.subs(h,k)*x+B_expected.subs(h,k)*x*x))==0,k
    fixed_h_series_checks+=1

checks=0
for r in [19,43,101,343]:
    c=comb(2*r,r)//(r+1)
    for k in range(0,min(8,(r-2)//2)+1):
        assert sp.Rational(signed_h(r,k),c)==rho_r448(r,k)
        checks+=1

def a_int(n):return sp.Rational(-n*(3*n+5),4)

def Vdet(js):return prod(js[j]-js[i] for i in range(len(js)) for j in range(i+1,len(js)))

minor_checks=0
for m in range(1,6):
    for js in combinations(range(9),m):
        # D'(0) = sum_i det with row i replaced by (j)_i*a(j-i).
        v=sp.Integer(Vdet(js))
        P=sp.Matrix([[falling(j,i) for j in js] for i in range(m)])
        assert P.det()==v
        D1=sp.Integer(0)
        for i in range(m):
            P1=P.copy()
            for c,j in enumerate(js):
                P1[i,c]=falling(j,i)*a_int(j-i)
            D1+=P1.det()
        LAMBDA=-3*sum(j*j for j in js)+(6*m-11)*sum(js)+m*(m-1)*(5-2*m)
        assert sp.simplify(D1/v-sp.Rational(LAMBDA,4))==0,(m,js)
        minor_checks+=1

evidence={
 'schema':'R449_SIGNED_BRC_POISSON_EDGE_SECOND_ORDER_EXACT_V1',
 'provenance':'R448 original signed convolution; symbolic h is an indeterminate',
 'c1':str(A), 'c2':str(B),
 'c1_identity_for_all_h':True,'c2_identity_for_all_h':True,
 'toeplitz_first_order':'[-3 sum(j_v^2)+(6m-11)sum(j_v)+m(m-1)*(5-2m)]/4',
 'numeric_original_convolution_exact_checks':checks,
 'independent_exact_fixed_h_series_checks':fixed_h_series_checks,
 'minor_first_order_integer_column_checks':minor_checks,
 'minor_orders_checked':[1,2,3,4,5],
 'scope':'fixed integer h and fixed columns as r goes to infinity; no uniformity in growing j',
 'status':'AUTHOR_SIDE_EXACT_SYMBOLIC; UNREVIEWED; NOT_ADMITTED',
}
Path(__file__).with_name('R449_EVIDENCE.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print('R449_PASS '+json.dumps(evidence,ensure_ascii=False,sort_keys=True))
