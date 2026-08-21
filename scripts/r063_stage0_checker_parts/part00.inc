#!/usr/bin/env python3
"""Deterministic R063 Stage 0 path-valued square-root checker.

Discovery is factorization-first.  The brute norm fiber exists only in the
verification phase and is never called by discover_from_scalar_root().
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction
from itertools import product
from math import comb, gcd, isqrt
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple

TASK_ID = "RS-R063-STAGE0-PATH-VALUED-SQUARE-ROOT-2500-DISCOVERY"
TASKBOOK_SOURCE = "e7dd7af0b7f01168afd25e55d04900e841cc399e"
OWNER_BRANCH = "research/r063-stage0-path-valued-sqrt-2500"
RESEARCHER_ID = "EM-R063S0-E7DD7A"
DEFAULT_N = 2500
REGRESSION_MAX_R = 512
SECTOR = "S_ij"

Gaussian = Tuple[int, int]
Pair = Tuple[int, int]

UNITS: Tuple[Tuple[str, Gaussian], ...] = (
    ("1", (1, 0)),
    ("J", (0, 1)),
    ("-1", (-1, 0)),
    ("-J", (0, -1)),
)


def canonical_json_bytes(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sha256_obj(obj: object) -> str:
    return hashlib.sha256(canonical_json_bytes(obj)).hexdigest()


def write_json(path: Path, obj: object) -> None:
    path.write_bytes(canonical_json_bytes(obj) + b"\n")


def write_text(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def factor_integer(n: int) -> Dict[int, int]:
    if n < 1:
        raise ValueError("factor_integer requires n >= 1")
    out: Dict[int, int] = {}
    x = n
    d = 2
    while d * d <= x:
        if x % d == 0:
            e = 0
            while x % d == 0:
                x //= d
                e += 1
            out[d] = e
        d = 3 if d == 2 else d + 2
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def factor_rows(n: int) -> List[Dict[str, int]]:
    return [{"prime": p, "exponent": e} for p, e in sorted(factor_integer(n).items())]


def divisors_from_factorization(factors: Mapping[int, int]) -> Tuple[int, ...]:
    values = [1]
    for p, e in sorted(factors.items()):
        values = [v * (p ** j) for v in values for j in range(e + 1)]
    return tuple(sorted(values))


def gmul(z: Gaussian, w: Gaussian) -> Gaussian:
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c)


def gconj(z: Gaussian) -> Gaussian:
    return (z[0], -z[1])


def gpow(z: Gaussian, e: int) -> Gaussian:
    if e < 0:
        raise ValueError("negative Gaussian exponent")
    out = (1, 0)
    base = z
    k = e
    while k:
        if k & 1:
            out = gmul(out, base)
        base = gmul(base, base)
        k >>= 1
    return out


def gnorm(z: Gaussian) -> int:
    return z[0] * z[0] + z[1] * z[1]


def tonelli_shanks(n: int, p: int) -> int:
    """Deterministic square root modulo an odd prime, returning the smaller root."""
    n %= p
    if n == 0:
        return 0
    if p == 2:
        return n
    if pow(n, (p - 1) // 2, p) != 1:
        raise ValueError("not a quadratic residue")
    if p % 4 == 3:
        r = pow(n, (p + 1) // 4, p)
        return min(r, p - r)
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1) // 2, p)
    while t != 1:
        i = 1
        t2i = (t * t) % p
        while i < m and t2i != 1:
            t2i = (t2i * t2i) % p
            i += 1
        if i == m:
            raise ArithmeticError("Tonelli-Shanks invariant failure")
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        t = (t * b * b) % p
        c = (b * b) % p
        m = i
    return min(r, p - r)


@lru_cache(maxsize=None)
def split_prime_gaussian(p: int) -> Gaussian:
    """Canonical p = pi * conjugate(pi) for p == 1 mod 4."""
    if p <= 2 or p % 4 != 1:
        raise ValueError("split_prime_gaussian requires p == 1 mod 4")
    t0 = tonelli_shanks(p - 1, p)
    for t in sorted({t0, p - t0}):
        r0, r1 = p, t
        while r1 * r1 > p:
            r0, r1 = r1, r0 % r1
        x = abs(r1)
        y2 = p - x * x
        y = isqrt(y2)
        if y * y == y2:
            a, b = sorted((x, y), reverse=True)
            if b > 0 and a * a + b * b == p:
                return (a, b)
    raise ArithmeticError(f"Cornacchia failed for split prime {p}")


def gaussian_factorization_metadata(M: int) -> Dict[str, object]:
    factors = factor_integer(M)
    rows: List[Dict[str, object]] = []
    representable = True
    for p, e in sorted(factors.items()):
        if p == 2:
            rows.append({
                "prime": p,
                "exponent_in_norm": e,
                "gaussian_type": "RAMIFIED",
                "gaussian_prime": [1, 1],
                "gaussian_exponent_fixed": e,
            })
        elif p % 4 == 1:
            pi = split_prime_gaussian(p)
            rows.append({
                "prime": p,
                "exponent_in_norm": e,
                "gaussian_type": "SPLIT",
                "pi": list(pi),
                "pi_conjugate": list(gconj(pi)),
                "allocation_range": [0, e],
            })
        else:
            if e % 2:
                representable = False
            rows.append({
                "prime": p,
                "exponent_in_norm": e,
                "gaussian_type": "INERT",
                "gaussian_integer_exponent": e // 2,
                "representable_requires_even_exponent": True,
            })
    return {
        "integer": M,
        "integer_factorization": factor_rows(M),
        "representable_as_gaussian_norm": representable,
        "gaussian_prime_rows": rows,
    }


def gaussian_norm_root_records(M: int) -> Tuple[Dict[Gaussian, List[Dict[str, object]]], Dict[str, object]]:
    """Construct every z in Z[J] with norm M from prime-factor allocation only."""
    factors = factor_integer(M)
    metadata = gaussian_factorization_metadata(M)
    if not metadata["representable_as_gaussian_norm"]:
        return {}, metadata

    base: Gaussian = (1, 0)
    split: List[Tuple[int, int, Gaussian]] = []
    for p, e in sorted(factors.items()):
        if p == 2:
            base = gmul(base, gpow((1, 1), e))
        elif p % 4 == 1:
            split.append((p, e, split_prime_gaussian(p)))
        else:
            base = gmul(base, (p ** (e // 2), 0))

    allocation_ranges = [range(e + 1) for _, e, _ in split]
    allocations = product(*allocation_ranges) if allocation_ranges else [()]
    roots: Dict[Gaussian, List[Dict[str, object]]] = defaultdict(list)
    for alloc in allocations:
        z = base
        alloc_rows: List[Dict[str, object]] = []
        for (p, e, pi), t in zip(split, alloc):
            z = gmul(z, gpow(pi, t))
            z = gmul(z, gpow(gconj(pi), e - t))
            alloc_rows.append({
                "prime": p,
                "pi_exponent": t,
                "conjugate_exponent": e - t,
            })
        for unit_name, unit in UNITS:
            w = gmul(unit, z)
            if gnorm(w) != M:
                raise ArithmeticError("Gaussian norm construction error")
            roots[w].append({
                "unit": unit_name,
                "split_prime_allocations": alloc_rows,
                "pre_unit_value": list(z),
                "value": list(w),
            })
    return dict(roots), metadata


@lru_cache(maxsize=None)
def gaussian_norm_root_set(M: int) -> Tuple[Gaussian, ...]:
