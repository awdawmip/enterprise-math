#!/usr/bin/env python3
"""Exact K4 overlap-connection classification inside the current S4<S6 skeleton.

Extends the existing Euler FCC chirality cochain by realizing every edge bit as
one of exactly two overlap-fixing S4 axis permutations.
"""

from __future__ import annotations

from itertools import combinations, permutations
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
SRC = REPO_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from enterprise_math.euler_fcc_chirality import (  # noqa: E402
    ALL_ODD_FACES,
    ANTIBALANCED_EDGES,
    EDGES,
    ZERO_EDGES,
    ZERO_FACES,
    edge_assignments,
    face_holonomy,
)

V4 = tuple(range(4))
EDGE_INDEX = {edge: index for index, edge in enumerate(EDGES)}


def edge(a: int, b: int) -> tuple[int, int]:
    return tuple(sorted((a, b)))


def star(i: int) -> frozenset[tuple[int, int]]:
    return frozenset(edge(i, j) for j in V4 if j != i)


def transposition(a: int, b: int) -> tuple[int, ...]:
    p = list(V4)
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[x]] for x in V4)


def apply_edge_perm(p, e):
    return edge(p[e[0]], p[e[1]])


def support_size(p) -> int:
    return sum(index != value for index, value in enumerate(p))


def permutation_parity(p) -> int:
    return sum(
        p[a] > p[b]
        for a in range(4)
        for b in range(a + 1, 4)
    ) % 2


def complement_swap_transport(i: int, j: int) -> tuple[int, ...]:
    k, ell = [x for x in V4 if x not in (i, j)]
    return compose(transposition(i, j), transposition(k, ell))


def admissible_overlap_maps(i: int, j: int):
    """S4 maps S_i->S_j that fix the common line E_ij setwise."""
    out = []
    shared = edge(i, j)
    for p in permutations(V4):
        image_star = frozenset(apply_edge_perm(p, e) for e in star(i))
        if image_star != star(j):
            continue
        if apply_edge_perm(p, shared) != shared:
            continue
        out.append(tuple(p))
    return tuple(out)


def rotations3(t):
    return (t, (t[1], t[2], t[0]), (t[2], t[0], t[1]))


def same_cyclic(left, right) -> bool:
    return left in rotations3(right)


def opposite_cyclic(left, right) -> bool:
    return same_cyclic(left, (right[0], right[2], right[1]))


def boundary_star_cycle(i: int):
    face = [v for v in V4 if v != i]
    if i % 2:
        face[1], face[2] = face[2], face[1]
    return tuple(edge(i, v) for v in face)


def connection_map(i: int, j: int, edge_bit: int):
    """bit 1 = minimal-support transposition; bit 0 = remote-port swap."""
    if edge_bit not in (0, 1):
        raise ValueError("edge bit must be 0 or 1")
    return transposition(i, j) if edge_bit else complement_swap_transport(i, j)


def check_exact_two_overlap_maps():
    for i, j in EDGES:
        maps = admissible_overlap_maps(i, j)
        minus = transposition(i, j)
        plus = complement_swap_transport(i, j)
        assert set(maps) == {minus, plus}
        assert support_size(minus) == 2
        assert support_size(plus) == 4
        assert permutation_parity(minus) == 1
        assert permutation_parity(plus) == 0

        source = boundary_star_cycle(i)
        minus_image = tuple(apply_edge_perm(minus, e) for e in source)
        plus_image = tuple(apply_edge_perm(plus, e) for e in source)
        target = boundary_star_cycle(j)
        assert opposite_cyclic(minus_image, target)
        assert same_cyclic(plus_image, target)


def check_remote_port_semantics():
    for i, j in EDGES:
        k, ell = [x for x in V4 if x not in (i, j)]
        minus = transposition(i, j)
        plus = complement_swap_transport(i, j)

        # Minimal-support transport preserves each remote STAR port.
        assert apply_edge_perm(minus, edge(i, k)) == edge(j, k)
        assert apply_edge_perm(minus, edge(i, ell)) == edge(j, ell)

        # The other admissible transport swaps the two remote ports.
        assert apply_edge_perm(plus, edge(i, k)) == edge(j, ell)
        assert apply_edge_perm(plus, edge(i, ell)) == edge(j, k)


def check_all_64_connections_realize_euler_cochains():
    for bits in edge_assignments():
        for i, j, k in combinations(V4, 3):
            hol = compose(
                connection_map(k, i, bits[EDGE_INDEX[edge(k, i)]]),
                compose(
                    connection_map(j, k, bits[EDGE_INDEX[edge(j, k)]]),
                    connection_map(i, j, bits[EDGE_INDEX[edge(i, j)]]),
                ),
            )

            start = boundary_star_cycle(i)
            image = tuple(apply_edge_perm(hol, e) for e in start)
            assert frozenset(image) == star(i)

            face_bit = (
                bits[EDGE_INDEX[edge(i, j)]]
                ^ bits[EDGE_INDEX[edge(i, k)]]
                ^ bits[EDGE_INDEX[edge(j, k)]]
            )

            # The abstract Euler face bit is exactly the parity/orientation
            # character of the actual S4 loop permutation.
            assert permutation_parity(hol) == face_bit
            if face_bit:
                assert opposite_cyclic(image, start)
                assert support_size(hol) == 2  # visible transposition
            else:
                assert same_cyclic(image, start)
                assert support_size(hol) in (0, 3)  # identity or visible 3-cycle


def check_two_fully_symmetric_endpoints():
    # Minimal-support / remote-port-preserving connection.
    assert face_holonomy(ANTIBALANCED_EDGES) == ALL_ODD_FACES
    for i, j, k in combinations(V4, 3):
        hol = compose(
            transposition(k, i),
            compose(transposition(j, k), transposition(i, j)),
        )
        assert hol == transposition(j, k)

    # Remote-port-swapping connection.
    assert face_holonomy(ZERO_EDGES) == ZERO_FACES
    for i, j, k in combinations(V4, 3):
        hol = compose(
            complement_swap_transport(k, i),
            compose(
                complement_swap_transport(j, k),
                complement_swap_transport(i, j),
            ),
        )
        assert hol == tuple(V4)


def main():
    check_exact_two_overlap_maps()
    check_remote_port_semantics()
    check_all_64_connections_realize_euler_cochains()
    check_two_fully_symmetric_endpoints()

    print("PASS: exact K4 overlap-connection classification")
    print("each overlap has exactly two shared-line-fixing S4 transports")
    print("minimal support preserves remote ports and reverses chirality")
    print("double transposition swaps remote ports and preserves chirality")
    print("all 64 Euler edge cochains are realized by actual S4 axis permutations")
    print("face holonomy equals the parity/orientation character of loop transport")


if __name__ == "__main__":
    main()
