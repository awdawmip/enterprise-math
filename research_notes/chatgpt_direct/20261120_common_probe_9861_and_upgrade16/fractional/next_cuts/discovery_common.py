"""Portable helpers for discovery only; the published verifier is independent.

The three routines below were extracted from the original star_closure.py and
average_stabilizer.py.  No solver is called when this module is imported.
"""
from collections import Counter
from functools import lru_cache
import importlib.util
import json
from math import lcm
from pathlib import Path

HERE = Path(__file__).resolve().parent
DELIVERY_ROOT = HERE.parent.parent
EXPECTED_TYPES = {(9, 557): 24000, (10, 744): 12000,
                  (11, 936): 4500, (11, 944): 12000}
EXPECTED_FRAME_COUNTS = {1: 7953, 2: 8538, 3: 8718, 4: 8476, 5: 7958}


def points(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask -= bit


@lru_cache(maxsize=None)
def native_module(delivery_root=DELIVERY_ROOT):
    """Load the shipped native observation/symmetry definitions by file path."""
    path = Path(delivery_root).resolve().joinpath(
        *(['previous'] * 6), 'bounds', 'prior_bounds.py')
    if not path.is_file():
        raise FileNotFoundError(f'Native dependency not found: {path}')
    spec = importlib.util.spec_from_file_location('discovery_prior_bounds', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_problem(frame_number, bank_path, delivery_root=DELIVERY_ROOT):
    """Read the complete four-type bank and form the point/type equalities.

The bank has 24-byte <QQII rows (mask low, mask high, cost, size/tag).
It can contain other types; all 52,500 candidates of the four needed types must
be present.  Counts and uniqueness are checked before restriction to a frame.
"""
    import numpy as np
    from scipy.sparse import coo_matrix

    delivery_root = Path(delivery_root).resolve()
    bank_path = Path(bank_path).resolve()
    if not bank_path.is_file():
        raise FileNotFoundError(
            f'Candidate bank not found: {bank_path}. Supply --bank or build it '
            'with prepare_discovery_bank.py --work DIRECTORY.')
    if bank_path.stat().st_size % 24:
        raise ValueError(f'Candidate bank has an incomplete 24-byte row: {bank_path}')
    source = json.loads((delivery_root / 'lower/fractional_covers.json').read_text())
    frame = next(f for f in source['frames'] if f['frame'] == frame_number)
    counts = {tuple(map(int, t.split('-')[:2])): int(t.split('-')[2])
              for t in source['tag'].split('_')}
    counts.pop((12, 1104))
    assert set(counts) == set(EXPECTED_TYPES)
    types = sorted(counts)
    bank = np.fromfile(bank_path, dtype=[('lo', '<u8'), ('hi', '<u8'),
                                       ('cost', '<u4'), ('tag', '<u4')])
    allowed = np.array([(int(r['tag']) % 256, int(r['cost'])) in counts
                        for r in bank], dtype=bool)
    bank = bank[allowed]
    observed = Counter((int(r['tag']) % 256, int(r['cost'])) for r in bank)
    if dict(observed) != EXPECTED_TYPES:
        raise ValueError(f'Incomplete or unexpected type bank: {dict(observed)}')
    all_masks = [int(r['lo']) + (int(r['hi']) << 64) for r in bank]
    assert len(set(all_masks)) == len(all_masks), 'duplicate candidate mask'
    assert all(0 < m < (1 << 125) and m.bit_count() == int(r['tag']) % 256
               for m, r in zip(all_masks, bank))
    free = int(frame['free'])
    lo, hi = np.uint64(free % (1 << 64)), np.uint64(free >> 64)
    bank = bank[((bank['lo'] & ~lo) == 0) & ((bank['hi'] & ~hi) == 0)]
    masks = [int(r['lo']) + (int(r['hi']) << 64) for r in bank]
    assert len(masks) == EXPECTED_FRAME_COUNTS[frame_number]
    ts = [types.index((int(r['tag']) % 256, int(r['cost']))) for r in bank]
    ri, ci = [], []
    for j, (mask, t) in enumerate(zip(masks, ts)):
        support = list(points(mask)) + [125 + t]
        ri.extend(support)
        ci.extend([j] * len(support))
    eq = coo_matrix((np.ones(len(ri), dtype=np.int8), (ri, ci)),
                    shape=(125 + len(types), len(masks))).tocsr()
    target = np.zeros(125 + len(types), dtype=np.int64)
    target[list(points(free))] = 1
    for i, t in enumerate(types):
        target[125 + i] = counts[t]
    return source, frame, bank, masks, ts, types, eq, target


def verify_stars(weights, free):
    """Exact positive-anchor/free-point check used during discovery."""
    masks = list(weights)
    q = 1
    for weight in weights.values():
        q = lcm(q, weight.denominator)
    integers = [int(weights[mask] * q) for mask in masks]
    best = None
    for i, mask in enumerate(masks):
        compatible = [0] * 125
        for other, weight in zip(masks, integers):
            if other & mask:
                continue
            for p in points(other):
                compatible[p] += weight
        for p in points(free ^ mask):
            slack = compatible[p] - integers[i]
            if best is None or slack < best[0]:
                best = (slack, mask, p, integers[i], compatible[p])
    return q, best
