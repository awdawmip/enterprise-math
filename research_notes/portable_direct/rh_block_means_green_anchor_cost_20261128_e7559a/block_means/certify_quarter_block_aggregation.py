#!/usr/bin/env python3
"""Aggregate the NEW saved square-root block means into quarter-scale means.

No sieve, prime logarithm, old road, or previous statistic is rerun.  Ordinary
interval subtraction is used after the common block averaging; this is safe
without assuming any cancellation of the already-stored radii.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode = True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--previous', type=Path, required=True)
    parser.add_argument('--block-certificate', type=Path,
                        default=Path(__file__).with_name('block_mean_certificate.json'))
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('quarter_block_certificate.json'))
    args = parser.parse_args()
    helpers = list(args.previous.rglob('certify_fast_harmonic_energy.py'))
    assert len(helpers) == 1
    helper = helpers[0]
    spec = importlib.util.spec_from_file_location('quarter_block_intervals', helper)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    original = json.loads(args.block_certificate.read_text())
    rows, total_means, total_lags, total_pairs = [], 0, 0, 0
    for old in original['ordinary_prime_statistics']['rows']:
        k, X = old['k'], old['X']
        r = 2**(3*k//4)
        M, ratio = X//r, r//old['r']
        assert r % old['r'] == 0 and M*ratio == old['M']
        means = []
        for i in range(M):
            selected = old['means'][i*ratio:(i+1)*ratio]
            lo = sum(int(z['value']['integer_bounds'][0]) for z in selected)
            hi = sum(int(z['value']['integer_bounds'][1]) for z in selected)
            value = lo//ratio, m.ceildiv(hi, ratio)
            means.append(value)
        entries = []
        for j in range(k-3*k//4):
            d = 2**j
            lo_sq, hi_sq, unresolved = 0, 0, 0
            for i in range(M-d):
                lo, hi = means[i+d][0]-means[i][1], means[i+d][1]-means[i][0]
                lo_sq += max(lo, 0)**2
                hi_sq += max(hi, 0)**2
                unresolved += int(lo < 0 < hi)
            denominator = X*d*m.S
            bounds = lo_sq//denominator, m.ceildiv(hi_sq, denominator)
            old_lag = next(v for v in old['lags'] if v['block_lag'] == ratio*d)
            inherited = tuple(map(int, old_lag['directed_over_Xd']['integer_bounds']))
            # Jensen across consecutive old blocks yields new C(d)<=old C(ratio*d).
            assert bounds[0] <= inherited[1]
            separated = bounds[1] <= inherited[0]
            if not separated:
                assert max(bounds[0], inherited[0]) <= min(bounds[1], inherited[1])
            entries.append({'block_lag': d, 'integer_lag': r*d, 'pairs': M-d,
                            'directed_over_Xd': m.record(bounds),
                            'sign_unresolved': unresolved,
                            'interval_upper_below_finer_lower': separated})
        intervals = [tuple(map(int, z['directed_over_Xd']['integer_bounds'])) for z in entries]
        bounds = max(z[0] for z in intervals), max(z[1] for z in intervals)
        winners = [entries[i]['block_lag'] for i, z in enumerate(intervals)
                   if all(z[0] > q[1] for j, q in enumerate(intervals) if i != j)]
        rows.append({'k': k, 'X': X, 'r': r, 'M': M,
                     'old_means_per_new_mean': ratio,
                     'means': [m.record(v) for v in means],
                     'C_plus': m.record(bounds),
                     'certified_unique_maximizing_block_lags': winners,
                     'lags': entries})
        total_means += M
        total_lags += len(entries)
        total_pairs += sum(v['pairs'] for v in entries)
    assert (len(rows), total_means, total_lags, total_pairs) == (14, 88, 32, 190)
    result = {'schema': 'EM_QUARTER_BLOCK_AGGREGATION_CERTIFICATE_V1',
              'date': '2026-11-28',
              'inputs': [
                  {'path': args.block_certificate.name,
                   'sha256': hashlib.sha256(args.block_certificate.read_bytes()).hexdigest()},
                  {'path_in_previous': str(helper.relative_to(args.previous)),
                   'sha256': hashlib.sha256(helper.read_bytes()).hexdigest()}],
              'windows': len(rows), 'block_means': total_means,
              'window_lag_groups': total_lags, 'directed_mean_pairs': total_pairs,
              'new_prime_log_calls': 0, 'new_sieve_calls': 0,
              'old_certificate_recomputations': 0,
              'derivation': 'Exact consecutive equal-size averaging, then outward positive square statistics.',
              'rows': rows}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(f'PASS: {len(rows)} windows, {total_means} quarter-scale means, {total_lags} lags, {total_pairs} directed pairs; no new sieve or log calls.')
    for row in rows:
        print(f"X={row['X']}, r={row['r']}, M={row['M']}, C+=[{row['C_plus']['lower']}, {row['C_plus']['upper']}], winner={row['certified_unique_maximizing_block_lags']}")


if __name__ == '__main__':
    main()
