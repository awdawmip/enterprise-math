#!/usr/bin/env python3
"""Exact checker for centered-X6 fixed-radius / C6->C12 rotation microtrace results.

Research scope:
- current signed X6 Cell-center Foundation;
- current FCC/K4 four-STAR carrier atlas;
- local C6 phase adjacency induced by 60-degree carrier-neighbor directions;
- native primitive transitions are signed unit-axis steps in Z^6.

No floating-point geometry is used.
"""

from itertools import combinations, product
from math import factorial

V = {
    1: (1, 1, 0),
    2: (1, -1, 0),
    3: (1, 0, 1),
    4: (1, 0, -1),
    5: (0, 1, 1),
    6: (0, 1, -1),
}

STARS = {
    "A": {1, 3, 6},
    "B": {1, 4, 5},
    "C": {2, 3, 5},
    "D": {2, 4, 6},
}


def dot3(a, b):
    return sum(x * y for x, y in zip(a, b))


def signed_carrier_vector(direction):
    line, sign = direction
    return tuple(sign * x for x in V[line])


def carrier_dot(a, b):
    return dot3(signed_carrier_vector(a), signed_carrier_vector(b))


def native_vector(direction):
    line, sign = direction
    z = [0] * 6
    z[line - 1] = sign
    return tuple(z)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def norm2(a):
    return sum(x * x for x in a)


def support(a):
    return sum(x != 0 for x in a)


def l1(a):
    return sum(abs(x) for x in a)


def shortest_path_multiplicity(delta):
    m = l1(delta)
    out = factorial(m)
    for c in delta:
        out //= factorial(abs(c))
    return out


def c6_adjacency(star):
    directions = [(line, sign) for line in sorted(STARS[star]) for sign in (1, -1)]
    adjacency = {d: [] for d in directions}
    for a, b in combinations(directions, 2):
        # All listed FCC representatives have norm^2 = 2.
        # Dot = 1 is therefore exactly a 60-degree carrier angle.
        if carrier_dot(a, b) == 1:
            adjacency[a].append(b)
            adjacency[b].append(a)
    assert all(len(adjacency[d]) == 2 for d in directions)
    return adjacency


def one_chiral_cycle(star):
    adjacency = c6_adjacency(star)
    start = next(iter(adjacency))
    nxt = adjacency[start][0]
    cycle = [start, nxt]
    prev, cur = start, nxt
    while True:
        candidates = [d for d in adjacency[cur] if d != prev]
        assert len(candidates) == 1
        nxt = candidates[0]
        if nxt == start:
            break
        cycle.append(nxt)
        prev, cur = cur, nxt
    assert len(cycle) == 6
    assert len(set(cycle)) == 6
    return cycle


def check_shell_independence():
    # Exact identity for a primitive step x -> x + eps e_i:
    # ||x + eps e_i||^2 - ||x||^2 = 2 eps x_i + 1,
    # an odd integer and therefore never zero.
    for xi in range(-100, 101):
        for eps in (-1, 1):
            delta = 2 * eps * xi + 1
            assert delta != 0
            assert delta % 2 != 0

    # Small finite regression in a Z^3 restriction.
    for x in product(range(-2, 3), repeat=3):
        x2 = sum(t * t for t in x)
        for i in range(3):
            for eps in (-1, 1):
                y = list(x)
                y[i] += eps
                assert sum(t * t for t in y) != x2


def check_star_cycles_and_brc():
    cycles = {}
    for star in STARS:
        cycle = one_chiral_cycle(star)
        cycles[star] = cycle
        adjacency = c6_adjacency(star)
        assert set(cycle) == set(adjacency)

        outer_intermediates = []
        microcycle = []
        for k, a in enumerate(cycle):
            b = cycle[(k + 1) % 6]
            na, nb = native_vector(a), native_vector(b)
            delta = sub(nb, na)

            # Macro endpoints are both on the native unit shell.
            assert norm2(na) == 1
            assert norm2(nb) == 1

            # An adjacent local C6 phase change is a two-axis composite displacement.
            assert support(delta) == 2
            assert l1(delta) == 2
            assert shortest_path_multiplicity(delta) == 2

            inner = (0, 0, 0, 0, 0, 0)
            outer = add(na, nb)

            # The two shortest native realizations are exactly:
            #   a -> 0 -> b
            #   a -> a+b -> b
            assert sub(inner, na) == neg(na)
            assert sub(nb, inner) == nb
            assert sub(outer, na) == nb
            assert sub(nb, outer) == neg(na)
            assert support(sub(inner, na)) == 1
            assert support(sub(nb, inner)) == 1
            assert support(sub(outer, na)) == 1
            assert support(sub(nb, outer)) == 1
            assert norm2(inner) == 0
            assert norm2(outer) == 2
            outer_intermediates.append(outer)

            # All-outer choice gives a native 12-Cell primitive cycle.
            microcycle.append(na)
            microcycle.append(outer)

            # The outer Cell lies on the same carrier ray as the C12 bisector/gate.
            ua, ub = signed_carrier_vector(a), signed_carrier_vector(b)
            w = tuple(ua[i] + ub[i] for i in range(3))
            assert dot3(ua, ua) == 2
            assert dot3(ub, ub) == 2
            assert dot3(ua, ub) == 1
            assert dot3(w, w) == 6
            assert dot3(ua, w) == 3
            # cos^2(half-angle) = 9/(2*6) = 3/4 = (sqrt(3)/2)^2.
            assert 4 * dot3(ua, w) ** 2 == 3 * dot3(ua, ua) * dot3(w, w)

        assert len(set(outer_intermediates)) == 6
        assert len(microcycle) == 12
        assert len(set(microcycle)) == 12
        for u, w in zip(microcycle, microcycle[1:] + microcycle[:1]):
            step = sub(w, u)
            assert support(step) == 1
            assert l1(step) == 1

    return cycles


def check_star_frame_memory(cycles):
    line_stars = {line: [] for line in range(1, 7)}
    for star, lines in STARS.items():
        for line in lines:
            line_stars[line].append(star)

    # Every line family belongs to exactly two STAR slices: one unresolved frame bit.
    assert all(len(stars) == 2 for stars in line_stars.values())

    for line in range(1, 7):
        s1, s2 = line_stars[line]
        other1 = STARS[s1] - {line}
        other2 = STARS[s2] - {line}
        # After fixing the current line, the two candidate STARs have disjoint
        # possible next line families. A sweep bit alone therefore cannot erase frame.
        assert other1.isdisjoint(other2)

        # Conversely, any valid adjacent previous/current line pair identifies
        # the unique STAR frame containing both.
        for star in (s1, s2):
            for previous_line in STARS[star] - {line}:
                common = [
                    candidate
                    for candidate, lines in STARS.items()
                    if line in lines and previous_line in lines
                ]
                assert common == [star]

    # Same macro endpoints do not determine the inner/outer BRC path branch.
    for star, cycle in cycles.items():
        for k, a in enumerate(cycle):
            b = cycle[(k + 1) % 6]
            na, nb = native_vector(a), native_vector(b)
            inner = (0, 0, 0, 0, 0, 0)
            outer = add(na, nb)
            assert inner != outer
            assert norm2(inner) == 0
            assert norm2(outer) == 2


def check_c24_single_cell_ray_no_go():
    # In a triangular carrier basis u=(1,0), v=(1/2,sqrt(3)/2), any lattice ray
    # p*u + q*v has tan(theta)=q*sqrt(3)/(2p+q).
    # Setting theta=15 degrees, tan(15)=2-sqrt(3), gives
    # q*sqrt(3)=(2p+q)(2-sqrt(3)). Comparing Q(sqrt(3)) coefficients:
    # 2(2p+q)=0 and q=-(2p+q), hence p=q=0.
    solutions = []
    for p in range(-100, 101):
        for q in range(-100, 101):
            if 2 * (2 * p + q) == 0 and q == -(2 * p + q):
                solutions.append((p, q))
    assert solutions == [(0, 0)]


def main():
    check_shell_independence()
    cycles = check_star_cycles_and_brc()
    check_star_frame_memory(cycles)
    check_c24_single_cell_ray_no_go()
    print("PASS: centered-X6 fixed-radius/C12 microtrace checks")
    for star in sorted(cycles):
        print(f"STAR {star}: {cycles[star]}")


if __name__ == "__main__":
    main()
