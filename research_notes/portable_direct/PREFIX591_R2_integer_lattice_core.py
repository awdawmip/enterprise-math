#!/usr/bin/env python3
"""Exact native X6-BRC integer-lattice intertwining certificate (PREFIX-591).
Native transitions reused verbatim from co-located PREFIX589_R2_dual_carrier_certificate.py.
"""
from pathlib import Path
import runpy
m=runpy.run_path(str(Path(__file__).with_name('PREFIX589_R2_dual_carrier_certificate.py')))
A,T,blocks=m['A'],m['D'],m['blocks']
N=96

def W(v):
    y=[0]*N
    for g in blocks:
        s=sum(v[i] for i in g)
        for i in g:y[i]=s-v[i]
    return y

def H(v):
    y=[0]*N
    for g in blocks:
        s=sum(v[i] for i in g)
        for i in g:y[i]=s-3*v[i]
    return y

def lattice(v):
    return all(len({v[i]%3 for i in g})==1 for g in blocks)

def move(M,v):
    return [sum(w*u for w,u in zip(row,v)) for row in M]

# Integer version of T_k H = H A_k. Seven native labelled generators,
# all 96 columns; no floating-point or surrogate transition model.
for k in range(7):
    for j in range(N):
        e=[int(t==j) for t in range(N)]
        assert move(T[k],H(e))==H(move(A[k],e))
        assert W(H(e))==[3*x for x in e]
        assert lattice(H(e))

inputs=[[int(j==0) for j in range(N)], [1]*N,
        [int(j in blocks[0]) for j in range(N)],
        [int(j in (0,1,4,5,9,16,71)) for j in range(N)]]
steps=[(2,3,5,7,11,13,17),(1,1,1,1,1,1,1),
       (3,1,4,1,5,9,2),(1,7,2,8,1,8,4)]
for r in inputs:
    a=r[:]; v=H(r)
    plus=W(r); minus=[2*x for x in r]
    for d in range(13):
        assert lattice(v) and W(v)==[3*x for x in a]
        assert v==[plus[j]-minus[j] for j in range(N)]
        if d==12:break
        x=steps[d%4]; coefs=list(x[:6])+[x[0]*x[6]]
        aa=[[sum(coefs[k]*A[k][i][j] for k in range(7)) for j in range(N)] for i in range(N)]
        tt=[[sum(coefs[k]*T[k][i][j] for k in range(7)) for j in range(N)] for i in range(N)]
        a=move(aa,a);v=move(tt,v)
        plus=move(tt,plus);minus=move(tt,minus)
        assert all(z>=0 for z in plus+minus+a)

i,j=blocks[0][:2]
e=[int(t==i) for t in range(N)]
f=[int(t==j) for t in range(N)]
assert sum(e[t]*f[t] for t in range(N))==0
assert sum(t*u for t,u in zip(W(e),W(f)))==2
assert sum(t*u for t,u in zip(W(e),[2*v for v in f]))==2
print('ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED; 7 generators × 96 columns; 4 cases × 13 depths; 24 mod-3 blocks')
