"""Reconstruct exact cost profiles and reconcile completed finite-search receipts.

This verifies coverage of the profile list and preserves the original search
receipts. It does not claim to rerun the searches themselves.
"""
import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path


def profile_name(counts):
    return '_'.join('-'.join(map(str, (s, c, n)))
                    for (s, c), n in sorted(counts.items()))


def audit(previous, seed_file, spectrum_file, receipt_files, first, last, output):
    sys.path.insert(0, str(previous / 'previous/previous/previous/previous/low'))
    from profiles import get, make_profiles, mn

    caps = get(12, last)
    keys = set()
    if seed_file is not None:
        with seed_file.open() as source:
            for line in source:
                size, cost = map(int, line.split(' ', 2)[:2])
                if cost <= caps.get(size, 0):
                    keys.add((size, cost))
    else:
        spectrum = json.loads(spectrum_file.read_text())
        keys = {(size, cost) for size, cost in spectrum['size_cost_pairs']
                if cost <= caps.get(size, 0)}
    keys = sorted(keys)
    cases = {}
    for value, counts in make_profiles(12, last, first, mn, keys):
        row = {key: n for key, n in zip(keys, counts) if n}
        cores = row.get((12, 1104), 0) + row.get((13, 1296), 0)
        if cores not in (0, 1, 2) or cores + row.get((12, 1116), 0) >= 7:
            continue
        cases[profile_name(row)] = value

    observed = {}
    duplicates = 0
    for receipt_file in receipt_files:
        for line_number, line in enumerate(receipt_file.read_text().splitlines(), 1):
            row = json.loads(line)
            if not first <= row['cost'] <= last:
                continue
            if row['tag'] not in cases:
                raise ValueError(f'Unexpected profile in {receipt_file}:{line_number}')
            assert row['cost'] == cases[row['tag']] and row['found'] == 0
            if row['tag'] in observed:
                duplicates += 1
                continue
            observed[row['tag']] = dict(row)
            observed[row['tag']].setdefault('receipt_file', receipt_file.name)
            observed[row['tag']].setdefault('receipt_line', line_number)

    output.mkdir(parents=True, exist_ok=True)
    summaries = []
    for cost in range(first, last + 1):
        expected = {tag for tag, value in cases.items() if value == cost}
        completed = expected & observed.keys()
        missing = sorted(expected - completed)
        tags = '\n'.join(sorted(expected)) + '\n'
        summary = {
            'cost': cost,
            'expected_low_core_profiles': len(expected),
            'completed_low_core_profiles': len(completed),
            'complete': not missing,
            'profile_sha256': hashlib.sha256(tags.encode()).hexdigest(),
            'geometric_nodes': sum(observed[t]['geometric_nodes'] for t in completed),
            'search_nodes': sum(observed[t]['search_nodes'] for t in completed),
            'missing_profiles': missing,
        }
        summaries.append(summary)
        (output / f'cost_{cost}_profiles.txt').write_text(tags)
        (output / f'cost_{cost}_completed.jsonl').write_text(
            ''.join(json.dumps(observed[t], sort_keys=True) + '\n'
                    for t in sorted(completed)))
    result = {
        'scope': '12 labels; exactly 0, 1, or 2 cores; low-cost profile coverage',
        'arithmetic': 'integer',
        'verification': 'regenerated complete profile list; matched preserved zero-solution receipts',
        'search_rerun_claimed': False,
        'discarded_duplicate_receipts': duplicates,
        'layers': summaries,
    }
    (output / 'coverage.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--previous', type=Path, required=True)
    p.add_argument('--seeds', type=Path,
                   help='Optional freshly regenerated full class census seeds')
    p.add_argument('--spectrum', type=Path,
                   default=Path(__file__).with_name('class_cost_spectrum.json'))
    p.add_argument('--receipts', type=Path, nargs='+', required=True)
    p.add_argument('--first', type=int, default=9859)
    p.add_argument('--last', type=int, default=9860)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    audit(a.previous.resolve(), a.seeds, a.spectrum, a.receipts, a.first, a.last, a.output)
