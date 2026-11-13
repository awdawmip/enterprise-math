#!/usr/bin/env python3
"""Stage262 finite ternary IID: exact Bellman face and independent ordered-path audit.
Standard-library only; all mathematical calculations use fractions.Fraction.
"""
from fractions import Fraction as F
from itertools import product

P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
N = 12
A = F(6259962086479, 58047528960000)
B = F(25643113985, 34828517376)
LP = F(11983936, 141145)
LQ = F(7680708, 141145)
H = F(22366403903, 411578820)
ROOT = (0, 0, 0)
STATES = [(i, j, n-i-j) for n in range(N+1)
          for i in range(n+1) for j in range(n-i+1)]


def child(s, z):
    return tuple(s[k] + (k == z) for k in range(3))


def ratio(s):
    return F(2, 3)**s[0] * F(2)**s[1]


def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])


def bellman():
    vals = {}
    opt = {}
    counts = {'costs': 0, 'strict_gaps': 0}
    for s in reversed(STATES):
        action = {'P': LQ * ratio(s), 'Q': LP}
        if sum(s) < N:
            action['C'] = ratio(s) + sum(P[z]*vals[child(s, z)] for z in range(3))
        m = min(action.values())
        vals[s] = m
        opt[s] = tuple(key for key in ('P', 'Q', 'C') if key in action and action[key] == m)
        counts['costs'] += len(action)
        counts['strict_gaps'] += sum(v > m for v in action.values())
        assert all(v >= m for v in action.values())
    assert len(STATES) == 455
    assert counts == {'costs': 1274, 'strict_gaps': 817}
    assert vals[ROOT] == H
    ties = sorted(s for s in STATES if len(opt[s]) > 1)
    assert ties == [(0, 0, 5), (0, 1, 6)]
    return opt, ties


def policy(opt, ties, mask):
    choices = dict(zip(ties, mask))
    return {s: opt[s][choices[s]] if s in choices else opt[s][0] for s in STATES}


def dag_observers(pol):
    incoming = {ROOT: F(1)}  # Positive P source mass; Q=P*ratio(count).
    ep = eq = tp = tq = pmend = qmend = F(0)
    for s in STATES:
        pm = incoming.get(s, F(0))
        qm = pm*ratio(s)
        action = pol[s]
        if action == 'P':
            eq += qm; pmend += pm; qmend += qm
        elif action == 'Q':
            ep += pm; pmend += pm; qmend += qm
        else:
            assert sum(s) < N
            tp += pm; tq += qm
            for z in range(3):
                t = child(s, z)
                incoming[t] = incoming.get(t, F(0)) + pm*P[z]
    assert pmend == qmend == 1
    return (ep, eq, tp, tq)


def ordered_observers(pol):
    obs = [F(0) for _ in range(6)]  # eP, eQ, tP, tQ, terminal P, terminal Q
    nodes = terminals = 0

    def walk(s, pm, qm):
        nonlocal nodes, terminals
        nodes += 1
        action = pol[s]
        if action == 'C':
            assert sum(s) < N
            obs[2] += pm; obs[3] += qm
            for z in range(3):
                walk(child(s, z), pm*P[z], qm*Q[z])
        else:
            terminals += 1
            obs[4] += pm; obs[5] += qm
            if action == 'P':
                obs[1] += qm
            else:
                obs[0] += pm

    walk(ROOT, F(1), F(1))
    assert obs[4] == obs[5] == 1
    return tuple(obs[:4]), (nodes, terminals)


def main():
    opt, ties = bellman()
    vectors = {}
    totals = [0, 0]
    for mask in product((0, 1), repeat=len(ties)):
        pol = policy(opt, ties, mask)
        v = dag_observers(pol)
        check, size = ordered_observers(pol)
        assert v == check
        assert v[3] > v[2]
        assert v[3] + LP*v[0] + LQ*v[1] == H
        vectors[mask] = v
        totals = [totals[k] + size[k] for k in range(2)]
        print('POLICY', ''.join(map(str, mask)), 'eP,eQ,tP,tQ', *(str(x) for x in v),
              'ordered_nodes,terminals', *size)
    assert len(vectors) == 4
    assert totals == [2131, 1422]

    order = [(0, 0), (0, 1), (1, 1), (1, 0)]
    vertices = [vectors[k][:2] for k in order]
    turns = [cross(vertices[k], vertices[(k+1) % 4], vertices[(k+2) % 4])
             for k in range(4)]
    assert all(z > 0 for z in turns)
    area = sum(vertices[k][0]*vertices[(k+1) % 4][1]
               - vertices[(k+1) % 4][0]*vertices[k][1] for k in range(4))/2
    assert area == F(75810302734375, 623984373770747904)

    # The exact ordered-source vectors at Stage261 D5 and D6 agree at the full four-observer level.
    assert vectors[0, 0] == (
        F(1166286571, 11609505792), F(3274031045, 4353564672),
        F(2092263019, 483729408), F(1774015963, 362797056))
    assert vectors[1, 0] == (
        F(1786693553, 15479341056), F(4182329935, 5804752896),
        F(3064528817, 644972544), F(2580799409, 483729408))
    d5, d6 = vectors[0, 0][:2], vectors[1, 0][:2]
    assert cross(d5, d6, vectors[0, 1][:2]) < 0
    assert cross(d5, d6, vectors[1, 1][:2]) < 0
    r261_others = (
        (F(23837991977, 139314069504), F(10607552305, 17414258688)),
        (F(25325973227, 139314069504), F(10403158555, 17414258688)),
        (F(1692824803, 15479341056), F(4308598685, 5804752896)),
    )
    assert all(cross(d5, d6, v) > 0 for v in r261_others)
    assert cross(d5, d6, (A, B)) == -F(878615, 278628139008)

    selected = [(0, 0), (0, 1), (1, 0)]
    weights = (F(6390764742101, 13783691406250),
               F(196764774912, 6891845703125),
               F(279975884573, 551347656250))
    assert all(w > 0 for w in weights) and sum(weights) == 1
    mix = tuple(sum(weights[k]*vectors[selected[k]][j] for k in range(3))
                for j in range(4))
    assert mix[0] == A and mix[1] == B
    V = H-LP*A-LQ*B
    assert V == F(1311158074687830583, 256034952345600000)
    assert mix[3] == V and mix[3] > mix[2]
    assert mix[2] == F(1551378313594273399, 341379936460800000)
    assert mix[3]-mix[2] == F(4183622218063, 7255941120000)

    # A precise next candidate on the other side of face edge F5--F6.
    f5, f6 = vectors[0, 1][:2], vectors[1, 1][:2]
    a263 = (f5[0]+f6[0])/2 - F(1, 10000)
    b263 = (f5[1]+f6[1])/2
    assert (a263, b263) == (F(1443791791151, 14511882240000), F(6493321465, 8707129344))
    assert cross(f5, f6, (a263, b263)) == -F(415295, 139314069504)

    print('BELL', 'states=455 costs=1274 strict_gaps=817 ties=2')
    print('DUAL', 'lambdaP', LP, 'lambdaQ', LQ, 'thetaP=0 thetaQ=1', 'H', H)
    print('FACE', 'counterclockwise_masks', *(''.join(map(str, x)) for x in order),
          'area', area, 'strict_turns', *(str(z) for z in turns))
    print('MIX', 'weights', *(str(w) for w in weights),
          'errors', A, B, 'tP', mix[2], 'tQ', mix[3], 'gap', mix[3]-mix[2])
    print('OPTIMUM', V, 'approximately', format(float(V), '.15f'))
    print('ORDERED_AUDIT', 'nodes', totals[0], 'terminal_branches', totals[1])
    print('STAGE263_CANDIDATE', a263, b263, 'signed_cross', cross(f5, f6, (a263, b263)))
    print('STAGE262_EXACT_ALL_REAL_FACE_PASS')


if __name__ == '__main__':
    main()
