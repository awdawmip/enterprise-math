"""R720 exact finite certificate for three-tag-local BRC Boolean source recovery.

Run: python R720_BRC_THREE_AXIS_LEDGER_VERIFY.py
Python standard library only; source membership bits are labeled triple branches
and the 15-dimensional pair ledger is an exact integer-count observer.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path

V = tuple(range(6))
TAGS = frozenset((0, 1, 2))
EDGES = tuple(combinations(V, 2))
TRIPLES = tuple(t for t in combinations(V, 3) if TAGS.intersection(t))
assert len(EDGES) == 15 and len(TRIPLES) == 19
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}
BASE = 5  # Each pair belongs to four triples: packed counts have no carries.
COLUMN = tuple(sum(BASE ** EDGE_INDEX[e] for e in combinations(t, 2)) for t in TRIPLES)


def bareiss_det(matrix):
    """Fraction-free exact determinant."""
    a = [list(row) for row in matrix]
    n = len(a)
    prev, sign = 1, 1
    for k in range(n - 1):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * p - a[i][k] * a[k][j]
                assert numerator % prev == 0
                a[i][j] = numerator // prev
            a[i][k] = 0
        prev = p
    return sign * a[-1][-1]


def fibers_by_pair_ledger():
    """Exhaust 2^19 states once each, updating exact ledger in Gray-code order."""
    fibers = defaultdict(list)
    key = previous = 0
    for i in range(1 << len(TRIPLES)):
        state = i ^ (i >> 1)
        if i:
            changed = state ^ previous
            j = changed.bit_length() - 1
            key += COLUMN[j] if state & changed else -COLUMN[j]
        fibers[key].append(state)
        previous = state
    return fibers


@lru_cache(None)
def optimal_adaptive_depth(states):
    """Minimum possible worst-case depth among all membership-query decision trees."""
    if len(states) < 2:
        return 0
    best = len(states) - 1
    for j in range(len(TRIPLES)):
        left = tuple(s for s in states if (s >> j) & 1 == 0)
        if not left or len(left) == len(states):
            continue
        right = tuple(s for s in states if (s >> j) & 1 == 1)
        best = min(best, 1 + max(optimal_adaptive_depth(left),
                                  optimal_adaptive_depth(right)))
        if best == (len(states) - 1).bit_length():
            break
    return best


def main():
    fibers = fibers_by_pair_ledger()
    sizes = Counter(map(len, fibers.values()))
    differences = Counter()
    for states in fibers.values():
        for a, b in combinations(states, 2):
            differences[a ^ b] += 1
    fixed_counts = {}
    for k in range(5):
        count = 0
        for q in combinations(range(len(TRIPLES)), k):
            probe_mask = sum(1 << bit for bit in q)
            if all(probe_mask & diff for diff in differences):
                count += 1
        fixed_counts[k] = count

    probes = tuple(TRIPLES.index(t) for t in
                   ((0, 1, 3), (0, 1, 4), (0, 2, 3), (0, 2, 4)))
    remaining = tuple(i for i in range(19) if i not in probes)
    minor = [[int(e[0] in TRIPLES[j] and e[1] in TRIPLES[j])
              for j in remaining] for e in EDGES]
    det = bareiss_det(minor)

    adaptive = Counter()
    for states in fibers.values():
        adaptive[optimal_adaptive_depth(tuple(states))] += 1

    actual = {
        "states": sum(n * count for n, count in sizes.items()),
        "distinct_pair_ledgers": len(fibers),
        "fiber_size_histogram": {str(k): v for k, v in sizes.items()},
        "max_fiber_size": max(sizes),
        "max_fiber_count": sizes[max(sizes)],
        "collision_pairs": sum(differences.values()),
        "distinct_difference_supports": len(differences),
        "difference_support_histogram": {
            str(k): v for k, v in Counter(m.bit_count() for m in differences).items()
        },
        "minimal_fixed_queries": next(k for k, v in fixed_counts.items() if v),
        "number_optimal_fixed_query_sets": fixed_counts[4],
        "example_fixed_queries": ["".join(map(str, TRIPLES[i])) for i in probes],
        "determinant_remaining_matrix": det,
        "adaptive_depth_histogram": {str(k): v for k, v in adaptive.items()},
        "minimal_adaptive_queries": max(adaptive),
        "minimal_arbitrary_encoding_bits": (max(sizes) - 1).bit_length(),
    }
    expected = json.loads(Path(__file__).with_name(
        "R720_BRC_THREE_AXIS_LEDGER_EVIDENCE.json").read_text(encoding="utf-8"))
    for key, value in actual.items():
        assert value == expected[key], (key, value, expected[key])
    assert fixed_counts == {0: 0, 1: 0, 2: 0, 3: 0, 4: 1296}
    assert det == 96
    assert all(m.bit_count() in (8, 12) for m in differences)
    print("R720_BRC_THREE_AXIS_LEDGER_EXACT_PASS")
    print(json.dumps(actual, sort_keys=True))


if __name__ == "__main__":
    main()
