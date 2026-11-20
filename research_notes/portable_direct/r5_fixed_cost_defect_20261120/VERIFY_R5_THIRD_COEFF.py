#!/usr/bin/env python3
"""Independent exact rational coefficient/moment checks for R5 N^93 result.
General asymptotic relies on the symbolic proof in THIRD_COEFFICIENT.md.
"""
from fractions import Fraction as Q
from math import comb
from itertools import combinations_with_replacement

A=tuple(range(214,219))
out=tuple(range(219,315))
S1=sum(out)
S2=sum(k*k for k in out)
assert (S1,S2)==(25584,6891856)
c2=Q(3*S1*S1-S2,24)
assert c2==Q(244591414,3)
ratio=Q(219*220*221,214)+Q(219*220*221,215)
assert ratio==Q(456789762,4601)
expected={
    1:Q(1126735465100,13803),
    2:Q(2191356722009,4601),
    3:Q(7456025574970,4601),
    17:Q(4699616850358836,4601)}
for m in (1,2,3,4,5,17):
    values=[]
    for s in range(m):
        values.extend(sum(v) for v in combinations_with_replacement(A,s))
    J0=len(values)
    J1=sum(values)
    J2=sum(k*(k-1)//2 for k in values)
    c6=comb(m+4,6) if m>=2 else 0
    c7=comb(m+4,7) if m>=3 else 0
    assert J0==comb(m+4,5)
    assert J1==180*(m-1)*J0
    assert J2==116105*c6+699845*c7
    Gamma=c2*J0-Q(S1-1,2)*J1+J2+comb(m+6,7)*ratio
    if m in expected: assert Gamma==expected[m]
    print(f"PASS m={m}: J0={J0} J1={J1} J2={J2} Gamma={Gamma}")
print("PASS all exact coefficient checks")
