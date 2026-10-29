#!/usr/bin/env python3
"""Author-side exact fifth-digit audit of the ORIGINAL A216/B2304 finite sums.

Research evidence only; not an H0/B0 native computation or a formal Source Result.
No external dependencies.  Python >=3.8.
"""
from math import comb, isqrt


def eligible_primes(bound):
    sieve = bytearray(b'\x01') * bound
    sieve[0:2] = b'\x00\x00'
    for d in range(2, isqrt(bound - 1) + 1):
        if sieve[d]:
            sieve[d*d:bound:d] = b'\x00' * len(range(d*d, bound, d))
    return [p for p in range(5, bound) if sieve[p]]


def exact_sums(p):
    """Original binomial definitions, evaluated at modulus p^5."""
    M = p**5
    inv216 = pow(216, -1, M)
    inv2304 = pow(2304, -1, M)
    xa = xb = 1
    A = B = 0
    zones_a, zones_b = [0]*4, [0]*4
    for n in range(p):
        a = comb(2*n, n)**2 * comb(3*n, n)
        b = comb(2*n, n)**2 * comb(4*n, 2*n)
        wa = (6*n+1)*a*xa % M
        wb = (8*n+1)*b*xb % M
        A, B = (A+wa) % M, (B+wb) % M
        # For n<p and p>=5, these factorial-valuation formulas are exact.
        va = (2*n)//p + (3*n)//p
        vb = (4*n)//p
        assert 0 <= va <= 3 and 0 <= vb <= 3
        zones_a[va] = (zones_a[va]+wa) % M
        zones_b[vb] = (zones_b[vb]+wb) % M
        xa = xa*inv216 % M
        xb = xb*inv2304 % M
    return A, B, zones_a, zones_b


def recurrence_sums(p):
    """Independent exact hypergeometric recurrences in (Z/p^5 Z)."""
    M = p**5
    facts = [1]*p
    for n in range(1, p):
        facts[n] = facts[n-1]*n % M
    inv_factorial = pow(facts[p-1], -1, M)
    inv = [0]*p
    for n in range(p-1, 0, -1):
        inv[n] = inv_factorial*facts[n-1] % M
        inv_factorial = inv_factorial*n % M
    ia, ib = pow(36, -1, M), pow(576, -1, M)
    a = b = 1
    A = B = 0
    for n in range(p):
        A = (A+(6*n+1)*a) % M
        B = (B+(8*n+1)*b) % M
        if n < p-1:
            unit = pow(inv[n+1], 3, M)
            a = a*(2*n+1)*(3*n+1)*(3*n+2)*unit*ia % M
            b = b*(4*n+1)*(4*n+2)*(4*n+3)*unit*ib % M
    return A, B


def carry_ledger(p, zones_a, zones_b):
    M, chi = p**5, 1 if p % 3 == 1 else -1
    signed = [(zones_a[j]-2*zones_b[j]+(p*chi if j == 0 else 0)) % M
              for j in range(4)]
    partials, acc = [], 0
    for value in signed:
        acc = (acc+value) % M
        partials.append(acc)
    return signed, partials


def run():
    primes = eligible_primes(5000)
    assert len(primes) == 667
    target = [p for p in primes if p % 24 in (13, 19)]
    assert len(target) == 166
    failures_p4, zero_p5 = [], []
    audit = {}
    for p in primes:
        A, B = recurrence_sums(p)
        chi = 1 if p % 3 == 1 else -1
        difference = (A-2*B+p*chi) % (p**5)
        if difference % (p**4):
            failures_p4.append((p, difference))
        if difference == 0:
            zero_p5.append(p)
        if p in (13, 19, 373):
            rawA, rawB, az, bz = exact_sums(p)
            assert (rawA, rawB) == (A, B), (p, rawA, rawB, A, B)
            e, part = carry_ledger(p, az, bz)
            assert part[-1] == difference
            assert all(part[j] % p**(j+1) == 0 for j in range(4))
            assert all(part[j] % p**(j+2) != 0 for j in range(4))
            audit[p] = (A, B, difference, e, part,
                        [part[j]//p**(j+1) % p for j in range(4)])
    print('PRIMES_BELOW_5000', len(primes), 'TARGET_RESIDUE_CLASSES', len(target))
    print('P4_BRIDGE_FAILURES', failures_p4)
    print('P5_EXACT_ZERO_PRIMES', zero_p5)
    assert not failures_p4 and zero_p5 == [5, 7]
    for p, (A, B, d, e, partials, digits) in audit.items():
        print('P', p, 'A', A, 'B', B, 'D', d, 'D_OVER_P4', d//p**4)
        print('SOURCES', e, 'CUMULATIVE', partials, 'CARRY_DIGITS', digits)
    assert audit[13][2] == 9*13**4
    assert audit[19][2] == 14*19**4
    assert audit[373][2] == 174*373**4
    print('PASS_EXACT_A216_B2304_P5_SOURCE_CARRY')


if __name__ == '__main__':
    run()
