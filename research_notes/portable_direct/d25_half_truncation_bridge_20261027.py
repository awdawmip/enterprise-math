"""D25 original 216-model vs published Guo--Zudilin 2304-model half-truncation.
Exact finite diagnostics only; NOT original native H0/B0 divided-power execution.
"""
from math import comb


def certificate(p):
    assert p >= 13 and p % 24 in (13, 19)
    # All chosen inputs are prime. This routine is not a primality oracle.
    h, m = (p - 1) // 2, (p - 1) // 6
    z, q, mod = 4 * m, (3 * p - 1) // 4, p ** 3
    fact = [1] * p
    for j in range(1, p):
        fact[j] = fact[j - 1] * j % p

    def w(n):
        return ((6 * n + 1) * comb(2 * n, n) ** 2 * comb(3 * n, n)
                * pow(216, -n, mod)) % mod

    def s(n):
        return ((8 * n + 1) * comb(4 * n, 2 * n) * comb(2 * n, n) ** 2
                * pow(2304, -n, mod)) % mod

    # Two independent computations of the p^2-digit of the original W tail.
    d_wilson = 0
    for n in range(h + 1, z + 1):
        digit = ((6 * n + 1) * fact[2 * n - p] * fact[3 * n - p]
                 * pow(fact[n], -5, p) * pow(216, -n, p)) % p
        d_wilson = (d_wilson + digit) % p
    w_half = sum(w(n) for n in range(h + 1)) % mod
    w_tail = sum(w(n) for n in range(h + 1, z + 1)) % mod
    w_outer = sum(w(n) for n in range(z + 1, p)) % mod
    assert w_outer == 0
    assert w_tail == p ** 2 * d_wilson

    # Guo--Zudilin proves both S(p-1) and S(h) are the same mod p^3.
    # Here we check the local finite instances without claiming to reprove it.
    s_half = sum(s(n) for n in range(h + 1)) % mod
    s_early = sum(s(n) for n in range(h + 1, z + 1)) % mod
    s_gap = sum(s(n) for n in range(z + 1, q + 1)) % mod
    s_outer = sum(s(n) for n in range(q + 1, p)) % mod
    assert s_outer == 0
    assert (s_early + s_gap) % mod == 0
    assert w_half % p ** 2 == p
    assert s_half == p

    # Keep the original second p-adic digit as a separate signed BRC port.
    assert (w_half - p) % p ** 2 == 0
    half_defect = ((w_half - s_half) % mod) // (p ** 2)
    assert (half_defect + d_wilson) % p == 0
    assert (w_half + w_tail - s_half) % mod == 0  # tested examples, not theorem
    return (p, h, z, q, d_wilson, half_defect,
            s_early // p ** 2, s_gap // p ** 2,
            w_half, s_half, w_tail)


if __name__ == '__main__':
    primes = (13, 19, 37, 43, 61, 67, 211, 373)
    rows = [certificate(p) for p in primes]
    assert rows[0] == (13, 6, 8, 9, 10, 3, 7, 6, 520, 13, 1690)
    assert rows[1] == (19, 9, 12, 14, 9, 10, 3, 16, 3629, 19, 3249)
    assert rows[-1] == (373, 186, 248, 279, 266, 107,
                        92, 281, 14887176, 373, 37008314)
    for row in rows:
        print(row)
