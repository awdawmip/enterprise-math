#!/usr/bin/env python3
"""Exact selected signed Z^3 cube / historical min-zero atlas fiber check.
Frozen X6 native: 59538f585d037d09ef687b28715c4bc1a3f9fe03
Frozen legacy: fd2bcff10ca6e147348b6c1236027fc0d2877df3
"""
from __future__ import annotations
from collections import Counter
from itertools import product
from math import factorial
from pathlib import Path
import hashlib
import json


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def rho(x: tuple[int, int, int]) -> tuple[int, int, int]:
    h = min(x)
    return tuple(a - h for a in x)


def brc(x: tuple[int, int, int]) -> int:
    a = tuple(abs(t) for t in x)
    den = 1
    for t in a:
        den *= factorial(t)
    return factorial(sum(a)) // den


def dom(x: tuple[int, int, int]) -> tuple[tuple[int, int], ...]:
    m = max(abs(a) for a in x)
    return tuple((i, 1 if a > 0 else -1) for i, a in enumerate(x) if abs(a) == m and m)


def shell(m: int):
    return (v for v in product(range(m + 1), repeat=3) if min(v) == 0 and max(v) == m)


def audit(d: int) -> dict:
    require(d >= 0, "nonnegative halfwidth")
    counts = Counter(rho(x) for x in product(range(-d, d + 1), repeat=3))
    n = 2 * d
    fibers = {v: n - max(v) + 1 for m in range(n + 1) for v in shell(m)}
    require(dict(counts) == fibers, f"d={d}: fiber map")
    require(len(counts) == 3*n*n + 3*n + 1, f"d={d}: atlas")
    for m in range(n + 1):
        require(sum(max(v) == m for v in counts) == (1 if m == 0 else 6*m), f"d={d}: shell {m}")
    weighted = n + 1 + sum(6*m*(n - m + 1) for m in range(1, n + 1))
    require(weighted == sum(counts.values()) == (2*d + 1)**3, f"d={d}: cube")
    return {"d": d, "native_cube_cardinality": (2*d + 1)**3,
            "atlas_observer_count": len(counts), "weighted_fiber_sum": weighted,
            "distinct_fiber_sizes": sorted(set(counts.values()))}


def main() -> None:
    rows = [audit(d) for d in range(9)]
    for d in range(9, 513):
        n = 2*d
        weighted = n + 1 + sum(6*m*(n - m + 1) for m in range(1, n + 1))
        require(weighted == (2*d + 1)**3, f"d={d}: closed polynomial")
        require(3*n*n + 3*n + 1 == 12*d*d + 6*d + 1, f"d={d}: atlas formula")
    x, y = (-1, 0, 0), (0, 1, 1)
    require(rho(x) == rho(y) == (0, 1, 1), "observer collision")
    require(sum(t*t for t in x) == 1 and sum(t*t for t in y) == 2, "native norms")
    require(brc(x) == 1 and brc(y) == 2, "native positive-path BRC")
    require(dom(x) == ((0, -1),) and dom(y) == ((1, 1), (2, 1)), "dominant signed axes")
    result = {
        "schema": "X6_LP011_VALUATION_FIBER_WEIGHTED_CUBE_V1",
        "scope": "selected signed three-axis Cell displacements [-d,d]^3; not full six-axis shell",
        "native_frozen_commit": "59538f585d037d09ef687b28715c4bc1a3f9fe03",
        "legacy_frozen_commit": "fd2bcff10ca6e147348b6c1236027fc0d2877df3",
        "source": "research_notes/TOOL_DISCOVERY_NATIVE_VALUATION_EHRHART_BRION_CALCULUS_REPORT_20260822.md",
        "fiber": "h in [-d,d-max(rho(x))], weight=2d-max(rho(x))+1",
        "exhaustive_cube_d": "0..8", "exact_polynomial_d": "0..512", "rows": rows,
        "counterexample": {"x": x, "y": y, "rho": rho(x), "G_x": 1, "G_y": 2,
                           "B_x": 1, "B_y": 2, "Dom_x": dom(x), "Dom_y": dom(y)},
        "status": "AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED"
    }
    raw = json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    result["payload_sha256"] = hashlib.sha256(raw.encode()).hexdigest()
    out = Path(__file__).with_name("X6_LP011_VALUATION_FIBER_WEIGHTED_CUBE_RESULTS_20261116_0700.json")
    out.write_text(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print("PASS_X6_LP011_VALUATION_FIBER_WEIGHTED_CUBE_0_512", result["payload_sha256"])
    for r in rows[:3]:
        print(r)


if __name__ == "__main__":
    main()
