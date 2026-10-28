#!/usr/bin/env python3
"""Exact p-local reciprocal reflection for original weighted 216 model.

Author-side verifier only: neither canonical Result nor native H0/B0 execution.
No floating point, no external libraries, no hidden assumptions about p^3 LIFT.
"""
from math import comb, factorial

PRIMES = [7, 13, 19, 31, 37, 43, 61, 67, 73, 79, 97, 103, 109, 127, 139, 151, 157, 163, 181, 193, 199, 211, 373]


def source_terms(p):
    """Independent recurrence for original w_n = (6n+1) C(2n,n)^2 C(3n,n)/216^n."""
    q = p**4
    t = 1
    w = []
    for n in range(p):
        w.append((6*n + 1)*t % q)
        if n + 1 < p:
            numer = (2*n + 1)*(3*n + 1)*(3*n + 2)
            denom = 36*(n + 1)**3
            t = t*numer*pow(denom, -1, q) % q
    return w


def independent_binomial_term(p, n):
    q = p**4
    return ((6*n + 1) * comb(2*n, n)**2 * comb(3*n, n)
            * pow(pow(216, n, q), -1, q)) % q


def verify(p):
    assert p > 3 and p % 6 == 1
    m = (p-1)//6
    q = p**4
    w = source_terms(p)
    for n in range(p):
        # Independent integer factorial route, not the recurrence used above.
        assert w[n] == independent_binomial_term(p, n), (p, n, 'source mismatch')
    for n in range(1, p):
        a2, a3 = (2*n)//p, (3*n)//p
        # Divisible by p^3 for every 1 <= n < p; weight may give an extra p.
        product = w[n]*w[p-n] % q
        assert product % p**3 == 0, (p, n, 'valuation')
        actual = product // p**3
        sgn = -1 if (1+a2+a3) % 2 else 1
        expected = (sgn * factorial(a3) * factorial(2-a3)
                    * (1-36*n*n) * pow(36*n**3, -1, p)) % p
        assert actual == expected, (p, n, actual, expected)
    tail_sum = 0
    reciprocal_sum = 0
    sample = None
    previous_middle = None
    for r in range(m):
        n = 2*m+1+r
        assert n + (p-n) == p
        assert w[n] % p == 0 and w[n] % p**2 != 0, (p, r, 'middle valuation')
        assert w[p-n] % p**2 == 0 and w[p-n] % p**3 != 0, (p, r, 'high valuation')
        middle = (w[n] // p) % p
        if previous_middle is not None:
            rr = r-1
            numer = ((6*rr+11)*(4*m+3+2*rr)*(4*m+4+2*rr)
                     *(3*rr+3)*(3*rr+4)*(3*rr+5))
            denom = (216*(6*rr+5)*(2*m+2+rr)**5)
            assert middle == previous_middle*numer*pow(denom, -1, p) % p, (p, r, 'middle recurrence')
        previous_middle = middle
        high = (w[p-n] // p**2) % p
        kernel = (-(6*r+5)*(2*r+1) * pow(12*n**3, -1, p)) % p
        assert middle*high % p == kernel, (p, r, middle, high, kernel)
        predicted = kernel * pow(middle, -1, p) % p
        assert predicted == high
        reciprocal_sum = (reciprocal_sum + predicted) % p
        tail_sum = (tail_sum + high) % p
        if r == 0:
            sample = (n, middle, high, kernel)
    independent_tail = sum(w[3*m+1:4*m+1]) % p**3
    assert independent_tail % p**2 == 0
    assert independent_tail // p**2 == reciprocal_sum == tail_sum
    if p == 373:
        assert reciprocal_sum == 266
        assert sample == (125, 108, 203, 290)
        assert sum(w) % p**3 == 373
        bulk = sum(w[:3*m+1]) % p**3
        assert bulk == 14887176
        assert (bulk-373) % p**2 == 0
        assert ((bulk-373) % p**3)//p**2 == 107 == (-reciprocal_sum) % p
    return p, m, reciprocal_sum, sample


def main():
    results = [verify(p) for p in PRIMES]
    print('PASS_D25_ORIGINAL216_ALL_N_REFLECTION_AND_MIDDLE_HIGH_RECIPROCITY')
    print('primes_checked=', len(results), 'pairs_checked=', sum(p-1 for p in PRIMES))
    print('p13=', results[1], 'p19=', results[2], 'p373=', results[-1])


if __name__ == '__main__':
    main()
