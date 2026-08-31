#!/usr/bin/env python3
"""Exact checker for RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION.

The checker works entirely on the frozen finite A3 carrier.  It verifies the
scale-indexed prefix actions themselves, the support-transition factorization
of the cross-scale defect, the fixed-H alignment-coset projection, the Driver
counterexample, and a corrected three-radius state-level prototype.

No finite census is used as proof of an unbounded claim: all claims checked
here are finite identities on G=S4 and the explicitly declared B_n carriers.
The general formulas proved in the accompanying research artifact are then
specialized here as deterministic regressions.
"""
from __future__ import annotations

import json
from itertools import permutations, product

Perm = tuple[int, int, int, int]
Vec = tuple[int, int, int, int]
Marker = tuple[str, Vec]
State = tuple[Marker, ...]

G: tuple[Perm, ...] = tuple(permutations(range(4)))
E: Perm = (0, 1, 2, 3)
SWAP12: Perm = (1, 0, 2, 3)
SWAP23: Perm = (0, 2, 1, 3)


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
    """R_p = sgn(p) P_p, with (P_p x)_{p(i)} = x_i."""
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
        if abs(x4) <= n:
            out.append((x1, x2, x3, x4))
    return tuple(sorted(out))


def shell(n: int) -> tuple[Vec, ...]:
    return tuple(x for x in ball(n) if radius(x) == n)


def anchor(n: int) -> Vec:
    return (n, -n, 0, 0)


def prefix_site(n: int, depth: int, g: Perm, x: Vec) -> Vec:
    """D_{n,d}(g): rotate the outer depth shells and fix B_{n-d}."""
    if not (0 <= depth <= n):
        raise ValueError("depth must lie in [0,n]")
    return r_act(g, x) if radius(x) >= n - depth + 1 else x


def transition_site(n: int, depth: int, g: Perm, x: Vec) -> Vec:
    """J_{n,d}(g)=D_{n,d}(g)(D_{n+1,d}(g)|B_n)^(-1)."""
    return prefix_site(
        n,
        depth,
        g,
        prefix_site(n + 1, depth, inverse(g), x),
    )


def full_defect_site(
    n: int, depth: int, g_lower: Perm, g_upper: Perm, x: Vec
) -> Vec:
    """F=D_{n,d}(g_lower)(D_{n+1,d}(g_upper)|B_n)^(-1)."""
    return prefix_site(
        n,
        depth,
        g_lower,
        prefix_site(n + 1, depth, inverse(g_upper), x),
    )


def factorized_defect_site(
    n: int, depth: int, g_lower: Perm, g_upper: Perm, x: Vec
) -> Vec:
    relative = compose(g_lower, inverse(g_upper))
    return transition_site(
        n,
        depth,
        g_lower,
        prefix_site(n + 1, depth, relative, x),
    )


def state(*markers: Marker) -> State:
    names = [name for name, _ in markers]
    if len(names) != len(set(names)):
        raise ValueError("marker names must be unique")
    return tuple(sorted(markers))


def apply_state(n: int, depth: int, g: Perm, s: State) -> State:
    if any(radius(x) > n for _, x in s):
        raise ValueError("state marker outside B_n")
    return tuple(sorted((name, prefix_site(n, depth, g, x)) for name, x in s))


def apply_defect_state(
    n: int, depth: int, g_lower: Perm, g_upper: Perm, s: State
) -> State:
    return tuple(
        sorted(
            (
                name,
                full_defect_site(n, depth, g_lower, g_upper, x),
            )
            for name, x in s
        )
    )


def restrict_state(n: int, s: State) -> State:
    return tuple(sorted((name, x) for name, x in s if radius(x) <= n))


def position(s: State, name: str) -> Vec:
    for marker_name, x in s:
        if marker_name == name:
            return x
    raise KeyError(name)


def stabilizer(x: Vec) -> tuple[Perm, ...]:
    return tuple(g for g in G if r_act(g, x) == x)


def left_coset(H: tuple[Perm, ...], g: Perm) -> frozenset[Perm]:
    return frozenset(compose(h, g) for h in H)


def left_cosets(H: tuple[Perm, ...]) -> tuple[frozenset[Perm], ...]:
    seen: set[Perm] = set()
    out: list[frozenset[Perm]] = []
    for g in G:
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


def aligners_for_pointer(pointer: Vec, target: Vec) -> frozenset[Perm]:
    return frozenset(g for g in G if r_act(g, pointer) == target)


def residual_orbit_state(n: int, depth: int, H: tuple[Perm, ...], s: State) -> frozenset[State]:
    return frozenset(apply_state(n, depth, h, s) for h in H)


def main() -> None:
    H = stabilizer(anchor(2))
    assert set(H) == {E, SWAP12}
    assert len(left_cosets(H)) == 12

    site_factorization_checks = 0
    homomorphism_checks = 0
    j_homomorphism_checks = 0
    faithfulness_checks = 0

    # Exact finite replay of the general support formulas on the operational
    # radii needed by the revised prototype.
    for n in (2, 3):
        for depth in (1, 2):
            if depth > n:
                continue
            transition_radius = n - depth + 1

            # D_{n,d} and J_{n,d} are group actions on their invariant bands.
            for g in G:
                moved = {
                    x
                    for x in ball(n)
                    if transition_site(n, depth, g, x) != x
                }
                assert all(radius(x) == transition_radius for x in moved)
                if g == E:
                    assert not moved
                else:
                    assert moved
                faithfulness_checks += 1

                for h in G:
                    gh = compose(g, h)
                    for x in ball(n):
                        assert prefix_site(
                            n, depth, gh, x
                        ) == prefix_site(
                            n,
                            depth,
                            g,
                            prefix_site(n, depth, h, x),
                        )
                        homomorphism_checks += 1
                        assert transition_site(
                            n, depth, gh, x
                        ) == transition_site(
                            n,
                            depth,
                            g,
                            transition_site(n, depth, h, x),
                        )
                        j_homomorphism_checks += 1

            # Exhaustive two-aligner factorization and piecewise formula.
            for g_lower in G:
                for g_upper in G:
                    relative = compose(g_lower, inverse(g_upper))
                    for x in ball(n):
                        actual = full_defect_site(
                            n, depth, g_lower, g_upper, x
                        )
                        factored = factorized_defect_site(
                            n, depth, g_lower, g_upper, x
                        )
                        assert actual == factored

                        r = radius(x)
                        if r <= n - depth:
                            expected = x
                        elif r == transition_radius:
                            expected = r_act(g_lower, x)
                        else:
                            expected = r_act(relative, x)
                        assert actual == expected
                        site_factorization_checks += 1

    # The raw restriction square for a common nontrivial g never descends:
    # J is nontrivial on the transition shell.  The finite S4 replay checks
    # every g and the proof artifact supplies the all-n argument.
    for n in (2, 3):
        for depth in (1, 2):
            if depth > n:
                continue
            for g in G:
                equal_on_all_sites = all(
                    prefix_site(n + 1, depth, g, x)
                    == prefix_site(n, depth, g, x)
                    for x in ball(n)
                )
                assert equal_on_all_sites == (g == E)

    # Alignment families are precisely the accepted fixed-H left cosets.
    for k in (1, 2, 3, 4):
        target = anchor(k)
        assert set(stabilizer(target)) == set(H)
        for g in G:
            pointer = r_act(inverse(g), target)
            assert aligners_for_pointer(pointer, target) == left_coset(H, g)

    # Projection law to the already accepted fixed-H double-coset algebra.
    # The ordered pair of left cosets determines a well-defined double coset.
    cosets = left_cosets(H)
    projection_checks = 0
    for L_lower in cosets:
        for L_upper in cosets:
            projected: frozenset[Perm] | None = None
            for u in L_lower:
                for v in L_upper:
                    C = double_coset(H, compose(u, inverse(v)))
                    if projected is None:
                        projected = C
                    else:
                        assert C == projected
                    projection_checks += 1
            assert projected is not None

    # Mandatory Driver counterexample.  The frame-phase projection is C0
    # because the same g is used at both scales, but the transition factor J
    # moves S1 and survives the residual-H quotient.
    g = SWAP23
    p = anchor(1)
    assert r_act(g, p) == (-1, 0, 1, 0)
    assert {r_act(h, p) for h in H} == {p}
    assert r_act(g, p) not in {r_act(h, p) for h in H}
    assert double_coset(H, compose(g, inverse(g))) == frozenset(H)
    assert transition_site(2, 2, g, p) == r_act(g, p)

    # Stronger no-go: identical frame phase C0 occurs for two distinct typed
    # pair-groupoid arrows (H,H) and (Hg,Hg), but their transition actions
    # differ on the same S1 marker.  Therefore no function of the relative
    # double coset alone can classify H4.
    L0 = left_coset(H, E)
    Lg = left_coset(H, g)
    assert L0 != Lg
    assert double_coset(H, E) == double_coset(H, compose(g, inverse(g)))
    assert {
        transition_site(2, 2, u, p) for u in L0
    } != {
        transition_site(2, 2, u, p) for u in Lg
    }

    # Corrected three-radius state-level prototype.  Depth 2 requires lower
    # scale n>=2, so B1 subset B2 subset B3 is not a two-edge depth-2 H4
    # prototype.  Use B2 subset B3 subset B4 instead.
    pointers = {
        k: r_act(inverse(g), anchor(k)) for k in (2, 3, 4)
    }
    s4 = state(
        ("pointer4", pointers[4]),
        ("pointer3", pointers[3]),
        ("pointer2", pointers[2]),
        ("q2", anchor(2)),
        ("q1", anchor(1)),
    )

    # Edge 4 -> 3: transition shell is S2.
    path_a_43 = restrict_state(3, apply_state(4, 2, g, s4))
    path_b_43 = apply_state(3, 2, g, restrict_state(3, s4))
    assert position(path_a_43, "pointer3") == anchor(3)
    assert position(path_b_43, "pointer3") == anchor(3)
    assert position(path_a_43, "q2") == anchor(2)
    assert position(path_b_43, "q2") == r_act(g, anchor(2))
    assert path_b_43 not in residual_orbit_state(3, 2, H, path_a_43)

    # Edge 3 -> 2: transition shell is S1.
    s3 = restrict_state(3, s4)
    path_a_32 = restrict_state(2, apply_state(3, 2, g, s3))
    path_b_32 = apply_state(2, 2, g, restrict_state(2, s3))
    assert position(path_a_32, "pointer2") == anchor(2)
    assert position(path_b_32, "pointer2") == anchor(2)
    assert position(path_a_32, "q1") == anchor(1)
    assert position(path_b_32, "q1") == r_act(g, anchor(1))
    assert path_b_32 not in residual_orbit_state(2, 2, H, path_a_32)

    # Both adjacent old frame defects are C0 although both state-level squares
    # fail.  This is the revised H5/H6 regression.
    C0 = double_coset(H, E)
    assert double_coset(H, compose(g, inverse(g))) == C0

    # The exact defect map carries every chosen upper-path state to every
    # chosen lower-path state for the same raw restricted state.
    sample = restrict_state(2, s3)
    defect_state_checks = 0
    for u in Lg:
        for v in Lg:
            upper = apply_state(3, 2, v, sample)
            lower = apply_state(2, 2, u, sample)
            assert apply_defect_state(2, 2, u, v, upper) == lower
            defect_state_checks += 1

    summary = {
        "schema": "A3_PARTIAL_MOVE_SCALE_COHERENCE_REVISION_CERTIFICATE_V1",
        "status": "PASS",
        "group_size": len(G),
        "residual_H_size": len(H),
        "left_coset_objects": len(cosets),
        "site_factorization_checks": site_factorization_checks,
        "D_homomorphism_site_checks": homomorphism_checks,
        "J_homomorphism_site_checks": j_homomorphism_checks,
        "transition_faithfulness_group_checks": faithfulness_checks,
        "pair_groupoid_projection_rep_checks": projection_checks,
        "defect_state_checks": defect_state_checks,
        "mandatory_driver_counterexample": "PASS",
        "frame_only_classifier": "REFUTED",
        "corrected_three_radius": "B2<B3<B4",
        "adjacent_old_frame_defects": ["C0", "C0"],
        "adjacent_state_level_squares": ["NONCOMMUTING", "NONCOMMUTING"],
        "hard_target": "A3_PARTIAL_MOVE_SCALE_COMMUTATION_AND_RADIAL_DEFECT_EXACTLY_CLASSIFIED",
    }
    print("A3_PARTIAL_MOVE_SCALE_COHERENCE_REVISION_CHECK=PASS")
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
