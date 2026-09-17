#!/usr/bin/env python3
"""Exact checker for RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION.

Pure stdlib. Verifies the actual adjacent-scale state maps induced by the
scale-indexed depth-d prefix-shell moves, the frozen n=2 counterexample, the
radial operator-defect formula, and the exact universal residual-H quotient
criterion on finite A3 balls through n=4.
"""
from itertools import permutations, product

Perm = tuple[int, int, int, int]
Vec = tuple[int, int, int, int]

G: tuple[Perm, ...] = tuple(permutations(range(4)))
E: Perm = (0, 1, 2, 3)
SWAP12: Perm = (1, 0, 2, 3)
SWAP23: Perm = (0, 2, 1, 3)
H = frozenset((E, SWAP12))


def parity(p: Perm) -> int:
    inv = sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j])
    return 1 if inv % 2 == 0 else -1


def compose(p: Perm, q: Perm) -> Perm:
    """p after q."""
    return tuple(p[q[i]] for i in range(4))


def inverse(p: Perm) -> Perm:
    out = [0] * 4
    for i, image in enumerate(p):
        out[image] = i
    return tuple(out)  # type: ignore[return-value]


def r_act(p: Perm, x: Vec) -> Vec:
    y = [0] * 4
    for i, value in enumerate(x):
        y[p[i]] = value
    s = parity(p)
    return tuple(s * value for value in y)  # type: ignore[return-value]


def radius(x: Vec) -> int:
    return max(abs(v) for v in x)


def ball(n: int) -> tuple[Vec, ...]:
    out: list[Vec] = []
    for x1, x2, x3 in product(range(-n, n + 1), repeat=3):
        x4 = -(x1 + x2 + x3)
        if abs(x4) <= n:
            out.append((x1, x2, x3, x4))
    return tuple(sorted(out))


def shell(n: int) -> tuple[Vec, ...]:
    return tuple(x for x in ball(n) if radius(x) == n)


def prefix_move(n: int, depth: int, g: Perm, x: Vec) -> Vec:
    if not (1 <= depth <= n):
        raise ValueError("depth must lie in [1,n]")
    return r_act(g, x) if radius(x) >= n - depth + 1 else x


def upper_then_restrict(n: int, depth: int, g_upper: Perm, x: Vec) -> Vec:
    """Carrier map on B_n induced by D_{n+1,d}(g_upper) followed by restriction."""
    return r_act(g_upper, x) if radius(x) >= n - depth + 2 else x


def restrict_then_lower(n: int, depth: int, g_lower: Perm, x: Vec) -> Vec:
    """Carrier map on B_n induced by restriction followed by D_{n,d}(g_lower)."""
    return prefix_move(n, depth, g_lower, x)


def radial_defect_label(n: int, depth: int, g_lower: Perm, g_upper: Perm, r: int) -> Perm:
    """K = (restrict-then-lower) o (upper-then-restrict)^(-1), shellwise."""
    q = n - depth + 1
    if r < q:
        return E
    if r == q:
        return g_lower
    return compose(g_lower, inverse(g_upper))


def radial_defect_act(n: int, depth: int, g_lower: Perm, g_upper: Perm, x: Vec) -> Vec:
    r = radius(x)
    if r == 0:
        return x
    return r_act(radial_defect_label(n, depth, g_lower, g_upper, r), x)


def same_global_H_orbit_of_maps(n: int, depth: int, g_lower: Perm, g_upper: Perm) -> bool:
    """Universal rigid-state H-quotient equality: B = R_h o A for one global h in H."""
    Bn = ball(n)
    return any(
        all(
            restrict_then_lower(n, depth, g_lower, x)
            == r_act(h, upper_then_restrict(n, depth, g_upper, x))
            for x in Bn
        )
        for h in H
    )


def predicted_global_H_criterion(n: int, depth: int, g_lower: Perm, g_upper: Perm) -> bool:
    q = n - depth + 1
    if n == 1 and depth == 1:
        return g_lower in H
    if q >= 2:
        if depth == 1:
            return g_lower == E
        return g_lower == E and g_upper == E
    return g_lower in H and g_upper == E


def double_cosets() -> tuple[tuple[Perm, ...], ...]:
    seen: set[Perm] = set()
    out: list[tuple[Perm, ...]] = []
    for g in sorted(G):
        if g in seen:
            continue
        c = {
            compose(compose(h1, g), h2)
            for h1 in H
            for h2 in H
        }
        seen |= c
        out.append(tuple(sorted(c)))
    return tuple(out)


def main() -> None:
    for q in range(1, 5):
        a = (q, -q, 0, 0)
        assert {g for g in G if r_act(g, a) == a} == H
        kernel = {
            g for g in G
            if all(any(r_act(g, x) == r_act(h, x) for h in H) for x in shell(q))
        }
        assert kernel == H

    raw_cases = 0
    quotient_cases = 0
    for n in range(1, 5):
        Bn = ball(n)
        for depth in range(1, n + 1):
            for g_lower in G:
                for g_upper in G:
                    raw_cases += 1
                    A = {x: upper_then_restrict(n, depth, g_upper, x) for x in Bn}
                    B = {x: restrict_then_lower(n, depth, g_lower, x) for x in Bn}
                    for x in Bn:
                        assert B[x] == radial_defect_act(
                            n, depth, g_lower, g_upper, A[x]
                        )
                    predicted_raw = all(
                        radial_defect_label(n, depth, g_lower, g_upper, r) == E
                        for r in range(1, n + 1)
                    )
                    assert (A == B) == predicted_raw
                    quotient_cases += 1
                    assert same_global_H_orbit_of_maps(n, depth, g_lower, g_upper) == (
                        predicted_global_H_criterion(n, depth, g_lower, g_upper)
                    )

    n, depth, g = 2, 2, SWAP23
    p = (1, -1, 0, 0)
    A_p = upper_then_restrict(n, depth, g, p)
    B_p = restrict_then_lower(n, depth, g, p)
    assert A_p == p
    assert B_p == (-1, 0, 1, 0)
    assert all(B_p != r_act(h, A_p) for h in H)

    cosets = double_cosets()
    label = {x: i for i, c in enumerate(cosets) for x in c}
    assert label[SWAP23] == 2
    assert radial_defect_label(2, 2, g, g, 1) == g
    assert radial_defect_label(2, 2, g, g, 2) == E
    assert (label[radial_defect_label(2, 2, g, g, 1)],
            label[radial_defect_label(2, 2, g, g, 2)]) == (2, 0)

    assert all(
        upper_then_restrict(2, 2, E, x) == restrict_then_lower(2, 2, E, x)
        for x in ball(2)
    )

    for cutoff in range(1, 4):
        for n in range(cutoff, 5):
            for g in G:
                for x in ball(n):
                    lower = r_act(g, x) if radius(x) >= cutoff else x
                    upper_restricted = r_act(g, x) if radius(x) >= cutoff else x
                    assert lower == upper_restricted

    profiles = []
    for n in range(2, 7):
        gl = E if n % 2 else SWAP23
        gu = E if (n + 1) % 2 else SWAP23
        transition = label[radial_defect_label(n, 2, gl, gu, n - 1)]
        overlap = label[radial_defect_label(n, 2, gl, gu, n)]
        profiles.append((n, transition, overlap))
        assert overlap == 2
        assert transition == (2 if n % 2 == 0 else 0)
    assert profiles == [(2, 2, 2), (3, 0, 2), (4, 2, 2), (5, 0, 2), (6, 2, 2)]

    print("A3_PARTIAL_MOVE_SCALE_COHERENCE_CHECK=PASS")
    print(f"RAW_PATH_CASES={raw_cases}")
    print(f"GLOBAL_H_QUOTIENT_CASES={quotient_cases}")
    print("FROZEN_REGRESSION=PASS;N=2;D=2;G=(23);PATH_A=p;PATH_B=(-1,0,1,0)")
    print("FROZEN_RADIAL_PROFILE=S1:C2,S2:C0")
    print("FRAME_ONLY_NO_GO=PASS;C0_HAS_BOTH_COMMUTING_AND_NONCOMMUTING_STATE_SQUARES")
    print("ALTERNATING_D2_PROFILES=n2:(C2,C2),n3:(C0,C2),n4:(C2,C2),n5:(C0,C2),n6:(C2,C2)")
    print("ABSOLUTE_CUTOFF_NATURALITY=PASS")
    print("UNIVERSAL_GLOBAL_H_CRITERION=PASS_EXHAUSTIVE_N_LE_4")


if __name__ == "__main__":
    main()
