#!/usr/bin/env python3
"""Exact author-side six-axis signed native lift adapter, self-contained.

No external project-module import or formal Source/Driver admission is claimed.
The input is a *raw relative displacement readout* rho(z) in N^6 with min 0,
the native squared component norm G, and one bit [sum(z)>=0].  The
returned signed Z^6 tuple is not a final displayed Cell address.
"""
from itertools import product
from math import factorial, isqrt

D = 6


def rho(z):
    h = min(z)
    return tuple(x-h for x in z)


def square(z):
    return sum(x*x for x in z)


def shortest_brc(z):
    t = sum(map(abs,z))
    den = 1
    for x in z:
        den *= factorial(abs(x))
    return factorial(t)//den


def dominant(z):
    m = max(map(abs,z))
    return frozenset((i+1, 1 if x>0 else -1)
                     for i,x in enumerate(z) if m and abs(x)==m)


def candidate_depths(r,g):
    """Exact native depths compatible with (rho,G), at most two."""
    r = tuple(r)
    if len(r) != D or any(type(x) is not int or x<0 for x in r) or min(r)!=0:
        raise ValueError('six min-zero nonnegative exact integer components required')
    if type(g) is not int or g<0:
        raise ValueError('exact nonnegative native squared norm required')
    R,Q=sum(r),sum(x*x for x in r)
    w = R*R+D*(g-Q)
    if w<0: return ()
    t=isqrt(w)
    if t*t!=w: return ()
    hs=set()
    for s in (-t,t):
        if (s-R)%D==0:
            h=(s-R)//D
            z=tuple(x+h for x in r)
            if rho(z)==r and square(z)==g: hs.add(h)
    return tuple(sorted(hs))


def recover_native(r,g,nonnegative_signed_total):
    """One bit specifying the sign of sum_i z_i chooses a unique lift."""
    if type(nonnegative_signed_total) is not bool:
        raise ValueError('one exact Boolean orientation bit required')
    r=tuple(r)
    hs=candidate_depths(r,g)
    valid=[h for h in hs if (sum(r)+D*h>=0)==nonnegative_signed_total]
    if len(valid)!=1:
        raise ValueError('inconsistent observer / norm / orientation bit')
    z=tuple(x+valid[0] for x in r)
    return z


def recover_oriented(r,g,nonnegative_signed_total):
    """Scoped finite-path adapter: native lift, dominant set, exact BRC."""
    z=recover_native(r,g,nonnegative_signed_total)
    return z,dominant(z),shortest_brc(z)


def check():
    n=0;two=0;ambiguous_dom=0;observed_pairs={}
    for z in product(range(-3,4),repeat=D):
        r=rho(z);g=square(z);b=(sum(z)>=0)
        hs=candidate_depths(r,g)
        assert min(z) in hs and len(hs) in (1,2)
        x,dom,brc=recover_oriented(r,g,b)
        assert x==z and dom==dominant(z) and brc==shortest_brc(z)
        if len(hs)==2:
            two+=1
            counterpart=tuple(v+hs[0] for v in r) if min(z)!=hs[0] else tuple(v+hs[1] for v in r)
            assert sum(z)==-sum(counterpart)!=0
            assert recover_oriented(r,g,not b)[0]==counterpart
            if dom!=dominant(counterpart): ambiguous_dom+=1
        observed_pairs.setdefault((r,g),set()).add(min(z))
        n+=1
    # The previous counterexample is repaired; all other stated observables coincide.
    x=(-1,-1,-1,2,2,2);y=(-2,-2,-2,1,1,1)
    assert rho(x)==rho(y) and square(x)==square(y)==15
    assert shortest_brc(x)==shortest_brc(y)==45360
    assert candidate_depths(rho(x),15)==(-2,-1)
    assert recover_oriented(rho(x),15,True)[0]==x
    assert recover_oriented(rho(x),15,False)[0]==y
    assert dominant(x)!=dominant(y)
    # No integer or norm input may be accepted under silent Boolean coercion.
    for r,g,b in [((True,0,0,0,0,0),1,True),((0,)*6,True,True),
                  ((0,)*6,0,1),((0,)*6,1,True)]:
        try: recover_oriented(r,g,b)
        except ValueError: pass
        else: raise AssertionError(('accepted-invalid',r,g,b))
    # Large parameters are exact, without enumerating possible depths.
    M=10**45; xx=(-M,)*3+(2*M,)*3; yy=(-2*M,)*3+(M,)*3
    gg=15*M*M
    assert candidate_depths(rho(xx),gg)==(-2*M,-M)
    assert recover_native(rho(xx),gg,True)==xx
    assert recover_native(rho(xx),gg,False)==yy
    print('PASS_X6_LP011_LP026_NATIVE_G_ORIENTATION_BIT')
    print('full_signed_cube_7pow6',n,'two_lift_source_points',two,
          'two_lift_points_with_distinct_dominance',ambiguous_dom,
          'distinct_observed_rho_G',len(observed_pairs))
    print('witness_G15_BRC45360_orientation_repairs_both', True)
    print('huge_integer_scale',M,'passed_exactly')

if __name__ == '__main__':
    check()
