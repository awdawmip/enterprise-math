"""Verify the joint moment lemma and a finite-search pruning comparison.

The prior complete class census supplies completeness of the three size/cost
families. This verifier checks the moments of every supplied family member and
recomputes legality/cost of every orbit representative from the original menu.
"""
import argparse
import json
import struct
from collections import Counter, defaultdict
from itertools import product
from pathlib import Path

POINTS = tuple(product(range(5), repeat=3))
PAIRS = ((0, 1), (0, 2), (1, 2))
STEPS = {tuple((value if i == axis else 0) % 5 for i in range(3))
         for axis in range(3) for value in (-1, 1)}


def points(mask):
    return [POINTS[i] for i in range(125) if mask >> i & 1]


def moments(mask):
    values = points(mask)
    first = tuple(sum(v[i] for v in values) % 5 for i in range(3))
    cross = tuple(sum(v[i] * v[j] for v in values) % 5 for i, j in PAIRS)
    return first, cross


def native_class_cost(mask):
    values = points(mask)
    cost = 0
    for step, start in product((1, 3), POINTS):
        fibers = defaultdict(list)
        for value in values:
            active = tuple(j for j in range(3) if (value[j] - start[j]) % 5 in (0, step))
            fibers[active].append(tuple(value[j] for j in active))
        for targets in fibers.values():
            assert len(set(targets)) <= 2
            if len(set(targets)) == 2:
                cost += len(targets)
    return cost


def reachable_sets():
    result = [{(0, 0, 0)}]
    for _ in range(12):
        result.append({tuple((x+y) % 5 for x, y in zip(a, b))
                       for a in result[-1] for b in STEPS})
    for length, states in enumerate(result):
        for q in POINTS:
            distances = [min(v, 5-v) for v in q]
            least = sum(distances)
            odd_extra = min(5-2*d for d in distances)
            criterion = length >= least and (
                (length-least) % 2 == 0 or length >= least + odd_extra)
            assert criterion == (q in states)
    return result


def verify(bank, benchmark, tail_file, output):
    families = {(10, 744): [], (10, 768): [], (11, 936): []}
    reps = defaultdict(list)
    menu_checked = []
    for lo, hi, cost, size in struct.iter_unpack('<QQII', bank.read_bytes()):
        key = (size % 256, cost)
        if size >= 256:
            mask = lo + (hi << 64)
            assert native_class_cost(mask) == cost
            menu_checked.append({'size': size % 256, 'cost': cost,
                                 'points': [i for i in range(125) if mask >> i & 1]})
        if key in families:
            mask = lo + (hi << 64)
            families[key].append(mask)
            if size >= 256:
                reps[key].append(mask)
    assert {key: len(rows) for key, rows in families.items()} == {
        (10, 744): 12000, (10, 768): 1500, (11, 936): 4500}
    summaries = []
    for key, rows in sorted(families.items()):
        observed = Counter()
        for mask in rows:
            first, cross = moments(mask)
            if key[0] == 10:
                assert first == (0, 0, 0)
                signature = cross
                if key == (10, 744):
                    values = points(mask)
                    assert all(sum(v[j] == a for v in values) == 2
                               for j in range(3) for a in range(5))
            else:
                signature = tuple((cross[k] - first[i] * first[j]) % 5
                                  for k, (i, j) in enumerate(PAIRS))
            assert signature in STEPS
            observed[signature] += 1
        rep_points = []
        for mask in reps[key]:
            assert native_class_cost(mask) == key[1]
            rep_points.append([i for i in range(125) if mask >> i & 1])
        summaries.append({'size': key[0], 'cost': key[1], 'class_count': len(rows),
                          'orbit_representatives': rep_points,
                          'signature_counts': [{'signature': list(q), 'count': n}
                                               for q, n in sorted(observed.items())]})
    reaches = reachable_sets()
    before = list(map(int, (benchmark / 'moment_baseline.log').read_text().split()))
    after = list(map(int, (benchmark / 'moment_enhanced.log').read_text().split()))
    assert len(before) == 5 and len(after) == 7
    assert before[:3] == after[:3] and before[4] == after[4] == 0
    rejects = []
    for line in (benchmark / 'moment_enhanced.stderr').read_text().splitlines():
        if not line.startswith('MIXED_REJECT '):
            continue
        lo, hi, ten, eleven, index = map(int, line.split()[1:])
        mask = lo + (hi << 64)
        assert mask.bit_count() == 10 * ten + 11 * eleven
        first, cross = moments(mask)
        q = tuple((cross[k] - eleven * first[i] * first[j]) % 5
                  for k, (i, j) in enumerate(PAIRS))
        assert index == 25*q[0] + 5*q[1] + q[2]
        assert q not in reaches[ten+eleven] or (not eleven and first != (0,0,0))
        rejects.append({'free_history_ids': [i for i in range(125) if mask >> i & 1],
                        'ten_classes': ten, 'eleven_classes': eleven,
                        'first_moment': list(first), 'corrected_cross_moment': list(q)})
    result = {'families': summaries,
              'native_menu_representatives_checked': menu_checked,
              'step_set': [list(q) for q in sorted(STEPS)],
              'reachable_counts': [len(s) for s in reaches],
              'reachable_closed_form_checked_for_lengths': list(range(13)),
              'comparison': {'cost': before[0], 'geometric_nodes': before[1],
                             'leaf_nodes': before[2], 'baseline_nodes': before[3],
                             'moment_nodes': after[3], 'both_found': 0,
                             'moment_tests': after[5], 'moment_rejections': after[6],
                             'nodes_saved': before[3]-after[3]},
              'rejection_examples': rejects}
    tail = json.loads(tail_file.read_text())
    ids = tail['free_history_ids']
    mask = sum(1 << i for i in ids)
    first, cross = moments(mask)
    assert len(ids) == 30 and first == cross == (0, 0, 0)
    assert all(sum(POINTS[i][j] == a for i in ids) == 6
               for j in range(3) for a in range(5))
    candidates = [m for m in families[10, 744] if m & mask == m]
    assert len(candidates) == tail['candidate_classes'] == 50
    assert (0, 0, 0) not in reaches[3]
    baseline_tail = list(map(int, (benchmark / 'tail_baseline.log').read_text().split()))
    enhanced_tail = list(map(int, (benchmark / 'tail_enhanced.log').read_text().split()))
    assert baseline_tail[:3] == [3, 50, 1] and baseline_tail[4:] == [0, 0, 0]
    assert enhanced_tail == [3, 50, 1, 1, 0, 1, 1]
    result['thirty_history_obstruction'] = dict(
        tail, coordinate_fiber_sizes=[6] * 15, first_moment=list(first),
        cross_moment=list(cross), baseline_nodes=baseline_tail[3], moment_nodes=1,
        coordinate_margin_check_passed=True, integer_cover_exists=False)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result['comparison'], sort_keys=True))


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--bank', type=Path, required=True)
    p.add_argument('--benchmark', type=Path, required=True)
    p.add_argument('--tail', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    verify(a.bank, a.benchmark, a.tail, a.output)
