#!/usr/bin/env python3
"""Exact finite checker for P000 philosophy-first S4 lift groupoid task.

This checker works only at the declared finite extension/relation-phase layer.
It consumes the accepted Gen12 carrier S4 action as a downstream regression and
does not promote S4, FCC/K4, or any hidden phase to bare-P000 native identity.
"""

from itertools import permutations
from collections import deque

S4 = list(permutations(range(4)))
ID4 = tuple(range(4))

def pmul(p, q):
    """p o q, apply q first."""
    return tuple(p[q[i]] for i in range(4))

def ppow(p, n):
    r = ID4
    for _ in range(n):
        r = pmul(r, p)
    return r

def parity(p):
    return sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) % 2

# Frozen carrier generators on A,B,C,D = 0,1,2,3.
A0 = (0, 2, 3, 1)  # (B C D)
B0 = (1, 0, 2, 3)  # (A B)

def generated_perm_group(gens):
    seen = {ID4}
    q = deque([ID4])
    while q:
        x = q.popleft()
        for g in gens:
            y = pmul(x, g)
            if y not in seen:
                seen.add(y)
                q.append(y)
    return seen

assert ppow(A0, 3) == ID4
assert ppow(B0, 2) == ID4
assert ppow(pmul(A0, B0), 4) == ID4
assert len(generated_perm_group([A0, B0])) == 24

class ProductZn:
    def __init__(self, n):
        self.n = n
        self.id = (0, ID4)
        self.elements = [(k, g) for k in range(n) for g in S4]

    def mul(self, x, y):
        k, g = x
        l, h = y
        return ((k + l) % self.n, pmul(g, h))

    def power(self, x, n):
        r = self.id
        for _ in range(n):
            r = self.mul(r, x)
        return r

    def fiber(self, g):
        return [(k, g) for k in range(self.n)]

    def kernel(self):
        return [(k, ID4) for k in range(self.n)]

class ProductV4:
    """K = C2 x C2 encoded by XOR on {0,1,2,3}."""
    def __init__(self):
        self.id = (0, ID4)
        self.elements = [(k, g) for k in range(4) for g in S4]

    def mul(self, x, y):
        k, g = x
        l, h = y
        return (k ^ l, pmul(g, h))

    def power(self, x, n):
        r = self.id
        for _ in range(n):
            r = self.mul(r, x)
        return r

    def fiber(self, g):
        return [(k, g) for k in range(4)]

    def kernel(self):
        return [(k, ID4) for k in range(4)]

class ParityC4Pullback:
    """G={(z,g) in C4 x S4 : z mod 2 = sgn(g)}, q(z,g)=g."""
    def __init__(self):
        self.id = (0, ID4)
        self.elements = [
            (z, g)
            for g in S4
            for z in range(4)
            if z % 2 == parity(g)
        ]
        self._set = set(self.elements)

    def mul(self, x, y):
        z, g = x
        w, h = y
        out = ((z + w) % 4, pmul(g, h))
        assert out in self._set
        return out

    def power(self, x, n):
        r = self.id
        for _ in range(n):
            r = self.mul(r, x)
        return r

    def fiber(self, g):
        return [(z, g) for z in range(4) if z % 2 == parity(g)]

    def kernel(self):
        return [(0, ID4), (2, ID4)]

def section_pairs(ext):
    """Sections via the S4 triangle presentation a^3=b^2=(ab)^4=1."""
    out = []
    for A in ext.fiber(A0):
        for B in ext.fiber(B0):
            if ext.power(A, 3) != ext.id:
                continue
            if ext.power(B, 2) != ext.id:
                continue
            if ext.power(ext.mul(A, B), 4) != ext.id:
                continue
            out.append((A, B))
    return out

def b_parameter(pair):
    return pair[1][0]

def groupoid_fingerprint(objects, gauge_maps):
    objects = list(objects)
    objset = set(objects)
    assert all(set(f(x) for x in objects) == objset for f in gauge_maps)
    unseen = set(objects)
    orbits = []
    while unseen:
        x = next(iter(unseen))
        orb = {f(x) for f in gauge_maps}
        # gauge_maps below are complete finite groups, so one-step orbit is full.
        orbits.append(orb)
        unseen -= orb
    stabilizers = {
        x: sum(1 for f in gauge_maps if f(x) == x)
        for x in objects
    }
    n = len(objects)
    pi0 = len(orbits)
    vacuous_all_pairwise_isomorphic = (n == 0) or (pi0 == 1)
    nonempty_pairwise_isomorphic = (n > 0 and pi0 == 1)
    unique_iso_class = (pi0 == 1)
    strict_unique_aut_free = (
        n == 1 and next(iter(stabilizers.values()), 0) == 1
    )
    return {
        "objects": n,
        "pi0": pi0,
        "stabilizers": sorted(stabilizers.values()),
        "vacuous_all_pairwise_isomorphic": vacuous_all_pairwise_isomorphic,
        "nonempty_pairwise_isomorphic": nonempty_pairwise_isomorphic,
        "unique_iso_class": unique_iso_class,
        "strict_unique_aut_free": strict_unique_aut_free,
    }

# Gen12 rigid/trivial-kernel regression.
gen12 = ProductZn(1)
gen12_sections = section_pairs(gen12)
assert len(gen12.elements) == 24
assert len(gen12.kernel()) == 1
assert len(gen12_sections) == 1
gen12_params = [b_parameter(s) for s in gen12_sections]
fp_gen12 = groupoid_fingerprint(gen12_params, [lambda x: x])
assert fp_gen12 == {
    "objects": 1,
    "pi0": 1,
    "stabilizers": [1],
    "vacuous_all_pairwise_isomorphic": True,
    "nonempty_pairwise_isomorphic": True,
    "unique_iso_class": True,
    "strict_unique_aut_free": True,
}

# Split C2 relation-phase extension: two sections, one free gauge orbit.
split_c2 = ProductZn(2)
split_sections = section_pairs(split_c2)
split_params = sorted(b_parameter(s) for s in split_sections)
assert split_params == [0, 1]
c2_gauge = [
    (lambda w: (lambda x: (x + w) % 2))(w)
    for w in range(2)
]
fp_c2 = groupoid_fingerprint(split_params, c2_gauge)
assert fp_c2["objects"] == 2
assert fp_c2["pi0"] == 1
assert fp_c2["stabilizers"] == [1, 1]
assert fp_c2["strict_unique_aut_free"] is False

# Same split extension but deliberately frozen gauge: existence without one iso class.
fp_c2_frozen = groupoid_fingerprint(split_params, [lambda x: x])
assert fp_c2_frozen["objects"] == 2
assert fp_c2_frozen["pi0"] == 2
assert fp_c2_frozen["nonempty_pairwise_isomorphic"] is False

# C3 relation-phase extension: exactly one section but nontrivial automorphism.
split_c3 = ProductZn(3)
c3_sections = section_pairs(split_c3)
c3_params = [b_parameter(s) for s in c3_sections]
assert c3_params == [0]
c3_gauge = [
    (lambda u: (lambda x: (u * x) % 3))(u)
    for u in (1, 2)
]
fp_c3 = groupoid_fingerprint(c3_params, c3_gauge)
assert fp_c3["objects"] == 1
assert fp_c3["pi0"] == 1
assert fp_c3["stabilizers"] == [2]
assert fp_c3["strict_unique_aut_free"] is False

# V4 relation-phase extension with full affine gauge: one iso class, S3 isotropy.
split_v4 = ProductV4()
v4_sections = section_pairs(split_v4)
v4_params = sorted(b_parameter(s) for s in v4_sections)
assert v4_params == [0, 1, 2, 3]

# All linear automorphisms of F2^2 are permutations of {1,2,3} fixing 0.
linear_maps = []
for perm_nonzero in permutations((1, 2, 3)):
    table = {0: 0, 1: perm_nonzero[0], 2: perm_nonzero[1], 3: perm_nonzero[2]}
    if all(table[x ^ y] == (table[x] ^ table[y]) for x in range(4) for y in range(4)):
        linear_maps.append(table)
assert len(linear_maps) == 6

v4_gauge = []
for table in linear_maps:
    for w in range(4):
        v4_gauge.append(
            (lambda table=table, w=w: (lambda x: table[x] ^ w))()
        )
assert len(v4_gauge) == 24
fp_v4 = groupoid_fingerprint(v4_params, v4_gauge)
assert fp_v4["objects"] == 4
assert fp_v4["pi0"] == 1
assert fp_v4["stabilizers"] == [6, 6, 6, 6]

# Non-split parity pullback: same 48/2/24 cardinality profile as split C2,
# but the single frozen b^2 relation already carries unavoidable kernel residue.
nonsplit = ParityC4Pullback()
nonsplit_sections = section_pairs(nonsplit)
assert len(nonsplit.elements) == len(split_c2.elements) == 48
assert len(nonsplit.kernel()) == len(split_c2.kernel()) == 2
assert len(nonsplit.fiber(A0)) == len(nonsplit.fiber(B0)) == 2
assert len(nonsplit_sections) == 0

central_residue = (2, ID4)
for B in nonsplit.fiber(B0):
    assert nonsplit.power(B, 2) == central_residue
    assert nonsplit.power(B, 4) == nonsplit.id
for B in split_c2.fiber(B0):
    assert split_c2.power(B, 2) == split_c2.id

# a-residue can be killed in the non-split model, but b-residue cannot.
a_residues = sorted({nonsplit.power(A, 3)[0] for A in nonsplit.fiber(A0)})
b_residues = sorted({nonsplit.power(B, 2)[0] for B in nonsplit.fiber(B0)})
ab_residues = sorted({
    nonsplit.power(nonsplit.mul(A, B), 4)[0]
    for A in nonsplit.fiber(A0)
    for B in nonsplit.fiber(B0)
})
assert a_residues == [0, 2]
assert b_residues == [2]
assert ab_residues == [0]

# Logical-strength boundary:
# "every pair is isomorphic" is vacuously true for empty groupoid, whereas
# "exactly one isomorphism class" is false. Once nonempty, the two coincide.
fp_empty = groupoid_fingerprint([], [lambda x: x])
assert fp_empty["vacuous_all_pairwise_isomorphic"] is True
assert fp_empty["unique_iso_class"] is False
for fp in (fp_gen12, fp_c2, fp_c2_frozen, fp_c3, fp_v4):
    assert fp["nonempty_pairwise_isomorphic"] == fp["unique_iso_class"]

# Model-isomorphism invariance regression at the finite action-groupoid level:
# conjugating the V4 object labels by any bijection preserves objects/pi0/isotropy.
relabel = {0: 2, 1: 3, 2: 0, 3: 1}
rinv = {v: k for k, v in relabel.items()}
conjugated_gauge = []
for f in v4_gauge:
    conjugated_gauge.append(
        (lambda f=f: (lambda x: relabel[f(rinv[x])]))()
    )
fp_v4_relabel = groupoid_fingerprint(sorted(relabel[x] for x in v4_params), conjugated_gauge)
assert fp_v4_relabel == fp_v4

print("PASS P000_PHILOSOPHY_FIRST_LIFT_GROUPOID_CHECK")
print("carrier_S4_order=24")
print("gen12=objects:1,pi0:1,isotropy:1")
print("split_C2_torsor=objects:2,pi0:1,isotropy:1")
print("split_C2_frozen_gauge=objects:2,pi0:2")
print("split_C3=objects:1,pi0:1,isotropy:2")
print("split_V4_affine=objects:4,pi0:1,isotropy:6")
print("nonsplit_C4_parity=objects:0,b2_residue:central_kernel_2")
print("minimal_difference=split_C2_vs_parity_C4_pullback_same_48_2_24_profile_single_b2_relation")
print("strength_boundary=pairwise_isomorphic_vacuous_on_empty;nonempty_pairwise_iff_unique_pi0")
print("model_isomorphism_invariance=PASS")
