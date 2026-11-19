#!/usr/bin/env python3
"""R762GF exact X6 relative-depth cocycle and named triad candidate test."""
from collections import Counter
from itertools import product, permutations
from pathlib import Path
import json

N = 6
AXES = range(N)
LETTERS = [(j, e) for j in AXES for e in (-1, 1)]


def canon(z):
    k = min(z)
    return tuple(x - k for x in z), k


def advance(r, j, e):
    a = list(r)
    a[j] += e
    c = min(a)
    return tuple(x - c for x in a), c


def direct(z, j, e):
    a = list(z)
    a[j] += e
    return tuple(a)


def expected_c(r, j, e):
    if e == -1:
        return -1 if r[j] == 0 else 0
    return 1 if r[j] == 0 and all(r[k] > 0 for k in AXES if k != j) else 0


def triad(ordered_axes, anchor):
    ports = ('p0', 'p1', 'p2')
    return {
        'axes': tuple(ordered_axes),
        'quantum': (1, 1, 1),
        'ports': ports,
        'links': (('p0', 'p1'), ('p1', 'p2'), ('p2', 'p0')),
        'anchor': tuple(anchor),
    }


def closure(event):
    axes, ports = event['axes'], event['ports']
    return (len(axes) == 3 and len(set(axes)) == 3 and
            all(0 <= i < N for i in axes) and len(ports) == 3 and
            len(set(ports)) == 3 and event['quantum'] == (1, 1, 1) and
            set(event['links']) ==
            {(ports[i], ports[(i + 1) % 3]) for i in range(3)})


def triad_transport(event):
    z = list(event['anchor'])
    for j in event['axes']:
        z[j] += 1
    return tuple(z)


def relink_gate(z, a, j=0):
    """Candidate named Cell/Link incidence: z is a +E_j neighbor of a."""
    return tuple(z) == direct(a, j, 1)


def verify():
    local_states = edge_checks = 0
    for r in product(range(3), repeat=N):
        if min(r) != 0:
            continue
        local_states += 1
        successors = set()
        for j, e in LETTERS:
            r1, c = advance(r, j, e)
            assert c == expected_c(r, j, e)
            assert (r1, c) == canon(direct(r, j, e))
            assert r1 not in successors
            successors.add(r1)
            for h in (-2, 0, 3):
                z = tuple(x + h for x in r)
                assert canon(direct(z, j, e)) == (r1, h + c)
            edge_checks += 1
    assert local_states == 3**N - 2**N == 665
    assert edge_checks == 7980

    # Exact dynamic programming with integer word multiplicity; m <= 6.
    dp = {(0,) * N: 1}
    returns = {}
    for m in range(1, 7):
        next_dp = Counter()
        for z, count in dp.items():
            for j, e in LETTERS:
                next_dp[direct(z, j, e)] += count
        dp = dict(next_dp)
        fiber = Counter()
        for z, count in dp.items():
            r, h = canon(z)
            if r == (0,) * N:
                fiber[h] += count
        returns[str(m)] = dict(sorted(fiber.items()))
        assert sum(dp.values()) == 12**m
    assert returns['6'] == {-1: 720, 0: 19920, 1: 720}

    # Independent six-step combinatorial partition.
    zero_count = 6*20 + (6*5)*180 + 20*720
    assert zero_count == 19920
    assert sum(returns['6'].values()) == zero_count + 2*720
    r, hol = (0,) * N, 0
    for j in AXES:
        r, c = advance(r, j, 1)
        hol += c
    assert r == (0,) * N and hol == 1

    covariance_checks = 0
    anchor = (-2, -1, 0, 1, 2, 3)
    for axes in permutations(AXES, 3):
        event = triad(axes, anchor)
        assert closure(event)
        assert not closure({**event, 'links': (('p0', 'p1'), ('p1', 'p2'))})
        target = triad_transport(event)
        for perm in permutations(AXES):
            def permute(z):
                out = [0] * N
                for old, new in enumerate(perm):
                    out[new] = z[old]
                return tuple(out)
            transformed = triad(tuple(perm[j] for j in axes), permute(anchor))
            assert closure(transformed)
            assert triad_transport(transformed) == permute(target)
            covariance_checks += 1
    assert covariance_checks == 86400

    anchor_cell = (0,) * N
    z = direct(anchor_cell, 0, 1)
    shifted = tuple(x + 1 for x in z)
    assert canon(z)[0] == canon(shifted)[0]
    assert relink_gate(z, anchor_cell) and not relink_gate(shifted, anchor_cell)
    for u in ((0,) * N, (3, -1, 4, 0, -2, 7)):
        sh = lambda v: tuple(x + y for x, y in zip(v, u))
        assert relink_gate(z, anchor_cell) == relink_gate(sh(z), sh(anchor_cell))

    return {
        'result': 'PASS',
        'claim': 'R762GF',
        'space': 'signed X6 primitive coordinate adjacency; proposed triad model typed separately',
        'local_relative_states': local_states,
        'local_relative_edges_checked': edge_checks,
        'six_step_return_fibers': returns['6'],
        'all_depth_return_counts': returns,
        'all_s6_typed_triad_covariance_checks': covariance_checks,
        'zero_cell_six_step_words': zero_count,
        'nonzero_depth_six_step_words': 1440,
        'six_step_relative_return_words': 21360,
        'positive_brc_weight_denominator': 12**6,
        'shortest_nonzero_depth_loop_length': 6,
        'author_verification': 'EXACT_INTEGER_DP_AND_FINITE_CHECKS',
        'independent_review': 'NOT_REVIEWED'
    }


if __name__ == '__main__':
    evidence = verify()
    Path(__file__).with_name('R762GF_EVIDENCE.json').write_text(
        json.dumps(evidence, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps(evidence, ensure_ascii=False, indent=2))
