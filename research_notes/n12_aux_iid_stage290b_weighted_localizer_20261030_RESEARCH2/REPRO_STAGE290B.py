#!/usr/bin/env python3
"""Stage290-B: exact Fraction witnesses for weighted localizing residuals.

Scientific scope: external finite-source repeated Bernoulli port model,
not P000 native dynamics. Universal inequalities are proved in PROOF_STAGE290B.md.
"""
from fractions import Fraction as F
from itertools import product

ZERO = F(0)
ONE = F(1)
QUARTER = F(1, 4)


def g(t):
    return t*t-t+F(1, 8)


def localizer(t, order):
    w = t if order == 5 else t*(1-t)
    return w*g(t)**2


def leaves(y, n):
    # Ordered stop words: 0, 10, 110, ..., 1^(n-1)0, 1^n.
    out = [y**j*(1-y) for j in range(n)] + [y**n]
    assert sum(out) == ONE and all(x >= 0 for x in out)
    return out


def mixture_leaves(measure, n):
    return [sum((p*leaves(y, n)[j] for p,y in measure), ZERO)
            for j in range(n+1)]


def tv(p, q):
    assert len(p) == len(q)
    return sum((abs(a-b) for a,b in zip(p,q)), ZERO)/2


P = (F(1,16),F(3,16),F(9,16),F(3,16))
Q = (F(1,9),F(2,9),F(4,9),F(2,9))
assert sum(P) == ONE and sum(Q) == ONE


def labeled_leaves(source, measure, n):
    leaf = mixture_leaves(measure, n)
    return [s*b for s in source for b in leaf]


def K_mass(measure):
    return sum((p for p,t in measure if QUARTER <= t <= F(3,4)), ZERO)


def E_localizer(measure, order):
    return sum((p*localizer(t, order) for p,t in measure), ZERO)


# Sharp rational certificate on K=[1/4,3/4], with equality witness.
for order, eta in ((5,F(1,1024)),(6,F(3,4096))):
    for j in range(257):
        t = QUARTER+F(j,512)
        assert localizer(t, order) >= eta
    assert localizer(QUARTER,order) == eta
    if order == 6:
        assert localizer(F(3,4),order) == eta
    mu = ((F(3,4),ZERO),(F(1,4),QUARTER))
    eps = E_localizer(mu,order)
    assert K_mass(mu) == F(1,4)
    assert eps == eta/4
    assert K_mass(mu) == eps/eta
    # All 5^2 positive rational supported measures on {0,1/4,1/2,3/4,1}.
    grid = (ZERO,QUARTER,F(1,2),F(3,4),ONE)
    for a,b in product(grid,repeat=2):
        for k in range(9):
            weight=F(k,8)
            m=((weight,a),(ONE-weight,b))
            assert K_mass(m)*eta <= E_localizer(m,order)
    print(f"K_SHARP order={order} eta={eta} epsilon={eps} muK=1/4")

# For each d>0, Dirac(0) and Dirac(d) have full Y-TV = 1;
# ordered BRC leaves have TV=d for all n>=1 and both P/Q labeled sources.
for n in (1,5,6):
    for d in (F(1,2),F(1,8),F(1,64),F(1,256)):
        a = ((ONE,ZERO),)
        b = ((ONE,d),)
        assert tv(mixture_leaves(a,n),mixture_leaves(b,n)) == d
        for source in (P,Q):
            assert tv(labeled_leaves(source,a,n),labeled_leaves(source,b,n)) == d
            assert sum(labeled_leaves(source,b,n)) == ONE
            assert len(labeled_leaves(source,b,n)) == 4*(n+1)
        assert localizer(d,5) > 0 and localizer(d,6) > 0
        print(f"DIRAC n={n} d={d} eps5={localizer(d,5)} eps6={localizer(d,6)} ordered_TV={d} hidden_TV=1")

# For any finitely-supported distribution on rational atoms, check direct
# discrete W1-to-zero-set upper bounds for endpoint-adjacent case: delta0 reference.
for order, c in ((5,F(1,4096)),(6,F(7,32768))):
    for d in (F(1,256),F(1,128),F(1,64),F(1,32)):
        # Distance to zero set is <=d (because 0 lies in both Z).
        assert d*d*c <= localizer(d,order)
    print(f"LOCAL_QUADRATIC_ENDPOINT_CHECK order={order} c={c}")

# Exact moment-to-leaf consistency, shared Y (not independently resampled Y).
for n in (5,6):
    mu=((F(3,4),ZERO),(F(1,4),QUARTER))
    moments=[sum((p*y**k for p,y in mu),ZERO) for k in range(n+1)]
    leaf=mixture_leaves(mu,n)
    assert leaf == [moments[j]-moments[j+1] for j in range(n)]+[moments[n]]
    assert sum(leaf)==ONE
    print(f"MOMENT_LEAF n={n} m1={moments[1]} m2={moments[2]} terminal={leaf[-1]}")
print('STAGE290B_WEIGHTED_LOCALIZER_OBSERVER_EXACT_PASS')
