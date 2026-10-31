#!/usr/bin/env python3
"""Exact source-port check for D25 uniform-Gosper obstruction.

The rational no-go is proved in the companion note; this executable tests
original weighted 216 strip against the factorial port, not native H0/B0.
"""
from math import comb, factorial


def check_prime(p: int) -> tuple[int, int, int, int]:
    assert p > 3 and p % 6 == 1
    ell = (p - 1) // 6
    mod = p**3
    c = (factorial(3 * ell) * factorial(4 * ell) * factorial(2 * ell)) % p
    assert c % p
    total = 0
    old = None
    for j in range(1, ell + 1):
        numerator = (pow(2, 2 * ell + j, p)
                     * pow(factorial(2 * ell + j - 1), 3, p)
                     * factorial(ell - j) * factorial(2 * ell - j))
        term = numerator * pow(factorial(j - 1), -1, p) % p
        if old is not None:
            k = j - 1
            den = k * (ell - k) * (2 * ell - k)
            assert den % p
            ratio = 2 * (2 * ell + k) ** 3 * pow(den, -1, p) % p
            assert term == old * ratio % p
        old = term
        total = (total + (1 - 12 * ell - 6 * j) * term) % p
    finite_port = total * pow(12 * c, -1, p) % p
    original = sum((6 * n + 1) * comb(2 * n, n) ** 2 * comb(3 * n, n)
                   * pow(216, -n, mod)
                   for n in range(3 * ell + 1, 4 * ell + 1)) % mod
    assert original % (p * p) == 0
    direct = original // (p * p)
    assert direct == finite_port
    return p, ell, finite_port, total


def main() -> None:
    expected = {7: 5, 13: 10, 19: 9, 37: 20, 67: 58, 373: 266}
    for p, answer in expected.items():
        result = check_prime(p)
        assert result[2] == answer
        print(f"p={result[0]} ell={result[1]} I_p={result[2]} raw_moment={result[3]}")
    print("PASS_D25_UNIFORM_GOSPER_NO_GO_PORT_GUARD six_exact_primes")


if __name__ == "__main__":
    main()
