"""Native finite-census proof of the universal 9/10 marginal cost bound.

The quick mode verifies every packaged seed against the original menus and
checks the exact complete-census projection certificates. --full regenerates
the original complete census (with only its size-12 output ceiling extended
from 1230 to 1244) and the complete embedded/proper cost catalogue. Existing
full census output can instead be supplied through --extended-seeds or --seeds.
"""
import argparse
from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, permutations, product
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
POINTS = tuple(product(range(5), repeat=3))
FULL = (1 << 125)-1
BASE = {9: 557, 10: 744}
CUTOFF = {s: c+9*(s-2) for s, c in BASE.items()}
ORIGINAL_CEILINGS = {8: 550, 9: 740, 10: 880, 11: 1090, 12: 1230, 13: 1350}


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def point_ids(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length()-1
        mask -= bit


def mask_of(ids):
    return sum(1 << i for i in ids)


def orbit(ids):
    oriented = {tuple(sorted(25*(POINTS[x][perm[0]]*sign[0]*scale % 5)
                             +5*(POINTS[x][perm[1]]*sign[1]*scale % 5)
                             +POINTS[x][perm[2]]*sign[2]*scale % 5 for x in ids))
                for perm in permutations(range(3))
                for sign in product((1, -1), repeat=3) for scale in (1, 2)}
    return {mask_of(25*((POINTS[x][0]+a) % 5)+5*((POINTS[x][1]+b) % 5)
                    +(POINTS[x][2]+c) % 5 for x in row)
            for row in oriented for a, b, c in POINTS}


def hist(mask):
    result = [0]*15
    for p in point_ids(mask):
        for axis, value in enumerate(POINTS[p]):
            result[5*axis+value] += 1
    return tuple(result)


def delta(histogram, k=1):
    return sum(max(h-2*k, 0) for h in histogram)


def seed_rows(path):
    for line in path.read_text().splitlines():
        size, cost, *ids = map(int, line.split())
        assert len(ids) == len(set(ids)) == size
        assert ids == sorted(ids) and ids[0] == 0 and all(0 <= i < 125 for i in ids)
        yield size, cost, ids


def check_original_seeds(path, bindings):
    assert digest(path) == bindings['original_full_seeds']['sha256']
    selected = []
    count = 0
    with path.open('rb') as stream:
        for line in stream:
            count += 1
            size, cost = map(int, line.split()[:2])
            if size in CUTOFF and cost <= CUTOFF[size]:
                selected.append(line)
    assert count == bindings['original_full_seeds']['rows']
    assert b''.join(selected) == (HERE/'low_cost_seeds.txt').read_bytes()
    return count


def check_extended_seeds(path, bindings):
    original = sha256()
    original_count = 0
    small = []
    large = []
    with path.open('rb') as stream:
        for line in stream:
            size, cost = map(int, line.split()[:2])
            if cost <= ORIGINAL_CEILINGS[size]:
                original.update(line)
                original_count += 1
            if size in CUTOFF and cost <= CUTOFF[size]:
                small.append(line)
            if size in (12, 13):
                large.append(line)
    assert original.hexdigest() == bindings['original_full_seeds']['sha256']
    assert original_count == bindings['original_full_seeds']['rows']
    assert b''.join(small) == (HERE/'low_cost_seeds.txt').read_bytes()
    assert b''.join(large) == (HERE/'large_class_seeds.txt').read_bytes()
    assert digest(path) == bindings['extended_full_seeds']['sha256']
    return original_count


@lru_cache(None)
def ordered_parts(total, count, allowed, smallest=1):
    if count == 0:
        return ((),) if total == 0 else ()
    if total < count*smallest or total > count*max(allowed):
        return ()
    return tuple((s,)+tail for s in allowed if smallest <= s <= total//count
                 for tail in ordered_parts(total-s, count-1, allowed, s))


def embedding_profiles(catalogue, embedded_count, cap):
    minima = {}
    for size, embedded, cost, _difference in catalogue:
        key = size, embedded
        minima[key] = min(minima.get(key, 10**9), cost)
    e_sizes = tuple(sorted(s for s, e in minima if e))
    p_sizes = tuple(sorted(s for s, e in minima if not e))
    proper_count = 12-embedded_count
    result = []
    for e_total in range(0, 13*embedded_count+1):
        for embedded in ordered_parts(e_total, embedded_count, e_sizes):
            e_cost = sum(minima[s, 1] for s in embedded)
            for proper in ordered_parts(125-e_total, proper_count, p_sizes):
                cost = e_cost+sum(minima[s, 0] for s in proper)
                if cost <= cap:
                    result.append({'embedded_sizes': list(embedded), 'proper_sizes': list(proper),
                                   'minimum_total_cost': cost})
    return sorted(result, key=lambda row: (row['minimum_total_cost'], row['proper_sizes'], row['embedded_sizes']))


def verify(args, bindings, census_rerun, catalogue_rerun):
    native = load_module('marginal_native', args.previous/'fractional/proof/verify.py')
    bad, pair = native.observation_tables()
    counts = Counter()
    least_slack = {9: 10**9, 10: 10**9}
    by_price = defaultdict(lambda: {'rows': 0, 'maximum_delta': 0, 'minimum_slack': 10**9})
    for size, cost, ids in seed_rows(HERE/'low_cost_seeds.txt'):
        assert size in BASE and cost <= CUTOFF[size]
        mask = mask_of(ids)
        assert native.native_class(mask, bad, pair) == (size, cost)
        d = delta(hist(mask))
        assert d <= 3*(size-2)
        slack = cost-BASE[size]-3*d
        assert slack >= 0, (size, cost, ids, d)
        least_slack[size] = min(least_slack[size], slack)
        counts[size] += 1
        row = by_price[size, cost]
        row['rows'] += 1
        row['maximum_delta'] = max(row['maximum_delta'], d)
        row['minimum_slack'] = min(row['minimum_slack'], slack)
    assert counts == {9: 14344, 10: 5327}
    assert least_slack == {9: 0, 10: 0}

    representatives = json.loads((HERE/'representatives.json').read_text())
    mothers = orbit(representatives['mother13']['points'])
    proper12 = orbit(representatives['proper12_1244']['points'])
    assert len(mothers) == 250 and len(proper12) == 3000
    hists = {}
    centres = {}
    for mother in mothers:
        assert native.native_class(mother, bad, pair) == (13, 1296)
        h = hists[mother] = hist(mother)
        assert all(sorted(h[5*j:5*j+5]) == [2, 2, 2, 2, 5] for j in range(3))
        centre = tuple(h[5*j:5*j+5].index(5) for j in range(3))
        centres[mother] = centre
        assert mother >> (25*centre[0]+5*centre[1]+centre[2]) & 1
    embedded12 = {}
    embedded_cost_counts = Counter()
    for mother in mothers:
        centre = centres[mother]
        centre_id = 25*centre[0]+5*centre[1]+centre[2]
        for p in point_ids(mother):
            mask = mother ^ (1 << p)
            cost = 1104 if p == centre_id else 1116
            assert mask not in embedded12  # A twelve-point class has a unique mother.
            assert native.native_class(mask, bad, pair) == (12, cost)
            embedded12[mask] = (mother, cost)
            embedded_cost_counts[cost] += 1
            hists[mask] = hist(mask)
            if cost == 1104:
                assert all(sorted(hists[mask][5*j:5*j+5]) == [2, 2, 2, 2, 4] for j in range(3))
    assert embedded_cost_counts == {1104: 250, 1116: 3000}
    peaks = {}
    for mask in proper12:
        assert native.native_class(mask, bad, pair) == (12, 1244)
        assert not any(mask & ~mother == 0 for mother in mothers)
        h = hists[mask] = hist(mask)
        assert all(sorted(h[5*j:5*j+5]) == [2, 2, 2, 2, 4] for j in range(3))
        peaks[mask] = tuple(h[5*j:5*j+5].index(4) for j in range(3))
    families = {(13, 1296): mothers, (12, 1244): proper12,
                (12, 1104): {m for m, (_, c) in embedded12.items() if c == 1104},
                (12, 1116): {m for m, (_, c) in embedded12.items() if c == 1116}}
    large_seed_counts = Counter()
    large_seed_representatives = {}
    for size, cost, ids in seed_rows(HERE/'large_class_seeds.txt'):
        mask = mask_of(ids)
        assert (size, cost) in families and mask in families[size, cost]
        large_seed_counts[size, cost] += 1
        large_seed_representatives.setdefault((size, cost), ids)
    assert set(large_seed_counts) == set(families)
    for key, ids in large_seed_representatives.items():
        assert orbit(ids) == families[key]

    # These exhaustive pair checks corroborate the short per-axis proof.
    # For embedded12, the full parents themselves may intersect; only the
    # actual selected mother13 and selected twelve-point class must be disjoint.
    pair_stats = {'two_full13': Counter(), 'full13_embedded12': Counter(),
                  'full13_proper12': Counter()}
    intersecting_parent_pairs = 0
    for first, second in combinations(sorted(mothers), 2):
        if first & second:
            continue
        s = sum(a == b for a, b in zip(centres[first], centres[second]))
        residual = tuple(25-a-b for a, b in zip(hists[first], hists[second]))
        assert sum(residual) == 3*99
        assert delta(residual, 10) == 9+s
        assert 2*1296+557+9*744+3*(9+s) == 9872+3*s
        pair_stats['two_full13'][s] += 1
    for first in mothers:
        for second, (parent, cost) in embedded12.items():
            if first & second:
                continue
            s = sum(a == b for a, b in zip(centres[first], centres[parent]))
            residual = tuple(25-a-b for a, b in zip(hists[first], hists[second]))
            assert sum(residual) == 3*100
            assert delta(residual, 10) >= 9+s
            if cost == 1104:
                assert delta(residual, 10) == 9+s
            assert 1296+cost+10*744+3*(9+s) == 9867+(cost-1104)+3*s
            pair_stats['full13_embedded12'][cost, s, delta(residual, 10)] += 1
            intersecting_parent_pairs += bool(first & parent)
        for second in proper12:
            if first & second:
                continue
            s = sum(a == b for a, b in zip(centres[first], peaks[second]))
            residual = tuple(25-a-b for a, b in zip(hists[first], hists[second]))
            assert sum(residual) == 3*100
            assert delta(residual, 10) == 9+s
            assert 1296+1244+10*744+3*(9+s) == 10007+3*s
            pair_stats['full13_proper12'][s] += 1

    catalogue = [tuple(map(int, line.split())) for line in (HERE/'catalog.txt').read_text().splitlines()]
    e2 = embedding_profiles(catalogue, 2, 9995)
    assert e2 == json.loads((HERE/'two_embedded_profiles.json').read_text())
    assert len(e2) == 14
    assert [row['minimum_total_cost'] for row in e2[:3]] == [9840, 9845, 9912]
    assert e2[0]['embedded_sizes'] == [12, 13] and e2[0]['proper_sizes'] == [10]*10
    assert e2[1]['embedded_sizes'] == [13, 13] and e2[1]['proper_sizes'] == [9]+[10]*9
    assert not embedding_profiles(catalogue, 0, 10006)
    e1 = embedding_profiles(catalogue, 1, 10006)
    assert e1 == [{'embedded_sizes': [13], 'proper_sizes': [10]*10+[12], 'minimum_total_cost': 9980}]
    # In the E=1 budget, increasing the proper12 cost from 1244 to its next
    # complete-catalogue price 1376 already exceeds 10006.
    proper12_prices = sorted(c for n, e, c, _ in catalogue if n == 12 and e == 0)
    assert proper12_prices == [1244, 1376, 1484, 1560]
    assert 1296+proper12_prices[1]+10*744 > 10006

    result = {
        'schema': 'UNIVERSAL_MARGINAL_COST_BOUND_V1', 'all_checks_passed': True,
        'census_rerun': census_rerun, 'catalogue_rerun': catalogue_rerun,
        'full_seed_projection_checked': bool(args.full or args.seeds or args.extended_seeds),
        'extended_large_seed_projection_checked': bool(args.full or args.extended_seeds),
        'original_menu_choices': 250, 'forbidden_triples': 47000,
        'bases': BASE, 'finite_cost_cutoffs': CUTOFF,
        'small_native_seed_checks': dict(sorted(counts.items())),
        'small_native_seed_checks_total': sum(counts.values()),
        'minimum_integer_slack': least_slack,
        'large_classes_checked_natively': len(mothers)+len(embedded12)+len(proper12),
        'large_class_orbit_counts': [{'size': s, 'cost': c, 'classes': len(families[s, c]),
                                     'complete_normalized_seed_rows': large_seed_counts[s, c]}
                                    for s, c in sorted(families)],
        'class_cost_profiles': [{'size': s, 'cost': c, **row} for (s, c), row in sorted(by_price.items())],
        'pair_checks': {name: [{'parameters': key if isinstance(key, int) else list(key), 'pairs': n}
                               for key, n in sorted(stats.items())] for name, stats in pair_stats.items()},
        'embedded12_actual_disjoint_pairs_with_intersecting_parents': intersecting_parent_pairs,
        'universal_class_bounds': ['c9 >= 557 + 3 Delta1', 'c10 >= 744 + 3 Delta1'],
        'regional_bound': 'a nine-point and b ten-point classes covering U cost at least 557a+744b+3 Delta_(a+b)(U)',
        'conditional_two_full13_bound': '9872 + 3s; remaining classes are one nine-point and nine ten-point classes',
        'conditional_full13_embedded12_bound': '9867 + (c12-1104) + 3s; remaining classes are ten ten-point classes; actual classes disjoint, full parents need not be disjoint',
        'conditional_full13_proper12_1244_bound': '10007 + 3s; remaining classes are ten ten-point classes',
        'exact_two_embedded_profiles_below_9996': 14,
        'exact_two_embedded_global_lower_bound': 9867,
        'at_most_one_embedded_global_lower_bound': 10007,
        'structural_consequence': 'Every twelve-class table with total cost <=9866 has at least three classes contained in a thirteen-point mother; these need not all have size >=11.',
        'review_status': 'NOT_REVIEWED',
        'scope': 'Universal local inequalities and conditional/global embedding-count strata. This is not a whole-domain twelve-label lower bound of 9867.'}
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({key: result[key] for key in ['all_checks_passed', 'census_rerun', 'catalogue_rerun',
                                                'small_native_seed_checks_total', 'large_classes_checked_natively',
                                                'exact_two_embedded_global_lower_bound', 'at_most_one_embedded_global_lower_bound']}, sort_keys=True))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous', type=Path, required=True)
    parser.add_argument('--seeds', type=Path, help='Existing original complete census output, for projection equality')
    parser.add_argument('--extended-seeds', type=Path, help='Existing complete census with only the size12 output ceiling raised to1244')
    parser.add_argument('--full', action='store_true', help='Rebuild all native census and catalogue inputs in a fresh temporary directory')
    parser.add_argument('--output', type=Path, default=HERE/'verification.json')
    args = parser.parse_args()
    args.previous = args.previous.resolve()
    bindings = json.loads((HERE/'bindings.json').read_text())
    for row in bindings['source_bindings']:
        assert digest(args.previous/row['path']) == row['sha256'], row['path']
    for row in bindings['packaged_inputs']:
        assert digest(HERE/row['path']) == row['sha256'], row['path']
    if args.seeds:
        check_original_seeds(args.seeds, bindings)
    if args.extended_seeds:
        check_extended_seeds(args.extended_seeds, bindings)
    if args.full:
        with tempfile.TemporaryDirectory(prefix='marginal_bound_') as temporary:
            work = Path(temporary)
            original = args.previous/'previous/previous/previous/previous/previous/low/class_enumeration.cpp'
            text = original.read_text()
            old = '550,740,880,1090,1230,1350'
            new = '550,740,880,1090,1244,1350'
            assert text.count(old) == 1
            (work/'census.cpp').write_text(text.replace(old, new))
            assert digest(work/'census.cpp') == bindings['extended_census_source_sha256']
            bounds = load_module('marginal_prior_bounds', args.previous/'previous/previous/previous/previous/previous/previous/bounds/prior_bounds.py')
            bounds.observation_file(work/'obs')
            assert digest(work/'obs') == bindings['observation_sha256']
            subprocess.run(['c++', '-std=c++20', '-O3', '-mpopcnt', work/'census.cpp', '-o', work/'census'], check=True)
            with (work/'census.log').open('w') as log:
                subprocess.run([work/'census', work/'obs', work/'seeds'], stdout=log, check=True)
            assert digest(work/'census.log') == bindings['native_census_stdout_sha256']
            check_extended_seeds(work/'seeds', bindings)
            rep = json.loads((HERE/'representatives.json').read_text())['mother13']['points']
            mothers = orbit(rep)
            (work/'parents').write_text(''.join(f'{m % (1 << 64)} {m >> 64}\n' for m in sorted(mothers)))
            subprocess.run(['c++', '-std=c++20', '-O3', '-mpopcnt', args.previous/'previous/bias/menu.cpp', '-o', work/'menu'], check=True)
            with (work/'catalog.txt').open('w') as out, (work/'catalog.stderr').open('w') as err:
                subprocess.run([work/'menu', work/'obs', work/'parents'], stdout=out, stderr=err, check=True)
            assert (work/'catalog.txt').read_bytes() == (HERE/'catalog.txt').read_bytes()
    verify(args, bindings, args.full, args.full)


if __name__ == '__main__':
    main()
