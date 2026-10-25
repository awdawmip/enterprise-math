"""Exact author-side verification of finite-ring blind-observer collision moments.

Portable algebra only; NOT an authenticated native CM/divided-power experiment,
not formal checking, and not independent mathematical review.
"""
from collections import Counter


def predicted_power_sum(p: int, r: int, q: int) -> int:
    assert p % 2 == 1 and r >= 2 and q >= 1
    m = r - 2
    return p**q * (
        p ** (q * (m // 2))
        + 2 ** (q - 1) * (p - 1)
        * sum(p ** (m - 2 * e - 1 + q * e) for e in range((m - 1) // 2 + 1))
    )


def check_case(p: int, r: int, a: int, b: int, u: int, v: int):
    modulus = p**r
    m = r - 2
    output_modulus = p**m
    F = u*a + v*b
    L = 4*u*b + 2*v*a
    assert (a*a - 2*b*b) % p != 0
    assert F % p != 0 and L % p == 0
    ell = L // p
    norm = (a*a - 2*b*b) % modulus

    # Path 1: explicitly retain both marked source coefficients and evaluate f.
    fibers = Counter()
    for x in range(p ** (r-1)):
        t = p*x
        inv = pow((1 - 2*t*t) % modulus, -1, modulus)
        aa = (a*(1+2*t*t) + 4*b*t)*inv % modulus
        bb = (b*(1+2*t*t) + 2*a*t)*inv % modulus
        assert (aa*aa-2*bb*bb) % modulus == norm
        observed_difference = ((u*aa+v*bb)-F) % modulus
        assert observed_difference % (p*p) == 0
        yy = observed_difference // (p*p)
        assert 0 <= yy < output_modulus
        fibers[yy] += 1

    # Path 2: independently count all roots of square map at declared depth.
    squares = Counter(z*z % output_modulus for z in range(output_modulus))
    for y in range(output_modulus):
        D = (ell*ell+16*F*y+8*p*p*y*y) % output_modulus
        assert fibers[y] == p*squares[D]

    # Every power-sum moment uses the full positive-integer fiber histogram.
    moments = {}
    for q in range(1,5):
        observed = sum(n**q for n in fibers.values())
        expected = predicted_power_sum(p,r,q)
        assert observed == expected, (p,r,q,observed,expected)
        moments[q] = observed
    N = p**(r-1)
    assert moments[1] == N
    assert moments[2] == N*(p+m*(p-1))
    assert (moments[2]-N)//2 == N*(m+1)*(p-1)//2
    return {
        'p':p,'r':r,'source_count':N,'observed_values':len(fibers),
        'nonzero_fiber_histogram':dict(sorted(Counter(fibers.values()).items())),
        'moment_2':moments[2],'moment_3':moments[3],
        'pair_probability_numerator':p+m*(p-1),
        'pair_probability_denominator':N,
    }


def main():
    cases = [
        (13,2,2,3,2,7),
        (13,3,2,3,2,7),
        (13,4,2,3,2,7),
        (13,5,2,3,2,7),
        (19,3,2,3,2,13),
        (19,4,2,3,2,13),
        (373,3,92060,21788,302,-308),
    ]
    for case in cases:
        print('PASS', check_case(*case))

if __name__ == '__main__':
    main()
