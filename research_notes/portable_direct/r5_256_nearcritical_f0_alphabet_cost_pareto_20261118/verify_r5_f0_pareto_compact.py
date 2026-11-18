#!/usr/bin/env python3
"""Exact full-256 f=0 near-critical global-budget Pareto certificate.
Usage: python3 verify_r5_f0_pareto_compact.py EXACT_R5_ALL_101_BUDGETS.json
"""
import hashlib,itertools,json,sys
from functools import lru_cache
from collections import Counter
S='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
T=1876919155234970890319953920000
D=1882951873548292168718745600000
raw=open(sys.argv[1],'rb').read();assert hashlib.sha256(raw).hexdigest()==S
J=json.loads(raw); K=tuple(range(214,315));H=range(256)
N={k:tuple(map(int,J['counts_and_cohorts'][str(k)]['counts'])) for k in K}
assert all(len(v)==256 for v in N.values())

def supports(c,t):
 o=sorted(H,key=lambda h:(c[h],h));r=0;windows=[]
 for l in H:
  r=max(l,r)
  while r<256 and c[o[r]]-c[o[l]]<=t:r+=1
  windows.append(sum(1<<o[z] for z in range(l,r)))
 w=set(windows)
 return tuple(sorted(a for a in w if not any(a!=b and a&b==a for b in w)))
M={k:supports(N[k],D-1) for k in K}
assert M=={k:supports(N[k],T) for k in K}
P=list(itertools.combinations(H,2));ALL=(1<<len(P))-1
B={k:sum(1<<i for i,(a,b) in enumerate(P) if abs(N[k][a]-N[k][b])>=D) for k in K}
assert [k for k in K if abs(N[k][11]-N[k][14])>=D]==[217]
other=tuple(k for k in K if k!=217)
assert not any((B[217]|B[a]|B[b])==ALL for a,b in itertools.combinations(other,2))
four=[(217,a,b,c) for a,b,c in itertools.combinations(other,3) if B[217]|B[a]|B[b]|B[c]==ALL]
assert set(four)=={(217,a,m,v) for a in (218,219) for m in range(224,291) for v in range(298,312)}

def value(alphabet):
 @lru_cache(None)
 def V(s):
  if s.bit_count()==1:return 0
  best=10**8
  for k in alphabet:
   if k>=best:break
   children={s&c for c in M[k]}-{0}
   if s in children:continue
   worst=0
   for x in children:
    worst=max(worst,V(x))
    if k+worst>=best:break
   best=min(best,k+worst)
  return best
 ans=V((1<<256)-1)
 return ans,V.cache_info().currsize
hist=Counter()
for A in four:
 v,_=value(A);assert v==sum(A);hist[v]+=1
assert len(four)==1876 and hist[957]==1 and min(hist)==957
v5,s5=value((215,217,218,224,298))
va,sa=value(K)
assert v5==va==955
assert value((217,218,224,298))[0]==957
print(json.dumps({'status':'PASS_R5_FULL256_F0_NEARCRITICAL_GLOBAL_ALPHABET_PARETO',
 'input_sha256':S,'tau_left_inclusive':str(T),'tau_right_exclusive':str(D),
 'pair_count':len(P),'four_alphabets_tested':len(four),
 'four_type_minimum':957,'four_type_unique_minimizer':[217,218,224,298],
 'four_type_cost_eq_sum':True,'four_type_cost_histogram':dict(sorted(hist.items())),
 'five_type_witness':[215,217,218,224,298],'five_type_value':v5,
 'full_101_budget_value':va,'five_type_memo_states':s5,'full_memo_states':sa,
 'pareto':{'m_le_3':'infeasible','m_4':957,'m_ge_5':955}},indent=2)
