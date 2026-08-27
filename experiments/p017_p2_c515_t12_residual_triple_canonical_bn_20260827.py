#!/usr/bin/env python3
"""Exact finite checker for the corrected residual triple B x N split."""

K = 116_009_280_740_973_308
W = K + 1
N0 = 18_455


def primes_upto(n: int) -> list[int]:
    ps: list[int] = []
    for x in range(2, n + 1):
        ok = True
        for p in ps:
            if p * p > x:
                break
            if x % p == 0:
                ok = False
                break
        if ok:
            ps.append(x)
    return ps


def main() -> None:
    # Exact short-scale location.
    assert N0**4 <= W < (N0 + 1) ** 4
    assert 29**3 > N0

    hard = [p for p in primes_upto(N0) if p >= 29]
    assert len(hard) == 2105
    assert hard[-1] == 18451

    pair_count = 0
    pair_products: set[int] = set()
    for i, p in enumerate(hard):
        for q in hard[i + 1 :]:
            value = p * q
            if value > N0:
                break
            pair_count += 1
            pair_products.add(value)

    assert pair_count == 895
    assert len(pair_products) == 895
    assert 1 + len(hard) + pair_count == 3001

    print("P017 corrected residual triple canonical BxN checker: PASS")
    print("floor N0 =", N0)
    print("single-prime short states =", len(hard))
    print("two-prime short states =", pair_count)
    print("total short hard states = 3001")
    print("29^3>N0: high-prefix shells have hard modulus 1")


if __name__ == "__main__":
    main()
