"""Meaningful small-instance exact checks of the 192-bit minimizer.

Uses Python arbitrary precision and brute force, including shift provenance.
These checks are auxiliary; the proof of the full minimization is in proof.md.
"""
import json
from pathlib import Path
import random
import subprocess
import tempfile

from prepare_family import write_binary


def main():
    directory = Path(__file__).resolve().parent
    rng = random.Random(9700)
    widths = [8, 16, 32, 63, 64, 65, 127, 128, 129, 179, 180, 181, 187, 190]
    count = 0
    for width in widths:
        for repetition in range(4):
            modulus = (1 << (width-1)) + rng.getrandbits(width-1) | 1
            left, right = [], []
            for values in [left, right]:
                while len(values) < 2*(2+repetition):
                    v = rng.randrange(1, modulus)
                    if v not in values and modulus-v not in values:
                        values.extend([v, modulus-v])
            with tempfile.TemporaryDirectory(dir=directory) as tempdir:
                path = Path(tempdir)/'toy.bin'
                write_binary(path, modulus, left, right)
                result = json.loads(subprocess.check_output([str(directory/'minimize_family'), str(path), '17']))
            expected_global = None
            for t, answer in enumerate(result['minima']):
                scale = pow(2, -t, modulus)
                a = [v*scale % modulus for v in left]
                b = [v*scale % modulus for v in right]
                candidates = [(u+v) % modulus for u in a for v in b]
                expected = min(v if v % 2 else v+modulus for v in candidates)
                actual = int(answer['root'])
                assert actual == expected
                assert actual == (a[answer['a_code']] + b[answer['b_code']]) % modulus
                assert answer['translation'] == t
                expected_global = expected if expected_global is None else min(expected_global, expected)
            assert int(result['minimum']['root']) == expected_global
            count += 1
    report = {'instances': count, 'shifts_each': 17, 'total_exact_bruteforce_comparisons': count*17,
              'integer_widths': widths, 'rng_seed': 9700,
              'all_minima_and_provenance_match': True}
    (directory/'kernel_checks.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
