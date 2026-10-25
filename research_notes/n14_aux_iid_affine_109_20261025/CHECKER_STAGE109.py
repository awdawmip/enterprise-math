#!/usr/bin/env python3
"""Full finite Bellman/first-hit/affine-primal rational check for Stage109."""
from fractions import Fraction as F
P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6)); N=14
A=(10,3,0); D=(10,3,3)
K=F(491857029,506348); L=F(116416632,126587); Gamma=K+L
alpha0=F(13084095824621807507,37682150988866125824)
V0=F(1934483126570299962385,150728603955464503296)
u0=F(159404052982303,211315200000000)
S=[(n,a,b) for n in range(N,-1,-1) for a in range(n+1) for b in range(n-a+1)]
def kids(s):
 n,a,b=s;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def R(s):return F(2**(s[1]+s[2]),3**s[1])
Dval={}; opts={}; gaps=[]
for s in S:
 cc={'P':K*R(s),'Q':L}
 if s[0]<N:cc['C']=1+sum((P[i]*Dval[t] for i,t in enumerate(kids(s))),F(0))
 v=min(cc.values());Dval[s]=v;opts[s]=tuple(a for a,x in cc.items() if x==v)
 gaps.extend(x-v for x in cc.values())
assert len(S)==680 and len(gaps)-len(S)==1240
assert {s for s in S if len(opts[s])>1}=={A,D}
assert sum(v>0 for v in gaps)==1238 and not any(v<0 for v in gaps)
assert min(v for v in gaps if v>0)==F(20261,759522)
assert Dval[0,0,0]==V0+Gamma*alpha0
pol={s:('C' if s in (A,D) else opts[s][0]) for s in S}
counts={(0,0,0):1}; pm={(0,0,0):F(1)};qm={(0,0,0):F(1)}
for n in range(N):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b)
   if s not in counts or s in (A,D) or pol[s]!='C':continue
   for i,t in enumerate(kids(s)):
    counts[t]=counts.get(t,0)+counts[s]
    pm[t]=pm.get(t,F(0))+pm[s]*P[i]
    qm[t]=qm.get(t,F(0))+qm[s]*Q[i]
assert (counts[A],pm[A],qm[A])==(120,F(390625,5971968),F(390625,20155392))
assert (counts[D],pm[D],qm[D])==(2051,F(1281875,9172942848),F(1281875,3869835264))
M={}
for s in S:
 act=pol[s]
 if act=='P':v=(F(0),F(1),F(0),F(0),1)
 elif act=='Q':v=(F(1),F(0),F(0),F(0),1)
 else:
  rows=[M[t] for t in kids(s)]
  v=(sum((P[i]*rows[i][0] for i in range(3)),F(0)),
     sum((Q[i]*rows[i][1] for i in range(3)),F(0)),
     1+sum((P[i]*rows[i][2] for i in range(3)),F(0)),
     1+sum((Q[i]*rows[i][3] for i in range(3)),F(0)),sum(row[4] for row in rows))
 M[s]=v
assert M[A]==(F(635,165888),F(10201,10368),F(7711,6912),F(1069,864),21)
assert M[D]==(F(4075,4096),F(31,20736),F(1955,1536),F(75,64),15)
x=-pm[A]*M[A][0];y=qm[A]*(1-M[A][1]);zP=pm[D]*(1-M[D][0]);zQ=-qm[D]*M[D][1]
du=(zP-zQ)/(y-x);eta=x*du+zP
assert eta==y*du+zQ
assert du==F(22757603,10565760000)
assert eta==F(23181244375,130840802044674048)
assert u0+du<1
def moments(u,w):
 T={}
 for s in S:
  acts={'P':u,'C':1-u} if s==A else {'Q':w,'C':1-w} if s==D else {pol[s]:F(1)}
  res=[F(0)]*4
  for act,pct in acts.items():
   if act=='P':v=(F(0),F(1),F(0),F(0))
   elif act=='Q':v=(F(1),F(0),F(0),F(0))
   else:
    rows=[T[t] for t in kids(s)]
    v=(sum((P[i]*rows[i][0] for i in range(3)),F(0)),
       sum((Q[i]*rows[i][1] for i in range(3)),F(0)),
       1+sum((P[i]*rows[i][2] for i in range(3)),F(0)),
       1+sum((Q[i]*rows[i][3] for i in range(3)),F(0)))
   for j in range(4):res[j]+=pct*v[j]
  T[s]=tuple(res)
 return T[0,0,0]
for w in (F(0),F(1,2),F(1)):
 eP,eQ,tP,tQ=moments(u0+du*w,w)
 assert eP==eQ==alpha0+eta*w
 assert tP==V0-Gamma*eta*w and tP>tQ
assert alpha0+eta==F(13084102500820187507,37682150988866125824)
assert V0-Gamma*eta==F(1934432626777903782385,150728603955464503296)
print('PASS_STAGE109_EXACT_680_STATES_1240_COMPARISONS_REAL_INTERVAL')
