#!/usr/bin/env python3
"""Exact, source-preserving finite checks for the 2013 CM supersingular scalar-port discharge.

This checks a proven published theorem's relevant instances and independently checks
an algebraic transport identity. Finite checks do not prove the D25 p^3 conjecture.
"""
from math import comb, isqrt
import json

def prime(p):
    return p > 1 and all(p % d for d in range(2,isqrt(p)+1))

def verify(p):
    assert p > 3 and prime(p) and p % 24 in (13,19)
    m=(p-1)//6
    M=p**3
    inv2=pow(2,-1,M)
    a=[1]
    E=[1]
    for k in range(p-1):
        a.append(a[-1]*(2*k+1)*(3*k+1)*(3*k+2)*pow(18*(k+1)**3,-1,M)%M)
        E.append(E[-1]*(2*k+1)*pow(2*(k+1),-1,M)%M)
    f=sum(a[k]*pow(inv2,k,M) for k in range(p))%M
    W=sum((6*k+1)*a[k]*pow(inv2,k,M) for k in range(p))%M
    assert f%(p*p)==0
    P=[0]*(p+3*m)
    for j in range(3*m+1):
        e=((-1)**j*comb(3*m,j))%M
        for k in range(p):P[k+j]=(P[k+j]+e*a[k])%M
    C=[0]*p
    for j in range(p):
        ej=E[j]
        for k in range(p-j):C[k+j]=(C[k+j]+ej*a[k])%M
    A=P[:p]; H=P[p:]
    D=[(c-v)%M for c,v in zip(C,A)]
    def obs(coeffs,shift=0):
        return sum((3*(i+shift)-1)*v*pow(inv2,i+shift,M) for i,v in enumerate(coeffs))%M
    L=obs(C)
    U=obs(H,p)
    T=obs(D)
    e0=pow(2,-3*m,M)
    assert W==(2*pow(e0,-1,M)*(L+U-T)+3*p*f)%M
    q=(2**(p-1)-1)//p
    q_rhs=(-p*inv2+p*p*q*pow(4,-1,M))%M
    assert q_rhs==(p*e0*inv2)%M
    assert (L+U-T)%M==q_rhs
    return {"p":p,"f_over_p2_mod_p":(f//(p*p))%p,"W_mod_p3":W,
       "L":L,"U":U,"T":T,"U_over_p2_mod_p":(U//(p*p))%p,
       "signed_L_plus_U_minus_T":(L+U-T)%M,
       "fermat_q2_mod_p":q%p,"explicit_target":q_rhs}

if __name__ == '__main__':
    r=[verify(p) for p in [13,19,37,43,109,373,1171]]
    print(json.dumps({'status':'FINITE_EXACT_REPLAY_PASS_NOT_UNIVERSAL_PROOF',
       'results':r},indent=2))
