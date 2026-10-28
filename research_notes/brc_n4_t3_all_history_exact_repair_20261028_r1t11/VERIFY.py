#!/usr/bin/env python3
"""Exact 729-vertex BRC N4 S3 quotient repair certificate.
SciPy proposes occupancies; Fraction checks every fact and real behavior.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from hashlib import sha256
from pathlib import Path
import json
import numpy as np
from scipy.optimize import linprog
Z,O=F(0),F(1); A=('P','Q','C')
N={1:{'A':(F(1,2),F(1,2),None),'B':(F(1,2),F(3,2),None)},
   2:{'AU':(F(1,6),O,'A'),'AV':(F(1,3),F(1,4),'A'),
      'BU':(F(1,4),O,'B'),'BV':(F(1,4),F(2),'B')}}
for t in (3,4):
 N[t]={}
 for h,(q,r,_) in N[t-1].items():
  e=({'AU':F(1,10),'AV':Z,'BU':F(4,5),'BV':Z}[h] if t==3
     else Z if h=='AV0' else F(3,50) if h=='AV1' else F(1,20))
  for j,s in enumerate((-1,1)):N[t][h+str(j)]=(q/2,r*(1+s*e),h)
for t in N:
 assert len(N[t])==2**t and all(q>0 and r>0 for q,r,_ in N[t].values())
 assert sum((q for q,r,_ in N[t].values()),Z)==sum((q*r for q,r,_ in N[t].values()),Z)==O
T2={'AU':(F(1,2),F(1,6),F(1,3)),'AV':(Z,Z,O),'BU':(Z,F(1,2),F(1,2)),'BV':(O,Z,Z)}
H3=('AU0','AU1','AV0','AV1','BU0','BU1'); V=((O,Z,Z),(Z,O,Z),(Z,Z,O))
K=[(t,h,a) for t in (2,3,4) for h in N[t] for a in A[:(3 if t<4 else 2)]]
ID={k:i for i,k in enumerate(K)};EQ=[]
def add(d,b):EQ.append((d,F(b)))
for t in (2,3,4):
 for h in N[t]:
  d={(t,h,a):O for a in A[:(3 if t<4 else 2)]}
  if t>2:d[t-1,N[t][h][2],'C']=-O
  add(d,O if t==2 else Z)
for h,a,v in [('AV','P',Z),('AV','Q',Z),('BV','P',O)]:add({(2,h,a):O},v)
for a in A:add({(3,'AV0',a):O,(3,'AV1',a):-O},Z)
for a in A[:2]:add({(4,'AV00',a):O,(4,'AV01',a):-O},Z)
LAW=[]
for t in (2,3,4):
 for a in A[:2]:
  for R in (0,1):
   LAW.append(({(t,h,a):q*(r if R else O) for h,(q,r,_) in N[t].items()},
               8*R+2*(t-1)+(a=='Q')))
def row(d):
 x=np.zeros(len(K))
 for k,v in d.items():x[ID[k]]+=float(v)
 return x
M=np.stack([row(d) for d,b in EQ]+[row(d) for d,j in LAW]);B=np.array([float(b) for d,b in EQ])
def law(policy):
 y=[Z]*16
 for leaf,(q,r,_) in N[4].items():
  alive=O
  for t,h in enumerate((leaf[:1],leaf[:2],leaf[:3],leaf),1):
   p=(Z,Z,O) if t==1 else policy[t,h]
   assert all(v>=0 for v in p) and sum(p,Z)==O
   if t==4:assert p[2]==Z
   j=2*(t-1)
   y[j]+=q*alive*p[0]; y[j+1]+=q*alive*p[1]
   y[8+j]+=q*r*alive*p[0]; y[9+j]+=q*r*alive*p[1]
   alive*=p[2]
  assert alive==Z
 assert sum(y[:8],Z)==sum(y[8:],Z)==O
 return y
def target(v):
 p={(2,h):a for h,a in T2.items()}
 p.update({(3,h):V[z] for h,z in zip(H3,v)})
 p.update({(3,h):(O,Z,Z) for h in N[3] if h.startswith('BV')})
 p.update({(4,h):(Z,O,Z) if N[4][h][1]<F(2501,10000) else (O,Z,Z) for h in N[4]})
 return law(p)
GROUPS={}
for t in (3,4):
 GROUPS[t]=defaultdict(list)
 for h,(_,r,_) in N[t].items():GROUPS[t][r].append(h)
def exact(x,y):
 assert set(x)==set(K) and all(v>=0 for v in x.values())
 for d,b in EQ:assert sum((x[k]*v for k,v in d.items()),Z)==b
 for d,j in LAW:assert sum((x[k]*v for k,v in d.items()),Z)==y[j]
 surv={(t,h):(O if t==2 else x[t-1,N[t][h][2],'C']) for t in (2,3,4) for h in N[t]}
 for t,G in GROUPS.items():
  for hs in G.values():
   for h in hs[1:]:
    for a in A[:(3 if t<4 else 2)]:assert x[t,hs[0],a]*surv[t,h]==x[t,h,a]*surv[t,hs[0]]
 policy={}
 for (t,h),s in surv.items():
  z=(tuple(x[t,h,a]/s for a in A[:(3 if t<4 else 2)]) if s else ((Z,Z,O) if t<4 else (O,Z)))
  policy[t,h]=z if t<4 else z+(Z,)
 assert law(policy)==y
ROOT=Path(__file__).resolve().parent;digest=sha256();lines=[];maxden=1;maxnz=0
for v in product(range(3),repeat=6):
 y=target(v)
 b=np.concatenate([B,np.array([float(y[j]) for d,j in LAW])])
 res=linprog(np.zeros(len(K)),A_eq=M,b_eq=b,bounds=(0,None),method='highs')
 assert res.success,(v,res.message)
 x={k:F(float(f)).limit_denominator(1000000) for k,f in zip(K,res.x)}
 exact(x,y)
 entries=[[t,h,a,str(z)] for (t,h,a),z in x.items() if z]
 doc={'vertex':list(v),'nonzero_occupancies':entries}
 s=json.dumps(doc,sort_keys=True,separators=(',',':'))+'\n'
 digest.update(s.encode());lines.append(s)
 maxden=max(maxden,max(z.denominator for z in x.values()))
 maxnz=max(maxnz,len(entries))
from gzip import compress
(ROOT/'CERTIFICATES.jsonl.gz').write_bytes(compress(''.join(lines).encode(),mtime=0))
out={'status':'PASS_EXACT_RATIONAL_N4_S3_ALL_729_VERTEX_REPAIRS','vertices_checked':729,
     'certificate_stream_sha256':digest.hexdigest(),'max_rational_denominator':maxden,
     'max_nonzero_occupancies':maxnz,'proof_status':'AUTHOR_EXACT_COMPUTATIONAL_PROOF / UNREVIEWED / NOT_ADMITTED',
     'scope':'Same strict positive N4 tree, frozen t2 behavior and t4 LR threshold, all real t3 histories and actions, exact two-law (T,D).'}
(ROOT/'RESULT_SHORT.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print(json.dumps(out,sort_keys=True))
