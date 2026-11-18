#!/usr/bin/env python3
"""Stage270: self-contained exact external-IID Bellman, face and ordered-word test.

Uses Python stdlib Fraction only. No native Heartbeat/BRC arithmetic claim.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product

P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
N = 12
LP, LQ = F(134304895492096, 947487230457), F(48948392988, 643236409)
H = F(34613913912513106850567, 458327437076524179456)
A, B = F(402360299687, 5283615080448), F(431878115465, 557256278016)
OPT = F(267107458235, 46438023168)
T, U = (0, 0, 5), (1, 2, 2)
STATES = [(i, j, n-i-j) for n in range(N+1)
          for i in range(n+1) for j in range(n-i+1)]


def next_state(s, k):
    return tuple(s[t] + int(t == k) for t in range(3))


def likelihood(s):
    i, j, k = s
    return P[0]**i * P[1]**j * P[2]**k, Q[0]**i * Q[1]**j * Q[2]**k


def bellman(lp=LP, lq=LQ):
    values, costs, ties, gaps = {}, {}, {}, []
    for s in reversed(STATES):
        p, q = likelihood(s)
        options = {'P': lq*q, 'Q': lp*p}
        if sum(s) < N:
            options['C'] = q + sum(values[next_state(s, k)] for k in range(3))
        v = min(options.values())
        values[s], costs[s] = v, options
        best = tuple(k for k, cost in options.items() if cost == v)
        if len(best) > 1:
            ties[s] = best
        gaps.extend(cost-v for cost in options.values() if cost > v)
    return values, costs, ties, gaps


def optimal_policy(values, costs, r, u):
    policy = {s: next(a for a, c in costs[s].items() if c == values[s])
              for s in STATES}
    policy[T] = 'C' if r else 'P'
    policy[U] = 'C' if u else 'Q'
    assert all(costs[s][a] == values[s] for s, a in policy.items())
    return policy


def count_flow(policy):
    arrived = defaultdict(int)
    arrived[(0, 0, 0)] = 1
    o, ended = [F(0)]*4, [F(0)]*2
    for s in STATES:
        multiplicity = arrived[s]
        if not multiplicity:
            continue
        p, q = likelihood(s)
        a = policy[s]
        if a == 'P':
            o[1] += multiplicity*q
            ended[0] += multiplicity*p
            ended[1] += multiplicity*q
        elif a == 'Q':
            o[0] += multiplicity*p
            ended[0] += multiplicity*p
            ended[1] += multiplicity*q
        else:
            assert a == 'C' and sum(s) < N
            o[2] += multiplicity*p
            o[3] += multiplicity*q
            for k in range(3):
                arrived[next_state(s, k)] += multiplicity
    assert ended == [1, 1]
    return tuple(o), arrived


def ordered_word_flow(policy):
    # Independent from count_flow: never merges histories or uses binomial counts.
    o, ended = [F(0)]*4, [F(0)]*2
    nodes = leaves = 0
    def walk(word, p, q):
        nonlocal nodes, leaves
        nodes += 1
        state = (word.count(0), word.count(1), word.count(2))
        action = policy[state]
        if action == 'P':
            o[1] += q
            ended[0] += p
            ended[1] += q
            leaves += 1
        elif action == 'Q':
            o[0] += p
            ended[0] += p
            ended[1] += q
            leaves += 1
        else:
            assert action == 'C' and len(word) < N
            o[2] += p
            o[3] += q
            for k in range(3):
                walk(word+(k,), p*P[k], q*Q[k])
    walk((), F(1), F(1))
    assert ended == [1, 1]
    return tuple(o), nodes, leaves


def orient(x, y, z):
    return (y[0]-x[0])*(z[1]-x[1])-(y[1]-x[1])*(z[0]-x[0])


def main():
    values, costs, ties, gaps = bellman()
    assert len(STATES) == 455
    assert sum(len(x) for x in costs.values()) == 1274
    assert ties == {U: ('Q', 'C'), T: ('P', 'C')}
    assert len(gaps) == 817
    assert min(gaps) == F(89351863, 1931388047598192427008)
    assert values[(0, 0, 0)] == H
    corners = {}
    nodes = leaves = 0
    for r, u in product((0, 1), repeat=2):
        policy = optimal_policy(values, costs, r, u)
        by_counts, arrived = count_flow(policy)
        by_words, n, l = ordered_word_flow(policy)
        assert by_counts == by_words
        assert arrived[T] == 1 and arrived[U] == 10
        assert LP*by_counts[0]+LQ*by_counts[1]+by_counts[3] == H
        assert by_counts[3] > by_counts[2]
        corners[r,u] = by_counts
        nodes += n
        leaves += l
        print('corner', r, u, ','.join(map(str, by_counts)),
              'ordered_nodes_leaves', n, l)
    C, D, E, F_corner = [corners[k] for k in ((0,0),(1,0),(0,1),(1,1))]
    assert C[:2] == (F(1135528662191,15850845241344),
                     F(146193716605,185752092672))
    assert D[:2] == (F(1281650262191,15850845241344),
                     F(424896849815,557256278016))
    assert all(F_corner[i]-D[i] == E[i]-C[i] for i in range(4))
    area = abs(orient(C,D,E))
    assert orient(C,D,E) == -area
    assert area == F(123370733132421875,69007679864054552199168)
    prior_W = (F(378877764437,5283615080448),
               F(146176760405,185752092672))
    assert orient(C,D,prior_W) == F(15006059401671875,17251919966013638049792)>0
    x = tuple(D[i]-C[i] for i in range(4))
    y = tuple(E[i]-C[i] for i in range(4))
    det = orient(C,D,E)
    r = ((A-C[0])*y[1]-(B-C[1])*y[0])/det
    u = (x[0]*(B-C[1])-x[1]*(A-C[0]))/det
    assert (r,u) == (F(49,100), F(1,50))
    witness = tuple(C[i]+r*x[i]+u*y[i] for i in range(4))
    assert witness[:2] == (A,B)
    assert witness[2] == F(3221924873893,660451885056)
    assert witness[3] == OPT == H-LP*A-LQ*B
    assert witness[3] > witness[2]
    assert orient(C,D,witness) == F(-4934829325296875,138015359728109104398336)
    print('STAGE270_EXACT_ALL_REAL_FACE_PASS')
    print('bellman_states',len(STATES),'legal_actions',sum(len(x) for x in costs.values()),
          'positive_gaps',len(gaps),'minimum_gap',min(gaps),'ties',ties)
    print('lambdaP',LP,'lambdaQ',LQ,'thetaP',0,'thetaQ',1,'root_H',H)
    print('R270_vertices', 'C,D,F,E', 'area',area,'old_side',orient(C,D,prior_W))
    print('caps',A,B,'exact_optimum',OPT,'decimal',format(float(OPT),'.15f'))
    print('r,u',r,u,'tP',witness[2],'tQ',witness[3],
          'tQ_minus_tP',witness[3]-witness[2])
    print('total_ordered_nodes',nodes,'total_ordered_terminal_leaves',leaves,
          'each_policy_P_Q_terminal_mass_exactly_one',True)
    # A strict-exterior Stage271 witness, deliberately only a feasible bound.
    policy = optimal_policy(values, costs, 0, 1)
    E_original, reached = count_flow(policy)
    switch = (1,2,3)
    assert policy[switch] == 'Q' and reached[switch] == 20
    policy[switch] = 'C'
    changed, _ = count_flow(policy)
    changed_words, n, l = ordered_word_flow(policy)
    assert changed == changed_words
    future = tuple(F(49,100)*E[i]+F(49,100)*F_corner[i]
                   +F(1,50)*changed[i] for i in range(4))
    assert future[:2] == (F(133853268599,1761205026816),
                          F(431993556815,557256278016))
    assert future[3] == F(89124381535,15479341056) > future[2]
    assert orient(E,F_corner,future) == F(-4050750660078125,69007679864054552199168)<0
    assert orient(E,F_corner,C) > 0
    print('STAGE271_EXTERIOR_FEASIBLE_WITNESS_PASS',
          'state_Q_to_C',switch,'reached_histories',reached[switch],
          'caps',future[:2], 'tQ_upper',future[3],
          'side',orient(E,F_corner,future), 'ordered_nodes_leaves',n,l)

if __name__ == '__main__':
    main()
