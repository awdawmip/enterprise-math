"""Independent finite certificates for unprotected erasures of labelled exponents."""
from collections import Counter
from itertools import combinations
from math import isqrt
import json


def adjacent_matching(marks, r):
    """Maximum disjoint distance-r edges, by the alternating matching on each path."""
    marks = set(marks)
    total = 0
    for start in marks:
        if start - r in marks:
            continue
        end = start + r
        while end in marks:
            end += r
        total += (end - start) // (2 * r)
    return total


def prime_list(n):
    return [v for v in range(2, n + 1) if all(v % d for d in range(2, isqrt(v) + 1))]


def exact_cut(marks, r, p):
    """Exact vertex losses for equal partitions mod r and mod pr."""
    coarse = Counter(x % r for x in marks)
    fine = Counter(x % (p * r) for x in marks)
    largest = Counter()
    for b, n in fine.items():
        largest[b % r] = max(largest[b % r], n)
    return sum(n - largest[b] for b, n in coarse.items())


def robust(marks, h, e, span):
    ps = prime_list(span)
    for r in range(1, h + 1):
        for p in ps:
            if p > 2 and p * r > span:
                break
            if exact_cut(marks, r, p) <= e:
                return False
    return True


def dispensable(h, e):
    if h >= 2 * e:
        return set(range(e + 1, h)) if h >= 2 * e + 3 else set()
    left = set(range(1, e - 1))
    return left | {3 * e - x for x in left}


def holes(h, e):
    if h >= 2 * e:
        t = (h - 2 * e) // 3
        return set(range(e + t, e + 2 * t))
    k = min(2 * e - h, e // 10)
    if k == 0:
        return set(sorted(dispensable(h, e))[:1])
    left = set(range(5 * k, 6 * k))
    return left | {x + 2 * e - k for x in left}


def direct_partitions_identify(marks, h, span):
    seen = {}
    for r in range(1, span + 2):
        pattern = tuple((x - y) % r == 0 for x, y in combinations(marks, 2))
        output = r if r <= h else 0
        if pattern in seen and seen[pattern] != output:
            return False
        seen[pattern] = output
    return True


def check():
    one_hole_supports = direct_masks = interval_pairs = paired_parameters = 0
    for e in range(1, 13):
        for h in range(e + 1, 3 * e):
            span = e + max(h, 2 * e)
            full = set(range(span + 1))
            for x in full:
                assert robust(full - {x}, h, e, span) == (x in dispensable(h, e))
                one_hole_supports += 1
            if e <= 3:
                for x in sorted(full):
                    s = full - {x}
                    # Robustness of a known erasure pattern is monotone in survivors.
                    actual = all(direct_partitions_identify(s - set(loss), h, span)
                                 for loss in combinations(s, e))
                    assert actual == (x in dispensable(h, e))
                    direct_masks += 1
            interval_pairs += 1
    families = {(e, h) for e in range(1, 36) for h in range(e + 1, 3 * e)}
    for e in [50, 51, 74, 75, 99, 100, 125, 150]:
        for j in {1, e // 10, e // 10 + 1, e // 3, e - 1}:
            families.add((e, 2 * e - j))
        families.add((e, 3 * e - 1))
    for e, h in sorted(families):
        span = e + max(h, 2 * e)
        omit = holes(h, e)
        marks = set(range(span + 1)) - omit
        assert {0, span} <= marks
        assert min(adjacent_matching(marks, r) for r in range(1, h + 1)) > e
        if 0 < 2 * e - h <= e // 10:
            assert len(omit) == 2 * (2 * e - h)
            paired_parameters += 1
    retained = set(range(12)) - {4, 5, 6, 7}
    pattern = lambda r: [(x-y) % r == 0 for x,y in combinations(sorted(retained), 2)]
    assert pattern(4) == pattern(8)
    small = {0, 3, 6}
    assert exact_cut(small, 1, 3) == 0 and exact_cut(small, 1, 2) == 1
    examples = []
    for e, h in [(4, 7), (10, 20), (10, 22), (10, 27), (25, 49), (50, 98), (75, 147), (100, 196)]:
        span = e + max(h, 2 * e)
        omit = holes(h, e)
        marks = set(range(span + 1)) - omit
        examples.append(dict(H=h, e=e, A=span, omitted=sorted(omit), marks=len(marks),
                             minimum_disjoint_edges=min(adjacent_matching(marks,r) for r in range(1,h+1))))
    return dict(single_omission_parameters=interval_pairs, single_omission_exact_cuts=one_hole_supports,
                direct_erasure_and_equality_single_omission_tests=direct_masks,
                multiple_omission_parameters=len(families), sharp_paired_parameters=paired_parameters,
                examples=examples)


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
