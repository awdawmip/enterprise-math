#!/usr/bin/env python3
"""R326 exact polynomial certificate for BRC Newton triangle, fixed q=0..64.
SymPy is used only for exact integer/rational polynomial arithmetic.
No floating-point sign decision. Run: python R326_verify_uniform_strips64.py
"""
import hashlib
import json
from math import comb
import sympy as S

LIMIT_Q=64
x,t,u=S.symbols('x t u')
def C(n,k):return comb(n,k) if 0<=k<=n else 0

def kernel(i):
    d=(-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),
       C(7,i-2),-C(9,i-3))
    return S.Poly(S.expand(-sum(v*t**(i-1)*(1+t)**(i+1-j)
        for j,v in enumerate(d,1) if v)),t)

def source(row):
    if row>10:return S.Poly(0,t)
    return S.Poly(S.expand(sum(v*t**row*(1+t)**power for v,power in
        ((-C(3,row-1),row),(-C(6,row-1),row-1),
         (C(8,row-2),row-2)) if v)),t)
K=[None]+[kernel(i) for i in range(1,13)]
assert K[1].as_expr()==2+3*t
assert K[2].as_expr()==-t+4*t**2+4*t**3
H=[S.Poly(0,x) for _ in range(LIMIT_Q+1)]
for i in range(1,13):
    for (j,),v in K[i].terms():
        if j<=LIMIT_Q:H[j]+=S.Poly(v*x**i,x)
assert H[0].as_expr()==2*x
A=[S.Poly(0,x) for _ in range(LIMIT_Q+1)]
A[0]=S.Poly(1,x);A[1]=S.Poly(1,x)
for row in range(1,11):
    for (j,),v in source(row).terms():
        if j<=LIMIT_Q:A[j]+=S.Poly(v*x**row,x)
D=S.Poly(1-2*x,x)
P=[S.Poly(1,x)]
checksum=hashlib.sha256()
positive_coeffs=0
# q=0 shifted polynomial is 1.
checksum.update(b'0|1\n');positive_coeffs+=1
record_q13={}
for q in range(1,LIMIT_Q+1):
    num=A[q]*D**q
    for j in range(1,q+1):num+=H[j]*P[q-j]*D**(j-1)
    assert num.degree()<=2*q
    P.append(num)
    # Phi_q(q+u)=sum_{j=0}^{2q} p_j 2^{-j} binom(2q+u-j,q).
    shifted=S.Poly(0,u,domain=S.QQ)
    factorial=S.factorial(q)
    for (j,),v in num.terms():
        f=S.Poly(1,u,domain=S.QQ)
        for r in range(q):f*=S.Poly(u+2*q-j-r,u)
        shifted+=f*S.Rational(v,2**j*factorial)
    coefficients=[shifted.nth(j) for j in range(q+1)]
    assert all(c>0 for c in coefficients),q
    positive_coeffs+=len(coefficients)
    checksum.update((str(q)+'|'+','.join(str(v) for v in coefficients)+'\n').encode('ascii'))
    if q==13:
        den=S.ilcm(*[v.q for v in coefficients]);nums=[int(v*den) for v in coefficients]
        assert den==16715531679694848
        assert nums==[600063448538865991680,855370013229105827328,
         535089264741495831744,194904160247200340976,
         46629308507865187104,7844915168393714840,
         967888364674159500,89737993157044375,6313449831975000,
         335205873234375,13105279687500,357586328125,6093750000,48828125]
        record_q13={'denominator':str(den),'ascending_numerator':[str(v) for v in nums],
                    'boundary_coefficient':'294080970'}

# Independent original-in-t recurrence cross-check of the q=13 diagonal to row 192.
B={0:S.Poly(1+t,t)}
checks=0
s=S.symbols('s')
q=13
phi=S.Poly(0,s,domain=S.QQ)
for (j,),v in P[q].terms():
    phi+=S.Poly(S.Rational(v,2**j*S.factorial(q))*
                   S.prod(s-j+k for k in range(1,q+1)),s,domain=S.QQ)
for row in range(1,193):
    v=source(row)
    for i in range(1,min(row,12)+1):v+=K[i]*B[row-i]
    B[row]=v
    if row>=q:
        assert v.nth(q)==2**row*phi.eval(row) and v.nth(q)>0
        checks+=1
    if row>12:del B[row-12]
assert checks==180
print(json.dumps({'status':'PASS',
 'structural_theorem':'for each q>=0, F_q=P_q/(1-2x)^(q+1), integer P_q with degree<=2q',
 'finite_symbolic_q_range':[0,LIMIT_Q],
 'strictly_positive_shift_coefficients':positive_coeffs,
 'valid_unbounded_region':'all integers 0<=q<=64 and s>=q',
 'certificate_sha256':checksum.hexdigest(),
 'q13_certificate':record_q13,
 'independent_in_t_recurrence_q13_range':[13,192],
 'independent_comparisons':checks,
 'arithmetic':'exact rational and integer; no floating-point signs',
 'review_status':'AUTHOR_COMPUTER_ASSISTED_NOT_DRIVER_ADMITTED'},ensure_ascii=False,indent=2))
