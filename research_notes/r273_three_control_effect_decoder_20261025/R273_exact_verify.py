#!/usr/bin/env python3
"""R273 exact integer verifier: formal six-slot BRC, not native heartbeat X6."""
from collections import defaultdict
from itertools import product
from functools import lru_cache
from json import dumps

EDGES = {
    0: ((2,-1,-1),(2,1,-1)),
    1: ((0,-1,-1),(0,1,-1)),
    2: ((1,1,1),(2,1,-1)),
}
DELTA=((1,0),(2,0),(2,2))
BASE={7:(2,2,3,1,1,9),8:(1,6,1,9,2,16),9:(1,19,2,20,4,28)}
RESET=16482

def step(s,a):
    q,r,e,k=s
    q2,eta,b=EDGES[q][a]
    return q2,DELTA[r][a],eta*e,eta*k+b

def full_next(x):
    z=defaultdict(int)
    for key,w in x.items():
        for a in (0,1):z[step(key,a)]+=w
    return z

def three_next(x):
    z=defaultdict(int)
    for (q,e,k),w in x.items():
        for q2,eta,b in EDGES[q]:
            z[(q2,eta*e,eta*k+b)]+=w
    return z

def fib(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a

def tally(x):
    z=defaultdict(lambda:[0,0])
    for (q,r,e,k),w in x.items():
        z[(q,e,k)][int(r==2)]+=w
    return z

def reset_lower(n):
    if n<7:return None
    K=(n-7)//30
    t=n-30*K
    j=7+(t-7)%3
    h=(t-j)//3
    e,k={7:(1,-3),8:(1,0),9:(-1,-1)}[j]
    b=BASE[j]
    L=sum(min(b[2*q],b[2*q+1]) for q in range(3))
    return (K,j,(e,k-e*(4*K+h)),L*RESET**K)

def run(N=128):
    x={(0,0,1,0):1}
    u={(0,1,0):1}
    examples={}
    brute=0
    for n in range(N+1):
        if n<=12:
            zz=defaultdict(int)
            for seq in product((0,1),repeat=n):
                st=(0,0,1,0)
                for a in seq:st=step(st,a)
                zz[st]+=1
            assert dict(zz)==dict(x)
            brute+=2**n
        z=tally(x)
        assert all(sum(counts)==u[key] for key,counts in z.items())
        assert len(z)==len(u)
        A=sum(a for a,b in z.values())
        B=sum(b for a,b in z.values())
        assert A==fib(n+2) and A+B==2**n
        M=sum(min(a,b) for a,b in z.values())
        assert M<=min(A,B)
        if n<=2:assert M==0
        if n>=3:assert M>=1
        if n==3:assert M==1
        if n==30:assert x.get((0,0,1,-4),0)==RESET
        if n in BASE:
            g={7:(1,-3),8:(1,0),9:(-1,-1)}[n]
            b=tuple(z.get((q,*g),(0,0))[h] for q in range(3) for h in (0,1))
            assert b==BASE[n]
        lb=reset_lower(n)
        if lb:
            K,j,g,bound=lb
            assert M>=bound
            assert sum(min(z.get((q,*g),(0,0))) for q in range(3))>=bound
        if n in (0,1,2,3,4,7,8,9,20,30,60,80,96,128):
            examples[str(n)]={"M":str(M),"F_nplus2":str(A),
                              "two_to_n":str(2**n),
                              "three_control_majority_l1":str(2*M),
                              "reset_lower":str(lb[3]) if lb else None}
        if n<N:
            x=full_next(x)
            u=three_next(u)
    assert ((lambda a,b:(a[0],a[2],a[3])==(b[0],b[2],b[3]))(
        __import__('functools').reduce(lambda st,a:step(st,int(a)),"000",(0,0,1,0)),
        __import__('functools').reduce(lambda st,a:step(st,int(a)),"101",(0,0,1,0))))
    print(dumps({"status":"PASS","depth_max":N,
                 "raw_words_brute_checked":brute,
                 "native_execution":"NOT_RUN",
                 "samples":examples},indent=2))
if __name__=="__main__":run()
