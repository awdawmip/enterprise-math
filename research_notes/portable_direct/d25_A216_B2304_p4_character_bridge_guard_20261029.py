#!/usr/bin/env python3
"""Independent author-side finite diagnostic for original 216/2304 sums.

All arithmetic is exact in Z/(p**order); denominators n**3 are units for 1<=n<p.
No native H0/B0 object or Source task run is evaluated.
"""
from math import comb


def primes_below(bound):
    marks = bytearray(b"\x01") * bound
    if bound > 0:
        marks[0] = 0
    if bound > 1:
        marks[1] = 0
    for q in range(2, int(bound ** 0.5) + 1):
        if marks[q]:
            for t in range(q * q, bound, q):
                marks[t] = 0
    return [p for p in range(5, bound) if marks[p]]


def original_sums_recurrence(p, precision=4):
    mod = p ** precision
    a = b = 1
    sum_a = sum_b = 0
    for n in range(p):
        sum_a = (sum_a + (6 * n + 1) * a) % mod
        sum_b = (sum_b + (8 * n + 1) * b) % mod
        k = n + 1
        if k < p:
            a = (a * (2*k-1) * (3*k-2) * (3*k-1) * pow(36 * k**3, -1, mod)) % mod
            b = (b * (2*k-1) * (4*k-3) * (4*k-1) * pow(288 * k**3, -1, mod)) % mod
    return sum_a, sum_b


def original_sums_binomial(p, precision=4):
    mod = p ** precision
    base_a = pow(216, -1, mod)
    base_b = pow(2304, -1, mod)
    a_power = b_power = 1
    sum_a = sum_b = 0
    for n in range(p):
        source_a = comb(2*n,n)**2 * comb(3*n,n)
        source_b = comb(2*n,n)**2 * comb(4*n,2*n)
        sum_a = (sum_a + (6*n+1)*source_a*a_power) % mod
        sum_b = (sum_b + (8*n+1)*source_b*b_power) % mod
        a_power = a_power * base_a % mod
        b_power = b_power * base_b % mod
    return sum_a, sum_b


def verify(bound=1500):
    primes = primes_below(bound)
    assert len(primes) == 237
    classes = {13: 0, 19: 0}
    exceptions_p4 = []
    exceptions_p3 = []
    for p in primes:
        sa, sb = original_sums_recurrence(p, 4)
        chi = 1 if p % 3 == 1 else -1
        if p % 24 in classes:
            classes[p % 24] += 1
        if (sa - sb) % p**3 or (sb - chi*p) % p**3:
            exceptions_p3.append(p)
        if (sa - 2*sb + chi*p) % p**4:
            exceptions_p4.append(p)
    assert not exceptions_p3, exceptions_p3
    assert not exceptions_p4, exceptions_p4
    print('PASS_AB_P3_THEOREM_CONSISTENCY_AND_P4_BRIDGE', len(primes), 'primes <', bound)
    print('target_classes', classes)
    for p in (5, 7, 11, 13, 19, 373):
        rec = original_sums_recurrence(p, 5)
        if p in (13, 19, 373):
            assert rec == original_sums_binomial(p, 5), ('independent mismatch',p)
        chi = 1 if p % 3 == 1 else -1
        qa = (rec[0]-chi*p) % p**4 // p**3
        qb = (rec[1]-chi*p) % p**4 // p**3
        defect5 = (rec[0] - 2*rec[1] + chi*p) % p**5 // p**4
        print(f'p={p} chi={chi} A_mod_p4={rec[0]%p**4} B_mod_p4={rec[1]%p**4} '
              f'A_cubic={qa} B_cubic={qb} p5_bridge_quotient={defect5}')
    assert (original_sums_recurrence(11,5)[0] - 2*original_sums_recurrence(11,5)[1] - 11) % 11**5 == 5*11**4
    print('PASS_INDEPENDENT_RAW_BINOMIAL_13_19_373_P5')
    print('SHARPNESS_P5_COUNTEREXAMPLE_p11=5*p^4')


if __name__ == '__main__':
    verify()
