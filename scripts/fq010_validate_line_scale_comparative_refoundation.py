#!/usr/bin/env python3
"""
Deterministic validator for FQ010 line-scale comparative refoundation.

No floating point, metric, current LENGTH value, or external package is used.
All theorem decisions are exact finite/integer/relational checks.
"""
from __future__ import annotations

import json
from collections import defaultdict
from itertools import product, permutations
from typing import Dict, Iterator, List, Sequence, Set, Tuple

Token = Tuple[int, int]
Pair = Tuple[Token, Token]
Triple = Tuple[int, int, int]

MAX_N = 8
MAX_EXHAUSTIVE_TOKENS = 6
COMPONENTS = (0, 1, 2)
S3 = tuple(permutations(COMPONENTS))


def sector_supported_states(max_n: int = MAX_N) -> List[Triple]:
    return [t for t in product(range(max_n + 1), repeat=3) if 0 in t]


def tokens(n: Triple) -> Tuple[Token, ...]:
    return tuple((c, i) for c in COMPONENTS for i in range(n[c]))


def r_type(n: Triple) -> Set[Pair]:
    u = tokens(n)
    return {(x, y) for x in u for y in u if x[0] == y[0]}


def r_fine(n: Triple) -> Set[Pair]:
    u = tokens(n)
    return {(x, x) for x in u}


def r_coarse(n: Triple) -> Set[Pair]:
    u = tokens(n)
    return {(x, y) for x in u for y in u}


def qk(n: Triple) -> int:
    return len(r_type(n))


def q_formula(n: Triple) -> int:
    return sum(v * v for v in n)


def total(n: Triple) -> int:
    return sum(n)


def permute_state(n: Triple, sigma: Sequence[int]) -> Triple:
    out = [0, 0, 0]
    for old in COMPONENTS:
        out[sigma[old]] = n[old]
    return tuple(out)  # type: ignore[return-value]


def component_relabel_token(x: Token, sigma: Sequence[int]) -> Token:
    return (sigma[x[0]], x[1])


def image_relation(rel: Set[Pair], f) -> Set[Pair]:
    return {(f(x), f(y)) for x, y in rel}


def token_renamings(n: Triple):
    # Two deterministic fiberwise bijections. Exact proof for arbitrary
    # renaming is supplied in the theorem packet; these are regressions.
    def reverse(x: Token) -> Token:
        c, i = x
        return (c, n[c] - 1 - i)

    def rotate(x: Token) -> Token:
        c, i = x
        return (c, (i + 1) % n[c]) if n[c] else x

    return (reverse, rotate)


def set_partitions(items: Tuple[int, ...]) -> Iterator[Tuple[Tuple[int, ...], ...]]:
    """Generate every set partition, with canonicalization performed later."""
    if not items:
        yield ()
        return
    first = items[0]
    for part in set_partitions(items[1:]):
        yield ((first,),) + part
        for i in range(len(part)):
            new_block = tuple(sorted((first,) + part[i]))
            new_part = list(part)
            new_part[i] = new_block
            new_part = sorted(new_part, key=lambda b: b[0])
            yield tuple(new_part)


def canonical_partitions(items: Tuple[int, ...]) -> Iterator[Tuple[Tuple[int, ...], ...]]:
    seen = set()
    for p in set_partitions(items):
        key = tuple(sorted((tuple(sorted(b)) for b in p), key=lambda b: b[0]))
        if key not in seen:
            seen.add(key)
            yield key


def relation_from_partition(
    partition: Tuple[Tuple[int, ...], ...], u: Tuple[Token, ...]
) -> Set[Pair]:
    rel: Set[Pair] = set()
    for block in partition:
        for i in block:
            for j in block:
                rel.add((u[i], u[j]))
    return rel


def partition_preserves_component_observation(
    partition: Tuple[Tuple[int, ...], ...], u: Tuple[Token, ...]
) -> bool:
    return all(len({u[i][0] for i in block}) <= 1 for block in partition)


def fq008_reconstruct(max_n: int = MAX_N) -> Dict[Tuple[int, int], int]:
    """Reconstruct Q solely from axis-square boundary + zero mixed difference."""
    q: Dict[Tuple[int, int], int] = {}
    for a in range(max_n + 1):
        q[(a, 0)] = a * a
    for b in range(max_n + 1):
        q[(0, b)] = b * b
    for a in range(1, max_n + 1):
        for b in range(1, max_n + 1):
            q[(a, b)] = q[(a - 1, b)] + q[(a, b - 1)] - q[(a - 1, b - 1)]
    return q


def mixed_second_difference(f, a: int, b: int) -> int:
    return f(a + 1, b + 1) - f(a + 1, b) - f(a, b + 1) + f(a, b)


def main() -> int:
    mismatches: List[dict] = []
    states = sector_supported_states()

    relation_checks = 0
    relabel_checks = 0
    token_rename_checks = 0
    for n in states:
        rel = r_type(n)
        relation_checks += 1
        if len(rel) != q_formula(n):
            mismatches.append(
                {"kind": "relation_cardinality", "state": n, "got": len(rel), "want": q_formula(n)}
            )

        for sigma in S3:
            n2 = permute_state(n, sigma)
            f = lambda x, sigma=sigma: component_relabel_token(x, sigma)
            if image_relation(rel, f) != r_type(n2):
                mismatches.append(
                    {"kind": "component_relabel_equivariance", "state": n, "sigma": sigma}
                )
            relabel_checks += 1

        for f in token_renamings(n):
            if image_relation(rel, f) != rel:
                mismatches.append({"kind": "token_rename_invariance", "state": n})
            token_rename_checks += 1

    # Exhaustively enumerate all equivalence relations (= set partitions) on
    # small carriers and verify R_type is the unique greatest relation through
    # whose quotient the component observation still factors.
    maximality_states = 0
    maximality_partitions = 0
    component_preserving_partitions = 0
    for n in states:
        u = tokens(n)
        if len(u) > MAX_EXHAUSTIVE_TOKENS:
            continue
        maximality_states += 1
        rt = r_type(n)
        for partition in canonical_partitions(tuple(range(len(u)))):
            maximality_partitions += 1
            if not partition_preserves_component_observation(partition, u):
                continue
            component_preserving_partitions += 1
            e = relation_from_partition(partition, u)
            if not e.issubset(rt):
                mismatches.append(
                    {"kind": "maximality_failure", "state": n, "partition": partition}
                )
        if any(x[0] != y[0] for x, y in rt):
            mismatches.append({"kind": "r_type_not_component_preserving", "state": n})

    axis_checks = 0
    for c in COMPONENTS:
        for nval in range(MAX_N + 1):
            state = [0, 0, 0]
            state[c] = nval
            state_t = tuple(state)
            if qk(state_t) != nval * nval:
                mismatches.append(
                    {"kind": "axis_square", "component": c, "n": nval, "got": qk(state_t)}
                )
            axis_checks += 1

    mixed_checks = 0
    sector_pairs = ((0, 1), (1, 2), (2, 0))
    for i, j in sector_pairs:
        def f(a: int, b: int, i=i, j=j) -> int:
            n = [0, 0, 0]
            n[i], n[j] = a, b
            return qk(tuple(n))

        for a in range(MAX_N):
            for b in range(MAX_N):
                d2 = mixed_second_difference(f, a, b)
                if d2 != 0:
                    mismatches.append(
                        {"kind": "mixed_second_difference", "sector": (i, j), "a": a, "b": b, "got": d2}
                    )
                mixed_checks += 1

    fq = fq008_reconstruct()
    fq008_checks = 0
    for i, j in sector_pairs:
        for a in range(MAX_N + 1):
            for b in range(MAX_N + 1):
                n = [0, 0, 0]
                n[i], n[j] = a, b
                got = fq[(a, b)]
                want = qk(tuple(n))
                if got != want:
                    mismatches.append(
                        {"kind": "fq008_reconstruction", "sector": (i, j), "a": a, "b": b, "got": got, "want": want}
                    )
                fq008_checks += 1

    observation_checks = 0
    for n in states:
        fine = len(r_fine(n))
        comp = len(r_type(n))
        coarse = len(r_coarse(n))
        if fine != total(n):
            mismatches.append({"kind": "fine_readout", "state": n, "got": fine, "want": total(n)})
        if comp != q_formula(n):
            mismatches.append({"kind": "component_readout", "state": n, "got": comp, "want": q_formula(n)})
        if coarse != total(n) ** 2:
            mismatches.append({"kind": "coarse_readout", "state": n, "got": coarse, "want": total(n) ** 2})
        observation_checks += 1

    # Orbit-level scalar collisions witness relation-to-scalar information loss.
    by_q: Dict[int, Set[Triple]] = defaultdict(set)
    for n in states:
        by_q[qk(n)].add(tuple(sorted(n)))
    collisions = []
    for q, sigs in sorted(by_q.items()):
        if len(sigs) > 1:
            collisions.append({"q": q, "orbit_signatures": [list(s) for s in sorted(sigs)]})

    required_witnesses = {
        25: {(0, 0, 5), (0, 3, 4)},
        65: {(0, 1, 8), (0, 4, 7)},
    }
    collision_map = {item["q"]: {tuple(x) for x in item["orbit_signatures"]} for item in collisions}
    for q, witnesses in required_witnesses.items():
        if not witnesses.issubset(collision_map.get(q, set())):
            mismatches.append({"kind": "missing_collision_witness", "q": q})

    discriminator = {
        "fine_axis_n2": len(r_fine((2, 0, 0))),
        "component_axis_n2": len(r_type((2, 0, 0))),
        "coarse_axis_n2": len(r_coarse((2, 0, 0))),
        "fine_mixed_d2": mixed_second_difference(lambda a, b: a + b, 0, 0),
        "component_mixed_d2": mixed_second_difference(lambda a, b: a*a + b*b, 0, 0),
        "coarse_mixed_d2": mixed_second_difference(lambda a, b: (a+b)*(a+b), 0, 0),
    }
    expected_discriminator = {
        "fine_axis_n2": 2,
        "component_axis_n2": 4,
        "coarse_axis_n2": 4,
        "fine_mixed_d2": 0,
        "component_mixed_d2": 0,
        "coarse_mixed_d2": 2,
    }
    if discriminator != expected_discriminator:
        mismatches.append(
            {"kind": "resolution_discriminator", "got": discriminator, "want": expected_discriminator}
        )

    regression = {
        "schema": "FQ010_REGRESSION_V1",
        "max_component_multiplicity": MAX_N,
        "sector_supported_state_count": len(states),
        "relation_construction_checks": relation_checks,
        "component_relabeling_checks": relabel_checks,
        "token_renaming_regression_checks": token_rename_checks,
        "maximality_exhaustive_token_limit": MAX_EXHAUSTIVE_TOKENS,
        "maximality_state_count": maximality_states,
        "equivalence_partitions_enumerated": maximality_partitions,
        "component_preserving_equivalence_partitions": component_preserving_partitions,
        "axis_square_checks": axis_checks,
        "mixed_second_difference_checks": mixed_checks,
        "fq008_reconstruction_checks": fq008_checks,
        "observation_resolution_checks": observation_checks,
        "scalar_collision_group_count": len(collisions),
        "scalar_collision_witnesses": [x for x in collisions if x["q"] in (25, 65)],
        "observation_resolution_discriminator": discriminator,
        "mismatch_count": len(mismatches),
        "status": "PASS" if not mismatches else "FAIL",
    }

    print(json.dumps({"regression": regression, "mismatches": mismatches}, indent=2, sort_keys=True))
    return 0 if not mismatches else 1


if __name__ == "__main__":
    raise SystemExit(main())
