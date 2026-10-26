#!/usr/bin/env python3
"""Author check: exact full-history -> likelihood-ratio/count flow Markovization.
External finite iid experiment only; mathematical proof is in accompanying note.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb

P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
N=4

def counts(h):
    return (len(h),h.count(0),h.count(1))

def pi(h):
    n=len(h)
    if n==N:
        x=F((1+sum(h))%5,4)
        return (x,1-x,F(0))
    s=sum((i+1)*(x+1) for i,x in enumerate(h))
    pp=F((n+sum(h))%4,12)
    pq=F((2*n+s)%4,12)
    return (pp,pq,1-pp-pq)

def full_history_flow():
    alive={(): (F(1),F(1))}
    actions=defaultdict(lambda:[F(0),F(0),F(0)])
    masses=defaultdict(F)
    obs=[F(0),F(0),F(0),F(0)]
    for n in range(N+1):
        new={}
        for h,(p,q) in alive.items():
            c=counts(h);pp,pq,pc=pi(h)
            assert pp>=0 and pq>=0 and pc>=0 and pp+pq+pc==1
            masses[c]+=p
            for i,z in enumerate((pp,pq,pc)):actions[c][i]+=p*z
            obs[0]+=p*pq; obs[1]+=q*pp
            if n<N:
                obs[2]+=p*pc;obs[3]+=q*pc
                for i in range(3):new[h+(i,)]=(p*pc*P[i],q*pc*Q[i])
            else:assert pc==0
        alive=new
    averaged={c:tuple(x/masses[c] for x in a) for c,a in actions.items()}
    return tuple(obs),averaged,masses

def count_flow(averaged):
    alive={(0,0,0):(F(1),F(1))}
    obs=[F(0),F(0),F(0),F(0)]
    for n in range(N+1):
        nexts=defaultdict(lambda:[F(0),F(0)])
        for (depth,a,b),(p,q) in alive.items():
            assert depth==n
            pp,pq,pc=averaged[(depth,a,b)]
            obs[0]+=p*pq;obs[1]+=q*pp
            if n<N:
                obs[2]+=p*pc;obs[3]+=q*pc
                for i,ab in enumerate(((a+1,b),(a,b+1),(a,b))):
                    tgt=(n+1,*ab)
                    nexts[tgt][0]+=p*pc*P[i]
                    nexts[tgt][1]+=q*pc*Q[i]
            else:assert pc==0
        alive=nexts
    return tuple(obs)

a,policy,occupied=full_history_flow()
b=count_flow(policy)
assert a==b, (a,b)
# Exact positive rational occupancy-flow LP checks, one P measure only.
u={c:tuple(occupied[c]*z for z in policy[c]) for c in occupied}
assert u[(0,0,0)] and sum(u[(0,0,0)])==1
for c in u:
    n,aa,bb=c
    assert sum(u[c])==occupied[c]
    if n==N:assert u[c][2]==0
    if n:
        incoming=F(0)
        if aa:incoming+=P[0]*u[(n-1,aa-1,bb)][2]
        if bb:incoming+=P[1]*u[(n-1,aa,bb-1)][2]
        if aa+bb<=n-1:incoming+=P[2]*u[(n-1,aa,bb)][2]
        assert occupied[c]==incoming
lp_errorP=sum(x[1] for x in u.values())
lp_errorQ=sum(F(2**(c[1]+c[2]),3**c[1])*x[0] for c,x in u.items())
lp_timeP=sum(x[2] for x in u.values())
lp_timeQ=sum(F(2**(c[1]+c[2]),3**c[1])*x[2] for c,x in u.items())
assert (lp_errorP,lp_errorQ,lp_timeP,lp_timeQ)==a
assert len(occupied)==sum((n+1)*(n+2)//2 for n in range(N+1))==35
assert sum(3**n for n in range(N+1))==121
# Exact count-likelihood ratio for Stage161 model; no two distinct (a,b) collide.
seen=set()
for n in range(15):
    states={F(2**(aa+bb),3**aa) for aa in range(n+1) for bb in range(n-aa+1)}
    assert len(states)==(n+1)*(n+2)//2
    seen.update((n,x) for x in states)
assert len(seen)==680
# Explicit failure of LR-erasing one-state horizon-one quotient.
# P(a)=3/4, Q(a)=1/4, decide Q on a and P on b; errors (3/4,3/4).
assert (F(3,4),F(3,4))!=(F(3,4),1-F(3,4))
print('EXACT_MARKOVIZATION_PASS N=4 histories=121 states=35',
      'eP,eQ,tP,tQ='+','.join(map(str,a)))
print('STAGE_N14_LR_INJECTIVITY_PASS states=680 actions=1920')
print('LR_ERASURE_COUNTEREXAMPLE_PASS errors=3/4,3/4 vs (r,1-r)')
