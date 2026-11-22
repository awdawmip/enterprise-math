#!/usr/bin/env python3
"""Native signed X6 BRC one-Link rooted loops: formal exact Green reduction.

All weights are the original integer BRC multipliers 1 or -5. The Laurent
coefficient calculation is a proved post-observer algebraic transformation;
the independent check uses named Cell, incoming port, and path order.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb, factorial
import json


def green_coefficients(N):
    # [t^(2a+j)] I_j(2t) I_0(2t)^5, as an exact factorial counting identity.
    K = N//2+1
    def convolution(a, b):
        c = [Fraction(0)]*K
        for i,x in enumerate(a):
            for j in range(K-i): c[i+j] += x*b[j]
        return c
    g0 = [Fraction(1,factorial(i)**2) for i in range(K)]
    base = [Fraction(1)]+[Fraction(0)]*(K-1)
    for _ in range(5): base = convolution(base,g0)
    G = []
    for j in range(3):
        gj = [Fraction(1,factorial(i)*factorial(i+j)) for i in range(K)]
        c = convolution(base,gj)
        walks = {r:int(c[(r-j)//2]*factorial(r)) for r in range(j,N+1,2)}
        assert all(c[(r-j)//2]*factorial(r) == walks[r] for r in walks)
        z = [0]*(N+1)
        for r,v in walks.items():
            for ell in range((N-r)//2+1):
                z[r+2*ell] += v*(-36)**ell*comb(r+ell,ell)
        G.append(z)
    return G


def rank_two_loops(N):
    # z-adic arithmetic; each array stores coefficients 0,...,N.
    G0,G1,G2=green_coefficients(N)
    unit=[1]+[0]*N
    def add(a,b): return [x+y for x,y in zip(a,b)]
    def sub(a,b): return [x-y for x,y in zip(a,b)]
    def scale(a,c): return [c*x for x in a]
    def shift(a,j=1): return [0]*j+a[:N+1-j]
    def multiply(a,b): return [sum(a[i]*b[k-i] for i in range(k+1)) for k in range(N+1)]
    def inverse(a):
        assert a[0]==1
        out=[0]*(N+1)
        out[0]=1
        for k in range(1,N+1): out[k]=-sum(a[i]*out[k-i] for i in range(1,k+1))
        return out
    Hinv=inverse(sub(unit,scale(shift(unit,2),36)))
    # U's are the two forbidden BRC directed-edge rows.
    a=multiply(Hinv,add(sub(G0,scale(shift(G1),12)),scale(shift(G2,2),36)))
    b=multiply(Hinv,sub(add(G1,scale(shift(G1,2),36)),scale(shift(add(G0,G2)),6)))
    A=multiply(Hinv,add(sub(add(G1,scale(shift(G1,2),36)),scale(shift(G0),12)),scale(shift(unit),36)))
    B=multiply(Hinv,sub(add(G0,scale(shift(G0,2),36)),add(scale(shift(G1),12),scale(unit,6))))
    c=sub(G1,scale(shift(G0),6))
    d=sub(G0,scale(shift(G1),6))
    p=add(unit,shift(A)); q=shift(B)
    idet=inverse(sub(multiply(p,p),multiply(q,q)))
    y1=multiply(idet,sub(multiply(p,c),multiply(q,d)))
    y2=multiply(idet,sub(multiply(p,d),multiply(q,c)))
    L=sub(d,shift(add(multiply(a,y1),multiply(b,y2))))
    assert all(L[n]==0 for n in range(1,N+1,2))
    return [L[2*k] for k in range(N//2+1)]


def native_brc_direct(K=10):
    directions=[(i,sgn) for sgn in (1,-1) for i in range(6)]
    origin=(0,)*6
    e1=(1,0,0,0,0,0)
    nmax=2*K
    states={(origin,6):1}  # h = -e1 (incoming-neighbour port)
    loops=[]
    for n in range(nmax+1):
        if not n%2:
            loops.append(sum(v for (x,h),v in states.items() if x==origin))
        if n==nmax: break
        remaining=nmax-n-1
        nxt=defaultdict(int)
        for (x,h),v in states.items():
            for d,(i,sign) in enumerate(directions):
                if (x==origin and d==0) or (x==e1 and d==6): continue
                y=list(x); y[i]+=sign
                # Exact return cone: no deleted endpoint contribution.
                if sum(abs(a) for a in y)>remaining: continue
                nxt[(tuple(y),(d+6)%12)] += v*(-5 if h==d else 1)
        states={key:weight for key,weight in nxt.items() if weight}
    return loops


def main():
    algebraic=rank_two_loops(40)
    direct=native_brc_direct(10)
    prior=[1,-25,390,-2365,-49550,1645010,-22026080]
    assert algebraic[:7]==prior
    assert algebraic[:11]==direct
    print(json.dumps({
        'schema':'PREFIX1010_R6_RANK_TWO_GREEN_CERTIFICATE_V1',
        'model':'P000 V5 frozen; X6 signed twelve-port Stage46 candidate BRC, incoming -e1, one blocked Link {0,e1}',
        'observer':'signed closed 2k-step Cell=0 return summed over final named incoming-neighbour ports',
        'method':'Formal Laurent coefficient, rank-two forbidden-edge resolvent; integer power-series convolution, exact rational factorial construction; independent typed signed BRC DP',
        'analytical_max_k':20,
        'coefficients_L_0_to_20':[str(x) for x in algebraic],
        'independent_native_brc_k_0_to_10':[str(x) for x in direct],
        'checks':'All eleven direct BRC coefficients agree with rank-two method; first seven agree with PREFIX-1009; odd formal-power coefficients zero',
        'claim_scope':'exact in the named candidate BRC kernel and blocked Link; no full path-port equivalence, native physical calibration, or independent mathematical review',
        'review':'AUTHOR_PROOF / EXACT_INTEGER_CROSS_CHECK / NOT_REVIEWED'
    },ensure_ascii=False,indent=2))


if __name__=='__main__': main()
