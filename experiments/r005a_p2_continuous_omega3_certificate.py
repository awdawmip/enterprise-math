#!/usr/bin/env python3
"""R005-A continuous p=2 Omega=3 residual certificate through k=894427190.

Combines exact local verification for 2<=k<11990 with an external exhaustive prime-gap premise plus the known maximal-gap first-occurrence record table for 11990<=k<=894427190.

It proves a residual-arity statement, NOT no-residual / least-basis.
"""

from __future__ import annotations
import importlib.util
from math import isqrt
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
SRC = HERE / "r005a_p2_exact_residual_family.py"
spec = importlib.util.spec_from_file_location("p2family", SRC)
if spec is None or spec.loader is None:
    raise RuntimeError(f"cannot load {SRC}")
family = importlib.util.module_from_spec(spec)
spec.loader.exec_module(family)

X = 400_000_000_000_000_000

# (first prime P, actual next-prime difference). PrimePages displays number of
# composites in its maximal-gap table, so these are displayed_gap+1.
RECORD_GAPS = [
    (2,1),(3,2),(7,4),(23,6),(89,8),(113,14),(523,18),(887,20),(1129,22),(1327,34),
    (9551,36),(15683,44),(19609,52),(31397,72),(155921,86),(360653,96),(370261,112),
    (492113,114),(1349533,118),(1357201,132),(2010733,148),(4652353,154),(17051707,180),
    (20831323,210),(47326693,220),(122164747,222),(189695659,234),(191912783,248),
    (387096133,250),(436273009,282),(1294268491,288),(1453168141,292),(2300942549,320),
    (3842610773,336),(4302407359,354),(10726904659,382),(20678048297,384),(22367084959,394),
    (25056082087,456),(42652618343,464),(127976334671,468),(182226896239,474),
    (241160624143,486),(297501075799,490),(303371455241,500),(304599508537,514),
    (416608695821,516),(461690510011,532),(614487453523,534),(738832927927,540),
    (1346294310749,582),(1408695493609,588),(1968188556461,602),(2614941710599,652),
    (7177162611713,674),(13829048559701,716),(19581334192423,766),(42842283925351,778),
    (90874329411493,804),(171231342420521,806),(218209405436543,906),(1189459969825483,916),
    (1686994940955803,924),(1693182318746371,1132),(43841547845541059,1184),
    (55350776431903243,1198),(80873624627234849,1220),(203986478517455989,1224),
    (218034721194214273,1248),(305405826521087869,1272),(352521223451364323,1328),
    (401429925999153707,1356),
]


def ceil_sqrt(n: int) -> int:
    r = isqrt(n)
    return r if r*r == n else r + 1


def c4(k: int) -> int:
    return isqrt(k)


def gmax(x: int) -> int:
    g = 1
    for start, gap in RECORD_GAPS:
        if start <= x:
            g = gap
        else:
            break
    return g


def exact_small_prefix() -> dict:
    failures = []
    checks = 0
    for k in range(2, 11_990):
        C = c4(k)
        assert family.integer_root(k*k + 2*k, 4) == C
        bad = []
        for q in family.BASE_PRIMES:
            if q > C:
                break
            checks += 1
            if not family.witness_forced(k, q):
                bad.append(q)
        if bad:
            failures.append((k, C, tuple(bad)))

    assert failures == [(121, 11, (11,))]

    k = 121
    A = k*k
    U = A + 2*k
    forced = {q for q in family.BASE_PRIMES if q <= k and family.witness_forced(k, q)}
    residual = []
    for n in range(A + 1, U + 1):
        x = n
        factors = []
        for q in family.BASE_PRIMES:
            if q*q > x:
                break
            if x % q == 0:
                e = 0
                while x % q == 0:
                    x //= q
                    e += 1
                factors.append((q,e))
        if x > 1:
            factors.append((x,1))
        if len(factors) == 1 and factors[0] == (n,1):
            continue
        support = {q for q,e in factors if q <= k}
        if support and not support.intersection(forced):
            residual.append((n, tuple(factors), tuple(sorted(support))))
    assert residual == []

    return {
        "k_range": [2, 11989],
        "fourth_root_witness_checks": checks,
        "core_failures": failures,
        "exceptional_basin_121_residual_count": 0,
        "conclusion": "every residual in the exact prefix, if any, has Omega=3; k=121 is the only fourth-root-core failure and has no residual",
    }


def last_k_inside_external_region() -> int:
    return isqrt(2*X - 2*1328)


def discontinuity_certificate(K0: int, K1: int) -> dict:
    assert K0 == 11_990
    assert K1 == 894_427_190
    assert RECORD_GAPS[-2] == (352521223451364323, 1328)
    assert RECORD_GAPS[-1][0] > X

    points = {K0, K1}
    for c in range(isqrt(K0), isqrt(K1) + 2):
        k = c*c
        if K0 <= k <= K1:
            points.add(k)
    for start, _ in RECORD_GAPS:
        k = ceil_sqrt(2*start)
        if K0 <= k <= K1:
            points.add(k)

    minimum = None
    for k in sorted(points):
        C = c4(k)
        G = gmax((k*k)//2)
        margin = 2*k - G*C
        row = (margin, k, C, G)
        if minimum is None or row < minimum:
            minimum = row
        assert margin >= 0

    assert K1*K1 + 2*1328 <= 2*X
    assert (K1+1)*(K1+1) + 2*1328 > 2*X

    return {
        "k_range": [K0, K1],
        "discontinuity_points_checked": len(points),
        "minimum_margin": {"margin": minimum[0], "k": minimum[1], "C4": minimum[2], "max_gap": minimum[3]},
        "logic": "between C4 jumps and maximal-gap-record jumps, both C4 and G are constant, so 2k-G*C4 strictly increases",
    }


def main() -> None:
    small = exact_small_prefix()
    K1 = last_k_inside_external_region()
    large = discontinuity_certificate(11_990, K1)
    result = {
        "status": "R005-A CONTINUOUS P2 RESIDUAL-ARITY CERTIFICATE / EXACT PREFIX + EXTERNAL EXHAUSTIVE GAP PREMISE",
        "external_premise": {
            "double_checked_through": X,
            "maximal_gap_first_occurrence_table_used": True,
            "max_actual_prime_difference_below_selected_boundary": 1328,
        },
        "exact_prefix": small,
        "record_gap_transfer": large,
        "continuous_k_range": [2, K1],
        "conclusion": f"For every 2<=k<={K1}, under the stated external gap premise, every square-basin residual composite, if one exists, has Omega exactly 3.",
        "nonclaim": "This does not state that every basin has a residual or that every basin lacks a least witness basis.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
