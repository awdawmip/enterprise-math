#!/usr/bin/env python3
"""Finite high-precision cross-checks for FULL_ROAD_WINDOW_BRIDGE.md.

These are floating-point checks, not interval certificates; the report supplies
the general proofs. The finite ranges below are the actual reported coverage.
"""
from pathlib import Path
import json
import mpmath as mp

mp.mp.dps = 80


def factor_primes(n):
    factors = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        factors.append(n)
    return factors


def road(a, n):
    return mp.fprod(-mp.expm1(-a * mp.log(p)) for p in factor_primes(n))


def mangoldt(n):
    ps = factor_primes(n)
    return mp.log(ps[0]) if len(ps) == 1 else mp.mpf(0)


def check():
    thicknesses = [mp.mpf(1), mp.mpf(1)/2, mp.mpf(1)/10,
                   mp.mpf(1)/1000, mp.mpf('1e-8')]
    count = 0
    worst = mp.mpf(0)
    for a in thicknesses:
        for n in range(2, 501):
            error = abs(road(a, n)/a - mangoldt(n))
            bound = a * mp.log(n)**2 / 2
            ratio = error / bound
            assert ratio <= 1 + mp.mpf('1e-60')
            worst = max(worst, ratio)
            count += 1

    rows = []
    for theta in [mp.mpf(3)/5, mp.mpf(3)/4, mp.mpf(9)/10]:
        for lam in [mp.mpf(3)/2, mp.mpf(2)]:
            for Y in [mp.mpf(3), mp.mpf(10), mp.mpf(25)]:
                a = Y**(-lam*(1-theta))/(lam*mp.log(Y))**3
                assert 0 < a < 1
                end = Y**lam
                horizons = [Y, (Y+end)/2, end]
                max_n = int(mp.floor(end))
                r = [mp.mpf(0), mp.mpf(1)] + [road(a,n) for n in range(2,max_n+1)]
                v = [mp.mpf(0), mp.mpf(0)] + [mangoldt(n) for n in range(2,max_n+1)]
                for y in horizons:
                    N = int(mp.floor(y))
                    direct = mp.fsum(r[n]/a*(y/n-1) for n in range(2,N+1))
                    prime = mp.fsum(v[n]*(y/n-1) for n in range(2,N+1))
                    # Independently accumulate S_a(t)-1 on its unit intervals.
                    cumulative = mp.mpf(0)
                    integral = mp.mpf(0)
                    for n in range(2,N+1):
                        cumulative += r[n]
                        upper = min(mp.mpf(n+1), y)
                        if upper > n:
                            integral += cumulative*(mp.mpf(1)/n-1/upper)
                    integral *= y/a
                    identity_error = abs(direct-integral)
                    assert identity_error < mp.mpf('1e-65')*max(1,abs(direct))
                    error = abs(direct-prime)
                    bound = a*y*mp.log(y)**3/2
                    assert error <= bound + mp.mpf('1e-65')
                    assert bound <= y**theta/2 + mp.mpf('1e-65')
                    rows.append({
                        'theta':mp.nstr(theta,18),'lambda':mp.nstr(lam,18),
                        'Y':mp.nstr(Y,18),'a_Y':mp.nstr(a,24),'y':mp.nstr(y,24),
                        'error':mp.nstr(error,24),'proved_error_bound':mp.nstr(bound,24),
                        'window_scale':mp.nstr(y**theta,24),
                        'integral_identity_absolute_error':mp.nstr(identity_error,8),
                        'integer_terms':max(0,N-1),
                        'composite_multi_prime_terms':sum(len(factor_primes(n))>=2 for n in range(2,N+1)),
                    })
    return {
        'status':'PASS', 'arithmetic':'mpmath 80 decimal digits; non-interval numerical cross-check',
        'general_proof':'FULL_ROAD_WINDOW_BRIDGE.md',
        'pointwise_cases':count,'pointwise_n_range':[2,500],
        'pointwise_thicknesses':[mp.nstr(a,18) for a in thicknesses],
        'largest_pointwise_error_bound_ratio':mp.nstr(worst,24),
        'window_horizon_cases':len(rows),'window_cases':rows,
    }


if __name__ == '__main__':
    result = check()
    out = Path(__file__).with_name('road_window_bridge_results.json')
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='window_cases'},ensure_ascii=False,indent=2))
