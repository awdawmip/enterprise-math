#!/usr/bin/env python3
"""Exact integer structural check for the R5 d29/d32 characteristic-zero tail proof.

Confirms exhaustively which six-cone t denominators have linear repetitions,
and the absence of quadratic-linear root collisions. The only remaining
algebraic identities are the two explicit paired-cone cancellations in
EXTENSION_29_32_CHARACTERISTIC_ZERO.md.
"""
from itertools import permutations

for d in (29,32):
    collisions = []
    for r in (219,220,221):
        for a,b,c in permutations((214,215,r)):
            lin=(0,216,217,218,a+b)
            residues=[v%d for v in lin]
            equal=[(i,j) for i in range(5) for j in range(i+1,5)
                   if residues[i]==residues[j]]
            quadratic=(429+r)%d
            cross=[i for i,v in enumerate(lin) if (2*v-quadratic)%d==0]
            assert not cross,(d,r,a,b,c,cross)
            if equal:
                assert d==29 and equal==[(0,4)]
                assert (r,a,b,c) in {
                    (220,215,220,214),(220,220,215,214),
                    (221,214,221,215),(221,221,214,215)}
                collisions.append((r,a,b,c))
            else:
                assert len(set(residues))==5
    assert len(collisions)==(4 if d==29 else 0)
    print("d=",d,"collision_terms=",len(collisions),"pairs=",collisions)
print("PASS: only four d29 pair collisions; no mixed collisions; all d32 factors simple")
