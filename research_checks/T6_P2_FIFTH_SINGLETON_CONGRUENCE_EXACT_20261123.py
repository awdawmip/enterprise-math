#!/usr/bin/env python3
"""Exact T6 v2(d)=5 singleton rigidity check; no floating-point arithmetic.

Assumes previous universal v2>=6 cancellation. The theorem uses original
full H0..H6 equality and two separate exponent-mass budgets <=2331.
"""
from collections import defaultdict
from itertools import combinations

CAP = 2331
JS = [j for j in range(1, (CAP+1)//32+1, 2) if 32*j-1 <= CAP]
assert len(JS) == 36 and JS[0] == 1 and JS[-1] == 71

def invpow(j, k, modulus):
    return pow(j, -k, modulus)

def signed_moment_mod(a, b, k, bits):
    modulus = 1 << bits
    return (invpow(a,k,modulus)-invpow(b,k,modulus)) % modulus

groups = defaultdict(list)
for j in JS:
    groups[invpow(j,5,32)].append(j)
assert len(groups) == 16
assert sorted(map(len,groups.values())) == [2]*12+[3]*4

rejected = []
for a,b in combinations(JS,2):
    if invpow(a,5,32) != invpow(b,5,32):
        continue
    assert (b-a)%32 == 0
    d4 = signed_moment_mod(a,b,4,7)
    d6 = signed_moment_mod(a,b,6,9)
    assert d4%16 == 0 and d6%64 == 0
    t4 = (d4//16)%8
    t6 = (d6//64)%8
    t = (b-a)//32
    assert t4 == 0
    assert t6 == (3*t*invpow(a,7,8))%8
    assert t4 != t6
    rejected.append((a,b,t4,t6))
assert len(rejected) == 24
assert all(b-a in (32,64) for a,b,_,_ in rejected)

# Check the symbolic mod256 implication on 1024 additional cases.
for a in range(1,256,2):
    for t in range(1,9):
        b = a+32*t
        d4 = signed_moment_mod(a,b,4,7)
        d6 = signed_moment_mod(a,b,6,9)
        assert d4%16 == 0 and d6%64 == 0
        assert (d4//16)%8 == 0
        assert (d6//64)%8 == (3*t*invpow(a,7,8))%8
        assert ((((d4//16)-(d6//64))%8) == 0) == (t%8 == 0)

print("PASS 36 admissible odd factors in exact v2=5")
print("PASS 16 fifth-moment classes modulo 32")
print("PASS 606 first-tier exclusions and 24 cross-valuation exclusions")
print("PASS 1024 extension checks and modulo-256 singleton rigidity")
