#!/usr/bin/env python3
"""Exact finite checks for the X6 integral component-isometry group and Ori6 gate."""
from collections import deque
from itertools import combinations, permutations, product

N=6
ID=tuple(range(1,N+1))

def compose(g,h):
    out=[]
    for x in h:
        s=1 if x>0 else -1
        y=g[abs(x)-1]
        out.append(s*y)
    return tuple(out)

def q_triad(S):
    i,j,k=S
    q=list(ID)
    q[i]=-(j+1);q[j]=-(k+1);q[k]=-(i+1)
    return tuple(q)

def perm_parity(g):
    p=[abs(x)-1 for x in g]
    return sum(p[i]>p[j] for i in range(N) for j in range(i+1,N))%2

def matrix_det_sign(g):
    return (-1 if perm_parity(g) else 1) * __import__('math').prod(1 if x>0 else -1 for x in g)

def closure(gens):
    G={ID};q=deque([ID])
    while q:
        h=q.popleft()
        for g in gens:
            x=compose(g,h)
            if x not in G:G.add(x);q.append(x)
    return G

# Entire signed permutation/isometry group B6.
B6={tuple(signs[i]*(p[i]+1) for i in range(N))
    for p in permutations(range(N)) for signs in product((-1,1),repeat=N)}
assert len(B6)==(2**6)*720==46080

# Triadic generated subgroup from all 20 canonical Q_S.
R=closure(tuple(q_triad(S) for S in combinations(range(N),3)))
assert len(R)==23040
assert all(perm_parity(g)==0 for g in R)
assert {g for g in B6 if perm_parity(g)==0}==R

# Every sign pattern occurs in R over identity positive permutation.
sign_kernel={g for g in R if tuple(abs(x) for x in g)==ID}
assert len(sign_kernel)==64

# Add one odd positive-axis transposition: full B6 is generated.
swap01=(2,1,3,4,5,6)
assert perm_parity(swap01)==1
full=closure(tuple(q_triad(S) for S in combinations(range(N),3))+(swap01,))
assert full==B6

# Positive-permutation parity is not the same as ordinary matrix determinant,
# because the sign kernel contains both determinant signs.
parity_det={(perm_parity(g),matrix_det_sign(g)) for g in B6}
assert parity_det=={(0,1),(0,-1),(1,1),(1,-1)}

# Unit lattice shell consists exactly of signed coordinate units. This finite
# fact is the computational shadow of the proof that every integral isometry is
# a signed permutation.
unit_shell=[]
for z in product(range(-1,2),repeat=N):
    if sum(x*x for x in z)==1: unit_shell.append(z)
assert len(unit_shell)==12
assert all(sum(x!=0 for x in z)==1 for z in unit_shell)

print('PASS_X6_INTEGRAL_ISOMETRY_ORI6_V7')
print('integral_linear_isometry_group_order',len(B6))
print('triadic_subgroup_order',len(R))
print('triadic_index',len(B6)//len(R))
print('sign_kernel_order',len(sign_kernel))
print('one_odd_positive_axis_generator_closes_full_B6',True)
print('positive_axis_parity_equals_matrix_det',False)
print('norm1_lattice_vectors',len(unit_shell))
