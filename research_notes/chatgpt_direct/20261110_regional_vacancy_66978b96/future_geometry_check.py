"""Exact integer checks for empty-prefix certificates and deletion lifetime.

This checker knows static residue sets. Actual BRC request observations are
executed by the separate production experiment.
"""
from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path


def mask(values):
    out = 0
    for value in values:
        out |= 1 << value
    return out


def capacity(start, colors, depth, prefix):
    delta = 1 << depth
    first = (prefix - start) % delta
    return 0 if first >= colors else 1 + (colors - 1 - first) // delta


def check():
    counts = dict(capacity_cells=0, phase_minima=0,
                  universal_internal_prefixes=0, sibling_partitions=0,
                  opposite_child_repairs=0, deletion_subsets=0,
                  lifetime_guarantees=0, sharp_deletion_witnesses=0,
                  antipodal_domains=0)
    ranges = dict(capacities_and_partitions_r=[1, 63],
                  all_prefix_deletion_subsets_r=[1, 15],
                  actual_target_phases='0 <= t < B/gcd(M,B)',
                  depths='0 <= ell <= b; every legal prefix')
    sharp_examples = []
    for r in range(1, 64):
        colors = r + 1
        width = r.bit_length()
        modulus = 1 << width
        period = modulus // gcd(colors, modulus)
        targets = [mask((1 + t * colors + c) % modulus
                        for c in range(colors)) for t in range(period)]
        prefixes = {(depth, prefix): mask(range(prefix, modulus, 1 << depth))
                    for depth in range(width + 1)
                    for prefix in range(1 << depth)}
        for (depth, prefix), points in prefixes.items():
            delta = 1 << depth
            actual = [(points & target).bit_count() for target in targets]
            for t, actual_size in enumerate(actual):
                assert actual_size == capacity(1 + t * colors, colors, depth, prefix)
                counts['capacity_cells'] += 1
            mu = min(actual)
            assert mu == colors // delta
            counts['phase_minima'] += 1
            if depth < width:
                assert all(actual)
                counts['universal_internal_prefixes'] += 1
            for x in range(prefix, modulus, delta):
                union = 0
                for j in range(depth, width):
                    sibling_prefix = x % (1 << j) + (1 - ((x >> j) & 1)) * (1 << j)
                    sibling = prefixes[j + 1, sibling_prefix]
                    assert union & sibling == 0
                    union |= sibling
                assert union == points & ~(1 << x)
                counts['sibling_partitions'] += 1
                if depth < width:
                    child_prefix = prefix + (1 - ((x >> depth) & 1)) * delta
                    child = prefixes[depth + 1, child_prefix]
                    assert child & (1 << x) == 0
                    assert child & ~points == 0
                    assert child.bit_count() * 2 == points.bit_count()
                    counts['opposite_child_repairs'] += 1
            if r > 15:
                continue
            first_failure_size = points.bit_count() + 1
            deleted = points
            while True:
                remaining = points & ~deleted
                covered = all(remaining & target for target in targets)
                d = deleted.bit_count()
                if d < mu:
                    assert covered
                    counts['lifetime_guarantees'] += 1
                if not covered:
                    first_failure_size = min(first_failure_size, d)
                counts['deletion_subsets'] += 1
                if depth == 0:
                    half = modulus // 2
                    low = deleted & ((1 << half) - 1)
                    high = deleted >> half
                    empty_pair_exists = (low | high) != (1 << half) - 1
                    internal_empty_exists = any(
                        prefixes[width - 1, p] & deleted == 0
                        for p in range(half))
                    assert empty_pair_exists == internal_empty_exists
                    if d < half:
                        assert empty_pair_exists
                    counts['antipodal_domains'] += 1
                if deleted == 0:
                    break
                deleted = (deleted - 1) & points
            assert first_failure_size == mu
            t0 = actual.index(mu)
            sharp_deleted = points & targets[t0]
            assert sharp_deleted.bit_count() == mu
            assert (points & ~sharp_deleted) & targets[t0] == 0
            counts['sharp_deletion_witnesses'] += 1
            if depth == 1 and prefix == 1 and r in (4, 6, 8, 14):
                sharp_examples.append(dict(r=r, M=colors, B=modulus,
                                           depth=depth, prefix=prefix,
                                           minimum_capacity=mu,
                                           target_phase=t0,
                                           deleted=[x for x in range(modulus)
                                                    if sharp_deleted >> x & 1]))

    # An arbitrary first safe point need not have a safe universal partner.
    r, colors, modulus = 8, 9, 16
    occupied = {7, 8, 9}
    safe = set(range(modulus)) - occupied
    target_sets = [{(1 + t * colors + c) % modulus for c in range(colors)}
                   for t in range(modulus)]
    partners = [x for x in range(1, modulus)
                if all({0, x} & target for target in target_sets)]
    assert partners == [7, 8, 9]
    assert not any(x in safe for x in partners)
    assert all({1, 10} & target for target in target_sets)
    # A finite target intersection can have two separate components.
    intersection = set(range(5)) & {4, 5, 6, 7, 0}
    assert intersection == {0, 4}
    return dict(status='PASS', model='exact finite integer control',
                actual_request_table_read=False, ranges=ranges,
                counts=counts, sharp_examples=sharp_examples,
                first_point_counterexample=dict(r=8, M=9, B=16,
                                                occupied=sorted(occupied),
                                                first_point=0,
                                                all_universal_partners=partners,
                                                alternate_safe_pair=[1, 10]),
                disconnected_intersection=dict(r=4, M=5, B=8,
                                               starts=[0, 4], intersection=[0, 4]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('future_geometry_checks.json'))
    args = parser.parse_args()
    result = check()
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))
