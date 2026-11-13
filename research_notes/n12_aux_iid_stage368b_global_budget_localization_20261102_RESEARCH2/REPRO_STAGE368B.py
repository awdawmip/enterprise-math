#!/usr/bin/env python3
"""Stage368-B: exact universal budget localization, original labelled Bernoulli observer."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import sys

WEIGHTS = (1, 3, 3, 1)
TARGET = (61, 21, 9, 9)
E = F(11, 5000)
LOW = F(377, 100000)                  # 0.00377: certified global b lower bound
CAP = F(61, 6250)                     # 0.00976: strict upper bound on 2 beta_* + E
OUT = CAP - LOW                       # 0.00599
RECT = (F(219, 1000), F(239, 1000), F(51, 100), F(64, 100))

def B(k, z):
    return z**k * (1-z)**(3-k)

def r(k, x, y):
    return (4*B(k, x) + B(k, y))/5 - F(TARGET[k], 160)

def b(x, y):
    return F(5, 32)*sum(WEIGHTS[k]*abs(r(k, x, y)) for k in range(4))

def D3(a, z):
    return sum(WEIGHTS[k]*abs(B(k, a)-B(k, z)) for k in range(4))/2

def c(x, y):
    return (63*D3(F(1, 4), x) + D3(F(3, 4), x)
            + 9*D3(F(1, 4), y) + 7*D3(F(3, 4), y))/256

@lru_cache(None)
def bounds_B(k, a, z):
    values = [B(k, a), B(k, z)]
    critical = F(k, 3)
    if a < critical < z:
        values.append(B(k, critical))
    return min(values), max(values)

def box_lower(x0, x1, y0, y1):
    s = F(0)
    for k in range(4):
        xl, xu = bounds_B(k, x0, x1)
        yl, yu = bounds_B(k, y0, y1)
        lo = (4*xl+yl)/5 - F(TARGET[k], 160)
        hi = (4*xu+yu)/5 - F(TARGET[k], 160)
        bound = F(0) if lo <= 0 <= hi else min(abs(lo), abs(hi))
        s += WEIGHTS[k]*bound
    return F(5, 32)*s

# Isolate the original simultaneous r0=r1=0 reference root without floats.
xs0, xs1 = F(2310839, 10**7), F(2310840, 10**7)
ys0, ys1 = F(5555086, 10**7), F(5555091, 10**7)
assert r(0, xs0, ys1)>0 and r(0, xs1, ys0)<0
assert r(1, xs0, ys0)>0 and r(1, xs1, ys1)<0
assert r(2, xs0, ys0)>0 and r(3, xs1, ys1)<0
# On this box: r0 strictly decreases in x,y; r1 increases in x and
# decreases in y. Hence its zero graph crosses r0=0 once.
# On the zero intersection b=15*r2/16, increasing in both coordinates.
star_error_upper = F(15, 16)*r(2, xs1, ys1)
assert star_error_upper < F(189, 50000)
assert 2*star_error_upper + E < CAP
assert OUT > LOW

# Every leaf carries a rigorous interval lower bound for all real points.
counts = Counter()
stack = [(F(0), F(1), F(0), F(1), 0)]
leaves = []
min_gap = F(1)
while stack:
    x0, x1, y0, y1, depth = stack.pop()
    L = box_lower(x0, x1, y0, y1)
    inside = x0>=RECT[0] and x1<=RECT[1] and y0>=RECT[2] and y1<=RECT[3]
    if L > OUT:
        label, gap = 'OUTSIDE_FORBIDDEN', L-OUT
    elif inside and L > LOW:
        label, gap = 'INSIDE_GLOBAL_BOUND', L-LOW
    else:
        assert depth < 40, 'unclosed rational interval leaf'
        counts['SPLIT'] += 1
        if 4*(x1-x0) >= y1-y0:
            mid = (x0+x1)/2
            stack.extend([(x0, mid, y0, y1, depth+1),
                          (mid, x1, y0, y1, depth+1)])
        else:
            mid = (y0+y1)/2
            stack.extend([(x0, x1, y0, mid, depth+1),
                          (x0, x1, mid, y1, depth+1)])
        continue
    counts[label] += 1
    min_gap = min(min_gap, gap)
    leaves.append((depth, x0, x1, y0, y1, label, L))

assert counts == Counter({'SPLIT': 603, 'OUTSIDE_FORBIDDEN': 338,
                          'INSIDE_GLOBAL_BOUND': 266})
assert len(leaves)==604 and max(t[0] for t in leaves)==28 and min_gap>0
fr = lambda a: f'{a.numerator}/{a.denominator}'
certificate = 'depth,xlo,xhi,ylo,yhi,classification,exact_lower_bound\n'
for d,x0,x1,y0,y1,label,L in leaves:
    certificate += ','.join((str(d),fr(x0),fr(x1),fr(y0),fr(y1),label,fr(L)))+'\n'
digest = sha256(certificate.encode('utf-8')).hexdigest()
if len(sys.argv)==3 and sys.argv[1]=='--emit':
    Path(sys.argv[2]).write_text(certificate, encoding='utf-8')
else:
    assert len(sys.argv)==1, 'usage: REPRO_STAGE368B.py [--emit FILE]'
print('STAGE368B_EXACT_GLOBAL_BUDGET_LOCALIZATION_PASS')
print('star_error_upper=', fr(star_error_upper))
print('global_b_lower=', fr(LOW), 'outside_b_lower=', fr(OUT))
print('feasible_source_rectangle=', ','.join(fr(t) for t in RECT))
print('splits=', counts['SPLIT'], 'outside_leaves=',counts['OUTSIDE_FORBIDDEN'],
      'inside_leaves=', counts['INSIDE_GLOBAL_BOUND'])
print('max_depth=',max(t[0] for t in leaves),'min_exact_slack=',fr(min_gap))
print('certificate_sha256=',digest,'certificate_bytes=',len(certificate.encode('utf-8')))
