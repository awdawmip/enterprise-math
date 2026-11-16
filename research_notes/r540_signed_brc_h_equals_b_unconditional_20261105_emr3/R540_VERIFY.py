#!/usr/bin/env python3
"""R540 exact finite regression for a universal FORMAL algebraic identity; proof is in R540_PROOF.zh-CN.md."""
from math import comb

def C(k):
    return 0 if k < 0 else comb(2*k, k)//(k+1)

def bc(n, j):
    return 0 if j < 0 or j > n else comb(n, j)

def Hcoef(k, t):
    r = 2*k+1
    if not 2 <= t <= r:
        return 0
    return sum(comb(r-t, q)*(bc(2*t, r-2*q)-bc(2*t, r-2*q-1))
               for q in range(r-t+1))

def Bcoef(k, t):
    r=2*k+1
    if not 2 <= t <= r:
        return 0
    return sum(comb(t-1, 2*q)*4**q*C(k-q)
               for q in range((t-1)//2+1))

def Gcoef(k, t):
    r=2*k+1
    return bc(t-1,r)*2**r + sum(bc(t-1,2*q)*4**q*C(k-q) for q in range(k+1))

def H(k, t):
    r=2*k+1
    return 0 if t>r or t<2 else comb(r+t,2*t)*Hcoef(k,t)

def B(k, t):
    r=2*k+1
    return 0 if t>r or t<2 else comb(r+t,2*t)*Bcoef(k,t)

eligible=0
for k in range(51):
    for t in range(2, 2*k+2):
        a,b,c=Hcoef(k,t),Bcoef(k,t),Gcoef(k,t)
        assert a==b==c,(k,t,a,b,c)
        assert H(k,t)==B(k,t)
        eligible+=1

edge=0
for k in range(12):
    for t in range(2*k+2,2*k+11):
        assert Gcoef(k,t)==bc(t-1,2*k+1)*2**(2*k+1)+sum(
            bc(t-1,2*q)*4**q*C(k-q) for q in range(k+1))
        assert H(k,t)==B(k,t)==0
        edge+=1
print(f"R540_EXACT_PY_PASS eligible_H_B_G_pairs={eligible} t_over_r_defined_zero_checks={edge}")
