#!/usr/bin/env python3
"""C272 author exact audit; import immutable C271 self-contained source.

The universal convexity argument is in C272 theorem Markdown. This checker
certifies all 232 *rational anchor* instances and a uniform finite-width tube;
it does not replace the universal analytic proof or imply native BRC admission.
"""
from fractions import Fraction as F
from itertools import combinations
from C271_R2_STANDALONE_EXACT_REPLAY import D, U, J, I, Q, H, A, Z

BAND = F(1, 3014)
assert I == (5, 50, 55, 56)
assert len(D) == 35 and len(J) == 75
# Exact interval-uniform strict-convexity witness:
assert U[54] == F(7, 9) and U[55] == F(15, 19) and U[56] == F(17, 21)
assert Z + U[54] - 2 * U[56] > 0

def q_value(a, b, x):
    """Q*A/H rational auxiliary collision factor, no floats."""
    assert U[55] < x < U[56] and a < U[55] and b < U[55]
    out = F(Q) * A / H / ((2-x*x)*(3-x*x))**3
    for j in J:
        out *= (Z-U[j]) / abs(x-U[j])
    for p in (a,b):
        out *= (Z-p) / abs(x-p)
    return out

def check():
    touched = crossed = safe = 0
    worst = None
    min_cap = None
    for i, j in combinations(range(35),2):
        l1,h1 = D[i]; l2,h2 = D[j]
        lo = tuple(min(v,w) for v,w in zip(l1,l2))
        hi = tuple(max(v,w) for v,w in zip(h1,h2))
        gap = hi[2]-lo[3]
        if gap < 0:
            safe += 1
            continue
        touched += (gap == 0)
        crossed += (gap > 0)
        a,b = (lo[0]+hi[0])/2, (lo[1]+hi[1])/2
        t = (hi[2]+lo[3])/2
        cap = min(2*(t-lo[2]), 2*(hi[3]-t), 2*(t-U[55]), 2*(U[56]-t))
        assert cap >= BAND
        if min_cap is None or cap < min_cap:
            min_cap = cap
        q0 = q_value(a,b,t)
        r = 2*(Z-t)*q0
        assert r*3014 > Q  # exact strict threshold for the full band
        ratio = r/Q
        if worst is None or ratio < worst[2]:
            worst = (i,j,ratio)
        left = t-BAND/2
        right = t+BAND/2
        assert lo[2] <= left <= hi[2] and lo[3] <= right <= hi[3]
        qm,qp = q_value(a,b,left),q_value(a,b,right)
        normalized = qm*(Z-right) + qp*(Z-left)
        assert normalized > r                 # illustrative exact endpoint check
        assert normalized > BAND*Q            # even two colliding terms > Q
    assert (safe,touched,crossed)==(363,124,108)
    assert worst[0:2] == (11,24)
    assert worst[2]*3013 < 1 and worst[2]*3014 > 1
    assert min_cap == F(73,25662)
    print('C272_EXACT_PASS', 'hulls', safe+touched+crossed,
          'collision',touched+crossed,'touch',touched,'cross',crossed,
          'certified_epsilon',str(BAND),'worst_anchor',str(worst[:2]),
          'worst_R_over_Q_approx',format(float(worst[2]),'.15f'),
          'geometric_min_cap',str(min_cap),
          'analytical_convexity_delta',str(Z+U[54]-2*U[56]))

if __name__ == '__main__':
    check()
