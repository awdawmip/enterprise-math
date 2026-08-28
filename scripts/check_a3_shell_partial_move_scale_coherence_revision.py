#!/usr/bin/env python3
"""Exact checker for RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION.

Pure-stdlib exact replay for the declared prefix-support semantics. The symbolic
proof is frozen in the accompanying research artifact; this checker is a
finite exact regression over the S4 frame action and the smallest relevant
nested A3 carriers.
"""
from __future__ import annotations

import json
from itertools import permutations, product

Perm = tuple[int, int, int, int]
Vec = tuple[int, int, int, int]

G: tuple[Perm, ...] = tuple(permutations(range(4)))
E: Perm = (0, 1, 2, 3)
SWAP12: Perm = (1, 0, 2, 3)
SWAP23: Perm = (0, 2, 1, 3)


def parity(p: Perm) -> int:
    inv = sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j])
    return 1 if inv % 2 == 0 else -1


def compose(p: Perm, q: Perm) -> Perm:
    """Return p after q."""
    return tuple(p[q[i]] for i in range(4))


def inverse(p: Perm) -> Perm:
    out = [0] * 4
    for i, image in enumerate(p):
        out[image] = i
    return tuple(out)  # type: ignore[return-value]


def r_act(p: Perm, x: Vec) -> Vec:
    """Faithful sign-twisted A3 frame action R_p = sgn(p) P_p."""
    y = [0] * 4
    for i, value in enumerate(x):
        y[p[i]] = value
    s = parity(p)
    return tuple(s * value for value in y)  # type: ignore[return-value]


def radius(x: Vec) -> int:
    return max(abs(value) for value in x)


def ball(n: int) -> tuple[Vec, ...]:
    out: list[Vec] = []
    for x1, x2, x3 in product(range(-n, n + 1), repeat=3):
        x4 = -(x1 + x2 + x3)
        x = (x1, x2, x3, x4)
        if abs(x4) <= n:
            out.append(x)
    return tuple(sorted(out))


def shell(n: int) -> tuple[Vec, ...]:
    if n <= 0:
        return tuple()
    prev = set(ball(n - 1))
    return tuple(x for x in ball(n) if x not in prev)


def anchor(n: int) -> Vec:
    return (n, -n, 0, 0)


def stabilizer(x: Vec) -> tuple[Perm, ...]:
    return tuple(g for g in G if r_act(g, x) == x)


def d_act(n: int, depth: int, g: Perm, x: Vec) -> Vec:
    """D_{n,d}: rotate exactly U_{n,d}=B_n\B_{n-d}."""
    if not (1 <= depth <= n):
        raise ValueError("require 1 <= depth <= n")
    if radius(x) > n:
        raise ValueError("state point outside B_n")
    return r_act(g, x) if radius(x) >= n - depth + 1 else x


def restricted_upper_act(n: int, depth: int, g: Perm, x: Vec) -> Vec:
    """Restriction to B_n of D_{n+1,d}."""
    if not (1 <= depth <= n):
        raise ValueError("require 1 <= depth <= n")
    if radius(x) > n:
        raise ValueError("state point outside B_n")
    return r_act(g, x) if radius(x) >= n - depth + 2 else x


def j_act(n: int, depth: int, g: Perm, x: Vec) -> Vec:
    """Support-transition action J_{n,d}(g)."""
    if not (1 <= depth <= n):
        raise ValueError("require 1 <= depth <= n")
    if radius(x) > n:
        raise ValueError("state point outside B_n")
    return r_act(g, x) if radius(x) == n - depth + 1 else x


def raw_defect(n: int, depth: int, low: Perm, high: Perm, x: Vec) -> Vec:
    """F_{n,d}(low,high)=D_low * restricted(D_high)^-1."""
    y = restricted_upper_act(n, depth, inverse(high), x)
    return d_act(n, depth, low, y)


def factored_defect(n: int, depth: int, low: Perm, high: Perm, x: Vec) -> Vec:
    rel = compose(low, inverse(high))
    y = restricted_upper_act(n, depth, rel, x)
    return j_act(n, depth, low, y)


def left_coset(H: tuple[Perm, ...], g: Perm) -> tuple[Perm, ...]:
    return tuple(sorted({compose(h, g) for h in H}))


def all_left_cosets(H: tuple[Perm, ...]) -> tuple[tuple[Perm, ...], ...]:
    seen: set[Perm] = set()
    out: list[tuple[Perm, ...]] = []
    for g in sorted(G):
        if g in seen:
            continue
        L = left_coset(H, g)
        seen.update(L)
        out.append(L)
    return tuple(out)


def double_coset(H: tuple[Perm, ...], g: Perm) -> frozenset[Perm]:
    return frozenset(
        compose(compose(h1, g), h2)
        for h1 in H
        for h2 in H
    )


def double_cosets(H: tuple[Perm, ...]) -> tuple[frozenset[Perm], ...]:
    seen: set[Perm] = set()
    out: list[frozenset[Perm]] = []
    for g in sorted(G):
        if g in seen:
            continue
        C = double_coset(H, g)
        seen.update(C)
        out.append(C)
    return tuple(out)


def map_state(points: tuple[Vec, ...], action) -> tuple[Vec, ...]:
    return tuple(action(x) for x in points)


def residual_orbit(H: tuple[Perm, ...], x: Vec) -> frozenset[Vec]:
    return frozenset(r_act(h, x) for h in H)


def main() -> None:
    B = {n: ball(n) for n in range(5)}

    # Frozen carrier sizes sufficient for the corrected B2<B3<B4 prototype.
    assert tuple(len(B[n]) for n in range(5)) == (1, 19, 85, 231, 489)

    # Frame action preserves each ball and shell.
    for n in range(1, 5):
        target = set(B[n])
        for g in G:
            assert {r_act(g, x) for x in B[n]} == target
            assert {r_act(g, x) for x in shell(n)} == set(shell(n))

    H = stabilizer(anchor(2))
    assert set(H) == {E, SWAP12}
    for n in range(1, 5):
        assert set(stabilizer(anchor(n))) == set(H)

    D_checks = 0
    J_checks = 0
    factor_checks = 0
    faithful_checks = 0

    # Exact finite regression for all frames on the smallest carriers supporting
    # both depth 1 and depth 2. The general theorem is symbolic in the artifact.
    for n in (2, 3):
        for depth in range(1, n + 1):
            sites = B[n]
            for g in G:
                # J is exactly the action on the transition shell and identity elsewhere.
                for x in sites:
                    expected = r_act(g, x) if radius(x) == n - depth + 1 else x
                    assert j_act(n, depth, g, x) == expected

                # Nonidentity g cannot kill the transition shell action.
                transition = shell(n - depth + 1)
                fixes_transition = all(r_act(g, x) == x for x in transition)
                assert fixes_transition == (g == E)
                faithful_checks += 1

                for h in G:
                    gh = compose(g, h)
                    for x in sites:
                        assert d_act(n, depth, g, d_act(n, depth, h, x)) == d_act(
                            n, depth, gh, x
                        )
                        D_checks += 1
                        assert j_act(n, depth, g, j_act(n, depth, h, x)) == j_act(
                            n, depth, gh, x
                        )
                        J_checks += 1
                        assert raw_defect(n, depth, g, h, x) == factored_defect(
                            n, depth, g, h, x
                        )
                        factor_checks += 1

    # Pair-groupoid frame projection is well-defined under representative choices.
    left = all_left_cosets(H)
    cosets = double_cosets(H)
    assert len(left) == 12
    assert len(cosets) == 7
    class_id = {g: i for i, C in enumerate(cosets) for g in C}
    pair_projection_checks = 0
    for L in left:
        for K in left:
            labels = {
                class_id[compose(u, inverse(v))]
                for u in L
                for v in K
            }
            assert len(labels) == 1
            pair_projection_checks += len(L) * len(K)

    # Mandatory Driver counterexample: edge B3 -> B2, depth 2, same g=(23).
    p = anchor(1)
    g = SWAP23
    upper_route = restricted_upper_act(2, 2, g, p)
    lower_route = d_act(2, 2, g, p)
    assert upper_route == p
    assert lower_route == (-1, 0, 1, 0)
    assert lower_route not in residual_orbit(H, upper_route)
    assert class_id[compose(g, inverse(g))] == class_id[E] == 0

    # Stronger frame-only collision: (H,H) and (Hg,Hg) both project to C0
    # but induce different transition-shell relations.
    id_arrow_maps = {
        raw_defect(2, 2, u, v, p)
        for u in left_coset(H, E)
        for v in left_coset(H, E)
    }
    g_arrow_maps = {
        raw_defect(2, 2, u, v, p)
        for u in left_coset(H, g)
        for v in left_coset(H, g)
    }
    assert id_arrow_maps != g_arrow_maps
    assert {class_id[compose(u, inverse(v))] for u in left_coset(H,E) for v in left_coset(H,E)} == {0}
    assert {class_id[compose(u, inverse(v))] for u in left_coset(H,g) for v in left_coset(H,g)} == {0}

    # Corrected uniform depth-2 three-radius prototype is B2<B3<B4.
    # Same aligner at all scales: old frame defects are C0,C0, but both
    # state-level squares fail because support shifts inward one shell per edge.
    q1 = anchor(1)
    q2 = anchor(2)
    upper_43 = restricted_upper_act(3, 2, g, q2)  # scale 4, then restrict to B3
    lower_43 = d_act(3, 2, g, q2)                 # restrict, then scale-3 align
    upper_32 = restricted_upper_act(2, 2, g, q1)  # scale 3, then restrict to B2
    lower_32 = d_act(2, 2, g, q1)                 # restrict, then scale-2 align
    assert upper_43 == q2 and lower_43 != q2
    assert upper_32 == q1 and lower_32 != q1
    assert lower_43 not in residual_orbit(H, upper_43)
    assert lower_32 not in residual_orbit(H, upper_32)

    # Defect maps really send the upper-path aligned state to lower-path aligned state.
    defect_state_checks = 0
    for n, x in ((3, q2), (2, q1)):
        hi = restricted_upper_act(n, 2, g, x)
        lo = d_act(n, 2, g, x)
        assert raw_defect(n, 2, g, g, hi) == lo
        assert factored_defect(n, 2, g, g, hi) == lo
        defect_state_checks += 2

    cert = {
        "schema": "A3_PARTIAL_MOVE_SCALE_COHERENCE_REVISION_CERTIFICATE_V1",
        "status": "PASS",
        "hard_target": "A3_PARTIAL_MOVE_SCALE_COMMUTATION_AND_RADIAL_DEFECT_EXACTLY_CLASSIFIED",
        "group_size": len(G),
        "residual_H_size": len(H),
        "left_coset_objects": len(left),
        "D_homomorphism_site_checks": D_checks,
        "J_homomorphism_site_checks": J_checks,
        "site_factorization_checks": factor_checks,
        "transition_faithfulness_group_checks": faithful_checks,
        "pair_groupoid_projection_rep_checks": pair_projection_checks,
        "mandatory_driver_counterexample": "PASS",
        "frame_only_classifier": "REFUTED",
        "corrected_three_radius": "B2<B3<B4",
        "adjacent_old_frame_defects": ["C0", "C0"],
        "adjacent_state_level_squares": ["NONCOMMUTING", "NONCOMMUTING"],
        "defect_state_checks": defect_state_checks,
    }
    print("A3_PARTIAL_MOVE_SCALE_COHERENCE_REVISION_CHECK=PASS")
    print(json.dumps(cert, sort_keys=True))


if __name__ == "__main__":
    main()
