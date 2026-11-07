#!/usr/bin/env python3
"""PREFIX-552: exact terminal-match compression, frozen X6 pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Requires published sibling PREFIX550_shared_gauge_compact_certificate.py.
"""
from collections import Counter,defaultdict
import json
import PREFIX550_shared_gauge_compact_certificate as x

def root(p):
 c=x.P[p][2]
 return tuple((1 if c>0 else -1) if a==abs(c) else 0 for a in range(1,7))

def move(f,kernel,axes):
 result=[{} for _ in range(51)]
 for c in range(51):
  a=axes[c]
  for (j,gate),n in kernel[c].items():
   for m,v in f[j].items():
    q=list(m)
    if a<5:q[a]+=1
    q[5]+=gate; t=tuple(q)
    result[c][t]=result[c].get(t,0)+n*v
 return result

def restore(total,same,d,axis):
 out=defaultdict(int)
 for m,n in total.items():
  k=same.get(m,0);assert 0<=k<=n
  for v,boundary in ((k,0),(n-k,1)):
   if v==0:continue
   q=list(m[:5]);p6=d-sum(q)
   if boundary:
    if axis==5:p6-=1
    else:q[axis]-=1
   assert min(q+[p6])>=0 and sum(q)+p6==d-boundary
   out[tuple(q)+(p6,m[5])]+=v
 assert sum(out.values())==6**d
 return dict(out)

def run(depth=8):
 ids,growth=x.classes(x.ROOTS[0]);assert growth==[1,12,51]
 ph={ids[p]:x.V[p][0] for p in range(96)}
 sig={c:root(ph[c]) for c in range(51)}
 axes={c:abs(x.P[ph[c]][2])-1 for c in range(51)}
 q0=x.quotient(ids,x.ZERO_ROOT)
 kernel={c:Counter((j,w[6]) for (j,w),n in q0[c].items() for _ in range(n)) for c in range(51)}
 assert all(sum(row.values())==6 for row in kernel.values())
 totals=[[{(0,)*6:1} for _ in range(51)]]
 for _ in range(depth):totals.append(move(totals[-1],kernel,axes))
 checked=positions=0
 for r in x.ROOTS:
  same=[{(0,)*6:1} if sig[c]==r else {} for c in range(51)]
  ref=[{x.ZERO_MON:1} for _ in range(51)]
  qr=x.quotient(ids,r)
  starts=[p for p in range(96) if root(x.V[p][0])==r]
  assert len(starts)==8
  for d in range(depth+1):
   for p in starts:
    c=ids[p];got=restore(totals[d][c],same[c],d,axes[c])
    assert got==ref[c],(p,d)
    checked+=1;positions+=len(got)
   if d<depth:
    same=move(same,kernel,axes);ref=x.evo(qr,ref)
 witness_count=0;short_pairs=0
 for r in x.ROOTS:
  found=False
  for start in range(96):
   if root(x.V[start][0])!=r:continue
   states={(start,x.ZERO_MON):()}
   for d in range(1,5):
    nxt={}
    for (p,m),route in states.items():
     for act in x.A:
      j,w=x.edge(p,act,x.ZERO_ROOT)
      key=(j,tuple(a+b for a,b in zip(m,w)))
      nxt.setdefault(key,route+(act,))
    states=nxt;seen={}
    for (p,m),route in states.items():
     bit=(root(x.V[p][0])==r)
     seen.setdefault(m,set()).add(bit)
     short_pairs+=1
     if len(seen[m])==2:
      assert d==4
      found=True
  assert found,r
  witness_count+=1
 return {'status':'ALL_CHECKS_PASS','pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
  'depth_inclusive':depth,'complete_joint_histograms':checked,'coefficient_positions':positions,
  'signed_root_collision_witnesses':witness_count,'enumerated_path_states':short_pairs,
  'minimum_collision_length':4}

if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2))
