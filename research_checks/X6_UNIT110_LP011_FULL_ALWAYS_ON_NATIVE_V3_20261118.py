# X6 Unit110 / 2026-11-18 / AUTHOR VALIDATION, UNREVIEWED/NOT_ADMITTED.
# Opt-in strict LP011 native consumer; Unit108 original preserved unchanged.
# Source Unit108 Git blob SHA1: 296e4cdb8b5710a6b2017f24e4b6059a2554714e.
# All original Python assert tests are made explicit and always-on, including observer and embedding checks.
# Native import is mandatory and pinned to frozen original Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176.
# This script does not run the frozen R063/Helly benchmark.
"""LP011 bounded raw signed X6 dominant/observer and BRC interface regression.

Standalone exact-integer regression, distinct from prior signed-shell 72/111 checks.
When executed inside enterprise-math, optionally uses the existing Source
experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py module.
Provenance: LP011 HIRR REQUEST_REVISION; current TASK_RESEARCH, NONBLIND.
"""
from __future__ import annotations
import importlib.util
import itertools
import json
from math import factorial
from pathlib import Path
SELECTED_AXES = (0, 2, 5)
REPO_ROOT = Path(__file__).resolve().parents[1]
BRC_SOURCE = REPO_ROOT / 'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py'

def dominant_signed(vector):
    v = tuple(vector)
    if len(v) not in (3, 6) or any((type(x) is not int for x in v)):
        raise ValueError('raw signed integer 3-slice or 6-X6 required')
    m = max(map(abs, v))
    if not m:
        return frozenset()
    return frozenset(((i, 1 if x > 0 else -1) for i, x in enumerate(v) if abs(x) == m))

def embed3(v):
    if not len(v) == 3:
        raise AssertionError('UNIT110_ALWAYS_ON_CHECK_01:line_36')
    out = [0] * 6
    for k, x in zip(SELECTED_AXES, v):
        out[k] = x
    return tuple(out)

def minzero(v):
    h = min(v)
    return (tuple((x - h for x in v)), h)

def signed_from_observer(a, h):
    if not (min(a) == 0 and all((type(x) is int and x >= 0 for x in a))):
        raise AssertionError('UNIT110_ALWAYS_ON_CHECK_02:line_49')
    M = max(a)
    if M == 0:
        if h == 0:
            return frozenset()
        return frozenset(((i, 1 if h > 0 else -1) for i in range(3)))
    theta = 2 * h + M
    positive = {(i, 1) for i, x in enumerate(a) if x == M}
    negative = {(i, -1) for i, x in enumerate(a) if x == 0}
    if theta > 0:
        return frozenset(positive)
    if theta < 0:
        return frozenset(negative)
    return frozenset(positive | negative)

def legacy_positive_selector(a):
    M = max(a)
    return frozenset(((i, 1) for i, x in enumerate(a) if x == M)) if M else frozenset()

def brc_shortest(v):
    v = tuple(v)
    n = sum(map(abs, v))
    out = factorial(n)
    for x in v:
        out //= factorial(abs(x))
    return out

def main():
    signed_points = 0
    positive_guard_matches = 0
    zero_cases = 0
    signed_ties = 0
    brc_samples = 0
    imported_module_calls = 0
    module = None
    if not BRC_SOURCE.is_file():
        raise RuntimeError('Unit110 requires real frozen native signed_brc.py; missing dependency')
    import hashlib
    b = BRC_SOURCE.read_bytes()
    blob = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
    if blob != '300a96e3dc24bf6fff73743037a0347a8bc83176':
        raise RuntimeError(f'Unit110 frozen native source blob mismatch: {blob}')
    if BRC_SOURCE.is_file():
        spec = importlib.util.spec_from_file_location('x6_signed_brc_source_lp011', BRC_SOURCE)
        if spec is None or spec.loader is None:
            raise RuntimeError('original signed BRC Source import loader unavailable')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    for d in itertools.product(range(-7, 8), repeat=3):
        signed_points += 1
        a, h = minzero(d)
        D3 = dominant_signed(d)
        D6 = dominant_signed(embed3(d))
        if not D3 == signed_from_observer(a, h):
            raise AssertionError('UNIT110_ALWAYS_ON_CHECK_03:line_98')
        if not D6 == frozenset(((SELECTED_AXES[i], sign) for i, sign in D3)):
            raise AssertionError('UNIT110_ALWAYS_ON_CHECK_04:line_99')
        if not dominant_signed(tuple((-x for x in d))) == frozenset(((i, -s) for i, s in D3)):
            raise AssertionError('UNIT110_ALWAYS_ON_CHECK_05:line_100')
        if not (D3 == legacy_positive_selector(a) if max(a) > 0 and 2 * h + max(a) > 0 or (max(a) == 0 and h == 0) else D3 != legacy_positive_selector(a)):
            raise AssertionError('UNIT110_ALWAYS_ON_CHECK_06:line_101')
        positive_guard_matches += D3 == legacy_positive_selector(a)
        zero_cases += d == (0, 0, 0)
        signed_ties += len(D3) > 1
        c3 = brc_shortest(d)
        c6 = brc_shortest(embed3(d))
        if not c3 == c6 == brc_shortest(tuple((-x for x in d))):
            raise AssertionError('UNIT110_ALWAYS_ON_CHECK_07:line_107')
        brc_samples += 1
        if module is not None:
            native_actual = module.shortest_path_multiplicity(embed3(d))
            if native_actual != c6:
                raise AssertionError(f'original signed BRC mismatch at {d}: {native_actual} != {c6}')
            imported_module_calls += 1
    if not dominant_signed((0, 0, 0)) == frozenset():
        raise AssertionError('UNIT110_ALWAYS_ON_CHECK_08:line_114')
    if not dominant_signed((0, 0, 0, 0, 0, 0)) == frozenset():
        raise AssertionError('UNIT110_ALWAYS_ON_CHECK_09:line_115')
    if not signed_from_observer((0, 2, 4), -2) == frozenset({(0, -1), (2, 1)}):
        raise AssertionError('UNIT110_ALWAYS_ON_CHECK_10:line_116')
    a = (0, 1, 4)
    if not brc_shortest(tuple((x - 2 for x in a))) == 30:
        raise AssertionError('UNIT110_ALWAYS_ON_CHECK_11:line_118')
    if not brc_shortest(a) == 5:
        raise AssertionError('UNIT110_ALWAYS_ON_CHECK_12:line_119')
    if not minzero(tuple((x - 2 for x in a)))[0] == minzero(a)[0]:
        raise AssertionError('UNIT110_ALWAYS_ON_CHECK_13:line_120')
    print(json.dumps({'status': 'PASS', 'signed_points': signed_points, 'signed_ties': signed_ties, 'zero_cases': zero_cases, 'legacy_selector_agreement': positive_guard_matches, 'three_axis_embedding': list(SELECTED_AXES), 'brc_shortest_formula_checks': brc_samples, 'existing_native_brc_imported': module is not None, 'existing_native_brc_calls': imported_module_calls, 'LP011_status': 'bounded proposed typed consumer; historical original caller not located'}, sort_keys=True))
if __name__ == '__main__':
    main()
