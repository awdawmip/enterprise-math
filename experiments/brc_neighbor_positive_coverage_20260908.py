"""Offline positive-family and fixed-cohort audit of a BRC neighbor identity.

All inputs are fixed toy constructions below 2**19. No target-input option,
multiplier search, adaptive dispatch, or search fallback is supplied.
"""
from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
from math import ceil, gcd, isqrt
from pathlib import Path
from random import Random
from statistics import median
from time import perf_counter_ns
import json
import platform
import sys


FIXTURE_BOUND = 2**19


def prime_seed(value):
    # Seed certification only. This never receives an unknown product target.
    return value >= 2 and all(value%d for d in range(2, isqrt(value)+1))


def audit_mod15_positive_families():
    # Fixed constructive audit, not a readout dispatcher for external inputs.
    coefficients = {1: (8, 1, 120, 1), 4: (24, 5, 40, 13),
                    11: (24, 19, 40, 27), 14: (8, 7, 120, 119)}
    assert {r for r in range(15) if r*r % 15 == 1} == set(coefficients)
    rows = []
    for r, (u1, u0, v1, v0) in coefficients.items():
        prime_examples = []
        for k in range(1, 17):
            u, v, c = u1*k+u0, v1*k+v0, 15*k+r
            n = u*v
            t, remainder = divmod(c*c-1, 15)
            assert remainder == 0 and n == 64*t+1 and n < FIXTURE_BOUND
            assert 15*n == (8*c)**2-49 and 1 < u < v
            if r in (4, 11):
                assert v < 2*u
            if prime_seed(u) and prime_seed(v):
                prime_examples.append({"k": k, "N": n, "known_pair": [u, v]})
        rows.append({"c_mod_15": r, "factor_coefficients": [u1, u0, v1, v0],
                     "positive_checks": 16, "factor_ratio_below_two": r in (4, 11),
                     "known_prime_pair_count": len(prime_examples), "prime_examples": prime_examples})
    assert (24*4+5)*(40*4+13) == 17473
    assert (24*5+19)*(40*5+27) == 31553
    return {"rows": rows, "positive_class_checks": 64, "balanced_class_checks": 32,
            "observation_stage": "classification after a certified square hit; not a front-gate predictor"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--enterprise-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    sys.path.insert(0, str(args.enterprise_root/"src"))
    from enterprise_math.brc_neighbor_square_lift_shortcut import neighbor_square_parameters
    from enterprise_math.brc_square_gap_prefilter import ceiling_completion_square_witness
    from enterprise_math.brc_opportunistic_shortcuts import RegimeShortcutLedger, ShortcutContext

    def fixed_a8_observation(n):
        if not 1 < n < FIXTURE_BOUND:
            raise ValueError("outside the fixed toy audit scope")
        low = n & 63
        if low == 1:
            epsilon = 1
        elif low == 63:
            epsilon = -1
        else:
            return None
        t, m, z = neighbor_square_parameters(n, 8, epsilon)
        c = isqrt(z)
        if c*c != z:
            return None
        factor = gcd(n, 8*c-(8-epsilon))
        if not 1 < factor < n:
            return None
        other = n//factor
        if factor*other != n:
            raise AssertionError("product verification failed")
        return epsilon, t, m, z, c, factor, other

    checks = Counter()
    families = []
    for a in (2, 4, 8):
        for epsilon in (1, -1):
            m = 2*a-epsilon
            for k in range(1, 17):
                p, q = a*k+1, a*m*k+epsilon
                n, c = p*q, 1+m*k
                assert 1 < p < q and n < FIXTURE_BOUND
                t, got_m, z = neighbor_square_parameters(n, a, epsilon)
                assert (t, got_m, z) == (m*k*k+2*k, m, c*c)
                assert m*n == (a*c)**2-(a-epsilon)**2
                assert a*c-(a-epsilon) == q
                assert a*c+(a-epsilon) == m*p
                assert ceiling_completion_square_witness(n, m) == (a*c, a-epsilon)
                old = ceiling_completion_square_witness(n, 1) is not None
                known_prime_pair = prime_seed(p) and prime_seed(q)
                j = isqrt(n)
                r = n-j*j
                mode = "Z" if r == 0 else "D" if r <= j else "U"
                if a == 8:
                    observed = fixed_a8_observation(n)
                    assert observed is not None and sorted(observed[-2:]) == [p, q]
                families.append({"a": a, "epsilon": epsilon, "k": k, "N": n,
                    "known_pair": [p, q], "m": m, "t": t, "c": c,
                    "J": j, "R": r, "direction": mode,
                    "known_prime_pair": known_prime_pair, "also_direct_completion": old})
                checks["positive_family_certificates"] += 1
    assert len({row["N"] for row in families if row["known_prime_pair"]}) == sum(row["known_prime_pair"] for row in families)
    family_summary = []
    for a in (2, 4, 8):
        rows = [row for row in families if row["a"] == a]
        prime_rows = [row for row in rows if row["known_prime_pair"]]
        family_summary.append({"a": a, "positive_constructed_count": len(rows),
            "known_prime_pair_count": len(prime_rows),
            "additional_prime_pair_count": sum(not row["also_direct_completion"] for row in prime_rows),
            "prime_direction_counts": dict(Counter(row["direction"] for row in prime_rows)),
            "examples": [row for row in prime_rows if not row["also_direct_completion"]][:3]})

    prime_seeds = [p for p in range(101, 252) if prime_seed(p)]
    cohort = []
    counts = Counter()
    direction_counts = {mode: Counter() for mode in ("D", "U")}
    added = []
    for i, p in enumerate(prime_seeds):
        for q in prime_seeds[i+1:]:
            n = p*q
            j = isqrt(n)
            r = n-j*j
            mode = "D" if r <= j else "U"
            direct = ceiling_completion_square_witness(n, 1) is not None
            trigger = (n & 63) in (1, 63)
            observed = fixed_a8_observation(n)
            hit = observed is not None
            if hit:
                assert sorted(observed[-2:]) == [p, q]
            for counter in (counts, direction_counts[mode]):
                counter["inputs"] += 1
                counter["triggered"] += trigger
                counter["direct_hits"] += direct
                counter["neighbor_hits"] += hit
                counter["additional_hits"] += hit and not direct
                counter["offline_union_hits"] += hit or direct
            if hit and not direct:
                added.append({"N": n, "known_pair": [p, q], "J": j, "R": r,
                              "direction": mode, "observation": list(observed), "verified_S": p+q})
            cohort.append(n)
    checks["prior_known_prime_product_cohort"] = len(cohort)

    # Complete low-bit periods make trigger frequency an exact baseline.
    background = tuple(range(4097, 8192, 2))
    background_triggered = [n for n in background if (n & 63) in (1, 63)]
    background_hits = []
    for n in background:
        observed = fixed_a8_observation(n)
        if observed is not None:
            assert observed[-1]*observed[-2] == n
            background_hits.append({"N": n, "observation": list(observed)})
    assert len(background_triggered) == len(background)//16
    checks["background_observations"] = len(background)
    checks["background_exact_trigger_count"] = len(background_triggered)

    def gate_only_batch(values):
        total = 0
        for n in values:
            low = n & 63
            total += low == 1 or low == 63
        return total

    def full_observation_batch(values):
        total = 0
        for n in values:
            hit = fixed_a8_observation(n)
            if hit is not None:
                total += hit[-2]+hit[-1]
        return total

    positive_a8 = tuple(row["N"] for row in families if row["a"] == 8)
    datasets = {
        "uniform_odd_background": background,
        "prior_known_prime_product_cohort": tuple(cohort),
        "constructed_positive_a8": positive_a8,
    }
    rng = Random(2026090802)
    ledger = RegimeShortcutLedger()
    timing_rows = []
    for name, values in datasets.items():
        hit_count = sum(fixed_a8_observation(n) is not None for n in values)
        trigger_count = gate_only_batch(values)
        expected = full_observation_batch(values)
        repeats = ceil(16384/len(values))
        timings = {"gate_only": [], "complete_observation": []}
        for _ in range(7):
            order = ["gate_only", "complete_observation"]
            rng.shuffle(order)
            for method in order:
                fn = gate_only_batch if method == "gate_only" else full_observation_batch
                expected_value = trigger_count if method == "gate_only" else expected
                start = perf_counter_ns()
                checksum = 0
                for _ in range(repeats):
                    checksum += fn(values)
                elapsed = perf_counter_ns()-start
                assert checksum == repeats*expected_value
                timings[method].append(elapsed/(repeats*len(values)))
        medians = {key: median(items) for key, items in timings.items()}
        # This ledger records costs only. Unknown downstream savings stay zero.
        context = ShortcutContext(n_bits=max(values).bit_length(), max_multiplier=17,
                                  expected_transitions=1, shadow_tag="fixed-a8|"+name)
        for n in values:
            ledger.record(context, "bounded_neighbor_observation", hit=fixed_a8_observation(n) is not None,
                          probe_cost=medians["complete_observation"], saved_cost=0.0)
        timing_rows.append({"population": name, "inputs": len(values), "triggers": trigger_count,
            "verified_hits": hit_count, "hit_rate": hit_count/len(values),
            "ns_per_input_median": medians, "ns_per_input_rounds": timings,
            "batch_repeats": repeats,
            "conditional_break_even_saved_ns_per_hit": medians["complete_observation"]*len(values)/hit_count if hit_count else None})

    module = args.enterprise_root/"src/enterprise_math/brc_neighbor_square_lift_shortcut.py"
    result = {
        "researcher_id": "EM-HME-0CE4FD", "global_snapshot": "618b0d18a0da1cb144e15a90a1e3fc819cae7c54",
        "parent_project_frontier": "a85bf8e00893ea0967601d9364d339769a716388",
        "scope": "fixed toy constructions below 2^19; algebraic certificates and offline hit-set comparison; no target workflow",
        "population_contract": "positive families, a fixed known-prime-product cohort, and complete low-bit periods are reported separately",
        "observer_contract": "one fixed a=8 branch uses N mod 64 to select at most one sign, then one square test and exact product verification",
        "maximum_constructed_N": max(row["N"] for row in families),
        "executed_neighbor_module_sha256": sha256(module.read_bytes()).hexdigest(),
        "checks": dict(checks), "positive_family_summary": family_summary,
        "positive_family_sha256": sha256(json.dumps(families, sort_keys=True).encode()).hexdigest(),
        "mod15_positive_classification": audit_mod15_positive_families(),
        "known_prime_product_counts": dict(counts),
        "known_prime_product_direction_counts": {key: dict(value) for key, value in direction_counts.items()},
        "additional_known_prime_product_witnesses": added,
        "background": {"definition": "all odd N from 4097 through 8191", "inputs": len(background),
                       "triggers": len(background_triggered), "verified_hits": background_hits},
        "timings": timing_rows, "existing_ledger_cost_only": ledger.to_dict(),
        "ledger_contract": {"usage": "COUNTS_AND_PROBE_COSTS_ONLY",
                            "downstream_savings": "UNMEASURED",
                            "saved_cost_zero_is_placeholder": True,
                            "eligible_for_adaptive_reordering": False},
        "cost_contract": "ns/input includes all misses; imports and fixture preparation are excluded; threshold c/h assumes equal downstream saving per hit and is not measured net benefit",
        "runtime": {"python": sys.version.split()[0], "platform": platform.platform()},
        "verdict": "PASS_POSITIVE_NEIGHBOR_FAMILY_AND_INCREMENTAL_FIXED_COHORT_COVERAGE",
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir/"brc_neighbor_positive_coverage_20260908.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("checks", "positive_family_summary", "known_prime_product_counts", "known_prime_product_direction_counts", "additional_known_prime_product_witnesses", "maximum_constructed_N", "verdict")}, indent=2))
    for row in timing_rows:
        print(json.dumps({key: value for key, value in row.items() if key != "ns_per_input_rounds"}))


if __name__ == "__main__":
    main()

