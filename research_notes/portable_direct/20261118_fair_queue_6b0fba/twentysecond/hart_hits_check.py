"""Exact shell counts on independently generated small prime samples; standard library."""
from fractions import Fraction
from math import gcd, isqrt
import json


def cube_floor(n):
    left, right = 0, 1 << ((n.bit_length()+2)//3)
    while left+1 < right:
        middle = (left+right)//2
        if middle**3 <= n:
            left = middle
        else:
            right = middle
    return right if right**3 <= n else left


def prime(n):
    return n >= 2 and all(n%d for d in range(2, isqrt(n)+1))


def parameters(p, q):
    n = p*q
    lower = cube_floor(n-1)+1
    upper = cube_floor(8*n)
    return n, lower, upper


def direct(p, q):
    n, lower, upper = parameters(p,q)
    hits = {}
    for k in range(lower,upper+1):
        x = isqrt(4*n*k-1)+1
        residual = x*x-4*n*k
        y = isqrt(residual)
        if y*y == residual:
            a, b = (x-y)//2, (x+y)//2
            assert gcd(a,n)*gcd(b,n) == n and 1 < a <= b < n
            if a%p:
                a,b = b,a
            hits[k] = (a//p, b//q, Fraction(residual,2*x-1))
    return hits


def parameterized(p, q):
    n, lower, upper = parameters(p,q)
    hits = {}
    # Largest possible v in the proven strip v < 2p / cubert(n).
    vmax = cube_floor(8*p**3 // n)
    for v in range(1,vmax+1):
        for u in range((lower+v-1)//v,upper//v+1):
            k = u*v
            x = p*u+q*v
            if (x-1)**2 < 4*n*k:
                assert k not in hits
                hits[k] = u,v,Fraction((p*u-q*v)**2,2*x-1)
    return hits


def case(p,q):
    assert p<q and prime(p) and prime(q)
    n,lower,upper = parameters(p,q)
    assert n>=4**3
    hits = direct(p,q)
    assert hits == parameterized(p,q)
    slopes = sorted({(u//gcd(u,v),v//gcd(u,v)) for u,v,_ in hits.values()})
    assert len(slopes) <= 24 and max(0,len(hits)-12)**3*n <= 8*p**3
    kfloor = cube_floor(n)
    near = 3*Fraction(kfloor+1,p) + 2*Fraction(q-p,kfloor) < 1
    if near:
        # Independently impose the strict diagonal condition
        # t(sqrt(q)-sqrt(p))^2 < 1 by comparison of nonnegative integers.
        diagonal = [t*t for t in range(isqrt(upper)+1)
                    if lower<=t*t<=upper and (t*(p+q)-1)**2 < 4*n*t*t]
        assert sorted(hits) == diagonal
    return {"prime_pair": [p,q], "shell": [lower,upper], "hit_count":len(hits),
            "slopes":slopes, "hit_multipliers":sorted(hits),
            "maximum_score":str(max((s for _,_,s in hits.values()),default=0)),
            "sufficient_diagonal_test_passed": near}


def main():
    primes = [p for p in range(3,152,2) if prime(p)]
    count = total = max_slopes = max_hits = 0
    many_slopes = None
    for i,p in enumerate(primes):
        for q in primes[i+1:]:
            if p*q < 64:
                continue
            d = case(p,q)
            count += 1
            total += d["hit_count"]
            max_hits = max(max_hits,d["hit_count"])
            if len(d["slopes"]) > max_slopes:
                max_slopes = len(d["slopes"])
                many_slopes = d
    examples = [case(p,q) for p,q in [(1009,1013),(1013,1031),(1009,1031),(10007,10009)]]
    print(json.dumps({"small_prime_limit":151,"semiprimes_checked":count,
                      "exact_hits":total,"maximum_hits_per_sample":max_hits,
                      "maximum_observed_slopes":max_slopes,"first_maximum_slope_case":many_slopes,
                      "additional_close_prime_examples":examples},indent=2))


if __name__=="__main__":
    main()
