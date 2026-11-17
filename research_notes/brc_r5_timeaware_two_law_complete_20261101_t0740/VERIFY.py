#!/usr/bin/env python3
"""Exact standard-library verifier for the R5 two-law time-aware merger theorem.
The universal statements use the Bellman and interpolation proofs in RESEARCH.md.
"""
from fractions import Fraction as F
from itertools import product, permutations

Q = F(1, 2)
ZERO = F(0)
ONE = F(1)


def obs(bits, a, b, full):
    """(P_error,Q_error,E_P[time],E_Q[time]).
    FULL bits=(pA,pB,qAlo,qAhi,qBlo,qBhi); LR=(p,qlo,qAhi,qBhi).
    At a=b, admissible LR additionally requires qAhi=qBhi.
    Each bit means stop; time 2 continue is terminal at time 3.
    """
    if full:
        pA, pB, la, ha, lb, hb = bits
    else:
        p, low, ha, hb = bits
        pA = pB = p
        la = lb = low
    v = [ZERO, ZERO, ZERO, ZERO]
    for alpha, p1, lo, hi in ((a, pA, la, ha), (b, pB, lb, hb)):
        p1, lo, hi = map(F, (p1, lo, hi))
        # Time 1 stop declares P.
        v[1] += Q * p1
        v[2] += Q * p1
        v[3] += Q * p1
        for branch, pcond, qcond, qstop in (
            ("lo", alpha / 2, alpha, lo),
            ("hi", ONE - alpha / 2, ONE - alpha, hi),
        ):
            pm = Q * (ONE - p1) * pcond
            qm = Q * (ONE - p1) * qcond
            if branch == "lo":
                # Time 2 stop declares P; time 3 default declares Q.
                v[0] += pm * (ONE - qstop)
                v[1] += qm * qstop
            else:
                # Time 2 stop declares Q; time 3 default declares P.
                v[0] += pm * qstop
                v[1] += qm * (ONE - qstop)
            v[2] += pm * (3 - qstop)
            v[3] += qm * (3 - qstop)
    return tuple(v)


def det(m):
    ans = ZERO
    for perm in permutations(range(len(m))):
        inv = sum(perm[i] > perm[j] for i in range(len(m))
                  for j in range(i + 1, len(m)))
        prod = ONE
        for i in range(len(m)):
            prod *= m[i][perm[i]]
        ans += (-ONE if inv % 2 else ONE) * prod
    return ans


def cost(v, theta):
    return (ONE + theta) * v[1] + v[3]


def vertices(a, b, full):
    return [(bits, obs(bits, a, b, full))
            for bits in product((0, 1), repeat=(6 if full else 4))]


def off_diagonal_check(a, b):
    assert ZERO < a < ONE and ZERO < b < ONE and a != b
    for alpha in (a,b):
        # Both transition laws are strictly positive and normalized.
        assert alpha > 0 and 1-alpha > 0
        assert alpha/2 > 0 and 1-alpha/2 > 0
        assert alpha + (1-alpha) == ONE
        assert alpha/2 + (1-alpha/2) == ONE
    # Time-2 LR keys: low 1/2, two distinct high keys >1.
    ha = (ONE-a/2)/(ONE-a)
    hb = (ONE-b/2)/(ONE-b)
    assert ha > ONE and hb > ONE and ha != hb
    fv, lv = vertices(a, b, True), vertices(a, b, False)
    assert len(fv) == 64 and len(lv) == 16
    for _,v in fv+lv:
        assert all(0 <= v[k] <= 1 for k in (0,1))
        assert all(1 <= v[k] <= 3 for k in (2,3))
    theta = (a+b)/2
    cf = min(cost(v, theta) for _,v in fv)
    cl = min(cost(v, theta) for _,v in lv)
    expected_cf = 2 + (min(a,b) + theta)/2
    expected_cl = 2 + theta
    gap = abs(a-b)/4
    assert cf == expected_cf and cl == expected_cl
    assert cl - cf == gap > 0
    if a < b:
        witness = obs((0,1,0,1,0,0),a,b,True)
    else:
        witness = obs((1,0,0,0,0,1),a,b,True)
    assert cost(witness,theta) == cf
    # The five named LR deterministic policies give a 4x4 determinant.
    base = obs((0,0,0,0), a, b, False)
    rows=[]
    for j in range(4):
        v=obs(tuple(int(i == j) for i in range(4)), a,b,False)
        rows.append([v[k]-base[k] for k in range(4)])
    determinant=det(rows)
    assert determinant == (b*b-a*a)/8 != ZERO
    return (cf,cl,gap,determinant,witness)


def on_diagonal_check(a):
    assert ZERO<a<ONE
    # At a=b the high keys coincide: only (p,qlo,qhi) are admissible.
    vv=[obs((p,lo,hi,hi),a,a,False)
        for p,lo,hi in product((0,1),repeat=3)]
    base=vv[0]
    tri=[]
    for bits in ((1,0,0,0),(0,1,0,0),(0,0,1,1)):
        v=obs(bits,a,a,False)
        tri.append([v[k]-base[k] for k in (0,1,2)])
    assert det(tri)==a*(4-a)/4>0
    # Arbitrary FULL real behavior can be Markovized at the (time,LR) keys.
    probs=(ZERO,F(1,3),Q,F(2,3),ONE)
    checks=0
    for pA,pB,qAl,qAh,qBl,qBh in product(probs,repeat=6):
        full=(pA,pB,qAl,qAh,qBl,qBh)
        survival=(ONE-pA)+(ONE-pB)
        p=(pA+pB)/2
        qlo=(((ONE-pA)*qAl+(ONE-pB)*qBl)/survival
             if survival else ZERO)
        qhi=(((ONE-pA)*qAh+(ONE-pB)*qBh)/survival
             if survival else ZERO)
        assert all(ZERO<=x<=ONE for x in (p,qlo,qhi))
        assert obs(full,a,a,True)==obs((p,qlo,qhi,qhi),a,a,False)
        checks+=1
    return checks


def interpolation_check():
    # Each of the 4x4 entries is affine in (a,b), so its determinant has
    # degree <=4 separately in a and b. Agreement on a five-by-five
    # rational grid proves the identity for all real a,b by root counting.
    aa=(F(1,20),F(1,10),F(1,5),F(1,4),F(3,10))
    bb=(F(1,2),F(3,5),F(2,3),F(3,4),F(4,5))
    for a,b in product(aa,bb):
        off_diagonal_check(a,b)
    return len(aa)*len(bb)


if __name__=='__main__':
    interpolation=interpolation_check()
    aa=(F(1,20),F(1,8),F(1,4),F(2,5),F(3,5),F(3,4),F(9,10))
    bb=(F(1,10),F(1,5),F(1,3),F(1,2),F(2,3),F(4,5),F(19,20))
    samples=0
    for a,b in product(aa,bb):
        if a!=b:
            off_diagonal_check(a,b)
            samples+=1
    diagonal=sum(on_diagonal_check(a) for a in (F(1,4),Q,F(3,4)))
    a,b=F(1,4),Q
    cf,cl,gap,D,witness=off_diagonal_check(a,b)
    assert (cf,cl,gap,D,witness)==(
        F(37,16),F(19,8),F(1,16),F(3,128),
        (Q,Q,F(25,16),F(13,8)))
    print('interpolation_grid_points=',interpolation)
    print('off_diagonal_rational_regression_pairs=',samples)
    print('on_diagonal_exact_markovization_checks=',diagonal)
    print('sample_a_b=',a,b,'theta=',(a+b)/2)
    print('sample_LR_keys=(1,1),(2,1/2),(2,7/6),(2,3/2)')
    print('sample_FULL_witness=',tuple(map(str,witness)))
    print('sample_cost_FULL_LR=',cf,cl,'support_gap=',gap)
    print('sample_LR_rank4_determinant=',D)
    print('sample_Linf_distance_lower_bound=',gap/(2+(a+b)/2))
    print('PASS_EXACT_R5_TIME_AWARE_TWO_LAW_COMPLETE_PARAM_CLASSIFICATION')
