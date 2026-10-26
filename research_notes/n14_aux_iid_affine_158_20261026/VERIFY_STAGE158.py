#!/usr/bin/env python3
"""Exact Stage158 author checker for the external iid ternary N=14 model.

All arithmetic uses fractions.Fraction, integers, finite Bellman DP and
unmerged ordered integer-weight DFS; no floats enter certificates.
"""
import json
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

N = 14
P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
K0 = F(3342600, 10529)
J, T, U = (10, 2, 0), (14, 0, 0), (6, 1, 2)
S = [(n, a, b) for n in range(N + 1)
     for a in range(n + 1) for b in range(n - a + 1)]
assert len(S) == 680

def child(s, i):
    n, a, b = s
    return ((n + 1, a + 1, b), (n + 1, a, b + 1), (n + 1, a, b))[i]

def likelihood(s):
    n, a, b = s
    return F(2**(a + b), 3**a)

@lru_cache(None)
def old_bellman(s):
    vals = {'P': K0 * likelihood(s), 'Q': K0}
    if s[0] < N:
        vals['C'] = 1 + sum(P[i] * old_bellman(child(s, i))[0] for i in range(3))
    m = min(vals.values())
    return (m, tuple(a for a, v in vals.items() if v == m))

assert [(s, old_bellman(s)[1]) for s in S if len(old_bellman(s)[1]) > 1] == [
    (J, ('P', 'C')), (T, ('P', 'Q'))]

# At Stage157 ties use J->P and T->Q; U is then a strict continue.
@lru_cache(None)
def old_aff(s):
    act = 'P' if s == J else 'Q' if s == T else old_bellman(s)[1][0]
    if act == 'P':
        return F(0), likelihood(s), F(0)
    if act == 'Q':
        return F(0), F(0), F(1)
    kids = [old_aff(child(s, i)) for i in range(3)]
    return tuple((F(1) if z == 0 else F(0)) + sum(P[i] * kids[i][z] for i in range(3))
                 for z in range(3))

def affine_actions(s):
    choices = {'P': (F(0), likelihood(s), F(0)), 'Q': (F(0), F(0), F(1))}
    if s[0] < N:
        kids = [old_aff(child(s, i)) for i in range(3)]
        choices['C'] = tuple((F(1) if z == 0 else F(0)) +
                             sum(P[i] * kids[i][z] for i in range(3)) for z in range(3))
    return choices

def ae(v, k, l):
    return v[0] + v[1] * k + v[2] * l

def minus(x, y):
    return tuple(x[i] - y[i] for i in range(len(x)))

jdiff = minus(affine_actions(J)['P'], affine_actions(J)['C'])
assert jdiff == (F(-15475, 13824), F(395, 46656), F(-1639, 331776))
s = jdiff[1] / (-jdiff[2])
assert s == F(25280, 14751)
# K=K0-epsilon, L=K0-s*epsilon: T chooses Q strictly for epsilon>0.
closures = []
for state in S:
    current = 'P' if state == J else 'Q' if state == T else old_bellman(state)[1][0]
    for act, val in affine_actions(state).items():
        if act == current:
            continue
        gap = minus(val, old_aff(state))
        gap0 = ae(gap, K0, K0)
        derivative = -(gap[1] + s * gap[2])
        assert gap0 >= 0, (state, act)
        if gap0 > 0 and derivative < 0:
            closures.append((gap0 / (-derivative), state, current, act))
        elif gap0 == 0 and state != J and state != T:
            raise AssertionError(('unexpected prior tie', state, act))
first = min(closures)
assert first == (F(6147978656669784, 910876079964721), U, 'C', 'Q')
epsilon = first[0]
K = K0 - epsilon
L = K0 - s * epsilon
assert (K, L) == (F(26880449139504, 86511167249), F(26463665283720, 86511167249))
assert 0 < L < K

@lru_cache(None)
def new_bellman(state):
    choices = {'P': K * likelihood(state), 'Q': L}
    if state[0] < N:
        choices['C'] = F(1) + sum(P[i] * new_bellman(child(state, i))[0]
                                for i in range(3))
    m = min(choices.values())
    return m, tuple(a for a, v in choices.items() if v == m), choices

new_ties = [(state, new_bellman(state)[1]) for state in S
            if len(new_bellman(state)[1]) > 1]
assert new_ties == [(U, ('Q', 'C')), (J, ('P', 'C'))]
strict_gaps = [v - new_bellman(state)[0] for state in S
               for v in new_bellman(state)[2].values() if v > new_bellman(state)[0]]
assert len(strict_gaps) == 1238
assert all(v > 0 for v in strict_gaps)
root = new_bellman((0, 0, 0))[0]
assert root == F(67118306721229522289887399231, 296195426721776135565213696)

def action(state, j, u):
    if state == J:
        return 'P' if j else 'C'
    if state == U:
        return 'Q' if u else 'C'
    if state == T:
        return 'Q'
    return old_bellman(state)[1][0]

def suffix_dp(j, u):
    @lru_cache(None)
    def go(state):
        a = action(state, j, u)
        if a == 'P':
            return F(0), F(1), F(0), F(0)
        if a == 'Q':
            return F(1), F(0), F(0), F(0)
        kids = [go(child(state, i)) for i in range(3)]
        return (sum(P[i] * kids[i][0] for i in range(3)),
                sum(Q[i] * kids[i][1] for i in range(3)),
                F(1) + sum(P[i] * kids[i][2] for i in range(3)),
                F(1) + sum(Q[i] * kids[i][3] for i in range(3)))
    return go((0, 0, 0))

# Independent ordered-path enumeration: retain each prefix and multiply integer weights.
PW, QW = (3, 1, 20), (1, 1, 10)
PPOW, QPOW = [24**i for i in range(N + 1)], [12**i for i in range(N + 1)]
def ordered_dfs(j, u, first_hit=False):
    stack = [(0, 0, 0, 1, 1)]
    ep = eq = tp = tq = nodes = leaves = 0
    hits = defaultdict(lambda: [0, F(0), F(0)])
    while stack:
        n, a, b, pn, qn = stack.pop()
        state = n, a, b
        nodes += 1
        if first_hit and state in (J, U):
            hits[state][0] += 1
            hits[state][1] += F(pn, PPOW[n])
            hits[state][2] += F(qn, QPOW[n])
        act = action(state, j, u)
        if act == 'C':
            assert n < N
            for i in (0, 1, 2):
                dest = child(state, i)
                stack.append((*dest, pn * PW[i], qn * QW[i]))
        else:
            leaves += 1
            pscaled = pn * PPOW[N - n]
            qscaled = qn * QPOW[N - n]
            if act == 'Q':
                ep += pscaled
            else:
                eq += qscaled
            tp += n * pscaled
            tq += n * qscaled
    return ((F(ep, PPOW[N]), F(eq, QPOW[N]),
             F(tp, PPOW[N]), F(tq, QPOW[N])), nodes, leaves, hits)

corners = {}
nodes = {}
for j in (0, 1):
    for u in (0, 1):
        key = str(j) + str(u)
        dp, dfs = suffix_dp(j, u), ordered_dfs(j, u)
        assert dp == dfs[0]
        corners[key] = dp
        nodes[key] = {'ordered_visited_nodes': dfs[1], 'ordered_stopping_prefixes': dfs[2]}
B = corners['00']
dJ = minus(corners['10'], B)
dU = minus(corners['01'], B)
mixed = minus(minus(corners['11'], corners['10']), dU)
assert mixed == (F(0),) * 4
assert B == tuple(F(t) for t in (
    '1220395842171464035/3505953353861431296',
    '223259694920365/641959232274432',
    '5285134543382516317/438244169232678912',
    '619867204468061/53496602689536'))

def vec(j,u):
    return tuple(B[i] + j*dJ[i] + u*dU[i] for i in range(4))

j0 = (B[1] - B[0]) / (dJ[0] - dJ[1])
beta = -(dU[0] - dU[1]) / (dJ[0] - dJ[1])
j1 = j0 + beta
assert (j0, beta, j1) == (
    F(660136987826389, 4611571200000000),
    F(5885193739, 72055800000),
    F(1036789387122389, 4611571200000000))
assert 0 < j0 < j1 < 1
start, end = vec(j0, 0), vec(j1, 1)
alpha157 = F(763084945158127578305, 2192919042319171190784)
V157 = F(3298586218925748578843, 274114880289896398848)
alpha158 = F(763167995878686618305, 2192919042319171190784)
V158 = F(3292184925194961698843, 274114880289896398848)
assert start[0] == start[1] == alpha157 and start[2] == V157
assert end[0] == end[1] == alpha158 and end[2] == V158
assert start[2] >= start[3] and end[2] >= end[3]
width = alpha158 - alpha157
assert width == F(54069479530625, 1427681668176543744) > 0
assert K + L == F(53344114423224, 86511167249)
assert V158 == V157 - (K + L) * width
assert root == V157 + (K + L) * alpha157
assert root == V158 + (K + L) * alpha158
hit_info = ordered_dfs(0, 0, first_hit=True)[3]
assert hit_info[J] == [45, F(1953125, 11943936), F(1953125, 26873856)]
assert hit_info[U] == [40, F(625, 124416), F(625, 46656)]

cert = {
    'schema':'EM_STAGE158_AUTHOR_EXACT_V1', 'scope':'external iid ternary N14 author-level',
    'P':[str(x) for x in P], 'Q':[str(x) for x in Q], 'N':N,
    'global_main_at_research_start':'a511c0782dae1f31e85e1d1c545039355fd018fc',
    'em_main_at_research_start':'4f1ceac47ab3b65fa69d0b4695b253bdda2f44e0',
    'old_KL':str(K0), 'offdiagonal_ray_dL_over_dK':str(s),
    'first_closure_epsilon':str(epsilon), 'first_closure_state':str(U),
    'K158':str(K), 'L158':str(L), 'root_dual_value':str(root),
    'bellman_states':len(S), 'strict_gaps':len(strict_gaps),
    'minimum_strict_gap':str(min(strict_gaps)),
    'ties':[str((state, acts)) for state, acts in new_ties],
    'first_hit':{str(state):[str(y) for y in hit_info[state]] for state in (J, U)},
    'corners':{key:[str(t) for t in val] for key,val in corners.items()},
    'dfs_coverage':nodes,
    'B':[str(x) for x in B], 'dJ':[str(x) for x in dJ],
    'dU':[str(x) for x in dU], 'mixed_cross_term':[str(x) for x in mixed],
    'j0':str(j0), 'dj_du':str(beta), 'j1':str(j1),
    'alpha157':str(alpha157), 'alpha158':str(alpha158),
    'interval_width':str(width), 'V157':str(V157), 'V158':str(V158),
    'slope':str(K+L), 'time_gap_start':str(start[2]-start[3]),
    'time_gap_end':str(end[2]-end[3]), 'dual_equalities':'EXACT_ZERO_BOTH_ENDPOINTS',
    'right_sharpness':'PROVED_ANALYTICALLY_VIA_TIE_SUPPORT_AND_FIRST_HIT_FIBERS',
    'native_claim':'NOT_OBTAINED', 'independent_driver_review':'NOT_OBTAINED',
}
if __name__ == '__main__':
    Path('certificate158.json').write_text(json.dumps(cert,indent=2,ensure_ascii=False)+'\n')
    print('STAGE158_AUTHOR_EXACT_PASS', 'states',len(S),'strict',len(strict_gaps),
          'corners',len(corners),'ordered_nodes',sum(x['ordered_visited_nodes'] for x in nodes.values()))
    print('alpha158',alpha158,'V158',V158,'width',width)
    print('K158',K,'L158',L,'j0',j0,'j1',j1)
