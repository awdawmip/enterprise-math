"""Exact closed forms, independent partition enumeration and optional frozen replay."""
import argparse
import json
from itertools import combinations
from math import inf, isqrt
import sys


def least_factor(value):
    for d in range(2, isqrt(value) + 1):
        if value % d == 0:
            return d
    return value


def dense_loss(n, r, p):
    quotient, extra = divmod(n, p * r)
    return n - quotient * r - min(r, extra)


def interval_loss(n, start, width, r):
    if r < width:
        return inf
    quotient, remainder = divmod(n, r)
    lo, hi = (0, remainder) if quotient % 2 == 0 else (remainder, r)
    block = start // r
    if block % 2 == 0:
        block += 1
    left = max(start, block * r + lo)
    right = min(start + width, block * r + hi)
    return dense_loss(n, r, 2) + max(0, right - left)


def ends_loss(n, a, b, r):
    if r < max(a, b):
        return inf
    lo = (n + 1 - a - b + r - 1) // r
    hi = (n - 1) // r
    if lo > hi:
        return dense_loss(n, r, 2)
    if lo != hi or lo == 1:
        return inf
    return dense_loss(n, r, least_factor(lo))


def prefix_span(h, width, e):
    if width > h:
        return width - 1
    return e + max(r * ((e + r) // r) for r in range(max(1, width), h + 1))


def signatures(s, a):
    pairs = [y - x for x, y in combinations(sorted(s), 2)]
    return [tuple(d % r == 0 for d in pairs) for r in range(1, a + 2)]


def fail(s, h, a):
    obs = signatures(s, a)
    return any(sig == obs[i] for i in range(h) for j, sig in enumerate(obs) if i != j)


def subsets(s):
    for k in range(len(s) + 1):
        yield from combinations(s, k)


def direct(n, protected, h):
    optional = sorted(set(range(n)) - protected)
    for erased in subsets(optional):
        if fail(set(range(n)) - set(erased), h, n - 1):
            return len(erased)
    return inf


def families(n):
    yield set(), lambda r: interval_loss(n, 0, 0, r)
    for width in range(1, n + 1):
        for start in range(n - width + 1):
            yield set(range(start, start + width)), lambda r: interval_loss(n, start, width, r)
    for a in range(1, n):
        for b in range(1, n - a + 1):
            yield set(range(a)) | set(range(n - b, n)), lambda r: ends_loss(n, a, b, r)


def run(frozen_src):
    stats = {}
    count = 0
    for n in range(2, 9):
        for core, cost in families(n):
            for h in range(1, n):
                assert min(cost(r) for r in range(1, h + 1)) == direct(n, core, h)
                count += 1
    stats['direct_erasure_all_order_instances_N_2_to_8'] = count

    count = 0
    for h in range(1, 22):
        for width in range(h + 3):
            for e in range(21):
                candidate = prefix_span(h, width, e)
                def viable(a):
                    return a >= max(h, width - 1) and all(interval_loss(a + 1, 0, width, r) > e for r in range(1, h + 1))
                assert viable(candidate) and not viable(candidate - 1)
                if e < h and width <= h:
                    assert candidate == e + (max(h, 2 * e) if width <= e else h)
                count += 1
    stats['prefix_threshold_inequalities_H_1_to_21'] = count

    count = 0
    for w in range(3, 8):
        amax = 3 * w
        for left in range(1, 2 * w):
            right = 2 * w - left
            p = set(range(left)) | set(range(amax + 1 - right, amax + 1))
            optional = sorted(set(range(amax + 1)) - p)
            weak = max(left, right) <= w + 1
            assert fail(p, amax, amax) == weak
            for x in optional:
                assert not fail(p | {x}, amax, amax)
            # Robustness now follows by monotonicity. Also check the actual
            # signatures on EVERY support, including the individual unique alias.
            for x in subsets(optional):
                sig = signatures(p | set(x), amax)
                aliases = [(i, j) for i, j in combinations(range(1, amax + 2), 2) if sig[i - 1] == sig[j - 1]]
                assert aliases == ([(w + 1, 2 * (w + 1))] if weak and not x else [])
                count += 1
    stats['two_strip_pareto_supports_w_3_to_7'] = count

    if frozen_src:
        sys.path.insert(0, frozen_src)
        from enterprise_math.group_ring_span_erasures import _coarsening_cut, certify_span_erasures
        count = 0
        for n in range(2, 19):
            s = tuple(range(n))
            for core, cost in families(n):
                for r in range(1, n):
                    ps = [p for p in range(2, (n - 1) // r + 1) if least_factor(p) == p]
                    cuts = [_coarsening_cut(s, r, p, core) for p in ps or (2,)]
                    assert min([len(x) for x in cuts if x is not None] or [inf]) == cost(r)
                    count += 1
        stats['frozen_per_r_source_comparisons_N_2_to_18'] = count
        count = 0
        for w in range(3, 8):
            h = 3 * w
            for left in range(1, 2 * w):
                right = 2 * w - left
                p = set(range(left)) | set(range(h + 1 - right, h + 1))
                for x in subsets(sorted(set(range(h + 1)) - p)):
                    ans = certify_span_erasures(p | set(x), h, h, protected=p).certificate
                    assert ans.minimum_deletions == (len(x) if max(left, right) <= w + 1 else None)
                    if ans.minimum_deletions is not None:
                        assert ans.erased_marks == tuple(x)
                    count += 1
        stats['frozen_full_certificate_Pareto_supports'] = count
    assert signatures({0, 1, 2, 3, 8, 9, 10, 11}, 11)[3] == signatures({0, 1, 2, 3, 8, 9, 10, 11}, 11)[7]
    assert signatures({0, 3, 6}, 6)[0] == signatures({0, 3, 6}, 6)[2]
    assert signatures({0, 3, 6}, 6)[0] != signatures({0, 3, 6}, 6)[1]
    assert ends_loss(4, 1, 1, 1) == 2 and direct(4, {0, 3}, 1) == 2
    assert interval_loss(5, 2, 1, 2) == 3 and dense_loss(5, 2, 2) == 2
    stats['witnesses'] = {'H6_existing_erase': [4, 5, 6, 7], 'sparse_existing_erase': [1], 'two_ends_A3_H1_erase': [1, 2], 'interior_N5_r2_extra_cost': 1}
    return stats


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--frozen-src', help='path to enterprise-math/src at the cited frozen revision')
    args = parser.parse_args()
    print(json.dumps(run(args.frozen_src), indent=2, sort_keys=True))
