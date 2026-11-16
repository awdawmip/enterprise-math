#!/usr/bin/env python3
"""X6 unit62: run the original frozen signed_brc against exact independently computed checks.

Invocation from repo root:
    python research_checks/X6_SIGNED_NATIVE_BRC_ORIGINAL_SOURCE_PLUS4_UNIT62_20261116.py
    python -O research_checks/X6_SIGNED_NATIVE_BRC_ORIGINAL_SOURCE_PLUS4_UNIT62_20261116.py

Source identity is guarded by the actual original Git blob, not by a path label.
The test deliberately uses explicit exceptions, never optimization-removed assertions.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from json import dumps
from math import factorial, isqrt, prod
from pathlib import Path
from subprocess import check_output

REPO = Path(__file__).resolve().parent.parent
SOURCE_REL = 'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py'
SOURCE = REPO / SOURCE_REL
BLOB = '300a96e3dc24bf6fff73743037a0347a8bc83176'


def require(condition: bool, message: str):
    if not condition:
        raise RuntimeError(message)


def source_producer():
    observed = check_output(['git', 'hash-object', str(SOURCE)], text=True).strip()
    require(observed == BLOB, f'FROZEN_BLOB_MISMATCH observed={observed} expected={BLOB}')
    spec = spec_from_file_location('x6_original_signed_brc', SOURCE)
    require(spec is not None and spec.loader is not None, 'FROZEN_IMPORT_SPEC_FAILED')
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def quadratic_sphere(g: int, dimensions: int = 6):
    def visit(remaining: int, slots: int, current: tuple[int, ...]):
        if slots == 0:
            if remaining == 0:
                yield current
            return
        radius = isqrt(remaining)
        for x in range(-radius, radius + 1):
            yield from visit(remaining-x*x, slots-1, current+(x,))
    yield from visit(g, dimensions, ())


def factor_ratio(t: int, pairs: int) -> int:
    return factorial(t+2*pairs)//factorial(t)


def plus4_coefficient(a: tuple[int, ...]) -> Fraction:
    # Configurations: two return-pairs on one axis; or one pair on each of two axes.
    return sum((Fraction(1, 2*(v+1)*(v+2)) for v in a), Fraction(0)) + sum(
        (Fraction(1, (a[i]+1)*(a[j]+1)) for i in range(len(a)) for j in range(i+1, len(a))),
        Fraction(0),
    )


def walks_at_length(m: int, dimension: int = 6):
    # Independent native signed-word recurrence, no calls into signed_brc.
    mass = {(0,)*dimension:1}
    for _ in range(m):
        following = defaultdict(int)
        for z, count in mass.items():
            for axis in range(dimension):
                for sign in (-1, 1):
                    q = list(z)
                    q[axis] += sign
                    following[tuple(q)] += count
        mass = following
    return mass


def run():
    original = source_producer()
    count_direct_words = 0
    for m in range(7):
        layer = walks_at_length(m)
        for z, count in layer.items():
            observed = original.endpoint_multiplicity(m, z)
            require(observed == count, f'DIRECT_WORD_RECURRENCE_FAIL m={m} z={z} actual={observed} expected={count}')
            count_direct_words += 1
        require(sum(layer.values()) == 12**m, f'DIRECT_WORD_TOTAL_FAIL m={m}')

    groups = defaultdict(lambda: {'points':0, 'shortest':0, 'plus2':0, 'plus4':0})
    weighted_checks = 0
    wp = (2,3,5,7,11,13)
    wm = (17,19,23,29,31,37)
    sample = None
    for z in quadratic_sphere(25):
        T = sum(abs(x) for x in z)
        a = tuple(abs(x) for x in z)
        s = sum(bool(x) for x in z)
        b0 = original.shortest_path_multiplicity(z)
        require(original.spatial_norm_squared(z) == 25, f'QUADRATIC_SPHERE_FAIL z={z}')
        require(original.endpoint_multiplicity(T, z) == b0, f'SHORTEST_NATIVE_FAIL z={z}')
        require(original.endpoint_multiplicity(T+1,z) == 0, f'PARITY_NATIVE_FAIL z={z}')
        b2 = original.endpoint_multiplicity(T+2,z)
        b4 = original.endpoint_multiplicity(T+4,z)
        independent2 = Fraction(b0 * factor_ratio(T,1)) * sum((Fraction(1,v+1) for v in a), Fraction(0))
        independent4 = Fraction(b0 * factor_ratio(T,2)) * plus4_coefficient(a)
        require(independent2.denominator == 1 and b2 == independent2.numerator, f'ONE_BACKTRACK_FAIL z={z}')
        require(independent4.denominator == 1 and b4 == independent4.numerator, f'TWO_BACKTRACK_FAIL z={z}')
        row = groups[(T,s)]
        row['points'] += 1
        row['shortest'] += b0
        row['plus2'] += b2
        row['plus4'] += b4
        if weighted_checks < 32:
            u = original.endpoint_weight(T+2,z,wp,wm)
            v = original.endpoint_weight(T+2,tuple(-x for x in z),wm,wp)
            require(u == v and u > 0, f'WEIGHT_SIGN_REVERSAL_FAIL z={z}')
            require(original.endpoint_weight(T+2,z,(1,)*6,(1,)*6) == b2, f'WEIGHT_UNIT_FAIL z={z}')
            require(original.endpoint_weight(T+1,z,wp,wm) == 0, f'WEIGHT_PARITY_FAIL z={z}')
            weighted_checks += 1
            if sample is None:
                sample = {'z': z, 'T': T, 'weighted_plus2_numerator': u.numerator, 'weighted_plus2_denominator': u.denominator}

    rows = [{'T':T,'support':s,**data} for (T,s),data in sorted(groups.items())]
    totals = {field:sum(row[field] for row in rows) for field in ('points','shortest','plus2','plus4')}
    require(totals['points'] == 7812, f'G25_POINT_COUNT_FAIL {totals}')
    require(totals['shortest'] == 2538954612, f'G25_SHORTEST_FAIL {totals}')
    require(totals['plus2'] == 939815793084, f'G25_PLUS2_FAIL {totals}')
    require(original.endpoint_multiplicity(9,(3,0,0,-4,0,0)) == 11214, 'MIXED_SIGN_WITNESS_FAIL')
    require(original.return_multiplicity(4) == 396, 'ORIGIN_RETURN_LENGTH4_FAIL')

    payload = {
        'schema':'X6_SIGNED_BRC_FROZEN_ORIGINAL_UNIT62_EXACT_V1',
        'observed_date':'2026-11-16',
        'parent_task':'RS-X6-LEGACY-PLANE-RECONCILIATION',
        'source_commit':'59538f585d037d09ef687b28715c4bc1a3f9fe03',
        'source_path':SOURCE_REL,
        'source_git_blob_sha1':BLOB,
        'G':25,
        'direct_six_axis_walk_recurrence_state_comparisons':count_direct_words,
        'rows':rows,
        'totals':totals,
        'weighted_sign_reversal_tests':weighted_checks,
        'origin_return_length4':396,
        'mixed_sign_witness':{'z':[3,0,0,-4,0,0], 'T':7, 'plus2':11214},
        'weighted_sample':sample,
        'evidence_status':'FROZEN_SOURCE_IMPORTED_AND_EXECUTED/AUTHOR-EXACT/UNREVIEWED/NOT_ADMITTED',
    }
    result = REPO / 'research_checks' / 'X6_SIGNED_NATIVE_BRC_ORIGINAL_SOURCE_PLUS4_UNIT62_RESULTS_20261116.json'
    result.write_text(dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + '\n',encoding='utf-8')
    print('PASS', dumps({'source_git_blob_sha1':BLOB,'totals':totals,'direct_walk_comparisons':count_direct_words,'weighted_checks':weighted_checks,'result_sha256':sha256(result.read_bytes()).hexdigest()},sort_keys=True))


if __name__=='__main__':
    run()
