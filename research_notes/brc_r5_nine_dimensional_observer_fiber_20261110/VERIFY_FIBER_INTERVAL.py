#!/usr/bin/env python3
"""Exact maximal BRC observation-fiber interval s_-(t)<=s<=s_+(t).
Import sibling FIBER_CERTIFICATE.py for pinned input/marginal/physical formulas.
"""
from sympy import Matrix, Rational
import FIBER_CERTIFICATE as m

A=m.base;S=m.S;K=m.SK
R=m.rho
lower=[];upper=[]
for i in range(26):
    if K[i]>0:
        lower.append((i,-A[i]/K[i],tuple(-S[i,j]/K[i] for j in range(8))))
    if K[i]<0:
        upper.append((i,A[i]/(-K[i]),tuple(S[i,j]/(-K[i]) for j in range(8))))
print('K_POSITIVE_LOWER_INEQUALITIES',[(i,str(a)) for i,a,_ in lower])
print('K_NEGATIVE_UPPER_INEQUALITIES',[(i,str(a)) for i,a,_ in upper])
lo=max(lower,key=lambda x:x[1]);up=min(upper,key=lambda x:x[1]);
print('CENTER_MAX_LOWER',lo[0],lo[1])
print('CENTER_MIN_UPPER',up[0],up[1])

def gap(x,y):
    i,a,u=x;j,b,v=y
    center=b-a; grad=tuple(v[k]-u[k] for k in range(8)); L=sum(abs(w) for w in grad)
    return (center/L if L else None,center,L)

mins_l=[]; mins_u=[]
for other in lower:
    if other[0]==lo[0]:continue
    rr=gap(other,lo)
    mins_l.append((rr[0],other[0],rr[1],rr[2]))
for other in upper:
    if other[0]==up[0]:continue
    rr=gap(up,other)
    mins_u.append((rr[0],other[0],rr[1],rr[2]))
print('LOWER_ACTIVE_STABILITY_RADIUS',min(mins_l))
print('UPPER_ACTIVE_STABILITY_RADIUS',min(mins_u))
print('CURRENT_CHART_RHO',R)
print('ACTIVE_LOWER_OVER_CHART',all(a is None or a>=R for a,_,_,_ in mins_l))
print('ACTIVE_UPPER_OVER_CHART',all(a is None or a>=R for a,_,_,_ in mins_u))
print('CENTER_FIBER_WIDTH',up[1]-lo[1])
print('LOWER_PIECEWISE_EXPRESSION',lo)
print('UPPER_PIECEWISE_EXPRESSION',up)

assert m.RHO/2==R
assert all(A[i]-R*sum(abs(S[i,k]) for k in range(8))>=0 for i in range(26) if K[i]==0)
assert lo[1]<0<up[1]
assert lo[0]==2 and up[0]==10
assert lo[2]==tuple(Rational(v,197600) for v in (1,-1,-3,1,-1,1,3,0))
assert up[2]==tuple(Rational(v,12018120) for v in (-7,-1,5,-1,7,1,-5,20))
print('PASS_EXACT_MAXIMAL_FIBER_INTERVAL_FORMULA')
