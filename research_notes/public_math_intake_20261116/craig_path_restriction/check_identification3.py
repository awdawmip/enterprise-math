"""Rational certificates for the two-colour subword tower's information bounds."""
from fractions import Fraction as Q
from math import factorial, prod

from check_weighted import load_signed_brc, words
from check_deletion import operator
from check_coherent import positive_root_coordinates, sqrt_enclosure


def model_word_probability(word, eps):
    # Named rank density f_X(t)=1+eps*(2*t-1) and f_Y(t)=1-eps*(2*t-1).
    # The ordered path contributes a simplex integral, evaluated via polynomial primitives.
    p = [Q(1)]
    for c in word:
        slope = eps if c == 'X' else -eps
        nxt = [Q(0)] * (len(p)+2)
        for j, coeff in enumerate(p):
            nxt[j+1] += coeff*(1-slope)/(j+1)
            nxt[j+2] += coeff*2*slope/(j+2)
        p = nxt
    return sum(p)*factorial(word.count('X'))*factorial(word.count('Y'))


def check_sqrt_stability():
    brc = load_signed_brc()
    levels = 0
    for eps in [Q(0), Q(1,7), Q(1,4), Q(3,4)]:
        previous = None
        for n in range(1,6):
            paths = list(words(n))
            assert len(paths) == brc.shortest_path_multiplicity((n,n,0,0,0,0))
            law = {w:model_word_probability(w,eps) for w in paths}
            assert min(law.values()) > 0 and sum(law.values()) == 1
            if n == 1:
                assert law['XY'] == Q(1,2)-eps/3
            if n == 2:
                gap = law['XXYY'] + law['YYXX'] - Q(1,3)
                assert gap == 4*eps**2/15
                assert (eps/3)**2 == Q(5,12)*gap
            if previous:
                pushed = {w:Q(0) for w in previous}
                for w,p in law.items():
                    for u,c in operator(w,n-1).items():
                        pushed[u] += p*c / n**2
                assert previous == pushed
            levels += 1
            previous = law
    return levels


def interval_product(a,b):
    endpoints = [x*y for x in a for y in b]
    return min(endpoints), max(endpoints)


def interval_add(a,b):
    return a[0]+b[0], a[1]+b[1]


def alternating_phase_distance_bounds(nodes, scale):
    # nodes are integers in [0,scale], scale a power of two.
    weights = [Q(1,prod(v-u for u in nodes if u!=v)) for v in nodes]
    total = sum(x for x in weights if x>0)
    weights = [w/total for w in weights]
    for j in range(len(nodes)-1):
        assert sum(w*v**j for w,v in zip(weights,nodes)) == 0
    real,imag=positive_root_coordinates(4*scale)
    point=((Q(1),Q(1)),(Q(0),Q(0))); z={0:point}
    for i in range(1,scale+1):
        a,b=point
        neg=interval_product(b,imag)
        point=(interval_add(interval_product(a,real),(-neg[1],-neg[0])),
               interval_add(interval_product(a,imag),interval_product(b,real)))
        z[i]=point
    coord=[]
    for dim in range(2):
        s=(Q(0),Q(0))
        for i,w in zip(nodes,weights):
            s=interval_add(s,interval_product((w,w),z[i][dim]))
        coord.append(s)
    low_sq=high_sq=Q(0)
    for lo,hi in coord:
        low_sq += min(abs(lo),abs(hi))**2 if lo*hi>0 else 0
        high_sq += max(abs(lo),abs(hi))**2
    return sqrt_enclosure(low_sq)[0],sqrt_enclosure(high_sq)[1]


def check_minimax():
    # Exact degree 2 witness at 0,1/4,3/4,1, and level-1 normal direction.
    lo,hi=alternating_phase_distance_bounds([0,1,3,4],4)
    print('K=2 diameter lower witness, enclosure in millionths:',
          (lo*10**6).__floor__(), (hi*10**6).__ceil__())
    assert Q(38,1000) < lo < hi < Q(40,1000)
    reports = []
    for k in (2,4,8,10):
        n=k+1
        diameter=Q(4, 2**n*factorial(n))
        reports.append((k,diameter))
        assert 2*Q(1,2*n)**n <= diameter
    return reports


if __name__ == '__main__':
    print('exact near-uniform positive model laws:',check_sqrt_stability())
    print('universal diameter upper bounds:',check_minimax())
