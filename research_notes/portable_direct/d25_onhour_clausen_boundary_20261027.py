#!/usr/bin/env python3
"""Exact modular checks for D25 original weighted-216 p^3 Clausen boundary.
No external packages, floating point, remote systems or native experiment.
"""
from math import comb

TARGET_PRIMES = (13, 19, 37, 43, 61, 67, 211, 373)
CONTROL_PRIMES = (7, 31, 73)


def run_prime(p: int, target: bool) -> dict:
    assert p > 3 and p % 6 == 1
    m = (p - 1) // 6
    modulus = p**3
    # t_k = (1/6)_k(1/3)_k / (k!)^2 * (1/2)^k.
    gauss = [1]
    for k in range(p - 1):
        gauss.append(
            gauss[-1] * (6 * k + 1) * (3 * k + 1)
            * pow(36 * (k + 1)**2, -1, modulus) % modulus
        )
    # Independent ORIGINAL weighted-216 evaluation using exact integer binomials.
    original = sum(
        (6*n + 1) * comb(2*n, n)**2 * comb(3*n, n)
        * pow(216, -n, modulus)
        for n in range(p)
    ) % modulus
    d0 = sum(gauss[:2*m + 1]) % modulus
    d1 = sum(k * gauss[k] for k in range(2*m + 1)) % modulus
    a0 = sum(gauss[:m + 1]) % modulus
    a1 = sum(k * gauss[k] for k in range(m + 1)) % modulus
    c = sum(gauss[2*m + 1:]) % modulus
    prefix0, prefix1 = [0], [0]
    for j in range(m + 1):
        prefix0.append((prefix0[-1] + gauss[j]) % modulus)
        prefix1.append((prefix1[-1] + j*gauss[j]) % modulus)
    raw_cross = sum(
        2 * gauss[k] * (
            (6*k+1) * prefix0[min(m, p-1-k)+1]
            + 6 * prefix1[min(m, p-1-k)+1]
        )
        for k in range(2*m+1, p)
    ) % modulus
    raw = (d0*d0 + 12*d0*d1 + raw_cross) % modulus
    assert raw == original, (p, 'raw Clausen finite-truncation mismatch')
    # All lost degree >=p terms from A(z) C(z).
    boundary = sum(
        gauss[k] * (
            (6*k+1) * (a0 - prefix0[p-k])
            + 6 * (a1 - prefix1[p-k])
        )
        for k in range(5*m+1, p)
    ) % modulus
    full_cross = 2 * (
        a0*c + 6*(a1*c + a0*sum(k*gauss[k] for k in range(2*m+1,p)))
    )
    assert (full_cross - 2*boundary) % modulus == raw_cross
    assert c % (p*p) == 0 and boundary % (p*p) == 0
    if target:
        assert p % 24 in (13, 19)
        assert a0 % p == 0 and d0 % p == 0
        reduced = (d0*d0 + 12*d0*d1 + 12*a1*c - 2*boundary) % modulus
        assert reduced == original
        r = d0 // p
        e = d1 % (p*p)
        j = a1 % p
        c2 = c // (p*p)
        h2 = boundary // (p*p)
        assert (12*r*e) % p == 1
        d2 = ((12*r*e-1)//p + r*r + 12*j*c2 - 2*h2) % p
        assert (original-p) % (p*p) == 0
        assert d2 == ((original-p)//(p*p)) % p
        row = dict(p=p, r=r % (p*p), e=e, j=j, c2=c2, h2=h2,
                   first_digit=(12*r*e) % p, residue=d2,
                   parts=[((12*r*e-1)//p)%p, (r*r)%p,
                          (12*j*c2)%p, (-2*h2)%p])
        if p == 373:
            assert (row['r'], row['e'], row['j'], row['c2'], row['h2']) == (
                110805, 108837, 294, 252, 98
            )
            assert row['parts'] == [169, 203, 197, 177]
            assert original == 373
        return row
    assert p % 24 in (1, 7)
    assert a0 % p != 0
    return {'p': p, 'raw_verified': True, 'a0_mod_p': a0 % p,
            'original_mod_p3': original}


def main() -> None:
    for p in TARGET_PRIMES:
        print('TARGET', run_prime(p, True))
    for p in CONTROL_PRIMES:
        print('CONTROL', run_prime(p, False))
    print('PASS_D25_CLAUSEN_TRUNCATION_AND_CM0_BOUNDARY_P3')


if __name__ == '__main__':
    main()
