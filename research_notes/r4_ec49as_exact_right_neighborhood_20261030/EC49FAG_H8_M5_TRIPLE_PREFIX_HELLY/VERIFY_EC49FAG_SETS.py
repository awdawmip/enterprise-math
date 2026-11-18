#!/usr/bin/env python3
"""Exact finite common-prefix obstruction scan; frozen H8/M5 signed-X6."""
import hashlib,itertools,collections,sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'EC49EXJ_H8_M4_S6_GLOBAL_EXACT'))
from SCREEN_H5_EC49EXJ import words,OPS,sig
p=Path(__file__).resolve().parent.parent/'EC49EXY_H8_M5_EXACT_CROSS_FIBER_CAPS/EC49EXY_DOUBLE_CANDIDATES.tsv'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='1e5f75bdc2491f355db6e2632fb6789a55397f7943c77c6ebf249807ee20712a'
raw=[]
for line in p.read_text().splitlines():
 if line.startswith('#') or not line.strip():continue
 nums=tuple(map(int,line.split()));a,b,c,d=nums[2:6]
 hs=((a,b),(c,d))+tuple((h,) for h in range(2,9) if h not in (a,b,c,d))
 keys=[tuple(nums[6+3*i:9+3*i]) for i in range(5)]
 groups=tuple(tuple((h,k,4 if k[0]+k[1]-h-1>=1 else 2) for h in group) for group,k in zip(hs,keys))
 raw.append((nums,groups))
assert len(raw)==12356
fset={f for _,gr in raw for group in gr for f in group}
assert len(fset)==137
prefix_by_fam={}
for f in sorted(fset):
 out=collections.defaultdict(set)
 for st,ss,w in words(*f):
  for depth in range(1,len(st)+1):out[depth].add(st[:depth])
 prefix_by_fam[f]=out
results={'source_tsv_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'rows':len(raw),'families':len(fset), 'words':sum(len(words(*f)) for f in fset)}
minimal_counts=collections.Counter();case_counts=collections.Counter();examples={}; counts_by_depth=collections.Counter()
for idx,(nums,gr) in enumerate(raw):
  dmax=2*(max(sum(k)-1 for k in [group[0][1] for group in gr]))
  sets=[[frozenset().union(*(prefix_by_fam[f].get(dep,()) for f in group)) for dep in range(1,dmax+1)] for group in gr]
  schedule_violations=set()
  for dep in range(1,dmax+1):
    S={1<<i:sets[i][dep-1] for i in range(5)}
    for mask in range(1,32):
      if mask in S:continue
      bit=mask&-mask
      S[mask]=S[bit] & S[mask^bit]
    for mask in range(1,32):
      k=mask.bit_count()
      if k<3:continue
      if any(not S[1<<i] for i in range(5) if mask&(1<<i)):continue
      if S[mask]:continue
      if all(bool(S[mask ^ (1<<i)]) for i in range(5) if mask&(1<<i)):
        minimal_counts[k]+=1; schedule_violations.add(k); counts_by_depth[(k,dep)]+=1
        if k not in examples:
          examples[k]={'row_index_zero_based':idx,'mask':mask,'fiber_indices':[i for i in range(5) if mask&(1<<i)],'depth':dep,
             'pair_intersection_counts':{f'{i},{j}':len(S[(1<<i)|(1<<j)]) for i,j in itertools.combinations(range(5),2) if mask&(1<<i) and mask&(1<<j)},
             'all_intersection_size':len(S[mask]),'group_specs':[[{'h':f[0],'key':list(f[1]),'observer_type':f[2]} for f in gr[i]] for i in range(5) if mask&(1<<i)]}
  for k in schedule_violations:case_counts[k]+=1
results.update({'minimal_bad_set_count_by_size':dict(minimal_counts),'schedule_count_with_minimal_bad_set_by_size':dict(case_counts),'example_by_size':examples,'counts_by_depth':{str(k):v for k,v in sorted(counts_by_depth.items())}})
out=Path(__file__).resolve().parent/'EC49FAG_SET_AUDIT.json'
out.write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in results.items() if k!='counts_by_depth'},indent=2))
