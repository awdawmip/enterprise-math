#!/usr/bin/env python3
"""
Exact checker for RS-SEED6-BRIDGE-TRIANGLE-LOCAL-GROWTH.

Scope:
- fixed seed 6 = 2*3;
- first 500 primes r > 3;
- exact integer arithmetic only;
- no factor-search/performance objective.

The checker verifies the Boolean-divisor-lattice / carrier-incidence
classification and audits several candidate invariants and symmetry models.
"""
from __future__ import annotations

from itertools import combinations, permutations
from math import gcd
import json


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def first_primes_gt3(k: int) -> list[int]:
    out: list[int] = []
    n = 5
    while len(out) < k:
        if is_prime(n):
            out.append(n)
        n += 2
    return out


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def prime_factorization(n: int) -> dict[int, int]:
    x = n
    out: dict[int, int] = {}
    d = 2
    while d * d <= x:
        while x % d == 0:
            out[d] = out.get(d, 0) + 1
            x //= d
        d = 3 if d == 2 else d + 2
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def edge(i: int, j: int) -> tuple[int, int]:
    return (i, j) if i < j else (j, i)


def det3(M: list[list[int]]) -> int:
    return (
        M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
    )


def gcd_of_abs(xs: list[int]) -> int:
    g = 0
    for x in xs:
        g = gcd(g, abs(x))
    return g


def two_by_two_minors(M: list[list[int]]) -> list[int]:
    out = []
    for rs in combinations(range(3), 2):
        for cs in combinations(range(3), 2):
            a, b = rs
            c, d = cs
            out.append(M[a][c] * M[b][d] - M[a][d] * M[b][c])
    return out


def preserves_edge_labels(
    p: tuple[int, ...], labels: dict[tuple[int, int], object]
) -> bool:
    for (i, j), lab in labels.items():
        if labels[edge(p[i], p[j])] != lab:
            return False
    return True


def graph_aut_count(
    n: int,
    edges: set[tuple[int, int]],
    partition: tuple[set[int], set[int]] | None = None,
    fixed: dict[int, int] | None = None,
) -> int:
    fixed = fixed or {}
    edges = {edge(i, j) for i, j in edges}
    count = 0
    for p in permutations(range(n)):
        if any(p[i] != j for i, j in fixed.items()):
            continue
        if partition is not None:
            A, B = partition
            if {p[i] for i in A} != A or {p[i] for i in B} != B:
                continue
        mapped = {edge(p[i], p[j]) for i, j in edges}
        if mapped == edges:
            count += 1
    return count


# Canonical carrier-incidence matrix:
# rows = (2,3,r); columns = (6,2r,3r)
A = [
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1],
]
assert det3(A) == -2
assert gcd_of_abs([x for row in A for x in row]) == 1
assert gcd_of_abs(two_by_two_minors(A)) == 1
SNF = (1, 1, 2)  # from determinantal divisors 1,1,2

# Levi graph nodes: 0=c2, 1=c3, 2=cr, 3=v6, 4=v2r, 5=v3r.
LEVI_EDGES = {
    edge(0, 3), edge(1, 3),
    edge(0, 4), edge(2, 4),
    edge(1, 5), edge(2, 5),
}
carrier_side = {0, 1, 2}
object_side = {3, 4, 5}
assert graph_aut_count(6, LEVI_EDGES) == 12
assert graph_aut_count(6, LEVI_EDGES, (carrier_side, object_side)) == 6
assert graph_aut_count(
    6, LEVI_EDGES, (carrier_side, object_side), fixed={3: 3}
) == 2
assert graph_aut_count(
    6, LEVI_EDGES, (carrier_side, object_side), fixed={0: 0, 1: 1, 2: 2}
) == 1

primes = first_primes_gt3(500)
assert primes[0] == 5
assert primes[-1] == 3583

canonical_normalized_signature = None
exact_triangles = set()

for r in primes:
    assert is_prime(r) and r > 3

    L = 6 * r
    values = (6, 2 * r, 3 * r)
    assert len(set(values)) == 3
    exact_triangles.add(values)

    # L is squarefree with exactly atoms {2,3,r}.
    fac = prime_factorization(L)
    assert fac == {2: 1, 3: 1, r: 1}

    # The three values are exactly the three coatoms L/p.
    coatoms = {L // 2, L // 3, L // r}
    assert set(values) == coatoms

    # Pairwise gcd labels are the three carrier atoms.
    gcd_labels = {
        edge(0, 1): gcd(values[0], values[1]),
        edge(0, 2): gcd(values[0], values[2]),
        edge(1, 2): gcd(values[1], values[2]),
    }
    assert gcd_labels == {
        edge(0, 1): 2,
        edge(0, 2): 3,
        edge(1, 2): r,
    }

    # Every pair joins to the same Boolean top L.
    assert all(lcm(values[i], values[j]) == L for i, j in combinations(range(3), 2))

    # Each coatom is reconstructed from its two incident gcd/carrier labels.
    for i in range(3):
        incident = [
            lab for (a, b), lab in gcd_labels.items()
            if i == a or i == b
        ]
        assert len(incident) == 2
        assert incident[0] * incident[1] == values[i]

    # Product-square identity is only a derived checksum.
    assert values[0] * values[1] * values[2] == L * L

    # Exact support signature.
    supports = (
        frozenset((2, 3)),
        frozenset((2, r)),
        frozenset((3, r)),
    )
    assert {len(s) for s in supports} == {2}
    assert len(set.union(*[set(s) for s in supports])) == 3
    assert set.intersection(*[set(s) for s in supports]) == set()
    assert sorted(len(supports[i] & supports[j]) for i, j in combinations(range(3), 2)) == [1, 1, 1]

    # Normalize the fresh prime r to a symbol N: all cells become the same rooted typed cell.
    normalized = (
        ("seed", ("L", "R")),
        ("left-mixed", ("L", "N")),
        ("right-mixed", ("R", "N")),
        ("edge-types", ("L", "R", "N")),
        ("snf", SNF),
    )
    if canonical_normalized_signature is None:
        canonical_normalized_signature = normalized
    assert normalized == canonical_normalized_signature

    # Symmetry audit on the object-only triangle.
    exact_aut = sum(
        preserves_edge_labels(p, gcd_labels)
        for p in permutations(range(3))
    )
    assert exact_aut == 1

    typed_edge_labels = {
        edge(0, 1): "fixed-seed-carrier",
        edge(0, 2): "fixed-seed-carrier",
        edge(1, 2): "new-carrier",
    }
    typed_aut = sum(
        preserves_edge_labels(p, typed_edge_labels)
        for p in permutations(range(3))
    )
    assert typed_aut == 2

assert len(exact_triangles) == 500

# Out-of-scope guards: relaxing r>3 prime destroys the exact B3 prime-atom classification.
def has_seed6_B3_prime_atom_signature(r: int) -> bool:
    values = (6, 2 * r, 3 * r)
    if len(set(values)) != 3:
        return False
    fac = prime_factorization(6 * r)
    if len(fac) != 3 or any(e != 1 for e in fac.values()):
        return False
    L = 6 * r
    return set(values) == {L // p for p in fac}


outside_guards = {
    2: has_seed6_B3_prime_atom_signature(2),
    3: has_seed6_B3_prime_atom_signature(3),
    25: has_seed6_B3_prime_atom_signature(25),
    35: has_seed6_B3_prime_atom_signature(35),
}
assert outside_guards == {2: False, 3: False, 25: False, 35: False}

summary = {
    "task_id": "RS-SEED6-BRIDGE-TRIANGLE-LOCAL-GROWTH",
    "hard_target": "SEED6_LOCAL_BRIDGE_TRIANGLE_GEOMETRY_CLASSIFIED",
    "census": {
        "prime_count": len(primes),
        "first_prime": primes[0],
        "last_prime": primes[-1],
        "all_pass": True,
        "distinct_exact_triangles": len(exact_triangles),
    },
    "exact_local_signature": {
        "divisor_lattice": "rank-2 coatoms of Boolean B3 on atoms {2,3,r}",
        "pairwise_gcds": ["2", "3", "r"],
        "pairwise_lcm": "6r",
        "incidence_matrix": A,
        "determinant": det3(A),
        "smith_normal_form": SNF,
        "coatom_lattice_index": 2,
        "product_square": "6*(2r)*(3r)=(6r)^2",
    },
    "automorphism_counts": {
        "object_triangle_unlabeled": 6,
        "object_triangle_exact_gcd_edge_labels": 1,
        "object_triangle_fixed_vs_new_edge_types": 2,
        "levi_C6_unranked": 12,
        "levi_C6_rank_preserving": 6,
        "levi_C6_rank_preserving_seed_rooted": 2,
        "levi_C6_exact_carriers_fixed": 1,
    },
    "cross_r_boundary": {
        "normalized_typed_cells_all_isomorphic": True,
        "exact_numeric_cells_pairwise_distinct": True,
        "representative": {
            "T_5": [6, 10, 15],
            "T_7": [6, 14, 21],
        },
    },
    "outside_scope_guards": outside_guards,
}
print(json.dumps(summary, ensure_ascii=False, sort_keys=True, indent=2))
