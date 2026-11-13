#!/usr/bin/env python3
"""Exact rational checker for R749SMD adaptive historical Walsh-source observer.
Scope: R749SF conditional lift plus declared controller; no native event permission.
"""
from fractions import Fraction as Q
from itertools import combinations, product
import json

HISTORY = list(product((-1, 1), repeat=3))

def emit(z, word):
    x, y, t = z
    out = Q(1)
    for i, a in enumerate(word):
        symbol = x if i == 0 else (y if word[0] == 1 else t) if i == 1 else y*t
        out *= Q(2 + a*symbol, 4)
    return out

def matr(h):
    return [[emit(z, w) for z in HISTORY] for w in product((-1,1), repeat=h)]

def rank_q(A):
    A = [[Q(v) for v in row] for row in A]
    if not A: return 0
    i = 0
    for j in range(len(A[0])):
        k = next((k for k in range(i,len(A)) if A[k][j]),None)
        if k is None: continue
        A[i], A[k] = A[k], A[i]
        v = A[i][j]
        A[i] = [q / v for q in A[i]]
        for r in range(len(A)):
            if r != i and A[r][j]:
                t = A[r][j]
                A[r] = [u - t*v for u,v in zip(A[r],A[i])]
        i += 1
        if i == len(A): break
    return i

def det_q(M):
    A = [[Q(v) for v in row] for row in M]
    assert len(A) == len(A[0]); n = len(A)
    d = Q(1)
    for j in range(n):
        k = next((k for k in range(j,n) if A[k][j]),None)
        if k is None: return Q(0)
        if k != j:
            A[j],A[k] = A[k],A[j]
            d = -d
        p = A[j][j]; d *= p
        for k in range(j+1,n):
            t = A[k][j] / p
            for l in range(j,n): A[k][l] -= t*A[j][l]
    return d

def marginal(prior, h):
    return [sum(prior[z] * emit(z,w) for z in HISTORY)
            for w in product((-1,1),repeat=h)]

axes = range(6)
supports = [frozenset(c) for c in combinations(axes,2)]
directed = [(A,B) for A in supports for B in supports if len(A&B)==1]
assert len(directed)==120
for A,B in directed:
    moves = [C for C in supports if len(B&C)==1]
    forced = A^B
    assert len(moves)==8 and forced in moves
    assert len([C for C in moves if C!=forced])==7

mats = [matr(h) for h in range(4)]
for h,M in enumerate(mats):
    assert len(M)==2**h and len(M[0])==8
    assert all(sum(M[i][j] for i in range(len(M)))==1 for j in range(8))
    assert rank_q(M)==2**h
assert abs(det_q(mats[3]))==Q(1,4096)

assert len({tuple(mats[2][i][j] for i in range(4)) for j in range(8)})==8
for z in HISTORY:
    x,y,t=z
    for word in product((-1,1),repeat=2):
        a,b=word
        u=y+Q(x*y,2) if a==1 else t-Q(x*t,2)
        pred=Q(1,4)+Q(a*x,8)+Q(b,8)*u
        assert pred==emit(z,word)

priors = {sgn:{z:Q(1+sgn*Q(1,2)*z[1]*z[2],8) for z in HISTORY}
          for sgn in (-1,1)}
for prior in priors.values():
    assert sum(prior.values())==1 and min(prior.values())==Q(1,16)
P2p,P2m=marginal(priors[1],2),marginal(priors[-1],2)
P3p,P3m=marginal(priors[1],3),marginal(priors[-1],3)
assert P2p==P2m==[Q(1,4)]*4
assert sum(abs(a-b) for a,b in zip(P3p,P3m))/2==Q(1,4)
assert sum(P3p[1::2])==Q(5,8) and sum(P3m[1::2])==Q(3,8)

result={
  "status":"PASS","arithmetic":"exact Fraction integers/rationals",
  "source_histories":8,"legal_directed_unsigned_supports":len(directed),
  "legal_next_supports_per_state":8,"forced_per_state":1,"nonforced_per_state":7,
  "horizon_ranks":{str(h):rank_q(mats[h]) for h in range(4)},
  "horizon2_distinct_deterministic_history_laws":8,
  "minimal_affine_expectation_dimensions":{str(h):2**h-1 for h in range(4)},
  "horizon3_determinant_abs":"1/4096",
  "positive_prior_witness_min_mass":"1/16",
  "prior_witness_TV_at_H2":"0","prior_witness_TV_at_H3":"1/4",
  "prior_witness_P_A3_plus":{"mu_plus":"5/8","mu_minus":"3/8"},
  "model":"R749SF conditional sign-lift + declared history-dependent choice controller",
  "native_event_permission":"NOT_CHECKED"
}
print(json.dumps(result,indent=2,ensure_ascii=False))
