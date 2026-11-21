#!/usr/bin/env python3
"""R73: exact finite D4 small-Port enumeration + rational chamber checks.

No third-party libraries; this is an author certificate, not independent review.
The all-p theorem uses the symbolic determinant/kernel argument in R73.md.
"""
import json
from fractions import Fraction
from math import gcd
from functools import reduce


def q(a):
    return max(sum(max(u, 0) for u in a), sum(max(-u, 0) for u in a))


def gaps(a):
    x, y, z = a
    z2, z3, z4 = 2*x + 6*y + 12*z, 6*x + 24*y + 60*z, 14*x + 78*y + 252*z
    C = max(abs(z2), abs(z2-z3), abs(z2-z4))
    B = max(abs(z3), abs(z4), abs(z3-z4))
    return C, B, (0, z2, z3, z4)


def domain(p):
    for x in range(-p, p+1):
        for y in range(-p, p+1):
            for z in range(-p, p+1):
                a = (x, y, z)
                if a == (0, 0, 0) or next(v for v in a if v != 0) < 0:
                    continue
                if q(a) <= p:
                    yield a


def eta(a, t):
    C, B, _ = gaps(a)
    return max(Fraction(C, 2)/(1+t), Fraction(B, 4))


def formula(p, t):
    if p == 4: return max(Fraction(6)/(1+t), Fraction(7, 2))
    if p == 5: return max(Fraction(4)/(1+t), Fraction(3))
    if 6 <= p <= 10: return Fraction(3)
    ordinary = max(Fraction(1)/(1+t), Fraction(1, 2))
    if p <= 124: return ordinary
    return min(ordinary, Fraction(12)/(1+t))


EXPECTED = {
    4: (154, 12, 14, (1,0,0)),
    5: (280, 8, 12, (4,-4,1)),
    6: (461, 6, 12, (6,-1,0)),
    7: (707, 6, 12, (6,-1,0)),
    8: (1028, 6, 12, (6,-1,0)),
    9: (1434, 6, 12, (6,-1,0)),
    10: (1935, 6, 12, (6,-1,0)),
    11: (2541, 2, 2, (10,-5,1)),
}
T = [Fraction(1,10), Fraction(1,5), Fraction(1,3), Fraction(1,2),
     Fraction(5,7), Fraction(1), Fraction(2), Fraction(23),
     Fraction(24), Fraction(100)]
rows = []
for p, (count, minC, minB, witness) in EXPECTED.items():
    vals = [(a, gaps(a)[:2]) for a in domain(p)]
    assert len(vals) == count, (p, len(vals), count)
    assert min(v[0] for _,v in vals) == minC
    assert min(v[1] for _,v in vals) == minB
    assert gaps(witness)[:2] == (minC, minB)
    for t in T:
        assert min(eta(a, t) for a,_ in vals) == formula(p,t), (p,t)
    rows.append({'p':p,'unoriented_count':count,'min_C':minC,
                 'min_B':minB,'simultaneous_witness':list(witness)})

# Elementary invariant and primitive integer kernel used in the symbolic proof.
assert 2*(24*252-60*78) == 2736  # cross product component check
cross = (24*252-60*78, 60*14-6*252, 6*78-24*14)
assert cross == (1368,-672,132)
g = reduce(gcd, (abs(v) for v in cross))
assert g == 12
kernel = tuple(v//g for v in cross)
assert kernel == (114,-56,11)
assert q(kernel) == 125 and gaps(kernel) == (24,0,(0,24,0,0))
assert q((10,-5,1)) == 11 and gaps((10,-5,1)) == (2,2,(0,2,0,2))
assert 288 == (2*(24*252-60*78) - 6*(6*252-60*14) + 12*(6*78-24*14))

sample = [(4,Fraction(1)), (4,Fraction(1,2)), (5,Fraction(1)),
          (5,Fraction(1,5)), (6,Fraction(1)), (11,Fraction(1,2)),
          (11,Fraction(1)), (124,Fraction(24)), (125,Fraction(23)),
          (125,Fraction(24)), (125,Fraction(100))]
examples=[{'p':p,'t':str(t),'eta_star':str(formula(p,t))} for p,t in sample]
assert formula(124,Fraction(24)) == Fraction(1,2)
assert formula(125,Fraction(24)) == Fraction(12,25)
assert formula(125,Fraction(23)) == Fraction(1,2)
assert formula(125,Fraction(23,1)) == formula(124,Fraction(23,1))

report={'schema':'X6_R73_D4_SINGLE_NOISY_CHANNEL_EXACT_V1',
        'arithmetic':'Python integers + fractions.Fraction; no floating point',
        'finite_scope':'all unoriented nonzero Z^3 differences with q<=p for p=4..11',
        'port_rows':rows,'t_grid':[str(t) for t in T],
        'finite_exact_comparisons':sum(row['unoriented_count'] for row in rows)*len(T),
        'kernel':list(kernel),'kernel_q':125,
        'symbolic_claim':'all p>=11, all real t>0 proved in accompanying paper via parity and primitive kernel',
        'sample_values':examples,'assertions':'PASS'}
print(json.dumps(report,ensure_ascii=False,indent=2))
