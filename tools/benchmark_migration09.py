#!/usr/bin/env python3
"""Actual rendered M09 engine vs M07 Python; finite tests, not complexity proof."""
from __future__ import annotations
import argparse,gc,hashlib,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
from nollm_visual_toolkit import multiplicative as m
spec=importlib.util.spec_from_file_location('m09_engine_helper',ROOT/'tools/nollm_visual_toolkit/tests/test_multiplicative_browser.py');helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)

def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()

def main():
    out=ROOT/'evidence/migration09';out.mkdir(parents=True,exist_ok=True)
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--full-only',action='store_true');args=parser.parse_args()
    rows=[]
    cases=[(4096,mode,s) for mode in ('valuation','mixed','spiral','radial') for s in ('1/2','1','3/2')]+[(65536,'valuation','1')]
    if args.full_only:cases=[(65536,'valuation','1')]
    for count,mode,text in cases:
        print('START',count,mode,text,flush=True)
        cfg=m.config(count,mode);pair,source=m.parse_cell_scale_text(text)
        js=helper.node('''const f=await MulExact.build(input.c,input.o);
            const stable=x=>x===null||typeof x!=='object'?JSON.stringify(x):Array.isArray(x)?'['+x.map(stable).join(',')+']':'{'+Object.keys(x).sort().map(k=>JSON.stringify(k)+':'+stable(x[k])).join(',')+'}';
            const hash=x=>require('crypto').createHash('sha256').update(stable(x)).digest('hex');
            return {summary:MulExact.summary(f),source:f.cell_scale_source,certificates_sha256:hash(f.cell_membership_exact.certificates),rows_sha256:hash(f.records.map(({ideal,...r})=>r))};''',{'c':cfg,'o':helper.options(text)})
        py=m.build_field(cfg,cell_scale=pair)
        psummary=m.cell_membership_summary(py)
        certs=digest(py['cell_membership_exact']['certificates'])
        identities=digest([{k:v for k,v in r.items() if k!='ideal'} for r in py['records']])
        equal=js['summary']==psummary and js['source']==source and js['certificates_sha256']==certs and js['rows_sha256']==identities
        if not equal:raise AssertionError((count,mode,text))
        row={'count':count,'scheme':mode,'scale_text':text,'summary_all_fields_equal':True,'ordered_certificates_sha256_equal':True,'ordered_identity_fields_sha256_equal':True,
             'certificates_sha256':certs,'rows_sha256':identities,'status':psummary['status'],'occupied_cells':psummary['occupied_cells'],'unresolved':len(psummary['unresolved_identities'])}
        rows.append(row);print(json.dumps(row),flush=True)
        del py,js;gc.collect()
    report={'schema':'M09_RENDERED_ENGINE_FINITE_MATRIX_V1','cases':rows,'case_count':len(rows),'scope':'full summaries and canonical ordered certificate/identity SHA256 comparison; no pixel equality or universal theorem; native Node crypto; browser DOM separate'}
    (out/('population_full.json' if args.full_only else 'population_matrix.json')).write_text(json.dumps(report,indent=2)+'\n')
if __name__=='__main__':main()
