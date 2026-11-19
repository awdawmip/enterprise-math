"""Independent arbitrary-precision bisect check of the two winning slices.

This uses a different minimization algorithm from the C++ two-pointer sweep.
The generated binary inputs are only reproducible working data.
"""
from bisect import bisect_left
import json
from pathlib import Path
import struct
import sys
from time import monotonic


def verify(directory: Path, suffix: str):
    start = monotonic()
    source = json.loads((directory / f'minimum_{suffix}.json').read_text())
    winner = source['minimum']
    data = (directory / f'family_{suffix}.bin').read_bytes()
    assert data[:8] == b'RIESELV4'
    low, middle, high, na, nb = struct.unpack_from('<QQQQQ', data, 8)
    modulus = low + (middle << 64) + (high << 128)
    assert modulus == int(source['modulus'])
    shift = winner['translation']
    scale = pow(2, -shift, modulus)
    a, b = [], []
    for i, (low, middle, high, code) in enumerate(struct.iter_unpack('<QQQQ', data[48:])):
        value = (low + (middle << 64) + (high << 128)) * scale % modulus
        (a if i < na else b).append(value)
    del data
    assert len(a) == na and len(b) == nb
    by_parity = [sorted(v for v in b if v % 2 == parity) for parity in range(2)]
    best = 2 * modulus
    for x in a:
        # Unwrapped sums must be odd.
        opposite = by_parity[1 - x % 2]
        if opposite:
            candidate = x + opposite[0]
            if candidate < modulus:
                best = min(best, candidate)
        # Wrapped sums must be even, since the modulus is odd.
        same = by_parity[x % 2]
        j = bisect_left(same, modulus - x)
        if j < len(same):
            best = min(best, x + same[j] - modulus)
    assert best == int(winner['root'])
    assert best == (a[winner['a_code']] + b[winner['b_code']]) % modulus
    assert best % 2 == 1
    if suffix == '3M':
        assert best % 3 == 0
    return {'branch': suffix, 'translation': shift, 'root': str(best),
            'left_count': na, 'right_count': nb,
            'algorithm': 'Python arbitrary-precision parity-separated binary search',
            'matches_complete_CXX_sweep': True, 'seconds': monotonic() - start}


if __name__ == '__main__':
    directory = Path(sys.argv[1] if len(sys.argv) > 1 else 'v4_phase_work')
    result = [verify(directory, suffix) for suffix in ['M', '3M']]
    out = Path(__file__).with_name('winner_slice_verification.json')
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))
