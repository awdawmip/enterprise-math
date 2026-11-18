#!/usr/bin/env python3
"""Exact R5 256-state repetition caps, 18 noise signatures and capped batches.
Run: python3 VERIFY_R5_REPEAT_CAP.py EXACT_R5_ALL_101_BUDGETS.json > RESULTS_R5_REPEAT_CAP.json
Standard-library Python; all integer operations; frozen 101-budget input.
"""
import hashlib
import itertools
import json
import sys
from pathlib import Path

PIN = "435e77af0d180eac32bd1f9c4c464bc4010b7551"
INPUT_SHA = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
L = 25845652773852463277015040000
C = 53550705027838197293383680000
U = 58182461585441404127941754880
KS = tuple(range(214, 315))
F8_NEED = 17

def separation_sets(counts, tau):
    patterns = {}
    for a in range(256):
        for b in range(a + 1, 256):
            m = sum(1 << i for i, vals in enumerate(counts)
                    if abs(vals[a] - vals[b]) > tau)
            patterns.setdefault(m, (a, b))
    return patterns

def minimal_masks(patterns):
    remaining = sorted(patterns, key=lambda x: (x.bit_count(), x))
    minima = []
    for m in remaining:
        if not any((p & m) == p for p in minima):
            minima.append(m)
    return frozenset(minima)

def mask(group):
    return sum(1 << (k - 214) for k in group)

def solve_low(q, groups):
    best = None
    optimum = None
    ties = 0
    inspected = 0
    ks = tuple(range(214, 222))
    for counts in itertools.product(range(q + 1), repeat=8):
        inspected += 1
        if any(sum(counts[k - 214] for k in group) < F8_NEED for group in groups):
            continue
        cost = sum(k * c for k, c in zip(ks, counts))
        if best is None or cost < best:
            best, optimum, ties = cost, {k: c for k,c in zip(ks, counts) if c}, 1
        elif cost == best:
            ties += 1
    assert best is not None and ties == 1
    return {"cost": best, "schedule": optimum, "optimal_count": ties, "vectors_checked": inspected}

def cheapest(group, cap):
    left = F8_NEED
    sched = {}
    for k in group:
        n = min(cap, left)
        if n:
            sched[k] = n
            left -= n
    assert left == 0
    return sched

def pair_coverage(counts, tau, sched):
    worst = 100000
    witness = None
    for a in range(256):
        for b in range(a + 1, 256):
            d = sum(n for k,n in sched.items() if abs(counts[k-214][a] - counts[k-214][b]) > tau)
            if d < worst:
                worst, witness = d, [a,b]
    assert worst >= F8_NEED
    return {"min_separations": worst, "witness": witness}

def main():
    raw = Path(sys.argv[1]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == INPUT_SHA
    obj = json.loads(raw)
    assert obj["budget_range"] == [214, 314]
    counts = [tuple(map(int, obj["counts_and_cohorts"][str(k)]["counts"])) for k in KS]
    assert all(len(x) == 256 for x in counts)
    gaps = set()
    for vs in counts:
        unique = sorted(set(vs))
        for a in range(len(unique)):
            for b in range(a + 1, len(unique)):
                gap = unique[b] - unique[a]
                if L < gap < U:
                    gaps.add(gap)
    chamber_starts = [L] + sorted(gaps)
    assert len(chamber_starts) == 18 and C in chamber_starts
    early = [list(range(214,220)),
             [214,216,217,218,219,220,221],
             [215,216,217,218,219,220,221],
             list(range(223,291)),
             list(range(296,313))]
    late = [list(range(214,219))] + early[1:]
    chamber_results = []
    for i,tau in enumerate(chamber_starts):
        pat = separation_sets(counts,tau)
        actual = minimal_masks(pat)
        expected = frozenset(map(mask, early if tau < C else late))
        assert actual == expected, (tau, actual, expected)
        d = min(m.bit_count() for m in pat)
        assert d == (6 if tau < C else 5)
        chamber_results.append({
          "tau_start":str(tau),
          "tau_end_exclusive":str(chamber_starts[i+1] if i+1 < len(chamber_starts) else U),
          "distinct_separation_sets":len(pat), "minimal_sets":len(actual),
          "minimum_distinct_separating_budgets":d,
          "minimum_uniform_repetition_cap_for_f8":(F8_NEED+d-1)//d
        })
    batch = {}
    for phase, tau, last, cap, groups in [
        ("early", L, C-1, 3, early),
        ("late", C, U-1, 4, late)
    ]:
        small = solve_low(cap, groups[:3])
        middle = cheapest(groups[3],cap)
        high = cheapest(groups[4],cap)
        sched = {**small["schedule"], **middle, **high}
        value = sum(k*n for k,n in sched.items())
        batch[phase] = {
          "cap":cap, "cost":value, "queries":sum(sched.values()),
          "schedule":{str(k):n for k,n in sorted(sched.items())},
          "small_group_certificate":small,
          "middle_cost":sum(k*n for k,n in middle.items()),
          "high_cost":sum(k*n for k,n in high.items()),
          "left_coverage":pair_coverage(counts,tau,sched),
          "right_coverage":pair_coverage(counts,last,sched)
        }
        assert batch[phase]["queries"] == 54
    assert batch["early"]["cost"] == 13240
    assert batch["late"]["cost"] == 13208
    print(json.dumps({
      "status":"PASS_R5_256_REPEAT_CAP_BATCH_18_CHAMBERS_EXACT",
      "science_pin":PIN, "input_sha256":INPUT_SHA,
      "state_count":256, "budgets":101, "pairs":32640,
      "noise_domain":[str(L),str(U)], "critical_tau":str(C),
      "internal_thresholds":[str(t) for t in chamber_starts[1:]],
      "five_minimal_separating_sets":{"early":early,"late":late},
      "chambers":chamber_results,
      "exact_capped_fixed_batch_f8":batch,
      "adaptive_feasibility":"all pairs a<b require sum_{k: |N_a(k)-N_b(k)|>tau} q_k >= 2*f+1",
      "uniform_repetition_capacity":"floor((q*d_min-1)/2)"
    },ensure_ascii=False,indent=2,sort_keys=True))
    print("PASS_R5_256_REPEAT_CAP_BATCH_18_CHAMBERS_EXACT",file=sys.stderr)

if __name__=="__main__":
    main()
