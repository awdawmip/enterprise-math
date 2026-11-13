#!/usr/bin/env python3
"""R5 exact 2^15 subset DP for legal atom orderings on the maximal feasible ray."""
from fractions import Fraction as F
from math import lcm, factorial
from pathlib import Path
import contextlib, io, runpy

with contextlib.redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(Path(__file__).with_name("VERIFY_R5_SHARP_RAY.py")))
X=prior["X"]; steps=prior["steps"]; eps=prior["eps_max"]
T=1<<len(steps)
assert T==32768
common=1
for z in X:common=lcm(common,z.denominator)
for j,i,a,v in steps:
    for w in v:
        if w:common=lcm(common,(eps*a*w).denominator)
base=[int(z*common) for z in X]
moves=[[int(eps*a*w*common) for w in v] for j,i,a,v in steps]

# Every subset has one unique exact intermediate vector independently of order.
states=[None]*T
states[0]=tuple(base)
valid=bytearray(T);valid[0]=1
by_degree=[0]*16;by_degree[0]=1
for mask in range(1,T):
    bit=mask&(-mask)
    index=bit.bit_length()-1
    parent=mask^bit
    states[mask]=tuple(u+v for u,v in zip(states[parent],moves[index]))
    valid[mask]=int(min(states[mask])>=0)
    by_degree[mask.bit_count()]+=valid[mask]

# Each Boolean-lattice monotone path from 0 to 2^15-1 gives one ordering.
ways=[0]*T;ways[0]=1
for mask in range(T):
    if not valid[mask] or not ways[mask]:continue
    remaining=(T-1)^mask
    while remaining:
        bit=remaining&(-remaining)
        nxt=mask|bit
        if valid[nxt]:ways[nxt]+=ways[mask]
        remaining^=bit

back=[0]*T;back[-1]=1
for mask in range(T-2,-1,-1):
    if not valid[mask]:continue
    remaining=(T-1)^mask
    while remaining:
        bit=remaining&(-remaining)
        nxt=mask|bit
        if valid[nxt]:back[mask]+=back[nxt]
        remaining^=bit
assert back[0]==ways[-1]

first=[];last=[]
for idx,(j,k,a,v) in enumerate(steps):
    bit=1<<idx
    first.append(((j,k),back[bit] if valid[bit] else 0))
    parent=(T-1)^bit
    last.append(((j,k),ways[parent] if valid[parent] else 0))
assert sum(v for _,v in first)==ways[-1]
assert sum(v for _,v in last)==ways[-1]
assert sum(by_degree)==7109
assert ways[-1]==3514190816
assert F(ways[-1],factorial(15))==F(109818463,40864824000)

print('COMMON_DENOMINATOR_DIGITS',len(str(common)))
print('VALID_SUBSET_COUNT',sum(valid))
print('VALID_SUBSETS_BY_CARDINALITY',by_degree)
print('ALL_15_ATOM_PERMUTATIONS',factorial(15))
print('EXACT_LEGAL_PERMUTATIONS_AT_MAX_RAY_ENDPOINT',ways[-1])
print('LEGAL_PERMUTATION_FRACTION',F(ways[-1],factorial(15)))
print('FIRST_MOVE_LEGAL_COUNTS',first)
print('LAST_MOVE_LEGAL_COUNTS',last)
print('PASS_R5_EXACT_ALL_2POWER15_PREFIX_STATES_AND_PERMUTATION_CENSUS')
