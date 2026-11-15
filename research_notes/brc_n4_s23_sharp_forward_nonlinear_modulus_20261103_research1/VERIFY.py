#!/usr/bin/env python3
"""BRC S23 exact finite-modulus test; Python standard library only."""
from fractions import Fraction as Q
from itertools import product
import json
import random

A = (0, 0, 0, 1, 1, 1)
B = (2, 2, 3, 2, 2, 4)
C = (5, 6, 7, 8, 9, 10)
M = ((10,10,0,0,0,0), (9,11,0,0,0,0), (0,0,20,0,0,0),
     (0,0,0,10,10,0), (0,0,0,2,18,0), (0,0,0,0,0,20))
MASKS = ((3,31), (7,27), (11,23), (15,19))
BETAS = ((Q(0),Q(0)), (Q(1,2),Q(1,2)), (Q(1,4),Q(3,4)))
DELTAS = (Q(0),Q(1,100),Q(1,20),Q(1,4),Q(1,2),Q(3,4),Q(1))

def branch(p,q,r):
    return (p, (1-p)*q, (1-p)*(1-q)*r, (1-p)*(1-q)*(1-r))

def observe(z, mask=0, beta=Q(0)):
    raw = [branch(beta if mask & (1<<A[i]) else z[A[i]],
                  beta if mask & (1<<B[i]) else z[B[i]], z[C[i]])
           for i in range(6)]
    return [tuple(sum(Q(M[j][i],20)*raw[i][k] for i in range(6))
                  for k in range(4)) for j in range(6)]

def tv(x,y):
    return sum(abs(a-b) for a,b in zip(x,y))/2

def distance(z,w,n,e,bn,be):
    return max(tv(p,q) for mask,beta in ((0,Q(0)),(n,bn),(e,be))
               for p,q in zip(observe(z,mask,beta),observe(w,mask,beta)))

def modulus(delta):
    return 1-(1-delta)**3

def witness(delta):
    z = [Q(0)]*11
    w = z.copy()
    for k in (0,2,5,6):
        w[k] = delta
    return z,w

count_witness = count_bound = count_rows = 0
rng = random.Random(202611030959)
for n,e in MASKS:
    for bn,be in BETAS:
        for delta in DELTAS:
            z,w = witness(delta)
            assert tv(observe(z)[0],observe(w)[0]) == modulus(delta)
            assert distance(z,w,n,e,bn,be) == modulus(delta)
            count_witness += 1
        for _ in range(100):
            z = [Q(rng.randrange(13),12) for _ in range(11)]
            w = [Q(rng.randrange(13),12) for _ in range(11)]
            delta = max(abs(x-y) for x,y in zip(z,w))
            for mask,beta in ((0,Q(0)),(n,bn),(e,be)):
                for p,q in zip(observe(z,mask,beta),observe(w,mask,beta)):
                    assert tv(p,q) <= modulus(delta)
                    count_rows += 1
            assert distance(z,w,n,e,bn,be) <= modulus(delta)
            count_bound += 1
assert all(sum(row)==20 for row in M)
result = {
  "status":"PASS_BRC_S23_SHARP_FORWARD_NONLINEAR_TV_MODULUS_20261103",
  "frozen_science":"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
  "theorem":"sup_{||z-w||_inf<=delta} max_{view,label} TV = 1-(1-delta)^3, 0<=delta<=1",
  "sharp_lipschitz":"3 (supremum as delta tends to zero)",
  "overwrite_masks":MASKS,
  "beta_pairs":[[str(x),str(y)] for x,y in BETAS],
  "counts":{"exact_extremizers":count_witness,"random_pair_bound_checks":count_bound,
            "labeled_row_bound_checks":count_rows},
  "scope":"finite checks corroborate; analytic Bernoulli coupling and extremizer prove real-domain statement"
}
print(json.dumps(result,indent=2))
