#!/usr/bin/env python3
"""Exact p^5 sharpness/exceptional-prime test of original full W216/V2304.

No floating point and no H0/B0 native experiment. Author-side evidence,
UNREVIEWED / NOT_ADMITTED. Frozen scientific pin unchanged.
"""
from math import comb, isqrt


def is_prime(n):
    if n < 2:
        return False
    for j in range(2, isqrt(n) + 1):
        if n % j == 0:
            return False
    return True


def original_sums_recurrence(p, power=5):
    """Compute weighted W,V from the original factorial-ratio recurrence."""
    assert p > 3 and is_prime(p)
    M = p ** power
    a, c, w, v = 1, 1, 0, 0
    i36, i288 = pow(36, -1, M), pow(288, -1, M)
    for n in range(p):
        w = (w + (6*n + 1)*a) % M
        v = (v + (8*n + 1)*c) % M
        if n+1 < p:
            u3 = pow(n + 1, -3, M)
            a = a*(2*n+1)*(3*n+1)*(3*n+2)*i36*u3 % M
            c = c*(4*n+1)*(4*n+3)*(2*n+1)*i288*u3 % M
    chi = 1 if pow(-3 % p, (p - 1)//2, p) == 1 else -1
    E = (w - 2*v + p*chi) % M
    assert E % p**4 == 0, (p, 'AF4 calculation fails', E)
    return w, v, chi, E, (E//p**4) % p


def original_sums_binomial(p, power=5):
    """Independent unbounded binomial integer sum with original denominators."""
    M = p**power
    i216, i2304 = pow(216, -1, M), pow(2304, -1, M)
    w, v = 0, 0
    for n in range(p):
        a = comb(2*n, n)**2 * comb(3*n, n)
        c = comb(4*n, 2*n) * comb(2*n, n)**2
        w = (w + (6*n+1)*a*pow(i216,n,M)) % M
        v = (v + (8*n+1)*c*pow(i2304,n,M)) % M
    chi = 1 if pow(-3 % p, (p-1)//2, p) == 1 else -1
    E = (w-2*v+p*chi) % M
    return w, v, chi, E, (E//p**4) % p if E%p**4 == 0 else None


def main():
    full = []
    for p in range(5,4001):
        if is_prime(p):
            _,_,chi,E,q = original_sums_recurrence(p)
            full.append((p,chi,q))
    exceptional = [(p,chi) for p,chi,q in full if q == 0]
    frozen = [p for p,chi,q in full if p % 24 in (13,19)]
    frozen_exceptional = [p for p,chi,q in full if p % 24 in (13,19) and q == 0]
    assert len(full) == 548, len(full)
    assert len(frozen) == 139, len(frozen)
    assert exceptional == [(5,-1),(7,1)], exceptional
    assert not frozen_exceptional
    checks = (5,7,13,19,37,43,73,373)
    for p in checks:
        r = original_sums_recurrence(p)
        b = original_sums_binomial(p)
        assert r == b, (p, r, b)
        print('P',p, 'p4',p**4,'p5',p**5,'W',r[0],'V',r[1],'chi',r[2],
              'E_mod_p5',r[3],'E/p4_modp',r[4])
    print('PASS:',len(full),'primes 5<=p<=4000;',len(frozen),
          'frozen-class primes; zero p5 obstruction:',exceptional)


if __name__ == '__main__':
    main()
