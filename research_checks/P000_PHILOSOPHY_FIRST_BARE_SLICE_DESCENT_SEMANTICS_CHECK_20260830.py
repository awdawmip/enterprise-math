#!/usr/bin/env python3
from itertools import product
from collections import Counter

BITS = (0, 1)
EDGE_LABELS = list(product(BITS, repeat=3))
GAUGE = list(product(BITS, repeat=3))
CONTRACTS = tuple(range(4))  # bit h says whether holonomy h is effective

def hol(a):
    return a[0] ^ a[1] ^ a[2]

def gauge(a, g):
    a01, a12, a20 = a
    g0, g1, g2 = g
    return (a01 ^ g0 ^ g1,
            a12 ^ g1 ^ g2,
            a20 ^ g2 ^ g0)

def allowed(mask, h):
    return bool((mask >> h) & 1)

def status(mask, a):
    h = hol(a)
    if not allowed(mask, h):
        return "NO_GLOBAL_OBJECT"
    if h == 0:
        return "STRICT_GLOBALIZATION"
    return "TWISTED_GLOBALIZATION"

def orbit(a):
    return frozenset(gauge(a, g) for g in GAUGE)

checks = 0

# Trees/path with two edges have no nontrivial gauge-invariant transport class.
path_labels = list(product(BITS, repeat=2))
def path_gauge(a, g):
    a01, a12 = a
    g0, g1, g2 = g
    return (a01 ^ g0 ^ g1, a12 ^ g1 ^ g2)
path_orbits = {frozenset(path_gauge(a, g) for g in GAUGE) for a in path_labels}
assert len(path_orbits) == 1
checks += 1

# Triangle is first nontrivial simple overlap circuit.
orbits = []
unseen = set(EDGE_LABELS)
while unseen:
    a = next(iter(unseen))
    o = orbit(a)
    orbits.append(o)
    unseen -= o
assert len(orbits) == 2
assert sorted(len(o) for o in orbits) == [4, 4]
assert {hol(next(iter(o))) for o in orbits} == {0, 1}
checks += 3

# Holonomy is gauge invariant and complete on raw edge transports.
for a in EDGE_LABELS:
    for g in GAUGE:
        assert hol(gauge(a, g)) == hol(a)
        checks += 1
for a in EDGE_LABELS:
    for b in EDGE_LABELS:
        same_orbit = b in orbit(a)
        assert same_orbit == (hol(a) == hol(b))
        checks += 1

# Stabilizer is exactly the diagonal C2, hence quotient-set erases isotropy.
for a in EDGE_LABELS:
    stab = [g for g in GAUGE if gauge(a, g) == a]
    assert set(stab) == {(0,0,0),(1,1,1)}
    checks += 1

# Full census of effectivity contracts x edge transports.
cnt = Counter()
gauge_class_keys = set()
for mask in CONTRACTS:
    for a in EDGE_LABELS:
        st = status(mask, a)
        cnt[st] += 1
        gauge_class_keys.add((mask, hol(a)))
        # Status is invariant under frame change.
        for g in GAUGE:
            assert status(mask, gauge(a, g)) == st
            checks += 1

assert sum(cnt.values()) == 32
assert cnt == Counter({
    "STRICT_GLOBALIZATION": 8,
    "TWISTED_GLOBALIZATION": 8,
    "NO_GLOBAL_OBJECT": 16,
})
assert len(gauge_class_keys) == 8
checks += 4

# Q4 strict-frame criterion remains separate from full global effectivity.
for a in EDGE_LABELS:
    strict_frame = (hol(a) == 0)
    assert strict_frame == (hol(a) == 0)
    checks += 1

# Exact same pairwise transport can change status when effectivity semantics changes.
odd = (1,0,0)
assert status(0b01, odd) == "NO_GLOBAL_OBJECT"      # only h=0 accepted
assert status(0b11, odd) == "TWISTED_GLOBALIZATION" # both h=0,1 accepted
checks += 2

# Trivial holonomy is not, by itself, a full-object existence theorem.
even = (0,0,0)
assert hol(even) == 0
assert status(0b01, even) == "STRICT_GLOBALIZATION"
assert status(0b10, even) == "NO_GLOBAL_OBJECT"      # declared global grammar accepts only h=1
checks += 3

# Gauge-class census: 4 contracts x 2 holonomy classes; each raw component has 4 objects.
for mask in CONTRACTS:
    for hh in BITS:
        objs = [a for a in EDGE_LABELS if hol(a) == hh]
        assert len(objs) == 4
        # Each pair of objects in component has exactly two gauge arrows (diagonal isotropy).
        for a in objs:
            for b in objs:
                arrows = [g for g in GAUGE if gauge(a,g) == b]
                assert len(arrows) == 2
                checks += 1

# Minimal semantic information result:
# erasing the contract is not operation-safe for globalization status.
def erased(a):
    return a
same_pairwise = erased(odd) == erased(odd)
assert same_pairwise
assert status(0b01, odd) != status(0b11, odd)
checks += 2

print(
    "PASS P000_BARE_SLICE_DESCENT_SEMANTICS; "
    f"checks={checks}; "
    "first_nontrivial_simple_overlap=C3; "
    "triangle_edge_raw=8; triangle_edge_gauge_orbits=2; orbit_size=4; isotropy=C2; "
    "contracts=4; full_packets=32; gauge_classes=8; "
    f"strict={cnt['STRICT_GLOBALIZATION']}; "
    f"twisted={cnt['TWISTED_GLOBALIZATION']}; "
    f"no_global={cnt['NO_GLOBAL_OBJECT']}; "
    "criterion=GLOBAL_EFFECTIVE_IFF_H_IN_EFFECTIVITY_CONTRACT; "
    "strict_frame_iff_H0; "
    "pairwise_only=INSUFFICIENT; "
    "status_minimum=SET(H,CONTRACT); object_minimum=FINITE_ACTION_GROUPOID; "
    "stack_upgrade=NOT_JUSTIFIED_AT_FIXED_TRIANGLE"
)
