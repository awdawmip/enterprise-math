"""Exact checks of the signed-width, height-coordinate and valuation formulas."""
from fractions import Fraction as Q
from math import prod
from functools import cache


def rising(x, d):
    return prod(range(x, x + d))


@cache
def a(c):
    return prod((Q(4 * n + 5, 4 * (n + 5)) for n in range(3, c+1)), start=Q(1))


def v2(x):
    def trailing(n):
        return (n & -n).bit_length() - 1
    return trailing(x.numerator) - trailing(x.denominator)


def native_block(k, c, v):
    rho = Q(k + 4*v, k + v)
    tau = Q(28*(k+4*v)*(k-1+4*v),(4*k+v)*(k-1+v))
    for j in range(v+1,c+1):
        rho *= Q(k+4*j,4*(k+j))
        tau *= Q(k+4*j,4*(4*k+j))
    return rho, tau


def tail(w):
    y = prod((Q(4*j+1, 4*(j+1)) for j in range(3, w+1)), start=Q(1))
    x = Q(840, (w+2)*(w+3)*(w+4))
    return [y*(x*a+b)/(1+x*y*a) for a,b in
            [(Q(3,32),Q(15,32)),(Q(3,2),Q(15,8)),(Q(6),Q(3))]]


def normalized(c, v):
    av = Q(4*v+5,v+5)/a(v)
    tv = av*28*(4+4*v)*Q(rising(v+5,15),v+4)
    return av,tv


def check(last=30):
    widths,order = 0,0
    for c in range(2,last+1):
        assert v2(a(c)) == -3*c + 3 + (c+5).bit_count()
        cache_d = []
        for v in range(2,c+1):
            rho, tau = native_block(5,c,v)
            av,tv=normalized(c,v)
            aa = a(c)
            assert aa*av==rho
            assert aa*tv/rising(c+6,15)==tau
            for w in range(2,v+1):
                r,t=native_block(3,v,w)
                inner=[(r+t*q)/(1+t*q) for q in tail(w)]
                outer=[(rho+tau*q)/(1+tau*q) for q in inner]
                width=tv*(max(inner)-min(inner))
                observed=max(1/(1-z) for z in outer)-min(1/(1-z) for z in outer)
                if max(outer)>1:
                    observed=-observed
                assert aa*width/(rising(c+6,15)*(1-aa*av)) == observed
                widths+=1
                cache_d.append((v,av,width,observed))
        # Compare c<=15, across every pair with a different first landing.
        if c<=15:
            for i,(v,av,d,obs) in enumerate(cache_d):
                for u,au,e,obs2 in cache_d[:i]:
                    if v==u:
                        continue
                    collision_test=d-e==a(c)*(d*au-e*av)
                    assert collision_test==(obs==obs2)
                    lv, lu = d/av, e/au
                    S = lv.numerator*lu.denominator
                    T = lu.numerator*lv.denominator
                    assert collision_test == (S/au - T/av == aa*(S-T))
                    order+=1
    print("signed widths",widths,"pair predicates, including shared-factor form",order,
          "dyadic product values",last-1)


if __name__=="__main__":
    check()
