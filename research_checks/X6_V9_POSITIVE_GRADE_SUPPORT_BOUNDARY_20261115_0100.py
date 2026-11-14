#!/usr/bin/env python3
"""Exact positive six-axis relative-observer support/weight audit; P000 signed-native axes are not quotiented."""
from math import comb, factorial, prod
from itertools import product

DIM = 6

def compositions(m, d=DIM):
    if d == 1:
        yield (m,)
    else:
        for k in range(m + 1):
            for tail in compositions(m - k, d-1):
                yield (k,) + tail

def canonical(v):
    base = min(v)
    return tuple(x-base for x in v)

def support(m, a):
    """Correct V9 positive occurrence support on A6_D; never merely m modulo 6."""
    if len(a) != DIM or min(a) != 0 or any(type(v) is not int or v < 0 for v in a):
        return False
    s = sum(a)
    return m >= s and (m-s) % DIM == 0

def mass(m, a):
    if not support(m,a):
        return 0
    k = (m-sum(a)) // DIM
    return factorial(m)//prod(factorial(x+k) for x in a)

def verify():
    for m in range(0,11):
        counts = list(compositions(m))
        assert len(counts) == comb(m+5,5)
        observed = {canonical(c) for c in counts}
        assert len(observed) == comb(m+5,5), "At fixed m, can6 is injective on occurrence histograms"
        assert all(support(m,a) for a in observed)
        assert sum(mass(m,a) for a in observed) == 6**m
        for a in observed:
            k=(m-sum(a))//DIM
            assert tuple(x+k for x in a) in counts
        false_candidate = (m+DIM,0,0,0,0,0)
        assert sum(false_candidate)%DIM == m%DIM, "grade matches"
        assert not support(m,false_candidate) and mass(m,false_candidate)==0
    a=(7,0,0,0,0,0)
    assert sum(a)%6==1 and not support(1,a)
    assert support(7,a) and mass(7,a)==1
    a=(1,0,0,0,0,0)
    assert support(1,a) and mass(1,a)==1
    print('PASS_X6_V9_POSITIVE_GRADE_REACHABILITY_GATE')
    print('m=0..10: reachable observer endpoints C(m+5,5); total weighted-free N-BRC mass 6^m')
    print('false grade-only candidate m=1,a=(7,0,0,0,0,0); k=-1 and N_m=0')

if __name__ == '__main__':
    verify()
