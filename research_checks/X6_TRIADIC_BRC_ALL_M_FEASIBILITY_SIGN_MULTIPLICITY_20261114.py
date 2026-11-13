#!/usr/bin/env python3
"""Exact independent checks for X6 signed triadic-event feasibility and BRC multiplicities.
Frozen mathematical source: experiments/x6_triadic_decomposition_brc_v2_20260906/
check_triadic_decomposition_brc.py (Git blob 5d0f2cb88a0d4e437b5025e9050e3044f7831cd4).
The universal theorems are proved in the companion note; this is finite corroboration.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, product
from math import comb, factorial, prod

TRIPLES = tuple(combinations(range(6), 3))
SIGNED = tuple(
    tuple((i, signs[j]) for j, i in enumerate(S))
    for S in TRIPLES for signs in product((-1, 1), repeat=3)
)

def greedy(D):
    D = list(D)
    if sum(D) % 3: return None
    m = sum(D) // 3
    if any(x < 0 for x in D) or max(D, default=0)>m: return None
    out = []
    for r in range(m, 0, -1):
        S = [i for i in range(6) if D[i] == r]
        for i in sorted(range(6), key=lambda i:(-D[i], i)):
            if len(S)==3: break
            if D[i]>0 and i not in S: S.append(i)
        if len(S)!=3: return None
        S = tuple(sorted(S))
        out.append(S)
        for i in S: D[i]-=1
        if max(D)>r-1: return None
    return tuple(out) if all(x==0 for x in D) else None

def candidates(m):
    def rec(k, remainder, prefix):
        if k == 6:
            if remainder == 0: yield prefix
            return
        for n in range(min(m, remainder)+1):
            yield from rec(k+1, remainder-n, prefix+(n,))
    yield from rec(0, 3*m, ())

@lru_cache(None)
def ordered_underlying(D):
    if sum(D)==0: return 1
    answer=0
    for S in TRIPLES:
        if all(D[i]>0 for i in S):
            rem=list(D)
            for i in S: rem[i]-=1
            answer+=ordered_underlying(tuple(rem))
    return answer

def signed_degree(tau):
    d=[0]*12
    for i,sign in tau: d[2*i+(0 if sign==1 else 1)]+=1
    return tuple(d)

def theoretical_count(d):
    D=tuple(d[2*i]+d[2*i+1] for i in range(6))
    n=ordered_underlying(D)
    for i in range(6): n*=comb(D[i], d[2*i])
    return n

def independent_uniform_multiset(m, count_per_axis):
    total=0; multi=0
    for ks in combinations_with_replacement(range(20),m):
        D=[0]*6
        for k in ks:
            for i in TRIPLES[k]: D[i]+=1
        if D == [count_per_axis]*6:
            multi+=1
            multiplicities=Counter(ks).values()
            total+=factorial(m)//prod(factorial(c) for c in multiplicities)
    return multi,total

def main():
    counts=[]
    for m in range(7):
        total=0
        for D in candidates(m):
            triads=greedy(D)
            assert triads is not None and len(triads)==m
            actual=tuple(sum(i in S for S in triads) for i in range(6))
            assert actual==D
            total+=1
        counts.append(total)
    assert counts==[1,20,141,580,1751,4332,9331]

    sign_types=[signed_degree(t) for t in SIGNED]
    states=Counter({(0,)*12:1})
    signed_details=[]
    for m in range(1,4):
        nxt=Counter()
        for d,count in states.items():
            for v in sign_types:
                nxt[tuple(a+b for a,b in zip(d,v))]+=count
        states=nxt
        assert sum(states.values())==160**m
        for d,count in states.items():
            assert count==theoretical_count(d)
        signed_details.append((m,len(states),sum(states.values())))
    assert signed_details==[(1,160,160),(2,5284,25600),(3,73580,4096000)]

    independent4=independent_uniform_multiset(4,2)
    independent6=independent_uniform_multiset(6,3)
    assert independent4==(85,1860)
    assert independent6==(550,297200)
    D=(3,)*6
    assert ordered_underlying(D)==independent6[1]
    fixed_sign_factor=prod(comb(3,2) for _ in range(6))
    assert fixed_sign_factor==729
    assert ordered_underlying(D)*fixed_sign_factor==216658800

    print("PASS_X6_TRIADIC_BRC_ALL_M_PROOF_CORROBORATION")
    print("admissible_degree_vectors_m0_to_6",counts)
    print("signed_degree_census_m1_to_3",signed_details)
    print("uniform_degree_two_m4",independent4)
    print("uniform_degree_three_m6",independent6)
    print("fixed_signed_degree_m6",216658800)
    print("arithmetic=exact_integers; coverage=finite; universal_proof=separate")

if __name__=="__main__":
    main()
