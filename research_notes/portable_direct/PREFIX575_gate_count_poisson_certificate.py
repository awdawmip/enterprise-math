#!/usr/bin/env python3
"""PREFIX-575: exact gate-frequency/Poisson identity on frozen native BRC.

Requires the published PREFIX565 and PREFIX566 native certificates beside this file.
Uses only Python standard-library integer arithmetic after those imports.
Scientific input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
import json
from collections import Counter, deque
from PREFIX565_positive_marginal_certificate import (
    SCIENCE_PIN, ZERO_ROOT, ROOTS, ACTIONS, edge)
from PREFIX566_gate_quotient_certificate import (
    marginal_gate_rows, weighted_quotient)

PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'
# Exact finite Poisson potential, denominator 768, indexed by the canonical 37 classes.
H = (0, 2, -6, -5, 123, 2, -1, 8, 2, -1, 18, 2, 3,
     2, -4, 124, -5, 123, -4, 17, 2, -1, 18, 2, -3, 12,
     5, -4, -1, 17, 3, 6, 5, 14, 17, 17, -3)

# Quadratic-variation Poisson potential, denominator 1,769,472.
W = (0, 4448, -13464, -11245, 236819, 4424, -2197, 17888, 4544,
     -2197, 40032, 4544, 6723, 4448, -9000, 238296, -11245,
     236819, -8968, 37871, 4544, -2197, 40032, 4544, -6777,
     26712, 11351, -8968, -2197, 37871, 6723, 13536, 11351,
     31424, 37871, 37871, -6777)


def main(depth=128):
    assert SCIENCE_PIN == PIN and len(ROOTS) == 9
    rows = marginal_gate_rows(ZERO_ROOT)
    assert all(marginal_gate_rows(r) == rows for r in ROOTS)
    ids, quotient, growth = weighted_quotient(rows)
    assert len(rows) == 96 and len(quotient) == 37 and len(W) == 37
    assert growth == [1, 4, 13, 21, 33, 37] and len(H) == 37
    native = [[edge(i, a, ZERO_ROOT) for a in ACTIONS] for i in range(96)]
    assert all(len(row) == 6 for row in native)
    indegree = Counter(j for row in native for j, w in row)
    assert set(indegree) == set(range(96)) and set(indegree.values()) == {6}
    gate_edges = [(i, j) for i, row in enumerate(native) for j, w in row if w[6]]
    assert sorted(gate_edges) == [(7, 9), (29, 9), (31, 9)]
    sizes = Counter(ids)
    assert sum(sizes.values()) == 96
    A, gate = [], []
    adj, rev = [set() for _ in quotient], [set() for _ in quotient]
    for i, row in enumerate(quotient):
        weight = Counter()
        gates = 0
        for (j, a, b, mark), count in row.items():
            weight[j] += count
            gates += mark * count
        assert sum(weight.values()) == 6
        A.append(weight)
        gate.append(gates)
        for j in weight:
            adj[i].add(j)
            rev[j].add(i)
    assert [(i, g) for i, g in enumerate(gate) if g] == [(4, 1), (15, 1), (17, 1)]
    assert all(sum(sizes[i] * A[i][j] for i in range(37)) == 6 * sizes[j]
               for j in range(37))
    # Exact Poisson equation: 6H_i - sum_j A_ij H_j = 768*g_i - 24.
    assert all(6 * H[i] - sum(count * H[j] for j, count in A[i].items())
               == 768 * gate[i] - 24 for i in range(37))

    def reachable(graph):
        seen = {0}; queue = deque([0])
        while queue:
            i = queue.popleft()
            for j in graph[i]:
                if j not in seen:
                    seen.add(j); queue.append(j)
        return seen
    assert len(reachable(adj)) == len(reachable(rev)) == 37
    # Every transition crosses the bipartition, and (0,7,0) is a 2-cycle.
    colors = [None] * 37; colors[0] = 0; queue = deque([0])
    while queue:
        i = queue.popleft()
        for j in adj[i]:
            if colors[j] is None:
                colors[j] = 1 - colors[i]; queue.append(j)
            assert colors[j] == 1 - colors[i]
    assert (colors.count(0), colors.count(1)) == (17, 20)
    assert 7 in adj[0] and 0 in adj[7]

    # Conditional zero-mean integer martingale increments, scaled by 768.
    # M = 768*gate - 4 + H[next] - H[current].
    vnum = []
    for i, row in enumerate(quotient):
        vnum.append(sum(mult * (768 * mark - 4 + H[j] - H[i])**2
                        for (j, a, b, mark), mult in row.items()))
    assert all(6 * W[i] - sum(mult * W[j] for j, mult in A[i].items())
               == 3 * vnum[i] - 54096 for i in range(37))
    assert sum(sizes[i] * vnum[i] for i in range(37)) == 1731072
    # 96-port independent integer DP for the first moment and centered
    # martingale's second moment, checked at ALL depths 0..128.
    dcount = [0] * 96  # total gate count across all action strings
    b_h = [H[ids[i]] for i in range(96)]
    b_w = [W[ids[i]] for i in range(96)]
    m1 = [0] * 96  # first moment of scaled martingale increment sum
    m2 = [0] * 96  # second moment of scaled martingale increment sum
    power = 1
    checked = 0
    for depth_now in range(depth + 1):
        for i in range(96):
            assert 768 * dcount[i] == (4 * depth_now + H[ids[i]]) * power - b_h[i]
            assert m1[i] == 0
            assert 3 * m2[i] == (9016 * depth_now + W[ids[i]]) * power - b_w[i]
            checked += 1
        if depth_now == depth:
            break
        next_d = []; next_b_h = []; next_b_w = []
        next_m1 = []; next_m2 = []
        for i, row in enumerate(native):
            next_d.append(sum(dcount[j] + w[6] * power for j, w in row))
            next_b_h.append(sum(b_h[j] for j, w in row))
            next_b_w.append(sum(b_w[j] for j, w in row))
            next_m1.append(sum(m1[j] + (768*w[6]-4+H[ids[j]]-H[ids[i]])*power
                               for j,w in row))
            next_m2.append(sum(m2[j] + 2*(768*w[6]-4+H[ids[j]]-H[ids[i]])*m1[j]
                               + (768*w[6]-4+H[ids[j]]-H[ids[i]])**2 * power
                               for j,w in row))
        dcount, b_h, b_w, m1, m2 = next_d, next_b_h, next_b_w, next_m1, next_m2
        power *= 6
    return {
        'status': 'ALL_CHECKS_PASS', 'scientific_pin': PIN,
        'model': '96-port ordered four-STAR X6-BRC; 6 native actions per port',
        'observer': 'q1=q2=q3=q4=q5=q6=1; gate count retained',
        'roots_same_gate_kernel': len(ROOTS), 'ports': 96, 'quotient_classes': 37,
        'native_indegree_each_port': 6, 'gate_edges': gate_edges,
        'stationary_uniform_native': True, 'stationary_gate_rate': '1/192',
        'strongly_connected_quotient': True, 'period': 2,
        'poisson_potential_denominator': 768, 'poisson_potential_numerators': H,
        'variance_martingale_quadratic_rate': '1127/221184',
        'quadratic_poisson_denominator': 1769472,
        'quadratic_poisson_numerators': W,
        'quadratic_poisson_identity_37_rows_checked': 37,
        'martingale_second_moment_identity': 'E_i[M_d^2]=d*1127/221184+(W[class(i)]-E_i[W[class(X_d)]])/1769472',
        'poisson_identity_37_rows_checked': 37,
        'expectation_identity': 'E_i[K_d]=d/192+(H[class(i)]-E_i[H[class(X_d)]])/768',
        'absolute_mean_correction_bound': '65/384',
        'original_96_port_depths_checked': [0, depth],
        'original_96_port_first_and_second_moment_checks_each': checked,
        'identity_valid_all_nonnegative_depths_by_poisson_telescoping': True,
        'admission': 'author exact finite certificate; independent review pending'
    }


if __name__ == '__main__':
    print(json.dumps(main(), ensure_ascii=False, indent=2))
