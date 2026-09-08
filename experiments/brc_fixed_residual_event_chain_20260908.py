"""Fixed small residual-fiber certificate and indexed-batch cost audit.

All fixtures are prescribed by (r, J), with J <= 512 and N < 2**19.
There is no external-integer input, multiplier scan, or target solver.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path
from random import Random
from statistics import median
from time import perf_counter_ns
import json
import platform
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--enterprise-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    sys.path.insert(0, str(args.enterprise_root / "src"))
    from enterprise_math.brc_multiplier_basin import point_cost_state
    from enterprise_math.brc_square_gap_prefilter import ceiling_completion_square_witness

    source_expectations = {
        "brc_multiplier_basin.py": "6fe4551f053e6427c67aef1e70e837615d75aa5a52b7477bf6c9cb96fb9a7d3a",
        "brc_square_gap_prefilter.py": "f8e178771a25221eaab16002b9ffacd188dc5f39be4948ec2b40ee3e22c9f716",
    }
    sources = {}
    for name, expected in source_expectations.items():
        digest = sha256((args.enterprise_root / "src" / "enterprise_math" / name).read_bytes()).hexdigest()
        assert digest == expected, (name, digest)
        sources[name] = digest

    # Positive odd-integer lanes. The mathematical note covers all r >= 1;
    # this fixed experiment selects r == 1 or 2 (mod 4), without target inputs.
    fibers = tuple((r, max(3, (r + 1) // 2), 512)
                   for r in range(1, 65) if r % 4 in (1, 2))

    def append_verified(rows, r, j, b, u, v):
        n = j*j + r
        if not (n < 2**19 and n % 2 == 1 and 1 < u < v and u*v == n
                and u+v == 2*(j+1) and v-u == 2*b):
            raise AssertionError((r, j, b, u, v))
        rows.append((r, j, b, n, u, v))

    def direct_indexed_batch(batch=fibers):
        rows = []
        for r, lower, upper in batch:
            # J parity is part of this prescribed odd-integer population.
            start = lower + ((lower - (1-r)) % 2)
            for j in range(start, upper + 1, 2):
                gap = 2*j + 1 - r
                b = isqrt(gap)
                if b*b == gap:
                    append_verified(rows, r, j, b, j+1-b, j+1+b)
        return rows

    def event_indexed_batch(batch=fibers):
        rows = []
        for r, lower, upper in batch:
            threshold = 2*lower + 1 - r
            b = isqrt(threshold)
            b += b*b < threshold
            b += (b - (1-r)) % 2
            j = (b*b + r - 1) // 2
            u, v = j+1-b, j+1+b
            while j <= upper:
                append_verified(rows, r, j, b, u, v)
                u, v = v, v+2*b+4
                j += 2*b + 2
                b += 2
        return rows

    direct = direct_indexed_batch()
    events = event_indexed_batch()
    assert direct == events

    def count_formula(r, lower, upper):
        if upper < lower:
            return 0
        threshold = 2*lower + 1 - r
        first_b = isqrt(threshold)
        first_b += first_b*first_b < threshold
        first_b += (first_b - (1-r)) % 2
        last_b = isqrt(2*upper + 1 - r)
        last_b -= (last_b - (1-r)) % 2
        return max(0, (last_b - first_b) // 2 + 1)

    def prime_seed(value):
        # Certification of the already constructed small factors only.
        return value >= 2 and all(value % d for d in range(2, isqrt(value) + 1))

    checks = Counter()
    directions = {key: Counter() for key in ("D", "U")}
    per_fiber = []
    certified_prime_events = []
    clean_shared_prime_pairs = []
    for r, lower, upper in fibers:
        expected_population = Counter()
        for j in range(lower, upper + 1):
            n = j*j + r
            if n % 2 == 0:
                continue
            state = point_cost_state(n, 1)
            assert (state.target_root, state.subtraction_cost, state.addition_cost) == (j, r, 2*j+1-r)
            mode = "D" if r <= j else "U"
            expected_population[mode] += 1
            directions[mode]["input_states"] += 1
            checks["unchanged_point_states"] += 1

        rows = [row for row in events if row[0] == r]
        row_counts = Counter()
        for _, j, b, n, u, v in rows:
            assert ceiling_completion_square_witness(n, 1) == (j+1, b)
            mode = "D" if r <= j else "U"
            assert (b*b > r) == (mode == "D")
            row_counts[mode] += 1
            directions[mode]["verified_events"] += 1
            checks["unchanged_completion_witnesses"] += 1
            if prime_seed(u) and prime_seed(v):
                s = u+v
                mu = Fraction(s, 3)
                m3 = sum((Fraction(x)-mu)**3 for x in (0, u, v))
                assert s == 2*(j+1) and 9*m3 == 2*s**3 - 9*n*s
                certified_prime_events.append({"r": r, "J": j, "b": b, "N": n, "pair": [u, v], "direction": mode})
                directions[mode]["known_prime_pair_events"] += 1
                checks["exact_prime_pair_moments"] += 1

        assert len(rows) == count_formula(r, lower, upper)
        assert row_counts["D"] == count_formula(r, max(lower, r), upper)
        assert row_counts["U"] == count_formula(r, lower, min(upper, r-1))
        checks["closed_form_direction_counts"] += 3
        clean = 0
        for left, right in zip(rows, rows[1:]):
            _, j, b, n, u, v = left
            _, next_j, next_b, next_n, next_u, w = right
            assert next_j-j == 2*b+2 and next_b == b+2 and next_u == v
            correction = gcd(r+4, b+1)
            while correction % 2 == 0:
                correction //= 2
            assert gcd(n, next_n) == v*correction
            checks["adjacent_factor_and_gcd_identities"] += 1
            if correction == 1:
                clean += 1
                checks["clean_shared_factor_pairs"] += 1
                if all(prime_seed(x) for x in (u, v, w)):
                    clean_shared_prime_pairs.append({"r": r, "left_N": n, "right_N": next_n, "factor_chain": [u, v, w]})
        per_fiber.append({"r": r, "J_min": lower, "J_max": upper,
                          "odd_input_states": dict(expected_population), "events": dict(row_counts),
                          "first_event": list(rows[0]), "last_event": list(rows[-1]),
                          "adjacent_pairs": max(0, len(rows)-1), "clean_shared_pairs": clean})

    checks["event_set_equality"] = len(events)
    checks["fixed_positive_residual_fibers"] = len(fibers)
    input_count = sum(c["input_states"] for c in directions.values())
    sample_chain = next(row for row in clean_shared_prime_pairs if row["left_N"] == 299)
    assert sample_chain == {"r": 10, "left_N": 299, "right_N": 851, "factor_chain": [13, 23, 37]}

    # Both measured paths receive the same already indexed fiber description,
    # return identical complete event lists and verify every output product.
    # Seed calculations are inside the measured batch, with no stored hit table.
    methods = {"direct_indexed": direct_indexed_batch, "event_indexed": event_indexed_batch}
    views = {"combined": fibers,
             "D": tuple((r, max(lower, r), upper) for r, lower, upper in fibers),
             "U": tuple((r, lower, min(upper, r-1)) for r, lower, upper in fibers if lower < r)}
    timing_by_view = {}
    rng = Random(6090801)
    repetitions = 16
    for view_name, batch in views.items():
        expected = [row for row in events if view_name == "combined" or ("D" if row[0] <= row[1] else "U") == view_name]
        assert direct_indexed_batch(batch) == event_indexed_batch(batch) == expected
        rounds = []
        for round_index in range(7):
            order = list(methods)
            rng.shuffle(order)
            values = {}
            for name in order:
                fn = methods[name]
                started = perf_counter_ns()
                for _ in range(repetitions):
                    result = fn(batch)
                elapsed = perf_counter_ns() - started
                assert result == expected
                values[name] = elapsed / repetitions
            rounds.append({"round": round_index+1, "order": order, "ns_per_complete_batch": values})
        medians = {name: median(row["ns_per_complete_batch"][name] for row in rounds) for name in methods}
        timing_by_view[view_name] = {"repetitions_per_round": repetitions, "rounds": rounds,
            "median_ns_per_batch": medians,
            "ratio_of_batch_medians": medians["direct_indexed"] / medians["event_indexed"],
            "event_faster_rounds": sum(row["ns_per_complete_batch"]["event_indexed"] < row["ns_per_complete_batch"]["direct_indexed"] for row in rounds),
            "fiber_seed_count": len(batch), "output_event_count": len(expected)}

    certificate = {
        "status": "FIXED_INDEXED_FIBER_MATH_AND_COST_CERTIFICATE",
        "researcher": "EM-HME-0CE4FD / TASK_RESEARCH",
        "global_snapshot": "e76fdc883f9f4a3a93c1284340e38c55aeba0a6a",
        "parent_project_frontier": "3b6d58809e1ec8af7f6fff25800dfe07315a4541",
        "source_sha256": sources,
        "python": sys.version, "platform": platform.platform(),
        "observer_contract": {
            "supplied": "prescribed residual r, COMPLETE ordered root interval, odd-input population",
            "r_only_is_not_the_runtime_carrier": True,
            "output": "complete immediate-completion event list with verified proper products",
            "directions": "D if r<=J; U if r>J; canonical collapse remains downward",
            "fixture_domain": "r in 1..64 with r%4 in (1,2); max(3,ceil(r/2))<=J<=512; odd N=J^2+r",
            "external_targets": False,
        },
        "cost_contract": {
            "timed": "all batch processing, event seeds, output allocation and exact product verification",
            "not_timed": "imports, data acquisition or conversion of an arbitrary input list into indexed fibers",
            "index_acquisition_cost": "UNMEASURED; not claimed free for external input lists",
            "arbitrary_sparse_input_list_membership": "NOT_IMPLEMENTED; full implicit fiber intervals are required",
            "materialize_nonhit_integers": False,
            "endpoint": "identical full event lists, not merely equal hit counts",
            "target_factorization_speedup": "UNMEASURED",
            "eligible_for_production_dispatch_or_adaptive_ranking": False,
        },
        "checks": dict(checks), "directions": {k: dict(v) for k, v in directions.items()},
        "fibers": per_fiber, "known_prime_pair_events": certified_prime_events,
        "clean_adjacent_known_prime_pairs": clean_shared_prime_pairs,
        "sample_shared_prime_chain": sample_chain,
        "operation_counts_per_batch": {"indexed_odd_states": input_count,
            "direct_square_root_calls": input_count, "event_seed_square_root_calls": len(fibers),
            "verified_output_products_each_method": len(events)},
        "timing_by_view": timing_by_view,
        "maximum_fixture_N": max(j*j+r for r, lower, upper in fibers for j in range(lower, upper+1) if (j*j+r)%2),
        "goal_status": "ACTIVE; real RSA task effectiveness is not established",
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "brc_fixed_residual_event_chain_20260908.json"
    output.write_text(json.dumps(certificate, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"output": str(output), "checks": certificate["checks"],
        "directions": certificate["directions"], "operations": certificate["operation_counts_per_batch"],
        "timings": {view: {key: value for key, value in data.items() if key != "rounds"} for view, data in timing_by_view.items()},
        "adjacent_known_prime_pairs": len(clean_shared_prime_pairs), "sample": sample_chain}, ensure_ascii=False))


if __name__ == "__main__":
    main()
