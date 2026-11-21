#!/usr/bin/env python3
"""R284CQ: third-order Port spectrum and the unique minimum 186-site core.

Place beside R284CO_spectral_witness_checker.py and the immutable
R284CO / R284CP JSON certificates. Python standard library only.
"""
from bisect import bisect_left
from collections import defaultdict
import json
from R284CO_spectral_witness_checker import P, D, Z, SELECT, FROZEN_SHA, words, arcs, dist


def deficit(sites, circles, radius, k, collect=False):
    """Exact count and optional sites with kth arc-distance > radius."""
    events = defaultdict(int)
    events[0] += 0
    events[P] += 0
    fixed = 0
    for a, width in circles:
        if width + 2 * radius >= P - 1:
            fixed += 1
            continue
        lo, hi = (a - radius) % P, (a + width + radius) % P
        if lo <= hi:
            events[lo] += 1
            events[hi + 1] -= 1
        else:
            events[0] += 1
            events[hi + 1] -= 1
            events[lo] += 1
            events[P] -= 1
    coverage, count, found = fixed, 0, []
    ev = sorted(events.items())
    for (lo, delta), (hi, _) in zip(ev, ev[1:]):
        coverage += delta
        if coverage >= k or lo == hi:
            continue
        left, right = bisect_left(sites, lo), bisect_left(sites, hi)
        count += right - left
        if collect:
            found.extend(sites[left:right])
    return count, found


def compute():
    A = arcs()
    W = words()  # Exact frozen SHA256 checked by the parent generator.
    sites = sorted(W)
    assert len(A) == 64 and len(set(sites)) == len(sites) == 65536
    with open('R284CO_spectral_witness_certificate.json', encoding='utf-8') as f:
        co = json.load(f)
    with open('R284CP_127_sweep_witness_certificate.json', encoding='utf-8') as f:
        cp = json.load(f)
    assert co['pins']['frozen_sha256'] == FROZEN_SHA
    assert co['pins']['P'] == P and tuple(co['pins']['D']) == D
    assert tuple(co['pins']['Z']) == Z and tuple(co['pins']['SELECT']) == SELECT

    U = co['U_all_64']
    win = co['winner_residue_k2_to_k64']
    margins = co['strict_margin_k2_to_k64']
    runner = cp['unique_runner_up_residues_k2_to_k64']
    assert len(U) == 64 and len(win) == len(runner) == len(margins) == 63
    assert len(set(win)) == len(set(runner)) == 63
    assert len(set(win) & set(runner)) == 2
    assert deficit(sites, A, 0, 1)[0] == 0

    third_values, third_sites, gaps = [], [], []
    scans = 0
    for i in range(63):
        k, u, v = i + 2, U[i + 1], U[i + 1] - margins[i]
        w, s = win[i], runner[i]
        assert 0 < v < u and w != s
        assert sorted(dist(w, a) for a in A)[k - 1] == u
        assert sorted(dist(s, a) for a in A)[k - 1] == v
        cnt, xs = deficit(sites, A, v, k, True)
        scans += 1
        assert (cnt, xs) == (1, [w])
        cnt, xs = deficit(sites, A, v - 1, k, True)
        scans += 1
        assert cnt == 2 and set(xs) == {w, s}

        low, high = 0, v - 1
        while low < high:
            mid = (low + high) // 2
            cnt, _ = deficit(sites, A, mid, k)
            scans += 1
            if cnt <= 2:
                high = mid
            else:
                low = mid + 1
        t = low
        cnt, before = deficit(sites, A, t - 1, k, True)
        scans += 1
        assert cnt == 3 and len(set(before)) == 3 and {w, s}.issubset(before)
        z = next(x for x in before if x not in {w, s})
        assert sorted(dist(z, a) for a in A)[k - 1] == t
        cnt, after = deficit(sites, A, t, k, True)
        scans += 1
        assert cnt == 2 and set(after) == {w, s}
        third_values.append(t)
        third_sites.append(z)
        gaps.append(v - t)

    assert len(set(third_sites)) == 62
    assert set(third_sites).isdisjoint(set(win) | set(runner))
    assert third_sites[4] == third_sites[17]
    assert all(third_sites[i] != third_sites[j]
               for i in range(63) for j in range(i + 1, 63)
               if (i, j) != (4, 17))
    core = set(win) | set(runner) | set(third_sites)
    assert len(core) == 186
    rows = {x: sorted(dist(x, a) for a in A) for x in core}
    for i in range(63):
        top = sorted((row[i + 1] for row in rows.values()), reverse=True)
        assert top[:3] == [U[i + 1], U[i + 1] - margins[i], third_values[i]]

    return {
        'schema': 'R284CQ_THIRD_WITNESS_MINIMAL_186_PORT_CORE_V1',
        'status': 'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
        'pins': {'P': P, 'D': list(D), 'Z': list(Z),
                 'SELECT': list(SELECT), 'frozen_sha256': FROZEN_SHA},
        'sources': ['R284CO_spectral_witness_certificate.json',
                    'R284CP_127_sweep_witness_certificate.json'],
        'third_values_k2_to_k64': third_values,
        'third_witness_residues_k2_to_k64': third_sites,
        'third_witness_indices_k2_to_k64': [W.index(x) for x in third_sites],
        'second_to_third_gap_k2_to_k64': gaps,
        'counts': {
            'population': 65536, 'arcs': 64, 'third_witness_levels': 63,
            'unique_third_sites': 62, 'top_two_core_sites': 124,
            'minimum_top_three_core_sites': 186,
            'third_witness_total_radius_scans_including_two_prior_checks': scans,
            'exact_core_site_arc_distance_evaluations': 186 * 64,
        },
        'third_duplicate': {'ranks': [6, 19], 'residue': third_sites[4]},
        'third_sites_overlap_top_two_core': 0,
        'minimum_second_to_third_gap': min(gaps),
        'minimum_gap_rank': [i + 2 for i, g in enumerate(gaps) if g == min(gaps)],
        'verification': {
            'full_frozen_word_sha_recomputed': True,
            'each_Fk_at_third_eq_2': True,
            'each_Fk_below_third_eq_3': True,
            'third_direct_distance_checked': True,
            '186_site_core_recomputed': True,
            'independent_review': 'NOT_REVIEWED',
        },
    }


if __name__ == '__main__':
    record = compute()
    with open('R284CQ_third_spectrum_certificate.json', 'w', encoding='utf-8') as f:
        json.dump(record, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(json.dumps({'core': record['counts']['minimum_top_three_core_sites'],
                      'scans': record['counts']['third_witness_total_radius_scans_including_two_prior_checks'],
                      'min_gap': record['minimum_second_to_third_gap']}))
