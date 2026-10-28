#!/usr/bin/env python3
"""Author-side finite-ring exploration, not a native H0/B0 benchmark.

Original beta_n = (1/8)_n (3/8)_n/(n!)^2.
K_b(z) = sum_{n=0}^b beta_n*z^n, with z=1/9.
B_p = sum_{n=0}^{p-1} (8n+1)*C(2n,n)^2*C(4n,2n)/2304^n.
All denominators are units for 0<=n<p, p>3.
"""

from math import comb, gcd, isqrt

LIMIT = 5000


def primes_under(limit):
    sieve = bytearray(b'\x01') * limit
    sieve[:2] = b'\x00\x00'
    for j in range(2, isqrt(limit - 1) + 1):
        if sieve[j]:
            sieve[j * j:limit:j] = b'\x00' * len(sieve[j * j:limit:j])
    return [j for j in range(limit) if sieve[j]]


def bands(p):
    if p % 8 == 5:
        return (5 * p - 1) // 8, (7 * p - 3) // 8
    if p % 8 == 3:
        return (p - 3) // 8, (3 * p - 1) // 8
    raise ValueError('Only p congruent to 3 or 5 modulo 8')


def beta_jet(p, precision):
    """K_b(1/9), theta K_b(1/9) mod p**precision via rational ratios."""
    _, b = bands(p)
    mod = p ** precision
    z = pow(9, -1, mod)
    t, k, d = 1, 0, 0
    for n in range(b + 1):
        k = (k + t) % mod
        d = (d + n * t) % mod
        if n < b:
            t = (t * (8 * n + 1) * (8 * n + 3) * z *
                 pow(64 * (n + 1) ** 2, -1, mod)) % mod
    return k, d


def beta_jet_product(p, precision):
    """Independent factorial-product evaluation, not using recurrence transport."""
    _, b = bands(p)
    mod = p ** precision
    numer = fact = 1
    k = d = 0
    inv_576 = pow(576, -1, mod)
    for n in range(b + 1):
        # Original product: prod_{j<n} (8j+1)(8j+3) / (576^n (n!)^2).
        c = numer * pow(fact * fact, -1, mod) * pow(inv_576, n, mod) % mod
        k = (k + c) % mod
        d = (d + n * c) % mod
        numer *= (8*n + 1) * (8*n + 3)
        fact *= n + 1
    return k, d


def original_b(p, precision):
    q = p ** precision
    w = pow(2304, -1, q)
    result = 0
    power = 1
    for n in range(p):
        result = (result + (8*n+1) * comb(2*n,n)**2 *
                  comb(4*n,2*n) * power) % q
        power = power * w % q
    return result


def source_carry_certificate(p):
    """Independently reconstruct B's original tagged high-degree pairs and R_B."""
    a, b = bands(p)
    q, z3, z1 = p**3, pow(9, -1, p**3), pow(9, -1, p)
    coeff = []
    t = 1
    for n in range(p):
        coeff.append(t)
        if n + 1 < p:
            t = t * (8*n + 1) * (8*n + 3) * z3 * pow(64*(n+1)**2, -1, q) % q
    k, d = sum(coeff[:b+1]) % q, sum(n*c for n, c in enumerate(coeff[:b+1])) % q
    U = (k*k + 16*k*d) % q
    H = sum((1 + 8*(i+j)) * coeff[i] * coeff[j]
            for i in range(b+1) for j in range(b+1) if i+j >= p) % q
    # A signed derivative is applied AFTER retaining original source pairs and degree.
    zpow = [pow(z1, n, p) for n in range(p)]
    qi = [comb(a, i)*comb(b, i) % p * zpow[i] % p for i in range(a+1)]
    QJ = []
    for j in range(b+1, p):
        assert coeff[j] % (p*p) == 0
        # coeff[j] includes evaluation at 1/9 already.
        QJ.append((j, coeff[j]//(p*p)))
    R = sum((1+8*(i+j)) * qi[i] * cj for i in range(a+1)
            for j, cj in QJ if i+j < p) % p
    B = original_b(p, 3)
    assert (U - H + 2*(p*p)*R - B) % q == 0, ('Clausen source full', p)
    if p % 24 == 13:
        assert k % (p*p) == 0
        k2 = k // (p*p)
        assert H == (-p + (p*p)*(16*k2*(d%p)+2*R)) % q, ('branch 13', p)
    else:
        assert H == 0
    return k, d, U, H, R, B


def main():
    cases = [p for p in primes_under(LIMIT) if p % 24 in (13, 19)]
    classes = {13: [], 19: []}
    exceptions13, exceptions19 = [], []
    for p in cases:
        k, d = beta_jet(p, 2)
        assert k % p == 0, ('root mod p fails', p, k)
        classes[p % 24].append(p)
        if p % 24 == 13:
            if k % (p*p):
                exceptions13.append((p, k))
            assert (k*k + 16*k*d) % (p*p) == 0, ('U_B valuation', p)
        if p % 24 == 19 and (16 * (k // p) * d - 1) % p:
            exceptions19.append((p, k, d))
    print('TARGET p<%d: p=13 mod24 %d, p=19 mod24 %d' % (
          LIMIT, len(classes[13]), len(classes[19])))
    print('BRANCH_13_K_MOD_P2_NONZERO:', exceptions13)
    print('BRANCH_19_16_K_OVER_P_D_MOD_P_NOT_ONE:', exceptions19)
    assert not exceptions13
    assert not exceptions19

    # Smaller set: cross-check by independent factorial products and original B.
    examples = (13, 19, 37, 43, 109, 139, 373, 379)
    for p in examples:
        k, d = beta_jet(p, 3)
        assert (k,d) == beta_jet_product(p, 3), ('independent product', p)
        # Clausen source operator (without high carry); p19 branch has no carry.
        square = (k*k + 16*k*d) % p**3
        if p % 24 == 19:
            assert square % (p*p) == p
        orig = original_b(p, 3)
        assert orig == p % (p**3), ('independent original B', p, orig)
        print('PIN p=%d residueK_p3=%d residueD_p=%d U_B_p3=%d B_original=%d' %
              (p, k, d % p, square, orig))
    for p in (13, 37, 109, 373, 19, 43):
        k,d,U,H,R,B = source_carry_certificate(p)
        print('SOURCES p=%d U=%d H=%d R=%d B=%d K/p2=%s' %
              (p,U,H,R,B,str(k//(p*p)) if p%24==13 else 'not_applicable'))
    print('PASS_D25_B2304_BRANCH_JET_OBSERVER p<%d exact modular samples=%d source_checks=6' %
          (LIMIT, len(examples)))


if __name__ == '__main__':
    main()
