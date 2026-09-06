#!/usr/bin/env python3
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product

V=tuple(range(6))
PAIRS=tuple(combinations(V,2))
TRIPLES=tuple(combinations(V,3))
PAIR_INDEX={p:i for i,p in enumerate(PAIRS)}
TRIPLE_INDEX={t:i for i,t in enumerate(TRIPLES)}

P=[[1 if set(e).issubset(S) else 0 for S in TRIPLES] for e in PAIRS]


def rank_q(M):
    A=[[Fraction(x) for x in row] for row in M]
    if not A: return 0
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        pivot=next((i for i in range(r,m) if A[i][c]),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        pv=A[r][c]
        A[r]=[x/pv for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c]
                A[i]=[x-f*y for x,y in zip(A[i],A[r])]
        r+=1
        if r==m: break
    return r


def det_int(M):
    A=[[Fraction(x) for x in row] for row in M]
    n=len(A); out=Fraction(1); sign=1
    for c in range(n):
        pivot=next((i for i in range(c,n) if A[i][c]),None)
        if pivot is None: return 0
        if pivot!=c:
            A[c],A[pivot]=A[pivot],A[c]; sign*=-1
        pv=A[c][c]; out*=pv
        for i in range(c+1,n):
            if A[i][c]:
                f=A[i][c]/pv
                for j in range(c,n): A[i][j]-=f*A[c][j]
    assert out.denominator==1
    return sign*out.numerator


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]


def transpose(A): return [list(x) for x in zip(*A)]

assert len(PAIRS)==15 and len(TRIPLES)==20
assert rank_q(P)==15
G=matmul(P,transpose(P))
assert det_int(G)==12*(6**5)*(2**9)


def perfect_matchings(items):
    items=tuple(items)
    if not items:
        yield (); return
    a=items[0]
    for idx in range(1,len(items)):
        b=items[idx]
        rest=items[1:idx]+items[idx+1:]
        for tail in perfect_matchings(rest):
            yield tuple(sorted(((min(a,b),max(a,b)),)+tail))

MATCHINGS=tuple(sorted(set(perfect_matchings(V))))
assert len(MATCHINGS)==15


def trade_vector(M):
    # M is three ordered pairs; choose first/second endpoint in each pair.
    plus=[]; minus=[]
    for bits in product((0,1),repeat=3):
        S=tuple(sorted(M[r][bits[r]] for r in range(3)))
        (plus if sum(bits)%2==0 else minus).append(S)
    v=[0]*20
    for S in plus: v[TRIPLE_INDEX[S]]+=1
    for S in minus: v[TRIPLE_INDEX[S]]-=1
    return tuple(v),tuple(plus),tuple(minus)

TRADES=[]
for M in MATCHINGS:
    v,plus,minus=trade_vector(M)
    assert sum(x*x for x in v)==8
    # pair shadow zero
    assert all(sum(P[e][s]*v[s] for s in range(20))==0 for e in range(15))
    assert len(plus)==len(minus)==4
    TRADES.append(v)

assert rank_q([list(v) for v in TRADES])==5

# Explicit saturated integer kernel basis from exact elimination. The five pivot
# triple rows are identity, so any integer kernel vector has integer coordinates.
B=[
[0,0,0,0,-1], [0,0,0,-1,0], [0,0,-1,0,0], [0,0,1,1,1],
[0,-1,0,0,0], [-1,0,0,0,0], [1,1,0,0,1], [1,1,1,1,1],
[-1,0,-1,0,-1], [0,-1,0,-1,-1], [0,1,0,1,1], [1,0,1,0,1],
[-1,-1,-1,-1,-1], [-1,-1,0,0,-1], [1,0,0,0,0], [0,1,0,0,0],
[0,0,-1,-1,-1], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]
]
assert rank_q(B)==5
assert matmul(P,B)==[[0]*5 for _ in range(15)]
PIVOTS=(14,15,17,18,19)
assert [[B[r][c] for c in range(5)] for r in PIVOTS]==[[1 if i==j else 0 for j in range(5)] for i in range(5)]

# Find a unimodular 5-subset of elementary trades in saturated kernel coordinates.
trade_coords=[[v[r] for r in PIVOTS] for v in TRADES]
unimodular=None
for inds in combinations(range(15),5):
    minor=[trade_coords[i] for i in inds]
    d=det_int(minor)
    if abs(d)==1:
        unimodular=(inds,d); break
assert unimodular is not None

# Minimal multiset collision census.
def shadow(ms):
    out=[0]*15
    for ti in ms:
        for e in range(15): out[e]+=P[e][ti]
    return tuple(out)

for m in (1,2,3):
    seen={}
    for ms in combinations_with_replacement(range(20),m):
        sh=shadow(ms)
        assert sh not in seen
        seen[sh]=ms

groups=defaultdict(list)
for ms in combinations_with_replacement(range(20),4): groups[shadow(ms)].append(ms)
ambiguous=[(sh,grp) for sh,grp in groups.items() if len(grp)>1]
assert len(ambiguous)==15
assert all(len(grp)==2 for _,grp in ambiguous)

# Every minimal ambiguous shadow is K6 minus one perfect matching, and each matching occurs once.
zero_matchings=[]
for sh,grp in ambiguous:
    assert set(sh)<= {0,1}
    assert sum(sh)==12
    zeros=tuple(PAIRS[i] for i,x in enumerate(sh) if x==0)
    assert len(zeros)==3
    flat=[v for e in zeros for v in e]
    assert sorted(flat)==list(V)
    zero_matchings.append(tuple(sorted(zeros)))
    # both branches have D=(2,...,2)
    for ms in grp:
        D=[0]*6
        for ti in ms:
            for v in TRIPLES[ti]: D[v]+=1
        assert tuple(D)==(2,2,2,2,2,2)
assert set(zero_matchings)==set(MATCHINGS)

# Tight-frame projector F = sum v v^T; exact identity F^2=24F and rank 5.
F=[[sum(v[i]*v[j] for v in TRADES) for j in range(20)] for i in range(20)]
F2=matmul(F,F)
assert F2==[[24*x for x in row] for row in F]
assert rank_q(F)==5
# image is in ker(P)
assert matmul(P,F)==[[0]*20 for _ in range(15)]

# Pair-factorized additive weights annihilate all trade contrasts.
for lam in (
    tuple(range(15)),
    tuple((-1)**i*(i+1) for i in range(15)),
):
    theta=[sum(P[e][s]*lam[e] for e in range(15)) for s in range(20)]
    assert all(sum(v[s]*theta[s] for s in range(20))==0 for v in TRADES)

print('PASS_X6_TRIADIC_INTERACTION_DEFECT_V18')
print('pair_shadow_rank',rank_q(P))
print('pure_triadic_dimension',20-rank_q(P))
print('perfect_matching_trades',len(TRADES))
print('first_collision_event_count',4)
print('minimal_ambiguous_pair_shadows',len(ambiguous))
print('integer_kernel_generated_by_trades',True)
print('tight_frame_constant',24)
print('pairwise_route_selector_complete',False)
