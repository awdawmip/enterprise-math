"""Exact finite seven-support certificate for the T6 large-prime cancellation theorem."""
from itertools import combinations

MAX_D = 2332
SIDE_BUDGET = 2331
EXCEPTIONAL_PRIMES = (131, 137, 139, 149, 151, 157, 163)


def kernel_profile(support, prime):
    """A generator of the kernel of the 6-by-7 inverse-power matrix over F_p."""
    x = [pow(j, -1, prime) for j in support]
    out = []
    for i, xi in enumerate(x):
        denom = xi
        for j, xj in enumerate(x):
            if i != j:
                denom = (denom * (xi - xj)) % prime
        out.append(pow(denom % prime, -1, prime))
    return out


def verify_prime(prime):
    q = MAX_D // prime
    support_count = candidate_count = 0
    for support in combinations(range(1, q + 1), 7):
        costs = [prime*j - 1 for j in support]
        if sum(costs) > 2 * SIDE_BUDGET:
            continue
        support_count += 1
        generator = kernel_profile(support, prime)
        individual_caps = [SIDE_BUDGET // cost for cost in costs]
        for scalar in range(1, prime):
            coeffs = [(scalar * v) % prime for v in generator]
            coeffs = [r - prime if r > prime // 2 else r for r in coeffs]
            if any(abs(c) > cap for c, cap in zip(coeffs, individual_caps)):
                continue
            if sum(abs(c) * cost for c, cost in zip(coeffs, costs)) > 2 * SIDE_BUDGET:
                continue
            candidate_count += 1
    assert candidate_count == 0, (prime, candidate_count)
    return (prime, q, support_count, (prime - 1) * support_count, candidate_count)


if __name__ == '__main__':
    rows = [verify_prime(p) for p in EXCEPTIONAL_PRIMES]
    for row in rows:
        print('p=%d q=%d supports=%d nonzero_scalars=%d survivors=%d' % row)
    print('TOTAL supports=%d scalars=%d survivors=%d' % (
        sum(r[2] for r in rows), sum(r[3] for r in rows), sum(r[4] for r in rows)))
