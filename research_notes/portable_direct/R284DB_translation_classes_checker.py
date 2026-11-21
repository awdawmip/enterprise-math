#!/usr/bin/env python3
"""R284DB: classify every equal-D source-mutation edge by lifted affine branch."""
from R284CO_spectral_witness_checker import P,FROZEN_SHA,words,arcs,dist
from R284DA_envelope_checker import envelope,farthest
from itertools import combinations
from collections import Counter,defaultdict
from pathlib import Path
import json,hashlib

def main():
 X=words();A=arcs();T,up,dn,_=envelope(A)
 F=[farthest(x,T,up,dn) for x in X]
 edges=[]
 for i,v in enumerate(F):
  u,l=divmod(i,4096)
  for p in range(12):
   j=u*4096+(l^(1<<(11-p)))
   if j>i and v==F[j]: edges.append(('flip',str(p),i,j,v))
  for p,q in combinations(range(12),2):
   if (l>>(11-p)&1)==(l>>(11-q)&1):continue
   j=u*4096+(l^(1<<(11-p))^(1<<(11-q)))
   if j>i and v==F[j]: edges.append(('swap',f'{p},{q}',i,j,v))
 assert len(edges)==307
 selected={i for _,_,i,j,_ in edges}|{j for _,_,i,j,_ in edges}
 W={}
 for i in selected:
  x=X[i];ds=[dist(x,a) for a in A]
  label=max(range(64),key=lambda j:ds[j]); assert ds.count(F[i])==1
  a,w=A[label];d=(x-a)%P
  left=d-w;right=P-d
  assert left!=right and min(left,right)==F[i]
  if left<right:
   slope=1; intercept=-((x-left))
  else:
   slope=-1;intercept=x+right
  assert F[i]==slope*x+intercept
  W[i]=(label,slope,intercept)
 classes=defaultdict(list)
 for kind,mutation,i,j,v in edges:
  la,sa,ca=W[i];lb,sb,cb=W[j]
  assert sa==sb
  assert la!=lb
  shift=X[j]-X[i]
  assert shift==(ca-cb)//sa and (ca-cb)%sa==0
  arc_pair=tuple(sorted((la,lb)))
  classes[(arc_pair,sa)].append((kind,mutation,i,j,v,shift))
 assert len(set(pair for pair,s in classes))==30
 assert len(classes)==35
 assert len(set(item[-1] for ls in classes.values() for item in ls))==28
 assert all(len({entry[-1] for entry in group})==1 for group in classes.values())
 branch_edges=Counter({str(s):sum(len(group) for (pair,ss),group in classes.items() if ss==s)
                       for s in (1,-1)})
 assert branch_edges==Counter({'1':145,'-1':162})
 canonical=[(kind,mut,i,j,v,W[i][0],W[j][0]) for kind,mut,i,j,v in edges]
 sha=hashlib.sha256(json.dumps(canonical,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
 assert sha=='251a3ca8d2d72cf6f7ca19869f174eb9e370f330533e484faf13dcb2a68dab8b'
 rows=[]
 for (pair,slope),group in sorted(classes.items()):
  rows.append({'arcs':list(pair),'slope':slope,'edge_count':len(group),'source_shift':group[0][-1]})
 cert={'schema':'R284DB_EXACT_AFFINE_TRANSLATION_CLASSES_V1',
       'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
       'population_sha256':FROZEN_SHA,'equal_edges':len(edges),
       'endpoints_examined':len(selected),'branch_tie_endpoints':0,
       'same_slope_edges':len(edges),'opposite_slope_edges':0,
       'same_winning_arc_edges':0,
       'positive_slope_edges':branch_edges['1'],
       'negative_slope_edges':branch_edges['-1'],
       'distinct_unordered_winner_arc_pairs':30,
       'pair_and_slope_classes':35,
       'distinct_lifted_integer_shift_values':28,
       'one_exact_shift_per_pair_and_slope_class':True,
       'classes':rows,
       'canonical_307_edge_sha256':sha,
       'scope':'R284CZ frozen 307 equal-d64 source-neighbor edges, not all coincident sites'}
 Path(__file__).with_name('R284DB_translation_classes_certificate.json').write_text(
  json.dumps(cert,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
 print(json.dumps({k:v for k,v in cert.items() if k!='classes'},ensure_ascii=False))

if __name__=='__main__':main()
