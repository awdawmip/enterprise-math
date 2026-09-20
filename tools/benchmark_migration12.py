#!/usr/bin/env python3
"""Finite M12 full-certificate equivalence; no performance/complexity claim."""
from __future__ import annotations
import argparse
import contextlib
import gc
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
from nollm_visual_toolkit import multiplicative as m


def hash_json(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def no_float(value):
    if isinstance(value,float):raise AssertionError('floating value in machine field')
    for child in (value.values() if isinstance(value,dict) else value if isinstance(value,(tuple,list)) else ()):
        no_float(child)


def run(count,scheme,scale):
    path=ROOT/'evidence/migration12/frozen_m11_multiplicative.py'
    spec=importlib.util.spec_from_file_location('nollm_visual_toolkit._m12_baseline',path)
    old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
    reference=old.build_field(old.config(count,scheme),cell_scale=scale)
    expected_cert_hash=hash_json(reference['cell_membership_exact'])
    expected_row_hash=hash_json([{k:v for k,v in r.items() if k!='ideal'} for r in reference['records']])
    expected_stats=old.statistics(reference)
    del reference;gc.collect()
    with contextlib.ExitStack() as stack:
        for name in ('sqrt','sin','cos','hypot','atan2','isfinite'):
            stack.enter_context(patch('math.'+name,side_effect=AssertionError('float '+name)))
        for name in ('_display_point','lattice_point','float','complex'):
            stack.enter_context(patch.object(m,name,side_effect=AssertionError('display '+name),create=True))
        field=m.build_field(m.machine_config(count,scheme),cell_scale=scale,include_display=False)
        actual_stats=m.statistics(field)
        no_float(field);no_float(actual_stats)
    certificate_sha256=hash_json(field['cell_membership_exact'])
    row_sha256=hash_json(field['records'])
    assert certificate_sha256==expected_cert_hash
    assert row_sha256==expected_row_hash
    assert actual_stats==expected_stats
    return {'count':count,'scheme':scheme,'scale':list(scale),
            'status':field['cell_membership_exact']['status'],
            'occupied_cells':actual_stats['occupied_hex_centers'],
            'unresolved':len(actual_stats['unresolved_cell_identities']),
            'full_certificate_sha256':certificate_sha256,'identity_record_sha256':row_sha256,
            'statistics_sha256':hash_json(actual_stats),
            'matches_frozen_m11_certificates_rows_and_statistics':True,
            'machine_state_has_no_floats':True,'display_functions_disabled_during_machine_build':True}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--count',type=int,default=4096)
    p.add_argument('--schemes',nargs='+',default=['valuation','mixed','spiral','radial'])
    p.add_argument('--scales',nargs='+',default=['1/2','1','3/2'])
    p.add_argument('--out',type=Path)
    args=p.parse_args()
    out=args.out or ROOT/'evidence/migration12'/f'population_{args.count}.json'
    scales=[m.parse_cell_scale_text(v)[0] for v in args.scales]
    rows=[]
    for mode in args.schemes:
        for scale in scales:
            row=run(args.count,mode,scale);rows.append(row)
            print(json.dumps({k:row[k] for k in ('count','scheme','scale','status','occupied_cells','unresolved')}),flush=True)
    record={'schema':'M12_MACHINE_POPULATION_COMPARISON_V1','rows':rows,
            'all_match':all(r['matches_frozen_m11_certificates_rows_and_statistics'] for r in rows),
            'finite_comparison_not_universal_theorem':True}
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(record,indent=2)+'\n')
    return 0
if __name__=='__main__':raise SystemExit(main())
