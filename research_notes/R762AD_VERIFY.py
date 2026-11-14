#!/usr/bin/env python3
"""R762AD: exact cap-two star BRC proof cross-check, Python stdlib only."""
from functools import lru_cache
from itertools import permutations
from math import factorial, prod
from collections import defaultdict
from pathlib import Path
import json


def cycles(pi):
    seen = set(); lengths = []
    for i in range(len(pi)):
        if i in seen: continue
        j = i; length = 0
        while j not in seen:
            seen.add(j); length += 1; j = pi[j]
        if length > 1: lengths.append(length)
    return tuple(sorted(lengths))


def dp_count(pi):
    """In/Out token subsets; for moved tokens, output its target once vacated."""
    m = len(pi); all_bits = (1 << m) - 1
    @lru_cache(None)
    def ways(in_mask, out_mask):
        if out_mask == all_bits: return 1
        total = 0
        if (in_mask & ~out_mask).bit_count() < 2:
            for i in range(m):
                if not (in_mask >> i) & 1:
                    total += ways(in_mask | (1 << i), out_mask)
        for i in range(m):
            if ((in_mask >> i) & 1 and not ((out_mask >> i) & 1)
                    and ((in_mask >> pi[i]) & 1)):
                total += ways(in_mask, out_mask | (1 << i))
        return total
    return ways(0, 0)


def bfs_count(pi):
    """Independent token-position BFS counting distinct shortest microstep sequences."""
    m = len(pi)
    start = tuple(range(m)) + (-1, -1)  # ports store token ID, unordered hub slots canonicalized
    target = tuple(pi.index(j) for j in range(m)) + (-1, -1)
    layers = {start: 1}
    for depth in range(2*m + 1):
        if depth == 2*m:
            return layers.get(target, 0)
        nxt = defaultdict(int)
        for state, weight in layers.items():
            ports, hub = state[:m], state[m:]
            if -1 in hub:
                for p, tok in enumerate(ports):
                    if tok < 0: continue
                    new_ports = list(ports); new_ports[p] = -1
                    new_hub = list(hub); new_hub[new_hub.index(-1)] = tok
                    new_hub.sort()
                    nxt[tuple(new_ports + new_hub)] += weight
            for p, tok in enumerate(ports):
                if tok >= 0: continue
                for h, htok in enumerate(hub):
                    if htok < 0: continue
                    new_ports = list(ports); new_ports[p] = htok
                    new_hub = list(hub); new_hub[h] = -1; new_hub.sort()
                    nxt[tuple(new_ports + new_hub)] += weight
        layers = nxt
    raise AssertionError('unreachable')


def predicted(pi):
    ls = cycles(pi)
    if not ls: return 1
    m = sum(ls); r = len(ls)
    return factorial(r) * (1 << (m - 1)) * prod(ls)


def main():
    by_m = {}
    fib = [0, 1]
    for i in range(2, 10): fib.append(fib[-1] + fib[-2])
    for m in range(2, 7):
        types = defaultdict(lambda: {'permutations': 0, 'count_values': set()})
        for pi in permutations(range(m)):
            if any(i == pi[i] for i in range(m)): continue
            exact = dp_count(pi)
            assert exact == predicted(pi), (m, pi, exact, predicted(pi))
            # BFS is independent of the subset recurrences, including its rule for hub moves.
            if m <= 4:
                assert bfs_count(pi) == exact, (m, pi)
            t = str(cycles(pi))
            types[t]['permutations'] += 1
            types[t]['count_values'].add(exact)
        total = sum(v['permutations'] * next(iter(v['count_values'])) for v in types.values())
        assert total == factorial(m) * (1 << (m-1)) * fib[m-1]
        by_m[str(m)] = {
            'derangement_count': sum(v['permutations'] for v in types.values()),
            'total_labeled_shortest_traces': total,
            'cycle_types': {t: {'permutations': v['permutations'], 'shortest_trace_count_each': next(iter(v['count_values']))}
                            for t, v in sorted(types.items())},
            'minimum_bits_to_restore_source_destination_map': (sum(v['permutations'] for v in types.values()) - 1).bit_length(),
        }
    for m in (8, 9, 10):
        pi = tuple(i ^ 1 for i in range(m)) if m % 2 == 0 else tuple((i//3)*3 + (i+1)%3 for i in range(m))
        assert dp_count(pi) == predicted(pi)
    result = {
        'schema': 'R762AD_STAR_PERMUTATION_BRC_EVIDENCE_V1',
        'scope': 'auxiliary source-labelled star, unit outer capacities, 2-slot hub, each moved token ingresses once and egresses once',
        'verification': 'exhaustive all derangements for moved support m=2..6; independent explicit-state BFS for m<=4; 3 larger representative cases',
        'formula': 'N2(pi)=r!*2^(m-1)*product(nontrivial_cycle_lengths)',
        'aggregate': 'sum_pi_derangement N2(pi)=m!*2^(m-1)*F_(m-1), Fibonacci F_1=F_2=1',
        'by_m': by_m,
        'frozen_science': 'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'parent_artifact': 'R762AC_X6_STAR_BUFFER_FORCE_SOURCE_RESIDUAL.md@ff7f13951e13d2b50134e6139e9493c2659a22f2',
        'native_TRIADIC_CLOSURE_E_admission': 'NOT_PROVED',
    }
    with Path(__file__).with_name('R762AD_EVIDENCE.json').open('w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(by_m, indent=2))


if __name__ == '__main__': main()
