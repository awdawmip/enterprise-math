#!/usr/bin/env python3
"""Finite M06 compatibility matrices and tie-policy audit; timings are telemetry."""
from __future__ import annotations
import importlib.util, json, sys, time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
from nollm_visual_toolkit import multiplicative as m
from nollm_visual_toolkit.certified_hex import certified_population


def frozen():
    path=ROOT/'evidence/migration06/frozen_multiplicative.py'
    spec=importlib.util.spec_from_file_location('m06_bench_frozen',path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod

OLD=frozen()


def aggregates(field, module):
    s=module.statistics(field)
    return dict(occupied=s['occupied_hex_centers'], collisions=s['collision_groups'],
                excess=s['extra_identities_at_shared_centers'], max_load=s['largest_fiber'])


def matrix4096():
    rows=[]
    for scheme in ('valuation','mixed','spiral','radial'):
        for num,den in ((1,2),(1,1),(3,2)):
            cfg=m.config(4096,scheme,scale=num/den)
            old=OLD.build_field(OLD.config(4096,scheme,scale=num/den))
            exact=m.build_field(cfg,cell_scale=(num,den))
            old_agg=aggregates(old,OLD); new_agg=aggregates(exact,m)
            diffs=[r['n'] for r,o in zip(exact['records'],old['records']) if r['coord']!=o['coord']]
            rows.append({'count':4096,'scheme':scheme,'scale':[num,den],
                         'status':exact['cell_membership_exact']['status'],
                         'ties':len(exact['cell_membership_exact']['tie_identities']),
                         'unresolved':len(exact['cell_membership_exact']['unresolved_identities']),
                         'aggregate_match':old_agg==new_agg,'old':old_agg,'exact':new_agg,
                         'individual_cell_difference_count':len(diffs),'first_differences':diffs[:20]})
    return {'schema':'M06_MATRIX4096_V1','rows':rows,
            'all_certified':all(r['status']=='CERTIFIED_ALL' for r in rows),
            'all_aggregate_match':all(r['aggregate_match'] for r in rows),
            'finite_not_universal':True}


def full65536():
    cfg=m.config(65536,'valuation',scale=1)
    t=time.perf_counter();old=OLD.build_field(OLD.config(65536,'valuation',scale=1));old_s=time.perf_counter()-t
    t=time.perf_counter();exact=m.build_field(cfg,cell_scale=(1,1));exact_s=time.perf_counter()-t
    a=aggregates(old,OLD);b=aggregates(exact,m)
    diffs=sum(r['coord']!=o['coord'] for r,o in zip(exact['records'],old['records']))
    return {'schema':'M06_FULL65536_V1','count':65536,'scheme':'valuation','scale':[1,1],
            'status':exact['cell_membership_exact']['status'],
            'ties':len(exact['cell_membership_exact']['tie_identities']),
            'unresolved':len(exact['cell_membership_exact']['unresolved_identities']),
            'legacy':a,'exact':b,'aggregate_match':a==b,
            'individual_cell_difference_count':diffs,
            'timing_seconds_telemetry_only':{'legacy':old_s,'exact':exact_s}}


def tie_audit():
    ties=diffs=0;examples=[]
    ticks=(0,16384,32768,49152)
    for num,den in ((1,2),(1,1),(3,2)):
        for tick in ticks:
            phi=[None]+[tick]*512
            base=certified_population(phi,num,den,include_certificates=True)
            for n,c in enumerate(base['certificates']):
                if c['status']!='CERTIFIED_TIE':continue
                ties+=1
                adapted=m._lexicographic_tie_cell(c)
                if adapted!=c['cell']:
                    diffs+=1
                    if len(examples)<20:examples.append({'n':n,'tick':tick,'scale':[num,den],'base':c['cell'],'lexicographic':adapted})
    return {'schema':'M06_TIE_POLICY_AUDIT_V1','population_n_range':'0..511 per case','ticks':list(ticks),
            'scales':[[1,2],[1,1],[3,2]],'certified_ties':ties,
            'base_vs_legacy_lexicographic_differences':diffs,'examples':examples,
            'conclusion':'BASE_CERTIFIER_TIE_RULE_NOT_EQUIVALENT_TO_LEGACY_AXIAL_LEXICOGRAPHIC_TIE',
            'finite_not_exhaustive':True}


def main():
    out=ROOT/'evidence/migration06';out.mkdir(parents=True,exist_ok=True)
    records={'matrix4096.json':matrix4096(),'full65536.json':full65536(),'tie_policy_audit.json':tie_audit()}
    for name,obj in records.items():(out/name).write_text(json.dumps(obj,indent=2)+'\n')
    print(json.dumps({name:{k:v for k,v in obj.items() if k in ('schema','all_certified','all_aggregate_match','status','aggregate_match','unresolved','ties','certified_ties','base_vs_legacy_lexicographic_differences','individual_cell_difference_count')} for name,obj in records.items()},indent=2))
if __name__=='__main__':main()
