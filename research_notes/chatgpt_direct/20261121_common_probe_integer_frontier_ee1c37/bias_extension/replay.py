#!/usr/bin/env python3
"""Replay the new finite lemmas and integer envelopes; audit inherited q2 receipts.
This is an author-team reproducibility program, not an independent review.
"""
from pathlib import Path
from fractions import Fraction
from hashlib import sha256
import argparse,json,os,subprocess,sys,time,importlib.util,struct
p=argparse.ArgumentParser();p.add_argument('--predecessor',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
H=Path(__file__).resolve().parent;I=H/'inputs';O=a.output.resolve();O.mkdir(parents=True,exist_ok=True);start=time.monotonic();receipts=[]
env={**os.environ,'PROBE_PREPARED':str(I),'PROBE_OUTPUT':str(O),'PYTHONDONTWRITEBYTECODE':'1'};os.environ.update(env)
def write(name,value): (O/name).write_text(json.dumps(value,indent=2)+'\n')
def run(cmd,name,stdin=None):
 t=time.monotonic();r=subprocess.run([str(x)for x in cmd],input=stdin,text=True,capture_output=True,env=env);(O/(name+'.stdout')).write_text(r.stdout);(O/(name+'.stderr')).write_text(r.stderr)
 q={'name':name,'command':[str(x)for x in cmd],'returncode':r.returncode,'seconds':time.monotonic()-t,'stdout_sha256':sha256(r.stdout.encode()).hexdigest(),'stderr_sha256':sha256(r.stderr.encode()).hexdigest()};receipts.append(q);assert r.returncode==0,(name,r.stderr[-3000:]);return r
bindings=json.loads((H/'INPUT_BINDINGS.json').read_text())
assert all(sha256((I/k).read_bytes()).hexdigest()==v for k,v in bindings['prepared'].items())
base=a.predecessor.resolve();r=run([sys.executable,'-B',base/'bias_q2/check_saved.py','--bundle',base/'bias_q2'],'inherited_q2_audit');q2=json.loads(r.stdout);assert q2['verified'] and q2['profiles']==775
sources=['menu_signed','packing_layers','trace_spectra','union','frame','seven_high_embedded','endpoint_11825','endpoint_11823','endpoint_11821_a','endpoint_11821_b']
for name in sources:run(['g++','-std=c++20','-O3',H/(name+'.cpp'),'-o',O/name],'compile_'+name)
# Replay the canonical finite-family reductions, not only their row counts.
frame_counts={}
for k,target in [(3,39),(4,49),(4,50),(4,52),(4,48),(3,38)]:
 name=f'f{k}_{target}';u=run([O/'union',k,target,-1,'all'],'union_'+name,(I/'parent').read_text());f=run([O/'frame',I/'parent',I/'maps',k],'frame_'+name,u.stdout)
 expected={tuple(map(int,l.split()))for l in (I/name).read_text().splitlines()};actual={tuple(map(int,l.split()))for l in f.stdout.splitlines()};assert expected==actual;frame_counts[name]=len(actual)
r=run([O/'menu_signed',I/'obs',I/'parent'],'native_signed_catalog');(O/'signed_catalog.txt').write_text(r.stdout)
assert r.stdout==(H/'signed_catalog.txt').read_text();signed={};typed={};entries=0
for line in r.stdout.splitlines():
 s,e,c,*ds=map(int,line.split());typed[s,e,c]=max(ds);signed.setdefault((s,c),set()).update(ds);entries+=len(ds)
old_typed={}
for line in (base/'integer_cuts/mother12/catalog.txt').read_text().splitlines():
 s,e,c,d=map(int,line.split())
 if e<2:old_typed[s,e,c]=d
assert typed==old_typed and len(typed)==2338 and entries==45146
# Full H and L translation pools; every emitted local witness is checked natively.
raw=(I/'obs').read_bytes();pair=[int.from_bytes(raw[j:j+32],'little')for j in range(0,125*125*32,32)];low=(1<<125)-1
parents=[int(x)+(int(y)<<64)for x,y in map(str.split,(I/'parent').read_text().splitlines()[:250])]
triples=[sum(1<<i for i in raw[j:j+3])for j in range(125*125*32,len(raw),3)]
def pts(m):return [j for j in range(125)if m>>j&1]
def cd(m):
 c=d=0;ids=pts(m)
 for x in ids:
  h=0
  for y in ids:h|=pair[125*x+y]
  c+=h.bit_count();d+=(h&low).bit_count()-(h>>125).bit_count()
 return c,d
def shift(i,x):return 25*((i//25+x//25)%5)+5*((i//5%5+x//5%5)%5)+(i%5+x%5)%5
banks={(c,s):set()for c in (1042,1059)for s in(-1,1)}
for l,h,c in struct.iter_unpack('<QQQ',(I/'B11').read_bytes()):
 if c not in(1042,1059):continue
 m=l+(h<<64);d=cd(m)[1]
 if abs(d)!={1042:142,1059:179}[c]:continue
 for x in range(125):banks[c,1 if d>0 else -1].add(sum(1<<shift(i,x)for i in pts(m)))
assert all(len(b)==(750 if c==1042 else 1500)for(c,s),b in banks.items())
def witness(core,masks,costs,sign):
 used=core
 for m,c in zip(masks,costs):
  assert m.bit_count()==11 and not used&m and cd(m)==(c,sign*{1042:142,1059:179}[c]);assert not any(t&m==t for t in triples);assert not any(m&p==m for p in parents);used|=m
 return [str(m)for m in masks]
local_witnesses=[];one=[]
for sign in(-1,1):
 rows=sorted(m for m in banks[1059,sign]if not m&parents[0]);name=f'one_mother_{sign}';path=O/(name+'.txt');path.write_text(str(len(rows))+'\n'+''.join(f'{m&((1<<64)-1)} {m>>64}\n'for m in rows))
 for target in(8,7):
  rr=json.loads(run([sys.executable,'-B',H/'pack_high.py',path,target],name+'_'+str(target)).stdout);assert rr['found']==(target==7);one.append({'sign':sign,**rr})
  if target==7:local_witnesses.append({'full_mothers':[0],'sign':sign,'high':witness(parents[0],list(map(int,rr['witness_masks'])),[1059]*7,sign),'mid':[]})
write('one_mother_result.json',one)
for script in ['packing_two_mothers.py','packing_three_mothers.py','packing_four_mothers.py','mixed_packing.py','mixed_two.py']:run([sys.executable,'-B',H/script],script[:-3])
for file,f,count in [('two_mothers_result.json',2,6),('three_mothers_result.json',3,4),('four_mothers_result.json',4,3)]:
 z=json.loads((O/file).read_text());assert z['complete'] and z['maximum']==count
 row=next(v for v in z['cases']if v['maximum']==count);frame=[0,row['second_mother']]if f==2 else list(map(int,(I/f'f{f}_{13*f}').read_text().splitlines()[row['frame']].split()));core=sum(parents[i]for i in frame)
 local_witnesses.append({'full_mothers':frame,'sign':row['sign'],'high':witness(core,list(map(int,row['witness'])),[1059]*count,row['sign']),'mid':[]})
for file,f,count in [('mixed_packing_result.json',3,0),('mixed_two_result.json',2,1)]:
 z=json.loads((O/file).read_text());assert z['complete'] and z['max_additional_142']==count
 row=next(v for v in z['cases']if v['maximum_additional_142']==count);frame=list(map(int,(I/'f3_39').read_text().splitlines()[row['frame']].split()))if f==3 else[(0,i)for i,m in enumerate(parents)if not m&parents[0]][row['frame']];core=sum(parents[i]for i in frame);hs=list(map(int,row['witness_high']));ls=list(map(int,row['witness_142']));witness(core,hs+ls,[1059]*len(hs)+[1042]*len(ls),row['sign']);local_witnesses.append({'full_mothers':list(frame),'sign':row['sign'],'high':list(map(str,hs)),'mid':list(map(str,ls))})
write('local_witnesses.json',local_witnesses)
# Replay each endpoint with the identical completed range, rebinding paths only.
geo=[]
for file in ['seven_high_embedded_result.json','endpoint_11825_result.json','endpoint_11823_result.json','endpoint_11821_result.json']:
 for i,row in enumerate(json.loads((H/file).read_text())):
  cmd=row['command'];cmd=[str(O/Path(cmd[0]).name),str(I/'obs'),str(I/'parent'),str(I/'B'),str(I/Path(cmd[4]).name)]+cmd[5:];r=run(cmd,file[:-5]+'_'+str(i));counts=list(map(int,r.stderr.split()));assert counts==row['counts'] and not r.stdout and counts[-1]==0;geo.append({'source_receipt':file,'index':i,'counts':counts,'completed':True,'command':cmd})
write('geometric_exclusions.json',geo)
r=run([O/'packing_layers',I/'catalog.txt','12500'],'packing_layers');(O/'packing_layer_bounds.txt').write_text(r.stdout);assert r.stdout==(H/'packing_layer_bounds.txt').read_text()
# Import the exact signed relaxation checker, before using geometric cost cuts.
spec=importlib.util.spec_from_file_location('boundary',H/'exact_boundary.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
expected={11825:{(9,688):[136],(11,1059):[179],(11,1042):[142],(12,1104):[0],(13,1296):[0]},11823:{(10,744):[60],(11,1059):[179],(11,1042):[142],(11,1046):[72],(12,1104):[0],(13,1296):[0]},11821:{(10,881):[165],(11,1059):[179],(11,1042):[142],(12,1104):[0],(12,1116):[0],(13,1296):[0],(9,655):[91]}}
intake=[]
for c,A,n in[(11825,1173,1),(11823,1169,1),(11821,1165,2)]:
 r=run([O/'trace_spectra',I/'catalog.txt','12500',c,A],f'intake_{c}_{A}');surv=[]
 for line in r.stdout.splitlines():
  ss=[tuple(map(int,x.split(':')))for x in line.split()[1:]]
  if not mod.check_spectrum(ss,c,A)['possible_in_signed_relaxation']:continue
  options=[sorted({s*d for d in signed[x,y]for s in(-1,1)})for x,y,z in ss];pre=[{0}];suf=[set()for _ in range(12)];suf[11]={0}
  for v in options:pre.append({x+y for x in pre[-1]for y in v})
  for j in range(10,-1,-1):suf[j]={x+y for x in suf[j+1]for y in options[j]}
  feasible=[]
  for j,(x,y,z)in enumerate(ss):
   values=[v for v in options[j]if any(A-v-u in suf[j+1]for u in pre[j])];assert values==expected[c][x,y],(c,x,y,values);feasible.append(values)
  surv.append({'spectrum':ss,'feasible_signed_values_per_slot':feasible})
 assert len(surv)==n;intake.append({'cost':c,'difference':A,'trace_spectra':len(r.stdout.splitlines()),'survivors':surv,'geometry_filters_complete':True})
write('endpoint_intake.json',intake)
run([sys.executable,'-B',H/'exact_boundary.py'],'exact_boundary');result=json.loads((O/'exact_boundary_result.json').read_text());assert result['certified_radius']=='525/1049'and result['remaining_pair']==[11817,1157]and result['excluded_pairs']==15
assert Fraction(12501-11292,1611-108)>Fraction(525,1049)
write('receipt.json',{'complete':True,'review_status':'NOT_REVIEWED','inherited_q2_receipts_audited_not_rerun':q2,'frame_counts':frame_counts,'typed_native_rows':2338,'native_absolute_difference_entries':45146,'new_geometric_nodes':sum(x['counts'][1]for x in geo),'certified_radius':'525/1049','closed_p_interval':['262/1049','787/1049'],'remaining_endpoint_pair':[11817,1157],'outer_endpoint_extra_equality_unresolved':True,'uniform_equal_tables':8000,'strict_interior_nonuniform_bias_equal_tables':4000,'commands':receipts,'seconds':time.monotonic()-start})
print(json.dumps({'complete':True,'certified_radius':'525/1049','closed_p_interval':['262/1049','787/1049'],'seconds':time.monotonic()-start,'receipt':str(O/'receipt.json')},indent=2))
