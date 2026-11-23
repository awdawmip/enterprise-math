"""Exact Port-10 six-pair BRC certificate for X6 R144.

Domain B >= 136, 528 <= D <= 1008, w=(136,B,176,D).
Uses only integer arithmetic and fractions.Fraction.
"""
from fractions import Fraction as Q
from itertools import product
from collections import Counter

CORE = {(1, 0, 0), (5, -4, 1), (5, -1, 0), (9, -5, 1)}
NEW_B = (4, -1, 0)
NEW_C = (6, -4, 1)

def population():
    return [a for a in product(range(-10, 11), repeat=3)
            if a != (0, 0, 0)
            and max(sum(max(v, 0) for v in a),
                    sum(max(-v, 0) for v in a)) <= 10
            and next(v for v in a if v != 0) > 0]

def gaps(a):
    x, y, z = a
    h = (0, x + 3*y + 6*z, 3*x + 12*y + 30*z,
         7*x + 39*y + 126*z)
    return tuple(abs(h[j] - h[i]) for i in range(4) for j in range(i+1,4))

A = population()
G = {a: gaps(a) for a in A}

def cap(B, D):
    return (136+B, 312, 136+D, B+176, B+D, 176+D)

def F(a, B, D):
    return max(Q(g, s) for g, s in zip(G[a], cap(B, D)))

def near(B, D):
    eta = min(F(a, B, D) for a in A)
    return eta, {a for a in A if 2*F(a, B, D) < 3*eta}

def predicted(B,D):
    s = set(CORE)
    if D > max(Q(1880,3), 832-B): s.add(NEW_B)
    if D > 696: s.add(NEW_C)
    return s

def run():
    assert len(A) == len(G) == 1935
    assert CORE | {NEW_B, NEW_C} <= G.keys()
    assert G[NEW_B] == (1,0,11,1,12,11)
    assert G[NEW_C] == (0,0,12,0,12,12)
    # A B-independent observation can certify the optimizer everywhere.
    # At upper D=1008, all three B-independent denominators are largest.
    lower = Counter()
    for a,g in G.items():
        js = [j for j in (1,2,5)
              if 104*g[j] >= cap(Q(136),Q(1008))[j]]
        assert js, ('optimizer_lower',a,g)
        lower[js[0]] += 1
    # The witness's constant pair (0,2) is g_02=3 with s_02=312.
    opt = (9,-5,1)
    assert G[opt][1] == 3 and cap(Q(136),Q(528))[1] == 312
    assert F(opt,Q(136),Q(528)) == Q(1,104)
    # Increasing B or D can only decrease its other five pair-scores.
    # Hence eta <= 1/104, and the previous certificate gives eta >=1/104.
    assert all(F(a,Q(136),Q(528)) < Q(3,208) for a in CORE)
    # Across an unbounded B-ray, pair indices 1,2,5 are independent of B.
    # Their denominators maximize at D=1008. One fixed pair excludes each
    # outsider other than the two explicitly classified newcomers.
    outside = Counter()
    for a,g in G.items():
        if a in CORE | {NEW_B, NEW_C}:
            continue
        js = [j for j in (1,2,5)
              if 208*g[j] >= 3*cap(Q(136),Q(1008))[j]]
        assert js, ('outsider_exclusion',a,g)
        outside[js[0]] += 1
    assert sum(outside.values()) == 1929
    # Exact positive-B slices and every relevant equality boundary.
    samples = 0
    for B in (Q(136), Q(137), Q(150), Q(200), Q(616,3),
              Q(240), Q(1000), Q(10**6)):
        wall = max(Q(1880,3), Q(832)-B)
        choices = [Q(528), Q(600), Q(1880,3), Q(696), Q(800), Q(1008),
                   wall, (wall+Q(528))/2]
        choices += [v for v in (wall-Q(1,100),wall+Q(1,100),
                               Q(696)-Q(1,100), Q(696)+Q(1,100))
                    if Q(528) <= v <= Q(1008)]
        for D in choices:
            eta, actual = near(B,D)
            assert eta == Q(1,104), ('eta',B,D,eta)
            assert actual == predicted(B,D), ('near',B,D,actual^predicted(B,D))
            samples += 1
    print('R144 UNBOUNDED-B TWO-ENTRY EXACT FAN CERTIFICATE PASS')
    print('population',len(G),'optimizer_lower_pairs',dict(lower),
          'permanent_outsider_exclusion_pairs',dict(outside))
    print('constant_eta',str(Q(1,104)),
          'new_B_entry','D>max(1880/3,832-B)',
          'new_C_entry','D>696')
    print('complete_exact_replays',samples,
          'domain','B>=136, 528<=D<=1008')

if __name__ == '__main__': run()
