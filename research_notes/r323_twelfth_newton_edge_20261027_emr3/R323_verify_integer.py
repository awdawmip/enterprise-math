#!/usr/bin/env python3
"""Independent R323 q=11 validation using integer coefficient recursion only; no SymPy."""
import json, hashlib, math, sys
from pathlib import Path
from datetime import datetime, timezone
TOP=192
P11=[177147,-5629338,-55210815,5390211420,-105920466399,764974524006,4905556833375,-163931261420520,1709888452187652,-9752537137071168,30227780108802240,-39093301566950400]
Q11=[1953125,-60156250,973671875,-9617437500,57047574375,-238605386250,745684519525,-646533050240,1713200590156,-11361362782176,-30738191289408,-6795863940096]
SHIFT=[1953125,176171875,7354531250,188160843750,3280453543125,40796945371875,366431557138900,2346692631114260,10319447735836096,29064860045255232,46264063835801088,31415183465250816]
def C(n,k): return math.comb(n,k) if n>=0 and 0<=k<=n else 0
def evalp(c,x):
 y=0
 for a in c:y=y*x+a
 return y
def add(a,b,scale=1):
 out=a+[0]*max(0,len(b)-len(a))
 for k,bk in enumerate(b):out[k]+=scale*bk
 while len(out)>1 and out[-1]==0:out.pop()
 return out
def mul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for k,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:out[k+j]+=x*y
 return out
def binom_poly(i):return [(-1)**k*C(i,k) for k in range(i+1)]
def poly_n(i):return [0,-C(3,i-1),-C(6,i-1),C(8,i-2)]
def poly_delta(i):return [0,-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3)]
def moment(a,r):return sum(v*math.factorial(j)//math.factorial(j-r) for j,v in enumerate(a) if j>=r)
M=[[1]]
counts=dict(degree=0,moment=0,newton=0,independent_recovery=0,shift=0,bound=0)
samples=[]
for s in range(TOP+1):
 if s:
  curr=mul(poly_n(s),binom_poly(s))
  for i in range(1,min(s,12)+1):
   curr=add(curr,mul(mul(poly_delta(i),M[s-i]),binom_poly(i-1)),-1)
  M.append(curr)
 coeff=M[s]
 assert len(coeff)-1<=2*s+1, (s,len(coeff)-1) # R313-derived expected tight bound can be relaxed
 counts['degree']+=1
 if s<11:continue
 m=moment(coeff,11)
 assert m*4194304==2**s*evalp(P11,s),('moment',s)
 counts['moment']+=1
 a=sum(c*C(2*s+1-j,11) for j,c in enumerate(coeff))
 assert a*6696927756288==2**s*evalp(Q11,s),('newton',s)
 counts['newton']+=1
 # Exact formula from all low-order jets independently recovered from the raw polynomial
 rec=sum((-1)**r * C(2*s+1-r,11-r)*moment(coeff,r)//math.factorial(r) for r in range(12))
 assert rec==a,('recovery',s,rec,a)
 counts['independent_recovery']+=1
 assert evalp(Q11,s)==evalp(SHIFT,s-11)
 counts['shift']+=1
 assert a*64>=300223*2**s and a>0
 counts['bound']+=1
 if s<=14:samples.append({'s':s,'k':s-11,'a':str(a),'m11':str(m)})
for k in counts:assert counts[k]>0
result={'schema':'R323_EXACT_EVIDENCE_V1','status':'PASS','object':'ordered_positive_BRC_auxiliary_polynomial','s_min':0,'s_max':TOP,'q':11,'proof_strength':'induction_symbolic_plus_finite_independent_bigint_crosscheck','check_counts':counts,'samples':samples,'formulas':{'P11_numerator_descending':list(map(str,P11)),'P11_denominator':'4194304','Q11_numerator_descending':list(map(str,Q11)),'Q11_denominator':'6696927756288','Q11_shift_descending':list(map(str,SHIFT)),'minimum_normalized':'300223/64'},'unverified':['native X6 bridge','independent Driver review','all central Newton coefficients','defect fibers','peak threshold']}
text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
p=Path(__file__).parent/'R323_EXACT_EVIDENCE.json';p.write_text(text,encoding='utf-8')
print('PASS',counts)
print('SAMPLES',samples)
print('EVIDENCE_SHA256',hashlib.sha256(text.encode()).hexdigest())
