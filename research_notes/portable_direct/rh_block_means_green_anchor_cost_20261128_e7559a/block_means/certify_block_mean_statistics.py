#!/usr/bin/env python3
"""New block-mean directed statistics; exact fractions and outward intervals.

The previous full-center certificate is read, never regenerated.  Its immutable
80-digit logarithm helper is reused, but the prime prefixes required by the NEW
statistic are computed and honestly counted here.
"""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import argparse
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode = True


def load_module(path):
    spec = importlib.util.spec_from_file_location('block_mean_intervals', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def mean(z):
    return sum(z, F(0))/len(z)


def exact_checks():
    counts = dict(vectors=0, blockings=0, jensen_lengths=0,
                  point_recovery=0, complete_block_recovery=0,
                  trapezoid_identities=0, sawtooth_blind_examples=0)
    rows = []
    for k in range(1, 8):
        X = 2**k
        increments = [
            [F(1)]*(X-1),
            [F(0)]*(X-1),
            [F(-17)]*(X-1),
            [F(1)-F((13*i*i+7*i+3) % 31, (i % 5)+1) for i in range(X-1)],
            [F(1)-F(10*X if i == X//2 else 0) for i in range(X-1)],
        ]
        for inc in increments:
            z = [F(3, 7)]
            for b in inc:
                z.append(z[-1]+b)
            assert all(z[i+1]-z[i] <= 1 for i in range(X-1))
            counts['vectors'] += 1
            for s in range(k):
                r, M, t = 2**s, X//2**s, k-s
                w = [mean(z[i*r:(i+1)*r]) for i in range(M)]
                lens = [2**j for j in range(t)]
                C = max(sum((max(w[i+d]-w[i], 0)**2
                             for i in range(M-d)), F(0))/(X*d) for d in lens)
                for d in lens:
                    numerator = sum((max(w[i+d]-w[i], 0)**2
                                     for i in range(M-d)), F(0))
                    raw = sum((max(z[u+r*d]-z[u], 0)**2
                               for u in range(X-r*d)), F(0))
                    assert r*numerator <= raw
                    counts['jensen_lengths'] += 1
                assert max(z[-1]-z[0]-(r-1), 0)**2 <= t*t*X*C
                counts['complete_block_recovery'] += 1
                for n in range(X):
                    # sqrt(2)<3/2 gives an entirely rational check.
                    assert max(z[n]-z[0]-2*r, 0)**2 <= (F(t)+F(5, 2))**2*X*C
                    if n >= r:
                        j = n//r
                        assert z[n]-w[j-1] <= F(3*r-1, 2)
                    counts['point_recovery'] += 1
                counts['blockings'] += 1
                rows.append({'k': k, 's': s, 'C': str(C)})
        for s in range(k):
            r, M = 2**s, X//2**s
            saw = [F(i % r) for i in range(X)]
            assert all(saw[i+1]-saw[i] <= 1 for i in range(X-1))
            w = [mean(saw[i*r:(i+1)*r]) for i in range(M)]
            assert len(set(w)) == 1 and saw[-1]-saw[0] == r-1
            counts['sawtooth_blind_examples'] += 1
            for d in [2**j for j in range(k-s)]:
                for i in sorted(set([0, (M-d-1)//2, M-d-1])):
                    a = i*r
                    weights = []
                    for n in range(a+1, a+(d+1)*r):
                        direct = F(sum(a+v < n <= a+r*d+v for v in range(r)), r)
                        formula = F(max(min(r, n-a)-max(0, n-a-r*d), 0), r)
                        assert direct == formula
                        weights.append((n, direct))
                    assert sum((v for n, v in weights), F(0)) == r*d
                    # Arbitrary nonnegative rational source, with full background.
                    source = [F(0)]+[F((5*n*n+7*n) % 19, n % 4+1) for n in range(1, X)]
                    field = [F(0)]
                    for n in range(1, X):
                        field.append(field[-1]+1-source[n])
                    ww = [mean(field[j*r:(j+1)*r]) for j in range(M)]
                    deficit = r*d-sum((v*source[n] for n, v in weights), F(0))
                    assert ww[i+d]-ww[i] == deficit
                    counts['trapezoid_identities'] += 1
    return {**counts, 'rows': rows,
            'scope': 'finite rational implementation checks; unbounded claims use the proof'}


def sieve(limit):
    prime = bytearray(b'\x01')*limit
    prime[:2] = b'\x00\x00'
    for p in range(2, isqrt(limit-1)+1):
        if prime[p]:
            prime[p*p:limit:p] = b'\x00'*((limit-1-p*p)//p+1)
    return prime


def prime_statistics(m, old, kmax=14):
    limit = 2**(kmax+1)
    prime = sieve(limit)
    theta_lo, theta_hi = [0]*limit, [0]*limit
    primes = 0
    for n in range(1, limit):
        theta_lo[n], theta_hi[n] = theta_lo[n-1], theta_hi[n-1]
        if prime[n]:
            lo, hi = m.LOG_TWO if n == 2 else m.log_int(n)
            theta_lo[n] += lo
            theta_hi[n] += hi
            primes += 1
    old_rows = {row['k']: row for row in old['ordinary_prime_statistics']['rows']}
    rows, block_count, pairs, lag_count, retained_raw_terms = [], 0, 0, 0, 0
    for k in range(1, kmax+1):
        X, s = 2**k, k//2
        r, M, t = 2**s, X//2**s, k-s
        block_lows = [sum(theta_lo[X+i*r:X+(i+1)*r]) for i in range(M)]
        block_highs = [sum(theta_hi[X+i*r:X+(i+1)*r]) for i in range(M)]
        means = []
        for i in range(M):
            integer_total = r*(2*(X+i*r)+r-1)//2
            bounds = ((integer_total*m.S-block_highs[i])//r,
                      m.ceildiv(integer_total*m.S-block_lows[i], r))
            means.append({'i': i, 'first_integer': X+i*r,
                          'last_integer': X+(i+1)*r-1, 'value': m.record(bounds)})
        entries = []
        for j in range(t):
            d = 2**j
            lo_sq, hi_sq, pos, neg, unresolved = 0, 0, 0, 0, 0
            for i in range(M-d):
                # Difference of block theta sums has NONNEGATIVE prime coefficients.
                # Shared history cancels before error propagation.  Numerator is r
                # times the mean deficit, so division by r^2 comes after squaring.
                lo = r*r*d*m.S-(block_highs[i+d]-block_highs[i])
                hi = r*r*d*m.S-(block_lows[i+d]-block_lows[i])
                assert lo <= hi
                lo_sq += max(lo, 0)**2
                hi_sq += max(hi, 0)**2
                if lo >= 0:
                    pos += 1
                elif hi <= 0:
                    neg += 1
                else:
                    unresolved += 1
            den = r*r*X*d*m.S
            bounds = lo_sq//den, m.ceildiv(hi_sq, den)
            inherited = next(row for row in old_rows[k]['lengths'] if row['d'] == r*d)
            old_bounds = tuple(map(int, inherited['J_plus_over_Xd']['integer_bounds']))
            assert bounds[0] <= old_bounds[1]
            strong_comparison = bounds[1] <= old_bounds[0]
            if not strong_comparison:
                assert max(bounds[0], old_bounds[0]) <= min(bounds[1], old_bounds[1])
            entries.append({'block_lag': d, 'integer_lag': r*d, 'mean_pairs': M-d,
                            'directed_over_Xd': m.record(bounds),
                            'nonnegative_intervals': pos, 'nonpositive_intervals': neg,
                            'sign_unresolved': unresolved,
                            'inherited_full_center_bound': inherited['J_plus_over_Xd'],
                            'interval_upper_below_inherited_lower': strong_comparison})
            pairs += M-d
            lag_count += 1
            retained_raw_terms += X-r*d
        intervals = [tuple(map(int, row['directed_over_Xd']['integer_bounds'])) for row in entries]
        bounds = max(v[0] for v in intervals), max(v[1] for v in intervals)
        winners = [entries[i]['block_lag'] for i, v in enumerate(intervals)
                   if all(v[0] > z[1] for j, z in enumerate(intervals) if j != i)]
        coarse_intervals = [tuple(map(int, e['inherited_full_center_bound']['integer_bounds']))
                            for e in entries]
        coarse = max(v[0] for v in coarse_intervals), max(v[1] for v in coarse_intervals)
        rows.append({'k': k, 'X': X, 'r': r, 'M': M,
                     'C_plus': m.record(bounds),
                     'certified_unique_maximizing_block_lags': winners,
                     'inherited_coarse_K_plus': m.record(coarse),
                     'means': means, 'lags': entries})
        block_count += M
        assert sum(M-2**j for j in range(t)) == (t-1)*M+1
    if kmax == 14:
        assert (block_count, lag_count, pairs, retained_raw_terms, primes) == (508, 56, 2582, 186069, 3512)
    return {'windows': kmax, 'largest_integer_source': limit-1,
            'block_means': block_count, 'window_lag_groups': lag_count,
            'directed_mean_pair_terms': pairs,
            'retained_raw_center_terms_in_inherited_comparison': retained_raw_terms,
            'previous_all_center_terms': old['ordinary_prime_statistics']['center_length_terms'],
            'ordinary_primes': primes, 'certified_prime_log_intervals': primes,
            'decimal_interval_digits': m.DIGITS,
            'full_source_sieve_and_prefix_construction_charged': True,
            'old_road_or_old_statistic_recomputed': False,
            'rows': rows}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--previous', type=Path, required=True)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('block_mean_certificate.json'))
    args = parser.parse_args()
    helpers = list(args.previous.rglob('certify_fast_harmonic_energy.py'))
    assert len(helpers) == 1, helpers
    helper = helpers[0]
    inherited = args.previous/'arithmetic_sampling/dyadic_windows_certificate.json'
    assert inherited.is_file()
    old = json.loads(inherited.read_text())
    m = load_module(helper)
    result = {'schema': 'EM_DIRECTED_BLOCK_MEANS_CERTIFICATE_V1',
              'date': '2026-11-28', 'proof': 'COARSE_BLOCK_MEANS_AND_RH.md',
              'dependencies': [
                  {'path_in_previous': str(p.relative_to(args.previous)),
                   'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
                  for p in [helper, inherited]],
              'exact_rational_checks': exact_checks(),
              'ordinary_prime_statistics': prime_statistics(m, old)}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    z = result['ordinary_prime_statistics']
    print(f"PASS: {z['windows']} windows, {z['block_means']} means, {z['window_lag_groups']} lag groups, "
          f"{z['directed_mean_pair_terms']} directed pairs; {z['ordinary_primes']} new certified log intervals.")
    for row in z['rows']:
        print(f"X={row['X']:5d}, r={row['r']:3d}, M={row['M']:3d}, C+=[{row['C_plus']['lower']}, {row['C_plus']['upper']}], "
              f"winner={row['certified_unique_maximizing_block_lags']}")


if __name__ == '__main__':
    main()
