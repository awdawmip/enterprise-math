"""Replay the cost envelope, unique first boundary spectrum, and signed exclusion."""
from pathlib import Path
from fractions import Fraction
import argparse,hashlib,json,subprocess,sys,time
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--baseline',type=Path,required=True);p.add_argument('--q3-proof',type=Path,required=True);p.add_argument('--work',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();h=Path(__file__).resolve().parent;out=a.output.resolve();out.mkdir(parents=True,exist_ok=True);w=a.work.resolve();cap=12043
q3=json.loads((a.q3_proof/'result_q3_weighted.json').read_text());assert q3['complete_exclusion'] and q3['profiles']==530 and q3['search_nodes']==584517341 and q3['competing_witness_profiles']==0
sys.path.insert(0,str(a.baseline.resolve()/'bias'));from plan_extended import catalog,checksum,source
embedded=json.loads((a.q3_proof/'embedded_bound_verification.json').read_text());assert checksum==embedded['single_class_catalog_sha256'] and embedded['all_bounds_verified']
entries={}
for (s,e),rows in catalog.items():
 if e==2:continue
 for c,d in rows.items():entries[s,c]=max(entries.get((s,c),-1),d)
items=sorted((s,c,d)for (s,c),d in entries.items());text=str(len(items))+'\n'+''.join(f'{s} {c} {d}\n'for s,c,d in items);fi=out/'catalog.txt';fi.write_text(text)
# Independently verify the size/count-only global absolute-difference cap.
md={13-s:max(d for ss,c,d in items if ss==s)for s in range(1,14)};dp={0:0}
for _ in range(11):
 nxt={}
 for used,v in dp.items():
  for deficit,add in md.items():
   if used+deficit<=18:nxt[used+deficit]=max(nxt.get(used+deficit,-1),v+add)
 dp=nxt
assert dp[18]==source['global_difference_cap']==1611
executables={}
for name in ['cost_envelope','trace_global','endpoint_search','endpoint_11594']:
 exe=out/name;cmd=['c++','-std=c++20','-O3'];
 if name.startswith('endpoint'):cmd.append('-mpopcnt')
 subprocess.run(cmd+[str(h/(name+'.cpp')),'-o',str(exe)],check=True);executables[name]=exe
start=time.time();r=subprocess.run([str(executables['cost_envelope']),str(fi),str(cap)],capture_output=True,text=True,check=True);bounds=dict(tuple(map(int,l.split()))for l in r.stdout.splitlines());cost_statistics=r.stderr.strip();assert all(v<=1611 for v in bounds.values())
def candidates(extra=False,second=False):
 rows=[]
 for c,raw in bounds.items():
  if c<11301:continue
  t=c-11292;allowed=min(raw,108+3*t-2)
  if extra and c==11595:allowed=min(allowed,1013)
  if second and c==11594:allowed=min(allowed,1010)
  assert (c-allowed)%2==0
  if allowed>108:rows.append((Fraction(t,allowed-108),c,raw,allowed))
 return sorted(rows)
old=candidates();assert old[0][0]==Fraction(303,907);lim=[x for x in old if x[0]==old[0][0]];assert lim==[(Fraction(303,907),11595,1015,1015)]
t=subprocess.run([str(executables['trace_global']),str(fi),'11595','11595'],capture_output=True,text=True,check=True);traces=[]
for line in t.stdout.splitlines():
 tag,*tokens=line.split();assert tag=='witness';traces.append(sorted(tuple(map(int,x.split(':')))for x in tokens))
expected=sorted([(10,744,60)]*2+[(11,1059,179)]*5+[(12,1104,0),(12,1116,0)]+[(13,1296,0)]*2);assert traces==[expected]
for s,c,d in expected:
 assert catalog.get((s,0 if s in (10,11)else 1),{}).get(c)==d
 assert c not in catalog.get((s,1 if s in (10,11)else 0),{})
for f,digest in json.loads((h/'prepared_inputs_sha256.json').read_text()).items():assert hashlib.sha256((w/f).read_bytes()).hexdigest()==digest,f
base=[w/'obs',w/'parent',w/'B',w/'f4_50','10,10,11,11,11,11,11','12,12,13,13',4812,11595,0,325,0,0,','.join(['0']*14)];signed=[]
for sign,want in [(1,[325,13972,13666,0,0]),(-1,[325,15498,15197,0,0])]:
 z=subprocess.run([str(executables['endpoint_search']),*map(str,base),str(sign)],capture_output=True,text=True,check=True);counts=list(map(int,z.stderr.split()));assert not z.stdout and counts==want;signed.append({'sign':sign,'counts':counts})
first_extension=candidates(True);assert first_extension[0][0]==Fraction(151,452)
geo_dir=out/'geometric';g=subprocess.run([sys.executable,str(h/'geometric_check.py'),'--baseline',str(a.baseline),'--q3-proof',str(a.q3_proof),'--output',str(geo_dir),'--cap','11793'],capture_output=True,text=True,check=True);geometry=json.loads((geo_dir/'summary.json').read_text())
proper=[(s,c,d)for s in [9,10,11]for c,d in sorted(catalog[s,0].items())];proper_file=out/'proper_catalog.txt';proper_file.write_text(str(len(proper))+'\n'+''.join(f'{s} {c} {d}\n'for s,c,d in proper));bound_file=out/'remaining_bounds.txt'
second_args=[w/'obs',w/'parent',w/'B',w/'f4_52','9,10,10,11,11,11,11','13,13,13,13',5184,11594,0,35,0,0,','.join(['0']*14),proper_file,bound_file]
z=subprocess.run([str(executables['endpoint_11594']),*map(str,second_args)],capture_output=True,text=True,check=True);second_counts=list(map(int,z.stderr.split()));assert not z.stdout and second_counts==[35,29628,29593,0,0]
subprocess.run([sys.executable,str(h/'check_remainder_bound.py'),'--table',str(bound_file),'--catalog',str(proper_file),'--output',str(out/'remainder_verification.json')],capture_output=True,text=True,check=True);remainder_verification=json.loads((out/'remainder_verification.json').read_text());assert remainder_verification['all_upper_bounds_certified']
new=candidates(True,True);radius=new[0][0];assert radius==Fraction(299,895);tail=Fraction(cap+1-11292,1611-108);assert tail>radius
result={'complete':True,'q3_basis':{'profiles':530,'search_nodes':584517341},'single_class_catalog_sha256':checksum,'merged_catalog_sha256':hashlib.sha256(text.encode()).hexdigest(),'catalog_entries':len(items),'global_difference_cap':1611,'cost_cap':cap,'global_cost_envelope_statistics':cost_statistics,'first_certified_radius':'303/907','first_radius_limiting_pair':{'C':11595,'A':1015},'unrestricted_spectrum_trace_statistics':t.stderr.strip(),'unique_limiting_spectrum':expected,'signed_endpoint_exclusions':signed,'signed_endpoint_search_nodes':sum(x['counts'][1]for x in signed),'new_actual_A_upper_at_11595':1013,'second_endpoint_geometry':geometry,'second_endpoint_exclusion':{'C':11594,'A':1012,'counts':second_counts,'both_signs_retained':True,'within_frame_affine_symmetry_pruning':False},'remaining_bound_verification':remainder_verification,'new_actual_A_upper_at_11594':1010,'certified_value_radius':str(radius),'certified_p_interval':[str((1-radius)/2),str((1+radius)/2)],'tail_radius_lower_bound':str(tail),'remaining_boundary_candidates':[{'radius':str(x),'C':c,'class_spectrum_upper_A':raw,'allowed_upper_A':allowed}for x,c,raw,allowed in new if x==radius],'optimum_counts':'8000 at p=1/2; 4000 elsewhere in the open certified interval. At the two outer endpoints additional ties have not been excluded.','scope':'All upper bounds are over the complete class spectrum; no unsearched cost is treated as geometrically excluded. The two additional geometric exclusions are (C,A)=(11595,1015) and (11594,1012); both signs are covered for each.','elapsed_seconds':time.time()-start,'difference_by_total':bounds}
(out/'result.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='difference_by_total'},indent=2),flush=True)
