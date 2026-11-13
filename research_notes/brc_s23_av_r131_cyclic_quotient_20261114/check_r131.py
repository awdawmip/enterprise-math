#!/usr/bin/env python3
"""R131 exact cyclic period quotient; all arithmetic is Fraction / integer."""
from bisect import bisect_left
from fractions import Fraction as F
from math import gcd
from functools import reduce
from random import Random


def frac(x):
    return x - x.numerator // x.denominator


def bit(x, a, d, e, i, t):
    return int(frac(x + (a + i*d)*t) < frac(e*t))


def word(x, a, d, e, m, t):
    return tuple(bit(x, a, d, e, i, t) for i in range(m))


def affine_roots(intercept, slope, lo, hi):
    if not slope:
        return set()
    u, v = intercept + slope*lo, intercept + slope*hi
    lower = min(u, v).numerator // min(u, v).denominator
    upper = -( -max(u,v).numerator // max(u,v).denominator )
    return {z for k in range(lower, upper+1)
            if lo < (z := (F(k)-intercept)/slope) < hi}


def cuts(x, a, d, e, m, lo=F(0), hi=F(1)):
    pts = affine_roots(F(0), e, lo, hi)
    for i in range(m):
        slope = a+i*d
        pts |= affine_roots(x, slope, lo, hi)
        pts |= affine_roots(x, slope-e, lo, hi)
    return sorted(pts)


def normalized_params(A, d, E):
    g = reduce(gcd, (abs(A),abs(d),abs(E)))
    if g == 0: return (1,0,0,0)
    return (g,A//g,d//g,E//g)


class CyclicIndex:
    def __init__(self, x, A, d, E, m):
        self.x, self.g, self.a, self.b, self.e, self.m = F(x), *normalized_params(A,d,E), m
        self.cuts=cuts(self.x,self.a,self.b,self.e,m)
        self.cuts_set=set(self.cuts)
        self.at_zero=word(self.x,self.a,self.b,self.e,m,F(0))
        ends=[F(0)]+self.cuts+[F(1)]
        self.cells=[word(self.x,self.a,self.b,self.e,m,(p+q)/2) for p,q in zip(ends,ends[1:])]
        self.at_cuts={c:word(self.x,self.a,self.b,self.e,m,c) for c in self.cuts}

    def query(self,theta):
        z=frac(F(theta)*self.g)
        if z==0:return self.at_zero
        if z in self.cuts_set:return self.at_cuts[z]
        return self.cells[bisect_left(self.cuts,z)]

    def vocabulary(self,l,h):
        alpha,beta=self.g*F(l),self.g*F(h)
        assert alpha<beta
        full=set(self.cells)|set(self.at_cuts.values())|{self.at_zero}
        if beta-alpha>1: return full
        boundaries={alpha,beta}
        j0=alpha.numerator//alpha.denominator
        j1=beta.numerator//beta.denominator
        for j in range(j0,j1+2):
            for c in [F(0)]+self.cuts:
                p=j+c
                if alpha<p<beta: boundaries.add(p)
        points=sorted(boundaries)
        observed={word(self.x,self.a,self.b,self.e,self.m,frac((p+q)/2))
                  for p,q in zip(points,points[1:])}
        observed.update(word(self.x,self.a,self.b,self.e,self.m,frac(p))
                        for p in points[1:-1])
        return observed


def brute_vocabulary(x,A,d,E,m,l,h):
    points=[F(l)]+cuts(F(x),A,d,E,m,F(l),F(h))+[F(h)]
    return {word(F(x),A,d,E,m,(p+q)/2) for p,q in zip(points,points[1:])} | {word(F(x),A,d,E,m,p) for p in points[1:-1]}


def tests():
    rng=Random(13120261114)
    samples=0; point_checks=0; boundary_checks=0
    for _ in range(250):
        m=rng.randrange(1,7)
        a,b,e=(rng.randrange(-4,5) for _ in range(3))
        g=rng.randrange(1,8)
        A,d,E=g*a,g*b,g*e
        x=F(rng.randrange(-3,4),rng.randrange(1,7))
        l=F(rng.randrange(-7,8),rng.randrange(1,8))
        width=F(rng.randrange(1,9),rng.randrange(1,8)*g)
        h=l+width
        idx=CyclicIndex(x,A,d,E,m)
        assert idx.vocabulary(l,h)==brute_vocabulary(x,A,d,E,m,l,h),(m,a,b,e,g,x,l,h)
        samples+=1
        for j in range(10):
            t=l+(h-l)*F(j+1,11)
            assert idx.query(t)==word(x,A,d,E,m,t)
            point_checks+=1
        for c in idx.cuts[:10]+[F(0)]:
            t=(c+3)*F(1,idx.g)
            assert idx.query(t)==word(x,A,d,E,m,t)
            boundary_checks+=1
    big=10**100
    idx=CyclicIndex(F(1,5),2*big,big,3*big,7)
    assert idx.g==big and len(idx.cuts)<1000
    assert idx.vocabulary(F(0),F(2))==idx.vocabulary(F(-7, big),F(2))
    for z in range(1,151):
        t=F(z,17*big)+F(13,19)
        assert idx.query(t)==word(idx.x,2*big,big,3*big,7,t)
    witness=None
    for m in range(1,5):
        for a in range(-3,4):
            for b in range(-2,3):
                for e in range(-3,4):
                    if a==b==e==0:continue
                    for x in [F(0),F(1,2),F(1,3)]:
                        z=CyclicIndex(x,a,b,e,m)
                        for c in [F(0)]+z.cuts:
                            full=z.vocabulary(F(-1,5),F(6,5))
                            omit=z.vocabulary(c,c+1)
                            if full!=omit:
                                missing=full-omit
                                assert missing=={z.query(c)}
                                witness=(m,a,b,e,str(x),str(c),sorted(map(str,missing)))
                                break
                        if witness:break
                    if witness:break
                if witness:break
            if witness:break
        if witness:break
    assert witness
    print('R131_CYCLIC_QUOTIENT_PASS', {'small_cases':samples,'query_checks':point_checks,
        'cut_checks':boundary_checks,'huge_scale_digits':len(str(big)),
        'huge_query_checks':150,'primitive_cuts':len(idx.cuts),
        'scaled_v_root_count_on_0_2':str(6*big-1),
        'period_open_endpoint_witness':witness})


if __name__=='__main__':tests()
