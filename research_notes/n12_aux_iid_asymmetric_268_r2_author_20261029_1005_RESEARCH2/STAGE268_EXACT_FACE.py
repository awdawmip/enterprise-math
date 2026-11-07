#!/usr/bin/env python3
"""Stage268 portable exact certificate, external IID N=12, full-history policies.
Standard library fractions only; independent count-flow and ordered-path observers.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product

N = 12
P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
LP, LQ = F(203678720, 1502937), F(12317244, 166993)
A, B = F(134248354729, 1761205026816), F(215912422795, 278628139008)
H = F(567931401748091045, 7754824802893824)
V = F(66742910965, 11609505792)
T1, T2 = (0, 0, 5), (3, 3, 5)
NEXT_SWITCH = (4, 4, 0)
STATES = [(i, j, n-i-j) for n in range(N+1) for i in range(n+1) for j in range(n-i+1)]
assert len(STATES) == 455


def child(s, k):
    return tuple(s[t] + int(k == t) for t in range(3))


def pq(s):
    i, j, k = s
    return P[0]**i * P[1]**j * P[2]**k, Q[0]**i * Q[1]**j * Q[2]**k


def bellman():
    values, costs, ties, gaps = {}, {}, {}, []
    actions = 0
    for s in reversed(STATES):
        p, q = pq(s)
        options = {'P': LQ*q, 'Q': LP*p}
        if sum(s) < N:
            options['C'] = q + sum(values[child(s, k)] for k in range(3))
        z = min(options.values())
        values[s], costs[s] = z, options
        best = tuple(a for a, cost in options.items() if cost == z)
        if len(best) > 1:
            ties[s] = best
        gaps.extend(cost-z for cost in options.values() if cost > z)
        actions += len(options)
    assert actions == 1274
    assert ties == {T2: ('Q', 'C'), T1: ('P', 'C')}, ties
    assert len(gaps) == 817
    assert values[(0, 0, 0)] == H
    return values, costs, ties, gaps, actions


def optimal_policy(values, costs, continue_t1=False, continue_t2=False):
    policy = {s: next(a for a, z in costs[s].items() if z == values[s]) for s in STATES}
    policy[T1] = 'C' if continue_t1 else 'P'
    policy[T2] = 'C' if continue_t2 else 'Q'
    assert all(costs[s][d] == values[s] for s, d in policy.items())
    return policy


def count_flow(policy):
    mass = defaultdict(int)
    mass[(0, 0, 0)] = 1
    eP = eQ = tP = tQ = F(0)
    for s in STATES:
        m = mass[s]
        if not m:
            continue
        p, q = pq(s)
        action = policy[s]
        if action == 'P':
            eQ += m*q
        elif action == 'Q':
            eP += m*p
        else:
            assert action == 'C' and sum(s) < N
            tP += m*p
            tQ += m*q
            for k in range(3):
                mass[child(s, k)] += m
    return (eP, eQ, tP, tQ), mass


def ordered_history(policy):
    # Independent recursion: no state multiplicity quotient, weights along each word.
    observations = [F(0)]*4
    terminated = [F(0), F(0)]
    nodes = leaves = 0
    def visit(history, mp, mq):
        nonlocal nodes, leaves
        nodes += 1
        s = (history.count(0), history.count(1), history.count(2))
        a = policy[s]
        if a == 'P':
            observations[1] += mq
            terminated[0] += mp; terminated[1] += mq
            leaves += 1
        elif a == 'Q':
            observations[0] += mp
            terminated[0] += mp; terminated[1] += mq
            leaves += 1
        else:
            assert len(history) < N
            observations[2] += mp; observations[3] += mq
            for k in range(3):
                visit(history+(k,), mp*P[k], mq*Q[k])
    visit((), F(1), F(1))
    assert terminated == [F(1), F(1)]
    return tuple(observations), nodes, leaves


def orient(x, y, z):
    return (y[0]-x[0])*(z[1]-x[1])-(y[1]-x[1])*(z[0]-x[0])


def no_t1_to_t2(policy):
    # Count reachability suffices for all ordered histories; the choices at T1
    # can only alter descendants that pass through the five-neutral prefix.
    frontier = {T1}
    reachable = set()
    while frontier:
        s = frontier.pop()
        if s in reachable:
            continue
        reachable.add(s)
        if s == T1 or policy[s] == 'C':
            assert sum(s) < N
            frontier.update(child(s, k) for k in range(3))
    assert T2 not in reachable
    return len(reachable)


def main():
    val, costs, ties, gaps, actions = bellman()
    observations = {}
    nodes = leaves = 0
    for r, u in product((0, 1), repeat=2):
        pol = optimal_policy(val, costs, r, u)
        o, mass = count_flow(pol)
        other, nn, ll = ordered_history(pol)
        assert o == other
        assert mass[T2] == 21
        assert LP*o[0] + LQ*o[1] + o[3] == H
        assert o[3] > o[2]
        observations[(r,u)] = o
        nodes += nn; leaves += ll
        print('vertex', (r,u), ','.join(map(str, o)), 'ordered_nodes_leaves', nn, ll)
    L5, W, L6, Z = (observations[(0,0)], observations[(0,1)], observations[(1,0)], observations[(1,1)])
    assert L5 == tuple(map(F, ('378878551937/5283615080448','146176716655/185752092672','27566628769787/5944066965504','254184258235/46438023168')))
    assert L6 == tuple(map(F, ('15836509331/195689447424','424845849965/557256278016','10156836789929/1981355655168','280280958235/46438023168')))
    assert W == tuple(map(F, ('378877764437/5283615080448','146176760405/185752092672','27566635857287/5944066965504','254184389485/46438023168')))
    assert Z == tuple(map(F, ('47509440493/587068342272','424845981215/557256278016','10156839152429/1981355655168','280281089485/46438023168')))
    assert tuple(W[i]-L5[i] for i in range(4)) == tuple(Z[i]-L6[i] for i in range(4))
    area = abs(orient(L5,L6,W))
    assert orient(L5,L6,W) < 0
    assert area == F(11415537109375, 7667519984894950244352)
    J5 = tuple(map(F, ('555154589/7739670528','3425906045/4353564672')))
    assert orient(L5,L6,J5) > 0
    assert no_t1_to_t2(optimal_policy(val, costs, True, True)) > 0
    # This mixture is an original full-history randomized policy, including
    # the already published feasible Stage268 exterior witness.
    witness = tuple(F(49,100)*L5[i]+F(49,100)*L6[i]+F(1,50)*W[i] for i in range(4))
    assert witness[:2] == (A,B)
    assert witness[3]-witness[2] == F(5182839518543,5944066965504) > 0
    assert witness[3] == V == H-LP*A-LQ*B
    assert 0 < A < 1 and 0 < B < 1

    # Stage269: strict exterior witness across the opposite W-Z side.
    alternative = optimal_policy(val, costs, False, True)
    base, reach = count_flow(alternative)
    assert base == W and reach[NEXT_SWITCH] == 1 and alternative[NEXT_SWITCH] == 'Q'
    alternative[NEXT_SWITCH] = 'C'
    U, ucount = count_flow(alternative)
    Upath, unn, ull = ordered_history(alternative)
    assert U == Upath
    assert U == tuple(map(F, ('6062044228643/84537841287168', '1754121124943/2229025112064', '441066173811605/95105071448064', '1016737558471/185752092672')))
    external = tuple(F(49,100)*W[i]+F(49,100)*Z[i]+F(1,50)*U[i] for i in range(4))
    assert external[:2] == (F(107398477982417,1408964021452800),F(28788331614361,37150418534400))
    assert orient(W,Z,L5) > 0 and orient(W,Z,external) == F(-499175946875,1472163837099830446915584*50) < 0
    assert 0 < external[0] < 1 and 0 < external[1] < 1
    assert external[3] > external[2]
    excess = LP*(U[0]-W[0]) + LQ*(U[1]-W[1]) + U[3]-W[3]
    assert excess == F(228242371,124077196846301184) > 0
    assert external[3] == F(53394354497531,9287604633600)
    print('STAGE268_EXACT_ALL_REAL_FACE_PASS')
    print('states', len(STATES), 'legal_action_costs', actions, 'strict_positive_gaps', len(gaps), 'ties', ties)
    print('minimum_positive_gap', min(gaps))
    print('lambdaP', LP, 'lambdaQ', LQ, 'thetaP', 0, 'thetaQ', 1, 'H', H)
    print('a268', A, 'b268', B, 'V268', V, 'decimal',format(float(V),'.15f'))
    print('face_R268_vertices', 'L5,L6,Z,W', 'area', area, 'all_real_iff', True)
    print('witness_mix', '49/100 L5 + 49/100 L6 + 1/50 W', 'tP',witness[2],'tQ',witness[3],'delta',witness[3]-witness[2])
    print('ordered_nodes',nodes,'ordered_leaves',leaves,'P_Q_mass_1_each',True)
    print('stage269_switch',NEXT_SWITCH,'Q->C','U_obs',','.join(map(str,U)), 'ordered_nodes_leaves', unn,ull)
    print('stage269_caps',external[0],external[1], 'feasible_tQ_upper',external[3], 'strict_exterior_orient',orient(W,Z,external),'old_support_slack',F(1,50)*excess)

if __name__ == '__main__':
    main()
