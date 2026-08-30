#!/usr/bin/env python3
"""Exact finite regression for RS-ADDMUL-WITT-GHOST-MULTISCALE-BRIDGE.

No floating point and no external algebra package are used.
The checker verifies finite big-Witt and p-typical ghost identities,
recursive integrality gates, Dwork-style congruence gates over Z,
truncation locality, prime-power embedding, composite information loss,
and closure of actual ghost images under coordinatewise + and *.
"""

from __future__ import annotations

from itertools import product
from math import isqrt


def divisors(n: int) -> list[int]:
    if n <= 0:
        raise ValueError("n must be positive")
    return [d for d in range(1, n + 1) if n % d == 0]


def prime_factorization(n: int) -> dict[int, int]:
    if n <= 0:
        raise ValueError("n must be positive")
    out: dict[int, int] = {}
    x = n
    p = 2
    while p * p <= x:
        while x % p == 0:
            out[p] = out.get(p, 0) + 1
            x //= p
        p += 1
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def is_divisor_closed(S: tuple[int, ...] | list[int] | set[int]) -> bool:
    T = set(S)
    return all(d in T for n in T for d in divisors(n))


def big_ghost(a: dict[int, int], S: tuple[int, ...] | list[int]) -> dict[int, int]:
    Sset = set(S)
    out: dict[int, int] = {}
    for n in sorted(S):
        if any(d not in a for d in divisors(n) if d in Sset):
            raise ValueError("missing Witt coordinate")
        out[n] = sum(d * (a[d] ** (n // d)) for d in divisors(n) if d in Sset)
    return out


def big_inverse_recursive(
    g: dict[int, int], S: tuple[int, ...] | list[int]
) -> tuple[bool, dict[int, int], tuple[int, int] | None]:
    """Return (integral?, recovered coords, failure=(n,numerator))."""
    Ssorted = tuple(sorted(S))
    if not is_divisor_closed(Ssorted):
        raise ValueError("recursive inverse requires divisor-closed S")
    a: dict[int, int] = {}
    for n in Ssorted:
        numerator = g[n] - sum(
            d * (a[d] ** (n // d)) for d in divisors(n) if d < n
        )
        if numerator % n:
            return False, a, (n, numerator)
        a[n] = numerator // n
    return True, a, None


def big_dwork_gate(g: dict[int, int], S: tuple[int, ...] | list[int]) -> bool:
    """Big Dwork congruence gate specialized to Z (Frobenius lift=id)."""
    Sset = set(S)
    for n in S:
        for p, e in prime_factorization(n).items():
            if n // p not in Sset:
                raise ValueError("Dwork gate requires divisor-closed S")
            if (g[n] - g[n // p]) % (p ** e):
                return False
    return True


def retained_partial_big_ghost(
    a: dict[int, int], retained: set[int], n: int
) -> int:
    return sum(
        d * (a[d] ** (n // d))
        for d in divisors(n)
        if d in retained
    )


def omitted_coordinate_defect(
    a: dict[int, int], retained: set[int], n: int
) -> int:
    return sum(
        d * (a[d] ** (n // d))
        for d in divisors(n)
        if d not in retained
    )


def ptyp_ghost(coords: tuple[int, ...], p: int) -> tuple[int, ...]:
    if p <= 1:
        raise ValueError("p must be prime-like positive >1 for this checker")
    out = []
    for k in range(len(coords)):
        out.append(
            sum(
                (p ** i) * (coords[i] ** (p ** (k - i)))
                for i in range(k + 1)
            )
        )
    return tuple(out)


def ptyp_inverse_recursive(
    ghosts: tuple[int, ...], p: int
) -> tuple[bool, tuple[int, ...], tuple[int, int] | None]:
    coords: list[int] = []
    for k, gk in enumerate(ghosts):
        numerator = gk - sum(
            (p ** i) * (coords[i] ** (p ** (k - i)))
            for i in range(k)
        )
        modulus = p ** k
        if numerator % modulus:
            return False, tuple(coords), (k, numerator)
        coords.append(numerator // modulus)
    return True, tuple(coords), None


def ptyp_dwork_gate(ghosts: tuple[int, ...], p: int) -> bool:
    return all(
        (ghosts[k] - ghosts[k - 1]) % (p ** k) == 0
        for k in range(1, len(ghosts))
    )


def check() -> dict[str, int]:
    checks = 0

    # 1. Big Witt roundtrip and Dwork-gate equivalence for arbitrary small ghosts.
    big_dwork_vectors = 0
    for N in range(1, 7):
        S = tuple(range(1, N + 1))
        assert is_divisor_closed(S)
        for values in product(range(-2, 3), repeat=N):
            g = dict(zip(S, values))
            integral, _, _ = big_inverse_recursive(g, S)
            dwork = big_dwork_gate(g, S)
            assert integral == dwork
            checks += 1
            big_dwork_vectors += 1

    # Explicit inverse obstruction: S={1,2}, (g1,g2)=(0,1) gives a2=1/2.
    ok, a, failure = big_inverse_recursive({1: 0, 2: 1}, (1, 2))
    assert not ok and a == {1: 0} and failure == (2, 1)
    checks += 1

    # 2. Big Witt actual-image roundtrip and ghost-wise operation closure.
    S4 = (1, 2, 3, 4)
    big_states = []
    for vals in product((-1, 0, 1), repeat=len(S4)):
        a = dict(zip(S4, vals))
        g = big_ghost(a, S4)
        ok, recovered, failure = big_inverse_recursive(g, S4)
        assert ok and failure is None and recovered == a
        assert big_dwork_gate(g, S4)
        big_states.append((a, g))
        checks += 1

    big_operation_pairs = 0
    for _, gx in big_states:
        for _, gy in big_states:
            for op in ("add", "mul"):
                if op == "add":
                    gz = {n: gx[n] + gy[n] for n in S4}
                else:
                    gz = {n: gx[n] * gy[n] for n in S4}
                ok, z, failure = big_inverse_recursive(gz, S4)
                assert ok and failure is None
                assert big_ghost(z, S4) == gz
                assert big_dwork_gate(gz, S4)
                checks += 1
            big_operation_pairs += 1

    # 3. Divisor-closed projection is exact.
    S12 = tuple(range(1, 13))
    a12 = {n: ((-1) ** n) * (n % 3) for n in S12}
    g12 = big_ghost(a12, S12)
    divisor_closed_targets = [
        (1,),
        (1, 2),
        (1, 3),
        (1, 2, 4),
        (1, 2, 3, 6),
        (1, 2, 4, 8),
        (1, 2, 3, 4, 6, 12),
    ]
    for T in divisor_closed_targets:
        assert is_divisor_closed(T)
        restricted_a = {n: a12[n] for n in T}
        restricted_g = big_ghost(restricted_a, T)
        assert restricted_g == {n: g12[n] for n in T}
        checks += 1

    # 4. Exact arbitrary-retention defect and non-divisor-closed witness.
    # Retain n=6 but drop d=2: changing only a2 changes retained g6.
    full = {1: 0, 2: 1, 3: 0, 6: 0}
    retained = {1, 3, 6}
    assert not is_divisor_closed(retained)
    full_g6 = big_ghost(full, (1, 2, 3, 6))[6]
    partial_g6 = retained_partial_big_ghost(full, retained, 6)
    defect = omitted_coordinate_defect(full, retained, 6)
    assert full_g6 == partial_g6 + defect == 2
    full_zero = dict(full)
    full_zero[2] = 0
    assert big_ghost(full_zero, (1, 2, 3, 6))[6] == 0
    checks += 1

    # Test defect identity on many finite states and arbitrary retained subsets containing 1.
    defect_cases = 0
    S6 = (1, 2, 3, 4, 5, 6)
    for vals in product((-1, 0, 1), repeat=len(S6)):
        a = dict(zip(S6, vals))
        g = big_ghost(a, S6)
        for mask in range(1 << (len(S6) - 1)):
            retained = {1}
            for j, n in enumerate(S6[1:]):
                if (mask >> j) & 1:
                    retained.add(n)
            for n in retained:
                partial = retained_partial_big_ghost(a, retained, n)
                defect = omitted_coordinate_defect(a, retained, n)
                assert g[n] == partial + defect
                checks += 1
                defect_cases += 1

    # 5. p-typical: roundtrip, Dwork equivalence, operation closure, p=2,3,5.
    ptyp_dwork_vectors = 0
    ptyp_operation_pairs = 0
    for p in (2, 3, 5):
        for ghosts in product(range(-2, 3), repeat=4):
            integral, _, _ = ptyp_inverse_recursive(tuple(ghosts), p)
            assert integral == ptyp_dwork_gate(tuple(ghosts), p)
            checks += 1
            ptyp_dwork_vectors += 1

        states = []
        for coords in product((-1, 0, 1), repeat=4):
            ghosts = ptyp_ghost(coords, p)
            ok, recovered, failure = ptyp_inverse_recursive(ghosts, p)
            assert ok and failure is None and recovered == coords
            assert ptyp_dwork_gate(ghosts, p)
            states.append((coords, ghosts))
            checks += 1

        for _, gx in states:
            for _, gy in states:
                for op in ("add", "mul"):
                    if op == "add":
                        gz = tuple(x + y for x, y in zip(gx, gy))
                    else:
                        gz = tuple(x * y for x, y in zip(gx, gy))
                    ok, z, failure = ptyp_inverse_recursive(gz, p)
                    assert ok and failure is None
                    assert ptyp_ghost(z, p) == gz
                    assert ptyp_dwork_gate(gz, p)
                    checks += 1
                ptyp_operation_pairs += 1

        # Explicit failure witness g0=0,g1=1 => a1=1/p.
        ok, a, failure = ptyp_inverse_recursive((0, 1), p)
        assert not ok and a == (0,) and failure == (1, 1)
        checks += 1

    # 6. Exact embedding of p-typical prefix into big Witt prime-power subtruncation.
    prime_power_embedding_cases = 0
    for p in (2, 3, 5):
        Spp = tuple(p ** i for i in range(4))
        assert is_divisor_closed(Spp)
        for coords in product((-1, 0, 1), repeat=4):
            a = {p ** i: coords[i] for i in range(4)}
            bg = big_ghost(a, Spp)
            pg = ptyp_ghost(coords, p)
            assert tuple(bg[p ** i] for i in range(4)) == pg
            checks += 1
            prime_power_embedding_cases += 1

    # 7. Prime-power skeleton loses mixed-composite coordinates.
    # States differ only at a6; all prime-power coordinates <= 8 agree, but g6 differs by 6.
    S8 = tuple(range(1, 9))
    zero = {n: 0 for n in S8}
    mixed = dict(zero)
    mixed[6] = 1
    gz = big_ghost(zero, S8)
    gm = big_ghost(mixed, S8)
    pp = (1, 2, 3, 4, 5, 7, 8)
    assert all(gz[n] == gm[n] for n in pp)
    assert gm[6] - gz[6] == 6
    checks += 1

    # 8. Prefix locality for p-typical: retained lower prefix is exact.
    for p in (2, 3, 5):
        coords = (1, -1, 2, -2, 1)
        ghosts = ptyp_ghost(coords, p)
        for r in range(len(coords)):
            assert ptyp_ghost(coords[: r + 1], p) == ghosts[: r + 1]
            checks += 1

        # Non-prefix retention obstruction: g2 depends on dropped a1 with coefficient p.
        c0 = (0, 0, 0)
        c1 = (0, 1, 0)
        assert ptyp_ghost(c1, p)[2] - ptyp_ghost(c0, p)[2] == p
        checks += 1

    return {
        "checks": checks,
        "big_dwork_vectors": big_dwork_vectors,
        "big_operation_pairs": big_operation_pairs,
        "defect_cases": defect_cases,
        "ptyp_dwork_vectors": ptyp_dwork_vectors,
        "ptyp_operation_pairs": ptyp_operation_pairs,
        "prime_power_embedding_cases": prime_power_embedding_cases,
    }


if __name__ == "__main__":
    stats = check()
    print("PASS")
    for key in sorted(stats):
        print(f"{key}={stats[key]}")
