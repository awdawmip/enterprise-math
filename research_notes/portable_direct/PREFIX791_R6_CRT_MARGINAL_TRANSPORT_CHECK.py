#!/usr/bin/env python3
"""PREFIX-791 exact integer verification: CRT marginals and sharp transport.

Finite external source-path integer-weight observer. No native X6 dynamics assumed.
Uses only Python standard-library integers and deterministic random sampling.
"""
from collections import Counter, defaultdict
from itertools import product
from math import gcd, lcm
from random import Random
import json

SEED = 79120261115


def crt_pair(a, b, m, n):
    g = gcd(m, n)
    if (a - b) % g:
        raise ValueError('CRT-incompatible residues')
    tmod = n // g
    k = 0 if tmod == 1 else (((b-a)//g) * pow(m//g, -1, tmod)) % tmod
    return (a + m*k) % lcm(m, n)


def margins(weights, m, n):
    return (Counter(w % m for w in weights), Counter(w % n for w in weights))


def sharp_bounds(row, col, m, n, a, b):
    g = gcd(m, n)
    if (a-b) % g:
        return (0, 0)
    h = a % g
    N = sum(row[x] for x in range(m) if x % g == h)
    assert N == sum(col[y] for y in range(n) if y % g == h)
    return (max(0, row[a] + col[b] - N), min(row[a], col[b]))


def exact_extreme_transport(row, col, m, n, a, b, cell_count):
    """Complete bipartite transportation within each gcd block, with one cell fixed."""
    g = gcd(m, n)
    assert (a-b) % g == 0
    ans = [[0 for _ in range(n)] for _ in range(m)]
    for h in range(g):
        xs = [x for x in range(m) if x % g == h]
        ys = [y for y in range(n) if y % g == h]
        rem_r = {x: row[x] for x in xs}
        rem_c = {y: col[y] for y in ys}
        if h == a % g:
            assert 0 <= cell_count <= min(rem_r[a], rem_c[b])
            ans[a][b] = cell_count
            rem_r[a] -= cell_count
            rem_c[b] -= cell_count
            for y in ys:
                if y == b: continue
                z = min(rem_r[a], rem_c[y])
                ans[a][y] += z
                rem_r[a] -= z
                rem_c[y] -= z
            assert rem_r[a] == 0
            for x in xs:
                if x == a: continue
                z = min(rem_r[x], rem_c[b])
                ans[x][b] += z
                rem_r[x] -= z
                rem_c[b] -= z
            assert rem_c[b] == 0
        for x in xs:
            for y in ys:
                if h == a % g and (x == a or y == b):
                    continue
                z = min(rem_r[x], rem_c[y])
                ans[x][y] += z
                rem_r[x] -= z
                rem_c[y] -= z
        assert all(v == 0 for v in rem_r.values())
        assert all(v == 0 for v in rem_c.values())
    assert all(sum(ans[x]) == row[x] for x in range(m))
    assert all(sum(ans[x][y] for x in range(m)) == col[y] for y in range(n))
    assert ans[a][b] == cell_count
    return ans


def realize(table, m, n):
    return [crt_pair(a, b, m, n) for a in range(m) for b in range(n)
            for _ in range(table[a][b])]


def crt_coprime(residues, moduli):
    L = lcm(*moduli)
    answer = 0
    for a, m in zip(residues, moduli):
        if m == 1: continue
        q = L // m
        answer += a * q * pow(q, -1, m)
    return answer % L


def k_way_endpoint(marginals, moduli, target, low):
    N = sum(marginals[0].values())
    wanted = [marginals[i][target[i]] for i in range(len(moduli))]
    if low:
        # Complements are consecutive nonoverlapping/cyclic blocks and thus
        # have the largest possible union, minimizing intersection of events.
        event_sets = []
        start = 0
        for r in wanted:
            complement = {(start+j) % N for j in range(N-r)} if N else set()
            start += N-r
            event_sets.append(set(range(N)) - complement)
    else:
        event_sets = [set(range(r)) for r in wanted]
    columns = []
    for i, m in enumerate(moduli):
        values = [None]*N
        for j in event_sets[i]:
            values[j] = target[i]
        free = [j for j in range(N) if values[j] is None]
        pool = [r for r in range(m) if r != target[i]
                for _ in range(marginals[i][r])]
        assert len(free) == len(pool)
        for j, r in zip(free, pool):
            values[j] = r
        columns.append(values)
    ws = [crt_coprime([columns[i][j] for i in range(len(moduli))],moduli)
          for j in range(N)]
    for i, m in enumerate(moduli):
        assert Counter(w % m for w in ws) == +marginals[i]
    return ws


def check():
    rng = Random(SEED)
    assertion_count = 0
    two_modulus_cases = 0
    pairs_checked = 0
    endpoint_constructions = 0
    strict_intervals = 0
    incompatible_pairs = 0
    for _ in range(1800):
        m, n = rng.randint(1, 12), rng.randint(1, 12)
        ws = [rng.randint(-120, 120) for _ in range(rng.randint(1, 16))]
        R, C = margins(ws, m, n)
        D = Counter((w % m,w % n) for w in ws)
        for a, b in product(range(m),range(n)):
            lo, hi = sharp_bounds(R,C,m,n,a,b)
            assert lo <= D[a,b] <= hi
            assertion_count += 1
            pairs_checked += 1
            if (a-b) % gcd(m,n):
                assert lo == hi == D[a,b] == 0
                incompatible_pairs += 1
                assertion_count += 1
                continue
            if lo < hi: strict_intervals += 1
            for x in {lo,hi}:
                table = exact_extreme_transport(R,C,m,n,a,b,x)
                rebuilt = realize(table,m,n)
                R2,C2 = margins(rebuilt,m,n)
                assert R2 == R and C2 == C
                assert Counter((w%m,w%n) for w in rebuilt)[a,b] == x
                assert len(rebuilt) == len(ws)
                assertion_count += 3
                endpoint_constructions += 1
        two_modulus_cases += 1

    examples = {
        'same_marginals_target_0_ambiguous': [ [0,1,2], [2,3,4] ],
        'same_marginals_target_0_forced_positive': [ [0,0,1], [0,3,4] ]
    }
    for key,(a,b) in examples.items():
        assert margins(a,2,3) == margins(b,2,3)
        assert Counter(w % 6 for w in a)[0] != Counter(w % 6 for w in b)[0]
        assertion_count += 2

    support_cases=[]
    for mods in [(1,), (2,3), (2,4), (3,4,5), (2,3,5), (1,7),
                 (3,6,9), (4,6,9), (1,1), (2,3,5,7)]:
        L, M = lcm(*mods), max(mods)
        S = set(range(M))
        G = set(range(L))
        assert all({t%m for t in S} == set(range(m)) for m in mods)
        assert len(G-S) == L-M
        support_cases.append({'moduli':mods,'lcm':L,'largest_modulus':M,
                              'actual_joint_classes':M,'consistent_classes':L,
                              'potential_false_classes':L-M})
        assertion_count += 2

    multi_cases=0
    for mods in [(2,3,5),(3,4,5),(2,5,7),(2,3,7,11),(1,3,5)]:
        for _ in range(300):
            N = rng.randint(1, 18)
            ws = [rng.randint(-200,200) for _ in range(N)]
            marg = [Counter(w%m for w in ws) for m in mods]
            target = [rng.randrange(m) for m in mods]
            sizes = [marg[i][target[i]] for i in range(len(mods))]
            lo = max(0,sum(sizes) - (len(mods)-1)*N)
            hi = min(sizes)
            actual = sum(all(w % m == r for m,r in zip(mods,target)) for w in ws)
            assert lo <= actual <= hi
            for islow, endpoint in [(True,lo),(False,hi)]:
                rebuilt = k_way_endpoint(marg, mods, target, islow)
                assert len(rebuilt) == N
                got = sum(all(w%m == r for m,r in zip(mods,target)) for w in rebuilt)
                assert got == endpoint
                assertion_count += 2
            multi_cases += 1
            assertion_count += 1
    return {
        'schema': 'PREFIX791_CRT_JOINT_RESIDUE_TRANSPORT_V1',
        'status': 'ALL_CHECKS_PASS PREFIX791 SHARP_CRT_MARGINAL_CERTIFICATES',
        'seed': SEED,
        'frozen_science': 'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'predecessor': 'PREFIX-790',
        'scope': 'finite multisets of integer path weights; independent marginal residues; external observer; exact integer arithmetic',
        'two_modulus_cases': two_modulus_cases,
        'compatible_and_incompatible_pairs_checked': pairs_checked,
        'incompatible_pairs_checked': incompatible_pairs,
        'sharp_intervals_with_multiple_feasible_counts': strict_intervals,
        'endpoint_constructions': endpoint_constructions,
        'multi_coprime_cases': multi_cases,
        'joint_support_bound_cases': support_cases,
        'fixed_examples': examples,
        'exact_assertions': assertion_count,
        'proof_basis': 'CRT bijection on gcd-compatible pairs; integer transportation in each full gcd block; sharp event-set intersection bound for coprime moduli; projection-cardinality extremum',
        'limitations': 'Target bounds concern all integer-weight path multisets with the given marginals; a fixed native provenance graph can impose stricter constraints. No native X6 experimental admission.'
    }

if __name__ == '__main__':
    out = check()
    print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))
