#!/usr/bin/env python3
"""EC49BP exact audit; byte-pinned native signed_brc.py from same repo."""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
import importlib.util, json
from sympy import Matrix
here=Path(__file__).resolve()
candidates=(here.with_name('signed_brc.py'),here.parents[3]/'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py')
p=next((z for z in candidates if z.is_file()),None)
if p is None:raise FileNotFoundError('pinned signed_brc.py missing; copy from experiments/x6_signed_native_spatial_v16_20260905')
b=p.read_bytes()
assert sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()=='300a96e3dc24bf6fff73743037a0347a8bc83176'
spec=importlib.util.spec_from_file_location('native_brc',p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
q=(2,3,3,2,1,1)
def ks(K,d=6):
 if d==1:yield (K,);return
 for i in range(K+1):
  for r in ks(K-i,d-1):yield (i,)+r
def words(k):
 c=Counter({s:v for i,v in enumerate(k,1) for s in (i,-i) if v}); w=[]
 def rec():
  if len(w)==2*sum(k):yield tuple(w);return
  for s in sorted(c):
   if c[s]:
    c[s]-=1;w.append(s);yield from rec();w.pop();c[s]+=1
 yield from rec()
def sw(w):return tuple((2 if s==1 else 1 if s==2 else -2 if s==-1 else -1 if s==-2 else s) for s in w)
def wt(w):
 a=F(1)
 for s in w:
  if s>0:a*=q[s-1]
 return a
def atom(w):return tuple(int(i in {abs(t) for t in w}) for i in (1,2,3))
klist=list(ks(2)); W=sorted(w for k in klist for w in words(k))
assert len(W)==396==len(set(W))
assert m.endpoint_multiplicity(4,(0,)*6)==396
assert sum(map(wt,W),F(0))==m.endpoint_weight(4,(0,)*6,tuple(map(F,q)),(1,)*6)==1560
assert all(wt(tuple(-s for s in reversed(w)))==wt(w) for w in W)
assert all(sw(w) in W for w in W)
A=sorted({atom(w) for w in W});assert len(A)==7
reps=[next(words(k)) for k in klist]
def matrix(X):
 rows=[[1 for w in X],[wt(w) for w in X],[wt(sw(w)) for w in X]]
 for a in A:
  for f in (wt,lambda w:wt(sw(w))):rows.append([int(atom(w)==a)*f(w) for w in X])
 return rows
r0=Matrix(matrix(W)[:3]).rank();r1=Matrix(matrix(W)).rank()
assert (r0,r1)==(3,10) and Matrix(matrix(reps)).rank()==r1
x=((5,1,-1,-5),(5,2,-2,-5));y=((5,3,-3,-5),(5,4,-4,-5))
agg=lambda E:(sum(map(wt,E),F(0)),sum((wt(sw(z)) for z in E),F(0)))
flt=lambda E:sum((wt(z) for z in E if 1 in {abs(s) for s in z}),F(0))
assert agg(x)==agg(y)==(5,5) and (flt(x),flt(y))==(2,0)
for c in ((4,),(-2,5),(1,-1)):
 for w in W:
  assert wt(c+w)==wt(c)*wt(w)
  assert all((i in {abs(s) for s in c+w})==((i in {abs(s) for s in c}) or (i in {abs(s) for s in w})) for i in (1,2,3))
print(json.dumps({'unit':'EC49BP','native_blob':'300a96e3dc24bf6fff73743037a0347a8bc83176','words':396,'native_endpoint_weight':1560,'histograms':21,'atoms':7,'candidate_rows':17,'unfiltered_rank_Q':r0,'filtered_rank_Q':r1,'context_checks':1188,'ensembles_orbit':[5,5],'filter_axis1':[2,0],'status':'AUTHOR_EXACT_AUDIT_PASS_UNREVIEWED'},sort_keys=True,indent=2))
