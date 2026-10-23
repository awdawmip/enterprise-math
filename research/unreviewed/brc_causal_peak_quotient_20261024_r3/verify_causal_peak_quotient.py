#!/usr/bin/env python3
"""Exact, standard-library BRC causal-peak quotient checker; not a formal proof."""
from functools import lru_cache
from itertools import product
from collections import defaultdict
from fractions import Fraction as F
import json

D=1000
ACT='023'
Q=((1,665,1,333),(333,333,1,333),(1,1,1,997))
E=((0,1),(1,2),(1,3),(2,3))

def inc(c,a):
    t=list(c)
    t[ACT.index(a)]+=1
    return tuple(t)

@lru_cache(None)
def delta(c):
    n=sum(c)
    if n<2: return F(0)
    total=0
    for i,j in E:
        be=ai=aj=1
        for k,x in enumerate(c):
            be*=(Q[k][i]+Q[k][j])**x
            ai*=Q[k][i]**x
            aj*=Q[k][j]**x
        total+=be-ai-aj
    return F(total,D**n)

@lru_cache(None)
def B(c):
    n=sum(c)
    total=0
    for i,j in E:
        z=1
        for k,x in enumerate(c):
            z*=(Q[k][i]+Q[k][j])**x
        total+=z
    return F(total,D**n)

@lru_cache(None)
def path_stats(c,word):
    t=c
    d=[delta(t)]
    for a in word:
        t=inc(t,a)
        d.append(delta(t))
    positive=sum((max(d[k]-d[k-1],0) for k in range(1,len(d))),F(0))
    return positive,max(d)

def state(word):
    c=(0,0,0)
    M=R=F(0)
    for a in word:
        c2=inc(c,a);d2=delta(c2)
        R+=max(d2-delta(c),0)-max(d2-M,0)
        M=max(M,d2)
        c=c2
    return c,R,M

def dp(word):
    occ=[0]*16
    occ[0]=1
    for a in word:
        nxt=[0]*16
        for mask,x in enumerate(occ):
            if not x: continue
            for i,p in enumerate(Q[ACT.index(a)]):
                nxt[mask|(1<<i)]+=x*p
        occ=nxt
    return F(sum(occ[(1<<i)|(1<<j)] for i,j in E),D**len(word))

# Complete ordered words through length 8: independent occupancy mask DP and cap dynamics.
mask_cases=cap_steps=0
states=[]
for n in range(9):
    for tup in product(ACT,repeat=n):
        w=''.join(tup)
        c,R,M=state(w)
        assert delta(c)==dp(w)
        mask_cases+=1
        if n<=6:
            states.append((w,c,R,M))
        h=rr=F(0)
        cc=(0,0,0)
        for a in w:
            cp=inc(cc,a);d1=delta(cp)
            rr+=max(d1-delta(cc),0)-max(d1-h,0)
            h=min(max(h,d1),B(cp))
            cc=cp
            cap_steps+=1
        assert rr==R and h==min(M,B(c))

# Full finite-suffix predictions and bounded-horizon quotient at length <= 6.
future_predictions=ideal_update_steps=0
for word,c,R,M in states:
    for length in range(4):
        # finite-horizon exact reachable sup
        U=max(path_stats(c,''.join(t))[1] for n in range(length+1)
              for t in product(ACT,repeat=n))
        H=min(M,U)
        for t in product(ACT,repeat=length):
            v=''.join(t)
            P,S=path_stats(c,v)
            actual=R+P-max(S-M,0)
            # original and ideal-capped recurrences, with decreasing horizon at each step
            rr=R;rh=R;mm=M;hh=H;cc=c
            for k,a in enumerate(v):
                cp=inc(cc,a);dn=delta(cp)
                rr+=max(dn-delta(cc),0)-max(dn-mm,0)
                mm=max(mm,dn)
                rh+=max(dn-delta(cc),0)-max(dn-hh,0)
                left=length-k-1
                nextU=max(path_stats(cp,''.join(s))[1] for n in range(left+1)
                          for s in product(ACT,repeat=n))
                hh=min(max(hh,dn),nextU)
                cc=cp
                ideal_update_steps+=1
            assert rr==rh==actual
            future_predictions+=1

# Complete pair checks in the same (c,R) fiber, suffix horizon 3.
groups=defaultdict(list)
for w,c,R,M in states:
    groups[c,R].append((w,M))
pairs=equivalent=0
for (c,R),entries in groups.items():
    U=max(path_stats(c,''.join(t))[1] for n in range(4)
          for t in product(ACT,repeat=n))
    for i in range(len(entries)):
        for j in range(i+1,len(entries)):
            wi,m1=entries[i];wj,m2=entries[j]
            predicted=min(m1,U)==min(m2,U)
            actual=all(
                R+path_stats(c,''.join(t))[0]-max(path_stats(c,''.join(t))[1]-m1,0)
                ==
                R+path_stats(c,''.join(t))[0]-max(path_stats(c,''.join(t))[1]-m2,0)
                for n in range(4) for t in product(ACT,repeat=n))
            assert predicted==actual
            pairs+=1
            equivalent+=int(predicted)

# Strict reachable all-future compression certificate.
c1,r1,m1=state('0223')
c2,r2,m2=state('2203')
assert c1==c2==(1,2,1) and r1==r2==0
assert m1==F(8684,15625) and m2==F(69305833,125000000)
assert delta(c1)==F(6341504559,15625000000)
assert B(c1)==F(29981759,62500000)<m2<m1
suffix_witness=0
for n in range(7):
    for t in product(ACT,repeat=n):
        P,S=path_stats(c1,''.join(t))
        assert S<=B(c1)<m2
        assert r1+P-max(S-m1,0)==r2+P-max(S-m2,0)
        suffix_witness+=1

report={
 'status':'AUTHOR_SIDE_EXACT_FINITE_CHECKS_PASSED',
 'word_length_0_to_8_mask_DP':mask_cases,
 'B_capped_observer_steps':cap_steps,
 'word_length_0_to_6_future_predictions':future_predictions,
 'ideal_bounded_horizon_update_steps':ideal_update_steps,
 'same_count_residual_pairs':pairs,
 'finite_horizon_future_equivalent_pairs':equivalent,
 'witness_suffixes_length_0_to_6':suffix_witness,
 'strict_witness':{'prefixes':['0223','2203'],'counts':c1,
    'R':'0','M':list(map(str,(m1,m2))),'delta4':str(delta(c1)),
    'B_4':str(B(c1))},
 'caution':'Finite checks only; infinite theorem established in separate analytical proof. No native X6 transfer, independent Driver review or canonical admission.'
}
print(json.dumps(report,ensure_ascii=False,indent=2))
