#!/usr/bin/env python3
"""Stage260 complete exact rational certificate for an external ternary IID model.

This script checks one Bellman dual; all Bellman-minimizing count-state policies;
all four original-source observables; every ordered history (without merging)
for 18 policies; the convex equality-fiber geometry, adjacency, and exact
attaining policy. It makes no P000-native-X6 dynamics or Source authority claim.
"""
from fractions import Fraction as F

N = 12
P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
LP = F(17915904, 217655)
LQ = F(11569812, 217655)
ROOT = F(44960725931, 846242640)
STATES = tuple((i, j, d - i - j) for d in range(N + 1)
               for i in range(d + 1) for j in range(d - i + 1))
assert len(STATES) == 455


def child(s, z):
    return tuple(s[i] + (i == z) for i in range(3))


def ratio(s):
    return F(2, 3) ** s[0] * F(2) ** s[1]


# Every action is evaluated exactly. P-normalized Bellman continuation
# includes Q-source observation time through the likelihood ratio.
H, OPTIMAL, action_count, strict_count = {}, {}, 0, 0
for s in reversed(STATES):
    costs = {'P': LQ * ratio(s), 'Q': LP}
    if sum(s) < N:
        costs['C'] = ratio(s) + sum(P[z] * H[child(s, z)] for z in range(3))
    minimum = min(costs.values())
    H[s] = minimum
    OPTIMAL[s] = tuple(a for a in ('P', 'Q', 'C')
                       if a in costs and costs[a] == minimum)
    action_count += len(costs)
    strict_count += sum(v > minimum for v in costs.values())
assert (action_count, strict_count, H[(0, 0, 0)]) == (1274, 810, ROOT)
expected_ties = {(0, 0, k) for k in range(4, 12)} | {(0, 1, 4)}
assert {s for s in STATES if len(OPTIMAL[s]) > 1} == expected_ties
assert all(OPTIMAL[(0, 0, k)] == ('P', 'C') for k in range(4, 12))
assert OPTIMAL[(0, 1, 4)] == ('Q', 'C')
assert all(OPTIMAL[(0, 0, k)] == ('C',) for k in range(0, 4))


def action(s, cutoff, special_continue):
    if s[0] == s[1] == 0:
        return 'P' if sum(s) >= cutoff else 'C'
    if s == (0, 1, 4):
        return 'C' if special_continue else 'Q'
    return OPTIMAL[s][0]


def suffix_dp(cutoff, special_continue):
    obs = {}
    for s in reversed(STATES):
        a = action(s, cutoff, special_continue)
        if a == 'P':
            obs[s] = (F(0), F(1), F(0), F(0))
        elif a == 'Q':
            obs[s] = (F(1), F(0), F(0), F(0))
        else:
            obs[s] = tuple(
                int(i >= 2) + sum((P if i in (0, 2) else Q)[z]
                                    * obs[child(s, z)][i] for z in range(3))
                for i in range(4)
            )
    return obs[(0, 0, 0)]


def unmerged_ordered_dfs(cutoff, special_continue):
    four = [F(0)] * 4
    source_terminal = [F(0), F(0)]
    nodes = terminal_paths = 0

    def visit(history, pm, qm):
        nonlocal nodes, terminal_paths
        nodes += 1
        s = (history.count(0), history.count(1), history.count(2))
        a = action(s, cutoff, special_continue)
        if a == 'C':
            four[2] += pm
            four[3] += qm
            for z in range(3):
                visit(history + (z,), pm * P[z], qm * Q[z])
        else:
            terminal_paths += 1
            source_terminal[0] += pm
            source_terminal[1] += qm
            if a == 'P':
                four[1] += qm
            else:
                four[0] += pm

    visit((), F(1), F(1))
    assert tuple(source_terminal) == (F(1), F(1))
    return tuple(four), nodes, terminal_paths


B, C = {}, {}
ordered_nodes = ordered_terminals = 0
for k in range(4, N + 1):
    for cont, dest in ((False, B), (True, C)):
        v = suffix_dp(k, cont)
        v_full, nodes, terms = unmerged_ordered_dfs(k, cont)
        assert v == v_full
        dest[k] = v
        ordered_nodes += nodes
        ordered_terminals += terms
        assert v[3] > v[2]
        assert v[3] + LP*v[0] + LQ*v[1] == ROOT

D4 = tuple(C[4][i]-B[4][i] for i in range(4))
D5 = tuple(C[5][i]-B[5][i] for i in range(4))
assert all(D4[i] == F(4, 5)*D5[i] for i in range(4))
for k in range(5, N + 1):
    assert all(C[k][i] - B[k][i] == D5[i] for i in range(4))
for k in range(4, N + 1):
    w = (B[k][0] - B[4][0]) / (B[N][0] - B[4][0])
    assert 0 <= w <= 1
    assert B[k] == tuple((1-w)*B[4][i]+w*B[N][i] for i in range(4))
for k in range(5, N + 1):
    w = (C[k][0] - C[5][0]) / (C[N][0] - C[5][0])
    assert 0 <= w <= 1
    assert C[k] == tuple((1-w)*C[5][i]+w*C[N][i] for i in range(4))

VERTICES = (C[4], C[5], C[N], B[N], B[4])
NAMES = ('C4', 'C5', 'C12', 'B12', 'B4')

def cross(o, u, v):
    return (u[0]-o[0])*(v[1]-o[1])-(u[1]-o[1])*(v[0]-o[0])

turns = tuple(cross(VERTICES[i], VERTICES[(i+1)%5],
                    VERTICES[(i+2)%5]) for i in range(5))
assert all(t > 0 for t in turns)
AREA = abs(sum(VERTICES[i][0]*VERTICES[(i+1)%5][1] -
               VERTICES[i][1]*VERTICES[(i+1)%5][0]
               for i in range(5)))/2
assert AREA == F(536059353705078125, 606512811305166962688)
OLD_LINE = F(33809389661, 34828517376)
NEXT_LINE = F(22312869149, 23219011584)
assert all(2*v[0] + v[1] <= OLD_LINE for v in VERTICES)
assert all(2*v[0] + v[1] >= NEXT_LINE for v in VERTICES)
assert all(2*v[0] + v[1] == OLD_LINE for v in (B[4], B[N]))
assert all(2*v[0] + v[1] == NEXT_LINE for v in (C[5], C[N]))
# Exact Stage259 four-observer edge; this is not only an error-pair match.
assert B[4] == (F(2315791267, 23219011584), F(6715503965, 8707129344),
                F(3454944163, 967458816), F(2845990051, 725594112))
assert B[N] == (F(13392328801, 69657034752), F(5104265215, 8707129344),
                F(16809787489, 2902376448), F(4457228801, 725594112))

A_CAP = F(6349626716117, 43535646720000)
B_CAP = F(984980765, 1451188224)
assert OLD_LINE - 2*A_CAP - B_CAP == F(3, 10000)
assert all(cross(VERTICES[i], VERTICES[(i+1)%5],
                 (A_CAP, B_CAP)) > 0 for i in range(5))
# Root mixture C4, B12, B4; exact barycentric target realization.
W = (F(3265173504, 85021484375),
     F(1803256470623293, 3593177972656250),
     F(1651928739406909, 3593177972656250))
assert sum(W) == 1 and all(w > 0 for w in W)
OBS = tuple(sum(w*v[i] for w,v in zip(W, (C[4], B[N], B[4])))
            for i in range(4))
assert OBS[0] == A_CAP and OBS[1] == B_CAP
assert OBS[3] > OBS[2]
assert OBS[3] == ROOT-LP*A_CAP-LQ*B_CAP
assert OBS[3] == F(82993854248339957, 16450956921600000)
assert OBS[2] == F(1851794737526929603, 394822966118400000)

if __name__ == '__main__':
    print('STAGE260_BELLMAN_PASS',len(STATES),action_count,strict_count,len(expected_ties))
    print('DUAL',LP,LQ,'thetaP',0,'thetaQ',1,'root',ROOT)
    for name,v in zip(NAMES,VERTICES):
        print('VERTEX',name,*(str(x) for x in v))
    print('D4_OVER_D5',F(4,5),'ALL_FOUR_OBSERVABLES')
    print('TURNS',*(str(x) for x in turns))
    print('AREA',AREA)
    print('TARGET_CAPS',A_CAP,B_CAP)
    print('TARGET_VALUE',OBS[3], 'tP',OBS[2], 'tQ',OBS[3])
    print('ROOT_MIXTURE',*(str(w) for w in W))
    print('OLD_LINE_GAP', OLD_LINE-(2*A_CAP+B_CAP))
    print('NEXT_EDGE_LINE', NEXT_LINE)
    print('ORDERED_DFS',ordered_nodes,ordered_terminals)
    print('STAGE260_EXACT_ALL_REAL_FACE_PASS')
