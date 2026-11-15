"""Exact finite checks for conditional m-product directed C12 phase fibers.

Standalone author-side verification only. No native Cell/Link/Port permission or
formal CLAIM/Result is asserted by these finite checks.
"""
from itertools import product
from math import comb


def choose(n, r):
    return comb(n, r) if 0 <= r <= n else 0


def phase_count_formula(m, k):
    return sum(
        (-1) ** j * comb(m - 1, j) * choose(k - 12 * j + m - 1, m - 1)
        for j in range(m)
    )


def phase_count_direct(m, k):
    return sum(
        k >= sum(a) and (k - sum(a)) % 12 == 0
        for a in product(range(12), repeat=m)
    )


def count_vectors(m, k):
    if m == 1:
        yield (k,)
    else:
        for i in range(k + 1):
            for tail in count_vectors(m - 1, k - i):
                yield (i,) + tail


def check_fibers(m, k):
    fibers = {}
    for n in count_vectors(m, k):
        a = tuple(x % 12 for x in n)
        fibers[a] = fibers.get(a, 0) + 1
    assert sum(fibers.values()) == choose(k + m - 1, m - 1)
    assert len(fibers) == phase_count_formula(m, k)
    assert max(fibers.values()) == choose(k // 12 + m - 1, m - 1)
    for a, size in fibers.items():
        q, rem = divmod(k - sum(a), 12)
        assert rem == 0 and q >= 0
        assert size == choose(q + m - 1, m - 1)


def main():
    checks = 0
    for m in range(1, 6):
        for k in range(51):
            f = phase_count_direct(m, k)
            assert f == phase_count_formula(m, k), (m, k, f)
            if k >= 11 * (m - 1):
                assert f == 12 ** (m - 1)
            if m >= 2 and k == 11 * (m - 1) - 1:
                assert f == 12 ** (m - 1) - 1
            checks += 1
    fiber_checks = 0
    for m, max_k in ((1, 32), (2, 35), (3, 35), (4, 24), (5, 16)):
        for k in range(max_k + 1):
            check_fibers(m, k)
            fiber_checks += 1
    assert choose(13, 1) == 13
    assert choose(13, 11) == 78
    print(
        f"X6_TIME_ALL_K_PHASE_FIBER_EXACT_PASS "
        f"phase_checks={checks} fiber_checks={fiber_checks}"
    )


if __name__ == "__main__":
    main()
