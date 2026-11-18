#!/usr/bin/env python3
"""EC49BW: exact native signed-X6 boundary selectors and finite-H rank checks.

Inputs are ordered native signed axis steps.  This is author-side finite evidence,
not a check of physical dynamics or independently accepted mathematics.
"""
from collections import defaultdict
from hashlib import sha1
from itertools import product
from json import dumps
from pathlib import Path
import sys
_NATIVE = Path(__file__).resolve().parent / 'signed_brc.py'
if not _NATIVE.exists():
    _NATIVE = Path(__file__).resolve().parent.parent / 'EC49BV_GROUP_FILTER_TRANSFER' / 'signed_brc.py'
sys.path.insert(0, str(_NATIVE.parent))
from signed_brc import endpoint_multiplicity, endpoint_weight

DIM = 6
ALPHABET = tuple((i, s) for i in range(DIM) for s in (1, -1))
WP = (2, 3, 3, 2, 1, 1)
WM = (1,) * DIM
SWAP = (1, 0, 2, 3, 4, 5)
ZERO = (0,) * DIM


def native_path_weight(path, permutation=tuple(range(DIM))):
    result = 1
    for axis, sign in path:
        j = permutation[axis]
        result *= WP[j] if sign == 1 else WM[j]
    return result


def closed_words(length):
    """Exact enumeration of all native words ending at X6 displacement zero."""
    def rec(left, coord, word):
        norm = sum(abs(x) for x in coord)
        if norm > left or (left - norm) % 2:
            return
        if not left:
            yield tuple(word)
            return
        for axis, sign in ALPHABET:
            nxt = list(coord)
            nxt[axis] += sign
            word.append((axis, sign))
            yield from rec(left - 1, tuple(nxt), word)
            word.pop()
    yield from rec(length, ZERO, [])


def prefix_suffix(path, r, s):
    return path[:r] + (path[len(path) - s:] if s else ())


def boundary_count_dp(n, L):
    """Sum of coefficients of (sum x_i + x_i^-1)^L with l1 norm <= n-L."""
    assert n % 2 == 0 and 0 <= L <= n
    states = {ZERO: 1}
    for _ in range(L):
        new = defaultdict(int)
        for vec, multiplicity in states.items():
            for axis, sign in ALPHABET:
                nxt = list(vec)
                nxt[axis] += sign
                new[tuple(nxt)] += multiplicity
        states = new
    return sum(c for d, c in states.items() if sum(abs(x) for x in d) <= n - L)


def brute_audit(n, r, s):
    """Compute exact per-boundary group-weight rank from all closed words."""
    first = {}
    rank_two = set()
    bag_sums = defaultdict(int)
    number = 0
    for p in closed_words(n):
        number += 1
        label = prefix_suffix(p, r, s)
        v = (native_path_weight(p), native_path_weight(p, SWAP))
        bag_sums[label] += v[0]
        prior = first.setdefault(label, v)
        if v[0] * prior[1] != v[1] * prior[0]:
            rank_two.add(label)
    native_number = endpoint_multiplicity(n, ZERO)
    native_sum = endpoint_weight(n, ZERO, WP, WM)
    assert number == native_number, (number, native_number)
    assert sum(bag_sums.values()) == native_sum, (sum(bag_sums.values()), native_sum)
    assert len(first) == boundary_count_dp(n, r + s)
    return {
        'n': n, 'prefix_length': r, 'suffix_length': s,
        'closed_words': number, 'native_weighted_total': int(native_sum),
        'attainable_boundary_atoms': len(first),
        'covariant_rank': len(first),
        'fixed_instrument_rank': len(first) + len(rank_two),
        'rank_two_boundary_atoms': len(rank_two),
        'group': ['identity', 'swap_axes_1_2'],
    }


def main():
    native = _NATIVE.read_bytes()
    native_blob = sha1(f'blob {len(native)}\0'.encode() + native).hexdigest()
    assert native_blob == '300a96e3dc24bf6fff73743037a0347a8bc83176'
    audits = [brute_audit(n, r, s) for n, r, s in (
        (2, 1, 0), (4, 1, 1), (4, 2, 0),
        (6, 1, 1), (6, 2, 2), (6, 3, 0),
    )]
    assert audits[1]['fixed_instrument_rank'] == 156
    assert audits[3]['fixed_instrument_rank'] == 288
    assert audits[-1]['covariant_rank'] == 12**3
    horizons = []
    for n, L in ((2, 1), (4, 2), (6, 3), (6, 4), (8, 4), (8, 6), (10, 5), (12, 6)):
        count = boundary_count_dp(n, L)
        lower = 6**(L // 2)
        assert lower <= count <= 12**L
        if n >= 2*L:
            assert count == 12**L
        horizons.append({'n': n, 'boundary_length': L,
                         'covariant_exact_rank': count,
                         'rigorous_lower_bound': lower, 'alphabet_upper_bound': 12**L})
    output = {'schema':'EC49BW_EXACT_NATIVE_X6_AUDIT_V1',
              'native_source_git_blob':native_blob,
              'native_weight_positive':list(WP),
              'native_weight_negative':list(WM),
              'brute_force_cases':audits,
              'dynamic_programming_cases':horizons,
              'scope':'Finite X6 closed ordered paths; Q-linear additive source-atom observations'}
    print(dumps(output, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
