#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction as F
from itertools import product,permutations,combinations
import json,hashlib
R=Path(__file__).resolve().parent; RID="EM-R059D-9C6B2A"; TASK="89cb38967d0780d40d06f528deb73640f398cb89"; PAR="7ec96d50055203293fe1161264246e1ccba88c84"; C=[]
def ck(n,x):
 C.append(n)
 if not x: raise AssertionError(n)
def L(n): return json.loads((R/n).read_text())
def e(n,i): return tuple(1 if k==i else 0 for k in range(n))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def ax(v): return tuple(i for i,x in enumerate(v) if x)
def rk(vs):
 A=[list(map(F,v)) for v in vs]; m=len(A); n=len(A[0]); r=0
 for c in range(n):
  p=next((i for i in range(r,m) if A[i][c]),None)
  if p is None: continue
  A[r],A[p]=A[p],A[r]; q=A[r][c]; A[r]=[x/q for x in A[r]]
  for i in range(m):
   if i!=r and A[i][c]:
    q=A[i][c]; A[i]=[A[i][j]-q*A[r][j] for j in range(n)]
  r+=1
 return r
req=["FULL_D12_STRAIGHTNESS_PROTOCOL","UNORIENTED_AXIS_PARTITION","IMMEDIATE_REVERSAL_AUDIT","AXIS_ORIENTATION_FACTORIZATION","FULL_AXIS_MEMORY_CREDIT","MEMORY_MINIMALITY_LEDGER","FIXED_RECIPIENT_REDUCTION","S4_AXIS_SYMMETRY_NOGO","ORIENTATION_FIBER_CONTEXT_PROTOCOL","D_DIMENSIONAL_FULL_STRAIGHTNESS_LEDGER","TRIVIALITY_LEAKAGE_LEDGER"]
for x in req:
 o=L("R059D_STAGE_T_"+x+".json"); ck("meta-"+x,o["researcher_id"]==RID and o["taskbook_source"]==TASK and o["frozen_parent"]==PAR)
D=[sub(e(4,i),e(4,j)) for i in range(4) for j in range(4) if i!=j]; A=sorted(set(ax(v) for v in D))
ck("D12",len(set(D))==12); ck("axes6",len(A)==6)
for x,y in combinations(D,2): ck("dep"+str((x,y)),(rk([x,y])==1)==(y==neg(x)))
for n in range(1,4):
 for s in product(D,repeat=n): ck("hist"+str((n,s)),(rk(s)==1)==(len({ax(v) for v in s})==1))
for v in D: ck("rev"+str(v),rk([v,neg(v)])==1)
P=list(permutations(range(4))); a=(0,1); O={tuple(sorted((p[a[0]],p[a[1]]))) for p in P}; S=[p for p in P if tuple(sorted((p[0],p[1])))==a]
ck("S4orbit",len(O)==6); ck("S4stab",len(S)==4)
inv=[]
for mask in range(64):
 Z={A[k] for k in range(6) if mask>>k&1}
 if all({tuple(sorted((p[i],p[j]))) for i,j in Z}==Z for p in P): inv.append(mask)
ck("S4inv",inv==[0,63])
M=L("R059D_STAGE_T_MEMORY_MINIMALITY_LEDGER.json"); ck("mem6",M["minimum_context_cardinality"]==6)
for i in range(4):
 Z=[sub(e(4,i),e(4,j)) for j in range(4) if j!=i]; ck("fixed"+str(i),len({ax(v) for v in Z})==3 and all(neg(v) not in Z for v in Z))
for d in range(2,11):
 n=d+1; Z=[sub(e(n,i),e(n,j)) for i in range(n) for j in range(n) if i!=j]
 ck("dc"+str(d),len(set(Z))==d*(d+1) and len({ax(v) for v in Z})==d*(d+1)//2)
 for x,y in combinations(Z,2): ck("dd"+str((d,x,y)),(rk([x,y])==1)==(ax(x)==ax(y)))
Q=L("R059D_STAGE_T_TRIVIALITY_LEAKAGE_LEDGER.json"); ck("parent",Q["status"]=="PASS" and Q["gates"]["stage_s_and_earlier_immutable"]=="PASS_BY_GITHUB_COMPARE_PRE_MANIFEST")
for k,v in Q["gates"].items():
 if k!="stage_s_and_earlier_immutable": ck("fw-"+k,v is False)
dig=hashlib.sha256("\n".join(C).encode()).hexdigest()
out={"schema":"R059D_STAGE_T_DETERMINISTIC_CHECKER_OUTPUT_V1","status":"PASS","researcher_id":RID,"taskbook_source":TASK,"frozen_parent":PAR,"checks_total":len(C),"checks_passed":len(C),"checks_failed":0,"checks_digest_sha256":dig,"parent_immutability":"PASS_BY_GITHUB_COMPARE_PRE_MANIFEST","methods":{"proof_core":"primitive-support/rank/group-action/cardinality theorems","enumeration":"finite oracle only"}}
(R/"R059D_STAGE_T_DETERMINISTIC_CHECKER_OUTPUT.json").write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
print(json.dumps(out,indent=2))
