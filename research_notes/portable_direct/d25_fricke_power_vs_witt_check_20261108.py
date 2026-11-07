"""Author-side exact check: raw p-th power versus the unramified Frobenius.

This is NOT a native H0/B0 or 373 original-class benchmark. No third-party
mathematical engine, approximate arithmetic, or outcome claims are used.
"""
from math import isqrt


def primes_below(limit):
    for n in range(5, limit + 1):
        if all(n % d for d in range(2, isqrt(n) + 1)):
            yield n


def fermat_quotient(p, numerator, denominator=1):
    modulus = p * p
    r = numerator * pow(denominator, -1, modulus) % modulus
    return ((pow(r, p - 1, modulus) - 1) // p) % p


def direct_delta(p, numerator, denominator=1, epsilon=1):
    """Coefficient of s in (a**p + a) / p mod p, a=eps*r*s,s²=2."""
    modulus = p * p
    r = numerator * pow(denominator, -1, modulus) % modulus
    coeff = (epsilon * (pow(r, p, modulus) * pow(2, (p - 1) // 2, modulus) + r)) % modulus
    assert coeff % p == 0
    return coeff // p


def check_prime(p):
    assert p % 24 in (13, 19)
    inv2 = pow(2, -1, p)
    q2 = fermat_quotient(p, 2)
    q3 = fermat_quotient(p, 3)
    qt = (-(3 * inv2 * q2 + q3)) % p
    qa = (-(7 * inv2 * q2 - 3 * q3)) % p
    qrel = fermat_quotient(p, 4, 81)
    assert qrel == (2 * q2 - 4 * q3) % p
    assert (qa - qt + qrel) % p == 0
    for eps in (-1, 1):
        assert direct_delta(p, 6, 1, eps) == (eps * 6 * qt) % p
        assert direct_delta(p, 8, 27, eps) == (eps * 8 * pow(27, -1, p) * qa) % p
    return (p, q2, q3, qt, qa, (qa-qt)%p, qrel)


if __name__ == '__main__':
    tested = [check_prime(p) for p in primes_below(2000) if p % 24 in (13, 19)]
    assert len(tested) == 77
    print('p q2 q3 delta_t delta_tangent relative q(4/81)')
    for row in tested:
        if row[0] in (13, 19, 43, 67, 373):
            print(row)
    print('PASS:', len(tested), 'target primes, two conjugate fibers, direct p-th powers and Fermat quotients.')
