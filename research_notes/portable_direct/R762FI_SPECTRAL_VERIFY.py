#!/usr/bin/env python3
"""Exact q=9 moving-center orbit spectrum and 33-order recurrence, cyclotomic integers."""
from collections import Counter
from itertools import product
import json
Q=9
M=Q//3
S=((0,0,0),(1,0,0),(0,0,1),(1,1,0),(1,1,1),(0,1,1))
HALF=pow(2,-1,Q)
Z=(0,)*(2*M)
ONE=(1,)+(0,)*(2*M-1)

def canonical(v):
    return min(tuple(sorted(v)),tuple(sorted((-x)%Q for x in v)))

def mul(a,b):
    z=[0]*Q
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:z[(i+j)%Q]+=x*y
    for i in range(2*M,Q):
        z[i-M]-=z[i];z[i-2*M]-=z[i]
    return tuple(z[:2*M])

def lamb(u):
    z=[0]*Q
    for s in S:
        t=((s[0]-HALF)%Q,(HALF-s[1])%Q,(s[2]-HALF)%Q)
        z[sum(u[j]*t[j] for j in range(3))%Q]+=1
    for i in range(2*M,Q):
        z[i-M]-=z[i];z[i-2*M]-=z[i]
    return tuple(z[:2*M])

def valuation3(n):
    if n==0:return None
    c=0
    while n%3==0:
        c+=1;n//=3
    return c

orbits=sorted({canonical(y) for y in product(range(Q),repeat=3)})
assert len(orbits)==85
vals=Counter(lamb(u) for u in orbits)
assert len(vals)==34 and vals[Z]==6
assert Counter(vals.values())==Counter({1:5,2:13,3:12,4:3,6:1})
for t in vals:
    c=mul(mul(t,t),t)
    assert all(x%3==0 for x in c)

# Q(T) = product over 33 *nonzero distinct* eigenvalues (T - lambda).
p=[ONE]
for v in sorted(t for t in vals if t!=Z):
    z=[Z]*(len(p)+1)
    for i,a in enumerate(p):
        prod=mul(v,a)
        z[i]=tuple(z[i][j]-prod[j] for j in range(2*M))
        z[i+1]=tuple(z[i+1][j]+a[j] for j in range(2*M))
    p=z
assert len(p)==34 and p[-1]==ONE
assert all(a[1:]==(0,)*(2*M-1) for a in p), 'Galois invariance failed'
coeff=[a[0] for a in p] # low to high, Q monic
assert coeff[-1]==1
# If j nonzero roots selected, elementary symmetric e_j has v3>=ceil(j/3).
valuation_bounds=[]
for j in range(1,34):
    c=coeff[33-j]
    bound=(j+2)//3
    assert c%3**bound==0, (j,c,bound)
    valuation_bounds.append({'j':j,'required':bound,'actual':valuation3(c)})

# Verify Q(C)C=0 on all 85 unit orbit-coordinate vectors, independently
# from the Fourier/cyclotomic characteristic computation.
T=tuple(((s[0]-HALF)%Q,(HALF-s[1])%Q,(s[2]-HALF)%Q) for s in S)
idx={k:i for i,k in enumerate(orbits)}
trans=[[idx[canonical(tuple((r[j]-step[j])%Q for j in range(3)))] for step in T] for r in orbits]
for basis in range(len(orbits)):
    v=[0]*85;v[basis]=1
    remainder=[0]*85
    for power in range(35):
        if power>=1:
            a=coeff[power-1]
            for j in range(85):
                remainder[j]+=a*v[j]
        if power<34:
            v=[sum(v[i] for i in row) for row in trans]
    assert not any(remainder), ('matrix-poly',basis)

result={
 'schema':'R762FI_Q9_MOVING_ORBIT_MINIMAL_SPECTRAL_RECURRENCE_V1',
 'status':'PASS', 'q':9,'endpoint_count':729,'symmetry_orbits':85,
 'dual_orbits_exhaustive':85,'distinct_eigenvalues':34,
 'nonzero_distinct_eigenvalues':33,'zero_eigenvalue_orbit_multiplicity':6,
 'dual_orbit_eigenvalue_collision_histogram':dict(sorted(Counter(vals.values()).items())),
 'cyclotomic_basis':'Z[zeta_9] basis {1,zeta,...,zeta^5}; zeta^6=-zeta^3-1',
 'Q_degree':33, 'Q_coefficients_low_to_high_as_decimal_strings':[str(c) for c in coeff],
 'coefficient_valuation_bounds':valuation_bounds,
 'all_lambda_cubed_divisible_by_3':True,
 'Q_of_C_times_C_full_85_by_85_matrix':'EXACT_PASS',
 'review':'AUTHOR_CHECKED_NOT_INDEPENDENTLY_REVIEWED'}
print(json.dumps(result,indent=2))
