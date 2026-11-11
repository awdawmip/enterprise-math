#!/usr/bin/env python3
"""Exact, bounded X6 selected signed three-axis N=2500 shell certificate.
This is not an R063 rerun or a full six-axis shell computation.
"""
from math import comb, factorial, isqrt
from itertools import permutations, product

NORM = 2500
R = isqrt(NORM)
assert R * R == NORM

# Complete sorted-triple search; no floating point.
patterns = []
for a in range(R + 1):
    for b in range(a, R + 1):
        z2 = NORM - a*a - b*b
        if z2 < 0:
            continue
        c = isqrt(z2)
        if c >= b and c*c == z2:
            patterns.append((a,b,c))
expected = [(0,0,50),(0,14,48),(0,30,40),(18,24,40),(24,30,32)]
assert patterns == expected, (patterns, expected)

def signed_orbit(shape):
    out = set()
    for perm in set(permutations(shape)):
        nz = [i for i, x in enumerate(perm) if x]
        for signs in product((-1,1), repeat=len(nz)):
            p = list(perm)
            for i, s in zip(nz, signs):
                p[i] *= s
            out.add(tuple(p))
    return out

def path_mass(d):
    n = sum(map(abs,d))
    result = factorial(n)
    for x in d:
        result //= factorial(abs(x))
    return result

orbits = [signed_orbit(shape) for shape in patterns]
assert [len(o) for o in orbits] == [6,24,24,48,48]
all_signed = set().union(*orbits)
assert len(all_signed) == 150

# Independent enumeration in signed (x,y) and exact square test for z.
second_route = set()
for x in range(-R, R+1):
    for y in range(-R, R+1):
        t = NORM - x*x - y*y
        if t < 0:
            continue
        z = isqrt(t)
        if z*z == t:
            second_route.add((x,y,z))
            second_route.add((x,y,-z))
assert second_route == all_signed
assert all(sum(x*x for x in d) == NORM for d in all_signed)
assert {sum(x!=0 for x in d) for d in all_signed} == {1,2,3}

per_B = [path_mass(next(iter(o))) for o in orbits]
assert per_B == [1,29078984349975,55347740058143507128,
                 146667819424252202137117683587961000,
                 559453321977660597511933995509550527400]
masses = [len(o)*mass for o, mass in zip(orbits,per_B)]
assert masses == [6,697895624399400,1328345761395444171072,
                  7040055332364105702581648812222128000,
                  26853759454927708680572831784458425315200]
assert sum(masses) == 26860799510260072787603759892561716013678

# Original R063 fixed nonnegative two-generator sector: same object, same values.
old_pairs = [(0,50),(14,48),(30,40),(40,30),(48,14),(50,0)]
assert all(a*a+b*b == NORM for a,b in old_pairs)
old_mass = sum(comb(a+b,a) for a,b in old_pairs)
assert old_mass == 110695538274255714208
assert (18,24,40) in all_signed
assert path_mass((18,24,40)) == 146667819424252202137117683587961000
print('PASS X6_R063_N2500 selected_signed_slice=150 support1=6 support2=48 '
      'support3=96 shapes=5 mass=' + str(sum(masses)) +
      ' old_fixed_positive_pair_mass=' + str(old_mass) +
      ' triple=(18,24,40)')
