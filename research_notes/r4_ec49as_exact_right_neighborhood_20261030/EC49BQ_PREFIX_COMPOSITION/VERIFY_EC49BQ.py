#!/usr/bin/env python3
"""EC49BQ published exact native-BRC census and rank verifier (Python 3, SymPy)."""
import hashlib, importlib.util, json
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from sympy import Matrix
here=Path(__file__).resolve()
paths=(here.with_name('signed_brc.py'),here.parents[3]/'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py')
p=next((x for x in paths if x.is_file()),None)
if p is None:raise FileNotFoundError('native signed_brc.py missing')
b=p.read_bytes(); blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
assert blob=='300a96e3dc24bf6fff73743037a0347a8bc83176'
spec=importlib.util.spec_from_file_location('native_brc',p); m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
D=tuple(range(1,7))+tuple(range(-1,-7,-1)); Q=(2,3,3,2,1,1); WP=tuple(map(F,Q)); WM=(F(1),)*6; Z=(0,)*6
def delta(w):
 v=[0]*6
 for s in w:v[abs(s)-1]+=1 if s>0 else -1
 return tuple(v)
def wt(w):
 a=F(1)
 for s in w:a*=WP[s-1] if s>0 else WM[-s-1]
 return a
def mid(p,s):return tuple(-a-b for a,b in zip(delta(p),delta(s)))
W=[w for w in product(D,repeat=4) if delta(w)==Z]
assert len(W)==m.endpoint_multiplicity(4,Z)==396
assert sum(map(wt,W),F())==m.endpoint_weight(4,Z,WP,WM)==1560
pairs=defaultdict(list)
for w in W:pairs[w[:1],w[-1:]].append(w)
assert len(pairs)==144
for p,s in product([(d,) for d in D],repeat=2):
 v=pairs[p,s]; z=mid(p,s)
 assert len(v)==m.endpoint_multiplicity(2,z)
 assert sum(map(wt,v),F())==wt(p)*m.endpoint_weight(2,z,WP,WM)*wt(s)
assert Counter(map(len,pairs.values()))==Counter({1:12,2:120,12:12})
rows=[[wt(w) if w[0]==d else F() for w in W] for d in D]
rows += [[wt(w) if w[-1]==d else F() for w in W] for d in D]
r=Matrix(rows).rank();rc=Matrix(rows+[[1]*len(W)]).rank();assert(r,rc)==(23,24)
assert any(len({wt(w) for w in v})>1 for v in pairs.values())
def t(a,b):return(a,-a,-b,b)
A=(t(1,2),t(4,3));B=(t(1,3),t(4,2))
def one(E):return(len(E),[sum((wt(w) for w in E if w[0]==d),F()) for d in D],[sum((wt(w) for w in E if w[-1]==d),F()) for d in D])
assert one(A)==one(B)
assert sum((wt(w) for w in A if(w[0],w[-1])==(1,2)),F())==6
assert sum((wt(w) for w in B if(w[0],w[-1])==(1,2)),F())==0
count6=sum(m.endpoint_multiplicity(4,mid(p,s)) for p,s in product([(d,) for d in D],repeat=2))
w6=sum((wt(p)*m.endpoint_weight(4,mid(p,s),WP,WM)*wt(s) for p,s in product([(d,) for d in D],repeat=2)),F())
assert count6==m.endpoint_multiplicity(6,Z)==19920
assert w6==m.endpoint_weight(6,Z,WP,WM)==152640
print(json.dumps({'unit':'EC49BQ','native_blob':blob,'n4_closed_words':len(W),'n4_native_endpoint_weight':1560,'n4_joint_fibres':len(pairs),'n4_native_fibres_verified':144,'one_shot_rank':r,'one_shot_plus_count_rank':rc,'composed_rank':144,'composed_plus_count_rank':145,'counterexample_joint_A_B':[6,0],'n6_closed_words_via_native':count6,'n6_weight_via_native':str(w6),'status':'AUTHOR_EXACT_PASS_UNREVIEWED'},sort_keys=True,indent=2))
