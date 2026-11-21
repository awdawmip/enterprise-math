"""Complete size/embedding minimum-cost plan for twelve nonempty classes.

E counts EVERY class contained in some legal thirteen-point mother. Large E
counts only such classes of size at least eleven; the two counts are distinct.
The native cost catalogue is hash-pinned. No eleven-label-only exclusion is
used. Both trivial and inherited unrestricted mother-union bounds are reported.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
from itertools import product
from pathlib import Path
import argparse
import json

HERE = Path(__file__).resolve().parent
NATIVE_SHA = '7a1ba8be4d450fc24c886aae475c9d29b53688c0ce06578a69ed140ff8b151e4'
UNION = (0, 13, 26, 39, 52, 65, 78, 85, 96, 102, 112, 119, 121, 125)
TRIVIAL = tuple(min(125, 13*k) for k in range(14))


def catalogue(path=HERE/'catalog.txt'):
    raw = path.read_bytes()
    assert sha256(raw).hexdigest() == NATIVE_SHA
    data = defaultdict(dict)
    for line in raw.splitlines():
        size, embedded, cost, difference = map(int, line.split())
        assert embedded in (0, 1) and 1 <= size <= 13 and cost not in data[size, embedded]
        data[size, embedded][cost] = difference
    assert data[1, 1] == {0: 0} and (1, 0) not in data and (13, 0) not in data
    assert data[12, 1] == {1104: 0, 1116: 0}
    return data


@lru_cache(None)
def partitions(total, count, smallest=1):
    if not count:
        return ((),) if not total else ()
    return tuple((s,)+tail for s in range(smallest, min(13, total//count)+1)
                 for tail in partitions(total-s, count-1, s))


def make_rows(cap, minima):
    result = []
    for sizes in partitions(125, 12):
        if sum(min(minima.get((s, 0), 100000), minima.get((s, 1), 100000)) for s in sizes) > cap:
            continue
        levels = sorted(set(sizes))
        multiplicities = [sizes.count(s) for s in levels]
        choices = [range(n+1) if (s, 0) in minima else (0,) for s, n in zip(levels, multiplicities)]
        for proper_counts in product(*choices):
            proper = tuple(s for s, n in zip(levels, proper_counts) for _ in range(n))
            embedded = tuple(s for s, n, p in zip(levels, multiplicities, proper_counts) for _ in range(n-p))
            floor = sum(minima[s, 0] for s in proper)+sum(minima[s, 1] for s in embedded)
            if floor > cap:
                continue
            k = len(embedded)
            assert len(proper)+k == 12 and sum(proper)+sum(embedded) == 125
            union_pass = all(sum(embedded[-j:]) <= UNION[j] for j in range(1, k+1))
            trivial_pass = all(sum(embedded[-j:]) <= TRIVIAL[j] for j in range(1, k+1))
            result.append({'proper_sizes': proper, 'embedded_sizes': embedded,
                           'embedded_count': k, 'large_embedded_count': sum(s >= 11 for s in embedded),
                           'minimum_embedded_cost': sum(minima[s, 1] for s in embedded),
                           'minimum_total_cost': floor,
                           'unrestricted_union_bound_passes': union_pass,
                           'trivial_union_bound_passes': trivial_pass,
                           'all_parents_for_embedded_classes_must_be_distinct': k < 2 or embedded[0]+embedded[1] > 13,
                           'old_union_enumerator_cannot_stop_before_k': sum(embedded) > 13*(k-1),
                           'outside_condition_inherited_union': bool(proper) and min(proper) > UNION[k]-sum(embedded),
                           'outside_condition_trivial_union': bool(proper) and min(proper) > TRIVIAL[k]-sum(embedded)})
    return sorted(result, key=lambda r: (r['embedded_count'], r['minimum_total_cost'], r['proper_sizes'], r['embedded_sizes']))


def minimum_by_number(minima, large_only=False):
    """Independent ordered min-plus DP; used only for minima, so order is harmless."""
    types = tuple((s, int(bool(e) and (not large_only or s >= 11)), c) for (s, e), c in minima.items())
    state = {(0, 0): 0}
    for count in range(1, 13):
        following = {}
        for (points, embedded), old in state.items():
            for s, e, c in types:
                total = points+s
                if total+(12-count) > 125 or total+13*(12-count) < 125:
                    continue
                key = total, embedded+e
                following[key] = min(following.get(key, 10**9), old+c)
        state = following
    return {e: state.get((125, e)) for e in range(13)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--budget', type=int, default=9995)
    parser.add_argument('--output', type=Path, default=HERE/'plan_9995.json')
    args = parser.parse_args()
    data = catalogue(); minima = {key: min(costs) for key, costs in data.items()}
    rows = make_rows(args.budget, minima)
    minima_E = minimum_by_number(minima)
    minima_large = minimum_by_number(minima, True)
    assert minima_E[0] == minima_large[0] == 10192
    assert minima_E[1] == minima_large[1] == 9980
    stats = {}
    for k in range(13):
        group = [r for r in rows if r['embedded_count'] == k]
        if group:
            assert min(r['minimum_total_cost'] for r in group) == minima_E[k]
            stats[k] = {'profiles': len(group), 'minimum_cost': minima_E[k],
                        'min_embedded_points': min(sum(r['embedded_sizes']) for r in group),
                        'max_embedded_points': max(sum(r['embedded_sizes']) for r in group),
                        'unrestricted_union_rejections': sum(not r['unrestricted_union_bound_passes'] for r in group),
                        'trivial_union_rejections': sum(not r['trivial_union_bound_passes'] for r in group),
                        'outside_failures_inherited_union': sum(not r['outside_condition_inherited_union'] for r in group),
                        'outside_failures_trivial_union': sum(not r['outside_condition_trivial_union'] for r in group),
                        'possible_shared_parent_profiles': sum(not r['all_parents_for_embedded_classes_must_be_distinct'] for r in group),
                        'old_union_early_stop_risk_profiles': sum(not r['old_union_enumerator_cannot_stop_before_k'] for r in group)}
    if args.budget == 9995:
        assert len(rows) == 2194
        assert [stats[k]['profiles'] for k in range(1, 11)] == [1, 14, 57, 164, 336, 491, 542, 396, 170, 23]
        assert all(r['outside_condition_inherited_union'] for r in rows if r['embedded_count'] in (1, 2, 3, 4, 9, 10))
        assert all(r['all_parents_for_embedded_classes_must_be_distinct'] for r in rows)
    # A separate plan at 10006 establishes exactly what the E=1 short proof
    # has to cover. Large-E=1 additionally allows one embedded ten-point class.
    expanded = make_rows(10006, minima)
    one_E = [r for r in expanded if r['embedded_count'] == 1]
    one_large = [r for r in expanded if r['large_embedded_count'] == 1]
    assert len(one_E) == 1
    assert one_E[0]['embedded_sizes'] == (13,)
    assert one_E[0]['proper_sizes'] == (10,)*10+(12,)
    assert len(one_large) == 2
    assert {(r['embedded_sizes'], r['proper_sizes'], r['minimum_total_cost']) for r in one_large} == {
        ((13,), (10,)*10+(12,), 9980), ((10, 13), (10,)*9+(12,), 10004)}
    result = {'schema': 'TWELVE_LABEL_FULL_EMBEDDING_SIZE_PLAN_V1', 'budget': args.budget,
              'native_catalog_sha256': NATIVE_SHA, 'native_catalog_rows': sum(map(len, data.values())),
              'all_size_partitions': len(partitions(125, 12)),
              'class_minima': [{'size': s, 'embedded': e, 'minimum_cost': c} for (s, e), c in sorted(minima.items())],
              'unrestricted_mother_union_bounds': UNION, 'trivial_mother_union_bounds': TRIVIAL,
              'union_bound_source': 'The predecessor mothers/replay.py curve loop searches the full 250-mother family at thresholds U(k)+1 for k=7..12; it has no label-count assumption. No eleven-label proper-count exclusion is imported.',
              'minimum_cost_by_all_embedded_count': minima_E,
              'minimum_cost_by_large_embedded_count': minima_large,
              'by_embedded_count': stats, 'profiles': rows,
              'budget10006_single_all_embedded_profiles': one_E,
              'budget10006_single_large_embedded_profiles': one_large,
              'review_status': 'NOT_REVIEWED',
              'scope': 'Complete necessary size/embedding configurations from exact single-class minima, not existence of geometrically compatible partitions. Outside-condition failures are unhandled configurations, not exclusions.'}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in ['budget', 'all_size_partitions', 'minimum_cost_by_all_embedded_count', 'minimum_cost_by_large_embedded_count', 'by_embedded_count']}, indent=2))


if __name__ == '__main__':
    main()
