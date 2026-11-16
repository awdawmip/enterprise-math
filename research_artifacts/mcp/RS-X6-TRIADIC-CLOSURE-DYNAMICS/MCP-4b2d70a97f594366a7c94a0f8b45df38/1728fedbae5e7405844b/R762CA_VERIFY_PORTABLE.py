"""Exact finite R762CA verifier. No physical/native event licensing is inferred."""
from itertools import product, permutations
from collections import defaultdict, Counter
from math import factorial
import json
S=tuple(product((-1,1),repeat=3)); P=range(3); A=range(6); B=(0,1,2)
def rot(s,p=None):
 t=(s[2],s[0],s[1]); return t if p is None else (t,(p+1)%3)
def ref(s,p=None):
 t=(s[0],s[2],s[1]); return t if p is None else (t,(0,2,1)[p])
def flip(s,p=None):
 t=tuple(-a for a in s); return t if p is None else (t,p)
def orbit(X,G,root=False):
 unseen=set(X); result=[]
 while unseen:
  seed=min(unseen); seen={seed}; queue=[seed]
  for x in queue:
   for g in G:
    y=g(*x) if root else g(x)
    if y not in seen: seen.add(y); queue.append(y)
  assert seen<=unseen; unseen-=seen; result.append(tuple(sorted(seen)))
 return result
def classify(G):
 C=orbit(S,G); E=orbit([(s,p) for s in S for p in P],G,True)
 cl={s:i for i,o in enumerate(C) for s in o}; r=[0]*len(C)
 for o in E:
  z={cl[s] for s,p in o}; assert len(z)==1; r[z.pop()]+=1
 pairs=1
 for v in r: pairs*=1+2**v
 brute=sum(all(not (gm>>i&1) or (cm>>cl[o[0][0]]&1) for i,o in enumerate(E))
           for cm in range(2**len(C)) for gm in range(2**len(E)))
 assert brute==pairs
 return [len(C),len(E),pairs,sorted(r)]
metrics={"C3":classify([rot]),"D3":classify([rot,ref]),
 "C3_flip":classify([rot,flip]),"D3_flip":classify([rot,ref,flip])}
assert metrics=={"C3":[4,8,729,[1,1,3,3]],"D3":[4,6,225,[1,1,2,2]],
 "C3_flip":[2,4,27,[1,3]],"D3_flip":[2,3,15,[1,2]]}
def step(frame,s,p,y):
 if y in frame or s[p]!=1:return None
 return frame[:p]+(y,)+frame[p+1:]
cov_axis=0
for t in permutations(A):
 b=tuple(t[x] for x in B)
 for s in S:
  for p in P:
   for y in (3,4,5):
    d=step(B,s,p,y); e=step(b,s,p,t[y])
    assert (None if d is None else tuple(t[x] for x in d))==e
    cov_axis+=1
assert cov_axis==51840
cov_cycle=0
for b in permutations(A,3):
 rb=(b[2],b[0],b[1]); absent=set(A)-set(b)
 for s in S:
  for p in P:
   for y in absent:
    d=step(b,s,p,y); e=step(rb,rot(s),(p+1)%3,y)
    assert (None if d is None else (d[2],d[0],d[1]))==e
    cov_cycle+=1
assert cov_cycle==8640
summ=[]; by_k={}; signed_holonomy=[]
for s in S:
 k=sum(a==1 for a in s); dp={B:1}; vals=[]
 for m in range(9):
  returns={f:v for f,v in dp.items() if set(f)==set(B)}
  vals.append((sum(returns.values()),len(returns)))
  assert sum(dp.values())==(3*k)**m
  nd=defaultdict(int)
  for f,w in dp.items():
   for p in P:
    if s[p]==1:
     for y in set(A)-set(f): nd[f[:p]+(y,)+f[p+1:]]+=w
  dp=nd
 if k in by_k: assert by_k[k]==vals
 else: by_k[k]=vals
 summ.append(vals)
aggregate=[sum(summ[i][m][0] for i in range(8)) for m in range(9)]
by_length=[sum(summ[i][m][1] for i in range(8)) for m in range(9)]
assert aggregate==[8,0,36,108,846,5418,41580,324576,2664810]
assert by_length==[8,0,7,13,15,15,15,15,15]
assert sum(factorial(sum(a==1 for a in s)) for s in S)==16
print(json.dumps({"symmetry_metrics_closure_gate_coherent_and_bits":metrics,
 "covariance_checks":{"S6":cov_axis,"C3":cov_cycle},
 "sign_plus_return_m0_to_8":aggregate,"sign_plus_holonomy_signatures_m0_to_8":by_length,
 "sign_plus_by_k":{str(k):v for k,v in sorted(by_k.items())},
 "positive_sign_gate_k_multiplicity":dict(Counter(sum(a==1 for a in s) for s in S)),
 "all_lengths_holonomy_signatures":16,"independent_review":"NOT_REVIEWED",
 "native_TRIADIC_CLOSURE_E_license":"OPEN"},sort_keys=True,indent=2))
