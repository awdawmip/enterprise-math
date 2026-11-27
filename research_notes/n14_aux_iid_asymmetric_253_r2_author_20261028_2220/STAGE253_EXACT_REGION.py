#!/usr/bin/env python3
"""Exact two-cap Bellman support polytope of the external ternary IID N=12 model.

All arithmetic is fractions.Fraction. The theorem (including its necessary
condition) is proved in PROOF_STAGE253.md; this file verifies its finite data.
No native-X6/P000 physical transfer is claimed.
"""
from fractions import Fraction as F
from functools import lru_cache

P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
N = 12
K = F(7416207288, 112220771)
A = (1, 0, 1)
B = (0, 0, 12)
O = (0, 0, 0)


def succ(s, z):
    return tuple(v + (i == z) for i, v in enumerate(s))


def L(s):
    return F(2, 3)**s[0] * F(2)**s[1]


@lru_cache(None)
def bell(s):
    costs = {'P': K*L(s), 'Q': K}
    if sum(s) < N:
        costs['C'] = 1 + sum(P[z]*bell(succ(s, z))[0] for z in range(3))
    val = min(costs.values())
    return val, tuple(a for a, cost in costs.items() if cost == val), costs


def policy(s, x, y):
    if s == A:
        return (('P', F(1)-x), ('C', x))
    if s == B:
        return (('P', y), ('Q', F(1)-y))
    return ((bell(s)[1][0], F(1)),)


def observe(x, y):
    @lru_cache(None)
    def tail(s):
        ep = eq = tp = tq = F(0)
        for action, coin in policy(s, x, y):
            if action == 'P':
                eq += coin
            elif action == 'Q':
                ep += coin
            else:
                ch = [tail(succ(s, z)) for z in range(3)]
                ep += coin*sum(P[z]*ch[z][0] for z in range(3))
                eq += coin*sum(Q[z]*ch[z][1] for z in range(3))
                tp += coin*(1 + sum(P[z]*ch[z][2] for z in range(3)))
                tq += coin*(1 + sum(Q[z]*ch[z][3] for z in range(3)))
        return ep, eq, tp, tq
    return tail(O)


def ordered_dfs(x, y):
    """Independently sum unmerged ordered P/Q source-labelled masses and depths."""
    mp = mq = ep = eq = tp = tq = F(0)
    nodes = leaves = 0

    def visit(s, depth, pw, qw):
        nonlocal mp, mq, ep, eq, tp, tq, nodes, leaves
        nodes += 1
        for action, chance in policy(s, x, y):
            if not chance:
                continue
            cp, cq = chance*pw, chance*qw
            if action == 'C':
                assert depth < N
                for z in range(3):
                    visit(succ(s, z), depth+1, cp*P[z], cq*Q[z])
            else:
                leaves += 1
                mp += cp
                mq += cq
                tp += depth*cp
                tq += depth*cq
                if action == 'P':
                    eq += cq
                else:
                    ep += cp

    visit(O, 0, F(1), F(1))
    assert (mp, mq) == (1, 1)
    return (ep, eq, tp, tq), nodes, leaves


def determinant(u, v):
    return u[0]*v[1] - u[1]*v[0]


def inverse(a, b, w, u, v):
    D = determinant(u, v)
    assert D != 0
    da, db = a-w[0], b-w[1]
    return ((da*v[1] - db*v[0])/D,
            (db*u[0] - da*u[1])/D)


def verify():
    states = [(i, j, n-i-j) for n in range(N+1)
              for i in range(n+1) for j in range(n-i+1)]
    assert len(states) == 455
    ties = []
    gaps = 0
    for s in states:
        h, acts, all_costs = bell(s)
        if len(acts) > 1:
            ties.append((s, acts))
        gaps += sum(cost > h for cost in all_costs.values())
        assert all(cost >= h for cost in all_costs.values())
    assert ties == [(A, ('P', 'C')), (B, ('P', 'Q'))], ties
    assert gaps == 817
    H = bell(O)[0]
    assert H == F(710830290256337191, 12527189335646208)
    w = observe(F(0), F(0))
    w10 = observe(F(1), F(0))
    w01 = observe(F(0), F(1))
    w11 = observe(F(1), F(1))
    u = tuple(w10[i]-w[i] for i in range(4))
    v = tuple(w01[i]-w[i] for i in range(4))
    assert w11 == tuple(w[i]+u[i]+v[i] for i in range(4))
    assert w == (F(62539020775, 185752092672), F(15285594535, 34828517376),
                 F(127456938773, 23219011584), F(15831662545, 2902376448))
    assert u == (F(68552185, 15479341056), -F(73629595, 8707129344),
                 F(171671465, 644972544), F(150969055, 725594112))
    assert v == (-F(244140625, 2176782336), F(244140625, 2176782336), 0, 0)
    D = determinant(u, v)
    assert D == -F(136988245849609375, 303256405652583481344)
    dt0 = w[2]-w[3]
    dt1 = dt0+u[2]-u[3]
    assert dt0 == F(89293157, 2579890176) > 0
    assert dt1 == F(2152801393, 23219011584) > 0
    assert v[2] == v[3] == 0

    corners = [(F(0), F(0)), (F(1), F(0)),
               (F(1), F(1)), (F(0), F(1))]
    target_a, target_b = F(3, 10), F(19, 40)
    target_x, target_y = inverse(target_a, target_b, w, u, v)
    assert (target_x, target_y) == (
        F(1564797113, 11222077100),
        F(1121360544147507, 3372018359375000))
    assert 0 < target_x < 1 and 0 < target_y < 1
    total_nodes = total_leaves = 0
    for x, y in corners + [(target_x, target_y)]:
        vec = tuple(w[i]+x*u[i]+y*v[i] for i in range(4))
        a, b, tp, tq = vec
        assert inverse(a, b, w, u, v) == (x, y)
        assert 0 < a < 1 and 0 < b < 1
        assert tp > tq
        assert tp == H-K*(a+b)
        assert observe(x, y) == vec
        dfs, nodes, leaves = ordered_dfs(x, y)
        assert dfs == vec
        total_nodes += nodes
        total_leaves += leaves
        print('witness (x,y)=', x, y, 'caps(a,b)=', a, b, 'V=', tp,
              'ordered_DFS_nodes=', nodes, 'leaves=', leaves)

    # Exact outside witness: x=-1/100 at y=1/2 lies in [0,1]^2 cap space,
    # but strictly outside the Bellman supporting parallelogram.
    xx, yy = -F(1, 100), F(1, 2)
    aout = w[0]+xx*u[0]+yy*v[0]
    bout = w[1]+xx*u[1]+yy*v[1]
    assert 0 < aout < 1 and 0 < bout < 1
    assert inverse(aout, bout, w, u, v) == (xx, yy)
    assert xx < 0
    # Explicitly feasible outside point: preserve its P-error cap by changing
    # only y at x=0; Q-error has strictly positive slack.
    feasible_y = yy + F(1, 100)*u[0]/(-v[0])
    assert feasible_y == F(156373393933, 312500000000)
    assert F(0) < feasible_y < F(1)
    outside_feasible = observe(F(0), feasible_y)
    assert outside_feasible[0] == aout
    assert bout - outside_feasible[1] == F(112220771, 2786281390080) > 0
    print('outside_feasible_coin_y=', feasible_y,
          'Q_error_slack=', bout-outside_feasible[1])
    print('STAGE253_EXACT_AUTHOR_PASS states=455 ties=2 gaps=817',
          'DFS_nodes=', total_nodes, 'terminal_branches=', total_leaves)
    print('H=', H, 'K=', K, 'w00=', w, 'u=', u, 'v=', v)
    print('D=', D, 'area=', -D, 'dt_at_x0=', dt0, 'dt_at_x1=', dt1)
    print('outside_witness_caps=', aout, bout, 'inverse_coins=', xx, yy)

if __name__ == '__main__':
    verify()
