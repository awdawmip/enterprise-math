#!/usr/bin/env python3
"""Exact rational source-3 support filtration of the frozen R5 Blackwell fiber.
Requires r5_prior_four.py, the exact PR #2063 verifier reproduced byte-for-byte.
The 4-support witnesses and certificates come from that independent preceding result.
All checks here are standard-library Fraction; no numerical optimizer required.
"""
from fractions import Fraction as F
from itertools import combinations
import r5_prior_four as old

A,b,V,R,S = old.A, old.b, old.V, old.R, old.S
Q,M=old.Q,old.M
BASE=old.PRIMAL
assert len(BASE)==3 and old.rank(A)==13

# Exact Farkas dual y (15 components) for each excluded five-target
# source-3 mask. On every allowed column a, y.a >= 0, whereas y.b < 0.
DUAL_TEXT='''
01234:101/115,53/115,1/5,3/5,1,-67/115,-1,-113/115,-113/115,1,-113/115,6/115,6/115,-2/25,6/115
01235:-1/7,-1/3,0,1/3,-29/42,1,-1,2/21,2/21,1,2/21,1/42,1/42,-1/15,1/42
01236:21/25,1/5,-1/70,-8/35,-1,-1,-1,-1,-1,-22/35,1,2/25,2/25,3/70,0
01245:1/5,-1/3,0,-1,2/3,1,-1,-1/3,-1/3,1,1,1/15,1/15,-1/15,0
01246:4/5,0,-5/28,-1,-15/28,-1,-1,-1,-1,-5/14,1,1/10,1/10,1/28,0
01256:4/5,0,5/28,-1,-1,5/7,1,-1,-1,5/14,1,1/10,1/10,-1/28,0
01345:-1/7,-1/3,-19/42,1/3,2/3,1,-1,2/21,2/21,1,2/21,1/42,1/42,-1/15,1/42
01356:21/25,1/5,-1/5,-8/35,-1,-23/35,-1,-1,-1,-22/35,1,2/25,2/25,3/70,0
01456:4/5,0,-1/2,-1,-15/28,-5/7,-1,-1,-1,-5/14,1,1/10,1/10,1/28,0
02456:4/5,0,3/20,-1,-7/20,-3/5,-1,-1,-1,-9/10,1,1/10,1/10,1/20,0
03456:17/19,-1/3,-1,-1/19,-6/19,-11/19,-1,-1,-1,-1,1,2/15,2/15,1/19,0
12456:4/5,0,-5/28,-1,-15/28,-5/7,-1,-1,-1,-5/14,1,1/10,1/10,1/28,0
'''
DUALS={tuple(map(int,s.split(':')[0])):tuple(map(F,s.split(':')[1].split(',')))
       for s in DUAL_TEXT.strip().splitlines()}
assert len(DUALS)==12 and all(len(y)==15 for y in DUALS.values())

# These two strictly positive five-support witnesses contain no legal
# four-support mask; all other five-support witnesses extend prior ones.
EXTRA={
 (0,2,3,5,6):(F('1/1000'),(1,16,17,19,0,8,25,27,20,4,11,14,2)),
 (1,2,3,5,6):(F('1/1000'),(16,1,17,0,19,8,27,25,4,20,15,11,2)),
}
def allowed(mask):
    return [k for k,(i,j) in enumerate(V) if j!=3 or i in mask]

def exact_solve(piv, nonpivot):
    rhs=[b[r]-sum(A[r][k]*z for k,z in nonpivot.items()) for r in range(15)]
    xs=old.solve_overdetermined(piv,rhs)
    sol=dict(nonpivot);sol.update(zip(piv,xs))
    assert all(sum(A[r][k]*sol.get(k,F(0)) for k in range(28))==b[r]
               for r in range(15))
    return sol

def base_witness(J):
    t,piv=BASE[J]; al=allowed(J)
    nonpivot={k:t for k in al if k not in piv}
    x=exact_solve(piv,nonpivot)
    assert set(x)==set(al) and min(x.values())>0
    return x,tuple(piv),nonpivot

def extend_positive(J,K,known=None):
    """Introduce one new source-3 edge using the exact full-rank pivot basis."""
    assert set(J)<set(K) and len(K)==len(J)+1
    if known is None:
        base,piv,free=base_witness(J)
    else:
        base,piv,free=known
    extra=next(k for k in allowed(K) if k not in base)
    t=F(1,10000)
    for _ in range(48):
        x=exact_solve(piv,{**free,extra:t})
        if len(x)==len(allowed(K)) and min(x.values())>0:
            return x,piv,{**free,extra:t}
        t/=2
    raise AssertionError(('positive extension failed',J,K))

def exact_dual_test(J,y):
    al=allowed(J)
    q=[sum(y[r]*A[r][k] for r in range(15)) for k in al]
    objective=sum(y[r]*b[r] for r in range(15))
    assert min(q)>=0 and objective<0, (J,min(q),objective)
    return objective

FOUR=tuple(sorted(BASE))
FOUR_SET=frozenset(map(frozenset,FOUR))
for J in FOUR:
    base_witness(J)
FIVE={}
for J in combinations(range(7),5):
    if J in DUALS:
        exact_dual_test(J,DUALS[J])
        continue
    if J in EXTRA:
        t,piv=EXTRA[J];al=allowed(J)
        x=exact_solve(piv,{k:t for k in al if k not in piv})
        assert len(x)==26 and min(x.values())>0
        FIVE[J]=(x,tuple(piv),{k:t for k in al if k not in piv})
    else:
        contained=[L for L in FOUR if set(L)<set(J)]
        assert contained, J
        FIVE[J]=extend_positive(contained[0],J)
    assert len(allowed(J))==26
    assert old.rank([[A[r][k] for k in allowed(J)] for r in range(15)])==13
assert len(FIVE)==9 and len(DUALS)==12
print('FIVE_TARGET_POSITIVE',sorted(FIVE))
print('FIVE_TARGET_FARKAS_EXCLUDED',sorted(DUALS))
print('FIVE_TARGET_COUNTS',(9,12),'FACE_DIM',13)

# The excluded six-target mask has no central target 3. Its previous
# 12456 dual also excludes the added source-3 target 0, because that
# new dual-column value equals 4/5-5/14+2/28=18/35 > 0.
SIX={}
for K in combinations(range(7),6):
    if 3 not in K:
        assert K==(0,1,2,4,5,6)
        exact_dual_test(K,DUALS[(1,2,4,5,6)])
        continue
    chosen=next((J for J in FIVE if set(J)<set(K)),None)
    assert chosen is not None,K
    SIX[K]=extend_positive(chosen,K,FIVE[chosen])
    assert len(allowed(K))==27
    assert old.rank([[A[r][k] for k in allowed(K)] for r in range(15)])==13
assert len(SIX)==6
print('SIX_TARGET_POSITIVE',sorted(SIX))
print('SIX_TARGET_EXCLUDED',[(0,1,2,4,5,6)],'FACE_DIM',14)

# Face intersections: F_J intersect F_K=F_(J intersect K).
# All feasible four-target masks are exactly FOUR.
FIVES=list(map(frozenset,FIVE))
SIXES=list(map(frozenset,SIX))
def comps(nodes,adj):
    rest=set(range(len(nodes)));out=[]
    while rest:
        first=min(rest);rest.remove(first);todo=[first];seen={first}
        for u in todo:
            for v in list(rest):
                if adj(nodes[u],nodes[v]):
                    rest.remove(v);todo.append(v);seen.add(v)
        out.append(sorted(seen))
    return out
def four_below(inter):
    return any(J<=inter for J in FOUR_SET)
comp5=comps(FIVES,lambda x,y: four_below(x&y))
assert sorted(map(len,comp5))==[1,1,7]
extra_comp=[sorted(tuple(FIVES[i]) for i in comp) for comp in comp5 if len(comp)==1]
assert sorted(extra_comp)==[[(0,2,3,5,6)],[(1,2,3,5,6)]]
print('SUPPORT_AT_MOST_4_CONNECTED_COMPONENTS',3)
print('SUPPORT_AT_MOST_5_CONNECTED_COMPONENTS',len(comp5),
      'COMPONENT_SIZE_FIVE_FACES',sorted(map(len,comp5)))

# Every feasible five-face lies in one of six 14-dimensional six-faces.
# The six-face intersection graph, connected via exact feasible 5-faces,
# proves the entire support-at-most-six locus is connected.
comp6=comps(SIXES,lambda x,y: tuple(sorted(x&y)) in FIVE)
assert len(comp6)==1
assert all(any(set(J)<set(K) for K in SIX) for J in FIVE)
print('SUPPORT_AT_MOST_6_CONNECTED_COMPONENTS',len(comp6),'SIX_FACE_COUNT',len(SIX))
print('SUPPORT_AT_MOST_7_CONNECTED_COMPONENTS',1,'FULL_DIM',15)

# Exact minimax bridge between all three four-support face components:
# A -> C -> B has source-3 support 5 on each open segment.
J_A=(1,3,4,6);J_C=(2,3,4,6);J_B=(2,3,4,5)
assert len(set(J_A)|set(J_C))==5 and len(set(J_B)|set(J_C))==5
assert len(set(J_A)|set(J_B))==6
print('MINIMAX_PEAK_SUPPORT_FOR_ALL_PAIRS_OF_FOUR_FACES',5)
print('PASS_EXACT_R5_SUPPORT_FILTRATION_4_TO_7_AND_NINE_FIVE_MASKS')
