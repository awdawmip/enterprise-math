#!/usr/bin/env python3
"""Finite exact checks for the fixed-216 normalized observer (author-side only)."""
from math import isqrt


def primes(n):
    s = bytearray(b'\x01') * n
    s[:2] = b'\x00\x00'
    for d in range(2, isqrt(n - 1) + 1):
        if s[d]:
            s[d*d:n:d] = b'\x00' * ((n - 1 - d*d)//d + 1)
    return [p for p in range(5, n) if s[p]]


def gauss(p):
    ell = (p-1)//6
    coefficient, value, derivative = 1, 1, 0
    for k in range(1, ell+1):
        coefficient = (coefficient * (ell-k+1) * (2*ell-k+1)
                       * pow(2*k*k, -1, p)) % p
        value = (value + coefficient) % p
        derivative = (derivative + 2*k*coefficient) % p
    return value, derivative


def original_observers(p):
    modulus = p**4
    parameters = (0, 1, -1, 2, -2)
    xs = [pow((1+p*t) % modulus, -1, modulus) for t in parameters]
    powers, values = [1]*5, [1]*5
    a = 1
    moment1 = moment2 = moment3 = 0
    for n in range(1, p):
        a = (a * (2*n-1)*(3*n-1)*(3*n-2)
             * pow(36*n*n*n, -1, modulus)) % modulus
        weighted = (6*n+1)*a % modulus
        moment1 = (moment1+n*weighted) % modulus
        moment2 = (moment2+n*n*weighted) % modulus
        moment3 = (moment3+n*n*n*weighted) % modulus
        for j, x in enumerate(xs):
            powers[j] = powers[j]*x % modulus
            values[j] = (values[j]+weighted*powers[j]) % modulus
    return values, (moment1, moment2, moment3)


def main():
    selected = [p for p in primes(5001) if p % 24 in (13, 19)]
    anchors = []
    for p in selected:
        zero, slope = gauss(p)
        assert zero == 0 and slope != 0, (p, 'CM assumption/sample')
        v, (m1, m2, m3) = original_observers(p)
        assert m1 % p == 3*slope*slope % p
        assert m2 % p == 5*slope*slope % p
        assert m3 % p == (56*pow(3, -1, p)*slope*slope) % p
        mod3, mod4 = p**3, p**4
        for t, plus, minus in [(1,v[1],v[2]),(2,v[3],v[4])]:
            difference = (plus + minus - 2*v[0]) % mod3
            assert difference == 8*p*p*t*t*slope*slope % mod3
            assert difference % (p*p) == 0 and difference != 0
        cubic = (v[3]-2*v[1]+2*v[2]-v[4]) % mod4
        assert cubic == p**3*(-238*pow(3,-1,p)*slope*slope % p)
        assert cubic % p**3 == 0 and cubic != 0
        if p in (13, 19, 37, 157, 373):
            anchors.append((p, slope, m1%p, m2%p, m3%p,
                            (8*slope*slope)%p, cubic//p**3))
    print('PASS_D25_FIXED216_CURVATURE_AND_CUBIC_STENCIL_EXACT')
    print('target_primes',len(selected),'curvature_pairs',2*len(selected),
          'cubic_stencils',len(selected))
    print('anchors (p, Gprime, M1, M2, M3, quadratic_quotient, cubic_quotient)')
    for row in anchors:
        print(row)

if __name__ == '__main__':
    main()
