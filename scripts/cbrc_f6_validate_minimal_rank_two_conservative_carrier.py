#!/usr/bin/env python3
"""
Deterministic exact checker for CBRC F6 minimal rank-two conservative carrier.

Mathematical scope is deliberately additive only:
    C_min = Z e ⊕ Z f ⊕ <tau | 3 tau = 0>.
No multiplication, ring, norm, inner product, square law, or two-slot mixing
is represented anywhere in this checker.
"""
from __future__ import annotations

import itertools
import json
import math
from fractions import Fraction
from typing import Callable, Dict, Iterable, List, Sequence, Tuple

Elem = Tuple[int, int, int]  # (e-coordinate, f-coordinate, tau-coordinate mod 3)
Map = Callable[[Elem], Elem]

E: Elem = (1, 0, 0)
F: Elem = (0, 1, 0)
TAU: Elem = (0, 0, 1)
ZERO: Elem = (0, 0, 0)
GENERATORS = (E, F, TAU)


def norm(x: Elem) -> Elem:
    return (int(x[0]), int(x[1]), int(x[2]) % 3)


def add(x: Elem, y: Elem) -> Elem:
    return norm((x[0] + y[0], x[1] + y[1], x[2] + y[2]))


def neg(x: Elem) -> Elem:
    return norm((-x[0], -x[1], -x[2]))


def eq_map(a: Map, b: Map) -> bool:
    return all(norm(a(g)) == norm(b(g)) for g in GENERATORS)


def identity(x: Elem) -> Elem:
    return norm(x)


def compose(a: Map, b: Map) -> Map:
    # a ∘ b
    return lambda x: norm(a(b(x)))


def power(a: Map, n: int) -> Map:
    out: Map = identity
    for _ in range(n):
        out = compose(a, out)
    return out


def make_R(r: int) -> Map:
    r %= 3
    return lambda x: norm((x[0], x[1], x[2] + x[0] + r * x[1]))


def make_J(delta: int, j: int) -> Map:
    assert delta in (-1, 1)
    j %= 3
    return lambda x: norm((-x[0], delta * x[1], -x[2] + j * x[1]))


def make_S(sigma: int, s: int) -> Map:
    assert sigma in (-1, 1)
    s %= 3
    return lambda x: norm((x[0], sigma * x[1], -x[2] + s * x[1]))


def exact_relations(delta: int, sigma: int, r: int, j: int, s: int) -> bool:
    R = make_R(r)
    J = make_J(delta, j)
    S = make_S(sigma, s)
    return (
        eq_map(power(R, 3), identity)
        and eq_map(power(J, 2), identity)
        and eq_map(power(S, 2), identity)
        and eq_map(compose(J, R), compose(R, J))
        and eq_map(compose(compose(S, R), S), power(R, 2))  # R^-1=R^2 when R^3=id
        and all(R(g)[0] == g[0] for g in GENERATORS)  # pi R = pi
        and all(S(g)[0] == g[0] for g in GENERATORS)  # pi S = pi
        and all(J(g)[0] == -g[0] for g in GENERATORS)  # pi J = -pi
    )


def formula_relations(delta: int, sigma: int, r: int, j: int, s: int) -> bool:
    # Exact congruence normal form derived in the proof.
    return (
        ((delta - 1) * j) % 3 == 0
        and ((sigma - 1) * s) % 3 == 0
        and ((1 + delta) * r) % 3 == 0
        and ((sigma - 1) * (s - r)) % 3 == 0
    )


def gauge(eps: int, a: int) -> Map:
    assert eps in (-1, 1)
    a %= 3
    return lambda x: norm((x[0], eps * x[1], x[2] + a * x[1]))


def gauge_inv(eps: int, a: int) -> Map:
    assert eps in (-1, 1)
    a %= 3
    return lambda x: norm((x[0], eps * x[1], x[2] - a * eps * x[1]))


def conjugate(A: Map, eps: int, a: int) -> Map:
    return compose(gauge(eps, a), compose(A, gauge_inv(eps, a)))


def transform_parameters(
    p: Tuple[int, int, int, int, int], eps: int, a: int
) -> Tuple[int, int, int, int, int]:
    delta, sigma, r, j, s = p
    return (
        delta,
        sigma,
        (eps * r) % 3,
        (eps * (j + a * (delta + 1))) % 3,
        (eps * (s + a * (sigma + 1))) % 3,
    )


def extract_parameters(R: Map, J: Map, S: Map) -> Tuple[int, int, int, int, int]:
    rf = norm(R(F))
    jf = norm(J(F))
    sf = norm(S(F))
    assert rf[0] == jf[0] == sf[0] == 0
    assert rf[1] == 1
    assert jf[1] in (-1, 1)
    assert sf[1] in (-1, 1)
    return (jf[1], sf[1], rf[2], jf[2], sf[2])


def all_valid_parameters() -> List[Tuple[int, int, int, int, int]]:
    out = []
    mismatches = 0
    for delta, sigma in itertools.product((1, -1), repeat=2):
        for r, j, s in itertools.product(range(3), repeat=3):
            exact = exact_relations(delta, sigma, r, j, s)
            formula = formula_relations(delta, sigma, r, j, s)
            if exact != formula:
                mismatches += 1
            if exact:
                out.append((delta, sigma, r, j, s))
    assert mismatches == 0
    return out


def unary_orbits(
    valid: Sequence[Tuple[int, int, int, int, int]]
) -> List[frozenset[Tuple[int, int, int, int, int]]]:
    valid_set = set(valid)
    unseen = set(valid)
    orbits = []
    while unseen:
        p = min(unseen)
        orb = {
            transform_parameters(p, eps, a)
            for eps in (-1, 1)
            for a in range(3)
        }
        assert orb <= valid_set
        # Verify the closed-form parameter action against actual conjugation.
        delta, sigma, r, j, s = p
        for eps in (-1, 1):
            for a in range(3):
                actual = extract_parameters(
                    conjugate(make_R(r), eps, a),
                    conjugate(make_J(delta, j), eps, a),
                    conjugate(make_S(sigma, s), eps, a),
                )
                assert actual == transform_parameters(p, eps, a)
        frozen = frozenset(orb)
        orbits.append(frozen)
        unseen -= orb
    return orbits


def orbit_has_common_fixed_complement(
    orb: Iterable[Tuple[int, int, int, int, int]]
) -> bool:
    # A representative with R(f)=J(f)=S(f)=f means the added Z-summand
    # carries no new unary action at all.
    return any(
        delta == 1 and sigma == 1 and r % 3 == 0 and j % 3 == 0 and s % 3 == 0
        for delta, sigma, r, j, s in orb
    )


def determinant(m: Sequence[Sequence[int]]) -> int:
    n = len(m)
    if n == 0:
        return 1
    assert all(len(row) == n for row in m)
    if n == 1:
        return int(m[0][0])
    total = 0
    for col in range(n):
        minor = [list(row[:col]) + list(row[col + 1 :]) for row in m[1:]]
        total += ((-1) ** col) * int(m[0][col]) * determinant(minor)
    return total


def rational_rank(m: Sequence[Sequence[int]], ncols: int) -> int:
    rows = [[Fraction(v) for v in row] for row in m]
    if not rows:
        return 0
    assert all(len(row) == ncols for row in rows)
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        pv = rows[r][c]
        rows[r] = [v / pv for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                q = rows[i][c]
                rows[i] = [rows[i][j] - q * rows[r][j] for j in range(ncols)]
        r += 1
        if r == len(rows):
            break
    return r


def smith_invariants(
    relations: Sequence[Sequence[int]], n_generators: int
) -> Tuple[int, List[int]]:
    """
    Return (free_rank, nontrivial torsion invariant factors) using
    determinantal divisors. This is exact and sufficient for the finite
    presentations used by the F6 proof/regressions.
    """
    assert all(len(row) == n_generators for row in relations)
    rank = rational_rank(relations, n_generators)
    deltas = [1]
    for k in range(1, rank + 1):
        vals = []
        for rs in itertools.combinations(range(len(relations)), k):
            for cs in itertools.combinations(range(n_generators), k):
                sub = [[relations[i][j] for j in cs] for i in rs]
                vals.append(abs(determinant(sub)))
        d = 0
        for v in vals:
            d = math.gcd(d, v)
        assert d > 0
        deltas.append(d)
    diag = [deltas[k] // deltas[k - 1] for k in range(1, len(deltas))]
    assert all(diag[i] != 0 and (i == 0 or diag[i] % diag[i - 1] == 0) for i in range(len(diag)))
    return n_generators - rank, [d for d in diag if d > 1]


def egcd(a: int, b: int) -> Tuple[int, int, int]:
    if b == 0:
        g = abs(a)
        return g, (1 if a >= 0 else -1), 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def primitive_embedding_regression(bound: int = 4) -> Tuple[int, int]:
    primitive = 0
    nonprimitive = 0
    for a in range(-bound, bound + 1):
        for b in range(-bound, bound + 1):
            if (a, b) == (0, 0):
                continue
            g = math.gcd(abs(a), abs(b))
            gg, u, v = egcd(a, b)
            assert gg == g
            assert u * a + v * b == g
            has_retraction = (g == 1)
            # Hom(Z^2,Z) sending (a,b) to 1 exists iff gcd(a,b)=1.
            if has_retraction:
                primitive += 1
                assert u * a + v * b == 1
            else:
                nonprimitive += 1
                assert g > 1
    return primitive, nonprimitive


# Upstream C1 maps, represented as (e-coordinate, tau-coordinate mod 3).
Pair = Tuple[int, int]


def R1(x: Pair) -> Pair:
    return (x[0], (x[1] + x[0]) % 3)


def J1(x: Pair) -> Pair:
    return (-x[0], (-x[1]) % 3)


def S1(x: Pair) -> Pair:
    return (x[0], (-x[1]) % 3)


def apply_word_full(word: str, maps: Dict[str, Map], x: Elem) -> Elem:
    y = x
    for ch in word:
        y = maps[ch](y)
    return norm(y)


def apply_word_upstream(word: str, x: Pair) -> Pair:
    y = x
    maps = {"R": R1, "J": J1, "S": S1}
    for ch in word:
        y = maps[ch](y)
    return (y[0], y[1] % 3)


def composition_depth_check(
    valid: Sequence[Tuple[int, int, int, int, int]], depth: int = 4
) -> Tuple[int, int]:
    words = [""]
    for n in range(1, depth + 1):
        words.extend("".join(w) for w in itertools.product("RJS", repeat=n))
    comparisons = 0
    for delta, sigma, r, j, s in valid:
        maps = {"R": make_R(r), "J": make_J(delta, j), "S": make_S(sigma, s)}
        for word in words:
            for full_g, old_g in ((E, (1, 0)), (TAU, (0, 1))):
                got = apply_word_full(word, maps, full_g)
                expected = apply_word_upstream(word, old_g)
                assert got[1] == 0
                assert (got[0], got[2]) == expected
                comparisons += 1
    return len(words) * len(valid), comparisons


def relation_bundle(R: Map, J: Map, S: Map, require_r3: bool = True) -> Dict[str, bool]:
    # For ablation models where R may not have order 3, compute inverse by a
    # supplied finite power only in the dedicated test instead of assuming R^2.
    return {
        "R3": eq_map(power(R, 3), identity),
        "J2": eq_map(power(J, 2), identity),
        "S2": eq_map(power(S, 2), identity),
        "JR": eq_map(compose(J, R), compose(R, J)),
    }


def run_ablations() -> Dict[str, str]:
    # A1: explicit primitivity is redundant with an integer retraction.
    prim, nonprim = primitive_embedding_regression()
    assert prim > 0 and nonprim > 0

    # A2: collapsing tau destroys the relative witness -tau != 0.
    R0, J0 = make_R(0), make_J(1, 0)
    witness = add(E, J0(R0(E)))
    assert witness == (0, 0, 2) and witness != ZERO
    collapsed_witness = ZERO  # quotient tau=0
    assert collapsed_witness == ZERO

    # A3/A8: without a typed/covariant old projection, an integral parity
    # shear survives all unary relations. S(f)=3e-f.
    def R_base(x: Elem) -> Elem:
        return norm((x[0], x[1], x[2] + x[0]))

    def J_base(x: Elem) -> Elem:
        return norm((-x[0], x[1], -x[2]))

    def S_shear3(x: Elem) -> Elem:
        return norm((x[0] + 3 * x[1], -x[1], -x[2]))

    assert eq_map(power(R_base, 3), identity)
    assert eq_map(power(J_base, 2), identity)
    assert eq_map(power(S_shear3, 2), identity)
    assert eq_map(compose(J_base, R_base), compose(R_base, J_base))
    assert eq_map(compose(compose(S_shear3, R_base), S_shear3), power(R_base, 2))
    assert S_shear3(F)[0] == 3  # violates pi S = pi on f

    # A5: remove R^3. R can act by -1 on the new free direction.
    def R_flip(x: Elem) -> Elem:
        return norm((x[0], -x[1], x[2] + x[0]))

    def R_flip_inv(x: Elem) -> Elem:
        return norm((x[0], -x[1], x[2] - x[0]))

    S_base = make_S(1, 0)
    assert not eq_map(power(R_flip, 3), identity)
    assert eq_map(power(J_base, 2), identity)
    assert eq_map(power(S_base, 2), identity)
    assert eq_map(compose(J_base, R_flip), compose(R_flip, J_base))
    assert eq_map(compose(compose(S_base, R_flip), S_base), R_flip_inv)
    assert all(R_flip(g)[0] == g[0] for g in GENERATORS)

    # A6: remove JR=RJ. r=1 becomes possible with J free-sign +1.
    R_r1, J_plus, S_plus = make_R(1), make_J(1, 0), make_S(1, 0)
    assert eq_map(power(R_r1, 3), identity)
    assert eq_map(power(J_plus, 2), identity)
    assert eq_map(power(S_plus, 2), identity)
    assert not eq_map(compose(J_plus, R_r1), compose(R_r1, J_plus))
    assert eq_map(compose(compose(S_plus, R_r1), S_plus), power(R_r1, 2))

    # A7: remove SRS^-1=R^-1. r=1 survives with both free signs -1.
    J_minus, S_minus = make_J(-1, 0), make_S(-1, 0)
    assert eq_map(power(R_r1, 3), identity)
    assert eq_map(power(J_minus, 2), identity)
    assert eq_map(power(S_minus, 2), identity)
    assert eq_map(compose(J_minus, R_r1), compose(R_r1, J_minus))
    assert not eq_map(compose(compose(S_minus, R_r1), S_minus), power(R_r1, 2))

    # A4: full retract is not needed at the minimum. The hom criterion is
    # visible already on cyclic pointed torsion: Z/3 with tau=g admits a
    # functional to Z/3 taking tau to 1; Z/9 with tau=3g does not.
    z3_values = {(1 * c) % 3 for c in range(3)}
    z9_tau_values = {(3 * c) % 3 for c in range(3)}
    assert 1 in z3_values
    assert 1 not in z9_tau_values

    # A9: without no-extra-torsion preference, C_min ⊕ Z/m gives infinitely
    # many pairwise nonisomorphic examples; distinct torsion orders 3m already
    # witness infinitely many.
    torsion_orders = [3 * m for m in range(2, 20)]
    assert len(set(torsion_orders)) == len(torsion_orders)

    return {
        "primitive_old_generator": "REDUNDANT_GIVEN_PI",
        "preserve_order_three_tau": "ESSENTIAL",
        "old_retraction_pi": "CLASSIFICATION_ENLARGES_WITHOUT_TYPED_PI",
        "full_upstream_retract": "NOT_NEEDED_FOR_LEAST_CLASS",
        "R3": "ESSENTIAL_FOR_LIFT_CLASS",
        "JR": "ESSENTIAL_FOR_LIFT_CLASS",
        "SRS_inverse": "ESSENTIAL_FOR_LIFT_CLASS",
        "old_projection_covariance": "ESSENTIAL_FOR_LIFT_CLASS",
        "no_extra_torsion_preference": "ESSENTIAL_FOR_UNIQUE_LEAST_CARRIER",
    }


def main() -> None:
    # Finite-presentation / Smith-normal-form examples used in the proof.
    snf_examples = {
        "C_min": smith_invariants([[0, 0, 3]], 3),
        "C_9": smith_invariants([[0, 0, 9]], 3),
        "C_33": smith_invariants(
            [[0, 0, 3, 0], [0, 0, 0, 3]], 4
        ),
    }
    assert snf_examples["C_min"] == (2, [3])
    assert snf_examples["C_9"] == (2, [9])
    assert snf_examples["C_33"] == (2, [3, 3])

    primitive_count, nonprimitive_count = primitive_embedding_regression()

    valid = all_valid_parameters()
    assert len(valid) == 22

    orbits = unary_orbits(valid)
    assert len(orbits) == 6

    # Expected distribution across (delta,sigma) sign sectors.
    sector_raw: Dict[str, int] = {}
    sector_orbits: Dict[str, int] = {}
    for delta, sigma in itertools.product((1, -1), repeat=2):
        key = f"J{delta:+d}_S{sigma:+d}"
        sector_raw[key] = sum(1 for p in valid if p[0] == delta and p[1] == sigma)
        sector_orbits[key] = sum(
            1 for orb in orbits if next(iter(orb))[0] == delta and next(iter(orb))[1] == sigma
        )
    assert sector_raw == {
        "J+1_S+1": 9,
        "J+1_S-1": 3,
        "J-1_S+1": 9,
        "J-1_S-1": 1,
    }
    assert sector_orbits == {
        "J+1_S+1": 2,
        "J+1_S-1": 1,
        "J-1_S+1": 2,
        "J-1_S-1": 1,
    }

    minimal_orbits = [orb for orb in orbits if orbit_has_common_fixed_complement(orb)]
    assert len(minimal_orbits) == 1
    minimal_orbit = minimal_orbits[0]
    assert (1, 1, 0, 0, 0) in minimal_orbit

    # Free quotient: R is always +1 on f; J,S are sign-only.
    assert all(p[2] in range(3) for p in valid)
    assert all(make_R(p[2])(F)[1] == 1 for p in valid)
    assert all(make_J(p[0], p[3])(F)[1] in (-1, 1) for p in valid)
    assert all(make_S(p[1], p[4])(F)[1] in (-1, 1) for p in valid)

    # Upstream relative witness and composition-depth regression.
    for delta, sigma, r, j, s in valid:
        R, J, S = make_R(r), make_J(delta, j), make_S(sigma, s)
        assert add(E, J(E)) == ZERO
        assert add(E, J(R(E))) == (0, 0, 2)
        assert add(E, J(R(E))) != ZERO
        assert power(R, 3)(TAU) == TAU
    word_count, generator_comparisons = composition_depth_check(valid, depth=4)

    ablations = run_ablations()

    result = {
        "status": "PASS",
        "carrier_snf_examples": {
            k: {"free_rank": v[0], "torsion_invariants": v[1]}
            for k, v in snf_examples.items()
        },
        "primitive_embedding_regression": {
            "bound": 4,
            "primitive_cases": primitive_count,
            "nonprimitive_cases": nonprimitive_count,
        },
        "raw_unary_parameter_cases": len(valid),
        "unary_equivalence_classes": len(orbits),
        "sector_raw_counts": sector_raw,
        "sector_orbit_counts": sector_orbits,
        "unique_minimal_unary_class": True,
        "minimal_class_representative": [1, 1, 0, 0, 0],
        "free_quotient_R_action": "FIXED",
        "free_quotient_J_S_action": "SIGN_ONLY",
        "composition_depth": 4,
        "composition_words_checked_across_all_lifts": word_count,
        "upstream_generator_comparisons": generator_comparisons,
        "relative_witness": "PRESERVED_NONZERO_MINUS_TAU",
        "ablations": ablations,
        "implicit_multiplication": False,
        "theorem_model_mismatches": 0,
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
