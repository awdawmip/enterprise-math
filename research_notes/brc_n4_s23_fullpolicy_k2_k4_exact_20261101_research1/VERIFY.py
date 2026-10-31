#!/usr/bin/env python3
"""Exact Fraction witness checker for common-encoder 2-,3-,4-state BRC/S23.

The arbitrary-real encoder lower bounds are analytical kernel statements in
PROOF.md; finite enumeration here verifies algebra, constructions and all
2048 deterministic S23 control tables, without replacing the proof.
"""
from fractions import Fraction as Q
from itertools import product, combinations

Z = Q(0)
M = [
 [Q(1,2),Q(1,2),Z,Z,Z,Z],
 [Q(9,20),Q(11,20),Z,Z,Z,Z],
 [Z,Z,Q(1),Z,Z,Z],
 [Z,Z,Z,Q(1,2),Q(1,2),Z],
 [Z,Z,Z,Q(1,10),Q(9,10),Z],
 [Z,Z,Z,Z,Z,Q(1)],
]
N = [
 [Q(11),Q(-10),Z,Z,Z,Z],
 [Q(-9),Q(10),Z,Z,Z,Z],
 [Z,Z,Q(1),Z,Z,Z],
 [Z,Z,Z,Q(9,4),Q(-5,4),Z],
 [Z,Z,Z,Q(-1,4),Q(5,4),Z],
 [Z,Z,Z,Z,Z,Q(1)],
]
assert all(sum(M[i][j]*N[j][h] for j in range(6))==int(i==h)
           for i in range(6) for h in range(6))
assert all(sum(row)==1 and min(row)>=0 for row in M)

# The 'conditioned nullspace' basis produces five effective inverse rows.
A = [(N[0][h]+N[1][h])/2 for h in range(6)]
assert A == [Q(1),Z,Z,Z,Z,Z]
B = [(N[3][h]+N[4][h])/2 for h in range(6)]
assert B == [Z,Z,Z,Q(1),Z,Z]
rows5 = [A,N[2],N[3],N[4],N[5]]
diam5 = {(i,j):sum(abs(rows5[i][h]-rows5[j][h]) for h in range(6))
         for i,j in combinations(range(5),2)}
assert max(diam5.values())==5
assert {p for p,d in diam5.items() if d==5}=={(2,3)}
rows4 = [A,N[2],B,N[5]]
assert all(sum(abs(rows4[i][h]-rows4[j][h]) for h in range(6)) == 2
           for i,j in combinations(range(4),2))

# Stronger nullspace inequalities for all zero-sum, small integer trial z:
# z0=z1 yields norm(N^T z) <=5P; both equalities yield =2P.
checks5 = checks4 = 0
for zs in product(range(-2,3),repeat=5):
    a,z2,z3,z4,z5=zs
    z=(a,a,z2,z3,z4,z5)
    if sum(z) or not any(z): continue
    P=sum(max(v,0) for v in z)
    nrm=sum(abs(sum(z[x]*N[x][h] for x in range(6))) for h in range(6))
    assert nrm<=5*P
    checks5+=1
    if z3==z4:
        assert nrm==2*P
        checks4+=1

# k-state deterministic common encoders and linear-in-F decoders.
# For k=2 the decoder symbols are probability mixtures of the A/B
# prepared laws, which are themselves mixtures of latent laws.
code_rows={
 2: (0,0,0,1,1,1),
 3: (0,0,1,2,2,1),
 4: (0,0,1,2,2,3),
}
weights={
 2: ((Q(9,40),Q(11,40),Q(1,2),Z,Z,Z),
     (Z,Z,Z,Q(1,20),Q(9,20),Q(1,2))),
 3: ((Q(19,40),Q(21,40),Z,Z,Z,Z),
     (Z,Z,Q(1,2),Z,Z,Q(1,2)),
     (Z,Z,Z,Q(3,10),Q(7,10),Z)),
 4: ((Q(19,40),Q(21,40),Z,Z,Z,Z),
     (Z,Z,Q(1),Z,Z,Z),
     (Z,Z,Z,Q(3,10),Q(7,10),Z),
     (Z,Z,Z,Z,Z,Q(1))),
}
for k in (2,3,4):
    assert all(sum(row)==1 and min(row)>=0 for row in weights[k])
    assert len(weights[k])==k
max_errors = {k:Z for k in (2,3,4)}
argmax = {}
checks=0
first_group = (0,0,0,1,1,1)
second_group = (0,0,1,0,0,2)
for ibits, rawbits in enumerate(product((Q(0),Q(1)), repeat=11)):
    first,second,last=rawbits[:2],rawbits[2:5],rawbits[5:]
    F=[]
    for x in range(6):
        a=first[first_group[x]];b=second[second_group[x]];c=last[x]
        F.append((a,(1-a)*b,(1-a)*(1-b)*c,(1-a)*(1-b)*(1-c)))
    assert all(sum(row)==1 for row in F)
    for k in (2,3,4):
        D=[tuple(sum(weights[k][j][x]*F[x][t] for x in range(6))
                 for t in range(4)) for j in range(k)]
        assert all(sum(row)==1 and min(row)>=0 for row in D)
        for i in range(6):
            tv = sum(abs(sum(M[i][x]*(F[x][t]-D[code_rows[k][x]][t])
                             for x in range(6))) for t in range(4))/2
            checks+=1
            if tv>max_errors[k]:
                max_errors[k]=tv
                argmax[k]=(ibits,i)
assert checks==3*2048*6
assert max_errors=={2:Q(1,2),3:Q(1,2),4:Q(1,5)}, max_errors
print('MN_identity_checks=36')
print('five_collapsed_inverse_diameter=5 unique_pair=(N3,N4)')
print('four_collapsed_inverse_diameter=2 all_pairs=2')
print(f'integer_dual_checks_one_equality={checks5} two_equalities={checks4}')
print(f'S23_deterministic_controls=2048 total_prepared_TV_checks={checks}')
for k in (2,3,4):
    print(f'k={k} max_TV={max_errors[k]} witness_policy_index_and_prepared={argmax[k]}')
print('REAL_STOCHASTIC_ENCODER_LOWER_BOUNDS_BY_DIMENSION_AND_NORM_ANALYSIS')
print('REAL_BEHAVIORAL_POLICY_UPPER_BOUNDS_BY_LINEAR_DECODER_AND_TV')
print('PASS_BRC_N4_S23_FULL_POLICY_K2_K4_EXACT_20261101')
