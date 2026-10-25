#!/usr/bin/env python3
"""Exact Stage114 Bellman + feasible optimal-real-segment certificate; Python stdlib."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K=F(1903247523,2052316); L=F(443700120,513079)
A=(10,3,0);D=(9,1,2)
ALPHA=F(183184813761431567431,527550113844125761536)
VALUE=F(27026770528279165031729,2110200455376503046144)
U=F(929342188946273,986137600000000)

def kids(s):
 n,a,b=s;return (n+1,a+1,b),(n+1,a,b+1),(n+1,a,b)
def values(s,v):
 n,a,b=s
 z={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<14:z['C']=1+sum((p*v(c) for p,c in zip(P,kids(s))),F(0))
 return z
@lru_cache(None)
def bell(s):return min(values(s,bell).values())
ss=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
choices={s:[act for act,cost in values(s,bell).items() if cost==bell(s)] for s in ss}
assert len(ss)==680
assert {s:act for s,act in choices.items() if len(act)>1}=={A:['P','C'],D:['Q','C']}
gaps=[v-bell(s) for s in ss for v in values(s,bell).values() if v!=bell(s)]
assert len(gaps)==1238 and min(gaps)==F(11023,9235422) and all(g>0 for g in gaps)

@lru_cache(None)
def moments(s,u,w):
 act=choices[s][0]
 def c():
  r=[moments(ch,u,w) for ch in kids(s)]
  return (sum((p*x[0] for p,x in zip(P,r)),F(0)),
          sum((q*x[1] for q,x in zip(Q,r)),F(0)),
          1+sum((p*x[2] for p,x in zip(P,r)),F(0)),
          1+sum((q*x[3] for q,x in zip(Q,r)),F(0)))
 if s==A:
  t=c();return tuple(u*x+(1-u)*y for x,y in zip((F(0),F(1),F(0),F(0)),t))
 if s==D:
  t=c();return tuple(w*x+(1-w)*y for x,y in zip((F(1),F(0),F(0),F(0)),t))
 if act=='P':return F(0),F(1),F(0),F(0)
 if act=='Q':return F(1),F(0),F(0),F(0)
 return c()
def root(u,w):return moments((0,0,0),u,w)
def minus(a,b):return tuple(x-y for x,y in zip(a,b))
b=root(F(0),F(0));du=minus(root(F(1),F(0)),b);dw=minus(root(F(0),F(1)),b)
assert minus(root(F(1),F(1)),tuple(b[i]+du[i]+dw[i] for i in range(4)))==(F(0),)*4
assert root(U,F(0))[:3]==(ALPHA,ALPHA,VALUE)
gamma=-(dw[0]-dw[1])/(du[0]-du[1])
assert gamma==F(465217,1320720)
wmax=(1-U)/gamma;assert wmax==F(170386233161181,1042086080000000)
eta=(gamma*du[0]+dw[0])*wmax
assert eta==F(594704749143575417,150993774647608376033280)
alpha114=ALPHA+eta; V114=VALUE-(K+L)*eta
assert alpha114==F(900372060659842701793,2592933255351443128320)
assert V114==F(132764620121352969281069,10371733021405772513280)
left=root(U,F(0));right=root(F(1),wmax)
assert right[:3]==(alpha114,alpha114,V114)
assert left[2]>left[3] and right[2]>right[3]
assert bell((0,0,0))==VALUE+(K+L)*ALPHA
# Forward count+positive rational first-hit carrier; count state merges only after scoped observer proof.
front={(0,0,0):(1,F(1),F(1))}
for _ in range(9):
 nxt=defaultdict(lambda:(0,F(0),F(0)))
 for s,(count,pm,qm) in front.items():
  if choices[s][0]!='C':continue
  for kid,p,q in zip(kids(s),P,Q):
   c0,p0,q0=nxt[kid];nxt[kid]=(c0+count,p0+pm*p,q0+qm*q)
 front=nxt
assert front[D]==(172,F(671875,53747712),F(671875,20155392))
@lru_cache(None)
def conditional(s):
 if s==D:act='C'
 else:act=choices[s][0]
 if act=='P':return F(0),F(1),F(0),F(0)
 if act=='Q':return F(1),F(0),F(0),F(0)
 r=[conditional(ch) for ch in kids(s)]
 return (sum((p*x[0] for p,x in zip(P,r)),F(0)),
         sum((q*x[1] for q,x in zip(Q,r)),F(0)),
         1+sum((p*x[2] for p,x in zip(P,r)),F(0)),
         1+sum((q*x[3] for q,x in zip(Q,r)),F(0)))
assert conditional(D)==(F(97421,98304),F(641,248832),F(51509,36864),F(25831,20736))
assert dw==(front[D][1]*(1-conditional(D)[0]),-front[D][2]*conditional(D)[1],-front[D][1]*conditional(D)[2],-front[D][2]*conditional(D)[3])
print('PASS_STAGE114_EXACT_680_1238_2_TIES_172_FIRST_HIT_SHARP_ENDPOINT')
print('alpha114=',alpha114,'V114=',V114,'eta=',eta,'wmax=',wmax)
