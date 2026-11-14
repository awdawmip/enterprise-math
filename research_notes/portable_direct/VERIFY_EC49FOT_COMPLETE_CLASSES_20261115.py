#!/usr/bin/env python3
"""Exact complete 147-class cross-check from frozen source + native profile CSV.
Usage: python3 VERIFY_EC49FOT_COMPACT.py EXTRACTED_EVIDENCE_DIR
"""
import collections,csv,hashlib,itertools,json,sys
from pathlib import Path
D=Path(sys.argv[1]);roots=(3,5,6,7)
p=D/'master_and_radius3_cases.txt'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
with p.open() as f:
 n,w,m=map(int,f.readline().split());assert(n,w,m)==(94,178850,38169)
 fam=[]
 for _ in range(n):
  size=int(f.readline());v=[0]*4
  for _ in range(size):
   l,b=f.readline().split();v[roots.index(int(b[:2],16))]|=1<<int(l)
  fam.append(v)
 cases=[tuple(map(int,f.readline().split())) for _ in range(m)]
def signature(case):
 E=[0]*24
 for key in case:
  for r,mask in enumerate(fam[key]):
   while mask:
    b=mask&-mask;E[b.bit_length()-1]|=1<<r;mask-=b
 assert all(E)
 return tuple(E)
classes=collections.defaultdict(list)
for i,c in enumerate(cases):classes[signature(c)].append(i)
assert len(classes)==625
selection={v[0]:v for v in classes.values() if 5<=len(v)<=64}
assert len(selection)==147 and sum(map(len,selection.values()))==3780
saved={int(k):v for k,v in json.loads((D/'EC49FOT_CLASSES.json').read_text()).items()}
assert saved==selection
all_ids={i for ids in selection.values() for i in ids}
data=collections.defaultdict(dict)
with (D/'EC49FOT_PROFILES.csv').open() as f:
 for row in csv.DictReader(f):
  c,r,must,opt,subset,cost=(int(row[k]) for k in ('config','root','must','opt','subset','cost'))
  assert c in all_ids and r in roots and (r,subset) not in data[c]
  data[c][r,subset]=(must,opt,cost)
assert set(data)==all_ids
stats=collections.Counter();witnesses=[]
for rep,ids in selection.items():
 E=signature(cases[rep]);free=[l for l,d in enumerate(E) if d.bit_count()>1]
 choices=[tuple(roots[j] for j in range(4) if E[l]&(1<<j)) for l in free]
 alloc=list(itertools.product(*choices))
 sub={}
 for j,r in enumerate(roots):
  opts=[l for l in free if E[l]&(1<<j)]
  sub[r]=tuple(sorted(sum(1<<l for l,b in zip(opts,flags) if b)
                     for flags in itertools.product((0,1),repeat=len(opts))))
  must=sum(1<<l for l,d in enumerate(E) if d==1<<j)
  opt=sum(1<<l for l in opts)
  for i in ids:
   assert {(root,s) for root,s in data[i] if root==r}=={(r,s) for s in sub[r]}
   assert all(data[i][r,s][:2]==(must,opt) for s in sub[r])
 signatures={};costs={}
 for i in ids:
  p=data[i]
  signatures[i]=tuple(p[r,s][2] for r in roots for s in sub[r])
  costs[i]=tuple(sum(p[r,sum(1<<l for l,t in zip(free,a) if t==r)][2]
                     for r in roots) for a in alloc)
 A=collections.defaultdict(list);B=collections.defaultdict(list)
 for i in ids:A[signatures[i]].append(i);B[costs[i]].append(i)
 def pairs(groups):return sum(len(v)*(len(v)-1)//2 for v in groups.values())
 rp,tp=pairs(A),pairs(B)
 assert tp>=rp
 for group in B.values():
  for i,j in itertools.combinations(group,2):
   if signatures[i]!=signatures[j]:witnesses.append((i,j))
 stats['classes']+=1;stats['configs']+=len(ids)
 stats['root_entries']+=len(ids)*sum(map(len,sub.values()))
 stats['terminal_evaluations']+=len(ids)*len(alloc)
 stats['pairs']+=len(ids)*(len(ids)-1)//2
 stats['root_equal']+=rp;stats['terminal_equal']+=tp
assert dict(stats)=={'classes':147,'configs':3780,'root_entries':682446,
 'terminal_evaluations':1702588,'pairs':68266,'root_equal':15257,'terminal_equal':15261}
assert witnesses==[(17741,31699),(24354,31700),(16786,19592),(20706,35148)],witnesses
print(json.dumps({'status':'EXACT_COMPLETE_PASS','statistics':dict(stats),'nonzero_gauges':witnesses},indent=2))
