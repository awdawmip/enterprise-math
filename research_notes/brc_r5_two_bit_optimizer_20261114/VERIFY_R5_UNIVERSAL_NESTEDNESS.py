#!/usr/bin/env python3
"""Exact pairwise nested-optimum certificate for all R5 gap closure masks.

Only the original 954-event pattern requires a full nested-gain DP;
the previous all-mask cost invariance plus monotone family inclusion
transfers its nested pairs to every 28-bit closure mask.
"""
import json
import random
import sys
from pathlib import Path
from itertools import combinations

SOURCE = Path(__file__).resolve().parents[1] / 'brc_r5_exact_cost_spectrum_20261114'
sys.path.insert(0, str(SOURCE))
from VERIFY_R5_COST_SPECTRA import frozen, closed_points
from VERIFY_R5_OPTIMAL_WITNESSES import optimum_counts_spectrum

INF = 10**12
PIN = '435e77af0d180eac32bd1f9c4c464bc4010b7551'


def nested_gain_spectrum(x):
    """K -> (optimal cost, largest 1-center insertion gain among K-optima)."""
    n = len(x)
    maxgap = max(x[j+1] - x[j] for j in range(n-1))

    def edge(i, j):
        cost = 0
        for t in range(i+1, j):
            value = min(x[t] - x[i], x[j] - x[t])
            if value > 2:
                return None
            cost += value
        return cost

    incoming = [[] for _ in range(n)]
    for j in range(n):
        for i in range(j-1, -1, -1):
            if x[j] - x[i] > 4 + maxgap:
                break
            old = edge(i, j)
            if old is None:
                continue
            gain = max((old - edge(i, h) - edge(h, j)
                        for h in range(i+1, j)), default=0)
            incoming[j].append((i, old, gain))

    pre = [INF]*n
    pre_gain = [0]*n
    suf = [INF]*n
    suf_gain = [0]*n
    for j in range(n):
        if x[j] - x[0] <= 2:
            pre[j] = sum(x[j] - x[t] for t in range(j))
            pre_gain[j] = max((pre[j] - (
                sum(x[h]-x[t] for t in range(h)) +
                sum(min(x[t]-x[h], x[j]-x[t]) for t in range(h+1, j)))
                for h in range(j)), default=0)
        if x[-1] - x[j] <= 2:
            suf[j] = sum(x[t] - x[j] for t in range(j+1, n))
            suf_gain[j] = max((suf[j] - (
                sum(min(x[t]-x[j], x[h]-x[t]) for t in range(j+1, h)) +
                sum(x[t]-x[h] for t in range(h+1, n)))
                for h in range(j+1, n)), default=0)

    F, G, output = pre[:], pre_gain[:], {}
    for k in range(1, n+1):
        if k > 1:
            next_cost = [INF]*n
            next_gain = [-1]*n
            for j in range(n):
                for i, cost, gain in incoming[j]:
                    candidate = F[i] + cost
                    if candidate < next_cost[j]:
                        next_cost[j] = candidate
                        next_gain[j] = max(G[i], gain)
                    elif candidate == next_cost[j]:
                        next_gain[j] = max(next_gain[j], G[i], gain)
            F, G = next_cost, next_gain
        best = INF
        best_gain = -1
        for j in range(n):
            value = F[j] + suf[j]
            if value < best:
                best, best_gain = value, max(G[j], suf_gain[j])
            elif value == best:
                best_gain = max(best_gain, G[j], suf_gain[j])
        if best < INF:
            output[k] = (best, best_gain)
    return output


def check_small_cases():
    rng = random.Random(115)
    for n in range(3, 9):
        for _ in range(40):
            y = [0]
            for j in range(n-1):
                y.append(y[-1] + rng.randint(1, 4))
            found = nested_gain_spectrum(y)
            for k in range(1, n):
                candidates = []
                for S in combinations(range(n), k):
                    distances = [min(abs(y[t]-y[j]) for j in S) for t in range(n)]
                    if max(distances) <= 2:
                        candidates.append((sum(distances), S))
                if not candidates:
                    assert k not in found
                    continue
                best = min(cost for cost, _ in candidates)
                gain = max((best - sum(min(abs(y[t]-y[j]) for j in (*S, h))
                            for t in range(n))
                            for cost, S in candidates if cost == best
                            for h in range(n) if h not in S), default=0)
                assert found[k] == (best, gain), (y, k, found[k], (best,gain))
    return 240


def verify():
    small = check_small_cases()
    x, cuts = frozen()
    base = nested_gain_spectrum(x)
    baseline_costs = optimum_counts_spectrum(x)
    assert all(base[k][0] == baseline_costs[k][0] for k in baseline_costs)
    assert set(base) == set(range(213, 955))
    gain_bands = [(292, 314, 3), (315, 350, 2), (351, 953, 1)]
    for first, last, expected in gain_bands:
        for k in range(first, last+1):
            cost, gain = base[k]
            assert gain == cost - base[k+1][0] == expected, (k,cost,gain)

    # Independent consistency checks on all four effective two-bit cases.
    for mask in (0, 1<<15, 1<<17, (1<<15)|(1<<17)):
        y = closed_points(x, cuts, mask)
        states = base if mask == 0 else nested_gain_spectrum(y)
        assert all(states[k][1] == states[k][0]-states[k+1][0]
                   for k in range(292, 954))
    return dict(status='PASS_R5_ALL_CLOSURE_PAIRWISE_NESTEDNESS',
        scientific_pin=PIN, observer='954 indexed events, radius 2',
        checked_baseline_transitions=662,
        exact_gain_bands=[dict(K_from=a, K_through=b, optimal_insertion_gain=g)
                          for a,b,g in gain_bands],
        crosschecked_four_effective_cases=4,
        independent_small_exact_subset_instances=small,
        all_pattern_theorem='For every B subset of 28 cuts and every 292<=K<=953, '
                            'some S in Opt_B(K) is a subset of some T in Opt_B(K+1)',
        reconfiguration_minimum_deletions=0, minimum_symmetric_difference=1,
        single_chain_across_all_K_claimed=False,
        mathematical_review='NOT_REVIEWED')


if __name__ == '__main__':
    print(json.dumps(verify(), ensure_ascii=False, indent=2))
