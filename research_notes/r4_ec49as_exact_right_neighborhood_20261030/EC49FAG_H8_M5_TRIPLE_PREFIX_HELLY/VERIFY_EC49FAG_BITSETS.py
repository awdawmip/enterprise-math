#!/usr/bin/env python3
"""Independent prefix-ID bitset audit of all depth-wise joint-prefix intersections."""
import sys,itertools,collections,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'EC49EXJ_H8_M4_S6_GLOBAL_EXACT'))
from SCREEN_H5_EC49EXJ import words
s=P.parent/'EC49EXY_H8_M5_EXACT_CROSS_FIBER_CAPS/EC49EXY_DOUBLE_CANDIDATES.tsv'
rows=[]
for line in s.read_text().splitlines():
 if line.startswith('#') or not line.strip():continue
 n=list(map(int,line.split()));a,b,c,d=n[2:6]
 hs=((a,b),(c,d))+tuple((h,) for h in range(2,9) if h not in (a,b,c,d));keys=[tuple(n[6+3*i:9+3*i]) for i in range(5)]
 rows.append((n,tuple(tuple((h,k,4 if k[0]+k[1]-h-1>=1 else 2) for h in group) for group,k in zip(hs,keys))))
fams=sorted({f for _,g in rows for group in g for f in group});assert len(fams)==137
prefix_ids=collections.defaultdict(dict)
fam_bits={}
for f in fams:
 b=collections.defaultdict(int)
 for st,_,_ in words(*f):
  for d in range(1,len(st)+1):
   prefix=st[:d]; IDs=prefix_ids[d]
   if prefix not in IDs:IDs[prefix]=len(IDs)
   b[d]|=1<<IDs[prefix]
 fam_bits[f]=b
assert sum(len(words(*f)) for f in fams)==120852
count=collections.Counter();sched=collections.Counter();count_deps=collections.Counter()
for ri,(n,groups) in enumerate(rows):
 group_bits=[]
 for g in groups:
  b={}
  for d in range(1,1+max(prefix_ids)):b[d]=0
  for f in g:
   for d,x in fam_bits[f].items():b[d] |= x
  group_bits.append(b)
 found=set()
 for d in range(1,1+max(prefix_ids)):
  S={1<<i:group_bits[i][d] for i in range(5)}
  for mask in range(1,32):
   if mask not in S:
    v=mask&-mask;S[mask]=S[v]&S[mask^v]
  for mask in range(1,32):
   if mask.bit_count()<3 or S[mask]:continue
   if any(S[1<<i]==0 for i in range(5) if mask&(1<<i)):continue
   if all(S[mask^(1<<i)] for i in range(5) if mask&(1<<i)):
    k=mask.bit_count();count[k]+=1;count_deps[(k,d)]+=1;found.add(k)
 for k in found:sched[k]+=1
report={'status':'PASS','algorithm':'independent_prefix_id_bitset_intersections','source_sha256':hashlib.sha256(s.read_bytes()).hexdigest(),'families':len(fams),'schedules':len(rows),'word_instances':sum(len(words(*f)) for f in fams),'distinct_prefixes_by_depth':{str(d):len(m) for d,m in prefix_ids.items()},'minimal_nonhelly_intersections_by_size':dict(count),'affected_schedules_by_size':dict(sched),'counts_by_depth':{str(k):v for k,v in sorted(count_deps.items())}}
(P/'EC49FAG_INDEPENDENT_AUDIT.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='counts_by_depth'},indent=2))
