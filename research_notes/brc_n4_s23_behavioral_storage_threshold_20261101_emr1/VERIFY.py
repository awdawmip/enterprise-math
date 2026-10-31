#!/usr/bin/env python3
"""Exact rational audit of the BRC N=4 six-state storage obstruction.

This certifies the finite matrix identities and six lawful witness laws.
The rank-nullspace quantifiers over arbitrary stochastic E are proved in PROOF.md.
"""
from fractions import Fraction as Q
from itertools import product

M = [
    [Q(1,2), Q(1,2), 0, 0, 0, 0],
    [Q(9,20), Q(11,20), 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, Q(1,2), Q(1,2), 0],
    [0, 0, 0, Q(1,10), Q(9,10), 0],
    [0, 0, 0, 0, 0, 1],
]
INV = [
    [11, -10, 0, 0, 0, 0],
    [-9, 10, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, Q(9,4), Q(-5,4), 0],
    [0, 0, 0, Q(-1,4), Q(5,4), 0],
    [0, 0, 0, 0, 0, 1],
]
N=6
assert all(all(x>=0 for x in row) and sum(row)==1 for row in M)
for i in range(N):
    for j in range(N):
        assert sum(INV[i][r]*M[r][j] for r in range(N)) == (1 if i==j else 0)

# Max_{||z||_infty<=1} ||M^{-T} z||_1; a convex piecewise-linear
# function reaches its maximum at a vertex of [-1,1]^6.
norms=[]
for z in product((-1,1), repeat=N):
    w=[sum(INV[i][j]*z[i] for i in range(N)) for j in range(N)]
    norms.append((sum(abs(x) for x in w),z))
C=max(v for v,_ in norms)
assert C == 47
assert any(v==47 and z==(1,-1,1,1,-1,-1) for v,z in norms)
assert all(sum(abs(x) for x in row) <= 21 for row in INV)

# For each source cell j, construct the *legal deterministic policy*:
# first-stage stop probs=0 on A and B, second-stage stop probs=0
# on U/AV/BV; third-stage c_x=1 precisely at cell j, 0 elsewhere.
# Its T=3 prepared probability column must be M e_j.
first_stage=[0,0,0,1,1,1]
second_stage=[0,0,1,0,0,2]
for j in range(N):
    a=(0,0); b=(0,0,0); c=tuple(int(x==j) for x in range(N))
    latent=[]
    for x in range(N):
        aa=a[first_stage[x]]; bb=b[second_stage[x]]; cc=c[x]
        latent.append((Q(aa), Q((1-aa)*bb), Q((1-aa)*(1-bb)*cc),
                       Q((1-aa)*(1-bb)*(1-cc))))
    assert all(sum(row)==1 for row in latent)
    prepared=[[sum(M[i][x]*latent[x][t] for x in range(N)) for t in range(4)]
              for i in range(N)]
    assert all(sum(row)==1 for row in prepared)
    for i in range(N):
        assert prepared[i][2]==M[i][j]
        assert prepared[i][3]==1-M[i][j]
        assert prepared[i][0]==prepared[i][1]==0

# Sample k=5 encoding merges the two AU latent cells, and the expected
# annihilator demonstrates how the abstract argument specializes.
E=[[int(x==grp) for grp in range(5)] for x in [0,0,1,2,3,4]]
z=[1,-1,0,0,0,0]             # E^T z=0
assert all(sum(E[x][j]*z[x] for x in range(N))==0 for j in range(5))
w=[sum(INV[i][j]*z[i] for i in range(N)) for j in range(N)]
assert all(sum(w[i]*sum(M[i][x]*E[x][h] for x in range(N))
               for i in range(N))==0 for h in range(5))
assert sum(abs(x) for x in w)==40
assert max(abs(sum(w[i]*M[i][j] for i in range(N))) for j in range(N))==1

print('PASS_BRC_N4_S23_BEH_STORAGE_K_LT6_OBSTRUCTION_20261101')
print('matrix_inverse_exact=PASS')
print('M_stochastic_rows=6')
print('norm_inverse_transpose_inf_to_one=47')
print('sign_vectors_checked=64')
print('six_lawful_single_cell_stopping_policies=PASS')
print('k5_example_annihilator=PASS')
print('all_stochastic_encoder_k_le5_universal_bound=ANALYTIC_PROOF_IN_PROOF_MD')
print('bound_all_k_le5_all_m=1/47')
print('k_ge6_vanishing_error=PR_1762_ANALYTIC_QUANTIZATION')
print('native_X6_bridge_and_independent_review=NOT_CLAIMED')
