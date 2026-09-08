"""Fixed 16-bit BRC square-completion fixtures and bounded kernel timings.

No target-input option, multiplier search, or search fallback.
Counts concern all declared integer states, not RSA or semiprime populations.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from math import ceil, isqrt
from pathlib import Path
from random import Random
from statistics import median
from time import perf_counter_ns
import json
import platform
import sys


MAX_J = 255
FIXTURE_CEILING = 65535
BANDS = (("J16_128", 16, 128), ("J129_255", 129, 255))
SAMPLE_SIZE = 2048
ROUNDS = 7
REPEATS = 8


def native_gap_batch(values):
    checksum = 0
    for gap in values:
        b = isqrt(gap)
        if b*b == gap:
            checksum += b
    return checksum


def native_input_batch(values):
    checksum = 0
    for n in values:
        a = isqrt(n) + 1
        gap = a*a - n
        b = isqrt(gap)
        if b*b == gap:
            checksum += b
    return checksum


def verified_native_input_batch(values):
    checksum = 0
    for n in values:
        a = isqrt(n) + 1
        gap = a*a - n
        b = isqrt(gap)
        if b*b == gap:
            left, right = a-b, a+b
            if left > 1 and left*right == n:
                checksum += left+right
    return checksum


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--enterprise-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    sys.path.insert(0, str(args.enterprise_root / "src"))
    from enterprise_math.brc_multiplier_basin import point_cost_state
    from enterprise_math.brc_square_gap_prefilter import (
        filtered_square_root, ceiling_completion_square_witness,
    )
    from enterprise_math.brc_opportunistic_shortcuts import (
        RegimeShortcutLedger, ShortcutContext,
    )

    # This tiny table has a fixed, declared domain. It is not an arbitrary-N API.
    setup_samples = []
    for _ in range(31):
        start = perf_counter_ns()
        square_roots = {b*b: b for b in range(1, isqrt(2*MAX_J) + 1)}
        setup_samples.append(perf_counter_ns() - start)
    setup_ns = median(setup_samples)
    table_bytes = sys.getsizeof(square_roots) + sum(
        sys.getsizeof(k) + sys.getsizeof(v) for k, v in square_roots.items()
    )
    get_root = square_roots.get

    def lookup_gap_batch(values):
        checksum = 0
        for gap in values:
            checksum += get_root(gap, 0)
        return checksum

    def lookup_input_batch(values):
        checksum = 0
        for n in values:
            a = isqrt(n) + 1
            checksum += get_root(a*a-n, 0)
        return checksum

    def verified_lookup_input_batch(values):
        checksum = 0
        for n in values:
            a = isqrt(n) + 1
            b = get_root(a*a-n, 0)
            if b:
                left, right = a-b, a+b
                if left > 1 and left*right == n:
                    checksum += left+right
        return checksum

    def existing_filter_batch(values):
        checksum = 0
        for gap in values:
            checksum += filtered_square_root(gap) or 0
        return checksum

    populations = {(name, mode): [] for name, _, _ in BANDS for mode in ("D", "U")}
    checks = Counter()
    small_counts = []
    for j in range(1, MAX_J + 1):
        expected = {"D": isqrt(2*j)-isqrt(j), "U": isqrt(j)}
        actual = Counter()
        for r in range(1, 2*j + 1):
            n = j*j+r
            assert 1 <= n <= FIXTURE_CEILING
            gap = 2*j+1-r
            mode = "D" if r <= j else "U"
            b = isqrt(gap)
            hit = b*b == gap
            assert get_root(gap, 0) == (b if hit else 0)
            actual[mode] += hit
            checks["bounded_gap_classifications"] += 1
            for name, first, last in BANDS:
                if first <= j <= last:
                    populations[name, mode].append((n, j, r, gap, b if hit else 0))
            if r in {1, j, 2*j}:
                state = point_cost_state(n, 1)
                assert (state.target_root, state.subtraction_cost, state.addition_cost) == (j, r, gap)
                checks["unchanged_point_api_checks"] += 1
        assert actual == expected
        checks["proved_count_formula_basin_checks"] += 1
        if j in (16, 25, 64, 100, 128, 144, 225, 255):
            small_counts.append({"J": j, "states_per_direction": j, "hits": expected})

    # Construct positive witnesses directly; do not search for refuting inputs.
    families = []
    for r in range(1, 25):
        row = []
        for b in range(2, 21):
            if (b*b+r-1) % 2:
                continue
            j = (b*b+r-1)//2
            if j < max(r, 3):
                continue
            n = j*j+r
            assert n <= FIXTURE_CEILING
            assert isqrt(n) == j and 1 <= r <= j
            assert 2*j+1-r == b*b
            assert ceiling_completion_square_witness(n, 1) == (j+1, b)
            assert j+1-b >= 2 and (j+1-b)*(j+1+b) == n
            checks["constructed_D_witnesses"] += 1
            row.append({"N": n, "J": j, "R": r, "completion_root": j+1, "gap_root": b})
        families.append({"R": r, "positive_fixture_count": len(row), "first_three": row[:3]})

    # All prime seeds and all products are fixed toy construction data.
    # Prime generation stops at 251; no unknown input is accepted or searched.
    prime_seeds = [p for p in range(101, 252) if all(p%d for d in range(2, isqrt(p)+1))]
    semiprime_counts = {mode: {"attempts": 0, "hits": 0} for mode in ("D", "U")}
    semiprime_examples = {mode: [] for mode in ("D", "U")}
    for mode in ("D", "U"):
        populations["known_primes101_251", mode] = []
    for i, p in enumerate(prime_seeds):
        for q in prime_seeds[i+1:]:
            n = p*q
            assert n <= FIXTURE_CEILING
            state = point_cost_state(n, 1)
            mode = "D" if state.subtraction_cost <= state.target_root else "U"
            witness = ceiling_completion_square_witness(n, 1)
            populations["known_primes101_251", mode].append((n, state.target_root,
                state.subtraction_cost, state.addition_cost, witness[1] if witness else 0))
            semiprime_counts[mode]["attempts"] += 1
            if witness is not None:
                a, b = witness
                assert (a-b, a+b) == (p, q)
                observed_s = 2*a
                assert observed_s == p+q
                mu = Fraction(p+q, 3)
                measured_h3 = 9*sum((Fraction(v)-mu)**3 for v in (0, p, q))
                assert 2*observed_s**3 - 9*n*observed_s == measured_h3
                checks["positive_conditional_S_and_H3_checks"] += 1
                semiprime_counts[mode]["hits"] += 1
                if len(semiprime_examples[mode]) < 3:
                    semiprime_examples[mode].append({"N": n, "known_pair": [p, q],
                        "J": state.target_root, "R": state.subtraction_cost, "witness": [a, b],
                        "observed_S": observed_s, "observed_9M3": int(measured_h3)})
            checks["fixed_known_prime_product_observations"] += 1

    examples = []
    for n, known_pair in ((493, (17, 29)), (2021, (43, 47))):
        state = point_cost_state(n, 1)
        witness = ceiling_completion_square_witness(n, 1)
        assert known_pair[0]*known_pair[1] == n
        assert witness == ((sum(known_pair))//2, (known_pair[1]-known_pair[0])//2)
        examples.append({"N": n, "known_construction": list(known_pair), "J": state.target_root,
                         "R": state.subtraction_cost, "A": state.addition_cost,
                         "direction": "D" if state.subtraction_cost <= state.target_root else "U",
                         "witness": list(witness)})

    rng = Random(20260908)
    ledger = RegimeShortcutLedger()
    result_rows = []
    for (band, mode), population in populations.items():
        sample = rng.sample(population, min(SAMPLE_SIZE, len(population)))
        ns = [row[0] for row in sample]
        gaps = [row[3] for row in sample]
        expected_checksum = sum(row[4] for row in sample)
        expected_verified_checksum = sum(2*(row[1]+1) for row in sample if row[4])
        repeats = max(REPEATS, ceil(SAMPLE_SIZE*REPEATS/len(sample)))
        methods = {
            "hot_native_isqrt": (native_gap_batch, gaps, expected_checksum),
            "hot_bounded_lookup": (lookup_gap_batch, gaps, expected_checksum),
            "hot_existing_checked_filter": (existing_filter_batch, gaps, expected_checksum),
            "input_native_isqrt": (native_input_batch, ns, expected_checksum),
            "input_bounded_lookup": (lookup_input_batch, ns, expected_checksum),
            "verified_input_native_isqrt": (verified_native_input_batch, ns, expected_verified_checksum),
            "verified_input_bounded_lookup": (verified_lookup_input_batch, ns, expected_verified_checksum),
        }
        for fn, values, expected in methods.values():
            assert fn(values) == expected
        timings = {name: [] for name in methods}
        for round_index in range(ROUNDS):
            names = list(methods)
            rng.shuffle(names)
            for name in names:
                fn, values, expected = methods[name]
                start = perf_counter_ns()
                checksum = 0
                for _ in range(repeats):
                    checksum += fn(values)
                elapsed = perf_counter_ns() - start
                assert checksum == expected*repeats
                timings[name].append(elapsed/(repeats*len(values)))
        medians = {name: median(values) for name, values in timings.items()}
        hot_saving = medians["hot_native_isqrt"]-medians["hot_bounded_lookup"]
        input_saving = medians["input_native_isqrt"]-medians["input_bounded_lookup"]
        verified_saving = medians["verified_input_native_isqrt"]-medians["verified_input_bounded_lookup"]
        context = ShortcutContext(n_bits=max(ns).bit_length(), states_materialized=True,
                                  expected_transitions=len(sample),
                                  shadow_tag=f"bounded-positive-completion|{band}|direction={mode}")
        for row in sample:
            ledger.record(context, "fixed_fixture_gap_lookup", hit=bool(row[4]),
                          probe_cost=medians["hot_bounded_lookup"],
                          saved_cost=medians["hot_native_isqrt"])
        input_context = ShortcutContext(n_bits=max(ns).bit_length(), states_materialized=False,
                                        expected_transitions=len(sample),
                                        shadow_tag=f"bounded-positive-completion|{band}|direction={mode}")
        for row in sample:
            ledger.record(input_context, "fixed_fixture_verified_input_lookup", hit=bool(row[4]),
                          probe_cost=medians["verified_input_bounded_lookup"],
                          saved_cost=medians["verified_input_native_isqrt"])
        result_rows.append({
            "band": band, "direction": mode, "population_size": len(population),
            "population_square_completion_hits": sum(bool(row[4]) for row in population),
            "population_hit_rate": sum(bool(row[4]) for row in population)/len(population),
            "timing_sample_size": len(sample), "timing_sample_hits": sum(bool(row[4]) for row in sample),
            "timing_batch_repeats": repeats,
            "ns_per_item_median": medians,
            "ns_per_item_rounds": timings,
            "hot_speed_ratio_native_over_lookup": medians["hot_native_isqrt"]/medians["hot_bounded_lookup"],
            "input_speed_ratio_native_over_lookup": medians["input_native_isqrt"]/medians["input_bounded_lookup"],
            "verified_input_speed_ratio_native_over_lookup": medians["verified_input_native_isqrt"]/medians["verified_input_bounded_lookup"],
            "verified_input_lookup_faster_rounds": sum(a>b for a,b in zip(timings["verified_input_native_isqrt"],timings["verified_input_bounded_lookup"])),
            "lookup_setup_break_even_items_hot": ceil(setup_ns/hot_saving) if hot_saving > 0 else None,
            "lookup_setup_break_even_items_input": ceil(setup_ns/input_saving) if input_saving > 0 else None,
            "lookup_setup_break_even_items_verified_input": ceil(setup_ns/verified_saving) if verified_saving > 0 else None,
        })

    # One attempt is one exact completion-gap classification; no route is expanded.
    module_names = ("brc_multiplier_basin.py", "brc_square_gap_prefilter.py", "brc_opportunistic_shortcuts.py")
    result = {
        "researcher_id": "EM-HME-0CE4FD", "global_snapshot": "ca9cd753e298ccf9524393faf33047d9b5246d07",
        "prior_verified_frontier": "200d53277c5d033bc229e4758d5fee28da8a5c2e",
        "population_contract": "fixed positive nonsquare integers in complete J bands; not a semiprime or RSA distribution",
        "observer_contract": "direction counts are basin aggregates; timed hot kernel consumes already available exact gap A; input kernel includes N square root",
        "future_operation": "one immediate square-completion observation, followed by stop",
        "conditional_moment_contract": "on a certified immediate completion witness for a known odd-semiprime carrier, S=2a and 9M3=2S^3-9NS; reuses the classical completion channel",
        "maximum_fixture_N": FIXTURE_CEILING, "maximum_gap": 2*MAX_J,
        "checks": dict(checks), "per_basin_examples": small_counts,
        "constructed_positive_families": families, "known_construction_examples": examples,
        "known_prime_product_cohort": {
            "definition": "all distinct pairs from prime seeds in [101,251]; every product below 2^16; no unknown target input",
            "prime_seeds": prime_seeds, "counts": semiprime_counts,
            "positive_examples": semiprime_examples},
        "rows": result_rows,
        "lookup_setup_ns_median": setup_ns, "lookup_entries": len(square_roots),
        "lookup_python_size_bytes_sum_including_keys_values": table_bytes,
        "timing_contract": {"rounds": ROUNDS, "minimum_batch_repeats": REPEATS,
                            "minimum_observations_per_method_round": SAMPLE_SIZE*REPEATS,
                            "setup": "one-time table build timed separately; module import and observation logging excluded for both kernels",
                            "ledger": "costs in ns use batch median allocations; saved_cost is replaced square-root kernel cost, not estimated factorization work",
                            "input_kernel": "includes native isqrt(N) and gap construction; all fixtures are nonsquares",
                            "verified_input_kernel": "also constructs the two witness factors, checks the smaller is nontrivial and checks their product; returns only an aggregate checksum on the fixed fixtures"},
        "ledger_existing_api": ledger.to_dict(),
        "executed_module_sha256": {name: sha256((args.enterprise_root/"src"/"enterprise_math"/name).read_bytes()).hexdigest() for name in module_names},
        "runtime": {"python": sys.version.split()[0], "platform": platform.platform()},
        "verdict": "PASS_POSITIVE_REGIME_COUNTS_WITNESSES_AND_KERNEL_EQUIVALENCE",
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir/"brc_occasional_hit_regimes_20260908.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("checks", "lookup_entries", "lookup_setup_ns_median", "lookup_python_size_bytes_sum_including_keys_values", "known_construction_examples", "known_prime_product_cohort", "verdict")}, indent=2))
    for row in result_rows:
        print(json.dumps({key: row[key] for key in ("band", "direction", "population_size", "population_square_completion_hits", "population_hit_rate", "ns_per_item_median", "hot_speed_ratio_native_over_lookup", "input_speed_ratio_native_over_lookup", "verified_input_speed_ratio_native_over_lookup", "verified_input_lookup_faster_rounds", "lookup_setup_break_even_items_hot", "lookup_setup_break_even_items_input", "lookup_setup_break_even_items_verified_input")}))


if __name__ == "__main__":
    main()

