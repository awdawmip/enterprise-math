#!/usr/bin/env python3
"""Exact Fraction verification of a K3 P=Q time-gate subclass.
No third party dependencies or floating point arithmetic. The four effective
triple states represent all 8 deterministic z,t,u controls exactly:
when z=0, t,u do not matter; when t=0, u does not matter.
"""
from fractions import Fraction as F
from itertools import product

ALPHA = (F(1, 2), F(2, 3), F(1, 2), F(3, 4))
CSTAR = (F(1, 8), F(1, 6), F(1, 16), F(3, 32))
FULL_UP = ((0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 1, 0))
LR_UP = ((0, 0), (0, 1), (1, 0), (1, 1))
TRIPLES = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1))


def weights(x, y, i):
    return (F(1, 4), F(1-x, 4), F(y, 8), F(i, 8))


def observer(x, y, i, gates, r):
    w = weights(x, y, i)
    M = [w[s] * ALPHA[s] * gates[s][0] for s in range(4)]
    S = [F(2, 3) * M[s] * gates[s][1] for s in range(4)]
    U = [S[s] * gates[s][2] for s in range(4)]
    d = F(y, 16) + F(3*i, 32)
    return (
        F(107, 128)-F(21*x, 128)+d/4-sum(S)/2,
        F(13, 64)+F(3*x, 64)-d/2+sum(S)/8,
        3+sum(M)+F(3, 2)*sum(S)+sum(r[s]*U[s] for s in range(4)),
        3+sum(M)/2+F(3, 8)*sum(S)+sum(r[s]*U[s] for s in range(4))/4,
    )


def scalar(n, obs):
    return sum(F(a)*b for a, b in zip(n, obs))


def supports_enumerated(n, r):
    best_full = None
    best_lr = None
    nfull = 0
    nlr = 0
    for x, y, i in FULL_UP:
        for gates in product(TRIPLES, repeat=4):
            val = scalar(n, observer(x, y, i, gates, r))
            best_full = val if best_full is None else max(best_full, val)
            nfull += 1
    for x, y in LR_UP:
        i = (1-x)*y
        for gate in TRIPLES:
            val = scalar(n, observer(x, y, i, (gate,)*4, r))
            best_lr = val if best_lr is None else max(best_lr, val)
            nlr += 1
    assert (nfull, nlr) == (1536, 16)
    return best_full, best_lr


def gap_formula(r, t):
    pos = sum(c * max(F(0), rs-t) for c, rs in zip(CSTAR, r))
    neg = sum(c * max(F(0), t-rs) for c, rs in zip(CSTAR, r))
    return F(2, 3) * min(pos, neg)


def direction(t):
    return (F(0), -12-8*t, F(2), F(-4))


def main():
    kernels = (
        (F(1, 4), F(1, 2), F(3, 4), F(1, 2)),
        (F(1, 8), F(7, 8), F(3, 8), F(5, 8)),
        (F(1, 3),)*4,
    )
    thresholds = (F(1, 8), F(1, 4), F(3, 8), F(1, 2), F(5, 8), F(3, 4), F(7, 8))
    cases = 0
    for kernel in kernels:
        for th in thresholds:
            hf, hl = supports_enumerated(direction(th), kernel)
            assert hf-hl == gap_formula(kernel, th), (kernel, th, hf, hl)
            cases += 1
        print('KERNEL', ','.join(map(str,kernel)), 'CHECKED_THRESHOLDS',len(thresholds))
    r = kernels[0]
    n = direction(F(1, 2))
    hf, hl = supports_enumerated(n, r)
    assert hf == F(-767, 96)
    assert hl == F(-8)
    assert hf-hl == F(1, 96)
    # Only BJ uses z=t=u=1; other source gates are off.
    W = observer(0, 1, 1, ((0, 0, 0), (0, 0, 0), (1, 1, 1), (0, 0, 0)), r)
    assert W == (F(41, 48),F(25, 192),F(101, 32),F(391, 128))
    assert scalar(n, W) == hf
    assert (hf-hl)/sum(abs(x) for x in n) == F(1, 2112)
    print('RATIONAL_WITNESS', W)
    print('SIGNED_DIRECTION', n, 'FULL', hf, 'LR', hl, 'GAP', hf-hl)
    print('L_INFINITY_SEPARATION_LOWER_BOUND', F(1, 2112))
    print('EXACT_CASES', cases, 'FULL_ENUM_PER_CASE', 1536, 'LR_ENUM_PER_CASE', 16)
    print('PASS_EXACT_R5_K3_PROPORTIONAL_EQUAL_LAW_RIGIDITY')


if __name__ == '__main__':
    main()
