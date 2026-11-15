#!/usr/bin/env python3
"""Exact universal signed-X6 support obstruction witnesses, 1 <= r <= 512.

Theorem proof is in separate research note. Finite execution demonstrates the
constructive witness and checks r<=6 by independent direct signed shell enumeration.
This is NOT the original frozen R063 Stage0 six-source native benchmark.
"""
import hashlib
import json
from functools import lru_cache
from math import comb, isqrt
from pathlib import Path

MAX_R = 512
OUTPUT = Path(__file__).with_name('X6_R063_ALL_RADII_SIGNED_SUPPORT_OBSTRUCTION_RESULTS_20261116_0230.json')

@lru_cache(None)
def four_square_decomp(n):
    limit = isqrt(n)
    sums = {}
    for c in range(limit + 1):
        for d in range(limit + 1):
            sums.setdefault(c*c + d*d, []).append((c,d))
    for a in range(limit + 1):
        for b in range(limit + 1):
            rest = n-a*a-b*b
            if rest not in sums:
                continue
            for c,d in sums[rest]:
                if sum(v > 0 for v in (a,b,c,d)) >= 2:
                    return (a,b,c,d)
    raise ArithmeticError(f'No decomposition with two positive entries for n={n}')


def witness(r):
    if r == 1:
        return (1,0,0,0,0,0)
    if r % 2 == 0:
        k = r//2
        return (k,k,k,k,0,0)
    a,b,c,d = four_square_decomp(r-1)
    return (r-2, 2*a, 2*b, 2*c, 2*d, 0)


def brc(z):
    total = sum(abs(c) for c in z)
    ans = 1
    remain = total
    for c in z:
        ans *= comb(remain, abs(c))
        remain -= abs(c)
    assert remain == 0
    return ans


def lower_bound(z):
    s = sum(c != 0 for c in z)
    return comb(6, s)*(2**s)*brc(z)


def signed_shell(r):
    # Exact independent direct named signed-axis enumeration, only r <= 6.
    sq = r*r
    choices = range(-r,r+1)
    out=[]
    def walk(prefix, remaining):
        if len(prefix) == 6:
            if remaining == 0:
                out.append(tuple(prefix))
            return
        for k in choices:
            if k*k <= remaining:
                prefix.append(k)
                walk(prefix, remaining-k*k)
                prefix.pop()
    walk([],sq)
    return out

rows = []
for r in range(1, MAX_R+1):
    z = witness(r)
    s = sum(q != 0 for q in z)
    assert sum(q*q for q in z) == r*r
    assert (r == 1 and s == 1) or (r >= 2 and s >= 3)
    lb = lower_bound(z) if r>=2 else 0
    rows.append({'r':r,'witness_z':list(z),'support':s,'path_length':sum(z),'one_endpoint_brc':str(brc(z)),
                 'signed_placement_endpoint_lower_bound': comb(6,s)*2**s,
                 'signed_placement_brc_lower_bound':str(lb)})

small=[]
for r in range(1,7):
    shell=signed_shell(r)
    two=[z for z in shell if sum(x != 0 for x in z)<=2]
    complement=[z for z in shell if sum(x != 0 for x in z)>=3]
    all_mass=sum(brc(z) for z in shell)
    missing_mass=sum(brc(z) for z in complement)
    lower=int(rows[r-1]['signed_placement_brc_lower_bound'])
    assert missing_mass >= lower
    if r == 1:
        assert not complement
    if r == 2:
        assert len(shell)==252 and len(complement)==240 and missing_mass==5760 and lower==5760
    small.append({'r':r,'signed_endpoints':len(shell),'two_axis_endpoints':len(two),
                  'more_than_two_axis_endpoints':len(complement),
                  'full_signed_brc_mass':str(all_mass),
                  'missing_brc_mass':str(missing_mass),
                  'construction_lower_bound':str(lower)})

payload={'schema':'X6_R063_ALL_RADII_SIGNED_SUPPORT_OBSTRUCTION_V1',
         'claim':'Pair-sourced fixed-two-axis R063 construction equals all signed X6 norm-r shell endpoints iff r=1; for every integer r>=2 an explicit support>=3 witness exists.',
         'scientific_input':'awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03; signed Cell-relative X6 and natural path BRC',
         'checked_r_range':[1,MAX_R], 'row_count':len(rows),'rows':rows,
         'direct_independent_small_r':small,
         'original_native_r063_loader_executed':False,
         'verification':'AUTHOR_EXECUTED_NOT_INDEPENDENTLY_REVIEWED'}
compact=json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(',',':'))
OUTPUT.write_text(json.dumps(payload,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
summary={'rows':len(rows),'radius_max':MAX_R,'odd_count':sum(r['r']%2 for r in rows),
         'min_support_r_ge_2':min(r['support'] for r in rows[1:]),
         'max_support':max(r['support'] for r in rows),
         'rows_canonical_json_sha256':hashlib.sha256(json.dumps(rows,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
         'full_payload_canonical_json_sha256':hashlib.sha256(compact.encode()).hexdigest(),
         'small_cases':small}
print(json.dumps(summary,ensure_ascii=False,indent=2))
print('PASS_X6_R063_UNIVERSAL_SIGNED_SUPPORT_OBSTRUCTION')
