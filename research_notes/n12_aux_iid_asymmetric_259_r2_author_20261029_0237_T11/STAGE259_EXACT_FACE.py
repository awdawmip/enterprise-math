#!/usr/bin/env python3
"""Stage259 exact author certificate. External ternary IID; not native P000-X6.

Uses only Python stdlib Fraction. Finite ordered histories are independently
traversed: no merging in DFS, both source types retain positive branch masses.
"""
from fractions import Fraction as F

N = 12
P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
LP = F(107495424, 1321555)
LQ = F(69606372, 1321555)
ROOT = F(7515691301, 142727940)
STATES = tuple((i, j, d-i-j) for d in range(N+1)
               for i in range(d+1) for j in range(d-i+1))
assert len(STATES) == 455


def child(s, z):
    return tuple(s[i] + (i == z) for i in range(3))


def ratio(s):
    return F(2, 3)**s[0] * F(2)**s[1]


H, optimal, action_costs, strict_gaps = {}, {}, 0, 0
for s in reversed(STATES):
    costs = {'P': LQ*ratio(s), 'Q': LP}
    if sum(s) < N:
        costs['C'] = ratio(s) + sum(P[z]*H[child(s, z)] for z in range(3))
    H[s] = min(costs.values())
    optimal[s] = tuple(a for a in ('P', 'Q', 'C')
                       if a in costs and costs[a] == H[s])
    action_costs += len(costs)
    strict_gaps += sum(v > H[s] for v in costs.values())
assert action_costs == 1274 and strict_gaps == 809
assert H[(0, 0, 0)] == ROOT
expected_ties = {(0, 0, k) for k in range(3, N)} | {(0, 1, 3)}
assert {s for s in STATES if len(optimal[s]) > 1} == expected_ties
assert all(optimal[(0, 0, k)] == ('P', 'C') for k in range(3, N))
assert optimal[(0, 1, 3)] == ('Q', 'C')
assert optimal[(0, 0, 0)] == ('C',)
assert optimal[(0, 0, 1)] == ('C',)
assert optimal[(0, 0, 2)] == ('C',)


def action(s, cutoff, special_continue):
    if s[0] == s[1] == 0:
        return 'P' if sum(s) >= cutoff else 'C'
    if s == (0, 1, 3):
        return 'C' if special_continue else 'Q'
    return optimal[s][0]


def suffix_dp(cutoff, special_continue):
    out = {}
    for s in reversed(STATES):
        a = action(s, cutoff, special_continue)
        if a == 'P':
            out[s] = (F(0), F(1), F(0), F(0))
        elif a == 'Q':
            out[s] = (F(1), F(0), F(0), F(0))
        else:
            out[s] = tuple(
                int(i >= 2) + sum((P if i in (0, 2) else Q)[z]
                                    * out[child(s, z)][i] for z in range(3))
                for i in range(4)
            )
    return out[(0, 0, 0)]


def ordered_dfs(cutoff, special_continue):
    four = [F(0) for _ in range(4)]
    source_terminal = [F(0), F(0)]
    nodes, terminals = 0, 0

    def visit(history, pm, qm):
        nonlocal nodes, terminals
        nodes += 1
        s = (history.count(0), history.count(1), history.count(2))
        a = action(s, cutoff, special_continue)
        if a == 'C':
            four[2] += pm
            four[3] += qm
            for z in range(3):
                visit(history + (z,), pm*P[z], qm*Q[z])
        else:
            terminals += 1
            source_terminal[0] += pm
            source_terminal[1] += qm
            if a == 'P':
                four[1] += qm
            else:
                four[0] += pm

    visit((), F(1), F(1))
    assert tuple(source_terminal) == (F(1), F(1))
    return tuple(four), nodes, terminals


B, C = {}, {}
ordered_nodes = ordered_terminals = 0
for cutoff in range(3, N+1):
    for special_continue, table in ((False, B), (True, C)):
        v = suffix_dp(cutoff, special_continue)
        crosscheck, nn, nt = ordered_dfs(cutoff, special_continue)
        assert v == crosscheck
        table[cutoff] = v
        ordered_nodes += nn
        ordered_terminals += nt
        assert v[3] > v[2]
        assert v[3] + LP*v[0] + LQ*v[1] == ROOT

# The special tie receives three of four ordered paths at neutral cutoff 3,
# and four of four from cutoff 4 onward: positive-source provenance matters.
D3 = tuple(C[3][i]-B[3][i] for i in range(4))
D4 = tuple(C[4][i]-B[4][i] for i in range(4))
assert all(D3[i] == F(3, 4)*D4[i] for i in range(4))
for k in range(4, N+1):
    assert tuple(C[k][i]-B[k][i] for i in range(4)) == D4

# All Bellman equality policies lie on two 4-observer line segments,
# apart from C3. Thus these five vertices exhaust the contact fiber.
for k in range(3, N+1):
    w = (B[k][0]-B[3][0])/(B[N][0]-B[3][0])
    assert 0 <= w <= 1
    assert B[k] == tuple((1-w)*B[3][i]+w*B[N][i] for i in range(4))
for k in range(4, N+1):
    w = (C[k][0]-C[4][0])/(C[N][0]-C[4][0])
    assert 0 <= w <= 1
    assert C[k] == tuple((1-w)*C[4][i]+w*C[N][i] for i in range(4))

VERTICES = (C[3], C[4], C[N], B[N], B[3])

def cross(o, u, v):
    return (u[0]-o[0])*(v[1]-o[1])-(u[1]-o[1])*(v[0]-o[0])

turns = tuple(cross(VERTICES[i], VERTICES[(i+1)%5],
                    VERTICES[(i+2)%5]) for i in range(5))
assert all(t > 0 for t in turns)
area = abs(sum(VERTICES[i][0]*VERTICES[(i+1)%5][1] -
               VERTICES[i][1]*VERTICES[(i+1)%5][0]
               for i in range(5)))/2
assert area == F(163431317383515625, 151628202826291740672)
OLD_LINE = F(11379926137, 11609505792)
NEW_LINE = F(33809389661, 34828517376)
assert all(2*v[0]+v[1] <= OLD_LINE for v in VERTICES)
assert all(2*v[0]+v[1] >= NEW_LINE for v in VERTICES)
assert all(2*v[0]+v[1] == OLD_LINE for v in (B[3], B[N]))
assert all(2*v[0]+v[1] == NEW_LINE for v in (C[4], C[N]))
# Direct Stage258 shared four-observer edge (not merely equal 2D endpoints).
assert B[3] == (F(661800839, 7739670528), F(2348630905, 2902376448),
                F(917102471, 322486272), F(745221767, 241864704))
assert B[N] == (F(14080778551, 69657034752), F(5014749965, 8707129344),
                F(16378493239, 2902376448), F(4266808051, 725594112))

# An exact feasible cap strictly beyond Stage258's C3--C12 edge.
a = F(6257204592203, 43535646720000)
b = F(942101660479, 1360488960000)
assert OLD_LINE - 2*a-b == F(3, 10000)
# Positive root mixture of deterministic Bellman-equality policies C3, B12, B3.
W = (F(4353564672, 103246484375),
     F(841890839780122733, 1677666785610156250),
     F(765034255268522093, 1677666785610156250))
assert sum(W) == 1 and all(w > 0 for w in W)
MIX = (C[3], B[N], B[3])
obs = tuple(sum(W[j]*MIX[j][i] for j in range(3)) for i in range(4))
assert obs[0] == a and obs[1] == b
assert obs[3] > obs[2]
value = ROOT - LP*a - LQ*b
assert value == obs[3]
assert value == F(673365388654906643, 149830082294400000)
assert obs[2] == F(10196336991431739473, 2397281316710400000)

if __name__ == '__main__':
    print('STAGE259_EXACT_BELLMAN_PASS', len(STATES), action_costs,
          strict_gaps, len(expected_ties))
    print('DUAL', 'lambdaP', LP, 'lambdaQ', LQ,
          'thetaP', 0, 'thetaQ', 1, 'root', ROOT)
    for label, v in zip(('C3','C4','C12','B12','B3'), VERTICES):
        print('VERTEX', label, *(str(x) for x in v))
    print('D3', *(str(x) for x in D3))
    print('D4', *(str(x) for x in D4))
    print('AREA', area, 'TURNS', *(str(x) for x in turns))
    print('TARGET', a, b, 'value', value,
          'tP', obs[2], 'tQ', obs[3])
    print('MIXTURE', *(str(w) for w in W))
    print('OUTSIDE_STAGE258_BY', OLD_LINE-2*a-b)
    print('ORDERED_DFS', ordered_nodes, ordered_terminals)
    print('STAGE259_EXACT_ALL_REAL_FACE_PASS')
