#!/usr/bin/env python3
"""Stage256: rational Bellman certificate and independent ordered-source DFS.
External ternary-IID, horizon N=12; author-side research only, not native X6.
"""
from fractions import Fraction as F
from functools import lru_cache

P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
N = 12
ROOT = (0, 0, 0)
A = (0, 0, 8)  # stop P / continue
B = (0, 1, 2)  # stop Q / continue
CAP_A = F(6788660051, 34828517376)
CAP_B = F(572868317, 967458816)
K_P = F(644972544, 8007455)
K_Q = F(418575732, 8007455)
THETA_P = F(0)
THETA_Q = F(1)


def l(s):
    return F(2, 3) ** s[0] * F(2) ** s[1]


def succ(s, z):
    return tuple(s[i] + int(i == z) for i in range(3))


@lru_cache(None)
def bell(s):
    costs = {'P': K_Q * l(s), 'Q': K_P}
    if sum(s) < N:
        costs['C'] = l(s) + sum(P[z] * bell(succ(s, z))[0] for z in range(3))
    value = min(costs.values())
    minimizers = tuple(a for a, c in costs.items() if c == value)
    return value, minimizers, costs


def policy(s, x, y):
    if s == A:
        actions = (('P', 1-x), ('C', x))
    elif s == B:
        actions = (('Q', 1-y), ('C', y))
    elif s[0] == s[1] == 0:
        actions = ((('C' if sum(s) < N else 'P'), F(1)),)
    else:
        actions = ((bell(s)[1][0], F(1)),)
    assert all(c >= 0 and a in bell(s)[1] for a, c in actions)
    assert sum(c for _, c in actions) == 1
    return actions


def suffix_observers(x, y):
    @lru_cache(None)
    def tail(s):
        ep = eq = tp = tq = F(0)
        for action, coin in policy(s, x, y):
            if not coin:
                continue
            if action == 'P':
                eq += coin
            elif action == 'Q':
                ep += coin
            else:
                branches = [tail(succ(s, z)) for z in range(3)]
                ep += coin * sum(P[z] * branches[z][0] for z in range(3))
                eq += coin * sum(Q[z] * branches[z][1] for z in range(3))
                tp += coin * (1 + sum(P[z] * branches[z][2] for z in range(3)))
                tq += coin * (1 + sum(Q[z] * branches[z][3] for z in range(3)))
        return (ep, eq, tp, tq)
    return tail(ROOT)


def ordered_dfs(x, y):
    totalp = totalq = ep = eq = tp = tq = F(0)
    nodes = decisions = 0

    def walk(history, wp, wq):
        nonlocal totalp, totalq, ep, eq, tp, tq, nodes, decisions
        nodes += 1
        assert wp >= 0 and wq >= 0
        s = tuple(history.count(i) for i in range(3))
        depth = len(history)
        for action, coin in policy(s, x, y):
            if coin == 0:
                continue
            a = coin * wp
            b = coin * wq
            if action == 'C':
                assert depth < N
                for z in range(3):
                    walk(history + (z,), a * P[z], b * Q[z])
            else:
                decisions += 1
                totalp += a
                totalq += b
                tp += depth*a
                tq += depth*b
                if action == 'P':
                    eq += b
                else:
                    ep += a
    walk((), F(1), F(1))
    assert (totalp,totalq) == (1,1)
    return (ep,eq,tp,tq), nodes,decisions


def vec_add(u,v):
    return tuple(u[i]+v[i] for i in range(4))


def main():
    states = [(i,j,n-i-j) for n in range(N+1) for i in range(n+1) for j in range(n-i+1)]
    assert len(states)==455
    ties=[]
    positive_gaps=0
    for s in states:
        value,acts,costs=bell(s)
        assert value>=0 and len(acts)>=1
        ties += [(s,acts)] if len(acts)>1 else []
        positive_gaps+=sum(v>value for v in costs.values())
    expected = {(0,0,k):('P','C') for k in range(2,12)}
    expected[B]=('Q','C')
    assert dict(ties)==expected and len(ties)==11,ties
    assert positive_gaps==808,positive_gaps
    H=bell(ROOT)[0]
    assert H==F(30134718329,576536760)
    assert K_Q==12+K_P/2
    assert (F(-4648223,1679616)+F(5429473,53747712)*K_P
            -F(2070241,20155392)*K_Q)==0
    print('DUAL_THETA',(THETA_P,THETA_Q),'K_P',K_P,'K_Q',K_Q,'H',H)
    print('TIES',ties,'STRICT_GAPS',positive_gaps)

    w=suffix_observers(F(0),F(0))
    w10=suffix_observers(F(1),F(0))
    w01=suffix_observers(F(0),F(1))
    w11=suffix_observers(F(1),F(1))
    u=tuple(w10[i]-w[i] for i in range(4))
    v=tuple(w01[i]-w[i] for i in range(4))
    assert w11==vec_add(w,vec_add(u,v))
    det=u[0]*v[1]-u[1]*v[0]
    assert det==F(-52470725634765625,202170937101722320896)
    x=((CAP_A-w[0])*v[1]-(CAP_B-w[1])*v[0])/det
    y=((CAP_B-w[1])*u[0]-(CAP_A-w[0])*u[1])/det
    assert x==F(2942214371765387,4197658050781250)
    assert y==F(478956919,600559125)
    assert 0<x<1 and 0<y<1
    print('BASE',w,'U',u,'V',v,'DETERMINANT',det)
    print('TARGET_COINS x_continue_at_A,y_continue_at_B',x,y)

    total_nodes=total_decisions=0
    for xx,yy in [(F(0),F(0)),(F(1),F(0)),(F(0),F(1)),(F(1),F(1)),(x,y)]:
        obs=suffix_observers(xx,yy)
        expect=tuple(w[i]+xx*u[i]+yy*v[i] for i in range(4))
        assert obs==expect
        exact,nodes,decisions=ordered_dfs(xx,yy)
        assert exact==obs
        assert obs[3]>obs[2]
        # Primal/dual equality follows from Bellman actions and normalization.
        assert obs[3]+K_P*obs[0]+K_Q*obs[1]==H
        assert F(0)<=obs[0]<=1 and F(0)<=obs[1]<=1
        assert 2*obs[0]+obs[1]<1
        total_nodes+=nodes;total_decisions+=decisions
        print('COIN',xx,yy,'OBS',obs,'DFS_NODES',nodes,'DECISIONS',decisions)
    target=suffix_observers(x,y)
    assert target[:2]==(CAP_A,CAP_B)
    value=H-K_P*CAP_A-K_Q*CAP_B
    assert value==target[3]==F(3625356966401597,645573577789440)
    assert target[2]==F(62742333308848141,11620324400209920)
    tv=24*(1-CAP_A-CAP_B)
    assert value>tv and CAP_A+CAP_B<1
    threshold=F(6774487633,8707129344)
    assert CAP_A+CAP_B>threshold and 2*CAP_A+CAP_B<1
    print('TARGET_CAPS',CAP_A,CAP_B)
    print('TARGET_OBSERVERS',target)
    print('OPTIMUM',value,'TV_LOWER',tv,'STRICT_TV_GAP',value-tv)
    print('ALL_REAL_CONTACT_PARALLELOGRAM_AREA',abs(det))
    print('TOTAL_ORDERED_NODES',total_nodes,'TOTAL_DECISIONS',total_decisions)
    print('STAGE256_ASYMMETRIC_EXACT_PASS')

if __name__=='__main__':
    main()
