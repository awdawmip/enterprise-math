#!/usr/bin/env python3
"""Exact finite checker for #1158 C3/C2 holonomy and root-section independence.

This is a regression certificate for the finite claims in
research_notes/VIETE_C3_C2_HOLONOMY_NATIVE_PROMOTION_BOUNDARY_20260904.md.
It does not promote the tested cycle-cover model to native Foundation truth.
"""

from itertools import product

BITS = (0, 1)


def hol(a):
    h = 0
    for bit in a:
        h ^= bit
    return h


def cover_next(n, a, state):
    k, sheet = state
    return ((k + 1) % n, sheet ^ a[k])


def cover_components(n, a):
    states = {(k, s) for k in range(n) for s in BITS}
    comps = []
    while states:
        x0 = next(iter(states))
        orbit = []
        x = x0
        while x not in orbit:
            orbit.append(x)
            x = cover_next(n, a, x)
        comp = set(orbit)
        comps.append(comp)
        states -= comp
    return sorted(len(c) for c in comps)


def gauge_packet(a, g):
    n = len(a)
    return tuple(a[i] ^ g[i] ^ g[(i + 1) % n] for i in range(n))


def cycle_distance(n, k):
    k %= n
    return min(k, n - k)


def lifts(n, k):
    k %= n
    return (k, k + n)


def root_sections(n, k):
    ys = lifts(n, k)
    ds = [cycle_distance(2 * n, y) for y in ys]
    if ds[0] == ds[1]:
        return {"tie": tuple(sorted(ys)), "near": None, "far": None}
    near_i = 0 if ds[0] < ds[1] else 1
    far_i = 1 - near_i
    return {"tie": None, "near": ys[near_i], "far": ys[far_i]}


def neg(modulus, x):
    return (-x) % modulus


def run():
    checks = 0

    # Exact C3 transport census: two gauge orbits, classified by XOR holonomy.
    packets = list(product(BITS, repeat=3))
    gauges = list(product(BITS, repeat=3))
    orbits = []
    unseen = set(packets)
    while unseen:
        a = next(iter(unseen))
        o = {gauge_packet(a, g) for g in gauges}
        orbits.append(o)
        unseen -= o
    assert len(orbits) == 2
    assert sorted(len(o) for o in orbits) == [4, 4]
    assert {hol(next(iter(o))) for o in orbits} == {0, 1}
    checks += 3

    for a in packets:
        for g in gauges:
            assert hol(gauge_packet(a, g)) == hol(a)
            checks += 1

    for a in packets:
        comps = cover_components(3, a)
        if hol(a) == 0:
            assert comps == [3, 3]
        else:
            assert comps == [6]
        checks += 1

    # Matched homogeneous representatives used in the note.
    assert cover_components(3, (0, 0, 0)) == [3, 3]
    assert cover_components(3, (1, 1, 1)) == [6]
    checks += 2

    # On a path/tree, all edge packets are gauge equivalent: verify for 2-edge path.
    path_packets = list(product(BITS, repeat=2))
    path_gauges = list(product(BITS, repeat=3))

    def path_gauge(a, g):
        return (a[0] ^ g[0] ^ g[1], a[1] ^ g[1] ^ g[2])

    path_orbits = {
        frozenset(path_gauge(a, g) for g in path_gauges)
        for a in path_packets
    }
    assert len(path_orbits) == 1
    checks += 1

    # Connected double cover does not determine the root section.
    # Both near and far sections are inversion-equivariant away from antipodal ties.
    # Only the near section halves normalized Cayley distance exactly.
    root_cases = 0
    tie_cases = 0
    far_halving_accidents = 0
    for n in range(3, 65):
        for k in range(n):
            sec = root_sections(n, k)
            if sec["tie"] is not None:
                # The only tie is the coarse half-turn, when n is even.
                assert n % 2 == 0 and k == n // 2
                ys = sec["tie"]
                assert neg(2 * n, ys[0]) == ys[1]
                tie_cases += 1
                checks += 2
                continue

            near = sec["near"]
            far = sec["far"]
            inv = root_sections(n, neg(n, k))
            assert inv["tie"] is None
            assert inv["near"] == neg(2 * n, near)
            assert inv["far"] == neg(2 * n, far)

            lhs_near_num = cycle_distance(2 * n, near)
            coarse_num = cycle_distance(n, k)
            # d_{2N}/(2N) = (1/2) d_N/N  <=> d_{2N}=d_N.
            assert lhs_near_num == coarse_num

            lhs_far_num = cycle_distance(2 * n, far)
            if lhs_far_num == coarse_num:
                far_halving_accidents += 1
            root_cases += 1
            checks += 4

    assert root_cases > 0
    assert tie_cases > 0
    assert far_halving_accidents == 0
    checks += 3

    return {
        "checks": checks,
        "c3_packets": len(packets),
        "c3_gauge_orbits": len(orbits),
        "h0_cover": "C3_disjoint_union_C3",
        "h1_cover": "C6",
        "path_transport_orbits": len(path_orbits),
        "root_cases": root_cases,
        "antipodal_ties": tie_cases,
        "far_halving_accidents": far_halving_accidents,
        "terminal": "HOLONOMY_AND_SHORTEST_ROOT_ARE_INDEPENDENT_NATIVE_EXTENSION_OBLIGATIONS",
    }


if __name__ == "__main__":
    result = run()
    for k, v in result.items():
        print(f"{k}={v}")
