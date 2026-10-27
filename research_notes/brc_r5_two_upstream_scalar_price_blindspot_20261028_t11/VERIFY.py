#!/usr/bin/env python3
"""Exact rational certificate for the R5 two-upstream masking counterexample.

An external finite P/Q observation experiment, not native X6 dynamics.
No numerical tolerance: Fraction and integer arithmetic throughout.
"""
from fractions import Fraction as F
from itertools import product

# leaf = (t1 branch, t2 branch, t3 final LR or None, P*128, Q*128)
LEAVES = (
    ('U', 'C', F(1,2), 6, 12),
    ('U', 'C', F(1), 24, 24),
    ('U', 'C', F(3,2), 18, 12),
    ('U', 'O', None, 24, 16),
    ('V', 'C', F(1,2), 3, 6),
    ('V', 'C', F(1), 36, 36),
    ('V', 'C', F(3,2), 9, 6),
    ('V', 'O', None, 8, 16),
)
Y = (F(1,2), F(1), F(3,2))
ACTIONS = ('P','Q','C')
DECLARE = ('P','Q')
LAMBDA = (20, 23, 10, -9)


def outcome(ru, rv, cu, cv, ou, ov, yu, yv):
    """Outcome in units of 1/128; no shared persistent random seed."""
    o = [0,0,0,0]
    for root, sub, y, p, q in LEAVES:
        first = ru if root == 'U' else rv
        collision = cu if root == 'U' else cv
        side = ou if root == 'U' else ov
        if first != 'C':
            decision, tau = first, 1
        elif sub == 'O':
            decision, tau = side, 2
        elif collision != 'C':
            decision, tau = collision, 2
        else:
            decision, tau = (yu if root == 'U' else yv)[Y.index(y)], 3
        o[0] += p * (decision == 'Q')
        o[1] += q * (decision == 'P')
        o[2] += p * tau
        o[3] += q * tau
    return tuple(o)


def exact_bellman(alpha, beta, gamma, delta):
    """Minimize all real behavioral strategies via deterministic Bellman envelopes."""
    alpha, beta, gamma, delta = map(F, (alpha, beta, gamma, delta))
    f = lambda r: min(alpha * r, beta)
    price = lambda r: gamma * r + delta
    theta = F(3,4)
    d = F(1,2)
    a, b = F(1,4), F(1,8)
    D = 2*f(1) - f(F(1,2)) - f(F(3,2))
    assert D >= 0
    gains = (a*D, b*D)
    ratios = (1 + (1-theta)*d, 1 - (1-theta)*d)
    other = (1+d, 1-d)
    base=[]
    for r, ro in zip(ratios,other):
        stop = (f(r)+price(r))/2
        cont_before_C = (2*price(r)+theta*f(1)+(1-theta)*f(ro))/2
        base.append((stop,cont_before_C))
    full=sum(min(st,co-theta*max(g-price(1),0)/2) for (st,co),g in zip(base,gains))
    by_coll_action=[]
    for cont_C in (False,True):
        branch_choices=[]
        for (st,co),g in zip(base,gains):
            branch_choices.append((st,co-theta*(g-price(1))/2 if cont_C else co))
        by_coll_action.append(sum(min(v) for v in branch_choices))
    compressed=min(by_coll_action)
    return full, compressed, by_coll_action, gains, base


def display_o(o):
    return '(' + ', '.join(str(F(x,128)) for x in o) + ')'


def main():
    assert sum(p for *_,p,q in LEAVES) == 128
    assert sum(q for *_,p,q in LEAVES) == 128
    assert all(p > 0 and q > 0 for *_,p,q in LEAVES)
    assert all(F(p,q)==y for _,sub,y,p,q in LEAVES if sub == 'C')
    assert F(72,64)==F(9,8) and F(56,64)==F(7,8)
    for root in ('U', 'V'):
        pc = sum(p for h, sub, y, p, q in LEAVES if h == root and sub == 'C')
        qc = sum(q for h, sub, y, p, q in LEAVES if h == root and sub == 'C')
        assert (pc, qc) == (48, 48)  # distinct histories collide at LR=1
    assert (sum(p for h,sub,y,p,q in LEAVES if h == 'U'),
            sum(q for h,sub,y,p,q in LEAVES if h == 'U')) == (72,64)
    assert (sum(p for h,sub,y,p,q in LEAVES if h == 'V'),
            sum(q for h,sub,y,p,q in LEAVES if h == 'V')) == (56,64)
    assert F(24,16)==F(3,2) and F(8,16)==F(1,2)

    all_full = {}
    all_lr = {}
    count_full = count_lr = 0
    triple = tuple(product(DECLARE, repeat=3))
    for ru, rv, cu, cv, ou, ov in product(ACTIONS, ACTIONS, ACTIONS, ACTIONS, DECLARE, DECLARE):
        for yu in triple:
            for yv in triple:
                point = outcome(ru,rv,cu,cv,ou,ov,yu,yv)
                policy = (ru,rv,cu,cv,ou,ov,yu,yv)
                count_full += 1
                all_full.setdefault(point, policy)
                if cu == cv and yu == yv:
                    count_lr += 1
                    all_lr.setdefault(point, policy)
    assert (count_full, count_lr, len(all_full), len(all_lr)) == (20736,864,380,120)

    score = lambda v: sum(int(c)*x for c,x in zip(LAMBDA,v))
    full_point = min(all_full,key=score)
    lr_point = min(all_lr,key=score)
    v_full = F(score(full_point),128)
    v_lr = F(score(lr_point),128)
    bell_full,bell_lr,perC,gains,base=exact_bellman(*LAMBDA)
    assert v_full == bell_full == F(667,32)
    assert v_lr == bell_lr == F(167,8)
    assert v_lr-v_full == F(1,32)
    assert full_point == (86,28,304,304)
    assert lr_point == (128,0,184,192)
    assert perC == [F(167,8), F(1337,64)]
    assert gains == (F(7,4),F(7,8))
    assert base == [(F(99,8),F(101,8)),(F(69,8),F(17,2))]
    assert all(score(q) >= 2672 for q in all_lr)
    assert score(full_point)==2668

    # Finite signed alpha/beta and nonnegative scalar Q-time price checks are
    # a supplementary audit only: the *all-real* theorem is proved in PROOF.md.
    finite_check_count=0
    for alpha in range(-8,9):
        for beta in range(-8,9):
            for k in range(0,33):
                t=F(k,32)
                full_support,lr_support,*_=exact_bellman(alpha,beta,0,t)
                assert full_support == lr_support, (alpha,beta,t)
                finite_check_count += 1

    print('MODEL: 8 strictly positive rational P/Q leaves, denominator 128')
    print('P_TOTAL=1 Q_TOTAL=1')
    print('ROOT_LR: U=9/8 V=7/8')
    print('T2_LR: U.C=V.C=1; U.O=3/2; V.O=1/2')
    print('T3_C_LR: 1/2, 1, 3/2 for both hidden sources')
    print(f'POLICIES_FULL={count_full} POLICIES_LR={count_lr}')
    print(f'UNIQUE_OBSERVATIONS_FULL={len(all_full)} LR={len(all_lr)}')
    print(f'TARGET_LAMBDA={LAMBDA}')
    print(f'FULL_MIN={v_full}  FULL_POINT={display_o(full_point)}')
    print(f'FULL_POLICY={all_full[full_point]}')
    print(f'LR_MIN={v_lr}  LR_POINT={display_o(lr_point)}')
    print(f'LR_POLICY={all_lr[lr_point]}')
    print(f'EXACT_GAP={v_lr-v_full}')
    print(f'COMMON_COLLISION_STOP_MIN={perC[0]} CONTINUE_MIN={perC[1]}')
    print(f'G_A={gains[0]} G_B={gains[1]}')
    print(f'FINITE_SCALAR_PRICE_AUDIT_CASES={finite_check_count} (not a universal proof)')
    print('ALL EXACT TWO-UPSTREAM CHECKS PASSED')

if __name__ == '__main__':
    main()
