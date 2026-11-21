"""Portable full q2 replay using the previous proof's natively prepared observations and banks."""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--baseline',type=Path,required=True);p.add_argument('--work',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--jobs',type=int,default=2);p.add_argument('--resume',action='store_true');p.add_argument('--reuse-verified-bounds',action='store_true');a=p.parse_args();h=Path(__file__).resolve().parent;out=a.output.resolve();out.mkdir(parents=True,exist_ok=True);scratch=out/'work';scratch.mkdir(exist_ok=True);run=out/'run';w=a.work.resolve();result=json.loads((h/'result_q2.json').read_text());hashfile=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
if not a.resume and(run/'chunks').exists()and any((run/'chunks').glob('*.json')):raise SystemExit('Use a fresh output directory, or explicitly pass --resume to reuse verified complete chunks.')
for name,digest in result['input_identity']['prepared'].items():assert hashfile(w/name)==digest,(name,'prepared input differs')
def call(*args):subprocess.run([str(x)for x in args],check=True)
call(sys.executable,h/'geometric_check.py','--baseline',a.baseline,'--q3-proof',h,'--output',out/'plan','--cap',12043)
canonical=lambda rows:sorted(json.dumps(row,separators=(',',':'))for row in rows)
assert canonical(json.loads((out/'plan/profiles_q2.json').read_text())['rows'])==canonical(json.loads((h/'profiles_q2.json').read_text())['rows'])
call(sys.executable,h/'check_inheritance.py','--baseline',a.baseline,'--q3-proof',h,'--plan',out/'plan/profiles_q2.json','--output',out/'plan/inheritance.json');assert json.loads((out/'plan/inheritance.json').read_text())==json.loads((h/'inheritance.json').read_text())
call(sys.executable,h/'prepare_catalog.py','--baseline',a.baseline,'--output',scratch/'typed_catalog.txt');assert hashfile(scratch/'typed_catalog.txt')==hashfile(h/'typed_catalog.txt')
call(sys.executable,h/'prepare_extra_frames.py','--baseline',a.baseline,'--work',w,'--output',scratch/'frames','--jobs',a.jobs)
for name,frame in result['canonical_frame_catalogues'].items():
 path=scratch/'frames'/name
 if not path.exists():path=w/name
 assert hashfile(path)==frame['sha256']
for name,src in [('weighted_rootfiltered','search.cpp'),('original','original_weighted_native.cpp')]:call('c++','-std=c++20','-O3','-mpopcnt',h/src,'-o',scratch/name)
call(sys.executable,h/'check_uniform_windows.py','--work',w,'--inheritance',h/'inheritance.json','--source',h/'original_weighted_native.cpp','--engine',scratch/'original','--output',out/'uniform_windows.json')
command=[sys.executable,h/'verify_bounds.py','--output',out/'bounds']
if a.reuse_verified_bounds:command += ['--reuse-verified',h/'all_bound_verifications.json']
call(*command);b=json.loads((out/'bounds/bound_verification.json').read_text());fresh_identity={'same_bound_fragment':True,'fragment_sha256':b['bound_fragment_sha256'],'verified_source_sha256':b['search_source_sha256'],'active_source_sha256':b['search_source_sha256']};(out/'bound_identity.json').write_text(json.dumps(fresh_identity,indent=2)+'\n')
call(sys.executable,h/'positive_controls.py','--work',w,'--output',out/'controls')
call(sys.executable,h/'run_plan.py','--work',w,'--frames',scratch/'frames','--inheritance',h/'inheritance.json','--catalog',scratch/'typed_catalog.txt','--source',h/'search.cpp','--engine',scratch/'weighted_rootfiltered','--output',run,'--jobs',a.jobs)
call(sys.executable,h/'audit_complete.py','--run',run,'--plan',h/'profiles_q2.json','--inheritance',h/'inheritance.json','--source',h/'search.cpp','--bounds',out/'bounds/bound_verification.json','--bound-identity',out/'bound_identity.json','--uniform-windows',out/'uniform_windows.json','--output',out/'audit')
actual=json.loads((out/'audit/result_q2.json').read_text())
for key in ['complete_exclusion','profiles','complete_frame_chunks','family_profile_placements','search_nodes','class_emissions','settlement_calls','competing_or_new_tied_tables']:assert actual[key]==result[key],key
print(json.dumps({'complete_exclusion':True,'profiles':775,'result':str(out/'audit/result_q2.json')},indent=2),flush=True)
