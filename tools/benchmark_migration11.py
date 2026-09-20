#!/usr/bin/env python3
"""Finite full-population readout comparison; no new cell algorithm or speed claim."""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
from nollm_visual_toolkit import multiplicative as m
p=ROOT/'tools/nollm_visual_toolkit/tests/test_multiplicative_readouts.py'
spec=importlib.util.spec_from_file_location('m11_benchmark_helpers',p)
t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)

def digest(value):return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=ROOT/'evidence/migration11/populations.json')
    args=parser.parse_args();old=t.old_module();records=[]
    cases=[(4096,mode,n,d) for mode in ('valuation','mixed','spiral','radial')
           for n,d in ((1,2),(1,1),(3,2))]+[(65536,'valuation',1,1)]
    for count,scheme,n,d in cases:
        f=m.build_field(m.config(count,scheme),cell_scale=(n,d))
        before=old.statistics(f)
        with t.poison_float_math():after=m.statistics(f)
        js=t.node('(()=>{const {fibers,...s}=MulExactReadouts.stats(input);return s;})()',t.transport(f))
        assert after==js
        keys=('population','positive_population','prime_count','rings','sectors','grid','distinct_phases',
              'occupied_hex_centers','occupied_hex_centers_bounds','collision_groups',
              'extra_identities_at_shared_centers','largest_fiber','unresolved_cell_identities')
        assert all(after[k]==before[k] for k in keys)
        assert f['cell_membership_exact']['status']=='CERTIFIED_ALL'
        row={'count':count,'scheme':scheme,'cell_scale':[str(n),str(d)],
             'phase_source_sha256':f['cell_membership_exact']['phase_source_sha256'],
             'full_python_node_statistic_equal':True,'all_prior_integer_fields_equal':True,
             'certified_identities':f['cell_membership_exact']['certified_identities'],
             'statistics_sha256':digest(after),'statistics':after}
        records.append(row)
        print(f'PASS {count} {scheme} {n}/{d} cells={after["occupied_hex_centers"]}',flush=True)
    record={'schema':'M11_FINITE_POPULATIONS_V1','cases':len(records),'records':records,
            'scope':'Actual Python field and frozen M10 browser readout functions; no browser build/DOM execution; finite not universal'}
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(record,indent=2)+'\n')
if __name__=='__main__':main()
