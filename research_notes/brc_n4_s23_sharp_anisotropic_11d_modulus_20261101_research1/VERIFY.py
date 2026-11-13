#!/usr/bin/env python3
"""Exact positive-rational BRC/S23 anisotropic modulus checks; Python stdlib only."""
from fractions import Fraction as Q
from itertools import product
from random import Random

M20 = ((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
       (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
A = (0,0,0,1,1,1)
B = (2,2,3,2,2,4)
C = (5,6,7,8,9,10)
assert len(M20)==6 and all(len(row)==6 and sum(row)==20 for row in M20)
assert all(len({A[x],B[x],C[x]})==3 for x in range(6))

def latent(a,b,c):
    return (a,(1-a)*b,(1-a)*(1-b)*c,(1-a)*(1-b)*(1-c))

def prepare(theta):
    f=[latent(theta[A[x]],theta[B[x]],theta[C[x]]) for x in range(6)]
    return tuple(tuple(sum((Q(M20[i][x],20)*f[x][t] for x in range(6)),Q(0))
                       for t in range(4)) for i in range(6))

def tv(p,q):
    return sum((abs(a-b) for a,b in zip(p,q)),Q(0))/2

def source_modulus(eps,x):
    return 1-(1-eps[A[x]])*(1-eps[B[x]])*(1-eps[C[x]])

def row_moduli(eps):
    return tuple(sum((Q(M20[i][x],20)*source_modulus(eps,x)
                      for x in range(6)),Q(0)) for i in range(6))

zero=(Q(0),)*11
sample_eps=(Q(1,2),Q(1,3),Q(1,4),Q(2,5),Q(1,7),
            Q(3,8),Q(1,5),Q(2,7),Q(1,6),Q(3,10),Q(2,9))
for eps in (zero,sample_eps,(Q(1),)*11):
    exact=tuple(tv(a,b) for a,b in zip(prepare(zero),prepare(eps)))
    assert exact==row_moduli(eps)
    print('SHARP_ANISOTROPIC_EPS=',','.join(map(str,eps)),
          'ROW_MODULI=',','.join(map(str,exact)),
          'MAX=',max(exact))

# Full enumeration of all 2^11 nontrivial coordinate-active masks at epsilon=1/3.
for mask in range(1<<11):
    eps=tuple(Q(1,3) if mask&(1<<j) else Q(0) for j in range(11))
    got=tuple(tv(a,b) for a,b in zip(prepare(zero),prepare(eps)))
    assert got==row_moduli(eps)
    # One-label constant-e4 decoder makes the universal bank-risk modulus sharp.
    e4=(Q(0),Q(0),Q(0),Q(1))
    assert max(tv(p,e4) for p in prepare(eps))==max(row_moduli(eps))
print('ALL_2^11_EXACT_MASK_ATTAINMENTS_AND_ONE_LABEL_RISK=',1<<11)

# Sharp exact per-coordinate sensitivities.
weights=[]
for j in range(11):
    eps=tuple(Q(1,3) if k==j else Q(0) for k in range(11))
    weights.append(max(row_moduli(eps))/Q(1,3))
assert weights==[Q(1),Q(1),Q(1),Q(1),Q(1),Q(1,2),Q(11,20),
                 Q(1),Q(1,2),Q(9,10),Q(1)]
print('SHARP_SINGLE_COORDINATE_WEIGHTS=',','.join(map(str,weights)))

# Anisotropic nearest-vertex cell: only AU0 third-stage control has width 1/2.
h=tuple(Q(1,2) if j==5 else Q(0) for j in range(11))
mesh= max(row_moduli(tuple(v/2 for v in h)))
uniform=1-(1-Q(1,4))**3
assert mesh==Q(1,8) and uniform==Q(37,64) and mesh<uniform
print('ANISOTROPIC_CELL_MESH_GAP=',mesh,'UNIFORM_GAP=',uniform)

# Independent exact rational sampled upper-bound checks (not the universal proof).
rng=Random(20261101)
for trial in range(256):
    eps=tuple(Q(rng.randrange(6),5) for _ in range(11))
    theta=[];phi=[]
    for d in eps:
        a=Q(rng.randrange(21),20)
        lo=max(Q(0),a-d)
        hi=min(Q(1),a+d)
        b=lo+(hi-lo)*Q(rng.randrange(21),20)
        theta.append(a);phi.append(b)
    P=prepare(theta);R=prepare(phi)
    vals=row_moduli(eps)
    assert all(tv(P[i],R[i])<=vals[i] for i in range(6))
print('EXACT_RATIONAL_POLICY_PAIR_BOUND_CHECKS=',256)
print('PASS_BRC_N4_S23_SHARP_ANISOTROPIC_11D_MODULUS_20261101')
