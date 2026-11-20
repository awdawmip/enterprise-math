"""Unit177: exact 3-axis relative observer fiber vs native signed BRC.
No remote code is executed. Independent integer oracle for frozen R061/P000 types.
"""
from __future__ import annotations
import itertools
import json
from fractions import Fraction
from math import factorial


def can3(z):
    if len(z) != 3 or any(type(a) is not int for a in z):
        raise ValueError('signed integer triple required')
    lo = min(z)
    return tuple(a-lo for a in z)


def L(z):
    return sum(abs(a) for a in z)


def Q(z):
    return sum(a*a for a in z)


def B(z):
    n = L(z)
    numerator = factorial(n)
    denominator = 1
    for a in z:
        denominator *= factorial(abs(a))
    if numerator % denominator:
        raise RuntimeError('BRC divisibility failed')
    return numerator // denominator


def run():
    validations = 0
    witnesses = []
    for m in range(1, 65):
        a = (-3*m, -3*m, 0)
        b = (m, m, 4*m)
        if can3(a) != can3(b) or L(a) != L(b) or Q(a) != Q(b):
            raise RuntimeError(f'observer collision failed m={m}')
        ba, bb = B(a), B(b)
        r = Fraction(bb, ba)
        claimed = Fraction(factorial(3*m)**2, factorial(m)**2 * factorial(4*m))
        if r != claimed or r < Fraction(3, 2)**m:
            raise RuntimeError(f'exact ratio or lower bound failed m={m}')
        if m > 1 and r <= prev:
            raise RuntimeError(f'ratio not increasing at m={m}')
        prev = r
        validations += 1
        if m <= 6:
            witnesses.append({'m':m,'z_a':list(a),'z_b':list(b),'can3':list(can3(a)),
                'L':L(a),'Q':Q(a),'B_a':ba,'B_b':bb,
                'ratio_numerator':r.numerator,'ratio_denominator':r.denominator})
    groups = {}
    for z in itertools.product(range(-4, 5), repeat=3):
        groups.setdefault((can3(z),L(z),Q(z)),set()).add(B(z))
    collision_groups = sum(len(v)>1 for v in groups.values())
    if collision_groups < 1:
        raise RuntimeError('finite direct native information-loss witness absent')
    # Exact shift invariance and all-zero origin are checked separately.
    for z in itertools.product(range(-3, 4), repeat=3):
        for h in (-4,-1,0,1,4):
            if can3(tuple(t+h for t in z)) != can3(z):
                raise RuntimeError('diagonal observer invariance failed')
            validations += 1
    if can3((0,0,0)) != (0,0,0) or B((0,0,0)) != 1:
        raise RuntimeError('native origin failed')
    return {'schema':'X6_UNIT177_EXACT_INTEGER_CHECK_V1',
      'scope':'signed Z^3 selected X6 slice; R061 relative min-zero observer; native shortest-path BRC',
      'parametric_m_checked':[1,64], 'parametric_cases':64,
      'finite_box':[-4,4], 'finite_points':729,
      'observed_signature_buckets':len(groups),
      'buckets_same_can_L_Q_different_BRC':collision_groups,
      'exact_verifications':validations,
      'witnesses':witnesses,
      'ratio_growth_bound':'B_b/B_a >= (3/2)^m for all m>=1; algebraically proved separately',
      'violations':0,
      'native_R063_rerun':False,
      'historical_LP011_LP019_offender_found':False,
      'project_review':'UNREVIEWED / NOT_ADMITTED'}

if __name__ == '__main__':
    print(json.dumps(run(),sort_keys=True,separators=(',',':')))
