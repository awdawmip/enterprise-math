"""Integer checks of the P017 shell, its samples and the boundary averaging identity."""
from bisect import bisect_right
from fractions import Fraction
from itertools import accumulate
from math import gcd, isqrt
import json


def primes_up_to(n):
    marked = bytearray(b"\x01") * (n + 1)
    marked[:2] = b"\x00\x00"
    for d in range(2, isqrt(n) + 1):
        if marked[d]:
            marked[d*d::d] = bytes((n - d*d)//d + 1)
    return [p for p in range(3, n + 1, 2) if marked[p]]


def radius(p, num=1, den=1):
    return isqrt(2*p*num//den)


def prime_table_sample(primes, limit, center=False, num=1, den=1):
    eligible = occupied = 0
    for i, p in enumerate(primes):
        if p > limit:
            break
        h = radius(p, num, den)
        if center:
            h = min(h, limit-p)
        eligible += h
        occupied += bisect_right(primes, p + 2*h) - i - 1
    return eligible, occupied


def open_square_check(limit):
    nmax = limit*limit
    least = [0] * (nmax+1)
    for p in range(2, nmax+1):
        if not least[p]:
            for n in range(p, nmax+1, p):
                if not least[n]:
                    least[n] = p
    checked = occupied = 0
    for c in range(3, limit+1):
        shell = {}
        for n in range((c-1)**2+1, c*c):
            shell.setdefault(least[n], []).append(n)
        for r in range(1, isqrt(2*c) + 1):
            p = c-r
            if p < 3 or p % 2 == 0 or least[p] != p or r*r > 2*p:
                continue
            q = c+r
            expected = [p*q] if least[q] == q else []
            assert shell.get(p, []) == expected
            checked += 1
            occupied += bool(expected)
    return checked, occupied


def direct(primes, limit):
    prime_set = set(primes)
    pairs = []
    for p in primes:
        if p > limit:
            break
        for r in range(1, radius(p)+1):
            if p+2*r in prime_set:
                pairs.append((p, r))
    return pairs


def boundary(primes, Y):
    # D(x) counts eligible pairs with p <= x < p+r.
    pairs = direct(primes, 2*Y-1)
    histogram = [0] * (2*Y+2)
    clipped = interior_moment = 0
    for p,r in pairs:
        right = min(2*Y, p+r)
        histogram[p] += 1
        histogram[right] -= 1
        clipped += max(0, right-max(Y, p))
        if Y <= p < 2*Y:
            interior_moment += r
    discrepancy = list(accumulate(histogram))[Y:2*Y]
    assert sum(discrepancy) == clipped
    for x in range(Y, 2*Y):
        if x == Y or x % 97 == 0 or x+1 == 2*Y:
            assert (prime_table_sample(primes,x)[1] -
                    prime_table_sample(primes,x,center=True)[1]) == discrepancy[x-Y]
    return dict(Y=Y, sum_discrepancy=clipped, interior_radius_sum=interior_moment,
                endpoint_correction=clipped-interior_moment, min_D=min(discrepancy),
                max_D=max(discrepancy))


def midpoint_weights(m):
    weights = [Fraction(1,m)]*m
    odd_primes = primes_up_to(m)
    for ell in odd_primes:
        if m % ell == 0:
            for b in range(m):
                ratio = (Fraction(ell,ell-1) if b%ell==0 else
                         Fraction(ell*(ell-2),(ell-1)**2))
                weights[b] *= ratio
    units = [a for a in range(2*m) if gcd(a,2*m)==1]
    counts = [0]*m
    for a in units:
        for b in units:
            counts[(a+b)//2 % m] += 1
    assert weights == [Fraction(v,len(units)**2) for v in counts]
    return list(map(str, weights))


def main():
    limits = [1000, 10000, 100000, 1000000]
    primes = primes_up_to(limits[-1]+2*isqrt(2*limits[-1])+1)
    records = []
    for limit in limits:
        candidates, occupied = prime_table_sample(primes, limit)
        geom, measured = prime_table_sample(primes, limit, center=True)
        cdf = [prime_table_sample(primes,limit,num=i,den=16)[1] for i in (1,4,9,16)]
        records.append(dict(limit=limit, left_candidates=candidates, left_occupied=occupied,
                            center_candidates=geom, center_occupied=measured,
                            discrepancy=occupied-measured, depth_cuts=["1/16","1/4","9/16","1"],
                            depth_prefix_counts=cdf))
    small = open_square_check(501)
    assert small == prime_table_sample(primes,501,center=True)
    pairs = direct(primes, 5000)
    for cut in [Fraction(0),Fraction(1,16),Fraction(1,4),Fraction(1,2),Fraction(1)]:
        for limit in [17, 113, 1000, 5000]:
            for center in [False, True]:
                expected = sum((p+r if center else p) <= limit and
                               r*r*cut.denominator <= 2*p*cut.numerator for p,r in pairs)
                assert expected == prime_table_sample(primes,limit,center,cut.numerator,cut.denominator)[1]
    for modulus in range(1,73):
        midpoint_weights(modulus)
    center_mod_three = [[0,0,0] for _ in range(4)]
    for p,r in direct(primes,100000):
        if p == 3:
            continue
        for idx,i in enumerate((1,4,9,16)):
            if 16*r*r <= i*2*p:
                center_mod_three[idx][(p+r)%3] += 1
    print(json.dumps(dict(midpoint_crt_moduli_checked=72, midpoint_mod_three=dict(
                          limit=100000, prime_factors_coprime_to_6=True,
                          predicted=midpoint_weights(3), depth_prefix_counts=center_mod_three),
                          open_square=dict(max_center=501,checked=small[0],occupied=small[1]),
                          direct_threshold_comparisons=40, samples=records,
                          boundary=[boundary(primes,Y) for Y in (128,512,2048)]),indent=2))


if __name__ == "__main__":
    main()
