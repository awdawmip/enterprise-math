#!/usr/bin/env python3
"""Exact Fraction checks for the five-state deterministic BRC N4/S23 theorem."""
from fractions import Fraction as F
from itertools import combinations, product

Z = F(0)
M = [
    [F(1,2),F(1,2),Z,Z,Z,Z],
    [F(9,20),F(11,20),Z,Z,Z,Z],
    [Z,Z,F(1),Z,Z,Z],
    [Z,Z,Z,F(1,2),F(1,2),Z],
    [Z,Z,Z,F(1,10),F(9,10),Z],
    [Z,Z,Z,Z,Z,F(1)],
]
N = [
    [F(11),-F(10),Z,Z,Z,Z],
    [-F(9),F(10),Z,Z,Z,Z],
    [Z,Z,F(1),Z,Z,Z],
    [Z,Z,Z,F(9,4),-F(5,4),Z],
    [Z,Z,Z,-F(1,4),F(5,4),Z],
    [Z,Z,Z,Z,Z,F(1)],
]
assert all(sum(M[i][t]*N[t][j] for t in range(6))==int(i==j)
           for i in range(6) for j in range(6))
row_diffs = {(i,j):sum(abs(N[i][c]-N[j][c]) for c in range(6))
             for i,j in combinations(range(6),2)}
assert max(row_diffs.values())==40
assert [k for k,v in row_diffs.items() if v==40]==[(0,1)]
assert sum(M[0])==sum(M[1])==1

# Two independent values for all 11 causal behavioral information sets.
# A/B first-stage; U/AV/BV second-stage; six separate terminal cells.
sg=[0,0,0,1,1,1]
group=[0,0,1,0,0,2]
count=0
max_error=Z
for bits in list(product((F(1,4),F(3,4)), repeat=11)) + list(product((Z,F(1)), repeat=11)):
    a,b,c=bits[:2],bits[2:5],bits[5:]
    latent=[]
    for x in range(6):
        aa=a[sg[x]]; bb=b[group[x]]; cc=c[x]
        latent.append((aa,(1-aa)*bb,(1-aa)*(1-bb)*cc,(1-aa)*(1-bb)*(1-cc)))
    assert all(sum(f)==1 and min(f)>=0 for f in latent)
    # The encoder merges only AU0/AU1; 4 remaining cells are stored exactly.
    decoded=[tuple(F(19,40)*latent[0][t]+F(21,40)*latent[1][t]
                   for t in range(4))]*2+latent[2:]
    for i in range(6):
        true=[sum(M[i][x]*latent[x][t] for x in range(6)) for t in range(4)]
        pred=[sum(M[i][x]*decoded[x][t] for x in range(6)) for t in range(4)]
        tv=sum(abs(true[t]-pred[t]) for t in range(4))/2
        assert tv<=F(1,40)
        max_error=max(max_error,tv)
        count+=1
assert count==4096*6 and max_error==F(1,40)
# Reachability of the upper bound: stop at time 3 iff cell AU0, else time 4.
indicator=[(Z,Z,F(int(x==0)),F(int(x!=0))) for x in range(6)]
q=tuple(F(19,40)*indicator[0][t]+F(21,40)*indicator[1][t]
        for t in range(4))
for i in (0,1):
    true=sum(M[i][x]*indicator[x][2] for x in range(6))
    pred=sum(M[i][x]*(q[2] if x<2 else indicator[x][2]) for x in range(6))
    assert abs(true-pred)==F(1,40)
print('inverse_checks=36')
print('pairwise_inverse_row_differences=15')
print('max_inverse_row_difference=40 unique_pair=(AU0,AU1)')
print(f'control_tables=2048 deterministic_plus_2048_behavioral checked_prepared_laws={count}')
print(f'max_exact_TV_error={max_error}')
print('indicator_witness_TV_error=1/40')
print('PASS_BRC_N4_S23_DETERMINISTIC_K5_EXACT_FLOOR_20261101')
