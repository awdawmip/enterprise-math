#!/usr/bin/env python3
"""Exact signed-X6 2-support lift of frozen R063 C2 positive-chart image.

Uses only Python standard-library integer arithmetic. This is an independent
adapter/consumer check, NOT the unchanged original six-blob R063 benchmark.
"""
import hashlib
import json
from itertools import combinations, product
from math import comb, isqrt
from pathlib import Path


def target(r):
    r2 = r * r
    return tuple((a, b) for a in range(r + 1)
                 for b in [isqrt(r2 - a*a)] if b*b + a*a == r2)


def c2(r):
    found = set()
    for x in range(isqrt(r)+1):
        y2 = r-x*x
        y = isqrt(y2)
        if y*y != y2:
            continue
        a, b = abs(x*x-y*y), 2*x*y
        found.add((a,b))
        found.add((b,a))
    return tuple(sorted(found))


def signed_x6_image(roots):
    """Deduplicates native endpoints. Preserves separate axis/sign chart source."""
    native = {}
    sources = {}
    for i,j in combinations(range(6), 2):
        for si,sj in product((-1,1), repeat=2):
            for a,b in roots:
                z = [0]*6
                z[i], z[j] = si*a, sj*b
                z = tuple(z)
                value = comb(a+b,a)
                if z in native:
                    assert native[z] == value
                native[z] = value
                sources[z] = sources.get(z,0)+1
    return native, sources


def has_axis(r, roots):
    return (r,0) in roots and (0,r) in roots


def main():
    rows=[]
    digest=hashlib.sha256()
    for r in range(1,513):
        d=target(r)
        s=c2(r)
        assert set(s).issubset(d)
        full, fsrc=signed_x6_image(d)
        lift, lsrc=signed_x6_image(s)
        assert set(lift).issubset(full)
        assert all(full[z] == lift[z] for z in lift)
        axis=has_axis(r,s)
        assert ((r,0) in s) == ((0,r) in s)
        # At a selected native axis each of the other 5 axes and both unused
        # signs causes 10 source-labelled repeats; all 2-support words unique.
        assert all(n == (10 if sum(bool(v) for v in z)==1 else 1)
                   for z,n in fsrc.items())
        assert all(n == (10 if sum(bool(v) for v in z)==1 else 1)
                   for z,n in lsrc.items())
        d_mass=sum(comb(a+b,a) for a,b in d)
        c_mass=sum(comb(a+b,a) for a,b in s)
        full_formula=60*len(d)-108
        lift_formula=60*len(s)-108*int(axis)
        full_mass_formula=60*d_mass-108
        lift_mass_formula=60*c_mass-108*int(axis)
        assert len(full)==full_formula
        assert len(lift)==lift_formula
        assert sum(full.values())==full_mass_formula
        assert sum(lift.values())==lift_mass_formula
        # The missing endpoint and path masses are positive-integer residues.
        assert len(set(full)-set(lift))==full_formula-lift_formula
        assert sum(full[z] for z in full if z not in lift)==full_mass_formula-lift_mass_formula
        line={"r":r,"positive_target_roots":len(d),"c2_roots":len(s),
              "c2_axial_pair":axis,"signed_target_endpoints":len(full),
              "signed_c2_endpoints":len(lift),
              "signed_missing_endpoints":len(full)-len(lift),
              "signed_path_total":str(full_mass_formula),
              "signed_c2_path_total":str(lift_mass_formula),
              "signed_missing_path_mass":str(full_mass_formula-lift_mass_formula)}
        digest.update((json.dumps(line,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode('utf-8'))
        rows.append(line)
    r50=rows[49]
    assert r50['positive_target_roots']==6
    assert r50['c2_roots']==4
    assert r50['signed_target_endpoints']==252
    assert r50['signed_c2_endpoints']==132
    assert r50['signed_missing_endpoints']==120
    assert r50['signed_path_total']=='6641732296455342852372'
    assert r50['signed_c2_path_total']=='3489478121997012'
    assert r50['signed_missing_path_mass']=='6641728806977220855360'
    assert rows[4]['c2_axial_pair'] is False  # r=5 loses native axes
    assert rows[4]['signed_missing_endpoints']==12
    summary={"schema":"X6_R063_C2_SIGNED_PAIR_LIFT_512_V1",
             "scope":"frozen R063 C2 selected positive two-axis chart lifted to 60 signed labelled charts of P000 V5; dedup native endpoints",
             "status":"AUTHOR_EXACT_LOCAL_EXECUTED_UNREVIEWED_NOT_ADMITTED",
             "radii_checked":512,
             "row_sha256_sorted_jsonl":digest.hexdigest(),
             "r5":rows[4],"r50":r50,
             "missing_endpoint_total_across_all_r":sum(r['signed_missing_endpoints'] for r in rows),
             "c2_fully_covers_signed_pair_shell_radii":sum(x['signed_missing_endpoints']==0 for x in rows),
             "all_radii_sums_of_missing_path_masses":str(sum(int(x['signed_missing_path_mass']) for x in rows)),
             "algorithm":"independent integer isqrt input/target enumeration; direct 60 signed chart endpoint mapping; exact binomial BRC; symbol-by-symbol endpoint and source multiplicity verification"}
    dest=Path('/mnt/data/X6_R063_C2_SIGNED_PAIR_LIFT_512_RESULTS_20261115_2300.json')
    dest.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('PASS_X6_R063_C2_SIGNED_PAIR_LIFT_512')
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
