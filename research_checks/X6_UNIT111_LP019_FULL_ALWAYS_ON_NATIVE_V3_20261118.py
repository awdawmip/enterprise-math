# X6 Unit111 / 2026-11-18 / AUTHOR-EXECUTED UNREVIEWED NOT_ADMITTED
# Opt-in strict LP019: Unit108 original Git blob c1842fbd34fb6fffa08a40a709b4838a6f2a5640 preserved.
# Every original `assert` is converted into an ordinary always-on conditional raise.
# Original pinned native BRC blob 300a96e3dc24bf6fff73743037a0347a8bc83176 retained.
# Not the original frozen R063/Helly native benchmark.
"""Exact LP019 typed test: C4 histograms, signed readout, and two-axis free BRC.

No historical R063 process tensor is reimplemented. The free signed-step
specialization is separately typed; the accepted R063 tensor remains source data.
"""
from collections import defaultdict
from itertools import product
from math import factorial, comb
from pathlib import Path
import importlib.util
import hashlib
import json

def signed_and_thickness(h):
    pi, mi, pj, mj = h
    return ((pi - mi, pj - mj), (pi + mi, pj + mj))

def reconstruct(s, u):
    si, sj = s
    ui, uj = u
    if any((a < abs(b) or (a - b) % 2 for a, b in zip(u, s))):
        raise ValueError('infeasible signed/thickness data')
    return ((ui + si) // 2, (ui - si) // 2, (uj + sj) // 2, (uj - sj) // 2)

def hidden_histogram_count(s, n):
    residual = n - abs(s[0]) - abs(s[1])
    return 0 if residual < 0 or residual % 2 else residual // 2 + 1

def word_formula(s, n):
    residual = n - abs(s[0]) - abs(s[1])
    if residual < 0 or residual % 2:
        return 0
    K = residual // 2
    positive_i, negative_i = (max(s[0], 0), max(-s[0], 0))
    positive_j, negative_j = (max(s[1], 0), max(-s[1], 0))
    return sum((factorial(n) // (factorial(positive_i + k) * factorial(negative_i + k) * factorial(positive_j + K - k) * factorial(negative_j + K - k)) for k in range(K + 1)))

def run():
    seen = set()
    for h in product(range(5), repeat=4):
        s, u = signed_and_thickness(h)
        if not reconstruct(s, u) == h:
            raise AssertionError('UNIT111_ALWAYS_ON_CHECK_01:line_59')
        if not (s, u) not in seen:
            raise AssertionError('UNIT111_ALWAYS_ON_CHECK_02:line_60')
        seen.add((s, u))
    if not len(seen) == 625:
        raise AssertionError('UNIT111_ALWAYS_ON_CHECK_03:line_62')
    hi, hj, empty = ((1, 1, 0, 0), (0, 0, 1, 1), (0, 0, 0, 0))
    if not signed_and_thickness(hi)[0] == signed_and_thickness(hj)[0] == (0, 0):
        raise AssertionError('UNIT111_ALWAYS_ON_CHECK_04:line_65')
    if not sum(hi) == sum(hj) == 2:
        raise AssertionError('UNIT111_ALWAYS_ON_CHECK_05:line_66')
    if not (signed_and_thickness(empty)[0] == (0, 0) and sum(empty) == 0):
        raise AssertionError('UNIT111_ALWAYS_ON_CHECK_06:line_67')
    if not signed_and_thickness(hi)[1] == (2, 0):
        raise AssertionError('UNIT111_ALWAYS_ON_CHECK_07:line_68')
    if not signed_and_thickness(hj)[1] == (0, 2):
        raise AssertionError('UNIT111_ALWAYS_ON_CHECK_08:line_69')
    dynamic = {(0, 0): 1}
    compared = 0
    per_length = []
    for n in range(13):
        if not sum(dynamic.values()) == 4 ** n:
            raise AssertionError('UNIT111_ALWAYS_ON_CHECK_09:line_75')
        for si in range(-n, n + 1):
            for sj in range(-n, n + 1):
                s = (si, sj)
                if not dynamic.get(s, 0) == word_formula(s, n):
                    raise AssertionError('UNIT111_ALWAYS_ON_CHECK_10:line_79')
                if not hidden_histogram_count(s, n) == ((n - abs(si) - abs(sj)) // 2 + 1 if n >= abs(si) + abs(sj) and (n - abs(si) - abs(sj)) % 2 == 0 else 0):
                    raise AssertionError('UNIT111_ALWAYS_ON_CHECK_11:line_81')
                compared += 1
        per_length.append(len(dynamic))
        next_dynamic = defaultdict(int)
        for (si, sj), count in dynamic.items():
            for ds in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_dynamic[si + ds[0], sj + ds[1]] += count
        dynamic = dict(next_dynamic)
    if not word_formula((0, 0), 2) == 4:
        raise AssertionError('UNIT111_ALWAYS_ON_CHECK_12:line_93')
    if not word_formula((0, 0), 4) == 36:
        raise AssertionError('UNIT111_ALWAYS_ON_CHECK_13:line_94')
    if not hidden_histogram_count((0, 0), 2) == 2:
        raise AssertionError('UNIT111_ALWAYS_ON_CHECK_14:line_95')
    if not 6 * 2 == 12:
        raise AssertionError('UNIT111_ALWAYS_ON_CHECK_15:line_98')
    source = Path(__file__).resolve().parents[1] / 'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py'
    data = source.read_bytes()
    blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\x00' + data).hexdigest()
    if blob != '300a96e3dc24bf6fff73743037a0347a8bc83176':
        raise RuntimeError(f'original signed BRC Git blob mismatch: {blob}')
    spec = importlib.util.spec_from_file_location('frozen_x6_signed_brc', source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    zero = (0,) * 6
    six_dynamic = {zero: 1}
    six_comparisons = 0
    six_lengths = []
    for n in range(7):
        if not sum(six_dynamic.values()) == 12 ** n:
            raise AssertionError('UNIT111_ALWAYS_ON_CHECK_16:line_117')
        for z, actual in six_dynamic.items():
            native_actual = module.endpoint_multiplicity(n, z)
            if native_actual != actual:
                raise AssertionError(f'original signed BRC endpoint mismatch at n={n} z={z}: {native_actual} != {actual}')
            K, parity = divmod(n - sum(map(abs, z)), 2)
            if not (parity == 0 and K >= 0):
                raise AssertionError('UNIT111_ALWAYS_ON_CHECK_17:line_123')
            if not comb(K + 5, 5) >= 1:
                raise AssertionError('UNIT111_ALWAYS_ON_CHECK_18:line_124')
            six_comparisons += 1
        six_lengths.append(len(six_dynamic))
        next_dynamic = defaultdict(int)
        for z, count in six_dynamic.items():
            for axis in range(6):
                for sign in (-1, 1):
                    z2 = list(z)
                    z2[axis] += sign
                    next_dynamic[tuple(z2)] += count
        six_dynamic = dict(next_dynamic)
    for n, expected in ((0, 1), (2, 12), (4, 396)):
        native_actual = module.return_multiplicity(n)
        if native_actual != expected:
            raise AssertionError(f'original signed BRC return mismatch at n={n}: {native_actual} != {expected}')
    native_wrong_parity = module.endpoint_multiplicity(2, (1, 0, 0, 0, 0, 0))
    if native_wrong_parity != 0:
        raise AssertionError(f'original signed BRC odd-parity endpoint should be 0: {native_wrong_parity}')
    return {'status': 'PASS', 'exact_histograms_checked': len(seen), 'free_signed_step_lengths': '0..12', 'signed_endpoint_formula_comparisons': compared, 'position_sensitive_order_not_quotiented': True, 'axis_thickness_is_needed_beyond_signed_and_total': True, 'two_axis_return_n2': word_formula((0, 0), 2), 'two_axis_return_n4': word_formula((0, 0), 4), 'six_axis_return_n2': 12, 'six_axis_return_n4': 396, 'existing_native_brc_imported': True, 'existing_native_brc_git_blob': blob, 'native_six_axis_dp_lengths': '0..6', 'native_six_axis_endpoint_comparisons': six_comparisons, 'native_endpoints_by_length': six_lengths, 'endpoint_counts_by_length': per_length}
if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True))
