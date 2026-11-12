#!/usr/bin/env python3
"""Exact two-coordinate collision witnesses in the frozen 28-coordinate R5 auxiliary model.

No floating-point calculations, third-party packages, or repository-runtime imports.
The immutable original 15-atom fixture is enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551.
Atom vectors below are 36 times the physical residual operation vectors.
"""
from fractions import Fraction as Q
from collections import Counter, defaultdict
from functools import lru_cache

R = (2, 10, 15, 20, 25, 30, 38)
W = (336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
XS = (
 "250555781039/3397584400000,854053219229681/5470110884000000,"
 "155682221/156288882400000,1/800000,1/800000,19487331497/781444412000000,"
 "1001314300627/47566181600000,1/800000,6101786845061/95132363200000,"
 "19640941861/6795168800000,1/800000,1/800000,1/800000,1326387507069/95132363200000,"
 "155682221/25142124560000000,155682221/25142124560000000,"
 "969901373288483/5782688648800000,1627075388860003/11721666180000000,"
 "14139282599219/169879220000000,165067666637733/7814444120000000,"
 "1696529496568917/144567216220000000,31271973479/25142124560000000,"
 "12993863727852929/4047882054160000000,7517305745629/5782688648800000,"
 "36686587724849/3907222060000000,1308842702731/169879220000000,"
 "331925821992147/7814444120000000,54684907960963337/2023941027080000000"
)
X = tuple(map(Q, XS.split(',')))
V = tuple((i,j) for j in (1,2,3,5) for i in range(7))
IX = {p:k for k,p in enumerate(V)}
COEFF = {1:(12,8,1,13,8), 2:(3,13,7,4,2), 5:(-15,-21,-8,-17,-10)}
atoms = []
for j in (1,2,5):
    for i in range(1,6):
        b = [0]*7
        b[0], b[i], b[6] = R[i]-R[6], R[6]-R[0], R[0]-R[i]
        d = [0]*28
        for k,t in enumerate(b):
            d[IX[(k,j)]] += t*COEFF[j][i-1]
            d[IX[(k,3)]] -= t*COEFF[j][i-1]
        atoms.append(tuple(d))
assert len(X)==28 and len(atoms)==15
k0, k1 = IX[(0,3)], IX[(1,3)]
x = X[k0]
H = [0]*28
for i,v in ((1,-23),(2,28),(6,-5)):
    H[IX[(i,3)]] += v
    H[IX[(i,1)]] -= v
assert X[k1]==x and H[k1]==-23
assert tuple(a[k0] for a in atoms)==W
assert tuple(a[k1] for a in atoms)==(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
L = -Q(427508577031693280,628800490619)
U = Q(1,23)
E = Q(9,115400000)
assert all(X[k]+r*x*H[k]>=0 for r in (L,U) for k in range(28))
P = [(0,)*28]*(1<<15)
for m in range(1,1<<15):
    bit = m & -m
    j = bit.bit_length()-1
    old = P[m ^ bit]
    P[m] = tuple(old[k]+atoms[j][k] for k in range(28))
N = {-p[k0] for p in P if p[k0]<=-3}
assert (len(N),min(N),max(N))==(1144,3,1348)

# A pair (q,n) collides at r=(1-36q/n)/23.
# A *single* mask vanishes in both coordinates iff P[k0]=-n, P[k1]=-36q.
qset = (15,12,3)
candidate = {q:defaultdict(list) for q in qset}
for m in range(1,1<<15):
    n = -P[m][k0]
    if n not in N:
        continue
    for q in qset:
        if P[m][k1]==-36*q:
            candidate[q][n].append(m)

expected = {15:(229,504),12:(298,749),3:(538,1682)}
total_pairs=0
total_masks=0
for q in qset:
    buckets = candidate[q]
    distribution = Counter()
    verified_masks = 0
    cache_states = 0
    for n,masks in sorted(buckets.items()):
        r = (1-Q(36*q,n))/23
        eps = 36*x/n
        assert L<r<U and 0<eps<E
        base = tuple(X[k]+r*x*H[k] for k in range(28))
        @lru_cache(None)
        def allowed(mask):
            return all(base[k]+x*P[mask][k]/n>=0 for k in range(28))
        @lru_cache(None)
        def path(mask):
            if mask==0:
                return ()
            if not allowed(mask):
                return None
            for j in range(15):
                bit = 1<<j
                if mask&bit:
                    prior=path(mask ^ bit)
                    if prior is not None:
                        return prior+(j,)
            return None
        shortest=99
        for mask in masks:
            assert allowed(mask)
            order=path(mask)
            assert order is not None and len(order)==mask.bit_count()
            seen=0
            for j in order:
                assert not (seen & (1<<j))
                seen|=1<<j
                assert allowed(seen) # independently checked every constructed prefix
            assert seen==mask
            assert base[k0]+x*P[mask][k0]/n==0
            assert base[k1]+x*P[mask][k1]/n==0
            verified_masks+=1
            shortest=min(shortest,len(order))
        distribution[shortest]+=1
        cache_states+=allowed.cache_info().currsize
    assert (len(buckets),verified_masks)==expected[q]
    total_pairs+=len(buckets);total_masks+=verified_masks
    print("Q",q,"DUAL_ZERO_PAIRS",len(buckets),
          "DUAL_ZERO_ORDERABLE_MASKS",verified_masks,
          "MIN_STEPS",dict(sorted(distribution.items())),
          "VALIDATED_PREFIX_STATES",cache_states)
assert (total_pairs,total_masks)==(1065,2935)
assert (3432-total_pairs)==2367
assert 540 not in candidate[15]
assert 432 in candidate[12] and 108 in candidate[3]
# Explicit hand-checkable 0-parameter witnesses (1-based labels):
for q,n,order in ((12,432,(15,14,10,1,12)),(3,108,(15,6,4,3,2,12))):
    seen=0
    for a in order:
        seen|=1<<(a-1)
        assert all(X[k]+x*P[seen][k]/n>=0 for k in range(28))
    assert (P[seen][k0],P[seen][k1])==(-n,-36*q)
print("COLLISION_PAIRS",3432,"DUAL_ZERO_PAIR_EVENTS",total_pairs,
      "DUAL_ZERO_IMPOSSIBLE_EVENTS",2367)
print("PASS_R5_EXACT_DUAL_ZERO_COLLISION_CENSUS")
