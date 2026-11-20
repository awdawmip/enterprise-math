#!/usr/bin/env python3
"""EC49FUW: exact Fraction witnesses to finite-n fixed-j compulsory endpoint mixing.

Every asserted inequality uses exact fractions; printed floats are illustrative.
The universal asymptotic proof is in the companion Markdown theorem.
"""
from fractions import Fraction as F
from math import comb

E=F(31597745,1653649)
BETA=F(3,637)
UA=F(21829245984)
UB=F(45529434409)
UC=F(456083905)
ZERO=F(0)
U={ZERO:UA/UB, E:UA/(UB-UC*E)}
assert ZERO<U[ZERO]<U[E]<1

def pq(x,t):
    T=(1-x)*(1-BETA*x+BETA*x*t)
    p,q=1-T,1-U[t]*T
    assert 0<=p<q<=1
    return p,q

def signed(n,k,x,t):
    p,q=pq(x,t)
    return comb(n,k)*(q**k*(1-q)**(n-k)-p**k*(1-p)**(n-k))

def advantage(n,j,x,t):
    p,q=pq(x,t)
    return sum((comb(n,k)*(p**k*(1-p)**(n-k)-q**k*(1-q)**(n-k))
                for k in range(j)),ZERO)

def witness(n,j):
    # Exact b_(n,j) root isolation via rational arithmetic.
    lo,hi=F(0),F(1,2)
    assert signed(n,j,lo,E)>0 and signed(n,j,hi,E)<0,(n,j)
    for _ in range(105):
        mid=(lo+hi)/2
        if signed(n,j,mid,E)>0: lo=mid
        else: hi=mid
    assert signed(n,j,lo,E)>0 and signed(n,j,hi,E)<0
    # Rational point strictly left of E count-j Bayes crossing.
    x=lo*(1-F(1,1000))
    z=[signed(n,k,x,ZERO) for k in range(n+1)]
    e=[signed(n,k,x,E) for k in range(n+1)]
    g=advantage(n,j,x,E)-advantage(n,j,x,ZERO)
    h=advantage(n,j+1,x,E)-advantage(n,j+1,x,ZERO)
    d=e[j]-z[j]
    assert e[j]>0 and z[j]<0 and d>0
    assert g>0 and h<0, (n,j,float(g),float(h))
    lam=-z[j]/d
    assert 0<lam<1
    masses=[(1-lam)*a+lam*b for a,b in zip(z,e)]
    assert all(t<0 for t in masses[:j]),(n,j,"lower counts")
    assert masses[j]==0
    assert all(t>0 for t in masses[j+1:]),(n,j,"upper counts")
    # Left/right convex-TV slopes: H_j<0<G_j.
    assert h<0<g
    return n,j,float(x),float(lam),float(g),float(h)

if __name__=='__main__':
    for n in (20,30,40,60):
        for j in (1,2,3):
            n,j,x,lam,g,h=witness(n,j)
            print(f'PASS n={n} j={j} rational_x≈{x:.15g} unique_lambda≈{lam:.12g} G_j≈{g:.5g} H_j≈{h:.5g}',flush=True)
    print('ALL PASS: 12 exact rational local mixing witnesses; universal theorem is analytic.')
