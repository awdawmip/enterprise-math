"""Certify every Boolean-pair/type parity cut using an exact dyadic FWT.

The transformed integer objective has absolute error less than m/2**40,
where m is positive support size. All potentially violated cuts are retained
and checked directly with the original rational weights.
"""
from pathlib import Path
from fractions import Fraction
from hashlib import sha256
import argparse
import json
import subprocess

TYPES = ((9, 557), (10, 744), (11, 936), (11, 944))
COUNTS = (2, 5, 2, 1)
COORDS = [(i // 25, i // 5 % 5, i % 5) for i in range(125)]
SCALE = 1 << 40


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--witness', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--pair', type=int, nargs=2, required=True)
    parser.add_argument('--binary', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    data = args.witness.read_bytes(); doc = json.loads(data)
    free = int(doc['free_mask']); rows = doc['weights']
    axes = args.pair; assert len(set(axes)) == 2 and all(0 <= x < 3 for x in axes)
    weights = [Fraction(row['numerator'], row['denominator']) for row in rows]
    assert all(w > 0 for w in weights) and sum(weights) == 10
    fibers = [sum(1 << p for p, x in enumerate(COORDS)
                  if free >> p & 1 and 5*x[axes[0]]+x[axes[1]] == value)
              for value in range(1, 25)]
    rhs = [mask.bit_count() % 2 for mask in fibers] + [n % 2 for n in COUNTS]
    assert rhs[-1] == 1
    rhs_mask = sum(bit << j for j, bit in enumerate(rhs[:-1]))
    encoded = []
    for row, weight in zip(rows, weights):
        mask = int(row['mask']); kind = TYPES.index((row['size'], row['cost']))
        column = sum(((mask & f).bit_count() % 2) << j for j, f in enumerate(fibers))
        column |= 1 << (24 + kind)
        constant = column >> 27
        reduced = (column & ((1 << 27)-1)) ^ (rhs_mask if constant else 0)
        numerator = (weight.numerator * SCALE) // weight.denominator
        encoded.append((reduced, -numerator if constant else numerator))
    source = args.output / 'fwt_input.txt'
    source.write_text(f'27 {len(rows)} {SCALE}\n' + ''.join(f'{key} {w}\n' for key, w in encoded))
    run = subprocess.run([str(args.binary), str(source)], capture_output=True, text=True, check=True)
    (args.output / 'fwt.stdout').write_text(run.stdout)
    (args.output / 'fwt.stderr').write_text(run.stderr)
    candidates = []; indices = set(); violations = []
    for line in run.stdout.splitlines():
        bits, score = map(int, line.split())
        assert 0 <= bits < (1 << 27) and bits not in indices
        indices.add(bits)
        assert score >= 8*SCALE-len(rows)
        last = 1 ^ ((bits & rhs_mask).bit_count() % 2)
        full = bits | (last << 27)
        selected = [j+1 for j in range(24) if full >> j & 1]
        subset = 0
        for j in selected: subset ^= fibers[j-1]
        parities = [(full >> (24+j)) & 1 for j in range(4)]
        assert (subset.bit_count()+sum(a*n for a,n in zip(parities,COUNTS))) % 2 == 1
        lhs = sum((w for row,w in zip(rows,weights)
                   if ((int(row['mask']) & subset).bit_count() + parities[TYPES.index((row['size'], row['cost']))]) % 2), Fraction())
        direct_dyadic = sum((-w if (key & bits).bit_count() % 2 else w) for key,w in encoded)
        assert direct_dyadic == score
        candidate = {'pair': axes, 'selected_pair_values': [[v//5, v%5] for v in selected],
                     'type_parities': parities, 'subset_mask': str(subset),
                     'subset_size': subset.bit_count(), 'lhs': str(lhs), 'rhs': 1,
                     'gap': str(1-lhs), 'violated': lhs < 1, 'dyadic_score': score}
        candidates.append(candidate)
        if lhs < 1: violations.append(candidate)
    assert candidates  # the lone type with required multiplicity one is tight
    candidates.sort(key=lambda item: Fraction(item['lhs']))
    shortest = min(violations, key=lambda item: (len(item['selected_pair_values']), Fraction(item['lhs']))) if violations else None
    result = {'frame': doc['frame'], 'witness_sha256': sha256(data).hexdigest(),
              'family': 'arbitrary Boolean function of a coordinate pair, plus type parities',
              'pair': axes, 'indexed_cuts': 1 << 27, 'dyadic_scale': SCALE,
              'strict_score_error_bound': f'{len(rows)}/{SCALE}',
              'exact_threshold_candidates': len(candidates), 'violated_indexed_cuts': len(violations),
              'minimum': candidates[0], 'shortest_separator': shortest,
              'violations': violations, 'global_family_verified_exactly': True,
              'full_lp_infeasibility_proved': False, 'statistics': run.stderr.strip(),
              'arithmetic': 'signed 64-bit exact dyadic FWT; original rational check of every threshold candidate',
              'input_sha256': sha256(source.read_bytes()).hexdigest(),
              'engine_source_sha256': sha256(Path(__file__).with_suffix('.cpp').read_bytes()).hexdigest(),
              'review_status': 'NOT_REVIEWED'}
    (args.output / 'result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'violations'}))


if __name__ == '__main__': main()
