#!/usr/bin/env python3
"""Exact, standalone two-method certificate for first fixed-omega divisor-frontier log-concavity failure.

Scope: classical integers, 1 <= n <= 3_175_200, no physical/native residual claim.
All arithmetic is integer. No external packages or external runtime dependencies.
"""

N0 = 3_175_200
N1 = 3_326_400
FIRST_PRIMES = (2, 3, 5, 7, 11, 13, 17)
assert __import__('math').prod(FIRST_PRIMES) <= N0
assert __import__('math').prod(FIRST_PRIMES) * 19 > N1


def ordered_exponent_candidates(limit):
    """Exactly all n = prod p_i**a_i <= limit with a_1 >= ... >= a_k >= 1."""
    out = [(1, 1, 0, ())]

    def visit(i, last_a, n, div_count, exponents):
        if i >= len(FIRST_PRIMES):
            return
        p = FIRST_PRIMES[i]
        t = n
        for a in range(1, last_a + 1):
            if t > limit // p:
                break
            t *= p
            tt = div_count * (a + 1)
            row = (t, tt, i + 1, exponents + (a,))
            out.append(row)
            visit(i + 1, a, t, tt, row[3])

    visit(0, limit.bit_length() - 1, 1, 1, ())
    return sorted(out)


def first_violation_from_candidates(limit):
    candidates = ordered_exponent_candidates(limit)
    values = [0] * (len(FIRST_PRIMES) + 1)
    winners = [0] * (len(FIRST_PRIMES) + 1)
    first = None
    for n, tau, k, _ in candidates:
        if tau <= values[k]:
            continue
        values[k], winners[k] = tau, n
        for j in range(1, len(FIRST_PRIMES)):
            if values[j - 1] and values[j + 1] and values[j] ** 2 < values[j - 1] * values[j + 1]:
                first = (n, j, values[:], winners[:])
                return first, len(candidates)
    return None, len(candidates)


def first_violation_from_all_integers(limit):
    """Independent linear sieve of prime factors, omega and tau for EVERY n <= limit."""
    spf = [0] * (limit + 1)
    prime_list = []
    omega = bytearray(limit + 1)
    last_exp = bytearray(limit + 1)
    tau = [0] * (limit + 1)
    tau[1] = 1
    for n in range(2, limit + 1):
        if spf[n] == 0:
            spf[n] = n
            prime_list.append(n)
            omega[n] = 1
            last_exp[n] = 1
            tau[n] = 2
        for p in prime_list:
            v = n * p
            if v > limit:
                break
            spf[v] = p
            if p == spf[n]:
                last_exp[v] = last_exp[n] + 1
                omega[v] = omega[n]
                tau[v] = tau[n] // (last_exp[n] + 1) * (last_exp[v] + 1)
                break
            omega[v] = omega[n] + 1
            last_exp[v] = 1
            tau[v] = 2 * tau[n]

    maxima = [0] * (len(FIRST_PRIMES) + 1)
    champions = [0] * (len(FIRST_PRIMES) + 1)
    first = None
    for n in range(1, limit + 1):
        k = omega[n]
        if tau[n] <= maxima[k]:
            continue
        maxima[k], champions[k] = tau[n], n
        for j in range(1, len(FIRST_PRIMES)):
            if maxima[j - 1] and maxima[j + 1] and maxima[j] ** 2 < maxima[j - 1] * maxima[j + 1]:
                first = (n, j, maxima[:], champions[:])
                return first, len(prime_list)
    return None, len(prime_list)


def main():
    c, count = first_violation_from_candidates(N0)
    s, prime_count = first_violation_from_all_integers(N0)
    assert c is not None and s is not None
    assert c[:3] == s[:3]
    n, j, ds, ns = c
    assert (n, j) == (N0, 5), (n, j)
    assert ds == [1, 22, 91, 180, 270, 300, 336, 288], ds
    assert ns == [1, 2_097_152, 2_985_984, 2_592_000,
                  3_175_200, 2_494_800, 2_882_880, 3_063_060], ns
    assert 300 * 300 == 90_000
    assert 270 * 336 == 90_720
    assert 90_000 * 126 == 90_720 * 125
    # Upper bound for the first failure interval. The (D4,D5,D6) triple
    # stays constant at every candidate threshold N0 <= N < N1.
    later = ordered_exponent_candidates(N1)
    prev = [0] * (len(FIRST_PRIMES) + 1)
    for x, t, k, _ in later:
        if x >= N1:
            break
        if t > prev[k]:
            prev[k] = t
        if N0 <= x:
            assert (prev[4], prev[5], prev[6]) == (270, 300, 336)
    assert (prev[4], prev[5], prev[6]) == (270, 300, 336)
    restored = [0] * (len(FIRST_PRIMES) + 1)
    for x, t, k, _ in later:
        if t > restored[k]:
            restored[k] = t
    assert (restored[4], restored[5], restored[6]) == (270, 336, 336)
    print('CERTIFIED: first non-log-concave D_k(N) N =', n, '; k =', j)
    print('D[0..7] =', ds)
    print('min champions =', ns)
    print('strict defect D4*D6-D5^2 =', 270 * 336 - 300 ** 2)
    print('ratio D5^2/(D4*D6) = 125/126')
    print('first failing interval includes all N in [3175200, 3326399]')
    print('canonical candidate count =', count)
    print('independent sieve prime count =', prime_count)
    print('PASS: two independent complete integer enumeration paths agree')


if __name__ == '__main__':
    main()
