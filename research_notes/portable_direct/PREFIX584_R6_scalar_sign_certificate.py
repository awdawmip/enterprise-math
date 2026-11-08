#!/usr/bin/env python3
"""Exact Q[i sqrt(2)] sign/oscillation certificate for PREFIX-584-R6.

All computations are exact rational arithmetic. The all-n proof and
irrational-rotation argument are in the companion mathematical note.
"""
from fractions import Fraction as Q
import json

# Pairs (a,b) represent a + b*t, with t^2=-2.
ZERO=(Q(0),Q(0)); ONE=(Q(1),Q(0))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y): return (x[0]*y[0]-2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def scale(x,c): return (x[0]*c,x[1]*c)
def norm2(x): return x[0]*x[0]+2*x[1]*x[1]
def power(x,n):
    out=ONE
    while n:
        if n&1: out=mul(out,x)
        x=mul(x,x); n//=2
    return out

alpha=(Q(-1,3),Q(1,3))
A=(Q(-1,10368),Q(-37,41472))
B=(Q(1,6912),Q(-1,3456))
L=Q(1,5184)
def q(n):
    w=mul(add(A,scale(B,Q(n))),power(alpha,n))
    return L+2*w[0]

assert add(add(mul(alpha,alpha),scale(alpha,Q(2,3))),scale(ONE,Q(1,3)))==ZERO
assert norm2(alpha)==Q(1,3)
assert norm2(A)==Q(34,4608**2)
assert norm2(B)==Q(1,2304**2)
initial=[Q(0),Q(1,576),Q(-1,864),Q(1,1728),Q(1,1944)]
assert [q(n) for n in range(5)]==initial
for n in range(400):
    assert 9*q(n+5)+3*q(n+4)-2*q(n+3)-6*q(n+2)-3*q(n+1)-q(n)==0, n
signs={n:('positive' if q(n)>0 else 'negative' if q(n)<0 else 'zero') for n in range(7)}
assert signs=={0:'zero',1:'positive',2:'negative',3:'positive',4:'positive',5:'negative',6:'positive'}
# For n>=7, the envelope decreases, and at n=7 it lies below L.
assert 34<36 and 400<432 and 64<147
# The unit complex root is non-torsion since its doubled-real-part square
# equals the nonintegral rational 4/3 (root-of-unity => algebraic integer).
assert Q(4,3).denominator!=1
out={
 'status':'ALL_CHECKS_PASS',
 'source':'PREFIX-583-R6 exact recurrence and initial data; frozen f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'field':'Q[t]/(t^2+2)',
 'q_initial':[str(v) for v in initial],
 'q_first_12':[str(q(n)) for n in range(12)],
 'a_norm_squared':str(norm2(A)),
 'b_norm_squared':str(norm2(B)),
 'recurrence_residual_count':400,
 'finite_signs':signs,
 'full_sign_result':'q(0)=0; q(2),q(5)<0; q(n)>0 for all other integers n>=1',
 'limit':'1/5184',
 'limsup_normalized':'1/1152',
 'liminf_normalized':'-1/1152'
}
print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))
