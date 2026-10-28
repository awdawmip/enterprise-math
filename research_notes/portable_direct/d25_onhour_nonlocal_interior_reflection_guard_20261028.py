#!/usr/bin/env python3
"""AUTHOR-SIDE exact modular certificate; not a native H0/B0 execution."""
from math import comb


def isprime(p):
    return p > 1 and all(p % d for d in range(2, int(p ** .5) + 1))


def run(p):
    assert p > 3 and p % 6 == 1 and isprime(p)
    m = (p - 1) // 6
    q = p ** 3
    # Original factorial definition; independently cross-checked by recurrence.
    t = [
        (comb(2 * n, n) ** 2 * comb(3 * n, n) * pow(216, -n, q)) % q
        for n in range(p)
    ]
    b = 1
    for n in range(p):
        assert b == t[n], (p, n, b, t[n])
        if n < p - 1:
            b = (
                b * (2 * n + 1) * (3 * n + 1) * (3 * n + 2)
                * pow(36 * (n + 1) ** 3, -1, q)
            ) % q

    a = [
        (66 * n * n + 113 * n + 49)
        * t[n] * pow(9 * (n + 1) ** 3, -1, q) % q
        for n in range(p - 1)
    ]
    W = sum((6 * n + 1) * t[n] for n in range(p)) % q
    J = sum(a) % q
    assert (W - J + 4) % q == 0

    high = 0
    dual = 0
    for r in range(m):
        j = 2 * m + 1 + r
        k = 4 * m - r
        assert t[j] % p == 0 and t[j] % (p * p) != 0
        assert t[k] % (p * p) == 0 and t[k] % q != 0
        u = (t[j] % (p * p)) // p
        R = (
            9 * (66 * r * r - 25 * r + 3)
            * pow(4 * (1 - 3 * r) ** 3 * (3 * r + 2) ** 3, -1, p)
        ) % p
        observed = (a[k] // (p * p)) % p
        predicted = (R * pow(u, -1, p)) % p
        assert observed == predicted, (p, r, observed, predicted)
        # Independently check the underlying unweighted factorial reflection.
        assert (
            ((t[j] % (p * p)) // p)
            * ((t[k] % q) // (p * p))
            * 36 * j ** 3 - 1
        ) % p == 0
        high = (high + a[k]) % q
        dual = (dual + p * p * predicted) % q

    assert high == dual, (p, high, dual)
    for n in range(4 * m + 1, p - 1):
        assert a[n] == 0, (p, n, a[n])
    assert J == (sum(a[:3 * m + 1]) + dual) % q
    if p % 24 in (13, 19):
        assert W == p  # Only an instance-level regression, not a proof.
    return dict(
        p=p, m=m, W=W, J=J,
        reflected_tail=high // (p * p), pair_count=m,
        low=sum(a[:2 * m + 1]) % q,
        middle=sum(a[2 * m + 1:3 * m + 1]) % q,
    )


if __name__ == "__main__":
    ps = [p for p in range(7, 800) if p % 6 == 1 and isprime(p)]
    results = [run(p) for p in ps]
    print(
        "PASS_D25_J_INTERIOR_NONLOCAL_REFLECTION",
        len(results), "primes;",
        sum(item["pair_count"] for item in results), "paired terms",
    )
    for item in results:
        if item["p"] in (13, 19, 37, 43, 61, 67, 211, 373):
            print(item)
