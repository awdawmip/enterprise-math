#!/usr/bin/env python3
"""EC49BM exact independent finite reproducer; requires pinned source in repo."""
from collections import defaultdict
from fractions import Fraction
from hashlib import sha1
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product, permutations
from math import prod
from pathlib import Path
import json

pin="300a96e3dc24bf6fff73743037a0347a8bc83176"
rel=Path("experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py")
root=next(p for p in Path(__file__).resolve().parents if (p/rel).exists())
raw=(root/rel).read_bytes()
assert sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()==pin
spec=spec_from_file_location("signed_brc",root/rel); src=module_from_spec(spec); spec.loader.exec_module(src)
def d(w):
 z=[0]*6
 for t in w: z[t//2]+=1 if t%2==0 else -1
 return tuple(z)
def k(w):
 return tuple(w.count(2*i) for i in range(6))
def chi(w,wp,wm):
 return prod((wp[t//2] if t%2==0 else wm[t//2] for t in w),start=Fraction(1))
def sigma_word(w,s):return tuple(2*s[t//2]+t%2 for t in w)
W=[w for w in product(range(12),repeat=4) if d(w)==(0,)*6]
assert len(W)==396==src.endpoint_multiplicity(4,(0,)*6)
assert all(tuple(w.count(2*i+1) for i in range(6))==k(w) for w in W)
profiles=set(map(k,W)); assert len(profiles)==21
base={(w[0],w[-1]) for w in W}
aug={(w[0],w[-1],k(w)) for w in W}
assert len(base)==144 and len(aug)==204
pc=(3,5,7,11,13,17)
wc=(tuple(map(Fraction,pc)),tuple(Fraction(2,p) for p in pc))
ws=(tuple(map(Fraction,(2,2,2,2,2,3))),)*2
q0=tuple(a*b for a,b in zip(*wc));q1=tuple(a*b for a,b in zip(*ws))
assert len(set(wc[0]+wc[1]))==12 and q0==(Fraction(2),)*6
assert q1==tuple(map(Fraction,(4,4,4,4,4,9)))
perms=list(permutations(range(6)))
def sig(kv,q):return tuple(prod((q[s[i]]**kv[i] for i in range(6)),start=Fraction(1)) for s in perms)
c0={x:sig(x,q0) for x in profiles}
c1={x:sig(x,q1) for x in profiles}
assert len(set(c0.values()))==1 and len(set(c1.values()))==21
assert len({(w[0],w[-1],c0[k(w)]) for w in W})==144
assert len({(w[0],w[-1],c1[k(w)]) for w in W})==204
u=(0,2,3,1);v=(0,4,5,1);swap=(0,1,5,3,4,2)
assert (d(u),u[0],u[-1])==(d(v),v[0],v[-1])
assert chi(u,*wc)==chi(v,*wc)==4
assert chi(u,*ws)==chi(v,*ws)==16
assert chi(sigma_word(u,swap),*ws)==16 and chi(sigma_word(v,swap),*ws)==36
checks=0
for x in profiles:
 for i in range(1,6):
  a=[None]*6;a[0]=0;a[i]=5
  for j,y in zip((j for j in range(6) if j not in (0,i)),(1,2,3,4)):a[j]=y
  b=a[:];b[0],b[i]=b[i],b[0]
  ratio=prod((q1[a[j]]**x[j] for j in range(6)),start=Fraction(1))/prod((q1[b[j]]**x[j] for j in range(6)),start=Fraction(1))
  assert ratio==Fraction(9,4)**(x[i]-x[0]);checks+=1
assert checks==105
C=src.endpoint_weight(4,(0,)*6,*wc);S=src.endpoint_weight(4,(0,)*6,*ws)
assert C==sum((chi(w,*wc) for w in W),Fraction(0))==1584
assert S==sum((chi(w,*ws) for w in W),Fraction(0))==9126
print(json.dumps({"status":"EXACT_FINITE_PASS","native_blob":pin,"return_words":len(W),"histograms":len(profiles),"permutations":len(perms),"equal_q_classes":len(base),"unequal_q_classes":len(aug),"ratio_checks":checks,"native_aggregate_equal_q":str(C),"native_aggregate_unequal_q":str(S)},sort_keys=True))
