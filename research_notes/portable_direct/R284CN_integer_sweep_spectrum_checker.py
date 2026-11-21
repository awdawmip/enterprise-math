#!/usr/bin/env python3
"""R284CN. Exact integer-interval sweep for all finite Port k-fold radii.

Frozen input is the R284CL Port observer. No external dependencies.
"""
from bisect import bisect_left
from collections import defaultdict
import argparse
import json
import time
from R284CL_finite_codeword_support_checker import (
    P, D, Z, SELECT, FROZEN_SHA, arc_data, generate_codewords,
    distance_point_arc,
)


def coverage_events(arcs, radius):
    """Difference array for integer Port observations in [0,P-1]."""
    events = defaultdict(int)
    events[0] += 0
    events[P] += 0
    always = 0
    for a, width in arcs:
        if width + 2 * radius >= P - 1:
            always += 1
            continue
        left = (a - radius) % P
        right = (a + width + radius) % P
        if left <= right:
            events[left] += 1
            events[right + 1] -= 1
        else:
            events[0] += 1
            events[right + 1] -= 1
            events[left] += 1
            events[P] -= 1
    return always, sorted(events.items())


def minimum_population_coverage(arcs, sites, radius):
    always, events = coverage_events(arcs, radius)
    active = always
    least = len(arcs)
    witness = None
    for (left, delta), (right, _) in zip(events, events[1:]):
        active += delta
        pos = bisect_left(sites, left)
        if pos < len(sites) and sites[pos] < right and active < least:
            least, witness = active, sites[pos]
    return least, witness


def uncovered_integer_runs(arcs, radius, level):
    always, events = coverage_events(arcs, radius)
    active = always
    bad = []
    for (left, delta), (right, _) in zip(events, events[1:]):
        active += delta
        if active < level and right > left:
            bad.append([left, right - 1, active])
    return bad


def full_baseline(words, arcs):
    maximum = [-1] * len(arcs)
    for x in words:
        distances = sorted(distance_point_arc(x, a, width) for a, width in arcs)
        for i, d in enumerate(distances):
            if d > maximum[i]:
                maximum[i] = d
    return maximum


def compute(full=False):
    start = time.perf_counter()
    arcs = arc_data()
    words = [record[0] for record in generate_codewords()]
    sites = sorted(words)
    assert len(arcs) == 64 and len(sites) == len(set(sites)) == 65536
    prepared = time.perf_counter() - start
    observations = {}
    def guaranteed(radius):
        if radius not in observations:
            observations[radius] = minimum_population_coverage(arcs, sites, radius)[0]
        return observations[radius]
    t = time.perf_counter()
    thresholds = []
    for level in range(1, 65):
        low, high = -1, (P - 1) // 2
        while high - low > 1:
            mid = (low + high) // 2
            if guaranteed(mid) >= level:
                high = mid
            else:
                low = mid
        thresholds.append(high)
    fast_seconds = time.perf_counter() - t
    for level, radius in enumerate(thresholds, 1):
        assert guaranteed(radius) >= level
        if radius:
            assert guaranteed(radius-1) < level
    apex = 6683583465
    k = 54
    r = thresholds[k-1]
    assert r == 7642302204
    assert uncovered_integer_runs(arcs, r, k) == [[apex-392, apex+392, 53]]
    assert uncovered_integer_runs(arcs, r-1, k) == [[apex-393, apex+393, 53]]
    left_index = bisect_left(sites, apex)
    left, right = sites[left_index-1], sites[left_index]
    assert (left, right) == (6683583072, 6683702379)
    assert not any(left < x < apex+393 for x in sites)
    assert distance_point_arc(left, *arcs[0]) >= 0
    baseline_seconds = None
    if full:
        t = time.perf_counter()
        brute = full_baseline(words, arcs)
        baseline_seconds = time.perf_counter() - t
        assert brute == thresholds
    return {
        'schema': 'R284CN_INTEGER_SWEEP_SPECTRUM_V1',
        'status': 'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
        'input': {'P': P, 'D': D, 'Z': Z, 'SELECT': SELECT,
                  'frozen_codewords_sha256': FROZEN_SHA,
                  'codeword_count': len(sites), 'arc_count': len(arcs)},
        'algorithm': {'radius_domain': 'nonnegative integers',
                      'event_convention': 'closed integer interval, decrement at right+1',
                      'distinct_sweep_queries': len(observations),
                      'bisect_levels': 64,
                      'pairwise_arc_crossings_needed': 0,
                      'distance_evaluations_for_sweep': 0},
        'all_64_exact_U': thresholds,
        'k54': {'U54': r, 'continuous_maximum': 7642302597,
                'continuous_peak_port': apex, 'gap_double_radius': 786,
                'bad_integer_ports_at_U54': uncovered_integer_runs(arcs, r, k),
                'bad_integer_ports_at_U54_minus_1': uncovered_integer_runs(arcs, r-1, k),
                'preceding_word': left, 'following_word': right,
                'U54_lower_bound_witness_port': left},
        'validation': {'baseline_65536_times_64_equal': full,
                       'all_threshold_boundary_checks': True,
                       'frozen_sha_verified': True,
                       'runtime_seconds_single_host_observation': {
                           'source_generation_and_sort': round(prepared, 6),
                           'sweep_and_bisection': round(fast_seconds, 6),
                           'brute_baseline_if_requested': round(baseline_seconds, 6) if full else None},
                       'independent_review': 'NOT_REVIEWED'}
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--full', action='store_true', help='also recompute exhaustive 4,194,304 distances')
    parser.add_argument('--output', default='R284CN_integer_sweep_spectrum_certificate.json')
    args = parser.parse_args()
    result = compute(args.full)
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(json.dumps({'sweeps': result['algorithm']['distinct_sweep_queries'],
                      'U54': result['k54']['U54'],
                      'U64': result['all_64_exact_U'][-1],
                      'baseline_equal': result['validation']['baseline_65536_times_64_equal'],
                      'times': result['validation']['runtime_seconds_single_host_observation']}, indent=2))
