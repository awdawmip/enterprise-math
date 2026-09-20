#!/usr/bin/env python3
"""Finite actual Phase32 caller comparisons; timings are telemetry, not evidence of complexity."""
from __future__ import annotations
import json,time,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
from nollm_visual_toolkit import phase32_lab as m

def one(count,mode,n,d):
    cfg=dict(count=count,mode=mode,pitch=n/d)
    legacy=m.build(cfg);exact=m.build(cfg,cell_pitch=(n,d))
    old_stats=m.metrics(legacy);exact_stats=m.metrics(exact)
    differences=[];total_diff=0
    for i,cert in enumerate(exact['cell_membership_exact']['certificates']):
        old_cell=m.quantize(m.position(legacy,i),n/d)
        new_cell=None if cert['cell'] is None else tuple(map(int,cert['cell']))
        if old_cell!=new_cell:
            total_diff+=1
            if len(differences)<20:differences.append({'n':i,'legacy':old_cell,'exact':new_cell,'status':cert['status']})
    return {'count':count,'mode':mode,'pitch':[n,d],'status':exact['cell_membership_exact']['status'],
            'unresolved':len(exact['cell_membership_exact']['unresolved_identities']),
            'ties':len(exact['cell_membership_exact']['tie_identities']),
            'legacy':{k:old_stats[k] for k in ('occupied_cells','collision_excess','max_cell_multiplicity')},
            'exact':{k:exact_stats[k] for k in ('occupied_cells','collision_excess','max_cell_multiplicity')},
            'aggregate_match':all(old_stats[k]==exact_stats[k] for k in ('occupied_cells','collision_excess','max_cell_multiplicity')),
            'identity_cell_difference_count':total_diff,'first_differences':differences,
            'precision_counts':exact['cell_membership_exact']['precision_counts']}

def main():
    import argparse
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--part',choices=('4096','65536','all'),default='all');a=p.parse_args()
    out=ROOT/'evidence/migration17';out.mkdir(parents=True,exist_ok=True)
    if a.part in ('4096','all'):
        rows=[]
        for mode in ('golden','hash','spiral'):
            for n,d in ((1,2),(1,1),(3,2)):
                rows.append(one(4096,mode,n,d))
        record={'schema':'M17_PHASE32_ACTUAL_4096_V1','rows':rows,
                'all_certified':all(r['status']=='CERTIFIED_ALL' for r in rows),
                'all_aggregate_match':all(r['aggregate_match'] for r in rows),
                'all_identity_cells_match':all(r['identity_cell_difference_count']==0 for r in rows),
                'finite_not_universal':True}
        (out/'population_4096.json').write_text(json.dumps(record,indent=2)+'\n')
        print(json.dumps({'part':'4096','rows':len(rows),'all_certified':record['all_certified'],'all_aggregate_match':record['all_aggregate_match'],'all_identity_cells_match':record['all_identity_cells_match']},indent=2),flush=True)
    if a.part in ('65536','all'):
        full=one(65536,'golden',1,1)
        record={'schema':'M17_PHASE32_ACTUAL_65536_V1','row':full,
                'certified':full['status']=='CERTIFIED_ALL','aggregate_match':full['aggregate_match'],
                'identity_cells_match':full['identity_cell_difference_count']==0,'finite_not_universal':True}
        (out/'population_65536.json').write_text(json.dumps(record,indent=2)+'\n')
        print(json.dumps({'part':'65536',**{k:full[k] for k in ('status','unresolved','ties','legacy','exact','aggregate_match','identity_cell_difference_count','precision_counts')}},indent=2),flush=True)
    return 0
if __name__=='__main__':raise SystemExit(main())
