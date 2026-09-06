#!/usr/bin/env python3
"""Exact checker for Viète K4/FCC root-holonomy atlas and C24 anchor.

This extends the existing Euler FCC chirality tool rather than reclassifying
the K4 switching system from scratch. New checks:
- natural K4 transposition atlas connection on the six X6 axis labels;
- tetrahedral-boundary orientation reversal on every STAR transition;
- triangle holonomy as an actual visible-axis transposition;
- principal +/-3 root coordinate uses the same C2 local system as Euler J;
- C12 character and C24 balanced spinor glue after the two sign flips cancel;
- the same sheet controls every finite principal precision level;
- the full 20-slice S6 kinematic orientation cover has 40 states and is minimal.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from math import gcd
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
SRC = REPO_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from enterprise_math.euler_fcc_chirality import (  # noqa: E402
    ALL_ODD_FACES,
    ANTIBALANCED_EDGES,
    edge_assignments,
    face_holonomy,
    globalizable,
    transition_bit,
    verify_antibalanced_cube_cover,
)

V4 = tuple(range(4))
K4_EDGES = tuple(combinations(V4, 2))


def edge(a: int, b: int) -> tuple[int, int]:
    if a == b:
        raise ValueError("K4 edge requires distinct vertices")
    return tuple(sorted((a, b)))


def star(i: int) -> frozenset[tuple[int, int]]:
    return frozenset(edge(i, j) for j in V4 if j != i)


def transposition(a: int, b: int, n: int = 4) -> tuple[int, ...]:
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return p o q."""
    return tuple(p[q[x]] for x in range(len(p)))


def apply_edge_perm(
    p: tuple[int, ...], e: tuple[int, int]
) -> tuple[int, int]:
    return edge(p[e[0]], p[e[1]])


def rotations3(t: tuple[object, object, object]):
    return (t, (t[1], t[2], t[0]), (t[2], t[0], t[1]))


def same_cyclic_orientation(
    left: tuple[object, object, object],
    right: tuple[object, object, object],
) -> bool:
    return left in rotations3(right)


def opposite_cyclic_orientation(
    left: tuple[object, object, object],
    right: tuple[object, object, object],
) -> bool:
    reversed_right = (right[0], right[2], right[1])
    return same_cyclic_orientation(left, reversed_right)


def boundary_star_cycle(i: int) -> tuple[tuple[int, int], ...]:
    """STAR cyclic orientation induced from boundary of [0,1,2,3]."""
    face = [v for v in V4 if v != i]
    # Boundary sign (-1)^i. Encode a minus sign by reversing face orientation.
    if i % 2:
        face[1], face[2] = face[2], face[1]
    return tuple(edge(i, v) for v in face)


def check_k4_transposition_connection():
    for i, j in K4_EDGES:
        p = transposition(i, j)
        assert frozenset(apply_edge_perm(p, e) for e in star(i)) == star(j)
        assert apply_edge_perm(p, edge(i, j)) == edge(i, j)

        other = [v for v in V4 if v not in (i, j)]
        for k in other:
            assert apply_edge_perm(p, edge(i, k)) == edge(j, k)

        image_cycle = tuple(
            apply_edge_perm(p, e) for e in boundary_star_cycle(i)
        )
        assert opposite_cyclic_orientation(image_cycle, boundary_star_cycle(j))
        assert not same_cyclic_orientation(image_cycle, boundary_star_cycle(j))

    # Hence the natural connection is the all-negative K4 edge system.
    assert face_holonomy(ANTIBALANCED_EDGES) == ALL_ODD_FACES
    assert not globalizable(ANTIBALANCED_EDGES)
    cube = verify_antibalanced_cube_cover()
    assert cube["signed_slice_states"] == 8
    assert cube["cube_vertices"] == 8
    assert cube["cover_edges"] == 12


def check_triangle_holonomy_is_visible_transposition():
    for i, j, k in combinations(V4, 3):
        # Path i -> j -> k -> i.
        hol = compose(
            transposition(k, i),
            compose(transposition(j, k), transposition(i, j)),
        )
        assert hol == transposition(j, k)

        # It fixes the starting STAR as a set but reverses its local cycle.
        start_cycle = boundary_star_cycle(i)
        image_cycle = tuple(apply_edge_perm(hol, e) for e in start_cycle)
        assert frozenset(image_cycle) == star(i)
        assert opposite_cyclic_orientation(image_cycle, start_cycle)


def solve_root_signs(edges) -> tuple[tuple[int, ...], ...]:
    """All eps_i in +/-1 satisfying eps_j=(-1)^e_ij eps_i."""
    sols = []
    for eps in product((-1, 1), repeat=4):
        ok = True
        for i, j in K4_EDGES:
            expected = (-1 if transition_bit(edges, i, j) else 1) * eps[i]
            if eps[j] != expected:
                ok = False
                break
        if ok:
            sols.append(eps)
    return tuple(sols)


def check_root_sign_local_system_is_euler_chirality():
    flat_count = 0
    nonflat_count = 0
    for edges in edge_assignments():
        sols = solve_root_signs(edges)
        if globalizable(edges):
            flat_count += 1
            assert len(sols) == 2
        else:
            nonflat_count += 1
            assert len(sols) == 0
    assert flat_count == 8
    assert nonflat_count == 56

    # On the natural all-negative connection, every chart change flips both
    # local sweep/root sign and local J basis sign.
    for i, j in K4_EDGES:
        e = transition_bit(ANTIBALANCED_EDGES, i, j)
        assert e == 1
        sign = -1 if e else 1
        for eps_i in (-1, 1):
            eps_j = sign * eps_i

            # Source J_i expressed in target basis is sign * J_j.
            # Therefore K=eps*J is atlas-invariant.
            source_K_in_target = eps_i * sign
            target_K = eps_j
            assert source_K_in_target == target_K


def mul_cplx_pair(
    x: tuple[int, int], y: tuple[int, int]
) -> tuple[int, int]:
    """Multiply a+bJ and c+dJ with J^2=-1."""
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c


def check_c24_balanced_spinor_no_new_sheet():
    for i, j in K4_EDGES:
        e = transition_bit(ANTIBALANCED_EDGES, i, j)
        sign = -1 if e else 1
        for eps_i in (-1, 1):
            eps_j = sign * eps_i

            # Transport 1 + eps_i J_i to target basis J_j.
            transported_numerator = (1, eps_i * sign)
            target_numerator = (1, eps_j)
            assert transported_numerator == target_numerator

            # ((1+eps J)/sqrt(2))^2 = eps J.
            square_num = mul_cplx_pair(target_numerator, target_numerator)
            assert square_num == (0, 2 * eps_j)

            # Sweep reversal produces inverse spinor: U(eps) U(-eps) = 1.
            inverse_num = (1, -eps_j)
            product_num = mul_cplx_pair(target_numerator, inverse_num)
            assert product_num == (2, 0)


def modulus(m: int) -> int:
    return 6 * (2**m)


def order_mod(x: int, n: int) -> int:
    return n // gcd(x % n, n)


def check_all_level_principal_sheet():
    for m in range(12):
        n = modulus(m)
        plus = 3 % n
        minus = (-3) % n
        assert order_mod(plus, n) == 2 ** (m + 1)
        assert order_mod(minus, n) == 2 ** (m + 1)
        if m == 0:
            assert plus == minus
        else:
            assert plus != minus
            assert minus == (-plus) % n

        if m > 0:
            prev = modulus(m - 1)
            assert plus % prev == 3 % prev
            assert minus % prev == (-3) % prev


def normalize_cycle3(cycle: tuple[int, int, int]) -> tuple[int, int, int]:
    return min(rotations3(cycle))


def canonical_orientations(s: tuple[int, int, int]):
    a, b, c = sorted(s)
    pos = normalize_cycle3((a, b, c))
    neg = normalize_cycle3((a, c, b))
    assert pos != neg
    return pos, neg


def all_oriented_slices6():
    states = []
    for s in combinations(range(6), 3):
        states.extend(canonical_orientations(s))
    return tuple(states)


def apply_cycle_perm(
    p: tuple[int, ...], cycle: tuple[int, int, int]
) -> tuple[int, int, int]:
    return normalize_cycle3(tuple(p[x] for x in cycle))


def check_full_s6_orientation_cover():
    perms6 = tuple(permutations(range(6)))
    base_s = (0, 1, 2)
    base_o = canonical_orientations(base_s)[0]
    all_states = set(all_oriented_slices6())
    assert len(all_states) == 40

    orbit = {apply_cycle_perm(p, base_o) for p in perms6}
    assert orbit == all_states

    base_set = frozenset(base_s)
    base_stab = [
        p for p in perms6 if frozenset(p[x] for x in base_s) == base_set
    ]
    oriented_stab = [p for p in perms6 if apply_cycle_perm(p, base_o) == base_o]
    assert len(base_stab) == 36
    assert len(oriented_stab) == 18

    # A visible transposition fixes the base slice but flips its orientation.
    flip = transposition(0, 1, n=6)
    assert frozenset(flip[x] for x in base_s) == base_set
    assert apply_cycle_perm(flip, base_o) == canonical_orientations(base_s)[1]

    # Therefore no S6-equivariant section of the 2:1 orientation cover can
    # choose one orientation on every underlying 3-subset.
    assert flip in base_stab
    assert flip not in oriented_stab


def check_four_star_cover_is_eight_state_orbit():
    # S4 acts on the oriented STAR cycles. There are exactly 4*2=8 states.
    perms4 = tuple(permutations(V4))
    base = boundary_star_cycle(0)

    def apply_star_cycle(p, cycle):
        return normalize_cycle3(tuple(apply_edge_perm(p, e) for e in cycle))

    orbit = {apply_star_cycle(p, base) for p in perms4}
    expected = set()
    for i in V4:
        cycle = boundary_star_cycle(i)
        pos = normalize_cycle3(cycle)
        neg = normalize_cycle3((cycle[0], cycle[2], cycle[1]))
        expected.add(pos)
        expected.add(neg)
    assert len(expected) == 8
    assert orbit == expected


def main():
    check_k4_transposition_connection()
    check_triangle_holonomy_is_visible_transposition()
    check_root_sign_local_system_is_euler_chirality()
    check_c24_balanced_spinor_no_new_sheet()
    check_all_level_principal_sheet()
    check_full_s6_orientation_cover()
    check_four_star_cover_is_eight_state_orbit()

    print("PASS: Viète FCC/K4 root atlas + C24 anchor")
    print("natural K4 transposition connection -> all-negative / face holonomy 1111")
    print("triangle holonomy is an actual visible-axis transposition")
    print("Viète +/-3 root sign uses the Euler chirality local system")
    print("C24 balanced spinor glues with no additional atlas bit")
    print("full 20-slice S6 orientation cover has 40 states; no equivariant base section")


if __name__ == "__main__":
    main()
