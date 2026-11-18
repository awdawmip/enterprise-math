#!/usr/bin/env python3
"""Stage263: exact finite N=12 ternary-IID Bellman dual and ordered-path check.

This is an external auxiliary probability model, NOT native P000/X6 dynamics.
All proof assertions use Fraction exact rational arithmetic; no floating point.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product

N = 12
P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
CAP_A = F(1443791791151, 14511882240000)
CAP_B = F(6493321465, 8707129344)
LAMBDA_P = F(47156, 545)
LAMBDA_Q = F(60111, 1090)
ROOT_H = F(89584701487, 1627361280)
OPTIMUM = F(1313484313680967, 247155494400000)
T_P = F(1532741199372751, 329540659200000)
GAP_T = F(1203144324047, 1813985280000)

STATES = [
    (i, j, d - i - j)
    for d in range(N + 1)
    for i in range(d + 1)
    for j in range(d - i + 1)
]
assert len(STATES) == 455

def nxt(s, z):
    return tuple(x + int(q == z) for q, x in enumerate(s))

# Bellman costs normalized by the strictly positive P probability of each
# specific history. The normalized likelihood ratio is identical for all
# ordered histories sharing count s, but their paths remain distinct.
VALUES, MIN_ACTIONS = {}, {}
strict_gaps = []
action_costs = 0
for s in reversed(STATES):
    i, j, k = s
    ratio = F(2, 3) ** i * F(2) ** j
    costs = {'P': LAMBDA_Q * ratio, 'Q': LAMBDA_P}
    if sum(s) < N:
        costs['C'] = ratio + sum(P[z] * VALUES[nxt(s, z)] for z in range(3))
    action_costs += len(costs)
    minimum = min(costs.values())
    VALUES[s] = minimum
    MIN_ACTIONS[s] = tuple(a for a in ('P', 'Q', 'C') if a in costs and costs[a] == minimum)
    strict_gaps.extend(cost - minimum for cost in costs.values() if cost > minimum)
assert VALUES[(0, 0, 0)] == ROOT_H
assert action_costs == 1274 and len(strict_gaps) == 817
TIES = tuple((s, MIN_ACTIONS[s]) for s in ((0, 1, 7), (0, 0, 5)))
assert {s for s in STATES if len(MIN_ACTIONS[s]) > 1} == {s for s, _ in TIES}
assert TIES == (((0, 1, 7), ('Q', 'C')), ((0, 0, 5), ('P', 'C')))


def make_policy(bit_tuple):
    assert len(bit_tuple) == len(TIES)
    result = {s: MIN_ACTIONS[s][0] for s in STATES}
    for (s, actions), bit in zip(TIES, bit_tuple):
        result[s] = actions[bit]
    return result


def count_dag_observers(policy):
    mass = defaultdict(lambda: (F(0), F(0)))
    mass[(0, 0, 0)] = (F(1), F(1))
    ep = eq = tp = tq = endp = endq = F(0)
    for s in STATES:
        pp, qq = mass[s]
        a = policy[s]
        if a == 'P':
            eq += qq
            endp += pp
            endq += qq
        elif a == 'Q':
            ep += pp
            endp += pp
            endq += qq
        else:
            assert a == 'C' and sum(s) < N
            tp += pp
            tq += qq
            for z in range(3):
                oldp, oldq = mass[nxt(s, z)]
                mass[nxt(s, z)] = (oldp + pp * P[z], oldq + qq * Q[z])
    assert endp == endq == 1
    return ep, eq, tp, tq


def ordered_history_observers(policy):
    """Independent full ternary ordered-word DFS, no count mass aggregation."""
    result = [F(0) for _ in range(6)]  # errors, times, terminal P/Q
    visited = terminal_branches = 0

    def visit(word, pp, qq):
        nonlocal visited, terminal_branches
        visited += 1
        s = tuple(word.count(z) for z in range(3))
        a = policy[s]
        if a == 'P':
            result[1] += qq
            result[4] += pp
            result[5] += qq
            terminal_branches += 1
        elif a == 'Q':
            result[0] += pp
            result[4] += pp
            result[5] += qq
            terminal_branches += 1
        else:
            assert a == 'C' and len(word) < N
            result[2] += pp
            result[3] += qq
            for z in range(3):
                visit(word + (z,), pp * P[z], qq * Q[z])
    visit((), F(1), F(1))
    assert result[4] == result[5] == 1
    return tuple(result[:4]), visited, terminal_branches

# Ties in explicit bit order (0,1,7), (0,0,5).
# F5,F6 coincide with the immutable Stage262 boundary vertices.
MASKS = ((0, 0), (0, 1), (1, 0), (1, 1))
POLICIES = {bits: make_policy(bits) for bits in MASKS}
V = {bits: count_dag_observers(POLICIES[bits]) for bits in MASKS}

F5 = (
    F(4312568159, 46438023168), F(13246202305, 17414258688),
    F(8556473951, 1934917632), F(7350985727, 1451188224),
)
F6 = (
    F(182851367, 1719926784), F(471373465, 644972544),
    F(348833063, 71663616), F(298085351, 53747712),
)
G5 = (
    F(668435839, 7739670528), F(2229900905, 2902376448),
    F(1450753471, 322486272), F(1259213767, 241864704),
)
G6 = (
    F(1524881053, 15479341056), F(4295642435, 5804752896),
    F(3198716317, 644972544), F(2764486909, 483729408),
)
assert V == dict(zip(MASKS, (F5, F6, G5, G6)))
assert len(set(V.values())) == 4
for v in V.values():
    assert v[3] > v[2]
    assert v[3] + LAMBDA_P * v[0] + LAMBDA_Q * v[1] == ROOT_H

# Root randomization amongst F5,F6,G5 realizes the exact outside caps.
WEIGHTS = (
    F(122100138041, 266113281250),
    F(1082351533, 2128906250),
    F(4359600792, 133056640625),
)
assert all(w > 0 for w in WEIGHTS) and sum(WEIGHTS) == 1
mixed = tuple(sum(w * v[q] for w, v in zip(WEIGHTS, (F5, F6, G5))) for q in range(4))
assert mixed == (CAP_A, CAP_B, T_P, OPTIMUM)
assert mixed[3] - mixed[2] == GAP_T > 0
assert ROOT_H - LAMBDA_P * CAP_A - LAMBDA_Q * CAP_B == OPTIMUM

# Exact all-real equality-region geometry: R263=conv(F5,G5,G6,F6).
def orient(u, v, w):
    return (v[0] - u[0]) * (w[1] - u[1]) - (v[1] - u[1]) * (w[0] - u[0])

REGION = (F5, G5, G6, F6)
corners = tuple(orient(REGION[i], REGION[(i + 1) % 4], REGION[(i + 2) % 4]) for i in range(4))
assert corners == (
    F(665283203125, 7312316880125952),
    F(133056640625, 1218719480020992),
    F(133056640625, 1218719480020992),
    F(665283203125, 7312316880125952),
)
assert all(c > 0 for c in corners)
area = abs(sum(REGION[i][0] * REGION[(i + 1) % 4][1]
               - REGION[(i + 1) % 4][0] * REGION[i][1] for i in range(4))) / 2
assert area == F(1463623046875, 14624633760251904)
D5 = (F(1166286571, 11609505792), F(3274031045, 4353564672))
D6 = (F(1786693553, 15479341056), F(4182329935, 5804752896))
assert orient(F5, F6, G5) < 0 and orient(F5, F6, G6) < 0
assert orient(F5, F6, D5) > 0 and orient(F5, F6, D6) > 0
assert orient(F5, F6, (CAP_A, CAP_B)) == -F(415295, 139314069504)

# Independent full-history verification of each of the four tie policies.
total_nodes = total_terminal_branches = 0
for bits in MASKS:
    exact, nodes, branches = ordered_history_observers(POLICIES[bits])
    assert exact == V[bits]
    total_nodes += nodes
    total_terminal_branches += branches
    print('MASK', bits, 'OBS', tuple(map(str, exact)), 'ORDERED_NODES', nodes,
          'ORDERED_TERMINALS', branches)

print('STATES', len(STATES), 'ACTION_COSTS', action_costs,
      'STRICT_POSITIVE_GAPS', len(strict_gaps), 'MIN_GAP', min(strict_gaps),
      'TIES', TIES)
print('DUAL', 'lambdaP', LAMBDA_P, 'lambdaQ', LAMBDA_Q,
      'thetaP', 0, 'thetaQ', 1, 'H', ROOT_H)
print('TARGET', 'a', CAP_A, 'b', CAP_B,
      'mix_weights_F5_F6_G5', tuple(map(str, WEIGHTS)),
      'tP', T_P, 'tQ', OPTIMUM, 'tQ_minus_tP', GAP_T)
print('R263_AREA', area, 'CORNER_CROSSES', tuple(map(str, corners)),
      'CROSS_F5_F6_TARGET', orient(F5, F6, (CAP_A, CAP_B)))
print('ORDERED_TOTAL_NODES', total_nodes, 'ORDERED_TERMINAL_BRANCHES', total_terminal_branches)
print('STAGE263_EXACT_ALL_REAL_FACE_PASS')
