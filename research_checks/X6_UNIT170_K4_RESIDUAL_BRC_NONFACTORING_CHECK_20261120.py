"""Unit170: exact K4 endpoint-sum residual vs signed-six-axis BRC comparator.

Frozen source semantics: K4 edge coordinates are DERIVED; this independent
checker compares the six integer entries with the frozen native Z^6 formula
under an explicitly named axis-label bijection, not a physical identification.
No historical R063 benchmark is imported or executed.
"""
from __future__ import annotations

import itertools
import json
import math
from collections import defaultdict

EDGES = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))


def ensure(predicate: bool, reason: str) -> None:
    if not predicate:
        raise RuntimeError(reason)


def delta(v: tuple[int, ...]) -> tuple[int, ...]:
    ensure(len(v) == 4 and sum(v) == 0, "invalid V0 input")
    return tuple(v[i] + v[j] for i, j in EDGES)


def code(x: tuple[int, ...]) -> tuple[int, int, int]:
    ensure(len(x) == 6 and sum(x) == 0, "invalid E0 input")
    a, b, c, d, e, f = x
    return (a + f, b + e, (a + b + c) % 2)


def exact_shortest(x: tuple[int, ...]) -> tuple[int, int, int]:
    n = sum(abs(t) for t in x)
    den = math.prod(math.factorial(abs(t)) for t in x)
    ensure(math.factorial(n) % den == 0, "multinomial denominator")
    return n, sum(t*t for t in x), math.factorial(n) // den


def run() -> dict:
    vs = [v for v in itertools.product(range(-3, 4), repeat=4) if sum(v) == 0]
    xs = [p + (-sum(p),) for p in itertools.product(range(-1, 2), repeat=5)]
    ensure(len(xs) == 243, "X count")
    gauge_pairs = 0
    for v in vs:
        shift = delta(v)
        ensure(code(shift) == (0, 0, 0), f"lift non-zero code: {v}")
        for x in xs:
            y = tuple(a + b for a, b in zip(x, shift))
            ensure(code(x) == code(y), "code not invariant")
            gauge_pairs += 1

    # Finite search is a scoped witness consistency check, not a novelty claim
    buckets: dict[tuple[int, int, int, int, int], dict[int, tuple[int, ...]]] = defaultdict(dict)
    for v in vs:
        x = delta(v)
        length, q, b = exact_shortest(x)
        buckets[(*code(x), length, q)].setdefault(b, v)
    colliding = {k: vals for k, vals in buckets.items() if len(vals) >= 2}
    ensure(bool(colliding), "expected fixed-type collision absent")

    v1 = (-3, 0, 0, 3)
    v2 = (3, 1, -2, -2)
    x1, x2 = delta(v1), delta(v2)
    ensure(x1 == (-3, -3, 0, 0, 3, 3), "first witness changed")
    ensure(x2 == (4, 1, 1, -1, -1, -4), "second witness changed")
    ensure(code(x1) == code(x2) == (0, 0, 0), "witness code mismatch")
    ell1, q1, b1 = exact_shortest(x1)
    ell2, q2, b2 = exact_shortest(x2)
    ensure((ell1, q1) == (ell2, q2) == (12, 36), "witness scalar mismatch")
    ensure((b1, b2) == (369600, 831600), "witness BRC mismatch")
    ensure(b1 * 9 == b2 * 4, "expected BRC ratio 9/4")

    zero = (0, 0, 0, 0, 0, 0)
    k_entries = []
    for k in range(0, 7):
        x = delta((k, -k, 0, 0))
        result = exact_shortest(x)
        ensure(result[0] == 4*k and result[1] == 4*k*k, "unbounded family arithmetic")
        ensure(code(x) == (0, 0, 0), "unbounded family code")
        k_entries.append({"k": k, "x": list(x), "ell": result[0], "q": result[1], "B": result[2]})
    ensure(exact_shortest(zero) == (0, 0, 1), "origin")

    # Strict check of exact recovery: code plus original zero-total vertex lift.
    lift_checks = 0
    for p in xs:
        m0, m1, parity = code(p)
        rep = (m0, m1, parity - m0 - m1, -parity, 0, 0)
        diff = tuple(a-b for a,b in zip(p,rep))
        a,b,c = diff[:3]
        ensure((a+b+c) % 2 == 0, "canonical lift integral")
        t = (a+b+c)//2
        lift = (t,a-t,b-t,c-t)
        ensure(sum(lift)==0 and tuple(aa+bb for aa,bb in zip(rep,delta(lift)))==p,
               "canonical code plus full lift did not recover x")
        lift_checks += 1

    first = min((k for k in colliding), key=lambda k:(k[3],k[4]))
    return {
        "schema":"X6_UNIT170_EXACT_CHECK_V1",
        "scientific_scope":"K4-derived E0/endpoint_sum(V0) compared via a fixed named bijection to frozen native signed-X6 endpoint readouts; not physical axis identification",
        "frozen_historical_commit":"fd2bcff10ca6e147348b6c1236027fc0d2877df3",
        "frozen_scientific_commit":"59538f585d037d09ef687b28715c4bc1a3f9fe03",
        "sample_vertex_states":len(vs),
        "sample_edge_states":len(xs),
        "source_invariance_pairs":gauge_pairs,
        "complete_recovery_checks":lift_checks,
        "bounded_same_code_ell_q_distinct_B_groups":len(colliding),
        "first_bounded_collision_code_ell_q":list(first),
        "witness":{
            "v1":list(v1),"x1":list(x1),"v2":list(v2),"x2":list(x2),
            "residual_code":[0,0,0],"same_ell":ell1,"same_q":q1,
            "B1":b1,"B2":b2,"B2_over_B1":"9/4",
        },
        "infinite_family_first_seven":k_entries,
        "violations":0,
        "author_status":"AUTHOR_DERIVED_EXACT_FINITE_EXECUTED_UNREVIEWED_NOT_ADMITTED",
        "original_R063_benchmark_rerun":False,
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, sort_keys=True, separators=(",", ":")))
