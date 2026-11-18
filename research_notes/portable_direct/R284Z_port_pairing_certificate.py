#!/usr/bin/env python3
"""Independent exact verification of R284Z Port two-terminal path-pairing identity.
Finite examples are checks, not a general proof. Only Python standard library.
"""
from fractions import Fraction as F
from itertools import permutations
from random import Random
import json


def det(a):
    n = len(a)
    if n == 0:
        return F(1)
    total = F(0)
    for perm in permutations(range(n)):
        inv = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        p = F(-1 if inv % 2 else 1)
        for i,j in enumerate(perm):
            p *= a[i][j]
        total += p
    return total


def minor_M(W, rr, cc):
    return [[F(i == j)-W[i][j] for j in cc] for i in rr]


def paths(W, start, stop, inner):
    # Every permitted directed path has only inner vertices before its final stop.
    def dfs(u, used, weight):
        if W[u][stop]:
            yield (used, weight*W[u][stop], (u, stop))
        for v in inner:
            if v not in used and W[u][v]:
                for visited, wt, trace in dfs(v, used+(v,), weight*W[u][v]):
                    yield visited, wt, (u,)+trace
    return list(dfs(start, (), F(1)))


def matching_present(A):
    n=len(A)
    return any(all(A[i][j] != 0 for i,j in enumerate(perm)) for perm in permutations(range(n)))


def check(W, S, P, Q):
    rr=S+P
    cc=S+Q
    A=minor_M(W,rr,cc)
    lhs=det(A)
    families=[[],[]]
    pairings=[(0,1),(1,0)]
    value=F(0)
    for pairing_idx,perm in enumerate(pairings):
        local=[]
        for first in paths(W,P[0],Q[perm[0]],S):
            for second in paths(W,P[1],Q[perm[1]],S):
                if not set(first[0]).isdisjoint(second[0]):
                    continue
                active=set(first[0])|set(second[0]); left=[s for s in S if s not in active]
                term=first[1]*second[1]*det(minor_M(W,left,left))
                value+= (1 if pairing_idx==0 else -1)*term
                local.append((first[2],second[2],term))
        families[pairing_idx]=local
    assert lhs == value, (lhs,value,S,P,Q)
    assert matching_present(A) == bool(families[0] or families[1])
    if not families[0]:
        assert lhs <= 0
        if families[1]: assert lhs<0
    if not families[1]:
        assert lhs >= 0
        if families[0]: assert lhs>0
    return lhs, families


def make(n_inner, rng):
    n=n_inner+4
    P=[0,1];S=list(range(2,2+n_inner));Q=[n-2,n-1]
    W=[[F(0) for _ in range(n)] for _ in range(n)]
    for u in P+S:
        for v in S+Q:
            if u in P and v in P: continue
            if rng.random()<0.53:
                W[u][v]=F(rng.randint(1,3),32)
    assert all(sum(row)<1 for row in W)
    return W,S,P,Q


def main():
    rng=Random(28426)
    report={"schema":"R284Z_EXACT_PORT_PAIRING_CHECK_V1", "seed":28426,"cases":0,
            "cases_by_internal_size":{},"one_pair_only":0,"both_pairs":0,"neither_pair":0,"match_present":0}
    for k in range(4):
        for _ in range(128):
            W,S,P,Q=make(k,rng)
            lhs, fam=check(W,S,P,Q)
            report['cases']+=1
            report['cases_by_internal_size'][str(k)]=report['cases_by_internal_size'].get(str(k),0)+1
            pair_count=sum(bool(z) for z in fam)
            report[['neither_pair','one_pair_only','both_pairs'][pair_count]]+=1
            report['match_present']+=bool(pair_count)
    # Cyclic planar-like example: only swapped terminal pairing, with one self-loop.
    # P=(0,1), S=(2), Q=(3,4)
    W=[[F(0) for j in range(5)] for i in range(5)]
    W[0][4]=F(1,8);W[0][2]=F(1,8);W[1][3]=F(1,8)
    W[2][2]=F(1,5);W[2][4]=F(1,8)
    planar,fam=check(W,[2],[0,1],[3,4]);assert planar == F(-37,2560)
    assert len(fam[0])==0 and len(fam[1])==2
    report['one_pair_cyclic_example']={'det_cofactor':str(planar),'identity_routings':len(fam[0]),'swapped_routings':len(fam[1]),'row_sums':[str(sum(x)) for x in W]}
    # Both pairings, algebraic cancellation with strictly substochastic weights.
    W=[[F(0) for _ in range(4)] for _ in range(4)]
    for i in [0,1]:
        for j in [2,3]: W[i][j]=F(1,8)
    balanced,fam=check(W,[],[0,1],[2,3]);assert balanced==0 and len(fam[0])==len(fam[1])==1
    report['two_pair_cancellation_example']={'det_cofactor':str(balanced),'identity_routings':len(fam[0]),'swapped_routings':len(fam[1]),'edit_formula':'(z+t)/8+zt for edits 0->2 and 1->3'}
    print(json.dumps(report,sort_keys=True,indent=2))


if __name__=='__main__': main()
