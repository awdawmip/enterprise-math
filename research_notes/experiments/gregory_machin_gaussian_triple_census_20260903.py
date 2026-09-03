#!/usr/bin/env python3
"""Exact bounded census for #1160 Gaussian-valuation three-denominator certificates.

This is a task-local research checker, not a registered global tool family.
It uses only Python's standard library and exact integer arithmetic for endpoint
certification. Floating-point logarithms are used only to rank the classical
Lehmer completion measure after exact endpoint feasibility has been decided.

Default height 5000 reproduces the 2026-09-03 research return.
"""

from __future__ import annotations

import argparse
import itertools
import math
from collections import defaultdict, deque
from functools import lru_cache


def factorint(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    while n % 2 == 0:
        out[2] = out.get(2, 0) + 1
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


@lru_cache(maxsize=None)
def sum_two_squares_prime(p: int) -> tuple[int, int]:
    assert p % 4 == 1
    for b in range(1, math.isqrt(p) + 1):
        a2 = p - b * b
        a = math.isqrt(a2)
        if a * a == a2:
            return (max(a, b), min(a, b))
    raise AssertionError(f"no sum-of-two-squares representation for p={p}")


def gaussian_div_exact(
    z: tuple[int, int], w: tuple[int, int]
) -> tuple[int, int] | None:
    a, b = z
    c, d = w
    norm = c * c + d * d
    nr = a * c + b * d
    ni = b * c - a * d
    if nr % norm or ni % norm:
        return None
    return (nr // norm, ni // norm)


@lru_cache(maxsize=None)
def signature(D: int) -> tuple[int, tuple[tuple[int, int], ...]]:
    """Return (epsilon mod 8, sorted split-prime oriented valuations)."""
    z = (D, 1)
    coords: dict[int, int] = {}
    for p, e in factorint(D * D + 1).items():
        if p == 2:
            continue
        assert p % 4 == 1, (D, p)
        pi = sum_two_squares_prime(p)
        pib = (pi[0], -pi[1])
        vp = vb = 0
        while True:
            q = gaussian_div_exact(z, pi)
            if q is None:
                break
            z = q
            vp += 1
        while True:
            q = gaussian_div_exact(z, pib)
            if q is None:
                break
            z = q
            vb += 1
        assert vp + vb == e, (D, p, e, pi, z, vp, vb)
        coords[p] = vp - vb

    ramified = 0
    while True:
        q = gaussian_div_exact(z, (1, 1))
        if q is None:
            break
        z = q
        ramified += 1

    unit_exp = {
        (1, 0): 0,
        (0, 1): 1,
        (-1, 0): 2,
        (0, -1): 3,
    }.get(z)
    assert unit_exp is not None, (D, z)
    epsilon = (ramified + 2 * unit_exp) % 8
    return epsilon, tuple(sorted((p, v) for p, v in coords.items() if v))


def support(D: int) -> tuple[int, ...]:
    return tuple(p for p, _ in signature(D)[1])


def leaf_prime_core(height: int) -> tuple[list[int], int, int]:
    denominators = list(range(2, height + 1))
    d_support = {D: support(D) for D in denominators}
    p_to_d: dict[int, set[int]] = defaultdict(set)
    for D, ps in d_support.items():
        for p in ps:
            p_to_d[p].add(D)

    active = set(denominators)
    degree = {p: len(ds) for p, ds in p_to_d.items()}
    queue = deque(p for p, d in degree.items() if d == 1)

    while queue:
        p = queue.popleft()
        if degree.get(p, 0) != 1:
            continue
        neighbors = [D for D in p_to_d[p] if D in active]
        if len(neighbors) != 1:
            continue
        D = neighbors[0]
        active.remove(D)
        for pp in d_support[D]:
            degree[pp] -= 1
            if degree[pp] == 1:
                queue.append(pp)

    core_primes = set()
    for D in active:
        core_primes.update(d_support[D])
    return sorted(active), height - 1 - len(active), len(core_primes)


def normalized_direction(items: tuple[tuple[int, int], ...]) -> tuple[tuple[int, int], ...]:
    g = 0
    for _, v in items:
        g = math.gcd(g, abs(v))
    vals = tuple((p, v // g) for p, v in items)
    if vals and vals[0][1] < 0:
        vals = tuple((p, -v) for p, v in vals)
    return vals


def sparse_wedge_key(
    v: dict[int, int], w: dict[int, int]
) -> tuple[tuple[int, int, int], ...] | None:
    indices = sorted(set(v) | set(w))
    minors: list[tuple[int, int, int]] = []
    g = 0
    for pos, i in enumerate(indices):
        vi = v.get(i, 0)
        wi = w.get(i, 0)
        for j in indices[pos + 1 :]:
            val = vi * w.get(j, 0) - v.get(j, 0) * wi
            if val:
                minors.append((i, j, val))
                g = math.gcd(g, abs(val))
    if not minors:
        return None
    minors = [(i, j, val // g) for i, j, val in minors]
    if minors[0][2] < 0:
        minors = [(i, j, -val) for i, j, val in minors]
    return tuple(minors)


def cross(a: tuple[int, int, int], b: tuple[int, int, int]) -> tuple[int, int, int]:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def dot(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def normalize_int_vector(v: tuple[int, int, int]) -> tuple[int, int, int]:
    g = math.gcd(math.gcd(abs(v[0]), abs(v[1])), abs(v[2]))
    v = tuple(x // g for x in v)
    for x in v:
        if x:
            if x < 0:
                v = tuple(-y for y in v)
            break
    return v


def lehmer_measure(trio: tuple[int, int, int]) -> float:
    return sum(1.0 / math.log10(D) for D in trio)


def census(height: int):
    core, removed, core_prime_count = leaf_prime_core(height)

    prime_index = {
        p: i
        for i, p in enumerate(sorted({p for D in core for p in support(D)}))
    }
    vectors: dict[int, dict[int, int]] = {}
    eps: dict[int, int] = {}
    raw_coords: dict[int, dict[int, int]] = {}
    direction_groups: dict[tuple[tuple[int, int], ...], list[int]] = defaultdict(list)

    for D in core:
        e, items = signature(D)
        eps[D] = e
        coords = dict(items)
        raw_coords[D] = coords
        vectors[D] = {prime_index[p]: v for p, v in items}
        direction_groups[normalized_direction(items)].append(D)

    span_sets: dict[tuple[tuple[int, int, int], ...], set[int]] = defaultdict(set)
    for a, b in itertools.combinations(core, 2):
        key = sparse_wedge_key(vectors[a], vectors[b])
        if key is not None:
            span_sets[key].update((a, b))

    candidate_triples: set[tuple[int, int, int]] = set()
    for denominators in span_sets.values():
        if len(denominators) >= 3:
            candidate_triples.update(itertools.combinations(sorted(denominators), 3))

    endpoint_sets = []
    for trio in candidate_triples:
        primes = sorted(set().union(*(raw_coords[D] for D in trio)))
        rows = [tuple(raw_coords[D].get(p, 0) for D in trio) for p in primes]
        r1 = next(r for r in rows if any(r))
        r2 = next((r for r in rows if cross(r1, r) != (0, 0, 0)), None)
        if r2 is None:
            continue
        c0 = normalize_int_vector(cross(r1, r2))
        if 0 in c0 or not all(dot(r, c0) == 0 for r in rows):
            continue

        torsion = sum(c * eps[D] for c, D in zip(c0, trio)) % 8
        if torsion % 2 == 0:
            continue

        # Every odd residue is its own inverse mod 8. Choose the least-absolute
        # integer representative that sends torsion to 1 mod 8.
        scale = min((torsion, torsion - 8), key=abs)
        coeffs = tuple(scale * c for c in c0)
        assert sum(c * eps[D] for c, D in zip(coeffs, trio)) % 8 == 1
        for p in primes:
            assert sum(c * raw_coords[D].get(p, 0) for c, D in zip(coeffs, trio)) == 0

        endpoint_sets.append(
            (lehmer_measure(trio), sum(abs(c) for c in coeffs), trio, coeffs)
        )

    rank_one_groups = sorted(
        sorted(ds) for ds in direction_groups.values() if len(ds) >= 3
    )
    endpoint_sets.sort()
    return {
        "height": height,
        "core_size": len(core),
        "removed": removed,
        "core_prime_count": core_prime_count,
        "candidate_rank2_triples": len(candidate_triples),
        "rank2_endpoint_sets": len(endpoint_sets),
        "rank_one_groups": rank_one_groups,
        "best": endpoint_sets,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--height", type=int, default=5000)
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args()
    assert args.height >= 3

    result = census(args.height)
    print(f"height={result['height']}")
    print(f"core_size={result['core_size']}")
    print(f"removed_by_leaf_prime={result['removed']}")
    print(f"core_split_primes={result['core_prime_count']}")
    print(f"candidate_rank2_triples={result['candidate_rank2_triples']}")
    print(f"rank2_endpoint_sets={result['rank2_endpoint_sets']}")
    print(f"rank_one_groups={result['rank_one_groups']}")
    print("best_by_Lehmer_measure:")
    for mu, l1, trio, coeffs in result["best"][: args.top]:
        print(f"  mu={mu:.15f} L1={l1:3d} D={trio} c={coeffs}")

    if args.height == 5000:
        assert result["core_size"] == 1913
        assert result["removed"] == 3086
        assert result["core_prime_count"] == 446
        assert result["candidate_rank2_triples"] == 9433
        assert result["rank2_endpoint_sets"] == 86
        assert result["rank_one_groups"] == [[2, 3, 7]]
        mu, l1, trio, coeffs = result["best"][0]
        assert trio == (18, 57, 239)
        assert coeffs == (12, 8, -5)
        assert l1 == 25
        assert abs(mu - 1.7866075340193157) < 1e-14
        print("H=5000 regression certificate: PASS")


if __name__ == "__main__":
    main()
