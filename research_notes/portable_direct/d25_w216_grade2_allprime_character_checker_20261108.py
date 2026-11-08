"""Direct original-binomial vs finite 3F2 original 216 grade-two digit (all p>3).
Usage: python d25_w216_grade2_allprime_character_checker_20261108.py [max_p]
Author-side exact integer experiment; NOT native H0/B0.
"""
from math import comb, isqrt
import sys


def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def check(p):
    assert p > 3 and prime(p)
    N = (p + 1) // 2
    L = (2 * p - 1) // 3
    M = L - N + 1
    assert M == (p + 4) // 6
    k, S = 1, 0
    for r in range(M):
        S = (S + (6 * r + 4) * k) % p
        if r + 1 < M:
            k = (k * (r + 1) * (6 * r + 5) * (6 * r + 7)
                 * pow(9 * (2 * r + 3)**3, -1, p)) % p
    chi = pow(6, (p - 1) // 2, p)
    assert chi in (1, p - 1)
    expected = chi * pow(9, -1, p) * S % p
    mod = p**3
    inv216 = pow(216, -1, mod)
    power = pow(inv216, N, mod)
    direct = 0
    for n in range(N, L + 1):
        term = (6*n + 1) * comb(2*n, n)**2 * comb(3*n, n) * power % mod
        assert term % p**2 == 0
        direct = (direct + term // p**2) % p
        power = power * inv216 % mod
    assert direct == expected, (p, direct, expected)
    return p, M, direct, S, (1 if chi == 1 else -1)


if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    tested = [check(p) for p in range(5, limit + 1) if prime(p)]
    print("allprime_exact_agreement", len(tested))
    for p in (5, 7, 11, 13, 17, 19, 23, 31, 37, 211, 373):
        if p <= limit:
            print(check(p))
