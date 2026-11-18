"""Count precommitted protection sets by size and minimum destructive cost."""

from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb, prod


def histogram(support, r, d):
    groups = defaultdict(Counter)
    for x in support:
        groups[x % r][x % (r*d)] += 1
    coefficients = Counter({(0, 0): 1})
    for counts in groups.values():
        n = sum(counts.values())
        local = Counter({(0, n-max(counts.values())): 1})
        for size in counts.values():
            for j in range(1, size + 1):
                local[j, n-size] += comb(size, j)
        new = Counter()
        for (j, e), a in coefficients.items():
            for (k, f), b in local.items():
                new[j+k, e+f] += a*b
        coefficients = new
    return coefficients


def blocks_all_counts(support, r, primes):
    out = Counter()
    for flags in product((0, 1), repeat=len(primes)):
        d = prod(p**b for p, b in zip(primes, flags))
        for (j, _), count in histogram(support, r, d).items():
            out[j] += (-1)**sum(flags) * count
    return out


def powerset(values):
    for j in range(len(values)+1):
        yield from combinations(values, j)


def alias(points, r, p):
    return all((x-y) % r or (x-y) % (r*p) == 0 for x, y in combinations(points, 2))


def by_enumeration(support, r, primes):
    all_subsets = [frozenset(s) for s in powerset(support)]
    protected_counts = Counter()
    for p in primes:
        good_survivors = [s for s in all_subsets if alias(s, r, p)]
        actual = Counter()
        for core in all_subsets:
            sizes = [len(s) for s in good_survivors if core <= s]
            if sizes:
                actual[len(core), len(support)-max(sizes)] += 1
        assert histogram(support, r, p) == actual
    for core in all_subsets:
        if all(not alias(core, r, p) for p in primes):
            protected_counts[len(core)] += 1
    assert protected_counts == blocks_all_counts(support, r, primes)


def main():
    small = ((0, 2, 3), (0, 1, 2, 4, 7, 8), tuple(range(9)), (2, 4, 7, 10, 13, 18, 20))
    for support in small:
        for r in range(1, 7):
            by_enumeration(support, r, (2, 3, 5))
    support = tuple(range(31))
    counts = blocks_all_counts(support, 5, (2, 3, 5))
    print("S=0..30, r=5, protected sizes 2..6:", [counts[j] for j in range(2, 7)])
    by_cost = histogram(support, 5, 3)
    print("same support/r, comparison with 15, four protected:",
          sorted((e, v) for (j, e), v in by_cost.items() if j == 4))
    core = {0}
    assert alias((0, 2), 1, 2) and alias((0, 3), 1, 3)
    assert all(not alias(core | {z}, 1, 6) for z in (2, 3))
    print("24 support/order cases checked by enumerating cores and surviving sets")


if __name__ == "__main__":
    main()
