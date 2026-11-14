#!/usr/bin/env python3
"""Independent frozen native prefix-trie Python checker of case 32315 and 37->62
(case 33269), including all 168 named root projections and all 648 assignments.
Input: master_and_radius3_cases.txt at exact fixed SHA256 below.
Does not import/use the C++ rooted cost algorithm or its output for calculations.
"""
from pathlib import Path
import sys,hashlib,itertools,csv
ROOTS=(3,5,6,7)
EXPECTED_SHA='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
INF=10**9
p=Path(sys.argv[1]);raw=p.read_bytes()
assert hashlib.sha256(raw).hexdigest()==EXPECTED_SHA
it=iter(raw.decode().split())
assert [int(next(it)) for _ in range(3)]==[94,178850,38169]
words=[]
for k in range(94):
 n=int(next(it));part=[]
 for j in range(n):
  l=int(next(it));code=next(it)
  part.append((l,int(code[:2],16),tuple(bytes.fromhex(code[2:]))))
 words.append(part)
cases=[]
for i in range(38169):cases.append(tuple(int(next(it)) for _ in range(7)))
try:next(it);raise AssertionError('Trailing source')
except StopIteration:pass
assert cases[32315]==(0,4,5,11,37,39,81)
assert cases[33269]==(0,4,5,11,39,62,81)
def build(keys,r):
 terminals=[0];children=[{}]
 ls=sorted({l for k in keys for l,root,code in words[k] if root==r})
 idx={l:i for i,l in enumerate(ls)}
 for k in keys:
  for l,root,code in words[k]:
   if root!=r:continue
   u=0
   for a in code:
    if a not in children[u]:
     children[u][a]=len(children);children.append({});terminals.append(0)
    u=children[u][a]
   terminals[u]|=1<<idx[l]
 def visit(u):
  states={0:0}
  if terminals[u]:states[terminals[u]]=0
  for child in children[u].values():
   q=visit(child);new={}
   for m,c in states.items():
    for n,d in q.items():
     b=m|n;v=c+d
     if v<new.get(b,INF):new[b]=v
   states=new
  return {m:c+(m!=0) for m,c in states.items()}
 exact=visit(0)
 f=[INF]*(1<<len(ls))
 for m,c in exact.items():f[m]=c
 for j in range(len(ls)):
  for m in range(len(f)):
   if not(m>>j&1):f[m]=min(f[m],f[m|1<<j])
 return ls,idx,f
P={c:{r:build(cases[c],r) for r in ROOTS} for c in (32315,33269)}
dom={l:tuple(r for r in ROOTS if l in P[32315][r][1]) for l in range(24)}
assert all(dom[l]==tuple(r for r in ROOTS if l in P[33269][r][1]) for l in range(24))
D={}
for c in P:
 D[c]={}
 for r in ROOTS:
  labels,idx,f=P[c][r]
  must=[l for l in labels if len(dom[l])==1]
  opt=[l for l in labels if len(dom[l])>1]
  data={}
  for z in range(1<<len(opt)):
   mask=sum(1<<l for i,l in enumerate(opt) if z>>i&1)
   local=sum(1<<idx[l] for l in must)+sum(1<<idx[l] for i,l in enumerate(opt) if z>>i&1)
   data[mask]=f[local]
  D[c][r]=data
L=tuple(l for l in range(24) if len(dom[l])>1)
assert L==(5,7,13,15,17,19,21)
count=0;local_cancellations=0;first=None;example=None
for choices in itertools.product(*(dom[l] for l in L)):
 rho=dict(zip(L,choices))
 masks={r:sum(1<<l for l,x in rho.items() if x==r) for r in ROOTS}
 diffs={r:D[33269][r][masks[r]]-D[32315][r][masks[r]] for r in ROOTS}
 if sum(diffs.values())!=0:
  count+=1
  if first is None:first=(rho,diffs)
 if sum(diffs.values())==0 and any(diffs.values()):
  local_cancellations+=1
  if example is None:example=(rho,diffs)
assert count==357 and local_cancellations==54
assert first[1]=={3:0,5:1,6:0,7:0}
assert example[1]=={3:0,5:1,6:-1,7:0}
print('INDEPENDENT_648_PASS changed=',count,
      'nonzero_root_zero_terminal=',local_cancellations,
      'example=',example)
# Optional comparison with C++ exported native projections, which were NOT
# used above: 2 configs * 168 root entries = 336 exact integer agreements.
if len(sys.argv)>2:
 records={}
 for row in csv.DictReader(open(sys.argv[2])):
  key=(int(row['swap_out']),int(row['swap_in']))
  if key not in [(-1,-1),(37,62)]:continue
  r=int(row['root']);mask=int(row['subset'])
  records[key,r,mask]=int(row['cost'])
 for c,k in [(32315,(-1,-1)),(33269,(37,62))]:
  for r in ROOTS:
   for m,v in D[c][r].items():assert records[k,r,m]==v
 print('INDEPENDENT_CPP_AGREEMENT 336/336 projected costs PASS')
