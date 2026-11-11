"""C64 exact endpoint certificates for the first three suffixes and small k.

No external dependencies. Run python suffix_limits.py to print the certificate.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import gcd, lcm
import json


def integer_matrix(entries):
    entries = tuple(map(Q, entries))
    denominator = lcm(*(v.denominator for v in entries))
    values = tuple(v.numerator*(denominator//v.denominator) for v in entries)
    factor = gcd(*values)
    return tuple(v//factor for v in values)


def compose(left, right):
    a, b, c, d = left
    e, f, g, h = right
    return integer_matrix((a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h))


def evaluate(matrix, x):
    a, b, c, d = matrix
    return (a*x+b)/(c*x+d)


def block(r, c, consumption):
    """Probabilities of 5^consumption, 2, 3 from each of the three states."""
    assert r >= 1 and 0 <= consumption <= c-2
    likelihood = []
    K = 2*r+1
    for z, next_z in [(Q(1,4),Q(1)), (Q(1),Q(4)), (Q(4),Q(4))]:
        stock = c
        mass = Q(1)
        for _ in range(consumption):
            mass *= stock*z/(K+stock*z)
            stock -= 1
        mass *= r/(K+stock*z)
        mass *= r/(K-1+stock*next_z)
        likelihood.append(mass)
    a, b, h = likelihood
    return integer_matrix((0, 7*a, b-h, 7*a+h))


def terminal(c):
    """State-2 coordinate after observing the final c-2 fives, without the 7."""
    weights = []
    for z in (Q(1,4),Q(1),Q(4)):
        mass = Q(1)
        for stock in range(c,2,-1):
            mass *= stock*z/(1+stock*z)
        weights.append(mass)
    a, b, h = weights
    # For b<=h the other two coordinates are nondecreasing in u.
    assert b <= h
    return integer_matrix((-h,h,b-h,7*a+h))


def derivative_ratio(matrix, reference, x):
    p, q, s, t = matrix
    a, b, c, d = reference
    return Q(abs(p*t-q*s),abs(a*d-b*c))*((c*x+d)/(s*x+t))**2


def interval_image(matrix, interval):
    return tuple(sorted(evaluate(matrix,u) for u in interval))


def enclose_decimals(interval, places=40):
    scale = 10**places
    a, b = interval
    lower = (a.numerator*scale)//a.denominator
    upper = -((-b.numerator*scale)//b.denominator)
    def fmt(n):
        return f"{n//scale}.{n%scale:0{places}d}"
    return [fmt(lower),fmt(upper)]


def all_gaps(k):
    # Stars and bars for k-1 fives in k+1 slots.
    size = 2*k-1
    for positions in combinations(range(size),k):
        boundaries = (-1,)+positions+(size,)
        yield tuple(q-p-1 for p,q in zip(boundaries,boundaries[1:]))


def total_variation(k,gaps):
    c = k+1-gaps[0]
    endpoints = (Q(0),Q(1))
    for r,m in zip(range(k-1,0,-1),gaps[1:-1]):
        endpoints = interval_image(block(r,c,m),endpoints)
        c -= m
    assert gaps[-1] == c-2
    low, high = interval_image(terminal(c),endpoints)
    return high-low


def main():
    variants = {
        "A": (1,0,0),
        "B": (0,1,0),
        "C": (0,0,1),
    }
    matrices = {}
    for name,(m2,m1,last) in variants.items():
        matrix = compose(block(1,3-m2,m1),block(2,3,m2))
        matrices[name] = compose(terminal(2+last),matrix)
    assert matrices == {
        "A": (-115,124096,-51520,27872768),
        "B": (207,12152,24426,1074896),
        "C": (828,87776,267237,11696360),
    }
    incoming = (Q(0),Q(1))
    prefix = (1,0,0,1)
    bounds = {}
    for k in range(3,21):
        if k>3:
            prefix = compose(prefix,block(k-1,k,1))
        new_interval = interval_image(prefix,(Q(0),Q(1)))
        assert incoming[0] <= new_interval[0] < new_interval[1] <= incoming[1]
        incoming = new_interval
        row = {}
        for variant in ("B","C"):
            h = sorted(derivative_ratio(matrices[variant],matrices["A"],u)
                       for u in incoming)
            assert h[1] < (16 if variant=="B" else 25)
            if k>=4:
                lo,hi = (Q(15031228,10**6),Q(15031823,10**6)) if variant=="B" else (Q(23519700,10**6),Q(23520636,10**6))
                assert lo < h[0] <= h[1] < hi
            if k in (3,4,10,20):
                row[variant] = enclose_decimals(h)
        if row:
            bounds[k] = row
    small = {}
    for k in (2,3):
        ranked = sorted((total_variation(k,word),word) for word in all_gaps(k))
        assert all(a[0]<b[0] for a,b in zip(ranked,ranked[1:]))
        small[k] = [dict(gaps=g,total_variation=str(v),ratio=str(v/ranked[0][0]))
                    for v,g in ranked]
    assert small[2][1]['gaps']==(0,1,0) and small[3][1]['gaps']==(0,0,2,0)
    return dict(suffix_matrices=matrices,ratio_enclosures=bounds,
                suffix_limit_note="Bounds for k enclose all later ratios and their limit.",
                small_ranking=small)


if __name__=="__main__":
    print(json.dumps(main(),indent=2))
