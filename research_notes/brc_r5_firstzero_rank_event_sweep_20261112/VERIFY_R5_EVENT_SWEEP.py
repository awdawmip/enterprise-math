#!/usr/bin/env python3
"""Exact R5 rank-event sweep from immutable 15-atom (target0,source3) weights.

Uses the certified two-coordinate theorem from Draft PR #2139, commit
0db2aa81587b0ec7e70cfb7404cf016f70eeb8b5.
Does not recompute the 28-coordinate source reduction.
All comparisons and assertions use integer or Fraction arithmetic.
"""
from fractions import Fraction as F
from collections import Counter, defaultdict
from bisect import bisect_left

w=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
qset=(15,12,3)
x=F(155682221,25142124560000000)
E=F(9,115400000)
L=-F(427508577031693280,628800490619)
U=F(1,23)

# Signed subset-sum support by a shifted bitset.
B=-sum(min(v,0) for v in w)
C=sum(max(v,0) for v in w)
bits=1<<B
for v in w:
    bits|=bits<<v if v>0 else bits>>(-v)
N={B-i for i in range(B+C+1) if i<=B-3 and (bits>>i)&1}
assert (B,C,len(N),bits.bit_count(),min(N),max(N))==(1348,1348,1144,2293,3,1348)

# Independent complete finite 2^15-subset enumeration cross-check.
sumset={sum(w[i] for i in range(15) if mask&(1<<i))
        for mask in range(1<<15)}
assert {-h for h in sumset if h<=-3}==N
assert len(sumset)==bits.bit_count()

gates={q:(1-q*E/x)/23 for q in qset}
assert L<gates[15]<gates[12]<gates[3]<U
atlas=defaultdict(list)
for q in qset:
    for n in N:
        r=(1-F(36*q,n))/23
        assert gates[q]<r<U
        atlas[r].append((q,n))
assert len(atlas)==2905
multiplicities=Counter(len(pairs) for pairs in atlas.values())
assert multiplicities=={1:2603,2:77,3:225}
assert sum(k*v for k,v in multiplicities.items())==3432
assert all(g not in atlas for g in gates.values())

# Rational-coincidence pair intersections.
pair12=sum(k in N and 4*k in N for k in range(1,1350))
pair13=sum(k in N and 5*k in N for k in range(1,1350))
pair23=sum(4*k in N and 5*k in N for k in range(1,1350))
triple=sum(k in N and 4*k in N and 5*k in N for k in range(1,1350))
assert (pair12,pair13,pair23,triple)==(298,227,227,225)
pure_double=(pair12-triple,pair13-triple,pair23-triple)
assert pure_double==(73,2,2)

walls=sorted(set(atlas)|set(gates.values()))
assert len(walls)==2908
assert L<walls[0] and walls[-1]<U
assert len(walls)+1==2909

fixed_values=sorted(F(36)*x/n for n in N)
def active(r):
    return tuple(q for q in qset if gates[q]<r<U)
def open_rank(r,q):
    """One-indexed moving-value rank at a nonwall parameter."""
    assert q in active(r) and r not in atlas
    t=x*(1-23*r)/q
    j=bisect_left(fixed_values,t)
    assert j==sum(v<t for v in fixed_values)
    assert t not in fixed_values
    return 1+j+sum(q2>q for q2 in active(r))
def spectrum_count(r):
    return 1144+len(active(r))-len(atlas.get(r,()))

sectors=[("zero",L,gates[15],0,{}),
         ("one",gates[15],gates[12],1,{1:1}),
         ("two",gates[12],gates[3],2,{1:16,2:2}),
         ("three",gates[3],U,3,{1:2586,2:75,3:225})]
for name,a,b,num,expected in sectors:
    rows=[(r,pairs) for r,pairs in atlas.items() if a<r<b]
    assert Counter(len(pairs) for _,pairs in rows)==expected
    if rows:
        assert all(len(active(r))==num for r,_ in rows)
        assert all(spectrum_count(r)==1144+num-len(pairs)
                   for r,pairs in rows)

# Exact full ordered-label signatures on all 2909 open chambers.
signatures=set()
for i in range(len(walls)+1):
    a=L if i==0 else walls[i-1]
    b=U if i==len(walls) else walls[i]
    r=(a+b)/2
    active_q=active(r)
    moving=[(x*(1-23*r)/q,("M",q)) for q in active_q]
    ordered=tuple(label for _,label in sorted(
        [(F(36)*x/n,("F",n)) for n in N] + moving))
    assert len(ordered)==1144+len(active_q)
    assert len(ordered)==len(set(ordered))
    signatures.add(ordered)
assert len(signatures)==2909

assert atlas[F(0)]==[(15,540),(12,432),(3,108)]
assert (spectrum_count(L),spectrum_count(F(0)),spectrum_count(U))==(1144,1144,1144)

print("SUPPORT_BOUNDS", -B,C, "SUBSET_SUM_VALUES",bits.bit_count())
print("FIXED_N_VALUES",len(N))
print("GATES",*((q,str(gates[q])) for q in qset))
print("COLLISION_PAIRS",3432,"DISTINCT_COLLISION_WALLS",len(atlas))
print("MULTIPLICITIES",dict(sorted(multiplicities.items())))
print("PAIR_INTERSECTIONS_3_12_3_15_12_15",(pair12,pair13,pair23))
print("TRIPLES",triple,"PURE_DOUBLES_3_12_3_15_12_15",pure_double)
print("COLLISION_SECTORS",
      *((name,len([r for r in atlas if a<r<b])) for name,a,b,_,_ in sectors))
print("ACTIVATION_AND_COLLISION_WALLS",len(walls))
print("DIFFERENT_OPEN_ORDER_CHAMBERS",len(signatures))
print("ZERO_R_COLLISIONS",atlas[F(0)])
print("PASS_R5_EXACT_EVENT_SWEEP_2909_CHAMBERS")
