#!/usr/bin/env python3
"""Independent exact R063 component-root comparison; supplementary, not the frozen native benchmark.

This checker does NOT import the pinned R063 C3/C4 code or Gaussian
prime-allocation backend. It enumerates primitive Euclid parameter pairs
directly and compares complete ordered root sets to a separate isqrt
norm-fiber enumeration, then checks the sum-of-two-squares root-count formula.
It does not test the original 17 gates, discovery freeze, or native outputs.
"""
from collections import Counter
from hashlib import sha256
import json
from math import comb, gcd, isqrt


def brute_ordered_sector(r: int) -> tuple[tuple[int, int], ...]:
    n = r * r
    roots = []
    for a in range(r + 1):
        y2 = n - a * a
        b = isqrt(y2)
        if b * b == y2:
            roots.append((a, b))
    return tuple(roots)


def euclid_ordered_sector(r: int) -> tuple[tuple[int, int], ...]:
    roots = {(0, r), (r, 0)}
    for m in range(2, isqrt(r) + 1):
        for n in range(1, m):
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            h = m * m + n * n
            if r % h != 0:
                continue
            k = r // h
            a, b = k * (m * m - n * n), 2 * k * m * n
            roots.add((a, b))
            roots.add((b, a))
    return tuple(sorted(roots))


def predicted_root_count(r: int) -> int:
    """First-quadrant ordered roots = 1 + product(2*v_p(r)+1), p=1 mod 4."""
    x, p, product = r, 2, 1
    while p * p <= x:
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            if p % 4 == 1:
                product *= 2 * e + 1
        p = 3 if p == 2 else p + 2
    if x > 1 and x % 4 == 1:
        product *= 3
    return 1 + product


def main() -> None:
    rows = []
    counts = Counter()
    for r in range(1, 513):
        brute = brute_ordered_sector(r)
        generated = euclid_ordered_sector(r)
        assert generated == brute, ("root-set mismatch", r, generated, brute)
        assert len(generated) == predicted_root_count(r), ("root-count mismatch", r)
        counts[len(generated)] += 1
        rows.append({"r": r, "roots": [list(p) for p in generated]})
    roots50 = brute_ordered_sector(50)
    expected50 = ((0, 50), (14, 48), (30, 40), (40, 30), (48, 14), (50, 0))
    assert roots50 == expected50
    mass50 = sum(comb(a + b, a) for a, b in roots50)
    assert mass50 == 110695538274255714208
    assert sum(k * v for k, v in counts.items()) == 1820
    payload = json.dumps(rows, sort_keys=True, ensure_ascii=True, separators=(",", ":")).encode()
    print(json.dumps({
        "status": "PASS_INDEPENDENT_EUCLID_R063_ORDERED_SECTOR_512",
        "r_range": [1, 512],
        "r_count": 512,
        "ordered_root_occurrences": 1820,
        "root_count_histogram": {str(k): counts[k] for k in sorted(counts)},
        "max_root_count": max(counts),
        "r_at_max": [row["r"] for row in rows if len(row["roots"]) == max(counts)],
        "r50_roots": [list(p) for p in roots50],
        "r50_positive_chart_brc_mass": str(mass50),
        "exact_root_rows_sha256": sha256(payload).hexdigest(),
        "native_17_gates_executed": False,
        "native_regression_replayed": False,
        "independent_of_original_gaussian_backend": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
