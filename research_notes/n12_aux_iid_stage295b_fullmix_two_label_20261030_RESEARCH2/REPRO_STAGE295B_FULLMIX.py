#!/usr/bin/env python3
"""Exact rational replay for the Stage295-B randomized two-label shared port witness.

External positive-rational BRC-style two-visit word model. This checker is a
finite witness and diagnostic, not a proof of continuum optimality or native X6.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement

ZERO, ONE, QUARTER = F(0), F(1), F(1, 4)


def source_laws(a):
    h = a * (ONE - a)
    r = (ONE - a) ** 2
    s = a ** 2
    return (h, r, s, h), (h, s, r, h)


def shared_port(theta):
    return ((ONE - theta)**2, theta*(ONE-theta),
            theta*(ONE-theta), theta**2)


def mix(weighted_params):
    assert sum((w for w, _ in weighted_params), ZERO) == ONE
    result = tuple(sum((w * shared_port(p)[i] for w, p in weighted_params), ZERO)
                   for i in range(4))
    assert sum(result, ZERO) == ONE
    return result


def tv(a, b):
    return sum((abs(x-y) for x, y in zip(a, b)), ZERO) / 2


def risk(p0, p1, q):
    return (tv(p0, q) + tv(p1, q)) / 2


def simplex(n, d=4):
    if d == 1:
        yield (n,)
    else:
        for k in range(n+1):
            for rest in simplex(n-k, d-1):
                yield (k,) + rest


print('STAGE295B_FULLMIX_TWO_LABEL / Fraction exact')
for a in (F(0), F(1, 8), F(1, 4), F(3, 8), F(1, 2)):
    p0, p1 = source_laws(a)
    qmid = tuple((x+y)/2 for x, y in zip(p0, p1))
    uniform = shared_port(F(1, 2))
    free = F(1, 2) - a
    physical = (ONE-a)**2 - QUARTER
    gap = (F(1, 2)-a)**2
    assert sum(p0, ZERO) == sum(p1, ZERO) == ONE
    assert risk(p0, p1, qmid) == free == tv(p0, p1)/2
    assert risk(p0, p1, uniform) == physical == free+gap
    assert qmid[1] == qmid[2] == F(1,2)-a*(ONE-a)
    assert qmid[1] > QUARTER if a != F(1,2) else qmid[1] == QUARTER
    if ZERO < a < F(1, 2):
        assert all(x > ZERO for x in p0+p1)
    print(f'a={str(a):>3} free={str(free):>4} mixed_physical={str(physical):>4} gap={str(gap):>4}')

# All 969 rational unrestricted kernels with denominator 16 (independent
# enumeration, not used as proof of the continuous unrestricted optimum).
a = F(1, 4)
p0, p1 = source_laws(a)
observed = min(risk(p0, p1, tuple(F(x,16) for x in nums))
               for nums in simplex(16))
assert observed == F(1,4)
assert sum(1 for _ in simplex(16)) == 969
print('free_16_simplex_grid=969 kernels, exact_optimum=', observed)

# Exhaust all 70 five-node pre-mixtures with weights in {0,1/4,1/2,3/4,1}
# and common two-use parameter; also check individual conditional source risk,
# which covers source-dependent choices of such mixes.
points = [F(0), F(1,4), F(1,2), F(3,4), F(1)]
count=0
for weights in simplex(4, len(points)):
    q = mix([(F(w,4), p) for w,p in zip(weights, points) if w])
    assert q[1] == q[2] <= QUARTER
    assert tv(p0,q) >= F(5,16)
    assert tv(p1,q) >= F(5,16)
    assert risk(p0,p1,q) >= F(5,16)
    count += 1
assert count == 70
print('mixed_5node_weight4_grid=',count,'exact_optimum=',F(5,16))

# A strict negative covariance in the free-LP midpoint, despite individual
# source paths and physical optimum all having strictly positive probabilities.
qmid = tuple((x+y)/2 for x,y in zip(p0,p1))
mean1 = qmid[2]+qmid[3]
mean2 = qmid[1]+qmid[3]
cov = qmid[3]-mean1*mean2
assert qmid == (F(3,16),F(5,16),F(5,16),F(3,16))
assert cov == -F(1,16)
assert qmid[0]*qmid[3]-qmid[1]*qmid[2] == -F(1,16)
assert qmid[1] > QUARTER
print('free_midpoint=',','.join(map(str,qmid)),'covariance=',cov)

# Two-visit mixture characterization: a positive-covariance example admits
# an explicit rational two-atom reconstruction at {0, d/m}.
original=mix([(F(1,2),F(1,4)),(F(1,2),F(3,4))])
m=original[2]+original[3]
d=original[3]
w=m*m/d
recovered=mix([(ONE-w,ZERO),(w,d/m)])
assert original == recovered == (F(5,16),F(3,16),F(3,16),F(5,16))
assert w == F(4,5) and d/m == F(5,8)
print('rational_2atom_reconstruction=1/5@0 + 4/5@5/8')
print('STAGE295B_FULLMIX_TWO_LABEL_EXACT_PASS')
