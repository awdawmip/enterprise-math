#!/usr/bin/env python3
"""Independent W2 combinatorial certificate, NOT the frozen R063 Stage3/Stage0 replay."""
from collections import Counter
from itertools import combinations, product
from math import comb
import json


def words(a, b):
    n = a + b
    return [''.join('i' if k in positions else 'j' for k in range(n))
            for positions in combinations(range(n), a)]


def remnant_sets(p, q):
    cells = [(r, s, (int(x == 'j') + int(y == 'j')) % 4)
             for r, x in enumerate(p) for s, y in enumerate(q)]
    groups = {k: [c for c in cells if c[2] == k] for k in range(4)}
    options = [()]
    for a, b in ((0, 2), (1, 3)):
        pool = groups[a] if len(groups[a]) >= len(groups[b]) else groups[b]
        survivors = abs(len(groups[a]) - len(groups[b]))
        options = [prev + extra for prev in options
                   for extra in combinations(pool, survivors)]
    return [tuple(sorted(x)) for x in options]


def ordered_linearizations(items):
    items = list(items)
    preds = [{j for j, d in enumerate(items)
              if d[0] <= c[0] and d[1] <= c[1]
              and (d[0] < c[0] or d[1] < c[1])}
             for c in items]
    output = Counter()

    def visit(used, word):
        if len(used) == len(items):
            output[word] += 1
            return
        for k in range(len(items)):
            if k not in used and preds[k].issubset(used):
                visit(used | {k}, word + ('i' if items[k][2] == 0 else 'j'))

    visit(frozenset(), '')
    return output


def relation(p, q):
    out = Counter()
    for residual in remnant_sets(p, q):
        out.update(ordered_linearizations(residual))
    return out


def neighbors(word):
    return {word[:k] + word[k + 1] + word[k] + word[k + 2:]
            for k in range(len(word) - 1) if word[k] != word[k + 1]}


def one_step(support):
    return set(support) | set().union(*(neighbors(w) for w in support))


def radius(support, full):
    reached, frontier, steps = set(support), set(support), 0
    while reached != full:
        frontier = set().union(*(neighbors(w) for w in frontier)) - reached
        assert frontier
        reached |= frontier
        steps += 1
    return steps


def minimal_covers(supports, full, transform=lambda s: s):
    found = []
    for count in range(1, len(supports) + 1):
        for ids in combinations(range(len(supports)), count):
            covered = set().union(*(supports[i] for i in ids))
            if transform(covered) == full:
                found.append(ids)
        if found:
            return count, found
    raise AssertionError('no cover')


def main():
    basis = words(2, 1)
    pairs = list(product(basis, repeat=2))
    layers = [relation(p, q) for p, q in pairs]
    supports = [set(r) for r in layers]
    target = set(words(3, 4))
    union = set().union(*supports)
    missing = sorted(target - union)
    base_size, base_min = minimal_covers(supports, union)
    swap_size, swap_min = minimal_covers(supports, target, one_step)
    boundary = {w: sorted(neighbors(w) & union) for w in missing}
    output = {
        'source_pairs': [list(x) for x in pairs],
        'support_size_matrix': [list(map(len, supports[i:i + 3])) for i in (0, 3, 6)],
        'formal_witness_sum_all_source_pairs': sum(map(lambda r: sum(r.values()), layers)),
        'native_path_count': comb(7, 3),
        'source_union_size': len(union),
        'missing_words': missing,
        'missing_one_swap_boundary': boundary,
        'minimum_source_pairs_for_stage3_union': base_size,
        'number_of_minimum_original_covers': len(base_min),
        'first_minimum_original_cover': [list(pairs[i]) for i in base_min[0]],
        'minimum_source_pairs_after_one_swap': swap_size,
        'number_of_minimum_one_swap_covers': len(swap_min),
        'first_minimum_one_swap_cover': [list(pairs[i]) for i in swap_min[0]],
        'max_one_pair_graph_radius': max(radius(s, target) for s in supports),
        'all_nine_union_graph_radius': radius(union, target),
        'subset_masks_checked': 2 ** 9 - 1,
    }
    assert output['support_size_matrix'] == [[5, 14, 8], [14, 11, 14], [8, 14, 5]]
    assert output['native_path_count'] == 35
    assert output['source_union_size'] == 31
    assert missing == ['iijjjji', 'ijjjjii', 'jiiijjj', 'jjjiiij']
    assert output['formal_witness_sum_all_source_pairs'] == 524
    assert (base_size, len(base_min)) == (6, 8)
    assert (swap_size, len(swap_min)) == (2, 4)
    assert output['max_one_pair_graph_radius'] == 9
    assert output['all_nine_union_graph_radius'] == 1
    assert all(len(v) == 2 for v in boundary.values())
    print(json.dumps(output, ensure_ascii=False, sort_keys=True, separators=(',', ':')))
    print('PASS_X6_LP019_R063_STAGE3_W2_MINIMAL_SOURCE_COVER')


if __name__ == '__main__':
    main()
