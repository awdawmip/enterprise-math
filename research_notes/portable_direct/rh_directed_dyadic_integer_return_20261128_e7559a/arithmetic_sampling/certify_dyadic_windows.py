#!/usr/bin/env python3
"""New exact directed average-chain checks and ordinary-prime dyadic statistics.

No previous road calculation or certificate is rerun.  The existing 80-place
integer interval logarithm is reused at its original immutable source bytes.
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
    spec = importlib.util.spec_from_file_location('dyadic_window_intervals', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def mean(z):
    return sum(z, F(0))/len(z)


def exact_chains():
    counts = {'vectors': 0, 'parent_child_contrasts': 0,
              'ordered_point_pairs': 0, 'shifted_average_steps': 0}
    sample_rows = []
    for k in range(1, 7):
        h = 2**k
        cases = [
            [F(3) for i in range(h)],
            [F(i) for i in range(h)],
            [F(-i) for i in range(h)],
            [F((-1)**i*(i+1), 3) for i in range(h)],
            [F((17*i*i+5*i+3) % 29-14, i % 5+1) for i in range(h)],
            [F(int(i == h//2)*h-int(i == h//2-1)*2*h) for i in range(h)],
        ]
        for z in cases:
            counts['vectors'] += 1
            lengths = [2**j for j in range(k)]
            jall = {d: sum(((z[i+d]-z[i])**2 for i in range(h-d)), F(0))
                    for d in lengths}
            jpos = {d: sum((max(z[i+d]-z[i], F(0))**2
                           for i in range(h-d)), F(0)) for d in lengths}
            kval = max(jall[d]/(h*d) for d in lengths)
            kp = max(jpos[d]/(h*d) for d in lengths)
            mu = mean(z)
            assert all((v-mu)**2 <= F(k*k*h, 4)*kval for v in z)
            assert (max(z)-min(z))**2 <= k*k*h*kval
            assert max(z[-1]-z[0], F(0))**2 <= k*k*h*kp
            for d in lengths:
                for a in range(0, h, 2*d):
                    left, right = mean(z[a:a+d]), mean(z[a+d:a+2*d])
                    diff = right-left
                    assert diff == sum((z[v+d]-z[v] for v in range(a, a+d)), F(0))/d
                    assert max(diff, F(0))**2 <= jpos[d]/d
                    counts['parent_child_contrasts'] += 1
            for i in range(h):
                for j in range(i+1, h):
                    counts['ordered_point_pairs'] += 1
                    d = 1 << ((j-i+1).bit_length()-1)
                    g = j-i+1-d
                    pos = i
                    telescoped = F(0)
                    for bit in range(g.bit_length()):
                        delta = 1 << bit
                        if not g & delta:
                            continue
                        before, after = mean(z[pos:pos+d]), mean(z[pos+delta:pos+delta+d])
                        diff = after-before
                        assert pos+delta+d <= j+1
                        assert max(diff, F(0))**2 <= jpos[delta]/d
                        telescoped += diff
                        pos += delta
                        counts['shifted_average_steps'] += 1
                    assert pos == j-d+1
                    assert telescoped == mean(z[j-d+1:j+1])-mean(z[i:i+d])
                    # 1+sqrt(2)<5/2 yields an entirely rational final check.
                    assert max(z[j]-z[i], F(0))**2 <= (F(k)+F(5, 2))**2*h*kp
            sample_rows.append({'k': k, 'K': str(kval), 'K_plus': str(kp)})
    blocks = []
    for k in range(1, 7):
        h = 2**k
        c = 4**k
        z = [F(c)]*h
        assert all(sum((max(z[i+d]-z[i], F(0))**2 for i in range(h-d)), F(0)) == 0
                   for d in (2**j for j in range(k)))
        blocks.append({'k': k, 'value': c, 'K': 0,
                       'next_boundary_jump': 4**(k+1)-c})
    return {**counts, 'vector_rows': sample_rows,
            'unpaid_bridge_counterexample': blocks,
            'finite_checks_are_not_the_unbounded_proof': True}


def sieve(limit):
    prime = bytearray(b'\x01')*limit
    prime[:2] = b'\x00\x00'
    for p in range(2, isqrt(limit-1)+1):
        if prime[p]:
            prime[p*p:limit:p] = b'\x00'*((limit-1-p*p)//p+1)
    return prime


def prime_statistics(module, kmax):
    m = module
    limit = 2**(kmax+1)
    prime = sieve(limit)
    lows, highs = [0]*limit, [0]*limit
    prime_count = 0
    for n in range(1, limit):
        lows[n], highs[n] = lows[n-1], highs[n-1]
        if prime[n]:
            lo, hi = m.LOG_TWO if n == 2 else m.log_int(n)
            lows[n] += lo
            highs[n] += hi
            prime_count += 1

    rows, total_pairs = [], 0
    for k in range(1, kmax+1):
        X = 2**k
        if 2*X < limit:
            assert not prime[2*X]
            assert lows[2*X] == lows[2*X-1] and highs[2*X] == highs[2*X-1]
        runs, current_run = [], 0
        for n in range(X+1, 2*X):
            if prime[n]:
                if current_run:
                    runs.append(current_run)
                    current_run = 0
            else:
                current_run += 1
        if current_run:
            runs.append(current_run)
        entries = []
        for j in range(k):
            d = 2**j
            lo_sq = hi_sq = lo_pos = hi_pos = 0
            positive_certified = negative_certified = unresolved = 0
            for u in range(X, 2*X-d):
                # Use the same interval's log sum.  Prehistory cancels exactly.
                lo = d*m.S-(highs[u+d]-highs[u])
                hi = d*m.S-(lows[u+d]-lows[u])
                assert lo <= hi
                if lo >= 0:
                    sl, sh = lo*lo, hi*hi
                    positive_certified += 1
                elif hi <= 0:
                    sl, sh = hi*hi, lo*lo
                    negative_certified += 1
                else:
                    sl, sh = 0, max(lo*lo, hi*hi)
                    unresolved += 1
                lo_sq += sl
                hi_sq += sh
                lo_pos += max(lo, 0)**2
                hi_pos += max(hi, 0)**2
            count = X-d
            total_pairs += count
            denominator = X*d*m.S
            full = (lo_sq//denominator, m.ceildiv(hi_sq, denominator))
            directed = (lo_pos//denominator, m.ceildiv(hi_pos, denominator))
            assert directed[0] <= full[1]
            entry = {'d': d, 'centers': count,
                            'J_over_Xd': m.record(full),
                            'J_plus_over_Xd': m.record(directed),
                            'strict_positive_or_zero_intervals': positive_certified,
                            'strict_negative_or_zero_intervals': negative_certified,
                            'sign_unresolved': unresolved}
            if d*m.S <= k*m.LOG_TWO[0]:
                empty_count = sum(max(r-d+1, 0) for r in runs)
                assert lo_pos == hi_pos == empty_count*d*d*m.S*m.S
                entry['short_length_empty_window_count'] = empty_count
                entry['exact_J_plus_over_Xd'] = str(F(empty_count*d, X))
            entries.append(entry)

        def max_record(field):
            intervals = [(int(row[field]['integer_bounds'][0]),
                          int(row[field]['integer_bounds'][1])) for row in entries]
            result = max(v[0] for v in intervals), max(v[1] for v in intervals)
            winners = [entries[i]['d'] for i, v in enumerate(intervals)
                       if all(v[0] > w[1] for j, w in enumerate(intervals) if i != j)]
            return {'value': m.record(result), 'certified_unique_maximizing_lengths': winners}

        rows.append({'k': k, 'X': X, 'K': max_record('J_over_Xd'),
                     'K_plus': max_record('J_plus_over_Xd'), 'lengths': entries})
    expected = (kmax-2)*2**(kmax+1)+kmax+4
    assert total_pairs == expected
    return {'kmax': kmax, 'largest_integer_source': limit-1,
            'windows': kmax, 'window_length_pairs': kmax*(kmax+1)//2,
            'center_length_terms': total_pairs, 'ordinary_primes': prime_count,
            'certified_prime_log_intervals': prime_count,
            'decimal_interval_digits': m.DIGITS,
            'source_sieve_executed_for_this_new_statistic': True,
            'old_road_samples_or_certificates_rerun': False,
            'rows': rows}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--previous', type=Path, required=True)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('dyadic_windows_certificate.json'))
    args = parser.parse_args()
    helpers = list(args.previous.rglob('certify_fast_harmonic_energy.py'))
    assert len(helpers) == 1, helpers
    helper = helpers[0]
    m = load_module(helper)
    result = {'schema': 'EM_DYADIC_DIRECTED_WINDOWS_CERTIFICATE_V1',
              'date': '2026-11-28',
              'proof': 'DYADIC_WINDOWS_AND_INTEGER_BRIDGES.md',
              'helper': {'path_in_previous': str(helper.relative_to(args.previous)),
                         'sha256': hashlib.sha256(helper.read_bytes()).hexdigest()},
              'exact_average_chains': exact_chains(),
              'ordinary_prime_statistics': prime_statistics(m, 14)}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    stats = result['ordinary_prime_statistics']
    print(f"PASS: {stats['windows']} dyadic windows, {stats['window_length_pairs']} lengths, "
          f"{stats['center_length_terms']} full-center terms; {stats['ordinary_primes']} prime log intervals.")


if __name__ == '__main__':
    main()
