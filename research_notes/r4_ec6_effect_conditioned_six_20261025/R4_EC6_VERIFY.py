#!/usr/bin/env python3
from collections import defaultdict
from fractions import Fraction
from itertools import product
import json

E={0:((2,-1,-1),(2,1,-1)),1:((0,-1,-1),(0,1,-1)),2:((1,1,1),(2,1,-1))}
R=((1,0),(2,0),(2,2))
def advance(s,b):
    q,r,e,k=s; qp,eta,t=E[q][b]
    return qp,R[r][b],eta*e,eta*k+t
def step(P):
    D=defaultdict(int)
    for s,m in P.items():
        for b in (0,1):D[advance(s,b)]+=m
    return D
def obs(P):
    D=defaultdict(int)
    for (q,r,e,k),m in P.items(): D[q,int(r==2),e,k]+=m
    return D
def theta(P,q,e,k):
    a=P.get((q,0,e,k),0);b=P.get((q,1,e,k),0)
    return Fraction(b,a+b) if a+b else Fraction(0)
def step6(A,P):
    D=defaultdict(Fraction)
    for (q,h,e,k),m in A.items():
        for b,(qp,eta,t) in enumerate(E[q]):
            key=(qp,h,eta*e,eta*k+t)
            if h or b:
                D[key]+=m
            else:
                x=theta(P,q,e,k)
                if x: D[(qp,1,eta*e,eta*k+t)]+=m*x
                if x<1: D[(qp,0,eta*e,eta*k+t)]+=m*(1-x)
    return D
def verify(N=90):
    P={(0,0,1,0):1}; A={(0,0,1,0):Fraction(1)}
    for n in range(N+1):
        C=obs(P)
        assert set(A)==set(C) and all(A[x]==v for x,v in C.items())
        assert sum(P.values())==2**n
        if n<=11:
            brute=defaultdict(int)
            for word in product((0,1),repeat=n):
                s=(0,0,1,0)
                for b in word:s=advance(s,b)
                brute[s]+=1
            assert dict(brute)==dict(P)
        if n==7:
            assert P.get((2,0,-1,1))==P.get((2,1,-1,1))==1
            assert theta(P,2,-1,1)==Fraction(1,2)
            channels=sorted((q,h,v) for (q,h,e,k),v in C.items() if (e,k)==(1,-3))
            assert channels==[(0,0,2),(0,1,2),(1,0,3),(1,1,1),(2,0,1),(2,1,9)]
        if n>=10:
            bins=[0,0,0]
            for (q,h,e,k),m in C.items():
                if q==2 and h==0:
                    t=theta(P,q,e,k)
                    bins[0 if t==0 else 2 if t==1 else 1]+=1
            assert bins==[8,2*(n-6),2],(n,bins)
        if n<N:
            A=step6(A,P)
            P=step(P)
    return {"status":"PASS","depth":N,
            "bruteforce_up_to":11,"all_six_channel_histograms_equal":True,
            "n7_mixed_example":"theta(2,-1,+1)=1/2",
            "mixed_effect_fibers_n_ge_10":"2*(n-6)"}
if __name__=="__main__":
    print(json.dumps(verify(),indent=2))
