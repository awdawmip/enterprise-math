#!/usr/bin/env python3
"""Exact rational certificate for BRC N4/S23 stochastic storage lower bounds.

This checker verifies inverse/readout geometry and finite support-subset enumeration.
The universal quantification over all stochastic encoders follows analytically
from rank nullity and a zero-sum dual argument in PROOF.md.
"""
from fractions import Fraction as Q
from itertools import combinations, product

Z=Q(0)
M=[
 [Q(1,2),Q(1,2),Z,Z,Z,Z],
 [Q(9,20),Q(11,20),Z,Z,Z,Z],
 [Z,Z,Q(1),Z,Z,Z],
 [Z,Z,Z,Q(1,2),Q(1,2),Z],
 [Z,Z,Z,Q(1,10),Q(9,10),Z],
 [Z,Z,Z,Z,Z,Q(1)],
]
N=[
 [Q(11),Q(-10),Z,Z,Z,Z],
 [Q(-9),Q(10),Z,Z,Z,Z],
 [Z,Z,Q(1),Z,Z,Z],
 [Z,Z,Z,Q(9,4),Q(-5,4),Z],
 [Z,Z,Z,Q(-1,4),Q(5,4),Z],
 [Z,Z,Z,Z,Z,Q(1)],
]
assert all(sum(M[i][j]*N[j][k] for j in range(6))==int(i==k)
           for i in range(6) for k in range(6))
assert all(sum(row)==1 for row in M)
dist={pair:sum(abs(N[pair[0]][i]-N[pair[1]][i]) for i in range(6))
      for pair in combinations(range(6),2)}
assert max(dist.values())==40
assert [p for p,v in dist.items() if v==40]==[(0,1)]

# For k code states, any k+1 source rows of E are linearly dependent.
# Their left dependency is automatically zero-sum as E 1 = 1.
# The inverse-row diameter of such a subset gives the exact subset-dual bound.
expected={1:(Q(2),(2,5)),2:(Q(5,2),(2,4,5)),
          3:(Q(5),(2,3,4,5)),4:(Q(45,2),(1,2,3,4,5)),
          5:(Q(40),(0,1,2,3,4,5))}
checked_subsets=0
for k in range(1,6):
    boxes=[]
    for subset in combinations(range(6), k+1):
        diameter=max(dist[tuple(sorted((i,j)))] for i,j in combinations(subset,2))
        boxes.append((diameter, subset))
        checked_subsets+=1
    best=min(boxes)
    assert best==expected[k],(k,best,expected[k])
    print(f'k={k} subsets={len(boxes)} min_inverse_row_diameter={best[0]} '
          f'best_subset={best[1]} universal_TV_floor={1/best[0]}')
assert checked_subsets==sum(__import__('math').comb(6,k+1) for k in range(1,6))==57

# For any zero-sum vector z supported on a subset U, the positive part
# u_x=1_{z_x>0} is a lawful S23 time-3 terminal indicator policy.
# Verify the key rational identity over an exhaustive representative set
# of 3^6-1 integer vectors with zero sum (the theorem covers all real z).
checked_duals=0
for z in product((-1,0,1),repeat=6):
    if not any(z) or sum(z):
        continue
    p=sum(max(0,zi) for zi in z)
    assert p==sum(max(0,-zi) for zi in z)>0
    v=[sum(N[x][j]*z[x] for x in range(6)) for j in range(6)]
    assert sum(abs(t) for t in v)<=40*p
    S={x for x in range(6) if z[x]>0}
    u=[int(x in S) for x in range(6)]
    assert sum(z[x]*u[x] for x in range(6))==p
    assert all(t in (0,1) for t in u)
    checked_duals+=1

# The sharp deterministic (hence stochastic-admissible) E has E[0]=E[1].
# Its policy-informed decoder uses q=(19f0+21f1)/40 for both merged rows.
# Check all 2048 extreme causal tables; analytic convexification handles
# all continuously randomized behavioral tables using complete policy info.
first_group=(0,0,0,1,1,1)
second_group=(0,0,1,0,0,2)
checked_prepared=0
max_err=Z
for bits in product((Z,Q(1)),repeat=11):
    first,second,last=bits[:2],bits[2:5],bits[5:]
    f=[]
    for x in range(6):
        a=first[first_group[x]]; b=second[second_group[x]];c=last[x]
        f.append((a,(1-a)*b,(1-a)*(1-b)*c,(1-a)*(1-b)*(1-c)))
    q=tuple((Q(19)*f[0][t]+Q(21)*f[1][t])/40 for t in range(4))
    dec=[q,q,*f[2:]]
    for i in range(6):
        tv=sum(abs(sum(M[i][x]*(f[x][t]-dec[x][t]) for x in range(6)))
               for t in range(4))/2
        assert tv<=Q(1,40),(bits,i,tv)
        max_err=max(max_err,tv)
        checked_prepared+=1
assert checked_prepared==2048*6 and max_err==Q(1,40)
F=[[Z,Z,Q(int(x==0)),Q(int(x!=0))] for x in range(6)]
q=[(Q(19)*F[0][t]+Q(21)*F[1][t])/40 for t in range(4)]
for i in (0,1):
    assert sum(abs(sum(M[i][x]*(F[x][t]-(q[t] if x<2 else F[x][t])) for x in range(6)))
               for t in range(4))/2==Q(1,40)
print('inverse_identity_checks=36')
print('inverse_pairwise_diameters=15; unique_max_pair=(0,1):40')
print(f'subset_diameter_certificates={checked_subsets}')
print(f'representative_integer_zero_sum_duals={checked_duals}')
print(f'deterministic_policy_tables=2048 exact_prepared_TV_checks={checked_prepared}')
print('sharp_stochastic_admissible_k5_upper=1/40 via deterministic_merge_(0,1)')
print('UNIVERSAL_ALL_REAL_STOCHASTIC_ENCODERS_FROM_ANALYTIC_PROOF_NOT_FINITE_TEST')
print('PASS_BRC_N4_S23_STOCHASTIC_K5_EXACT_AND_K1_K4_SUBSET_DUAL_20261101')
