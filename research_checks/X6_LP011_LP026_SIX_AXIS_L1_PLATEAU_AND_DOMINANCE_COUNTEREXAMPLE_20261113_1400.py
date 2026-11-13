#!/usr/bin/env python3
"""X6 signed native / relative observer: an exact six-axis L1-depth plateau.

Author-side standalone integer regression for a proved 6D statement;
not a replay of any original native benchmark or an admitted Result.
"""
from itertools import product
from math import factorial


def can6(z):
    h = min(z)
    return tuple(x-h for x in z)


def length(z):
    return sum(abs(x) for x in z)


def norm2(z):
    return sum(x*x for x in z)


def brc(z):
    total = length(z)
    den = 1
    for x in z:
        den *= factorial(abs(x))
    return factorial(total)//den


def median_signs(z):
    a = sorted(z)
    return tuple((x > 0)-(x < 0) for x in a[2:4])


def native_signed_dominance(z):
    m = max(map(abs,z))
    return frozenset((i,(x>0)-(x<0)) for i,x in enumerate(z) if m and abs(x)==m)


def test_plateau():
    checked = 0
    flat_profiles = 0
    flat_lifts = 0
    for r in product(range(3),repeat=6):
        if min(r):
            continue
        s=sorted(r)
        lo,hi=-s[3],-s[2]
        minimum=sum(s[3:])-sum(s[:3])
        predicted=set(range(lo,hi+1))
        actual=set()
        for h in range(-6,7):
            z=tuple(x+h for x in r)
            assert can6(z)==r
            assert length(z)>=minimum
            if length(z)==minimum:
                actual.add(h)
            checked+=1
        assert actual==predicted, (r,predicted,actual)
        if hi>lo:
            flat_profiles+=1
            flat_lifts+=len(predicted)
    return checked,flat_profiles,flat_lifts


def test_family():
    witness=None
    checked=0
    for M in range(1,13):
        r=(0,0,0,M,M,M)
        for k in range(M+1):
            z=(-k,-k,-k,M-k,M-k,M-k)
            assert can6(z)==r
            assert length(z)==3*M
            assert brc(z)==factorial(3*M)//(factorial(k)**3*factorial(M-k)**3)
            opposite=(-M+k,-M+k,-M+k,k,k,k)
            assert brc(z)==brc(opposite)
            assert norm2(z)==norm2(opposite)
            checked+=1
        if M==3:
            x=(-1,-1,-1,2,2,2)
            y=(-2,-2,-2,1,1,1)
            assert x!=y
            assert can6(x)==can6(y)==r
            assert length(x)==length(y)==9
            assert brc(x)==brc(y)==45360
            assert norm2(x)==norm2(y)==15
            assert median_signs(x)==median_signs(y)==(-1,1)
            assert native_signed_dominance(x)==frozenset((i,1) for i in (3,4,5))
            assert native_signed_dominance(y)==frozenset((i,-1) for i in (0,1,2))
            witness=(r,x,y,length(x),norm2(x),brc(x))
    assert witness is not None
    return checked,witness


def main():
    exact,profiles,lifts=test_plateau()
    cases,witness=test_family()
    print('PASS_X6_LP011_LP026_SIX_AXIS_L1_MEDIAN_PLATEAU')
    print('six_axis_0_2_residuals_h_minus6_plus6_checks',exact)
    print('flat_profiles',profiles,'flat_lifts',lifts)
    print('M_1_to_12_family_lifts',cases)
    print('exact_counterexample',witness)

if __name__=='__main__':
    main()
