#!/usr/bin/env python3
"""R324 independent exact-integer check of the BRC q=12 edge.
No SymPy or use of the lower-order symbolic proof expressions.
"""
from math import comb, factorial
import json
from pathlib import Path
TOP=192
PNUM=[531441,-20903346,-156538899,24419057850,-589075122537,5180686481322,39976532853543,-1658014965639450,21769552178530596,-161519782694967576,691580765570907456,-1417077340360041600,449369517758515200]
PDEN=16777216
QNUM=[9765625,-363281250,7145703125,-86743593750,663288759375,-3591743883750,13991452817375,-28159150504650,66872688629956,-223704270817368,-720738558196416,-545479132235904,2104890257885184]
QDEN=321452532301824
SHIFT=[9765625,1042968750,52005078125,1606053281250,34257886884375,530808187016250,6092940124382375,51722083655086350,318157241742680956,1361610809071604520,3783550721738548320,6040651471882507008,4182084966986809344]
assert len(PNUM)==len(QNUM)==len(SHIFT)==13
C=lambda n,k: comb(n,k) if n>=0 and 0<=k<=n else 0
def evalpoly(cs,x):
 y=0
 for c in cs:y=y*x+c
 return y
def add(a,b,scale=1):
 o=a+[0]*max(0,len(b)-len(a))
 for i,v in enumerate(b):o[i]+=scale*v
 while len(o)>1 and o[-1]==0:o.pop()
 return o
def mul(a,b):
 o=[0]*(len(a)+len(b)-1)
 for i,ai in enumerate(a):
  if ai:
   for j,bj in enumerate(b):
    if bj:o[i+j]+=ai*bj
 while len(o)>1 and o[-1]==0:o.pop()
 return o
def zp(k):return [(-1)**i*C(k,i) for i in range(k+1)]
def np(i):return [0,-C(3,i-1),-C(6,i-1),C(8,i-2)]
def dp(i):return [0,-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3)]
def moment(cs,r):return sum(v*factorial(j)//factorial(j-r) for j,v in enumerate(cs) if j>=r)
M=[[1]]
checks={"degree":0,"moment12":0,"newton12":0,"recovery":0,"shift":0,"lower_bound":0}
samples=[]
for s in range(TOP+1):
 if s:
  coeff=mul(np(s),zp(s))
  for i in range(1,min(s,12)+1):coeff=add(coeff,mul(mul(dp(i),M[s-i]),zp(i-1)),-1)
  M.append(coeff)
 coeff=M[s]
 assert len(coeff)-1<=2*s+1,(s,len(coeff)-1)
 checks['degree']+=1
 if s<12:continue
 mom=moment(coeff,12)
 assert mom*PDEN==2**s*evalpoly(PNUM,s),('m12',s)
 checks['moment12']+=1
 newt=sum(v*C(2*s+1-j,12) for j,v in enumerate(coeff))
 assert newt*QDEN==2**s*evalpoly(QNUM,s),('a12',s)
 checks['newton12']+=1
 recover=sum((-1)**r*C(2*s+1-r,12-r)*(moment(coeff,r)//factorial(r)) for r in range(13))
 assert recover==newt,('jet',s)
 checks['recovery']+=1
 assert evalpoly(QNUM,s)==evalpoly(SHIFT,s-12),('shift',s)
 checks['shift']+=1
 assert newt*4096>=53288801*2**s and newt>0,('lower_bound',s)
 checks['lower_bound']+=1
 if s<=15:samples.append({'s':s,'k':s-12,'a':str(newt),'m12':str(mom)})
assert all(n>0 for n in checks.values())
evidence={'schema':'R324_BRC_NEWTON_Q12_EXACT_V1','status':'PASS','scope':'ordered positive six-branch BRC auxiliary M_s, no native Cell lift','coverage':'s=0..192 for degree, s=12..192 for q12','q':12,'check_counts':checks,'samples':samples,'P12_num_desc':[str(x) for x in PNUM],'P12_den':str(PDEN),'Q12_num_desc':[str(x) for x in QNUM],'Q12_den':str(QDEN),'Q12_shift_num_desc':[str(x) for x in SHIFT],'normalized_minimum':'53288801/4096','method':'independent integer original recurrence; mathematical infinity from exact symbolic recurrence induction and positive shifted polynomial','not_verified':['general central q growing with s','original defect-fiber positivity','global peak 81','native six-dimensional Cell physics','independent Driver proof review']}
Path(__file__).parent.joinpath('R324_EXACT_EVIDENCE.json').write_text(json.dumps(evidence,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('PASS',checks)
print('SAMPLES',samples)
