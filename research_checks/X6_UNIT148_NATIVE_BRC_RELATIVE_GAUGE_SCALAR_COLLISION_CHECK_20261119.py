#!/usr/bin/env python3
"""Unit148: typed native X6 vs old three-coordinate min-zero observer.

Self-contained exact integer checker. Original frozen source module/benchmark is
not executed; its signed shortest-path formulas are independently recalculated.
Use plain CPython, -O, -OO; all substantive predicates are always-on checks.
"""
from __future__ import annotations
import json
from math import comb, factorial
from functools import lru_cache

FROZEN_NATIVE_BLOB = '300a96e3dc24bf6fff73743037a0347a8bc83176'
FROZEN_CELL_TORSOR_BLOB = 'b4d49a1bbcccad0521618c6d20f6dcfa242b420a'
HISTORIC_BRC_BRIDGE_BLOB = '6ec0d73a19e28ec586c59a97d24f5798c9119771'
CURRENT_BRC_BRIDGE_BLOB = '97ab1403ab04b4fa80034625fb1b2e3ed115e59b'

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def native(z):
    require(len(z) == 6 and all(type(c) is int for c in z), 'six signed integers')
    n = sum(map(abs, z))
    b = factorial(n)
    for v in z:
        b //= factorial(abs(v))
    return (sum(x*x for x in z), n, b)

def can3(d):
    h = min(d)
    return tuple(x-h for x in d)

@lru_cache(None)
def dp_words(i, j):
    if i == j == 0: return 1
    return (dp_words(i-1,j) if i else 0) + (dp_words(i,j-1) if j else 0)

def run():
    checked = 0
    equality = []
    max_brc = 0
    for b in range(1,65):
        for a in range(1,b+1):
            d = (-a,-b,0,0,0,0)
            r = can3(d[:3]) + (0,0,0)
            old = native(d)
            new = native(r)
            require(r == (b-a,0,b,0,0,0), 'relative canonicalization')
            require(new[0]-old[0] == b*(b-2*a), 'squared native norm exact defect')
            require(new[1]-old[1] == b-2*a, 'shortest count exact defect')
            require((old[0] == new[0]) == (b == 2*a), 'norm iff')
            require((old[1] == new[1]) == (b == 2*a), 'length iff')
            require(old[2] == comb(a+b,a), 'native multinomial')
            require(new[2] == comb(2*b-a,b-a), 'relative multinomial')
            if a <= 8 and b <= 16:
                require(old[2] == dp_words(a,b), 'independent DP of signed shortest words')
                require(new[2] == dp_words(b-a,b), 'independent DP of positive words')
            if b == 2*a:
                require(old == new == (5*a*a,3*a,comb(3*a,a)), 'simultaneous scalar collision')
                e0 = (1,0,0,0,0,0)
                d1 = tuple(x+y for x,y in zip(d,e0))
                r1 = tuple(x+y for x,y in zip(r,e0))
                require(native(r1)[0]-native(d1)[0] == 4*a, 'native operation squared norm wake')
                require(native(r1)[1]-native(d1)[1] == 2, 'native operation shortest length wake')
                equality.append(a)
                max_brc = max(max_brc, old[2])
            checked += 1
    require(checked == 2080 and equality == list(range(1,33)), 'complete bounded triangular census')
    d=(-1,-2,0,0,0,0); r=can3(d[:3])+(0,0,0)
    return {
        'schema': 'ENTERPRISE_MATH_UNIT148_SIGNED_BRCSCALAR_COLLISION_CHECK_V1',
        'type': 'INDEPENDENT_EXACT_INTEGER_CHECKER_NOT_ORIGINAL_NATIVE_MODULE_RUN',
        'source_blobs': {'signed_brc': FROZEN_NATIVE_BLOB, 'native_torsor': FROZEN_CELL_TORSOR_BLOB,
                         'historical_brc_bridge': HISTORIC_BRC_BRIDGE_BLOB,
                         'current_brc_bridge': CURRENT_BRC_BRIDGE_BLOB},
        'integer_domain': '1<=a<=b<=64; d=(-a,-b,0,0,0,0), r=(b-a,0,b,0,0,0)',
        'pairs_checked': checked,
        'simultaneous_native_G_N_B_equality_pairs': len(equality),
        'equality_a_values': equality,
        'max_equal_nbrc': str(max_brc),
        'smallest': {'a':1, 'b':2, 'signed_native_d':list(d),'minzero_chart_r':list(r),
                     'G_N_B': list(native(d)),
                     'after_positive_first_axis': {'d':list((0,-2,0,0,0,0)),
                                                   'r':list((2,0,2,0,0,0)),
                                                   'G_N_B_d':list(native((0,-2,0,0,0,0))),
                                                   'G_N_B_r':list(native((2,0,2,0,0,0)))}},
        'formula': {'G_r_minus_G_d':'b*(b-2*a)', 'N_r_minus_N_d':'b-2*a',
                    'equal_iff':'b=2*a', 'G_after_e0_difference':'4*a',
                    'N_after_e0_difference':'2'},
        'status':'PASS_EXACT_INTEGER_FINITE_AUTHOR_CHECK_UNREVIEWED_NOT_ADMITTED',
    }

if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, ensure_ascii=False, separators=(',',':')))
