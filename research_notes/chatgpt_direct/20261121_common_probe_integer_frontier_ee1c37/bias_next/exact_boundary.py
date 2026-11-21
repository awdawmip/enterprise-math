from pathlib import Path
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json,subprocess,time
import os
HERE=Path(os.environ['PROBE_OUTPUT'])
SOURCE=HERE/'trace_spectra'
CAT=Path(os.environ['PROBE_PREPARED'])/'catalog.txt'
signed={}
for line in (HERE/'signed_catalog.txt').read_text().splitlines():
 s,e,c,*ds=map(int,line.split());signed.setdefault((s,c),set()).update(ds)
bounds={}
for line in (HERE/'packing_layer_bounds.txt').read_text().splitlines():
 c,d=map(int,line.split())
 if c<11301:continue
 t=c-11292;a=min(d,108+2*t-1);a-=(a-c)%2;bounds[c]=min(a,{11825:1171,11823:1167,11821:1163}.get(c,a))
inherited=json.loads((Path(os.environ['PROBE_PROOF'])/'verification'/'exact_boundary_result.json').read_text())
for row in inherited['records']:
 if row['all_excluded']:bounds[row['cost']]=min(bounds[row['cost']],row['difference']-2)
cover_families=json.loads((HERE/'cover_families.json').read_text())
records=[];st=time.monotonic();trace_dir=HERE/'exact_traces';trace_dir.mkdir(exist_ok=True)
def check_spectrum(spec,c,a):
 m=sum(s==13 for s,cc,d in spec)
 if m>=5:return {"possible_in_signed_relaxation":False,"signed_witness":None,"states":0,"full_mothers":m,"reason":"Five-full-mother classification gives only the uniform optimum; six or more impossible."}
 cap=3 if m>=4 else 4 if m==3 else 6 if m==2 else 7 if m==1 else 11
 cap=min(cap,6 if c<11925 else 11)
 embedded=sorted(s for s,cc,d in spec if (s==11 and cc in(936,944,960)) or (s==12 and cc in(1104,1116)) or s==13)
 small=sorted(s for s,cc,d in spec if s<11)
 cover_limit=min([f['H_or_L']-1 for f in cover_families if f['E']==embedded and f['small']==small]+[11])
 options=[]
 for s,cc,d in spec:
  assert max(signed[s,cc])==d
  ds=sorted({v*sign for v in signed[s,cc]for sign in (-1,1)},reverse=True)
  options.append([(v,int(s==11 and cc==1059 and v==179),int(s==11 and cc==1042 and v==142),int(s==11 and cc==1126 and v==114))for v in ds])
 options.sort(key=len)
 rem=[0]*(len(options)+1)
 for i in range(len(options)-1,-1,-1):rem[i]=rem[i+1]+max(abs(v)for v,h,b,k in options[i])
 @lru_cache(None)
 def solve(i,target,h,b,k):
  if (embedded==[12,12,12,13] and small==[10] and k>=1 and h+b>=5) or (m>=2 and (b>6 or (h>=1 and b>4) or h+b>6)) or (m>=4 and (b>2 or h+b>3)) or h+b>cover_limit or (m>=3 and (b>4 or (h>=2 and b>=3))) or h>cap or ((m>=3 and h>=4 and b>=1) or (m>=2 and h>=5 and b>=2)) or abs(target)>rem[i]:return None
  if i==len(options):return ()if target==0 else None
  for d,inc,flag,inc_k in options[i]:
   rest=solve(i+1,target-d,h+inc,b+flag,k+inc_k)
   if rest is not None:return (d,)+rest
  return None
 hit=solve(0,a,0,0,0)
 return {'possible_in_signed_relaxation':hit is not None,'signed_witness':hit,'states':solve.cache_info().currsize,'full_mothers':m,'high_positive_cap':cap}
if __name__ == '__main__':
 while True:
  ratio,c,a=min((Fraction(c-11292,a-108),c,a)for c,a in bounds.items()if a>108)
  r=subprocess.run([str(SOURCE),str(CAT),'12500',str(c),str(a)],text=True,capture_output=True,check=True)
  (trace_dir/f'{c}_{a}.txt').write_text(r.stdout);(trace_dir/f'{c}_{a}.log').write_text(r.stderr)
  cases=[]
  for line in r.stdout.splitlines():
   tag,*words=line.split();assert tag=='witness';spec=[tuple(map(int,s.split(':')))for s in words];assert len(spec)==11 and sum(s for s,cc,d in spec)==125 and sum(cc for s,cc,d in spec)==c
   result=check_spectrum(spec,c,a);cases.append({'spectrum':spec,**result})
  row={'cost':c,'difference':a,'radius':str(ratio),'spectrum_count':len(cases),'cases':cases,'trace_statistics':r.stderr.strip(),'trace_sha256':sha256(r.stdout.encode()).hexdigest(),'all_excluded':all(not x['possible_in_signed_relaxation']for x in cases)};records.append(row)
  print({k:v for k,v in row.items()if k not in ('cases','trace_statistics')},flush=True)
  (HERE/'exact_boundary_progress.json').write_text(json.dumps({'records':records,'bounds_improved':{str(v['cost']):bounds[v['cost']] for v in records},'elapsed_seconds':time.monotonic()-st},indent=2)+'\n')
  if not row['all_excluded']:
   result={'complete_until_first_remaining_boundary':True,'certified_radius':str(ratio),'p_interval':[str((1-ratio)/2),str((1+ratio)/2)],'excluded_pairs':len(records)-1,'remaining_pair':[c,a],'records':records,'elapsed_seconds':time.monotonic()-st,'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()};(HERE/'exact_boundary_result.json').write_text(json.dumps(result,indent=2)+'\n');break
  bounds[c]=a-2
