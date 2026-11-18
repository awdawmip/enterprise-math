#!/usr/bin/env python3
"""R762ET: exact short certificate for minimal eventual period/preperiod.
No floating point, no external packages; six original named BRC shifts.
Run: python3 R762ET_VERIFY.py
"""
import hashlib
import json

Q = 9
DIM = Q ** 3
MOD = 3 ** 7
BRANCHES = ((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))

def index(x, y, z):
    return ((x % Q) * Q + y % Q) * Q + z % Q

permutations = []
for dx,dy,dz in BRANCHES:
    permutations.append([index(x+dx,y+dy,z+dz)
                         for x in range(Q) for y in range(Q) for z in range(Q)])

coefficients = [0] * DIM
coefficients[0] = 1
shadows = {}
supports = {}
for n in range(27):
    expected = max(0, n//3 - 2)
    divisor = 3 ** expected
    assert all(v % divisor == 0 for v in coefficients), (n, 'lower-bound')
    shadow = bytes((v // divisor) % 3 for v in coefficients)
    assert any(shadow), (n, 'nonzero')
    assert sum(coefficients) % MOD == pow(6, n, MOD), (n, 'augmentation')
    shadows[n] = shadow
    supports[n] = sum(bool(v) for v in shadow)
    if n == 26:
        break
    updated = [0] * DIM
    for perm in permutations:
        for i, v in enumerate(coefficients):
            updated[perm[i]] = (updated[perm[i]] + v) % MOD
    coefficients = updated

assert shadows[8] == shadows[26], 'new boundary period fails'
assert shadows[7] != shadows[25], 'transient witness fails'
assert shadows[7][0] == 1 and shadows[25][0] == 0
assert supports[9] == 27
assert all(supports[n] != 27 for n in range(10,27)), 'period distinctness'
assert supports[7] == 108 and supports[25] == 450
assert supports[8] == supports[26] == 324

result = {
    'schema':'R762ET_EXACT_TRANSIENT_PERIOD_CERTIFICATE_V1',
    'model':'P=1+X+Z+XY+YZ+XYZ in Z[(Z/9Z)^3]',
    'integer_arithmetic':'coefficients reduced mod 3^7=2187, sufficient for all f9(n)<=6 at n<=26',
    'checked_n':[0,26],
    'positions':DIM,
    'six_named_branches':BRANCHES,
    'lower_bound_sharp_and_augmentation_checks':27,
    'shadow_equal_8_26':True,
    'shadow_8_sha256':hashlib.sha256(shadows[8]).hexdigest(),
    'shadow_26_sha256':hashlib.sha256(shadows[26]).hexdigest(),
    'shadow_7_sha256':hashlib.sha256(shadows[7]).hexdigest(),
    'shadow_25_sha256':hashlib.sha256(shadows[25]).hexdigest(),
    'shadow_7_vs_25_witness_linear_index':0,
    'shadow_7_vs_25_value_pair':[shadows[7][0], shadows[25][0]],
    'supports_n7_n8_n9_n25_n26':[supports[n] for n in (7,8,9,25,26)],
    'supports_n9_to_n26':[supports[n] for n in range(9,27)],
    'period_18_unique_support_27_at_n9':True,
    'global_theorem_dependencies':['R762ES recurrence proof for S9(n+18)=S9(n) at n>=9',
        'R762ER exact Frobenius factorization for q=9h',
        'R762ER all-horizon nonvanishing of normalized shadows'],
    'independent_mathematical_review':'NOT_REVIEWED',
    'result':'PASS'
}
print(json.dumps(result,ensure_ascii=False,indent=2))
