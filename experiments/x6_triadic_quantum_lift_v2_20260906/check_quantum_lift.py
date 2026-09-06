#!/usr/bin/env python3
from functools import lru_cache
from itertools import combinations, product
from math import ceil

TRIPLES=tuple(combinations(range(6),3))

def decomposable(d):
    S=sum(d)
    return S%3==0 and max(d,default=0)<=S//3

@lru_cache(None)
def brute(d):
    d=tuple(d)
    if sum(d)==0: return True
    if sum(d)%3: return False
    for T in TRIPLES:
        if all(d[i]>0 for i in T):
            e=list(d)
            for i in T: e[i]-=1
            if brute(tuple(e)): return True
    return False

def defect(d):
    S=sum(d); M=max(d,default=0)
    m=max(M,ceil(S/3) if S else 0)
    return 3*m-S

def augment_greedy(d):
    d=list(d); S=sum(d); M=max(d,default=0)
    m=max(M,ceil(S/3) if S else 0); h=3*m-S
    out=d[:]
    for _ in range(h):
        i=next(i for i,x in enumerate(out) if x<m)
        out[i]+=1
    return tuple(out)

# Exhaustive small full-degree regression.
full_cases=0
for d in product(range(4), repeat=6):
    aug=augment_greedy(d)
    assert sum(aug)-sum(d)==defect(d)
    assert decomposable(aug)
    assert brute(aug)
    if defect(d)==0:
        assert decomposable(d)==brute(d)==True
    full_cases+=1

# Hidden-only completions for q<=3 visible axes. Brute-check minimal hidden cost
# for small visible degree vectors by enumerating hidden additions.
def hidden_formula(vis):
    if not vis or max(vis)==0: return 0
    M=max(vis); return 3*M-sum(vis)

def hidden_brute(vis):
    q=len(vis); hidden=6-q
    for h in range(30):
        for xs in product(range(h+1), repeat=hidden):
            if sum(xs)!=h: continue
            d=tuple(vis)+tuple(xs)
            if decomposable(d): return h
    raise AssertionError('search bound')

hidden_cases=0
for q in (1,2,3):
    for vis in product(range(1,4), repeat=q):
        assert hidden_formula(vis)==hidden_brute(vis)
        hidden_cases+=1

# Two-force hidden-axis family count theorem.
for a in range(1,8):
    for b in range(1,8):
        M=max(a,b); m=min(a,b); h=2*M-m
        assert h==hidden_formula((a,b))
        min_families=(h+M-1)//M
        assert min_families==(1 if a==b else 2)

# Three-force no-hidden closure iff equal multiplicity.
for a,b,c in product(range(1,6), repeat=3):
    h=hidden_formula((a,b,c))
    assert (h==0)==(a==b==c)
    if h:
        assert (h+max(a,b,c)-1)//max(a,b,c) in (1,2)

print('PASS_X6_TRIADIC_QUANTUM_LIFT_V2')
print('full_degree_vectors_checked',full_cases)
print('hidden_visible_cases_checked',hidden_cases)
print('two_force_equal_hidden_axis_families',1)
print('two_force_unequal_hidden_axis_families',2)
print('three_visible_no_hidden_iff_equal',True)
print('continuous_force_magnitude_defined',False)
