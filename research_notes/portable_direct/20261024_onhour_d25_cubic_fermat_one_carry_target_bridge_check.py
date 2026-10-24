#!/usr/bin/env python3
"""D25 one-carry/CM normalization: exact-Q and modular-p^2 independent checks.

Author-side finite regression, not a native benchmark or a proof of the open
D25 supercongruence. Standard-library only; no replacement source summands.
"""
from fractions import Fraction
from math import comb, factorial


def primes_through(limit):
    marks = bytearray(b'\x01') * (limit + 1)
    marks[:2] = b'\x00\x00'
    for d in range(2, int(limit**0.5) + 1):
        if marks[d]:
            marks[d*d::d] = b'\x00' * ((limit-d*d)//d + 1)
    return [i for i in range(7, limit + 1) if marks[i] and i % 6 == 1]


def exact_rational_product(m):
    p = 6*m+1
    U = Fraction(factorial(8*m), p * 216**(2*m) * factorial(4*m)**2)
    G = Fraction(4**(p-1) * factorial(2*m)**3, factorial(p-1))
    product = Fraction(1, 2*m * 24**(p-1))
    for a in range(1, 2*m):
        product *= 1 + Fraction(p, a)
    for a in range(1, 2*m+1):
        product *= (1 - Fraction(p, a))**2
    assert U/G == product, (m, 'exact rational product mismatch')


def modular_prime_test(p):
    m = (p-1)//6
    M = p*p
    # An independent original factorial path: multiply all integers to
    # p+2m-1, stripping the *single* p-factor at its true index j=p.
    # All other factors, including the original positive factors, are retained.
    unit_top = 1
    F = F4 = W = None
    for j in range(1, p+2*m):
        if j != p:
            unit_top = unit_top * j % M
        if j == 2*m:
            F = unit_top
        if j == 4*m:
            F4 = unit_top
        if j == p-1:
            W = unit_top
    assert F is not None and F4 is not None and W is not None
    U = unit_top * pow(216, -2*m, M) * pow(F4, -2, M) % M
    G = pow(4, p-1, M) * pow(F, 3, M) * pow(W, -1, M) % M
    assert G % p and U % p

    product = pow(2*m, -1, M) * pow(24, -(p-1), M) % M
    for a in range(1, 2*m):
        product = product * (1 + p*pow(a, -1, M)) % M
    for a in range(1, 2*m+1):
        product = product * pow(1 - p*pow(a, -1, M), 2, M) % M
    assert U * pow(G, -1, M) % M == product, (p, 'ratio')

    def fq(a):
        return (pow(a, p-1, M) - 1)//p

    h_prev = sum(pow(j, -1, p) for j in range(1, 2*m)) % p
    h_full = (h_prev + pow(2*m, -1, p)) % p
    # Independently check the harmonic identity also proved algebraically
    # by the cubic-root-of-unity argument in the companion note.
    assert (h_full + 3*pow(2, -1, p)*fq(3)) % p == 0, (p, 'cubic harmonic')
    eta = (19*pow(9, -1, p) - 2*pow(3, -1, p)*h_prev
           - pow(3, -1, p)*fq(6)) % p
    xi = (37*pow(3, -1, p) - 10*fq(2)
          + 7*pow(2, -1, p)*fq(3)) % p
    left = (G - U * (1+p*eta)) % M
    right = G * (4+p*xi) % M
    assert left == right, (p, 'regular bridge coefficient')

    # This last observation is NOT used to prove the universal statement.
    # It documents exactly the unfinished first-digit prime-only target.
    low = 0
    for n in range(m+1):
        bn = (-1 if n & 1 else 1) * comb(m,n) * pow(2, -n, p) % p
        kn = ((1-3*n)*(6*n+3) * pow((3*n+1)*(3*n+2), -1, p)) % p
        low = (low+bn*kn)%p
    assert low == 4*G % p, (p, 'observed first-digit only')
    return p, m, G, U, xi, left


def main():
    for m in range(1, 10):
        exact_rational_product(m)
    results = [modular_prime_test(p) for p in primes_through(3000)]
    print(f'PASS: 9 exact-Q product identities; {len(results)} primes p<=3000, p=1 mod6; '
          'independent factorial/product paths, cubic harmonic, p^2 seam normalization.')
    print('FINITE OBSERVATION ONLY (UNPROVED): regular LOW first-digit congruence '
          f'also matches in {len(results)}/{len(results)} tested primes.')
    for p in (7,13,19,37,211):
        print('witness', modular_prime_test(p))


if __name__ == '__main__':
    main()
