#!/usr/bin/env python3
"""Exact residual Y,Y,Ri,Rj 4th cumulant matrix from published PREFIX581 full
126-coefficient original native X6 gate polynomial. Rational SymPy only.
This is a derived observer contraction, not another native kernel evaluation.
"""
import json
from pathlib import Path
import sympy as sp

here=Path(__file__).resolve().parent
data=json.loads((here/'PREFIX581_R2_exact_monomial_certificate.json').read_text())
assert len(data['coefficients'])==126
y=sp.symbols('y1:7')
a=sp.symbols('a1:7')
b=sp.symbols('b')
P=sp.Add(*(sp.Rational(v)*sp.prod(q**int(k) for q,k in zip(y,key.split('/')))
           for key,v in data['coefficients'].items()))
assert len(sp.Poly(P,*y).terms())==126
# Native deterministic edge identity R1+...+R6=d, no deletion of native axis 6.
G=P.subs(dict(zip(y,[a[i]-a[5] for i in range(5)]+[b])),simultaneous=True)
residual=[sp.Rational(-3,64),sp.Rational(-1,64),sp.Rational(-3,64),
          sp.Rational(-1,64),sp.Integer(0),sp.Integer(0)]
at={a[i]:residual[i] for i in range(6)}
at[b]=sp.Integer(1)
# Quartic polarization D^2 F /12 = Cum(v,v,e_i,e_j), D F/4 = Cum(v,v,v,e_i).
B=sp.Matrix(6,6,lambda i,j:sp.diff(G,a[i],a[j]).subs(at)/12)
C=sp.Matrix([sp.diff(G,a[i]).subs(at)/4 for i in range(6)])
assert B==B.T and B*sp.ones(6,1)==sp.zeros(6,1)
assert B.rank()==5 and B.nullspace()==[sp.ones(6,1)]
den=sp.ilcm(*[q.q for q in B]); N=B*den
assert den==3057647616
EXPECTED_N=[
[-864041,223411,1754386,-769250,-172253,-172253],
[223411,187015,-769250,352114,3355,3355],
[1754386,-769250,-864041,223411,-172253,-172253],
[-769250,352114,223411,187015,3355,3355],
[-172253,3355,-172253,3355,695830,-358034],
[-172253,3355,-172253,3355,-358034,695830]]
assert N==sp.Matrix(EXPECTED_N)
assert N[:5,:5].det()==-53061477936613189085277978624
minors=[B[:k,:k].det() for k in range(1,6)]
assert all(x<0 for x in minors)
signs=[sp.sign(minors[k]/(minors[k-1] if k else 1)) for k in range(5)]
assert list(signs)==[-1,1,1,1,1]
cubic=[sp.Rational(208423,150994944),sp.Rational(-127301,150994944),
       sp.Rational(208423,150994944),sp.Rational(-127301,150994944),
       sp.Rational(-40561,75497472),sp.Rational(-40561,75497472)]
assert list(C)==cubic and sum(C)==0
out={
 'schema':'ENTERPRISE_MATH_PREFIX582_NATIVE_RESIDUAL_YY_SIXAXIS_QUARTIC_V1',
 'source':'PREFIX581_R2_exact_monomial_certificate.json, original frozen X6 BRC',
 'frozen_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'residual':'Y=K-(3R1+R2+3R3+R4)/64+d/48',
 'B_RiRj_Y_Y':[[str(q) for q in row] for row in B.tolist()],
 'B_denominator':str(den),
 'B_numerator':EXPECTED_N,
 'B_rank':B.rank(),
 'B_kernel':['1','1','1','1','1','1'],
 'B_inertia':{'positive':4,'negative':1,'zero':1},
 'B_principal_minor_5x5_numerator_det':str(N[:5,:5].det()),
 'B_leading_rational_minors':[str(m) for m in minors],
 'B_LDL_pivot_signs':[int(s) for s in signs],
 'cubic_YYY_Ri':[str(q) for q in C],
 'verification':'AUTHOR_SIDE_EXACT_ALGEBRA_ALL_ASSERTIONS_PASS',
 'independent_review':'PENDING'
}
(here/'PREFIX582_R2_residual_YY_sixaxis_certificate.json').write_text(
 json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('ALL_ASSERTIONS_PASS rank=5 inertia=(4+,1-,1zero)')
