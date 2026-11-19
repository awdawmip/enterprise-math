"""Certified physical rounding counts at the cubic-root inventory scale."""
from argparse import ArgumentParser
from fractions import Fraction
from itertools import product
from math import log2
from pathlib import Path
import json
import numpy as np
import critical_bins as C
from native import native_tail_ratios


def source_region(c, v, w):
    # C81's explicit full-macro-single-preimage region, checked with integers.
    return (6**4 * c**15 < 7**4 * 256 * v**15
            and 25**4 * 256 * v**15 < 29**4 * c**15
            and 11**4 * v**9 < 10**4 * 256 * w**9
            and w < v)


def singleton_mask(keys):
    _, inverse, counts = np.unique(keys, axis=0, return_inverse=True,
                                   return_counts=True)
    return counts[inverse] == 1


def calculate(c, b, p):
    stocks = [c, c+b, c+2*b]
    C.prepare(stocks[-1])
    C.terminal.cache_clear()
    rows, region = [], []
    native = 0
    for v in range(2, c+1):
        for w in range(2, v+1):
            middle = C.block(v, w, 3, C.terminal(w))
            values = [C.full_width(n, v, middle) for n in stocks]
            if c <= 16:
                for n, (lo, hi) in zip(stocks, values):
                    tails = native_tail_ratios(n, v, w)
                    exact = max(tails)/min(tails)
                    assert isinstance(exact, Fraction)
                    assert lo <= exact*C.UNIT <= hi
                    native += 1
            rows.append([C.bin_number(value, p+1, (0, 1))-(1 << (p+1))
                         for value in values])
            region.append(source_region(c, v, w))
    table = np.asarray(rows, dtype=np.int64)
    region = np.asarray(region, dtype=bool)
    origins = []
    for origin in product(range(2), repeat=3):
        keys = (table+np.asarray(origin))//2
        pair = singleton_mask(keys[:, [0, 2]])
        triple = singleton_mask(keys)
        assert np.all(triple | ~pair)
        origins.append({'offsets_halves': list(origin),
                        'second_difference_halves_mod2':
                            (origin[0]-2*origin[1]+origin[2]) % 2,
                        'endpoint_unique': int(pair.sum()),
                        'triple_unique': int(triple.sum()),
                        'region_endpoint_unique': int((region & pair).sum()),
                        'region_triple_unique': int((region & triple).sum())})
    return {'c': c, 'b': b, 'p': p, 'n': len(rows),
            'beta_display': b/c**(1/3),
            'L_display': 2**(p-1.75*log2(c)-.5*log2(c/b)),
            'interval_bits': C.BITS, 'native_enclosures': native,
            'region_n': int(region.sum()), 'origins': origins,
            'scope': 'Eight 0/half-grid origins; all physical competitors. '
                     'Finite counts do not establish limiting phase dependence.'}


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    results = []
    for case in [(8, 2, 7), (64, 4, 13), (64, 16, 12),
                 (512, 8, 19), (512, 32, 18)]:
        result = calculate(*case)
        results.append(result)
        args.output.write_text(json.dumps(results, indent=2)+'\n')
        print(case, result['n'], result['region_n'], flush=True)
