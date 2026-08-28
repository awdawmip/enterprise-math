#!/usr/bin/env python3
"""Independent regression checker for the native tri-sector N2 Foundation admission audit.

Finite checks are regression only. The research return contains the exact proofs.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return n == d
        d += 1
    return True


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def shell_start(r: int) -> int:
    return 1 + 3 * r * (r - 1) // 2


def balanced_orbit(r: int) -> set[tuple[int, int, int]]:
    hi = (r + 1) // 2
    lo = r // 2
    return set(permutations((hi, lo, 0)))


def framed_position(r: int, frame: tuple[int, int, int], x: tuple[int, int, int]) -> int:
    i, j, k = frame
    if x[k] == 0:
        return x[j]
    if x[i] == 0:
        return r + x[k]
    if x[j] == 0:
        return 2 * r + x[i]
    raise AssertionError("state is not on the accepted shell sector support")


def barycenter_formula(r: int) -> int:
    return 1 + (3 * r * r + (r & 1)) // 2


def check_barycenter() -> dict[str, int]:
    frames = list(permutations((0, 1, 2)))
    label_evaluations = 0
    for r in range(2, 129):
        orbit = balanced_orbit(r)
        expected_size = 3 if r % 2 == 0 else 6
        assert len(orbit) == expected_size
        multisets = []
        for frame in frames:
            labels = sorted(shell_start(r) + framed_position(r, frame, x) for x in orbit)
            label_evaluations += len(labels)
            multisets.append(labels)
        assert all(labels == multisets[0] for labels in multisets)
        mean = Fraction(sum(multisets[0]), len(multisets[0]))
        z = (mean.numerator + mean.denominator - 1) // mean.denominator
        assert z == barycenter_formula(r)
    assert Fraction(1 + 2 + 3, 3) == 2
    assert barycenter_formula(1) == 3
    return {"shells": 127, "frames_per_shell": 6, "label_evaluations": label_evaluations}


def q0(p: int) -> set[int]:
    return {x * x % p for x in range(p)}


def breaker_cover(p: int) -> bool:
    inv2 = pow(2, -1, p)
    i0 = {(-3 * x * x * inv2) % p for x in range(p)}
    i1 = {(-3 * x * x * inv2 - inv2) % p for x in range(p)}
    return i0 | i1 == set(range(p))


def check_breaker() -> dict[str, object]:
    candidates = []
    character_identity_checks = 0
    for p in range(5, 200):
        if not is_prime(p) or p in (2, 3):
            continue
        delta = pow(3, -1, p)
        q = q0(p)
        actual = len(q & {(x + delta) % p for x in q})
        numerator = p + 1 + legendre(delta, p) + legendre(-delta, p)
        assert numerator % 4 == 0
        predicted = numerator // 4
        assert actual == predicted
        character_identity_checks += 1
        if breaker_cover(p):
            candidates.append(p)
    assert candidates == [5]
    return {"breaker_primes_below_200": candidates, "character_identity_checks": character_identity_checks}


def scalar_base_mod5(r: int) -> int:
    return ((3 * r * r + (r & 1)) * pow(2, -1, 5)) % 5


def cyclic_max_nonzero(base: list[int], h: int) -> int:
    n = len(base)
    zeros = [(h + value) % 5 == 0 for value in base]
    assert any(zeros)
    best = run = 0
    for flag in zeros + zeros:
        if flag:
            run = 0
        else:
            run += 1
            best = max(best, run)
    return min(best, n - 1)


def check_capacity() -> dict[str, object]:
    base = [scalar_base_mod5(r) for r in range(10)]
    assert base == [0, 2, 1, 4, 4, 3, 4, 4, 1, 2]
    rows = {}
    for h in range(5):
        zeros = [r for r, value in enumerate(base) if (h + value) % 5 == 0]
        rows[h] = {"zeros_mod_10": zeros, "max_nonzero_run": cyclic_max_nonzero(base, h)}
    assert all(rows[h]["zeros_mod_10"] for h in rows)
    assert max(rows[h]["max_nonzero_run"] for h in rows) == 9
    assert [h for h in rows if len(rows[h]["zeros_mod_10"]) == 1] == [0, 2]
    for h in range(5):
        seq = [((h + scalar_base_mod5(r)) % 5 == 0) for r in range(2, 302)]
        best = run = 0
        for z in seq:
            if z:
                run = 0
            else:
                run += 1
                best = max(best, run)
        assert best == rows[h]["max_nonzero_run"]
    return {"base_period_mod_5": base, "phase_rows": rows, "sharp_capacity": 9}


def packet_values(m: int, p: int) -> tuple[int, int, int]:
    return (
        (6 * m * m - 2 * m + 1) % p,
        (6 * m * m + 1) % p,
        (6 * m * m + 2 * m + 1) % p,
    )


def saturation_roots(p: int) -> tuple[set[int], set[int], set[int]]:
    roots = [set(), set(), set()]
    for m in range(p):
        vals = packet_values(m, p)
        for i, value in enumerate(vals):
            if value == 0:
                roots[i].add(m)
    return tuple(roots)  # type: ignore[return-value]


def check_transverse() -> dict[str, object]:
    saturated = []
    partitions = {}
    for p in range(5, 200):
        if not is_prime(p) or p in (2, 3):
            continue
        roots = saturation_roots(p)
        union = set().union(*roots)
        if union == set(range(1, p)):
            saturated.append(p)
            partitions[p] = [sorted(x) for x in roots]
    assert saturated == [5, 7]
    assert partitions[5] == [[1], [2, 3], [4]]
    assert partitions[7] == [[2, 3], [1, 6], [4, 5]]
    return {"saturation_primes_below_200": saturated, "root_partitions": partitions}


def check_mixed_parity_extremal() -> dict[str, int]:
    checked = 0
    for k in range(5, 102, 2):
        best = -1
        maximizing_pairs: set[tuple[int, int]] = set()
        for w in range(k):
            same_parity_candidates = [u for u in range(k) if (u - w) % 2 != 0]
            for u, v in combinations(same_parity_candidates, 2):
                d1, d2 = abs(w - u), abs(w - v)
                product = d1 * d2
                pair = tuple(sorted((d1, d2)))
                if product > best:
                    best = product
                    maximizing_pairs = {pair}
                elif product == best:
                    maximizing_pairs.add(pair)
        assert best == (k - 2) * (k - 4)
        assert maximizing_pairs == {(k - 4, k - 2)}
        checked += 1
    return {"odd_windows_checked": checked}


def main() -> None:
    bary = check_barycenter()
    breaker = check_breaker()
    capacity = check_capacity()
    transverse = check_transverse()
    longitudinal = check_mixed_parity_extremal()
    assert (9 - 4) * (9 - 2) == 35
    assert 3 * 35 == 105
    assert (105 + 1) // 2 == 53
    print({
        "status": "PASS",
        "barycenter": bary,
        "breaker": breaker,
        "capacity": capacity,
        "transverse": transverse,
        "mixed_parity": longitudinal,
        "scalar_chain": [3, [5, 7], 9, 35, 105, 53],
    })


if __name__ == "__main__":
    main()
