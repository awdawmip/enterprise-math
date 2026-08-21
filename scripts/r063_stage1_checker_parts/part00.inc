#!/usr/bin/env python3
"""R063 Stage 1 deterministic general Gaussian path-norm-root checker.

Discovery is factorization-first.  No target-equation scan is reachable from
discover_general().  Brute verification starts only after discovery payloads
have been materialized and hashed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
from math import comb, isqrt
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple

sys.set_int_max_str_digits(0)

TASK_ID = "RS-R063-STAGE1-GENERAL-NON-SQUARE-PATH-NORM-ROOT-DISCOVERY"
TASKBOOK_SOURCE = "6a3c104f5e3a46125ccec6d591de6b824cf8dae9"
OWNER_BRANCH = "research/r063-stage1-general-path-norm-root"
RESEARCHER_ID = "EM-R063S1-6A3C10"
DEFAULT_MAX_N = 100000
MANDATORY_POSITIVE = (2, 5, 10, 13, 50, 65, 85, 125, 325)
MANDATORY_NEGATIVE = (3, 6, 7, 11, 12, 14, 15, 21, 27)
ANCHORS = (1, 25, 2500)
MULT_BASE = (2, 5, 13, 17, 25, 65)
SPARSE_SUITE = (
    999999937, 999999929, 999999893, 999999883, 1000000000,
    999999999, 999950000, 987654321, 536870912, 994990051,
    997210243, 9999991, 99999989, 500000005, 650000000,
    325000000, 125000000, 850000000, 130000000, 170000000,
)
STAGE0_N2500_ROOTSET_SHA256 = "6ae5a8224f4a4bcbdd2c83980ae70cda952e75893a3b3647a827b3c1082133ab"
STAGE0_N2500_TOTAL_PATH = 110695538274255714208

Gaussian = Tuple[int, int]
Pair = Tuple[int, int]
UNITS: Tuple[Tuple[str, Gaussian], ...] = (
    ("1", (1, 0)), ("J", (0, 1)), ("-1", (-1, 0)), ("-J", (0, -1)),
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
        raise ValueError("positive integer required")
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

def support_from_factors(factors: Mapping[int, int]) -> bool:
    return all(not (p % 4 == 3 and e % 2 == 1) for p, e in factors.items())

def support_reason(factors: Mapping[int, int]) -> Dict[str, object]:
    bad = [{"prime": p, "exponent": e} for p, e in sorted(factors.items()) if p % 4 == 3 and e % 2]
    return {
        "supported": not bad,
        "criterion": "every q == 3 (mod 4) has even exponent",
        "blocking_inert_prime_exponents": bad,
    }

def gmul(z: Gaussian, w: Gaussian) -> Gaussian:
    a, b = z
    c, d = w
    return (a*c - b*d, a*d + b*c)

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
    return z[0]*z[0] + z[1]*z[1]

def tonelli_shanks(n: int, p: int) -> int:
    n %= p
    if n == 0:
        return 0
    if p == 2:
        return n
    if pow(n, (p-1)//2, p) != 1:
        raise ValueError("not a quadratic residue")
    if p % 4 == 3:
        r = pow(n, (p+1)//4, p)
        return min(r, p-r)
    q = p-1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p-1)//2, p) != p-1:
        z += 1
    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q+1)//2, p)
    while t != 1:
        i = 1
        t2 = (t*t) % p
        while i < m and t2 != 1:
            t2 = (t2*t2) % p
            i += 1
        if i == m:
            raise ArithmeticError("Tonelli-Shanks invariant failure")
        b = pow(c, 1 << (m-i-1), p)
        r = (r*b) % p
        t = (t*b*b) % p
        c = (b*b) % p
        m = i
    return min(r, p-r)

@lru_cache(maxsize=None)
def split_prime_gaussian(p: int) -> Gaussian:
    if p <= 2 or p % 4 != 1:
        raise ValueError("p == 1 mod 4 required")
    t0 = tonelli_shanks(p-1, p)
    for t in sorted({t0, p-t0}):
        r0, r1 = p, t
        while r1*r1 > p:
            r0, r1 = r1, r0 % r1
        x = abs(r1)
        y2 = p - x*x
        y = isqrt(y2)
        if y*y == y2:
            a, b = sorted((x, y), reverse=True)
            if b > 0 and a*a + b*b == p:
                return (a, b)
    raise ArithmeticError(f"Cornacchia failed for {p}")

def gaussian_prime_typing(N: int) -> Dict[str, object]:
    factors = factor_integer(N)
    rows: List[Dict[str, object]] = []
    for p, e in sorted(factors.items()):
        if p == 2:
            rows.append({"prime": p, "exponent": e, "type": "RAMIFIED", "gaussian_prime": [1, 1]})
        elif p % 4 == 1:
            pi = split_prime_gaussian(p)
            rows.append({
                "prime": p, "exponent": e, "type": "SPLIT",
