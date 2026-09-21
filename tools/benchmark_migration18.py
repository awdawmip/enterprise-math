#!/usr/bin/env python3
"""Finite real Phase32 machine CLI versus frozen M17 exact observations."""
from __future__ import annotations
import argparse,contextlib,hashlib,importlib.util,io,json,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
from nollm_visual_toolkit import phase32_lab as m,core
spec=importlib.util.spec_from_file_location('nollm_visual_toolkit._m18_frozen',ROOT/'evidence/migration18/frozen_m17_phase32_lab.py')
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)

def digest(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def no_float(obj):
    if type(obj) is float:return False
    if isinstance(obj,dict):return all(no_float(v) for v in obj.values())
    if isinstance(obj,(list,tuple)):return all(no_float(v) for v in obj)
    return True

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--count',type=int,default=4096)
    p.add_argument('--mode',choices=['golden','hash','spiral'],default='golden')
    p.add_argument('--pitches',nargs='+',default=['0.50','1','3/2'])
    p.add_argument('--out',type=Path)
    args=p.parse_args();rows=[]
    out=args.out or ROOT/f'evidence/migration18/population_{args.count}_{args.mode}.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    for text in args.pitches:
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);report_path=root/'r.json';data_path=root/'d.json';config_path=root/'c.json'
            config=m.machine_config(args.count,args.mode)
            config_path.write_text(json.dumps(config))
            argv=sys.argv
            try:
                sys.argv=['phase32_lab','--machine-only','--config',str(config_path),'--cell-pitch',text,
                          '--report',str(report_path),'--hex-data',str(data_path)]
                with contextlib.redirect_stdout(io.StringIO()):
                    if m.main()!=0:raise AssertionError('machine CLI failed')
            finally:sys.argv=argv
            report=json.loads(report_path.read_text());data=core.read_data(data_path)
            pair=tuple(int(report['cell_pitch_source'][k]) for k in ('numerator','denominator'))
            legacy_cfg={k:v for k,v in config.items() if k!='schema'}
            frozen=old.build(legacy_cfg,cell_pitch=pair)
            new=m.build(config,cell_pitch=pair,include_display=False)
            population=frozen['cell_membership_exact']
            checks={
                'complete_certificates_match':new['cell_membership_exact']==population,
                'summary_match':report['cell_membership_exact']=={k:v for k,v in population.items() if k!='certificates'},
                'metrics_match':report['metrics']==old.metrics(frozen),
                'multiplication_match':report['multiplication']==old.multiplication(frozen,config['a'],config['b']),
                'all_identity_records_match':data['records']==old.hex_data(frozen)['records'],
                'phases_and_factor_states_match':all(new[k]==frozen[k] for k in ('phase','spf','omega','primes')),
                'report_and_export_float_free':no_float(report) and no_float(data),
                'literal_pitch_preserved':report['cell_pitch_source']['text']==text,
                'all_identities_retained':[r['id'] for r in data['records']]==[str(i) for i in range(args.count)],
                'source_config_preserved':report['config']==config,
            }
            if not all(checks.values()):raise AssertionError(checks)
            row=dict(count=args.count,mode=args.mode,pitch_text=text,
                     status=population['status'],occupied_positive_cells=population['occupied_cells'],
                     collision_excess=population['collision_excess'],unresolved=len(population['unresolved_identities']),
                     certificate_sha256=digest(population['certificates']),report_sha256=digest(report),
                     records_sha256=digest(data['records']),checks=checks)
            rows.append(row)
            out.write_text(json.dumps(dict(schema='M18_PHASE32_CLI_POPULATION_MATRIX_V1',rows=rows,
                finite_not_universal=True,comparison='actual machine CLI against unchanged M17 exact observations'),indent=2)+'\n')
            print(json.dumps(row),flush=True)
    return 0
if __name__=='__main__':raise SystemExit(main())
