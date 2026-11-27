from collections import Counter
from functools import cache
from itertools import combinations_with_replacement
import json


P = 11
BUDGET = 2331
MODULI = tuple(P ** k for k in range(1, 7))


def smooth(value):
    for prime in (2, 3, 5, 7, 11):
        while value % prime == 0:
            value //= prime
    return value == 1


ALL_UNITS = tuple(m for m in range(1, (BUDGET + 1) // P + 1) if m % P)
SMOOTH_UNITS = tuple(m for m in ALL_UNITS if smooth(m))
REMAINDER = {m: P * (m % P) - 1 for m in ALL_UNITS}
SIGNATURE = {
    m: tuple(pow(m, -k, modulus) for k, modulus in enumerate(MODULI, start=1))
    for m in ALL_UNITS
}


def signature(side):
    return tuple(sum(SIGNATURE[m][k] for m in side) % modulus for k, modulus in enumerate(MODULI))


def top_sides(atoms):
    limit = BUDGET - P * P * 19
    possible = tuple(m for m in atoms if REMAINDER[m] <= limit)
    return [
        side for length in range(1, 4) for side in combinations_with_replacement(possible, length)
        if sum(m // P for m in side) == 19 and sum(REMAINDER[m] for m in side) <= limit
    ]


def prefix_counts(sides):
    stats = []
    for n in range(1, 7):
        counts = Counter(signature(side)[:n] for side in sides)
        stats.append([len(counts), sum(c * (c - 1) // 2 for c in counts.values())])
    return stats


def collision_examples(sides, n):
    first = {}
    examples = []
    for u in sides:
        key = signature(u)[:n]
        if key in first:
            examples.append((first[key], u))
        first[key] = u
    return examples


def older_squared_check():
    units = tuple(m for m in range(1, (BUDGET + 1) // (P * P) + 1) if m % P)
    counts = Counter()

    def walk(start, budget, side):
        counts[tuple(sum(pow(m, -k, P ** k) for m in side) % (P ** k) for k in (1, 2, 3))] += 1
        for i in range(start, len(units)):
            m = units[i]
            cost = P * P * m - 1
            if cost > budget:
                break
            walk(i, budget - cost, (*side, m))

    walk(0, BUDGET, ())
    assert len(counts) == counts.total() == 2020
    return len(counts)


def emit_smooth(order, collect):
    limit = BUDGET - P * P * order
    atoms = tuple(sorted(SMOOTH_UNITS, key=lambda m: (m < P, -(m // P), REMAINDER[m])))
    mod5, mod6 = MODULI[-2:]
    q = tuple(m // P for m in atoms)
    w = tuple(REMAINDER[m] for m in atoms)
    sig = tuple(SIGNATURE[m][-2:] for m in atoms)
    unreachable = limit + 1
    minimum = [[0] + [unreachable] * order for _ in range(len(atoms) + 1)]
    for i in range(len(atoms) - 1, -1, -1):
        minimum[i] = minimum[i + 1].copy()
        if q[i]:
            for elevation in range(q[i], order + 1):
                minimum[i][elevation] = min(minimum[i][elevation], minimum[i][elevation - q[i]] + w[i])

    @cache
    def next_atoms(start, elevation, budget):
        return tuple(i for i in range(start, len(atoms)) if q[i] <= elevation and
                     w[i] + minimum[i][elevation - q[i]] <= budget)

    def walk(start, elevation, budget, s5, s6):
        if elevation == 0:
            collect(s5 % mod5, s6 % mod6)
        for i in next_atoms(start, elevation, budget):
            a5, a6 = sig[i]
            walk(i, elevation - q[i], budget - w[i], s5 + a5, s6 + a6)

    walk(0, order, limit, 0, 0)


def exact_counts(order):
    budget = BUDGET - P * P * order
    ways = [[0] * (budget + 1) for _ in range(order + 1)]
    ways[0][0] = 1
    for m in SMOOTH_UNITS:
        for elevation in range(m // P, order + 1):
            for cost in range(REMAINDER[m], budget + 1):
                ways[elevation][cost] += ways[elevation - m // P][cost - REMAINDER[m]]
    return sum(ways[order])


def main():
    literal = top_sides(ALL_UNITS)
    smooth_top = top_sides(SMOOTH_UNITS)
    assert len(literal) == 73 and len(smooth_top) == exact_counts(19) == 9
    literal_stats = prefix_counts(literal)
    smooth_stats = prefix_counts(smooth_top)
    assert literal_stats[3] == [70, 3] and literal_stats[4] == [73, 0]
    assert smooth_stats[2] == [8, 1] and smooth_stats[3] == [9, 0]
    keys19 = Counter(signature(side)[-2:] for side in smooth_top)
    keys18 = Counter()

    def record18(s5, s6):
        keys18[s5, s6] += 1

    emit_smooth(18, record18)
    assert keys18.total() == exact_counts(18) == 33276
    targets5 = Counter(key[0] for key in keys19.elements())
    targets6 = Counter(key[1] for key in keys19.elements())
    comparisons18 = [sum(targets5[s5] * count for (s5, _), count in keys18.items()),
                     sum(targets6[s6] * count for (_, s6), count in keys18.items()),
                     sum(keys19[key] * count for key, count in keys18.items())]
    projection5 = Counter()
    projection6 = Counter()
    for (s5, s6), count in keys18.items():
        projection5[s5] += count
        projection6[s6] += count
    internal18 = [sum(n * (n - 1) // 2 for n in frequencies.values())
                  for frequencies in (projection5, projection6, keys18)]
    count17 = 0
    comparisons17 = [0, 0, 0]

    def record17(s5, s6):
        nonlocal count17
        count17 += 1
        comparisons17[0] += targets5.get(s5, 0)
        comparisons17[1] += targets6.get(s6, 0)
        comparisons17[2] += keys19.get((s5, s6), 0)

    emit_smooth(17, record17)
    assert count17 == exact_counts(17) == 4180135
    assert not internal18[-1] and not comparisons17[-1] and not comparisons18[-1]
    print(json.dumps({
        "older_squared_profiles": older_squared_check(),
        "literal_order19_profile_count": len(literal),
        "literal_order19_prefix_counts": literal_stats,
        "literal_order19_four_row_matches": collision_examples(literal, 4),
        "smooth_order19_sides": smooth_top,
        "smooth_order19_prefix_counts": smooth_stats,
        "smooth_order19_three_row_match": collision_examples(smooth_top, 3),
        "smooth_order17_profiles": count17,
        "smooth_order18_profiles": keys18.total(),
        "order18_equal_signature_pair_counts_row5_row6_and_both": internal18,
        "orders_17_and_19_equal_signature_pair_counts_row5_row6_and_both": comparisons17,
        "orders_18_and_19_equal_signature_pair_counts_row5_row6_and_both": comparisons18,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
