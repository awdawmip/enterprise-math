#!/usr/bin/env python3
"""Exact certificates: local-ray theorem instance, global counterexample, rank four.

No external dependencies. The universal geometric theorems are proved in RESEARCH.md;
this script checks the finite counterexample and rational certificates, not an
unbounded universal quantifier by sampling.
"""
from fractions import Fraction as F
from itertools import product

SOURCES = ('A', 'B')
P_LOW = {'A': F(1, 8), 'B': F(1, 4)}
Q_LOW = {'A': F(1, 4), 'B': F(1, 2)}
# Terminal port W=(zero, alpha, beta). Binary response is 0 for zero and 1 for alpha,beta.
PORT = {
    ('A', True, 'P'): (F(1, 2), F(1, 3), F(1, 6)),
    ('A', True, 'Q'): (F(1, 2), F(1, 3), F(1, 6)),
    ('B', True, 'P'): (F(1, 2), F(1, 6), F(1, 3)),
    ('B', True, 'Q'): (F(1, 2), F(1, 6), F(1, 3)),
    ('A', False, 'P'): (F(1, 4), F(3, 8), F(3, 8)),
    ('A', False, 'Q'): (F(3, 4), F(1, 8), F(1, 8)),
    ('B', False, 'P'): (F(3, 4), F(1, 8), F(1, 8)),
    ('B', False, 'Q'): (F(1, 4), F(3, 8), F(3, 8)),
}
LR_KEYS = ('c', 'l', 'hA', 'hB')
FULL_KEYS = ('cA', 'cB', 'lA', 'hA', 'lB', 'hB')


def error_one(src, low, law):
    return sum(PORT[src, low, law][1:], F(0))


def observer(policy, lr=False):
    eP, eQ, TP, TQ = F(0), F(1), F(1), F(1)
    for s in SOURCES:
        c = policy['c'] if lr else policy['c'+s]
        if not c:
            continue
        # P/Q source prior 1/2, time 1 -> 3 (two units).
        TP += c
        TQ += c
        for low in (True, False):
            pm = F(1, 2) * (P_LOW[s] if low else 1 - P_LOW[s])
            qm = F(1, 2) * (Q_LOW[s] if low else 1 - Q_LOW[s])
            key = ('l' if low else 'h'+s) if lr else (('l' if low else 'h')+s)
            action = policy[key]
            eP += c * action * pm * error_one(s, low, 'P')
            eQ -= c * action * qm * error_one(s, low, 'Q')
            TP += c * action * pm
            TQ += c * action * qm
    return (eP, eQ, TP, TQ)


def det4(rows):
    m = [list(map(F, row)) for row in rows]
    out = F(1)
    for j in range(4):
        pivot = next((i for i in range(j, 4) if m[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            m[j], m[pivot] = m[pivot], m[j]
            out = -out
        x = m[j][j]
        out *= x
        for i in range(j + 1, 4):
            q = m[i][j] / x
            for k in range(j + 1, 4):
                m[i][k] -= q * m[j][k]
            m[i][j] = F(0)
    return out


def run():
    for s in SOURCES:
        for prob in (P_LOW[s], Q_LOW[s]):
            assert 0 < prob < 1
        for low,law in product((True, False), ('P','Q')):
            v = PORT[s, low, law]
            assert sum(v, F(0)) == 1 and all(0 < q < 1 for q in v)
    assert P_LOW['A']/Q_LOW['A'] == P_LOW['B']/Q_LOW['B'] == F(1,2)
    assert (1-P_LOW['A'])/(1-Q_LOW['A']) == F(7,6)
    assert (1-P_LOW['B'])/(1-Q_LOW['B']) == F(3,2)
    assert PORT['A',True,'P'] != PORT['B',True,'P']
    assert PORT['A',True,'Q'] != PORT['B',True,'Q']

    # Continue minus stop on the t=3, LR=1/2 collision when upstream both continue.
    D = {}
    for s in SOURCES:
        p, q = F(1,2)*P_LOW[s], F(1,2)*Q_LOW[s]
        D[s] = (p*error_one(s,True,'P'), -q*error_one(s,True,'Q'), p, q)
    assert D['A'] == (F(1,32),-F(1,16),F(1,16),F(1,8))
    assert D['B'] == tuple(2*x for x in D['A'])

    # Repair of a single last collision is exact even for arbitrary upstream FULL actions.
    # Other FULL keys remain source-dependent. This does NOT create a full LR policy.
    repairs = 0
    for bits in product((0,1), repeat=len(FULL_KEYS)):
        full = dict(zip(FULL_KEYS,bits))
        ca, cb = full['cA'], full['cB']
        den = ca + 2*cb
        common_low = F(ca*full['lA'] + 2*cb*full['lB'], den) if den else F(0)
        partial = dict(full)
        partial['lA'] = partial['lB'] = common_low
        assert observer(full) == observer(partial)
        repairs += 1

    lr = [(v,observer(dict(zip(LR_KEYS,v)),True)) for v in product((0,1),repeat=4)]
    full = [(v,observer(dict(zip(FULL_KEYS,v)),False)) for v in product((0,1),repeat=6)]
    weight = (F(5),F(0),F(-1),F(0))
    score = lambda x: sum((a*b for a,b in zip(weight,x)), F(0))
    max_LR = max(score(o) for _,o in lr)
    max_FULL = max(score(o) for _,o in full)
    assert max_LR == -1
    assert max_FULL == -F(45,64)
    assert max_FULL - max_LR == F(19,64)
    witness = observer(dict(zip(FULL_KEYS,(1,0,1,1,0,0))))
    assert witness == (F(23,64),F(27,32),F(5,2),F(5,2))
    assert score(witness) == max_FULL
    assert all(score(o) <= max_LR for _,o in lr)

    keys = ((0,0,0,0),(1,0,0,0),(1,0,0,1),(1,0,1,0),(1,1,0,0))
    vs = [observer(dict(zip(LR_KEYS,v)),True) for v in keys]
    minor = det4([[x-y for x,y in zip(v,vs[0])] for v in vs[1:]])
    assert minor == F(135,4096)
    print('TRUE_LR_KEYS_t1=1_t3low=1/2_t3highA=7/6_t3highB=3/2')
    print('POSITIVE_FINE_PORTS=8; LOW_PORT_NONLUMPABILITY=YES')
    print('LOW_COLLISION_D_A=(1/32,-1/16,1/16,1/8)')
    print('LOW_COLLISION_D_B=2*D_A')
    print('FULL_DETERMINISTIC_LOW_REPAIRS=', repairs, sep='')
    print('FULL_VERTICES=64 LR_VERTICES=16')
    print('LR_AFFINE_RANK4_MINOR=', minor, sep='')
    print('SUPPORT_DIRECTION=(5,0,-1,0)')
    print('MAX_FULL=',max_FULL,' MAX_LR=',max_LR,' GAP=',max_FULL-max_LR,sep='')
    print('FULL_WITNESS=(23/64,27/32,5/2,5/2)')
    print('LINF_DISTANCE_LOWER_BOUND=19/384')
    print('PASS_EXACT_R5_LAST_COLLISION_RAY_NOT_GLOBAL_HULL')

if __name__ == '__main__':
    run()
