"""Exact checks for the capacity sequence K(t) = Phi_12(2**t)."""

from math import gcd, isqrt


def capacity(t):
    return (1 << (4 * t)) - (1 << (2 * t)) + 1


def valuation(n, p):
    result = 0
    while n % p == 0:
        result += 1
        n //= p
    return result


def is_prime(n):
    return n > 1 and all(n % q for q in range(2, isqrt(n) + 1))


def prime_divisors(n):
    q = 2
    while q * q <= n:
        if n % q == 0:
            yield q
            while n % q == 0:
                n //= q
        q += 1
    if n > 1:
        yield n


def order_two(p):
    order = p - 1
    for q in prime_divisors(p - 1):
        while order % q == 0 and pow(2, order // q, p) == 1:
            order //= q
    return order


def main():
    bound = 160
    capacities = [0] + [capacity(t) for t in range(1, bound + 1)]
    pairs = 0
    for u in range(1, bound + 1):
        for v in range(u, bound + 1):
            g = gcd(u, v)
            predicted = capacities[g] if gcd((u // g) * (v // g), 6) == 1 else 1
            assert gcd(capacities[u], capacities[v]) == predicted
            pairs += 1

    tests = hits = lifted = 0
    for p in range(3, 5000, 2):
        if not is_prime(p):
            continue
        h = order_two(p)
        rank = h // 12 if h % 12 == 0 else None
        base_val = valuation(capacity(rank), p) if rank else 0
        for t, value in enumerate(capacities[1:], start=1):
            predicted = 0
            if rank and t % rank == 0 and gcd(t // rank, 6) == 1:
                predicted = base_val + valuation(t // rank, p)
            assert valuation(value, p) == predicted
            tests += 1
            hits += predicted > 0
            lifted += predicted > 1

    assert [valuation(capacities[t], 13) for t in (1, 2, 5, 13, 26)] == [1, 0, 1, 2, 0]
    print(f"{pairs} gcds, {tests} prime/layer valuations, {hits} positive, {lifted} with valuation >= 2")


if __name__ == "__main__":
    main()
