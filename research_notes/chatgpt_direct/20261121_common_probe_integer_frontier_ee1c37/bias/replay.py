"""Exclude all competing eleven-class tables at an exact action bias."""
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse,json,os,subprocess,sys,time
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--baseline',type=Path,required=True)
parser.add_argument('--output',type=Path,required=True)
parser.add_argument('--work',type=Path,required=True)
parser.add_argument('--denominator',type=int,default=3)
parser.add_argument('--jobs',type=int,default=2)
parser.add_argument('--resume',action='store_true')
parser.add_argument('--profiles',type=Path)
args=parser.parse_args()
BASELINE=args.baseline.resolve()
sys.path.insert(0,str(BASELINE/'bias'))
from plan_extended import root,mod,dangerous,source,catalog
HERE=args.output.resolve(); HERE.mkdir(parents=True,exist_ok=True)
SOURCE=BASELINE/'bias'
ELEVEN=root/'previous/eleven'
from contextlib import contextmanager
@contextmanager
def workspace():
 args.work.mkdir(parents=True,exist_ok=True)
 yield str(args.work.resolve())

def verify(q,jobs,resume=False):
 legacy=set(json.loads((SOURCE/"legacy_profiles_q5.json").read_text())) if q==5 else set()
 case_dir=HERE/f"completed_q{q}";case_dir.mkdir(exist_ok=True)
 cache_path=HERE/f"completed_q{q}.json"
 combined=json.loads(cache_path.read_text()) if resume and cache_path.exists() else {}
 previous=root/'previous/previous'
 if args.profiles:
  supplied=json.loads(args.profiles.read_text());assert supplied['q']==q
  cap,todo=supplied['cap'],supplied['rows']
 else:cap,todo=dangerous(q)
 assert (cap+1-mod.bias.OPTIMAL)*q>source['global_difference_cap']-mod.bias.OPTIMAL_DIFFERENCE
 for p,e,f,c in todo:
  assert sum(e[:2])>13 and min(p)>mod.bias.MOTHER_UNIONS[len(e)]-sum(e)
 assert max(catalog[11,0])<=1376 and max(catalog[12,0])<=1560
 keys=sorted({(len(e),sum(e))for p,e,f,c in todo})
 third=previous/'previous/previous/previous';second=third/'previous'
 os.environ['NATIVE_PROBE_PREVIOUS']=str(second)
 sys.path[:0]=[str(previous/'previous/parents'),str(third/'group'),str(second/'bounds')]
 from generate import maps
 from geometry import inventory,linear_actions
 from cyclic11 import observations
 from pairtypes import build
 from prior_bounds import observation_file
 forbidden,menus=observations();parents,centers=inventory(linear_actions(),forbidden,menus)
 rank={i:j for j,members in build(parents,centers)for i in members}
 parent_text=''.join(f'{m%2**64} {m>>64}\n'for m in parents)+' '.join(str(rank[i])for i in range(1,250))+'\n'
 linear,translations,_=maps();label=lambda s:','.join(map(str,s))
 with workspace()as tmp:
  w=Path(tmp);(w/'parent').write_text(parent_text)
  (w/'maps').write_bytes(b''.join(bytes(t[x]for x in g)for g in linear for t in translations));observation_file(w/'obs')
  def compile_source(name):
   src=previous/'mothers/union.cpp'if name=='union'else SOURCE/'weighted_native.cpp'if name=='native'else SOURCE/'weighted_native_before_hall.cpp'if name=='native_prior'else ELEVEN/(name+'.cpp')
   subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',src,'-o',w/name],check=True)
  with ThreadPoolExecutor(jobs)as pool:list(pool.map(compile_source,['union','census','bank','frame','native','native_prior']))
  subprocess.run([w/'census',w/'obs',w/'seeds','0','0','0','1376','1560'],stdout=subprocess.DEVNULL,check=True)
  bank=subprocess.run([w/'bank',w/'parent',w/'maps',w/'seeds',w/'B','0 0 0 0 0 0 0 0 0 0 0 1376 1560 0'],capture_output=True,text=True,check=True)
  inventory_rows={str(s):[count,rows]for s,count,rows in(map(int,l.split())for l in bank.stderr.splitlines())}
  assert inventory_rows['11']==[39,18920]and inventory_rows['12']==[4,540]
  def frames(item):
   k,s=item;assert 13*(k-1)<s
   raw=w/f'raw{k}_{s}'
   with raw.open('w')as f:subprocess.run([w/'union',str(k),str(s),'-1','all'],input=parent_text,text=True,stdout=f,check=True)
   with raw.open()as f,(w/f'f{k}_{s}').open('w')as o:r=subprocess.run([w/'frame',w/'parent',w/'maps',str(k)],stdin=f,stdout=o,stderr=subprocess.PIPE,text=True,check=True)
   raw.unlink();raw_count,canon=map(int,r.stderr.split());assert canon>0 and raw_count>=canon
   return f'{k},{s}',[raw_count,canon]
  with ThreadPoolExecutor(jobs)as pool:locations=dict(pool.map(frames,keys))
  def exclude(item):
   p,e,floor,ceiling=item;k,s=len(e),sum(e);family_count=locations[f'{k},{s}'][1]
   key=label(p)+'__'+label(e);algorithm='weighted'if key in legacy else 'weighted_hall';receipt=case_dir/(key+'.json')
   if resume and (receipt.exists() or key in combined):
    prior=json.loads(receipt.read_text()) if receipt.exists() else combined[key];v=prior['result'];assert prior['algorithm']==algorithm and v[:3]==[ceiling,floor,family_count]and v[-1]==0
    print(json.dumps({'cached_profile':key,'algorithm':algorithm,'counts':v[2:]}),flush=True);return key,v
   t=time.time();r=subprocess.run([w/('native_prior'if key in legacy else 'native'),w/'obs',w/'parent',w/'B',w/f'f{k}_{s}',label(p),label(e),str(floor),str(ceiling),'0',str(family_count),str(q),str(sum(min(q*c-d for c,d in catalog[s,1].items())for s in e)+q*(floor-sum(min(catalog[s,1])for s in e))),','.join(str(min((q*c-d for c,d in catalog.get((s,0),{}).items()),default=100000))for s in range(14))],capture_output=True,text=True,check=True)
   counts=list(map(int,r.stderr.split()))
   print(json.dumps({'P':p,'E':e,'ceiling':ceiling,'floor':floor,'counts':counts,'witness':r.stdout,'elapsed':time.time()-t}),flush=True)
   assert len(counts)==5
   assert counts[0]==family_count or counts[-1]>0
   if r.stdout:(HERE/(key+'.witness.txt')).write_text(r.stdout)
   assert bool(r.stdout)==bool(counts[-1])
   value=[ceiling,floor,*counts];receipt.write_text(json.dumps({'key':key,'algorithm':algorithm,'result':value},sort_keys=True)+'\n')
   return key,value
  with ThreadPoolExecutor(jobs)as pool:cases=dict(pool.map(exclude,todo))
 return dict(weighted_radius=str(Fraction(1,q)),p_interval=[str(Fraction(q-1,2*q)),str(Fraction(q+1,2*q))],uniform_optimum_family_count=8000,profiles=len(todo),cases=cases,competing_witness_profiles=sum(v[-1]>0 for v in cases.values()),complete_exclusion=all(v[-1]==0 for v in cases.values()),normalized_mother_locations=locations,large_exception_catalog=inventory_rows,search_nodes=sum(v[3]for v in cases.values()),family_profile_placements=sum(v[2]for v in cases.values()),tail_cap=cap,last_dangerous_budget=max(c for p,e,f,c in todo),global_difference_cap=source['global_difference_cap'],algorithm_profile_counts={'weighted':len(legacy),'weighted_hall':len(todo)-len(legacy)},settlement_calls=sum(v[5]for v in cases.values()))

if __name__=='__main__':
 start=time.time()
 value=verify(args.denominator,args.jobs,args.resume)
 if args.denominator==3:
  assert value['complete_exclusion'] and value['competing_witness_profiles']==0
  assert value['profiles']==530 and value['search_nodes']==584517341
  assert value['family_profile_placements']==3086925
  assert value['tail_cap']==11793 and value['last_dangerous_budget']==11594
 reference=Path(__file__).resolve().parent/f'result_q{args.denominator}_weighted.json'
 if reference.exists():
  expected=json.loads(reference.read_text())
  for key,actual in value.items():assert actual==expected[key],(key,actual,expected[key])
 value['elapsed_seconds']=time.time()-start
 target=HERE/f'result_q{args.denominator}_weighted.json'
 target.write_text(json.dumps(value,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'result':str(target),'profiles':value['profiles'],'nodes':value['search_nodes'],'complete_exclusion':value['complete_exclusion'],'witness_profiles':value['competing_witness_profiles'],'elapsed_seconds':value['elapsed_seconds']}),flush=True)
