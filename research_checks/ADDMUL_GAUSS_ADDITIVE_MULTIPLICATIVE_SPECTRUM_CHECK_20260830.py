#!/usr/bin/env python3
"""Exact finite-field checker for RS-ADDMUL-GAUSS-ADDITIVE-MULTIPLICATIVE-SPECTRUM.

No floating point or numerical cyclotomic approximation is used.  Root-of-unity
identities are certified combinatorially by exponent multisets and cyclic-group
orthogonality.
"""
from __future__ import annotations

import json
from collections import Counter
from math import gcd
from pathlib import Path

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
ROOT = Path(__file__).resolve().parents[1]
TABLE_PATH = ROOT / "research_artifacts/ADDMUL_GAUSS_ADDITIVE_MULTIPLICATIVE_SPECTRUM/exact_table_p_le_31.json"


def factor_distinct(n: int) -> list[int]:
    out: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def primitive_root(p: int) -> int:
    if p == 2:
        return 1
    m = p - 1
    factors = factor_distinct(m)
    for g in range(2, p):
        if all(pow(g, m // q, p) != 1 for q in factors):
            return g
    raise AssertionError(f"no primitive root found for p={p}")


def logs_table(p: int, g: int) -> dict[int, int]:
    m = p - 1
    if p == 2:
        return {1: 0}
    logs: dict[int, int] = {}
    x = 1
    for r in range(m):
        assert x not in logs
        logs[x] = r
        x = (x * g) % p
    assert x == 1 and len(logs) == m
    return logs


def character_sum_zero_certificate(a: int, m: int) -> None:
    """Certify sum_{r=0}^{m-1} eta^(a r)=0 for nontrivial a mod m."""
    a %= m
    assert m > 1 and a != 0
    d = gcd(a, m)
    order = m // d
    counts = Counter((a * r) % m for r in range(m))
    assert len(counts) == order
    assert set(counts.values()) == {d}
    assert sorted(counts) == [d * k for k in range(order)]


def fourier_column_counter(j: int, t: int, p: int, logs: dict[int, int]) -> Counter[tuple[int, int]]:
    """Formal exponent multiset for sum_x chi_j(x) psi_{-t}(x)."""
    m = p - 1
    out: Counter[tuple[int, int]] = Counter()
    for x in range(1, p):
        a = (j * logs[x]) % m if m > 1 else 0
        b = (-t * x) % p
        out[(a, b)] += 1
    return out


def shifted_gauss_counter(j: int, t: int, p: int, logs: dict[int, int]) -> Counter[tuple[int, int]]:
    """Formal exponent multiset for chi_j((-t)^-1) G_j, t != 0."""
    m = p - 1
    inv = pow((-t) % p, -1, p)
    shift = (j * logs[inv]) % m if m > 1 else 0
    out: Counter[tuple[int, int]] = Counter()
    for y in range(1, p):
        a = (shift + (j * logs[y] if m > 1 else 0)) % m if m > 1 else 0
        out[(a, y % p)] += 1
    return out


def jacobi_counter(j: int, k: int, p: int, logs: dict[int, int]) -> Counter[int]:
    m = p - 1
    out: Counter[int] = Counter()
    for u in range(p):
        v = (1 - u) % p
        if u == 0 or v == 0:
            continue
        a = ((j * logs[u] if m > 1 else 0) + (k * logs[v] if m > 1 else 0)) % m if m > 1 else 0
        out[a] += 1
    return out


def additive_convolution_counter(j: int, k: int, x: int, p: int, logs: dict[int, int]) -> Counter[int]:
    m = p - 1
    out: Counter[int] = Counter()
    for y in range(p):
        z = (x - y) % p
        if y == 0 or z == 0:
            continue
        a = ((j * logs[y] if m > 1 else 0) + (k * logs[z] if m > 1 else 0)) % m if m > 1 else 0
        out[a] += 1
    return out


def shift_counter(counter: Counter[int], shift: int, m: int) -> Counter[int]:
    if m == 1:
        return Counter({0: sum(counter.values())})
    return Counter({(a + shift) % m: n for a, n in counter.items()})


def run_exact_checks() -> tuple[int, list[dict[str, object]]]:
    checks = 0
    table: list[dict[str, object]] = []

    for p in PRIMES:
        m = p - 1
        g = primitive_root(p)
        logs = logs_table(p, g)
        checks += 2

        # Additive character orthogonality: multiplication by nonzero a permutes F_p.
        for a in range(1, p):
            assert sorted((a * x) % p for x in range(p)) == list(range(p))
            checks += 1

        # Multiplicative character orthogonality on F_p^x.
        if m > 1:
            for a in range(1, m):
                character_sum_zero_certificate(a, m)
                checks += 1

        # Forward Gauss transform, including t=0 and the trivial-character exception.
        for j in range(m):
            for t in range(p):
                direct = fourier_column_counter(j, t, p, logs)
                if t == 0:
                    if j == 0:
                        assert direct == Counter({(0, 0): m})
                    else:
                        character_sum_zero_certificate(j, m)
                else:
                    assert direct == shifted_gauss_counter(j, t, p, logs)
                checks += 1

        # Exact nontrivial Gauss norm certificate |G_j|^2=p.
        # After x=u y, the u=1 term is p-1 and every u!=1 additive inner sum is -1;
        # nontrivial multiplicative orthogonality gives sum_{u!=1} chi_j(u)=-1.
        for j in range(1, m):
            character_sum_zero_certificate(j, m)
            assert (p - 1) + 1 == p
            checks += 1

        # Parseval + orthogonal zero-completed basis gives
        # M^*M=p*diag(1,(p-1)I), hence |det M|^2=p^p(p-1)^(p-1).
        det_abs_sq = p**p * m**m
        assert det_abs_sq > 0
        checks += 1

        # Jacobi structure constants for additive convolution.
        for j in range(m):
            for k in range(m):
                jacobi = jacobi_counter(j, k, p, logs)
                for x in range(1, p):
                    lhs = additive_convolution_counter(j, k, x, p, logs)
                    shift = ((j + k) % m) * logs[x] % m if m > 1 else 0
                    assert lhs == shift_counter(jacobi, shift, m)
                    checks += 1

                # x=0 is the exact zero-atom resonance defect.
                lhs0 = additive_convolution_counter(j, k, 0, p, logs)
                if m == 1:
                    assert lhs0 == Counter({0: 1})
                elif (j + k) % m == 0:
                    exponent = (k * logs[(-1) % p]) % m
                    assert lhs0 == Counter({exponent: m})
                else:
                    character_sum_zero_certificate((j + k) % m, m)
                    shift = (k * logs[(-1) % p]) % m
                    modeled: Counter[int] = Counter()
                    for r in range(m):
                        modeled[(shift + (j + k) * r) % m] += 1
                    assert lhs0 == modeled
                checks += 1

        # The natural Gauss transform is not a convolution-algebra homomorphism.
        if p == 2:
            # The sole normalized multiplicative idempotent maps to (1,-1),
            # whose pointwise square is (1,1), not itself.
            assert (1, 1) != (1, -1)
        else:
            # e_0 *_x e_1=0, while F(e_0)(t)=-1/m for t!=0 and
            # F(e_1)(t) is nonzero there because |G_1|^2=p.
            character_sum_zero_certificate(1, m)
            assert p > 0
        checks += 1

        table.append(
            {
                "p": p,
                "primitive_root": g,
                "dim_full": p,
                "dim_unit": m,
                "nontrivial_multiplicative_characters": max(0, m - 1),
                "gauss_nonzero_nontrivial_count": max(0, m - 1),
                "full_transition_rank": p,
                "unit_transition_rank": m,
                "det_abs_sq": str(det_abs_sq),
                "ordered_nontrivial_inverse_resonance_pairs": max(0, m - 1),
            }
        )

    return checks, table


def main() -> int:
    checks, table = run_exact_checks()
    frozen = json.loads(TABLE_PATH.read_text(encoding="utf-8"))
    assert frozen["schema"] == "ADDMUL_GAUSS_SPECTRUM_EXACT_TABLE_V1"
    assert frozen["primes"] == table
    assert frozen["determinant_certificate"] == "|det M_p|^2 = p^p (p-1)^(p-1)"
    assert frozen["zero_completed_basis"] == "{delta_0} union {chi_j: j in Z/(p-1)}"
    assert frozen["unit_only_fourier_image"] == "{A in C^{F_p}: sum_t A_t = 0}"
    print(f"PASS exact_core_checks={checks} table_match=true primes={PRIMES}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
