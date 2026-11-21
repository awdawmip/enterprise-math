"""Exact separation by arbitrary Boolean functions of the three coordinates.

The three coordinates are the established finite original-menu history readout.
This script does not change their Heartbeat X6 interpretation or native model.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import lcm
from pathlib import Path
import argparse
import json

TYPES = ((9, 557), (10, 744), (11, 936), (11, 944))
COUNTS = (2, 5, 2, 1)
POINTS = list(product(range(5), repeat=3))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--witness', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    data = args.witness.read_bytes()
    point = json.loads(data)
    free = int(point['free_mask'])
    rows = point['weights']
    weights = [Fraction(r['numerator'], r['denominator']) for r in rows]
    den = lcm(*(w.denominator for w in weights))
    numerators = [w.numerator*(den//w.denominator) for w in weights]
    types = [TYPES.index((r['size'], r['cost'])) for r in rows]
    class_masks = [int(r['mask']) for r in rows]
    features = [sum(1 << p for p, x in enumerate(POINTS)
                    if (free >> p) & 1 and x[axis] == value)
                for axis in range(3) for value in range(1, 5)]
    parity_masks = [sum(1 << j for j, mask in enumerate(class_masks)
                        if (mask & feature).bit_count() % 2)
                    for feature in features]
    type_parity = [sum(COUNTS[t] for t in range(4) if a >> t & 1) % 2
                   for a in range(16)]
    best = None
    shortest = None
    violated = 0
    by_length = {}
    current_u = current_parity = previous_gray = 0
    for index in range(1 << 12):
        gray = index ^ (index >> 1)
        if index:
            flipped = (gray ^ previous_gray).bit_length()-1
            current_u ^= features[flipped]
            current_parity ^= parity_masks[flipped]
        previous_gray = gray
        odd_weight = [0]*4
        bits = current_parity
        while bits:
            j = (bits & -bits).bit_length()-1
            odd_weight[types[j]] += numerators[j]
            bits &= bits-1
        for a in range(16):
            if (current_u.bit_count()+type_parity[a]) % 2 != 1:
                continue
            lhs = sum(COUNTS[t]*den-odd_weight[t] if a >> t & 1 else odd_weight[t]
                      for t in range(4))
            candidate = (lhs, gray.bit_count(), gray, a, current_u)
            if best is None or candidate[:2] < best[:2]:
                best = candidate
            if lhs < den:
                violated += 1
                by_length[gray.bit_count()] = by_length.get(gray.bit_count(), 0)+1
                if shortest is None or (candidate[1], candidate[0]) < (shortest[1], shortest[0]):
                    shortest = candidate

    def record(candidate):
        if candidate is None:
            return None
        lhs, length, selected, a, u = candidate
        # Independent direct exact sum at the selected original masks.
        actual = sum((w for r, w, t in zip(rows, weights, types)
                      if (((int(r['mask']) & u).bit_count() + ((a >> t) & 1)) % 2)),
                     Fraction())
        assert actual == Fraction(lhs, den)
        assert (u.bit_count()+sum(COUNTS[t] for t in range(4) if a >> t & 1)) % 2 == 1
        return {'features': [{'axis': j//4, 'value': 1+j%4} for j in range(12) if selected >> j & 1],
                'feature_count': length, 'type_parities': [(a >> t) & 1 for t in range(4)],
                'subset_mask': str(u), 'subset_size': u.bit_count(), 'lhs': str(actual),
                'rhs': 1, 'gap': str(1-actual), 'violated': actual < 1}

    result = {'frame': point['frame'], 'witness_sha256': sha256(data).hexdigest(),
              'family': 'all coordinate-additive Boolean functions, with type parities',
              'indexed_cuts': (1 << 12)*8, 'violated_indexed_cuts': violated,
              'violated_by_feature_count': by_length,
              'minimum': record(best), 'shortest_separator': record(shortest),
              'arithmetic': 'exact integers and rational numbers',
              'scope': 'Separation of this specified point, not infeasibility of the full candidate LP.',
              'review_status': 'NOT_REVIEWED'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
