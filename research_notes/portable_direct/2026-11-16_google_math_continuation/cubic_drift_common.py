"""Exact all-common count-errors for seven positions / adjacent fourth differences.
Stdlib only. Stores JSON next to itself. Independent coordinate envelope solely
for proving the infinite tail.
"""
from itertools import product,combinations
from math import lcm,comb
from fractions import Fraction
from pathlib import Path
import json

P=(455,-295,-25,185,-25,-295); W=(1,-4,6,-4,1); phases=range(6)
errors=tuple(product(range(-2,3),repeat=2))
B=4000
U=tuple(sum(w*P[(a+i)%6] for i,w in enumerate(W)) for a in phases)
assert U==tuple(36*x for x in (20,20,20,-100,140,-100))
V=tuple(tuple(U[(a+k)%6] for k in range(3)) for a in phases)
gap=min(max(abs(x-y) for x,y in zip(V[a],V[b])) for a,b in combinations(phases,2))
assert gap==120*36 and all(sum(w*i**k for i,w in enumerate(W))==0 for k in range(4))
def counts(n):
    c=[0]*n;t=[0]*n;c[0]=1
    for i,w in enumerate((1,1,2,3,6)):
        for j in range(w,n):
            t[j]+=t[j-w]+(0 if i else c[j-w])
            c[j]+=c[j-w]
    C,T=[0],[0]
    for ct,tt in zip(c,t):
        C.append(C[-1]+ct);T.append(T[-1]+tt)
    return C,T
C,T=counts(B+72)
def bpoly(q):return 18*q**4+54*q**3-345*q*q+2070*q-16315
def tail():
    # C,T on each residue modulo 6 are polynomial of degrees <=5,6, since
    # GF in q−1 is 1/[(1-z)^3(1-z²)(1-z³)(1-z⁶)] for totals and z/(1-z)
    # times that for marks. Once cleared, each inequality has degree <=9.
    for q0 in range(B,B+6):
        for (e,d),sign in product(errors,(-1,1)):
            def f(t):
                q=q0+6*t;den=C[q]+d
                return 108*den+sign*(108*q**3*(T[q]+e)-(bpoly(q)+3*P[q%6])*den)
            v=[f(t) for t in range(10)]
            cs=[]
            while v:
                cs.append(v[0]);v=[y-x for x,y in zip(v,v[1:])]
            assert cs[0]>0 and all(x>=0 for x in cs)
            assert sum(c*comb(10,j) for j,c in enumerate(cs))==f(10)
    assert C[B]>2 and 2*sum(map(abs,W))*36<gap
def raw(q):
    return [(108*q**3*(T[q]+e)-bpoly(q)*(C[q]+d),3*(C[q]+d)) if C[q]+d>0 else None for e,d in errors]
obs=[None]+[raw(q) for q in range(1,B+7)]
def build(r):
    z=obs[r:r+7];sc=lcm(*(v[1] for col in z for v in col if v))
    return sc,[[v[0]*(sc//v[1]) if v else None for v in col] for col in z]
def evaluate(sc,v):
    Z=[sum(w*x for w,x in zip(W,v[j:])) for j in range(3)]
    dist=[max(abs(y-sc*p) for y,p in zip(Z,ref)) for ref in V]
    return Z,dist
def wit(r,sc,v,indices,b):
    a=r%6;Z,dist=evaluate(sc,v)
    assert b!=a and dist[b]<=dist[a]
    f=lambda d:str(Fraction(d,36*sc))
    return dict(r=r,phase=a,rival=b,errors=[errors[i] for i in indices],
                z=[f(x) for x in Z],true_distance=f(dist[a]),rival_distance=f(dist[b]))
def common(r):
    a=r%6;sc,cols=build(r)
    for i,v in enumerate(zip(*cols)):
        if None in v:continue
        Z,dist=evaluate(sc,v)
        for b,x in enumerate(dist):
            if b!=a and x<=dist[a]:return wit(r,sc,v,[i]*7,b)
if __name__=='__main__':
    tail()
    for r in range(B-1,0,-1):
        w=common(r)
        if w:break
    out=dict(threshold=r+1,witness=w)
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(out)
