#!/usr/bin/env python3
"""Replay the new joint packing/completion lemmas and integer bias envelope."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
import argparse,json,os,subprocess,sys,time,struct
p=argparse.ArgumentParser();p.add_argument('--base',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
H=Path(__file__).resolve().parent;B=a.base.resolve();I=B/'inputs';O=a.output.resolve();O.mkdir(parents=True,exist_ok=True);st=time.monotonic();commands=[]
env={**os.environ,'PROBE_PREPARED':str(I),'PROBE_OUTPUT':str(O),'PROBE_PROOF':str(B),'PYTHONDONTWRITEBYTECODE':'1'}
def save(name,v):(O/name).write_text(json.dumps(v,indent=2)+'\n')
def run(cmd,name,inp=None):
 t=time.monotonic();r=subprocess.run([str(x)for x in cmd],input=inp,capture_output=True,text=True,env=env);(O/(name+'.stdout')).write_text(r.stdout);(O/(name+'.stderr')).write_text(r.stderr);commands.append({'name':name,'command':list(map(str,cmd)),'returncode':r.returncode,'seconds':time.monotonic()-t,'stdout_sha256':sha256(r.stdout.encode()).hexdigest(),'stderr_sha256':sha256(r.stderr.encode()).hexdigest()});assert r.returncode==0,(name,r.stderr[-2000:]);return r
bind=json.loads((H/'BASE_BINDINGS.json').read_text());assert all(sha256((B/f).read_bytes()).hexdigest()==v for f,v in bind['sha256'].items());assert all(sha256((I/f).read_bytes()).hexdigest()==v for f,v in bind['base_input_bindings'].items());assert json.loads((B/'verification/receipt.json').read_text())['complete']
families=json.loads((H/'cover_families.json').read_text());sources=sorted({x['source']for x in families}|{'cover_hlk.cpp'})
for source in sources:run(['g++','-std=c++20','-O3',H/source,'-o',O/Path(source).stem],'compile_'+Path(source).stem)
for name in ['union','frame','trace_spectra']:run(['g++','-std=c++20','-O3',B/(name+'.cpp'),'-o',O/name],'compile_'+name)
# Recover the native finite-frame universe, not only its reported row counts.
frames={}
for family in families:
 row=json.loads((H/family['receipt']).read_text())[0];name=Path(row['command'][4]).name;frames[name]=(len(family['E']),sum(family['E']))
frames['f4_49']=(4,49)
for name,(k,n)in sorted(frames.items()):
 u=run([O/'union',k,n,-1,'all'],'union_'+name,(I/'parent').read_text());f=run([O/'frame',I/'parent',I/'maps',k],'frame_'+name,u.stdout);expected=H/name if(H/name).exists()else I/name;assert{tuple(map(int,l.split()))for l in f.stdout.splitlines()}=={tuple(map(int,l.split()))for l in expected.read_text().splitlines()};(O/name).write_text(f.stdout)
# Native costs and legality used for positive controls and local sharpness witnesses.
raw=(I/'obs').read_bytes();pair=[int.from_bytes(raw[j:j+32],'little')for j in range(0,125*125*32,32)];mask125=(1<<125)-1;triples=[sum(1<<x for x in raw[j:j+3])for j in range(125*125*32,len(raw),3)];parents=[int(x)+(int(y)<<64)for x,y in map(str.split,(I/'parent').read_text().splitlines()[:250])]
def pts(m):return[x for x in range(125)if m>>x&1]
def cd(m):
 c=d=0;xs=pts(m)
 for x in xs:
  v=0
  for y in xs:v|=pair[125*x+y]
  c+=v.bit_count();d+=(v&mask125).bit_count()-(v>>125).bit_count()
 return c,d
def legal(m):return not any(t&m==t for t in triples)
def check_partition(ms):
 seen=0
 for m in ms:assert m and not m&seen and legal(m);seen|=m
 assert seen==mask125
# A 115-label control checks that the exact-one-K counter and unrestricted small
# classes admit a genuine native cover. It is not an eleven-label construction.
roots=list(struct.iter_unpack('<QQQ',(I/'B11').read_bytes()));controls=[]
(O/'empty_frame').write_text('\n')
for exe,cost,delta in [('cover_hl',1059,179),('cover_hlk',1126,114)]:
 root=next((l,h,c)for l,h,c in roots if c==cost and cd(l+(h<<64))==(cost,delta));prefix=O/(exe+'_control_B');Path(str(prefix)+'11').write_bytes(struct.pack('<QQQ',*root));cmd=[O/exe,I/'obs',I/'parent',prefix,O/'empty_frame',','.join(['1']*114+['11']),'','0',str(cost),'0','1','0','0',','.join(['0']*14),'1'];r=run(cmd,exe+'_positive_control');words=r.stdout.split();assert words[:2]==['hit','1'];ms=[int(x)+(int(y)<<64)for x,y in(map(int,w.split(':'))for w in words[2:])];check_partition(ms);assert len(ms)==115 and sum(cd(m)[0]for m in ms)==cost and sum(cd(m)[1]for m in ms)==delta;controls.append({'engine':exe,'labels':115,'cost':cost,'difference':delta,'checked':True})
save('positive_controls.json',controls)
# Joint packing tables: all complete 2-, 3-, and 4-mother frames, both directions.
new_mixed=[]
for source in sorted(H.glob('mixed_*_h*.py')):
 run([sys.executable,'-B',source],source.stem);result=source.stem+'_result.json';r=json.loads((O/result).read_text());old=json.loads((H/result).read_text());assert r['complete']and r['nodes']==old['nodes']and r['max_additional_142']==old['max_additional_142'];assert[(x['sign'],x['frame'],x['maximum_additional_142'],x['nodes'])for x in r['cases']]==[(x['sign'],x['frame'],x['maximum_additional_142'],x['nodes'])for x in old['cases']];new_mixed.append(result)
expected={2:[6,4,4,3,2,1,0],3:[4,4,2,2,0],4:[2,2,1,0]};witnesses=[];joint=[]
for full,values in expected.items():
 for high,low in enumerate(values):
  if(full,high)==(2,5):path=B/'verification/mixed_two_result.json'
  elif(full,high)==(3,4):path=B/'verification/mixed_packing_result.json'
  else:path=O/f'mixed_{ {2:"two",3:"three",4:"four"}[full]}_h{high}_result.json'
  z=json.loads(path.read_text());assert z['complete']and z['max_additional_142']==low;row=next(x for x in z['cases']if x['maximum_additional_142']==low)
  frame=[(0,j)for j,m in enumerate(parents)if not m&parents[0]][row['frame']]if full==2 else tuple(map(int,(I/f'f{full}_{13*full}').read_text().splitlines()[row['frame']].split()));used=0
  for j in frame:assert not used&parents[j];used|=parents[j]
  hm=list(map(int,row['witness_high']));lm=list(map(int,row['witness_142']));assert len(hm)==high and len(lm)==low
  for m,c,d in[(m,1059,179)for m in hm]+[(m,1042,142)for m in lm]:assert m.bit_count()==11 and not m&used and legal(m)and cd(m)==(c,row['sign']*d)and not any(m&p==m for p in parents);used|=m
  witnesses.append({'full_mothers':list(frame),'sign':row['sign'],'H':list(map(str,hm)),'L':list(map(str,lm))});joint.append({'full_mothers':full,'H_count':high,'maximum_L':low,'source':str(path),'source_sha256':sha256(path.read_bytes()).hexdigest()})
save('joint_table.json',joint);save('local_witnesses.json',witnesses)
# Full-cost completion exclusions, with no cost or difference restriction on small classes.
completed=[]
for f in families:
 rows=json.loads((H/f['receipt']).read_text());assert f['H_or_L']+len(f['small'])+len(f['E'])==11 and 11*f['H_or_L']+sum(f['small'])+sum(f['E'])==125
 for index,row in enumerate(rows):
  cmd=row['command'];cmd=[O/Path(f['source']).stem,I/'obs',I/'parent',I/'B',O/Path(cmd[4]).name]+cmd[5:];assert int(cmd[8])>=f['total_cost_upper_bound'];r=run(cmd,f['id']+'_'+str(index));counts=list(map(int,r.stderr.split()));assert counts==row['counts']and not r.stdout and counts[-1]==0;completed.append({'family':f['id'],'sign':row['sign'],'counts':counts,'complete':True})
for index,row in enumerate(json.loads((H/'hl5_k1_s10_e12_12_12_13_result.json').read_text())):
 cmd=row['command'];cmd=[O/'cover_hlk',I/'obs',I/'parent',I/'B',O/'f4_49']+cmd[5:];r=run(cmd,'hl5_k1_'+str(index));counts=list(map(int,r.stderr.split()));assert counts==row['counts']and not r.stdout and counts[-1]==0;completed.append({'family':'hl5_k1_s10_e12_12_12_13','sign':row['sign'],'counts':counts,'complete':True})
save('completion_receipts.json',completed)
# Integer-only envelope and all maximal-difference spectrum traces.
for source in ['signed_catalog.txt','packing_layer_bounds.txt']:(O/source).write_bytes((B/source).read_bytes())
(O/'cover_families.json').write_bytes((H/'cover_families.json').read_bytes());run([sys.executable,'-B',H/'exact_boundary.py'],'exact_boundary');r=json.loads((O/'exact_boundary_result.json').read_text());old=json.loads((H/'exact_boundary_result.json').read_text());assert r['certified_radius']==old['certified_radius']=='479/957'and r['remaining_pair']==[11771,1065]and r['excluded_pairs']==23
assert [(x['cost'],x['difference'],x['trace_sha256'],x['all_excluded'])for x in r['records']]==[(x['cost'],x['difference'],x['trace_sha256'],x['all_excluded'])for x in old['records']];assert sum(x['possible_in_signed_relaxation']for x in r['records'][-1]['cases'])==3;assert Fraction(12501-11292,1611-108)>Fraction(479,957)
result={'complete':True,'review_status':'NOT_REVIEWED','certified_radius':'479/957','closed_p_interval':['239/957','718/957'],'remaining_pair':[11771,1065],'remaining_necessary_spectra':3,'outer_endpoint_new_equality_unresolved':True,'new_excluded_pairs':23,'new_excluded_spectra':1943,'completion_families':25,'completion_nodes':sum(x['counts'][1]for x in completed),'new_joint_packing_nodes':sum(json.loads((O/f).read_text())['nodes']for f in new_mixed),'joint_table_maxima':expected,'base_audited_not_recomputed':True,'seconds':time.monotonic()-st,'commands':commands};save('receipt.json',result);print(json.dumps({k:v for k,v in result.items()if k!='commands'},indent=2))
