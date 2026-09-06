#!/usr/bin/env python3
"""Exact finite checks for signed X6 triadic decomposition BRC V2."""
from itertools import combinations, product
from functools import lru_cache
from collections import Counter
from math import comb, factorial

AXES=range(6)
TRIPLES=tuple(combinations(AXES,3))
SIGNED_TYPES=tuple(
    tuple((i,signs[r]) for r,i in enumerate(S))
    for S in TRIPLES
    for signs in product((-1,1),repeat=3)
)
assert len(TRIPLES)==20
assert len(SIGNED_TYPES)==160


def ordered_underlying_count(D):
    D=tuple(D); total=sum(D)
    if total%3: return 0
    m=total//3
    states={(0,0,0,0,0,0):1}
    for _ in range(m):
        nxt={}
        for state,count in states.items():
            for S in TRIPLES:
                t=list(state); ok=True
                for i in S:
                    t[i]+=1
                    if t[i]>D[i]: ok=False; break
                if ok:
                    t=tuple(t); nxt[t]=nxt.get(t,0)+count
        states=nxt
    return states.get(D,0)


def greedy_decompose(D):
    D=list(D); total=sum(D)
    if total%3: return None
    m=total//3
    if m==0: return ()
    if max(D)>m: return None
    out=[]
    for remaining in range(m,0,-1):
        P=[i for i,d in enumerate(D) if d==remaining]
        assert len(P)<=3
        S=list(P)
        for i in sorted(range(6),key=lambda i:(-D[i],i)):
            if len(S)==3: break
            if D[i]>0 and i not in S: S.append(i)
        if len(S)!=3: return None
        S=tuple(sorted(S)); out.append(S)
        for i in S: D[i]-=1
        if max(D,default=0)>remaining-1: return None
    return tuple(out) if all(d==0 for d in D) else None


@lru_cache(None)
def brute_possible(D):
    D=tuple(D)
    if sum(D)==0: return True
    if sum(D)%3: return False
    for S in TRIPLES:
        if all(D[i]>0 for i in S):
            d=list(D)
            for i in S: d[i]-=1
            if brute_possible(tuple(d)): return True
    return False

# Existence theorem: sum=3m and max<=m, independently checked through m<=4.
existence_checks=0
for m in range(5):
    for D in product(range(m+1),repeat=6):
        if sum(D)!=3*m: continue
        criterion=(max(D,default=0)<=m)
        assert (greedy_decompose(D) is not None)==criterion
        assert brute_possible(tuple(D))==criterion
        existence_checks+=1


def signed_vector(tau):
    # order per axis: (+,-)
    out=[0]*12
    for i,s in tau:
        out[2*i+(0 if s==1 else 1)]+=1
    return tuple(out)

def add(a,b): return tuple(x+y for x,y in zip(a,b))

def formula_signed_ordered(d):
    D=tuple(d[2*i]+d[2*i+1] for i in AXES)
    n=ordered_underlying_count(D)
    for i in AXES: n*=comb(D[i],d[2*i])
    return n

# Exhaustive signed ordered branch census for one and two triadic events.
observed={signed_vector(t):1 for t in SIGNED_TYPES}
for d,count in observed.items(): assert count==formula_signed_ordered(d)==1
states=Counter()
for a in SIGNED_TYPES:
    va=signed_vector(a)
    for b in SIGNED_TYPES:
        states[add(va,signed_vector(b))]+=1
for d,count in states.items(): assert count==formula_signed_ordered(d)
signed_formula_checks=len(observed)+len(states)

# If individual force quanta are labeled, a fixed ordered underlying type sequence
# has prod_i D_i! assignments. Verify against sign-binomial times within-sign labels.
for d in list(states)[:500]:
    D=tuple(d[2*i]+d[2*i+1] for i in AXES)
    sign_and_labels=1
    for i in AXES:
        sign_and_labels*=comb(D[i],d[2*i])*factorial(d[2*i])*factorial(d[2*i+1])
    assert sign_and_labels==__import__('math').prod(factorial(x) for x in D)

# Unordered underlying triad decomposition counts via nondecreasing type recursion.
def unordered_underlying_count(D):
    D=tuple(D)
    @lru_cache(None)
    def rec(rem,start):
        if sum(rem)==0: return 1
        ans=0
        for k in range(start,len(TRIPLES)):
            S=TRIPLES[k]
            if all(rem[i]>0 for i in S):
                rr=list(rem)
                for i in S: rr[i]-=1
                ans+=rec(tuple(rr),k)
        return ans
    return rec(D,0)
assert unordered_underlying_count((1,1,1,1,1,1))==10
assert ordered_underlying_count((1,1,1,1,1,1))==20
assert unordered_underlying_count((2,2,2,2,2,2))==85
assert ordered_underlying_count((2,2,2,2,2,2))==1860

# Factorized signed-axis weights cannot distinguish decomposition branches with
# the same signed degree vector: every branch uses exactly those token counts.
weights=tuple(range(2,14)) # exact positive integer dummy weights for 12 signed dirs
for d in list(states)[:500]:
    common=1
    for j,n in enumerate(d): common*=weights[j]**n
    assert common>0
    # weighted ordered total therefore equals count * common factor
    assert states[d]*common==formula_signed_ordered(d)*common

print('PASS_X6_TRIADIC_DECOMPOSITION_BRC_V2')
print('atomic_unsigned_triad_types',len(TRIPLES))
print('atomic_signed_triad_types',len(SIGNED_TYPES))
print('existence_degree_sequences_checked',existence_checks)
print('signed_ordered_formula_states_checked',signed_formula_checks)
print('uniform_D1_ordered_unordered',(20,10))
print('uniform_D2_ordered_unordered',(1860,85))
print('factorized_axis_weights_select_decomposition',False)
