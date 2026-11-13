#!/usr/bin/env python3
"""R715: exact six-axis Boolean triad source reconstruction queries.
The scientific model is abstract C([6],3) -> C([6],2) pair-degree incidence.
No float, random trials, non-native physical laws, or external modules.
"""
import json
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations

TRIADS = tuple(combinations(range(6), 3))
PAIRS = tuple(combinations(range(6), 2))
PAIR_INDEX = {edge: i for i, edge in enumerate(PAIRS)}
WEIGHTS = tuple(sum(5 ** PAIR_INDEX[e] for e in combinations(t, 2)) for t in TRIADS)
N = 1 << len(TRIADS)

def all_fibers():
    groups = defaultdict(list)
    degree = previous = 0
    for index in range(N):
        state = index ^ (index >> 1)
        if index:
            j = (state ^ previous).bit_length() - 1
            degree += WEIGHTS[j] if ((state >> j) & 1) else -WEIGHTS[j]
        groups[degree].append(state)
        previous = state
    assert sum(map(len, groups.values())) == N
    return groups


def minimal_difference_supports(groups):
    differences = set()
    number_of_colliding_pairs = 0
    for states in groups.values():
        number_of_colliding_pairs += len(states) * (len(states) - 1) // 2
        for x, y in combinations(states, 2):
            differences.add(x ^ y)
    minimal = []
    for mask in sorted(differences, key=lambda m: (m.bit_count(), m)):
        if not any(mask & other == other for other in minimal):
            minimal.append(mask)
    return number_of_colliding_pairs, differences, minimal


def fixed_sensors(minimal):
    found = []
    all_counts = {}
    for k in range(6):
        successful = []
        for choice in combinations(range(20), k):
            m = sum(1 << j for j in choice)
            # All distinct same-ledger pairs must differ on at least one queried bit.
            if all(m & diff for diff in minimal):
                successful.append(m)
        all_counts[str(k)] = len(successful)
        if successful and not found:
            found = successful
    return found, all_counts


@lru_cache(None)
def distinguish_with_depth(states, depth):
    if len(states) <= 1:
        return True
    if depth == 0 or len(states) > (1 << depth):
        return False
    for j in range(20):
        zeros = tuple(m for m in states if not ((m >> j) & 1))
        ones = tuple(m for m in states if ((m >> j) & 1))
        if not zeros or not ones:
            continue
        if max(len(zeros), len(ones)) > (1 << (depth - 1)):
            continue
        if distinguish_with_depth(zeros, depth - 1) and distinguish_with_depth(ones, depth - 1):
            return True
    return False


def adaptive_census(groups):
    census = Counter()
    for states in groups.values():
        if len(states) == 1:
            continue
        state_tuple = tuple(states)
        for depth in range(1, 6):
            if distinguish_with_depth(state_tuple, depth):
                census[(len(states), depth)] += 1
                break
        else:
            raise AssertionError("No depth <= 5 decision tree found")
    return census


def determinant_bareiss(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    sign, previous = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pos = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if pos is None:
                return 0
            a[k], a[pos] = a[pos], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def main():
    groups = all_fibers()
    colliding_pairs, diffs, minimal = minimal_difference_supports(groups)
    fixed_sets, fixed_counts = fixed_sensors(minimal)
    adaptive = adaptive_census(groups)
    sample = min(fixed_sets)
    complement = [i for i in range(20) if not (sample >> i) & 1]
    rows = [[int(set(edge).issubset(TRIADS[j])) for j in complement] for edge in PAIRS]
    determinant = determinant_bareiss(rows)
    sizes = Counter(len(s) for s in groups.values())

    assert len(groups) == 995085 and colliding_pairs == 65286
    assert Counter(m.bit_count() for m in diffs) == {8: 15, 12: 15, 20: 1}
    assert Counter(m.bit_count() for m in minimal) == {8: 15, 12: 15}
    assert fixed_counts == {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 5184}
    assert determinant != 0
    assert adaptive == {(2,1):37650, (3,2):5340, (4,2):1080,
                        (5,3):360, (6,3):70, (7,4):20, (12,4):1}
    assert max(depth for (_, depth) in adaptive) == 4
    assert sum(adaptive.values()) + sizes[1] == len(groups)
    out = {
        'verdict': 'R715_BRC_TRIAD_MEMBERSHIP_QUERY_EXACT_PASS',
        'model': 'All Boolean subsets of C([6],3), 15 exact pair-degree counts known',
        'source_states': N,
        'ledger_fibers': len(groups),
        'fiber_size_histogram': {str(k): sizes[k] for k in sorted(sizes)},
        'colliding_state_pairs': colliding_pairs,
        'distinct_difference_supports': len(diffs),
        'difference_support_size_histogram': dict(sorted(Counter(m.bit_count() for m in diffs).items())),
        'minimal_difference_supports': len(minimal),
        'minimal_difference_support_sizes': dict(sorted(Counter(m.bit_count() for m in minimal).items())),
        'fixed_sensor_count_by_size': fixed_counts,
        'example_universal_fixed_queries': [list(TRIADS[i]) for i in range(20) if (sample >> i) & 1],
        'unqueried_15_column_determinant': determinant,
        'adaptive_depth_census': {f'{k}_states_{d}_queries': count for (k,d),count in sorted(adaptive.items())},
        'worst_case_adaptive_membership_queries': 4,
        'worst_case_fixed_membership_queries': 5,
        'unrestricted_auxiliary_bits_given_ledger': 4,
        'native_scope': 'Unreviewed abstract source carrier; X6 Cell/Link/Port V29/V39 admissibility pending'
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
