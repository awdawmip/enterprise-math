"""Exact BRC checks of area moments from a two-of-each source restriction."""
from collections import Counter
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import sys

# Accept a checkout or the flat workspace used for this computation.
here = Path(__file__).resolve().parent
previous = [here, here.parent / "craig_path_restriction", here.parent]
for path in previous:
    if (path / "check_weighted.py").is_file():
        sys.path.insert(0, str(path))
        break
from check_weighted import area, load_signed_brc, source_subwords, words


def law_from_comparisons(word):
    h = [i for i,c in enumerate(word) if c == 'X']
    v = [i for i,c in enumerate(word) if c == 'Y']
    a,b,c,d = (int(i < j) for i in h for j in v)
    return Q(a+b+c+d,4), Q(a*b+c*d,2), Q(a*c+b*d,2), Q(a*d+b*c,2)


W2 = ("XXYY","XYXY","XYYX","YXXY","YXYX","YYXX")
MOMENTS = (
    (1,1,1,1),
    (Q(3,4),Q(1,2),Q(1,2),Q(1,2)),
    (Q(1,2),Q(1,2),0,0),
    (Q(1,2),0,Q(1,2),0),
    (Q(1,4),0,0,0),
    (0,0,0,0),
)


def read_profile(profile):
    p,x,y,d = [sum(profile.get(w,0)*row[j] for w,row in zip(W2,MOMENTS))
                  for j in range(4)]
    b = profile.get("XYYX",0) + profile.get("YXXY",0)
    c = profile.get("XYXY",0) + profile.get("YXYX",0)
    assert 2*(x+y-2*d) == b and 4*(p-x-y+d) == c
    return tuple(map(Q,(p,d,b,c)))


def test_finite_words():
    brc = load_signed_brc()
    checked = 0
    for n in range(2,7):
        family = list(words(n))
        assert len(family) == brc.shortest_path_multiplicity((n,n,0,0,0,0))
        avoiding = []
        for w in family:
            norm = comb(n,2)**2
            pairs = Counter(u for _,u in source_subwords(w,2))
            profile = {u:Q(count,norm) for u,count in pairs.items()}
            p,d,b,c = read_profile(profile)
            a = Q(area(w),n*n)
            assert p == a
            assert a*a == d + b/(2*n) + c/(4*n*n)
            if b == 0 and c > 0:
                assert c == Q(4,n*n)
                avoiding.append(w)
            checked += 1
        assert set(avoiding) == {"X"*(n-1)+"YX"+"Y"*(n-1),
                                 "Y"*(n-1)+"XY"+"X"*(n-1)}
    return checked


def four_block(n,u):
    """X-low / Y-low / X-high / Y-high; each X high or Y low with probability u."""
    bins = Counter()
    for h in range(n+1):
        wh = comb(n,h)*(1-u)**h*u**(n-h)
        for v in range(n+1):
            wv = comb(n,v)*(1-u)**v*u**(n-v)
            bins['X'*h+'Y'*(n-v)+'X'*(n-h)+'Y'*v] += wh*wv
    return bins


def three_block(n,t):
    return {'X'*h+'Y'*n+'X'*(n-h): comb(n,h)*t**h*(1-t)**(n-h)
            for h in range(n+1)}


def test_projective_families():
    checks = 0
    for law in (three_block,four_block):
        for t in (Q(1,2),Q(2,3),Q(1,7),Q(1,101)):
            profile = law(2,t)
            p,d,b,c = read_profile(profile)
            j_inf = p-d
            j2 = j_inf-b/4-c/16
            if law is four_block:
                assert (b,c) == (4*t**3*(1-t),4*t*t*(1-t)**2)
                assert j_inf / j2 == 4*(1+t)/(3+t)
            else:
                assert j_inf == 2*j2 and c == 0
            for n in range(2,8):
                law_n = law(n,t)
                assert sum(law_n.values()) == 1
                target = sum(Q(area(w),n*n)**2 * mass for w,mass in law_n.items())
                assert target == d+b/(2*n)+c/(4*n*n)
                deletion = Counter()
                for w,mass in law_n.items():
                    for _,u in source_subwords(w,2):
                        deletion[u] += mass/comb(n,2)**2
                assert deletion == profile
                checks += 1
    return checks


if __name__ == '__main__':
    assert tuple(law_from_comparisons(word) for word in W2) == MOMENTS
    count = test_finite_words()
    print('two-level named-comparison table: 6; deterministic fine words:',count)
    print('exact full two-level restrictions and variance formulas:',test_projective_families())
