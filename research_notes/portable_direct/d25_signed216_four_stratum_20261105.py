#!/usr/bin/env python3
"""Signed original-216 four source strata; exact modular checks, not native H0/B0."""
from math import isqrt


def primes_up_to(limit):
    mask = bytearray(b'\x01') * (limit + 1)
    mask[:2] = b'\x00\x00'
    for d in range(2, isqrt(limit) + 1):
        if mask[d]:
            mask[d*d::d] = b'\x00' * (((limit - d*d) // d) + 1)
    return [i for i in range(7, limit + 1) if mask[i] and i % 6 == 1]


def certificate(p):
    assert p >= 7 and p % 6 == 1
    n, modulus = (p - 1) // 6, p ** 4
    beta = (pow(2, -1, modulus), pow(3, -1, modulus),
            2 * pow(3, -1, modulus) % modulus)
    m = (3*n, 2*n, 4*n)
    unit, valuation = 1, 0
    harmonic1 = harmonic2 = harmonic3 = 0
    ports = [0, 0, 0, 0]
    for k in range(p):
        L, J, K = harmonic1, harmonic2, harmonic3
        e2 = (L*L - J) * pow(2, -1, modulus) % modulus
        e3 = (L**3 - 3*L*J + 2*K) * pow(6, -1, modulus) % modulus
        expansion = (1+p*L+p*p*e2+p**3*e3,
                     1+p*L+p*p*e2,
                     1+p*L,
                     1)[valuation]
        term = ((6*k+1) * p**valuation * unit * expansion) % modulus
        ports[valuation] = (ports[valuation] + term) % modulus
        if k == p-1:
            break
        ratio = pow(2*(k+1)**3, -1, modulus)
        for j in range(3):
            r = k-m[j]
            if r == 0:
                valuation += 1
                ratio = ratio * beta[j] % modulus
            else:
                ratio = ratio * r % modulus
                x = beta[j] * pow(r, -1, modulus) % modulus
                harmonic1 = (harmonic1 + x) % modulus
                harmonic2 = (harmonic2 + x*x) % modulus
                harmonic3 = (harmonic3 + x*x*x) % modulus
        unit = unit * ratio % modulus
    # Independent recurrence: no valuation splitting.
    a = total = 1
    for k in range(1, p):
        j = k-1
        a = a * (2*j+1)*(3*j+1)*(3*j+2)*pow(36*k**3, -1, modulus) % modulus
        total = (total + (6*k+1)*a) % modulus
    assert sum(ports) % modulus == total, (p, ports, total)
    return ports, total, (total-p) % modulus


def main():
    ps = primes_up_to(1200)
    for p in ps:
        _, _, defect = certificate(p)
        assert defect % p**3 == 0, (p, defect)
    print('PASS', len(ps), 'primes p=1 mod6, 7<=p<=1200; mod p^4 four-port identities')
    for p in (7, 13, 19, 31, 37, 373):
        ports, total, defect = certificate(p)
        print('p', p, 'ports', ports, 'W', total,
              '(W-p)/p^3 mod p', defect // p**3)


if __name__ == '__main__':
    main()
