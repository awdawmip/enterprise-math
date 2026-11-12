#!/usr/bin/env python3
"""Exact native-G range on the signed X6 cyclic common-depth fibre.

Author-side executable science; not a native task Result/benchmark.
Frozen mathematical model: X6 signed Z^6 at 59538f585d037d09ef687b28715c4bc1a3f9fe03.
The old fast interval idea is reused, not claimed anew.
"""
from collections import defaultdict

D = 6


def exact_depth_interval(r, n):
    """Closed interval of all depth lifts reachable in exactly n signed steps."""
    r = tuple(r)
    if len(r) != D or min(r) != 0 or any(type(x) is not int or x < 0 for x in r):
        raise ValueError('six exact nonnegative min-zero coordinates required')
    if type(n) is not int or n < 0:
        raise ValueError('nonnegative exact length required')
    if (n - sum(r)) & 1:
        return None
    lo, hi = -n, n - max(r)
    if lo > hi:
        return None
    pivot = max(lo, min(hi, -sorted(r)[2]))
    f = lambda h: sum(abs(x+h) for x in r)
    if f(pivot) > n:
        return None
    a, b = lo, pivot
    while a < b:
        mid = (a+b)//2
        if f(mid) <= n:
            b = mid
        else:
            a = mid+1
    first = a
    a, b = pivot, hi
    while a < b:
        mid = (a+b+1)//2
        if f(mid) <= n:
            a = mid
        else:
            b = mid-1
    return first, a


def native_g_range(r, depth, modulus, n):
    """Return (min_G,max_G,argmin_depth,argmax_depth,lift_count,section_error_range).

    For m=0, the integer depth is retained. For m>=1, it is reduced modulo m.
    No reachable lift raises ValueError. All calculations exact, O(6 log(n+1)).
    """
    r = tuple(r)
    if type(depth) is not int or type(modulus) is not int or modulus < 0:
        raise ValueError('exact depth/modulus required')
    interval = exact_depth_interval(r, n)
    if interval is None:
        raise ValueError('no reachable native lift')
    lo, hi = interval
    if modulus == 0:
        if depth < lo or depth > hi:
            raise ValueError('no reachable native lift')
        first = last = depth
        count = 1
        stride = 1
    else:
        first = lo + ((depth - lo) % modulus)
        if first > hi:
            raise ValueError('no reachable native lift')
        last = hi - ((hi - depth) % modulus)
        stride = modulus
        count = (last-first)//stride + 1
    S = sum(r)
    C = sum(x*x for x in r)
    def g(h):
        return 6*h*h + 2*S*h + C
    # Nearest progression points to the rational vertex h* = -S/6.
    k = max(0, min(count-1, (-S-6*first)//(6*stride)))
    lo_candidates = [first + k*stride]
    if k+1 < count:
        lo_candidates.append(first + (k+1)*stride)
    argmin = min(lo_candidates, key=lambda h: (g(h), h))
    argmax = max((first,last), key=lambda h: (g(h), -h))
    lower, upper = g(argmin), g(argmax)
    return lower, upper, argmin, argmax, count, (lower-C, upper-C)


def key(z, m):
    h = min(z)
    return tuple(x-h for x in z), (h if m==0 else h % m)


def test():
    native = {(0,)*D:1}
    comparisons = 0
    ambiguous = 0
    max_count = 0
    for n in range(9):
        for m in range(8):
            fibers = defaultdict(set)
            for z in native:
                fibers[key(z,m)].add(min(z))
            for (r, h), depths in fibers.items():
                result = native_g_range(r,h,m,n)
                Gs = {sum((x+d)**2 for x in r) for d in depths}
                assert (result[0], result[1]) == (min(Gs),max(Gs)), (n,m,r,h,result,Gs)
                assert result[2] in depths and result[3] in depths
                assert result[4] == len(depths)
                assert result[5] == (min(Gs)-sum(x*x for x in r),max(Gs)-sum(x*x for x in r))
                comparisons += 1
                ambiguous += len(Gs)>1
                max_count = max(max_count,result[4])
        if n<8:
            nxt=defaultdict(int)
            for z, weight in native.items():
                for i in range(D):
                    for d in (-1,1):
                        q=list(z);q[i]+=d
                        nxt[tuple(q)]+=weight
            native=dict(nxt)
    # Same finite-cover key, different G, tight quantitative range.
    assert native_g_range((0,)*D,0,1,6)[:2] == (0,6)
    # Boundary N=9,m=3 has two distinct native endpoints, equal G=21.
    assert native_g_range((0,0,3,2,2,2),0,3,9)[:2] == (21,21)
    # Do not enumerate the 10^12 potential depths.
    lo,hi,_,_,count,error = native_g_range((0,)*D,0,1,10**12)
    assert (lo,hi,count)==(0,6*(10**12//6)**2,2*(10**12//6)+1)
    print('PASS_X6_LP026_CYCLIC_NATIVE_G_RANGE')
    print('independent_exact_fiber_comparisons',comparisons)
    print('nonconstant_native_G_fibers',ambiguous)
    print('maximum_lifts_in_test',max_count)
    print('N6_m1_relative_zero_range',native_g_range((0,)*D,0,1,6))
    print('N9_m3_equal_G_collision',native_g_range((0,0,3,2,2,2),0,3,9))
    print('N_10pow12_m1_numerical_range',lo,hi,count,error)


if __name__=='__main__':
    test()
