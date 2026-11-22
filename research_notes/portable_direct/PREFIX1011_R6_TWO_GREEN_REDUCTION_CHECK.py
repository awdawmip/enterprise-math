#!/usr/bin/env python3
"""PREFIX-1011: exact two-Green reduction of rooted one-Link signed X6 BRC loops.

Frozen science: P000 V5 @ f42f2906d77f24085c123f3ccfe9667d41caa96d;
Stage46 candidate twelve named signed ports w(h,d)=1-6*[h=d],
chart-relative Cell 0, incoming port -e1, block both directions of {0,e1}.

The two-Green rational identity is an exact post-observer reduction of the
original named BRC transfer. It is NOT a replacement native evolution law.
"""
from collections import defaultdict
from fractions import Fraction as Q
from math import factorial, comb
import json
from pathlib import Path

OUTPUT = Path(__file__).with_name('PREFIX1011_R6_EXACT_RESULTS.json')
MAX_K = 32
N=2*MAX_K

def convolve(a,b,n):
    out=[Q(0)]*(n+1)
    for i,x in enumerate(a[:n+1]):
        if x:
            for j,y in enumerate(b[:n+1-i]):
                if y:out[i+j]+=x*y
    return out

def green_0_1_2(N):
    # combinatorial coefficients of exact signed six-axis words; no external propagator
    kmax=N//2+1
    g0=[Q(1,factorial(i)**2) for i in range(kmax)]
    base=[Q(1)]+[Q(0)]*(kmax-1)
    for _ in range(5): base=convolve(base,g0,kmax-1)
    G=[]
    for j in range(3):
        gj=[Q(1,factorial(i)*factorial(i+j)) for i in range(kmax)]
        c=convolve(base,gj,kmax-1)
        v=[Q(0)]*(N+1)
        for r in range(j,N+1,2):
            w=c[(r-j)//2]*factorial(r)
            assert w.denominator==1
            for ell in range((N-r)//2+1):
                v[r+2*ell]+=w*(-36)**ell*comb(r+ell,ell)
        G.append(v)
    return G

def add(a,b):return [x+y for x,y in zip(a,b)]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def scale(a,t):return [x*t for x in a]
def shift(a,t=1):return [Q(0)]*t+a[:len(a)-t]
def mul(a,b):return convolve(a,b,len(a)-1)
def invert(a):
    assert a[0]==1
    n=len(a)-1
    v=[Q(0)]*(n+1);v[0]=1
    for k in range(1,n+1):v[k]=-sum(a[i]*v[k-i] for i in range(1,k+1))
    return v

def loops_two_green(G0,G2):
    n=len(G0)-1
    one=[Q(1)]+[Q(0)]*n
    zF=shift(G0,1)
    U=sub(add(G0,scale(shift(G0,2),36)),one)
    # (1+36z^2)G_0 - 12zG_1 = 1 (origin coefficient of D G=1)
    G1=scale(shift(U,0),Q(1,12)) # equals z G1, not G1 itself
    plus=add(one,mul(sub(one,scale(shift(one),6)),add(zF,G1)))
    minus=sub(one,mul(add(one,scale(shift(one),6)),sub(zF,G1)))
    R=scale(add(one,mul(sub(one,scale(shift(one,2),36)),G0)),Q(1,2))
    numerator=mul(R,sub(one,scale(shift(sub(G0,G2),2),6)))
    L=mul(numerator,invert(mul(plus,minus)))
    assert all(x.denominator==1 for x in L)
    assert all(L[i]==0 for i in range(1,n+1,2))
    return [int(L[2*k]) for k in range(n//2+1)]

def loops_three_green(G0,G1,G2):
    # Independent pre-existing PREFIX-1010 rank-two reconstruction
    n=len(G0)-1
    one=[Q(1)]+[Q(0)]*n
    Hinv=invert(sub(one,scale(shift(one,2),36)))
    a=mul(Hinv,add(sub(G0,scale(shift(G1),12)),scale(shift(G2,2),36)))
    b=mul(Hinv,sub(add(G1,scale(shift(G1,2),36)),scale(shift(add(G0,G2)),6)))
    A=mul(Hinv,add(sub(add(G1,scale(shift(G1,2),36)),scale(shift(G0),12)),scale(shift(one),36)))
    B=mul(Hinv,sub(add(G0,scale(shift(G0,2),36)),add(scale(shift(G1),12),scale(one,6))))
    c=sub(G1,scale(shift(G0),6)); d=sub(G0,scale(shift(G1),6))
    p=add(one,shift(A)); q=shift(B)
    detinv=invert(sub(mul(p,p),mul(q,q)))
    y1=mul(detinv,sub(mul(p,c),mul(q,d)))
    y2=mul(detinv,sub(mul(p,d),mul(q,c)))
    L=sub(d,shift(add(mul(a,y1),mul(b,y2))))
    assert all(L[2*k+1]==0 for k in range(n//2))
    return [int(L[2*k]) for k in range(n//2+1)]

def direct_brc(K):
    # Named h and d each in twelve directions, maintain signed Cell and port
    dirs=[(a,s) for s in (1,-1) for a in range(6)]
    O=(0,)*6; E=(1,0,0,0,0,0)
    states={(O,6):1}; out=[]
    for t in range(2*K+1):
        if t%2==0:out.append(sum(v for (x,h),v in states.items() if x==O))
        if t==2*K:break
        left=2*K-t-1
        nxt=defaultdict(int)
        for (x,h),weight in states.items():
            for d,(a,s) in enumerate(dirs):
                if (x==O and d==0) or (x==E and d==6):continue
                v=list(x);v[a]+=s;v=tuple(v)
                if sum(abs(i) for i in v)>left:continue
                nxt[(v,(d+6)%12)]+=weight*(-5 if h==d else 1)
        states={key:value for key,value in nxt.items() if value}
    return out

def main():
    G0,G1,G2=green_0_1_2(N)
    assert all(x==y for x,y in zip(add(G0,scale(shift(G0,2),36)),add([Q(1)]+[Q(0)]*N,scale(shift(G1),12))))
    L2=loops_two_green(G0,G2)
    L3=loops_three_green(G0,G1,G2)
    assert L2==L3
    historical=[1,-25,390,-2365,-49550,1645010,-22026080,78710035,4076647030,-215329002630,7724818416180,-146088496994110,-815898004254020,124676314144665400,-3443921270995306960,63438846740919530075,-1369266505018454720690,8879677449128497942850,2057298710193877238515720,-116199318172489902861767990,2654805287682237859503700820]
    assert L2[:21]==historical
    direct=direct_brc(8)
    assert direct==L2[:9]
    result={
        'schema':'PREFIX1011_R6_TWO_GREEN_EXACT_CERTIFICATE_V1',
        'frozen_source':'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json',
        'model':'Stage46 candidate signed X6 BRC, directions +/-e1..+/-e6; incoming -e1; blocked directed Link 0<->e1; no renormalization',
        'observer':'sum of named signed amplitude weights for all 2k-step paths from chart Cell 0 back to Cell 0',
        'result':'two Green series G0 and G2 suffice for the rooted-return generating observer, via the formal resolvent identity and origin coefficient relation',
        'max_k':MAX_K,
        'L_0_to_32':[str(x) for x in L2],
        'independent_native_brc_k_0_to_8':[str(x) for x in direct],
        'checks':['formal origin recurrence exact through z^64','two-series reduction agrees with prior three-series rank-two formula at k=0..32','historical PREFIX-1010 integer values agree at k=0..20','independent named 12-port BRC dynamic programming agrees at k=0..8','odd coefficients 0'],
        'scope':'two-series sufficiency at rooted scalar observer; no claim of algebraic minimality, port-resolved equivalence, physical-time mapping, or independent review',
        'review':'AUTHOR_ALGEBRAIC_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED'
    }
    OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print('PASS; native up to 8; 2-versus-3 to 32; k21..32=',L2[21:])

if __name__=='__main__':main()
