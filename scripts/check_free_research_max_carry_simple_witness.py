#!/usr/bin/env python3
"""Exact finite check of the simplified maximal Hamming-row carry witness.

For prime p and N>=1, set q=floor(log_p N) and k=p^q-1.  The claim is

  v_p(choose(N-1,k)) = q-v_p(N).

The script uses exact integers only and is evidence for the Lean route, not a
replacement for a proof.
"""

from math import comb


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def vp(n: int, p: int) -> int:
    assert n > 0 and is_prime(p)
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def floor_log_p(n: int, p: int) -> int:
    assert n >= 1 and p >= 2
    q = 0
    power = p
    while power * p <= n:
        power *= p
        q += 1
    return q


def check(limit: int = 1200) -> None:
    primes = [p for p in range(2, limit + 1) if is_prime(p)]
    for N in range(1, limit + 1):
        for p in primes:
            if p > N:
                break
            q = floor_log_p(N, p)
            a = vp(N, p)
            k = p**q - 1
            assert 0 <= k <= N - 1
            assert vp(comb(N - 1, k), p) == q - a, (N, p, q, a, k)

            # Kummer residue form: at level r<=q, a carry occurs iff p^r∤N.
            for r in range(1, q + 1):
                modulus = p**r
                residue_sum = k % modulus + (N - 1 - k) % modulus
                assert (residue_sum >= modulus) == (N % modulus != 0), (N, p, r)

    print("simplified maximal-carry witness checks: PASS")


if __name__ == "__main__":
    check()
