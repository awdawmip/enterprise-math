#!/usr/bin/env python3
"""R284EB: exhaustive exact decision-tree DP for R284EA's frozen auxiliary Boolean classifier.
Standard library only.  A query reveals one of nine already defined source bits.
The 512 bit vectors are equiprobable for the expected-cost claim.
"""
from functools import lru_cache
from itertools import product
from hashlib import sha256
from pathlib import Path
import json

BITS = ("Y", "Z", "U", "G", "H", "R", "B0", "B1", "B2")
W = (13, 6, 28, 25, 11, 12, 26, 17, 6)
THRESHOLD, FULL = 77, (1 << 9) - 1


def bounds(zero, one):
    free = FULL ^ (zero | one)
    low = sum(W[j] for j in range(9) if one & (1 << j))
    high = low + sum(W[j] for j in range(9) if free & (1 << j))
    return free, low, high


@lru_cache(None)
def average_optimum(zero, one):
    """(sum of reads over all completions, maximum depth, first queried bit)."""
    free, lo, hi = bounds(zero, one)
    if lo >= THRESHOLD or hi < THRESHOLD:
        return 0, 0, -1
    choices = []
    for j in range(9):
        if free & (1 << j):
            a = average_optimum(zero | (1 << j), one)
            b = average_optimum(zero, one | (1 << j))
            choices.append((2 ** free.bit_count() + a[0] + b[0],
                            1 + max(a[1], b[1]), j))
    return min(choices)


@lru_cache(None)
def worst_optimum(zero, one):
    """(minimax depth, then minimum sum of reads, first queried bit)."""
    free, lo, hi = bounds(zero, one)
    if lo >= THRESHOLD or hi < THRESHOLD:
        return 0, 0, -1
    options = []
    for j in range(9):
        if free & (1 << j):
            a = worst_optimum(zero | (1 << j), one)
            b = worst_optimum(zero, one | (1 << j))
            options.append((1 + max(a[0], b[0]),
                            2 ** free.bit_count() + a[1] + b[1], j))
    return min(options)


def evaluate(bits, chooser):
    zero = one = depth = 0
    while True:
        free, lo, hi = bounds(zero, one)
        if lo >= THRESHOLD or hi < THRESHOLD:
            outcome = lo >= THRESHOLD
            break
        j = chooser(zero, one, free)
        assert free & (1 << j)
        if bits[j]:
            one |= 1 << j
        else:
            zero |= 1 << j
        depth += 1
    assert outcome == (sum(w * b for w, b in zip(W, bits)) >= THRESHOLD)
    return depth


def main():
    all_states = [(zero, one) for zero in range(512) for one in range(512)
                  if (zero & one) == 0]
    assert len(all_states) == 3 ** 9
    states_data = []
    for zero, one in all_states:
        optimal = average_optimum(zero, one)
        worst = worst_optimum(zero, one)
        states_data.append((zero, one, *optimal, *worst))
    table_bytes = json.dumps(states_data, separators=(",", ":")).encode()
    root, minimax = average_optimum(0, 0), worst_optimum(0, 0)
    assert root == (2734, 9, 2)
    assert minimax == (9, 2734, 2)
    order = tuple(sorted(range(9), key=lambda j: (-W[j], j)))
    assert order == (2, 6, 3, 7, 0, 5, 4, 1, 8)
    hist_adaptive = dict.fromkeys(range(10), 0)
    hist_fixed = dict.fromkeys(range(10), 0)
    labels = 0
    for bits in product((0, 1), repeat=9):
        labels += sum(w*b for w,b in zip(W,bits)) >= THRESHOLD
        da = evaluate(bits, lambda z, o, f: average_optimum(z, o)[2])
        df = evaluate(bits, lambda z, o, f: next(j for j in order if f & (1<<j)))
        hist_adaptive[da] += 1
        hist_fixed[df] += 1
    assert labels == 223
    assert sum(k*v for k,v in hist_adaptive.items()) == root[0]
    assert sum(k*v for k,v in hist_fixed.items()) == root[0]
    assert max(k for k,v in hist_adaptive.items() if v) == 9
    assert max(k for k,v in hist_fixed.items() if v) == 9
    # A concrete full-16-bit exception-guard circuit: six core bits first,
    # then the optimal nine-bit threshold only when all six core bits equal 1.
    # B3 is retained in the original input, and never queried by this guard.
    all_guard_queries = 0
    full_hist = {}
    for core in product((0, 1), repeat=6):
        core_queries = next((j + 1 for j, v in enumerate(core) if v == 0), 6)
        active = all(core)
        for bits in product((0, 1), repeat=9):
            reads = core_queries + (evaluate(bits, lambda z, o, f:
                next(j for j in order if f & (1 << j))) if active else 0)
            all_guard_queries += 2 * reads  # both values of upper bit B3
            full_hist[reads] = full_hist.get(reads, 0) + 2
    assert sum(full_hist.values()) == 65536
    assert all_guard_queries == 134492
    assert full_hist[max(full_hist)] == 84 and max(full_hist) == 15
    result = {
        "schema": "R284EB_NINE_BIT_ADAPTIVE_QUERY_OPTIMALITY_V1",
        "scientific_input": "R284EA nine-bit score on frozen R284CO Port source",
        "source_ref": "awdawmip/enterprise-math@bc66d7bdd3210f426dc38497e6c0368ab11ab292:research_notes/portable_direct/R284EA_NINE_BIT_EXCEPTION_THRESHOLD_AND_SHARP_ADDITIVE_WEIGHT_20261122.md",
        "frozen_R284CO_commit": "acba2d8667903434aaa2a10720f43637fcc2421b",
        "bit_order": BITS,
        "weights": W,
        "threshold": THRESHOLD,
        "cost_model": "One unit per queried original bit, exact/noiseless query; independent equiprobable 512 input vectors; deterministic adaptive decision tree",
        "subcubes_checked": len(all_states),
        "optimal_total_queries_over_512": root[0],
        "optimal_expected_queries": {"numerator": root[0] // 2, "denominator": 256},
        "optimal_max_depth_secondary": root[1],
        "minimax_depth": minimax[0],
        "minimax_total_queries_secondary": minimax[1],
        "witness_fixed_order_zero_indexed": order,
        "witness_fixed_order_names": tuple(BITS[j] for j in order),
        "witness_fixed_order_histogram": {str(k):v for k,v in hist_fixed.items() if v},
        "adaptive_dp_histogram": {str(k):v for k,v in hist_adaptive.items() if v},
        "full_six_core_guard_total_queries_over_65536": all_guard_queries,
        "full_six_core_guard_mean": {"numerator": 33623, "denominator": 16384},
        "full_six_core_guard_worst_depth": max(full_hist),
        "full_six_core_guard_histogram": {str(k):v for k,v in sorted(full_hist.items())},
        "full_guard_scope": "Concrete short-circuit strategy; NOT proved globally optimal among interleavings of 15 original bits",
        "true_outputs": labels,
        "false_outputs": 512-labels,
        "dp_table_sha256": sha256(table_bytes).hexdigest(),
        "coverage": "Full 3^9 ternary partial-assignment DP, all 2^9 Boolean inputs and the 2^16-state guard input population",
        "research_status": "AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED",
    }
    return result


if __name__ == "__main__":
    result = main()
    output = Path(__file__).with_name("R284EB_exact_optimal_nine_bit_readout_certificate.json")
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
