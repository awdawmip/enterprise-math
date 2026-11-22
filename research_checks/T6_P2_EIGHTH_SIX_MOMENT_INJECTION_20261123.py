#!/usr/bin/env python3
"""T6 mass-bounded exact 2-adic high-denominator cancellation, v2>=8.

Only integer multiplicity enumeration, independent coin-change DP, and modular
inverses of odd denominator cofactors. Check complete original side budget.
"""
from collections import Counter
CAP = 2331
P = 2
EXPECTED = {
    11: [(2, 0)],
    10: [(2, 1), (3, 0)],
    9: [(2, 9), (4, 3), (7, 0)],
    8: [(2, 262), (4, 124), (15, 33), (25, 9), (31, 2), (33, 0)]
}
TOTAL = {11: 2, 10: 3, 9: 7, 8: 33}


def items(v):
    return [(j, 2 ** v * j - 1)
            for j in range(1, CAP // (2 ** v) + 1, 2)]


def enumerate_all(it):
    a = [0] * len(it)
    def go(i, budget):
        if i == len(it):
            yield tuple(a)
            return
        w = it[i][1]
        for n in range(budget // w + 1):
            a[i] = n
            yield from go(i + 1, budget - n * w)
        a[i] = 0
    return list(go(0, CAP))


def independent_count(it):
    dp = [0] * (CAP + 1)
    dp[0] = 1
    for _, w in it:
        for mass in range(w, CAP + 1):
            dp[mass] += dp[mass - w]
    return sum(dp)


def signature(a, it, K):
    return tuple(
        sum(n * pow(pow(j, k, 2 ** k), -1, 2 ** k)
            for n, (j, w) in zip(a, it)) % (2 ** k)
        for k in range(1, K + 1))


def run():
    assert 2 ** 12 > CAP + 1
    for v in (11, 10, 9, 8):
        it = items(v)
        all_profiles = enumerate_all(it)
        assert len(all_profiles) == independent_count(it) == TOTAL[v]
        for K, (unique, pairs) in enumerate(EXPECTED[v], 1):
            freqs = Counter(signature(a, it, K) for a in all_profiles)
            assert len(freqs) == unique
            assert sum(m * (m - 1) // 2 for m in freqs.values()) == pairs
            print(f"v2={v}, k={K}: {len(all_profiles)} profiles, {unique} signatures, {pairs} collision pairs")
        assert len(set(signature(a, it, len(EXPECTED[v]))
                       for a in all_profiles)) == len(all_profiles)
    print("PASS: all denominators divisible by 2^8 cancel from full H0..H6")


if __name__ == "__main__":
    run()
