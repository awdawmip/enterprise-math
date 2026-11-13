"""Exact finite-ring cross-check for the author-side all-precision square-port theorem.

Only integer-labelled units, modular polynomial iterates and original two-factor
observations are used. This is not native Heartbeat X6 computation or proof.
"""
from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timezone
import json
from pathlib import Path


def valuation(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("n must be nonzero")
    a = 0
    while n % p == 0:
        a += 1
        n //= p
    return a


def update(x: int, m: int, h: int, d: int) -> int:
    return (x + h * pow(x, d, m)) % m


def observe(x: int, m: int) -> int:
    return ((x + 1) * (pow(x, -1, m) + 1)) % m


def predicts(p: int, e: int, L: int, d: int) -> dict:
    a = valuation(d - 1, p)
    g = __import__("math").gcd(d - 1, (p - 1) // 2)
    B = (p - 3) * p ** (L - 1) // 2
    if L <= e:
        C = B
    elif p % 4 == 3:
        C = 0
    elif e > a:
        C = g * p ** min(L - 1, e + a)
    elif L <= 2 * e:
        C = g * p ** (L - 1)
    else:
        C = 0
    D = C if L <= 2 * e + a or L <= e else 0
    if L <= e or (p in (3, 5) and L <= e + 1):
        nfixed, ncausal = 1, 1
    elif p % 4 == 1 and e > a and L > 2 * e + a:
        nfixed, ncausal = 3, 2
    else:
        nfixed, ncausal = 2, 2
    return {"a": a, "g": g, "initial_noncritical_pairs": B,
            "C01_noncritical": C, "D_infinity_noncritical": D,
            "N_fixed_full_unit": nfixed, "N_causal_full_unit": ncausal}


def noncritical_census(p: int, e: int, L: int, d: int, lam: int) -> dict:
    m = p ** L
    h = p ** e * lam
    assert e >= 1 and L > e and d >= 2 and d % 2 == 0
    assert lam % p != 0
    pred = predicts(p, e, L, d)
    total_pairs = c01 = c012 = 0
    sample_transient = sample_persistent = None
    extra_checks = 0
    for x in range(1, m):
        if x % p in (0, 1, p - 1):
            continue
        y = pow(x, -1, m)
        if x >= y:
            continue
        total_pairs += 1
        x1 = update(x, m, h, d)
        y1 = update(y, m, h, d)
        z1 = observe(x1, m)
        w1 = observe(y1, m)
        same1 = z1 == w1
        if same1:
            c01 += 1
            x2 = update(x1, m, h, d)
            y2 = update(y1, m, h, d)
            z2 = observe(x2, m)
            w2 = observe(y2, m)
            same2 = z2 == w2
            if same2:
                c012 += 1
                if sample_persistent is None:
                    sample_persistent = {"x": x, "inverse_partner": y,
                                         "O0": observe(x, m), "O1": z1, "O2": z2}
                for _ in range(3, 8):
                    x2 = update(x2, m, h, d)
                    y2 = update(y2, m, h, d)
                    assert observe(x2, m) == observe(y2, m)
                    extra_checks += 1
            elif sample_transient is None:
                sample_transient = {"x": x, "inverse_partner": y,
                                    "O0": observe(x, m), "O1": z1,
                                    "O2_x": z2, "O2_y": w2}
    assert total_pairs == pred["initial_noncritical_pairs"], (p, e, L, d, lam, total_pairs, pred)
    assert c01 == pred["C01_noncritical"], (p, e, L, d, lam, c01, pred)
    assert c012 == pred["D_infinity_noncritical"], (p, e, L, d, lam, c012, pred)
    return {"p": p, "e": e, "L": L, "d": d, "lambda": lam,
            "predicted": pred, "checked_pairs": total_pairs,
            "observed_C01": c01, "observed_C012": c012,
            "sample_transient": sample_transient,
            "sample_persistent": sample_persistent,
            "later_equal_pair_checks": extra_checks, "status": "PASS"}


def group_counts(p: int, e: int, L: int, d: int, lam: int, full_period: bool) -> dict:
    m = p ** L
    h = p ** e * lam
    limit = p ** max(0, L - e) if full_period else 4
    signatures = [defaultdict(int) for _ in range(4)]
    future = defaultdict(int) if full_period else None
    source_count = 0
    for x in range(1, m):
        if x % p == 0:
            continue
        source_count += 1
        cur = x
        seq = []
        for t in range(limit):
            if t < 4:
                seq.append(observe(cur, m))
                signatures[t][tuple(seq)] += 1
            elif full_period:
                seq.append(observe(cur, m))
            cur = update(cur, m, h, d)
        if full_period:
            assert cur == x, (p, e, L, d, x, "cycle not complete")
            future[tuple(seq)] += 1
    sizes = [len(z) for z in signatures]
    if full_period:
        assert sizes[2] == len(future), (p, e, L, d, sizes, len(future))
    n = predicts(p, e, L, d)["N_fixed_full_unit"]
    assert sizes[n - 1] == sizes[2], (p, e, L, d, sizes, n)
    if n > 1:
        assert sizes[n - 2] < sizes[2], (p, e, L, d, sizes, n)
    return {"p": p, "e": e, "L": L, "d": d, "lambda": lam,
            "full_period": full_period, "time_steps": limit,
            "source_count": source_count, "classes_by_prefix_length_1_to_4": sizes,
            "classes_by_full_period": len(future) if full_period else None,
            "prediction": n, "status": "PASS"}


def two_time_witness(p: int, e: int, L: int, d: int, lam: int, deltas: tuple[int, ...]) -> list[dict]:
    m = p ** L
    h = p ** e * lam
    assert predicts(p, e, L, d)["N_fixed_full_unit"] == 3
    witnesses = []
    for delta in deltas:
        found = None
        for x in range(1, m):
            if x % p in (0, 1, p - 1):
                continue
            y = pow(x, -1, m)
            if x >= y:
                continue
            xp, yp = x, y
            for _ in range(delta):
                xp = update(xp, m, h, d)
                yp = update(yp, m, h, d)
            if observe(xp, m) != observe(yp, m):
                continue
            # The previous algebraic theorem says no permanent noncritical pair
            # occurs in the parameter regime being checked.
            x1, y1 = update(x, m, h, d), update(y, m, h, d)
            x2, y2 = update(x1, m, h, d), update(y1, m, h, d)
            assert (observe(x1, m) != observe(y1, m) or
                    observe(x2, m) != observe(y2, m))
            found = {"delta": delta, "source_pair_at_time_0": [x, y],
                     "shared_O0": observe(x, m), "shared_O_delta": observe(xp, m),
                     "O1_equal": observe(x1, m) == observe(y1, m),
                     "O2_equal": observe(x2, m) == observe(y2, m)}
            break
        assert found is not None, (p, e, L, d, lam, delta)
        witnesses.append(found)
    return witnesses


def main() -> None:
    cases = [
        (5, 1, 2, 2, 1), (5, 1, 3, 2, 1), (5, 1, 4, 2, 1),
        (5, 2, 3, 2, 1), (5, 2, 4, 2, 1), (5, 2, 5, 2, 1),
        (5, 2, 6, 2, 1), (5, 2, 7, 2, 1), (5, 2, 7, 2, 2),
        (5, 2, 4, 6, 1), (5, 2, 5, 6, 1), (5, 2, 6, 6, 1),
        (5, 2, 7, 6, 2), (5, 2, 6, 26, 1),
        (5, 3, 7, 26, 1), (5, 3, 8, 26, 1), (5, 3, 9, 26, 1),
        (7, 1, 2, 2, 1), (7, 1, 3, 2, 1), (7, 2, 4, 8, 1),
        (11, 1, 3, 2, 1), (11, 2, 4, 12, 1),
        (13, 1, 3, 2, 1), (13, 1, 4, 2, 1),
        (13, 1, 3, 14, 1), (13, 1, 4, 14, 2),
    ]
    census = [noncritical_census(*arg) for arg in cases]
    global_cases = [
        (3, 1, 2, 2, 1, True), (3, 1, 3, 2, 1, True),
        (5, 1, 2, 2, 1, True), (5, 1, 3, 2, 1, True),
        (5, 1, 4, 2, 1, True), (5, 2, 4, 6, 1, True),
        (5, 2, 5, 6, 1, True), (5, 2, 6, 6, 1, False),
        (5, 3, 8, 26, 1, False), (7, 1, 3, 2, 1, True),
        (7, 2, 4, 8, 1, False), (13, 1, 3, 2, 1, False),
        (13, 1, 3, 14, 1, False),
    ]
    group_results = [group_counts(*arg) for arg in global_cases]
    witness_results = [
        {"params": {"p": 5, "e": 1, "L": 4, "d": 2, "lambda": 1},
         "witnesses": two_time_witness(5, 1, 4, 2, 1, (1, 2, 3, 5, 25))},
        {"params": {"p": 5, "e": 2, "L": 6, "d": 6, "lambda": 1},
         "witnesses": two_time_witness(5, 2, 6, 6, 1, (1, 2, 3, 5, 25))},
    ]
    result = {
        "title": "Odd-prime square-port all-precision noncritical collision/future phase cross-check",
        "date_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "auxiliary Z/p^LZ units; actual integer-labelled sources, update and two-factor observation",
        "classification": "AUTHOR_EXACT_CHECKED_NOT_INDEPENDENT_NOT_NATIVE",
        "all_assertions": "PASS",
        "noncritical_configs": len(census),
        "noncritical_original_pairs_checked": sum(c["checked_pairs"] for c in census),
        "noncritical_C01_pairs": sum(c["observed_C01"] for c in census),
        "noncritical_C012_pairs": sum(c["observed_C012"] for c in census),
        "later_pair_comparisons": sum(c["later_equal_pair_checks"] for c in census),
        "global_configs": len(group_results),
        "global_original_sources_checked": sum(c["source_count"] for c in group_results),
        "two_time_witness_deltas_checked": sum(len(w["witnesses"]) for w in witness_results),
        "noncritical_census": census,
        "global_prefix_and_cycle_census": group_results,
        "exact_two_time_witnesses": witness_results,
    }
    output = Path(__file__).with_name("d25_square_port_all_precision_observer_phase_author_check_20261030.json")
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("all_assertions", "noncritical_configs", "noncritical_original_pairs_checked", "noncritical_C01_pairs", "noncritical_C012_pairs", "later_pair_comparisons", "global_configs", "global_original_sources_checked", "two_time_witness_deltas_checked")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
