"""R004. Finite, exact checks of cumulative scalar readings on one hidden graph.

Run with Python 3.9 or later. The default output is deterministic JSON.
"""

import json
from collections import Counter
from functools import cache
from itertools import product
from math import comb, gcd


def additive_order_length(value, modulus, p):
    length = 0
    while value:
        value = p * value % modulus
        length += 1
    return length


def cyclic_capacities(p, k):
    capacities = [1]
    for depth in range(1, k + 1):
        if depth < p:
            capacities.append(2 ** depth)
        else:
            capacities.append(sum(capacities[-p:]))
    return k + 1, capacities[-1]


def budget_formula(p, k):
    @cache
    def count(turns, depth, allowed):
        if allowed == 0:
            return 0
        if depth == 0 or turns == 0:
            return 1
        if allowed == 1:
            return count(turns, depth - 1, p)
        best = 0
        for length in range(1, depth + 1):
            new_depth = depth - length
            good = count(turns - 1, new_depth, p)
            first_wrong = count(turns - 1, new_depth, allowed - 1)
            later_wrong = count(turns - 1, new_depth, p - 1)
            best = max(best, good + first_wrong + (length - 1) * later_wrong)
        return best

    return [count(turns, k, p) for turns in range(k + 1)]


def cyclic_addresses(p, a, b):
    """Real coefficients before identifying equal readouts, including v outside G[p^a]."""
    modulus = p ** b
    values = range(0, modulus, p ** max(0, b - a))
    lengths = [additive_order_length(z, modulus, p) for z in range(modulus)]
    responses = {tuple(lengths[(v - u * x) % modulus] for x in values)
                 for u in range(p ** a) for v in range(modulus)}
    return len(values), sorted(responses)


def unrestricted_cyclic_trees(p, a, b):
    slopes, response_table = cyclic_addresses(p, a, b)
    indices = tuple(range(slopes))

    @cache
    def adaptive(height, candidates, turns):
        if turns == 0 or len(candidates) == 1:
            return 1
        best = 1
        for reading in response_table:
            groups = {}
            for index in candidates:
                result = max(height, reading[index])
                groups.setdefault(result, []).append(index)
            if len(groups) > 1:
                leaves = sum(adaptive(result, tuple(group), turns-1)
                             for result, group in groups.items())
                best = max(best, leaves)
        return best

    @cache
    def fixed(heights, partition):
        previous = len(set(partition))
        best = previous
        for reading in response_table:
            new_heights = tuple(map(max, heights, reading))
            # Relabel by first occurrence, so cached states depend only on membership.
            labels = {}
            new_partition = tuple(labels.setdefault(pair, len(labels))
                                  for pair in zip(partition, new_heights))
            if len(labels) > previous:
                best = max(best, fixed(new_heights, new_partition))
        return best

    fixed_leaves = fixed((0,) * slopes, (0,) * slopes)
    k = min(a, b)
    by_budget = [adaptive(0, indices, turns) for turns in range(k + 1)]
    assert by_budget == budget_formula(p, k)
    # Any informative step strictly reduces every candidate set on its branch.
    adaptive_leaves = adaptive(0, indices, slopes - 1)
    assert adaptive_leaves == by_budget[-1]
    assert (fixed_leaves, adaptive_leaves) == cyclic_capacities(p, min(a, b))
    return dict(p=p, a=a, b=b, slopes=slopes, named_addresses=p ** (a + b),
                distinct_address_readouts=len(response_table),
                fixed_leaves=fixed_leaves, adaptive_leaves=adaptive_leaves,
                adaptive_leaves_by_query_budget=by_budget)


def cyclic_digit_tree(p, k):
    """Execute the attaining policy on the actual scalar x and record its leaf."""
    modulus = p ** k
    leaves = {}
    for x in range(modulus):
        height = prefix_size = prefix_value = 0
        allowed = list(range(p))
        path = []
        while height + prefix_size < k:
            guess = allowed[0]
            center = prefix_value + guess * p ** prefix_size
            if len(allowed) > 1:
                u = p ** (k - height - prefix_size - 1)
                v = u * center % modulus
                raw = additive_order_length((v - u * x) % modulus, modulus, p)
                outcome = max(height, raw)
                path.append((u, v, outcome))
                if outcome > height:
                    assert outcome == height + 1
                    height = outcome
                    allowed = allowed[1:]
                    continue
            prefix_value = center
            prefix_size += 1
            allowed = list(range(p))
        leaves.setdefault(tuple(path), []).append(x)
    assert len(leaves) == cyclic_capacities(p, k)[1]
    return [dict(columns_and_readout=[list(step) for step in steps], slopes=slopes)
            for steps, slopes in leaves.items()]


def two_step_example():
    leaves = {}
    for x in range(8):
        first = additive_order_length((-4*x) % 8, 8, 2)
        second_target = 1 if first else 0
        second = max(first, additive_order_length((second_target-x) % 8, 8, 2))
        leaves.setdefault((first, second), []).append(x)
    assert sorted(leaves.values()) == [[0], [1, 5], [2, 6], [3, 7], [4]]
    return [[list(readings), candidates] for readings, candidates in sorted(leaves.items())]


def check_raw_matrix():
    """Independent determinantal divisor of the original two-row integer matrix."""
    q = 4
    all_columns = list(product(range(q), repeat=2))
    histogram = Counter()
    for x in range(q):
        for probes in product(all_columns, repeat=3):
            columns = ((1, x),) + probes
            minors = [a * d - b * c for i, (a, b) in enumerate(columns)
                      for c, d in columns[:i]]
            divisor = gcd(q, *minors)
            actual = (q // divisor).bit_length() - 1
            predicted = max(additive_order_length((v - u * x) % q, q, 2)
                            for u, v in probes)
            assert actual == predicted
            histogram[actual] += 1
    return dict(modulus=q, hidden_slopes=q, menu=len(all_columns), probes_per_word=3,
                cases=sum(histogram.values()), final_length_counts=sorted(histogram.items()))


def vector_total(x, y, scalar, p):
    return tuple((v + scalar * w) % p for v, w in zip(x, y))


def field_flag_check(p, s, t):
    vectors = list(product(range(p), repeat=t))
    target_basis = tuple(tuple(int(i == j) for i in range(t)) for j in range(t))
    histogram = Counter()
    for images in product(vectors, repeat=s):
        space = {(0,) * t}
        bits = []
        for v in images + target_basis:
            bits.append(int(v not in space))
            if bits[-1]:
                space = {vector_total(x, v, j, p) for x in space for j in range(p)}
        histogram[tuple(bits)] += 1

    assert len(histogram) == comb(s + t, s)
    for bits, multiplicity in histogram.items():
        increases = [i for i in range(s) if bits[i]]
        pivots = [j + 1 for j in range(t) if not bits[s + j]]
        exponent = sum(column - rank for rank, column in enumerate(pivots, 1))
        predicted = p ** exponent
        for i in range(s):
            prior = sum(row < i for row in increases)
            predicted *= p ** len(increases) - p ** prior if i in increases else p ** prior
        assert multiplicity == predicted

    result = dict(p=p, control_dimension=s, target_dimension=t, maps=p ** (s * t),
                  flag_leaves=len(histogram),
                  size_and_number=sorted(Counter(histogram.values()).items()))
    if (p, s, t) == (2, 2, 2):
        result["all_bit_strings"] = {"".join(map(str, bits)): amount
                                     for bits, amount in sorted(histogram.items())}
    return result


def field_tree_check(p, s, t):
    """Separate adaptive search over all actual linear maps and all column spans."""
    vectors = list(product(range(p), repeat=t))
    points = list(product(range(p), repeat=s+t))
    hidden_maps = list(product(vectors, repeat=s))
    point_index = {v: i for i, v in enumerate(points)}
    projections = []
    for images in hidden_maps:
        residuals = []
        for v in points:
            residual = tuple((v[s + j] - sum(v[i] * images[i][j] for i in range(s))) % p
                             for j in range(t))
            residuals.append(residual)
        projections.append(residuals)

    @cache
    def extensions(space):
        children = set()
        for v in range(1, len(points)):
            if v not in space:
                child = {point_index[vector_total(points[u], points[v], j, p)]
                         for u in space for j in range(p)}
                children.add(tuple(sorted(child)))
        return sorted(children)

    @cache
    def image_size(mapping, space):
        return len({projections[mapping][i] for i in space})

    @cache
    def leaves(space, candidates):
        if len(candidates) == 1:
            return 1
        best = 1
        for child in extensions(space):
            groups = {}
            for mapping in candidates:
                groups.setdefault(image_size(mapping, child), []).append(mapping)
            best = max(best, sum(leaves(child, tuple(group)) for group in groups.values()))
        return best

    actual = leaves((0,), tuple(range(len(hidden_maps))))
    assert actual == comb(s+t, s)
    return dict(p=p, s=s, t=t, maps=len(hidden_maps), named_addresses=len(points),
                adaptive_leaves=actual)


def main():
    cases = [(2, k, k) for k in range(1, 7)] + [(3, k, k) for k in range(1, 5)]
    cases += [(p, k, k) for p in (5, 7) for k in (1, 2)]
    cases += [(2, 2, 3), (2, 3, 2), (2, 3, 4), (2, 4, 3), (3, 1, 2), (3, 2, 1)]
    return {
        "contract": "One hidden graph, no reset, cumulative lengths, full named-column menu",
        "cyclic_all_address_search": [unrestricted_cyclic_trees(*case) for case in cases],
        "sample_2_adic_three_digits": cyclic_digit_tree(2, 3),
        "two_step_example_in_text": two_step_example(),
        "raw_matrix": check_raw_matrix(),
        "field_flag_multiplicities": [field_flag_check(*case) for case in
                                      [(2,2,2), (3,2,2), (2,2,3), (2,3,2), (3,1,3), (2,3,3)]],
        "field_all_address_search": [field_tree_check(*case) for case in
                                     [(2,1,2), (2,2,1), (3,1,1), (2,2,2)]],
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
