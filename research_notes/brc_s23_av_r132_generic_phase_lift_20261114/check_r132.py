#!/usr/bin/env python3
"""R132: constructive exact rational phase-lift witness checker."""
from fractions import Fraction as F
from random import Random


def frac(z): return z-(z.numerator//z.denominator)
def dist(z):
    r=frac(z)
    return min(r,1-r)
def rot_word(alpha,y,m):
    return tuple(int(frac(y+i*alpha)<alpha) for i in range(m))
def original_word(alpha,B,m):
    return tuple(int(frac((B+i)*alpha)<alpha) for i in range(m))
def nearest(z):
    return (z+F(1,2)).numerator//(z+F(1,2)).denominator


def lift(alpha,y,m):
    alpha,y=F(alpha),F(y)
    assert F(0)<alpha<F(1) and F(0)<=y<F(1) and m>=1
    eta=min(dist(y+i*alpha) for i in range(m))
    eta=min(eta,*(dist(y+(i-1)*alpha) for i in range(m)))
    if not eta: raise ValueError('boundary word; use separate exact analysis')
    M=max(1,m-1)
    limit=max(F(M,2)/eta,F(1,2)/min(alpha,1-alpha))
    B=limit.numerator//limit.denominator+1
    k=nearest(B*alpha-y)
    lifted=(F(k)+y)/B
    assert F(0)<lifted<F(1) and abs(lifted-alpha)<=F(1,2*B)
    assert frac(B*lifted)==y
    assert original_word(lifted,B,m)==rot_word(alpha,y,m)
    return B,lifted,eta


def tests():
    rng=Random(13220261114)
    checks=0;maxB=0;examples=[]
    for _ in range(400):
        m=rng.randrange(1,9)
        a=F(rng.randrange(1,40),rng.randrange(40,81))
        y=F(rng.randrange(1,79),rng.randrange(80,160))
        if not F(0)<a<F(1) or not F(0)<=y<F(1):continue
        try:B,w,eta=lift(a,y,m)
        except ValueError:continue
        for shift in (0,1,11,200):
            BB=B+shift; k=nearest(BB*a-y); ww=(F(k)+y)/BB
            assert F(0)<ww<F(1) and original_word(ww,BB,m)==rot_word(a,y,m)
            checks+=1
        maxB=max(maxB,B)
        if len(examples)<3:
            examples.append((str(a),str(y),m,str(eta),B,str(w),rot_word(a,y,m)))
    B=10**100
    for a,y,m in ((F(2,7),F(3,11),7),(F(5,13),F(2,17),8)):
        _,_,eta=lift(a,y,m)
        k=nearest(B*a-y);w=(F(k)+y)/B
        assert original_word(w,B,m)==rot_word(a,y,m)
        checks+=1
    print('R132_GENERIC_PHASE_LIFT_PASS',
        {'checked':checks,'max_base_B':maxB,'huge_B_digits':len(str(B)),'examples':examples})


if __name__=='__main__':tests()
