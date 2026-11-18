#!/usr/bin/env python3
"""Unit117: exact count for existing LP028 native validation callsites and CPython -O elision.

Standalone source-pattern control experiment; not an original-module integration run.
The source manifest and exact line classifications are in accompanying report.
"""
import hashlib
import json
from collections import Counter
from math import isqrt


def positive_square_roots(r):
    return [(a, isqrt(r*r-a*a)) for a in range(r+1)
            if isqrt(r*r-a*a)**2 == r*r-a*a]


def require(ok, msg):
    if not ok:
        raise RuntimeError(msg)

# This exact single-line AST idiom is used at source lines 80/81:
# assert shortest_path_multiplicity(delta) == mult
# assert endpoint_multiplicity(length,delta) == mult
# The original calls appear only in bare assert nodes in the audited file.
CONTROL = "def original_pattern(native):\n    assert native() == 1\n    return 'PASS'\n"
FIXED = "def fixed_pattern(native):\n    actual=native()\n    if actual != 1:\n        raise AssertionError('native mismatch')\n    return 'PASS'\n"


def run_pattern(code, optimization, bad=False):
    loc={}
    exec(compile(code, '<unit117-source-pattern>', 'exec', optimize=optimization), loc)
    calls=0
    def native():
        nonlocal calls
        calls += 1
        return 0 if bad else 1
    try:
        result = loc['original_pattern' if code is CONTROL else 'fixed_pattern'](native)
        return {'result':result,'calls':calls}
    except AssertionError:
        return {'result':'REJECTED','calls':calls}


def main():
    roots={r:len(positive_square_roots(r)) for r in range(1,129)}
    require(roots[50]==6, 'R063 positive roots r50')
    require(sum(roots.values())==398, 'positive R063 counts r1..128')
    expected_native_comparisons = 60 * (sum(roots.values()) + 2*roots[50])
    require(expected_native_comparisons==24600, 'original selected LP028 labelled charts r1..128 + two r50 starts')
    control={}
    for opt in (0,1,2):
        original_good=run_pattern(CONTROL,opt)
        original_bad=run_pattern(CONTROL,opt,True)
        fixed_good=run_pattern(FIXED,opt)
        fixed_bad=run_pattern(FIXED,opt,True)
        require(original_good=={'result':'PASS','calls':1 if opt==0 else 0},'original good')
        require(original_bad==({'result':'REJECTED','calls':1} if opt==0 else {'result':'PASS','calls':0}), 'original bad')
        require(fixed_good=={'result':'PASS','calls':1}, 'fixed good')
        require(fixed_bad=={'result':'REJECTED','calls':1}, 'fixed bad')
        control[str(opt)]={'original_good':original_good,'original_bad':original_bad,
                           'fixed_good':fixed_good,'fixed_bad':fixed_bad}
    result={
      'schema':'X6_UNIT117_SOURCE_PATTERN_EXACT_CERTIFICATE_V1',
      'date':'2026-11-18',
      'classification':'STANDALONE_CONTROL_EXECUTED; ORIGINAL_FULL_MODULE_THREE_MODE_NOT_EXECUTED_IN_THIS_UNIT',
      'original_lp028_consumer':'research_checks/X6_LP028_SIGNED_PATHSQRT_TYPED_CURRENT_CONSUMER_CHECK_20261112_2300.py',
      'original_source_blob_sha1':'db46dde5a962b93b65775bf2b4d8f52d5e3f83b9',
      'original_source_native_calls_inside_bare_assert':{
        'shortest_path_multiplicity':[80], 'endpoint_multiplicity':[81],
        'full_distance_squared':[78], 'spatial_norm_squared':[78]},
      'chart_root_distribution':dict(sorted(Counter(roots.values()).items())),
      'root_count_sum_r1_to128':sum(roots.values()),
      'root_count_r50':roots[50],
      'declared_chart_checks_r1_to128_plus_2_r50_starts':expected_native_comparisons,
      'source_control_test':control,
      'source_pattern_validation_optimized_native_calls':[1,0,0],
      'fixed_pattern_validation_optimized_native_calls':[1,1,1],
    }
    print(json.dumps(result,sort_keys=True,ensure_ascii=False,separators=(',',':')))


if __name__=='__main__': main()
