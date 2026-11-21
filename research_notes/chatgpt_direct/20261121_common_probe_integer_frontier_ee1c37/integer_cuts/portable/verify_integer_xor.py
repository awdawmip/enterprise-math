"""Verify parity cuts for XORs of at most three fibers/singletons, exactly.

This augments the point/type/full-star certificate verifier. It does not assert
that these indexed inequalities are all distinct, or that the point is integral.
"""
from pathlib import Path
from fractions import Fraction
from math import lcm, comb
import argparse
import hashlib
import importlib.util
import json
import subprocess
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--witness-dir', type=Path, required=True)
    parser.add_argument('--parallel-module', type=Path, required=True)
    parser.add_argument('--work', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--frames', type=int, nargs='+', default=[1, 2, 3, 4, 5])
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('parallel_definitions', args.parallel_module)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module.COUNTS == (2, 5, 2, 1) or module.COUNTS == [2, 5, 2, 1]
    args.work.mkdir(parents=True, exist_ok=True)
    binary = args.work.resolve() / 'integer_xor'
    source = Path(__file__).with_name('integer_xor.cpp')
    subprocess.run(['c++', '-std=c++20', '-O3', str(source), '-o', str(binary)], check=True)
    results = []
    for frame in args.frames:
        start = time.monotonic()
        path = args.witness_dir / f'cover_{frame}.json'
        data = path.read_bytes()
        point = json.loads(data)
        free = int(point['free_mask'])
        rows = point['weights']
        weights = [Fraction(r['numerator'], r['denominator']) for r in rows]
        assert all(0 < w <= 1 for w in weights)
        denominator = lcm(*(w.denominator for w in weights))
        # Every exact sum is at most 10*denominator. Thus 256 bits suffice.
        assert denominator.bit_length() <= 250
        def limbs(value):
            return ' '.join(str((value >> (64*k)) & (2**64-1)) for k in range(4))
        features = [0] + [h & free for line in module.FIBERS for h in line]
        features.extend(1 << p for p in range(125) if free >> p & 1)
        blocks = []
        for t, kind in enumerate(module.TYPES):
            subset = [(r, w) for r, w in zip(rows, weights) if (r['size'], r['cost']) == kind]
            assert sum((w for r, w in subset), Fraction()) == module.COUNTS[t]
            for i in range(0, len(subset), 8):
                blocks.append((t, subset[i:i+8]))
        assert sum(len(b) for t, b in blocks) == len(rows)
        lines = [f'{len(features)} {len(blocks)} {limbs(denominator)}',
                 ' '.join(str(h.bit_count() % 2) for h in features)]
        for t, block in blocks:
            values = [w.numerator * (denominator // w.denominator) for r, w in block]
            values.extend([0] * (8 - len(block)))
            lines.append(str(t) + ' ' + ' '.join(limbs(v)+' '+str((v*2**60)//denominator)
                                                for v in values))
        for h in features:
            lines.append(' '.join(str(sum(((int(r['mask']) & h).bit_count() % 2) << i
                                          for i, (r, w) in enumerate(block)))
                                  for t, block in blocks))
        result = subprocess.run([str(binary)], input='\n'.join(lines)+'\n',
                                text=True, capture_output=True)
        value = json.loads(result.stdout)
        if not value['verified']:
            assert result.returncode == 1
            subset = 0
            for index in value['features']:
                subset ^= features[index]
            bits = [(value['type_mask'] >> t) & 1 for t in range(4)]
            assert (subset.bit_count() + sum(b*n for b, n in zip(bits, module.COUNTS))) % 2 == 1
            actual = sum((w for r, w in zip(rows, weights)
                          if ((int(r['mask']) & subset).bit_count()
                              + bits[module.TYPES.index((r['size'], r['cost']))]) % 2), Fraction())
            assert actual < 1
            value.update(frame=frame, subset_mask=str(subset), subset_size=subset.bit_count(),
                         exact_lhs=str(actual), type_parities=bits,
                         witness_sha256=hashlib.sha256(data).hexdigest())
            args.output.write_text(json.dumps(value, indent=2)+'\n')
            print(json.dumps(value), flush=True)
            raise SystemExit(1)
        assert result.returncode == 0 and value['verified'], value
        expected = 1 + sum(comb(len(features) - 1, k) for k in (1, 2, 3))
        assert value['indexed_subsets'] == expected
        assert value['indexed_cuts'] == 8 * expected
        value.update(frame=frame, positive_classes=len(rows), features=len(features)-1,
                     witness_sha256=hashlib.sha256(data).hexdigest(),
                     denominator_bits=denominator.bit_length(), seconds=time.monotonic()-start)
        results.append(value)
        print(json.dumps(value), flush=True)
        args.output.write_text(json.dumps({'schema': 'EXACT_THREE_FEATURE_TYPE_PARITY_V1',
                                          'frames': results}, indent=2)+'\n')


if __name__ == '__main__':
    main()
