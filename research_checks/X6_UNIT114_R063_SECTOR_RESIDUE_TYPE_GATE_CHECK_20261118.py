#!/usr/bin/env python3
"""Unit114: source-pinned original R063 sector residue type-boundary regression.

Run from repo root, or pass --source path/to/original.py. No dependencies.
Checks an unchanged original Git blob; never patches or replaces its benchmark.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
import math
import pathlib
import sys

ORIGINAL = 'experiments/tool_discovery_native_geometry_of_numbers_minima_calculus_20260822.py'
PIN = '643b2bac659a445891dcb5588b647972977104e0'


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def strict_sector_residue(point, m):
    if type(m) is not int or m <= 0:
        raise ValueError('positive integer modulus required')
    if type(point) not in (tuple, list) or len(point) != 3:
        raise ValueError('triple required')
    if any(type(v) is not int for v in point):
        raise ValueError('exact integer coordinates required')
    a, b, c = point
    if a < 0 or b < 0 or c != 0:
        raise ValueError('only nonnegative fixed positive 2-generator chart (a,b,0)')
    return a % m, b % m


def strict_first_collision(points, m):
    seen = {}
    for p in points:
        q = strict_sector_residue(p, m)
        if q in seen:
            return seen[q], p, q
        seen[q] = p
    return None


def original_call(fn, *args):
    try:
        return {'kind':'VALUE','value':fn(*args)}
    except Exception as ex:
        return {'kind':'RAISED','exception':type(ex).__name__}


def run(source):
    content = source.read_bytes()
    blob = hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()
    require(blob == PIN, 'original Git blob mismatch')
    spec=importlib.util.spec_from_file_location('x6_original_r063_sector', source)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    optimized=sys.flags.optimize
    offplane=(1,0,1)
    good=(1,0,0)
    same_mod_signed=(-1,0,0)
    same_mod_positive=(2,0,0)
    bad_third=original_call(mod.residue,offplane,3)
    expected={'kind':'RAISED','exception':'AssertionError'} if optimized==0 else {'kind':'VALUE','value':(1,0)}
    require(bad_third==expected, 'off-plane optimized assert behavior changed')
    require(mod.residue(good,3)==(1,0),'valid chart residue mismatch')
    false_collision=original_call(mod.first_collision,[good,offplane],3)
    if optimized==0:
        require(false_collision=={'kind':'RAISED','exception':'AssertionError'},'expected original guard')
    else:
        require(false_collision=={'kind':'VALUE','value':(good,offplane,(1,0))},'expected cross-type alias')
    require(mod.residue(same_mod_signed,3)==mod.residue(same_mod_positive,3)==(2,0),
            'signed off-chart congruence witness mismatch')
    native_delta=[(list(good),list(offplane),1,2),
                  (list(same_mod_signed),list(same_mod_positive),1,2)]
    valid_cases=0
    for radius in range(0,10):
        pts=mod.sector_ball(radius)
        for modulus in range(2,21):
            for p in pts:
                require(mod.residue(p,modulus)==strict_sector_residue(p,modulus),
                        'valid chart comparison failed')
                valid_cases+=1
            require(mod.first_collision(pts,modulus)==strict_first_collision(pts,modulus),
                    'valid chart collision disagrees')
    invalid_cases=[((1,0,1),3),((1,0,-1),3),((-1,0,0),3),((0,-1,0),3),((True,0,0),3),((1.0,0,0),3),((0,0,0),0)]
    for point,modulus in invalid_cases:
        require(original_call(strict_sector_residue,point,modulus)=={'kind':'RAISED','exception':'ValueError'},
                'strict input gate failed')
    require(original_call(strict_first_collision,[good,offplane],3)=={'kind':'RAISED','exception':'ValueError'},
            'strict collision gate failed')
    result={
      'schema':'X6_UNIT114_R063_ORIGINAL_RESIDUE_TYPED_GATE_EXECUTION_V1',
      'original_source_path':ORIGINAL,
      'original_git_blob_sha1':blob,
      'optimization':optimized,
      'valid_chart_residue_checks':valid_cases,
      'valid_chart_collision_checks':10*19,
      'invalid_inputs_strict_rejected':len(invalid_cases),
      'original_offplane_result':bad_third,
      'original_offplane_collision':false_collision,
      'original_negative_signed_accepted':True,
      'signed_and_chart_native_length_witnesses':native_delta,
      'original_unchanged':True,
      'claims':'TYPE_BOUNDARY_REGRESSION_ONLY_NOT_R063_NATIVE_C3_C4_BENCHMARK'
    }
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,separators=(',',':')))


if __name__ == '__main__':
    args=sys.argv[1:]
    if args[:1]==['--source'] and len(args)==2:
        source=pathlib.Path(args[1])
    elif not args:
        source=pathlib.Path(ORIGINAL)
    else:
        raise SystemExit('usage: checker.py [--source exact_original.py]')
    run(source)
