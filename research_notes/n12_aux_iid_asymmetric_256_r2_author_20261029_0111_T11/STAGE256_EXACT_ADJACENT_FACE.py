#!/usr/bin/env python3
"""Stage256: finite exact Bellman and ordered-history certificate.

External ternary IID model, NOT P000-native spatial or heartbeat arithmetic.
Requires only Python 3 standard library; all proof-relevant arithmetic is Fraction.
"""
from fractions import Fraction as F
from itertools import combinations

N = 12
P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
LAMBDA_P = F(23219011584, 292565255)
LAMBDA_Q = F(15120288852, 292565255)
STATES = tuple((i, j, d-i-j) for d in range(N+1)
               for i in range(d+1) for j in range(d-i+1))
assert len(STATES) == 455

def child(s, z):
    return tuple(s[k] + (k == z) for k in range(3))

def likelihood(s):
    return F(2, 3)**s[0] * F(2, 1)**s[1]

H, optimal, evaluated = {}, {}, 0
strict_action_gaps = 0
for s in reversed(STATES):
    costs = {'P': LAMBDA_Q * likelihood(s), 'Q': LAMBDA_P}
    if sum(s) < N:
        costs['C'] = (likelihood(s) +
                      sum(P[z]*H[child(s, z)] for z in range(3)))
    evaluated += len(costs)
    H[s] = min(costs.values())
    optimal[s] = tuple(a for a in ('P', 'Q', 'C')
                       if a in costs and costs[a] == H[s])
    strict_action_gaps += sum(v > H[s] for v in costs.values())
assert evaluated == 1274
assert strict_action_gaps == 806
assert H[(0, 0, 0)] == LAMBDA_Q
expected_ties = {(0, 0, k) for k in range(N)} | {(0, 1, 0)}
assert {s for s in STATES if len(optimal[s]) > 1} == expected_ties
assert all(optimal[(0, 0, k)] == ('P', 'C') for k in range(N))
assert optimal[(0, 1, 0)] == ('Q', 'C')
assert optimal[(0, 0, N)] == ('P',)

# A is root-stop-P. B_k stops P after k neutrals, Q after first symbol 1.
# C_k is B_k except a first-position symbol 1 is followed by continue.
def action(s, stop_depth, special_continue):
    if stop_depth == 0 and s == (0, 0, 0):
        return 'P'
    if s == (0, 1, 0):
        return 'C' if special_continue else 'Q'
    if s[0] == 0 and s[1] == 0:
        return 'P' if sum(s) >= stop_depth else 'C'
    return optimal[s][0]

# Four-observer dynamic recursion conditioned on an arbitrary reached history.
def count_dp(stop_depth, special_continue):
    obs = {}
    for s in reversed(STATES):
        a = action(s, stop_depth, special_continue)
        if a == 'P':
            obs[s] = (F(0), F(1), F(0), F(0))
        elif a == 'Q':
            obs[s] = (F(1), F(0), F(0), F(0))
        else:
            successors = [obs[child(s, z)] for z in range(3)]
            obs[s] = (
                sum(P[z]*successors[z][0] for z in range(3)),
                sum(Q[z]*successors[z][1] for z in range(3)),
                1 + sum(P[z]*successors[z][2] for z in range(3)),
                1 + sum(Q[z]*successors[z][3] for z in range(3)),
            )
    return obs[(0, 0, 0)]

# This DFS does not merge complete histories, and propagates typed P/Q masses.
def ordered_dfs(stop_depth, special_continue):
    obs = [F(0)]*4
    mass = [F(0), F(0)]
    nodes = terminals = 0
    def go(history, pm, qm):
        nonlocal nodes, terminals
        nodes += 1
        s = (history.count(0), history.count(1), history.count(2))
        a = action(s, stop_depth, special_continue)
        if a == 'C':
            obs[2] += pm
            obs[3] += qm
            for z in range(3):
                go(history + (z,), pm*P[z], qm*Q[z])
        else:
            terminals += 1
            mass[0] += pm
            mass[1] += qm
            if a == 'P': obs[1] += qm
            else: obs[0] += pm
    go((), F(1), F(1))
    assert tuple(mass) == (F(1), F(1))
    return tuple(obs), nodes, terminals

A = (F(0), F(1), F(0), F(0))
assert count_dp(0, False) == A
B, C = {}, {}
ordered_nodes = ordered_terminals = 0
for k in range(1, N+1):
    B[k] = count_dp(k, False)
    C[k] = count_dp(k, True)
    for mark, v in [(False, B[k]), (True, C[k])]:
        dfs, nn, nt = ordered_dfs(k, mark)
        assert v == dfs, (k, mark)
        ordered_nodes += nn
        ordered_terminals += nt
    r = F(5, 6)**k
    assert B[k] == ((1-r)/4, (1+r)/2, 6*(1-r), 6*(1-r))

D = tuple(C[1][i]-B[1][i] for i in range(4))
assert all(tuple(C[k][i]-B[k][i] for i in range(4)) == D
           for k in range(1, N+1))
assert D[3] > D[2]
assert 2*D[0] + D[1] < 0

# Full exact error-contact quadrilateral for this Bellman support.
# Convex hull in (eP,eQ): A, B_12, C_12, C_1 (cyclic order).
VERTICES = (A, B[N], C[N], C[1])
def cross(o, u, v):
    return (u[0]-o[0])*(v[1]-o[1])-(u[1]-o[1])*(v[0]-o[0])
turns = [cross(VERTICES[k], VERTICES[(k+1)%4], VERTICES[(k+2)%4]) for k in range(4)]
assert all(t > 0 for t in turns) or all(t < 0 for t in turns)
area2 = sum(VERTICES[k][0]*VERTICES[(k+1)%4][1] -
            VERTICES[k][1]*VERTICES[(k+1)%4][0] for k in range(4))
AREA = abs(area2)/2
assert AREA > 0
# The old C_12 face occupies 2a+b>=1. Our face occupies 2a+b<=1,
# with the full A--B_12 side shared.
assert 2*A[0]+A[1] == 1
assert 2*B[N][0]+B[N][1] == 1
assert 2*C[1][0]+C[1][1] < 1
assert 2*C[N][0]+C[N][1] < 1

# For each Bellman-minimizing deterministic policy, tQ>=tP;
# no other tie state can enter after a nonneutral event except (0,1,0).
for v in (A, *B.values(), *C.values()):
    ep, eq, tp, tq = v
    assert tq >= tp
    assert tq + LAMBDA_P*ep + LAMBDA_Q*eq == H[(0, 0, 0)]

# Representative strict-interior rational point: average of all 4 vertices.
POINT = tuple(sum(v[i] for v in VERTICES)/4 for i in range(4))
a, b, tp, tq = POINT
assert 2*a+b < 1 and tq > tp
VALUE = H[(0,0,0)] - LAMBDA_P*a - LAMBDA_Q*b
assert VALUE == tq

if __name__ == '__main__':
    print('STAGE256_EXACT_BELLMAN_PASS')
    print('states', len(STATES), 'action_costs', evaluated,
          'strict_gaps', strict_action_gaps, 'tie_states', len(expected_ties))
    print('dual', 'lambdaP', LAMBDA_P, 'lambdaQ', LAMBDA_Q,
          'thetaP=0', 'thetaQ=1', 'root', H[(0,0,0)])
    for label,v in zip(('A','B12','C12','C1'),VERTICES):
        print(label, *(str(x) for x in v))
    print('DELTA',*(str(x) for x in D))
    print('AREA',AREA,'turns',*(str(x) for x in turns))
    print('POINT CAPS',a,b,'V12',VALUE,'tP',tp,'tQ',tq)
    print('strict exterior gap 1-2a-b',1-2*a-b)
    print('ordered_history_nodes',ordered_nodes, 'terminal_branches',ordered_terminals)
    print('STAGE256_EXACT_ALL_REAL_FACE_PASS')
