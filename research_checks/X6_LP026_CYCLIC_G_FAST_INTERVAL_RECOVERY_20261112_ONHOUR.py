#!/usr/bin/env python3
"""Exact logarithmic-time native norm recovery for a cyclic common-depth observer.

Self-contained research checker: deliberately does NOT claim imported-source integration
with experiments/.../x6_cover.py.  Uses the signed six-axis path-domain model.
"""
from collections import defaultdict

D = 6

class NoReachableNativeLift(ValueError):
    pass

class AmbiguousNativeNorm(ValueError):
    pass


def _validate(relative, depth, modulus, word_length):
    r = tuple(relative)
    if len(r) != D or any(type(x) is not int or x < 0 for x in r) or min(r) != 0:
        raise ValueError("expected six exact nonnegative min-zero coordinates")
    if type(depth) is not int or type(modulus) is not int or modulus < 0:
        raise ValueError("invalid exact depth / modulus")
    if type(word_length) is not int or word_length < 0:
        raise ValueError("word_length must be nonnegative")
    return r


def native_lift_interval(relative, word_length):
    """Return all reachable integer depths as a closed interval, or None.

    Parity is constant under diagonal lifts because the axis count is even.
    The two endpoint binary searches use convexity of sum_i |r_i+h|.
    """
    r = tuple(relative)
    n = word_length
    if (n - sum(r)) % 2:
        return None
    low, high = -n, n - max(r)
    if low > high:
        return None
    middle = max(low, min(high, -sorted(r)[2]))
    def distance(h):
        return sum(abs(x+h) for x in r)
    if distance(middle) > n:
        return None
    l, u = low, middle
    while l < u:
        h = (l+u)//2
        if distance(h) <= n:
            u = h
        else:
            l = h+1
    first = l
    l, u = middle, high
    while l < u:
        h = (l+u+1)//2
        if distance(h) <= n:
            l = h
        else:
            u = h-1
    return first, l


def recover_native_norm_fast(relative, depth, modulus, word_length):
    """Native sum(z_i^2) if constant across the exact-N cover fibre.

    At most O(6 log(N+1)) integer arithmetic operations, independent of the
    number of possible depth lifts.  Large integer arithmetic is exact.
    """
    r = _validate(relative, depth, modulus, word_length)
    bounds = native_lift_interval(r, word_length)
    if bounds is None:
        raise NoReachableNativeLift((r, depth, modulus, word_length))
    low, high = bounds
    if modulus == 0:
        first = last = depth
        if not (low <= depth <= high):
            raise NoReachableNativeLift((r, depth, modulus, word_length))
    else:
        first = low + (depth-low) % modulus
        if first > high:
            raise NoReachableNativeLift((r, depth, modulus, word_length))
        last = high - (high-depth) % modulus
        count = (last-first)//modulus + 1
        if count > 2 or (count == 2 and 3*(first+last) != -sum(r)):
            raise AmbiguousNativeNorm((r, depth, modulus, word_length))
    return sum((x+first)**2 for x in r)


def recover_native_norm_linear(relative, depth, modulus, word_length):
    """Independent original direct enumeration to test the fast version."""
    r = _validate(relative, depth, modulus, word_length)
    depths = (depth,) if modulus == 0 else (h for h in range(-word_length, word_length+1)
                                             if (h-depth)%modulus == 0)
    vals = set()
    for h in depths:
        z = tuple(x+h for x in r)
        L = sum(abs(x) for x in z)
        if L <= word_length and (word_length-L)%2 == 0:
            vals.add(sum(x*x for x in z))
            if len(vals) > 1:
                raise AmbiguousNativeNorm()
    if not vals:
        raise NoReachableNativeLift()
    return next(iter(vals))


def key(z, m):
    h = min(z)
    return tuple(x-h for x in z), (h if m==0 else h % m)


def test():
    # Deliberately different derivation from direct endpoint-word recurrence.
    dist = {(0,)*D: 1}
    checks = 0
    cls = defaultdict(int)
    for n in range(0, 8):
        for m in range(0, 7):
            keys = {key(z, m) for z in dist}
            for r, d in keys:
                try:
                    a = ("value", recover_native_norm_fast(r, d, m, n))
                except (NoReachableNativeLift, AmbiguousNativeNorm) as e:
                    a = (type(e).__name__,)
                try:
                    b = ("value", recover_native_norm_linear(r, d, m, n))
                except (NoReachableNativeLift, AmbiguousNativeNorm) as e:
                    b = (type(e).__name__,)
                assert a == b, (n, m, r, d, a, b)
                cls[a[0]] += 1
                checks += 1
        if n < 7:
            nxt = defaultdict(int)
            for z, count in dist.items():
                for i in range(D):
                    for d in (-1,1):
                        zz = list(z)
                        zz[i] += d
                        nxt[tuple(zz)] += count
            dist = dict(nxt)
    # Stress fast path with an enormous N but without performing O(N) work.
    try:
        recover_native_norm_fast((0,)*D, 0, 1, 10**12)
    except AmbiguousNativeNorm:
        pass
    else:
        raise AssertionError("large cover must have ambiguous norm")
    assert recover_native_norm_fast((0,)*D, 0, 0, 10**12) == 0
    assert recover_native_norm_fast((0,0,0,1,1,1), 0, 1, 3) == 3
    assert recover_native_norm_fast((0,0,3,2,2,2), 0, 3, 9) == 21
    assert native_lift_interval((0,)*D, 10**12) == (-(10**12//6), 10**12//6)
    for args in [((0,)*D,0,0,1), ((0,1,0,0,0,0),0,2,0), ((0,)*D,9,0,0)]:
        try: recover_native_norm_fast(*args)
        except NoReachableNativeLift: pass
        else: raise AssertionError(("expected no lift",args))
    print("PASS_X6_LP026_CYCLIC_NATIVE_G_FAST", checks, "reachable-key comparisons", dict(cls))
    print("large horizon", 10**12, "executed exactly without scanning depths")
    return checks

if __name__ == "__main__":
    test()
