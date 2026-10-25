#!/usr/bin/env python3
"""Stage116 exact rational Bellman and full-real primal certificate."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
N=14;P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K=F(37550061,41440);L=F(3296576,3885);S=K+L
D=(9,1,2);T=(14,7,4)
a115=F(900390060440962701793,2592933255351443128320)
v115=F(132635694365041929281069,10371733021405772513280)
w115=F(374236473161181,1042086080000000)
def kids(s):
 n,a,b=s;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
@lru_cache(None)
def H(s):
 n,a,b=s
 costs={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<N:costs['C']=1+sum(p*H(ch) for p,ch in zip(P,kids(s)))
 return min(costs.values())
ss=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
acts={};strict=[]
for s in ss:
 n,a,b=s; costs={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<N:costs['C']=1+sum(p*H(ch) for p,ch in zip(P,kids(s)))
 acts[s]=[name for name,v in costs.items() if v==H(s)]
 strict += [v-H(s) for v in costs.values() if v>H(s)]
assert len(ss)==680 and len(strict)==1238
assert min(strict)==F(200314681163,7919307325440)
assert {s:a for s,a in acts.items() if len(a)>1}=={D:['Q','C'],T:['P','Q']}
@lru_cache(None)
def M(s,w,z):
 action='D' if s==D else 'T' if s==T else acts[s][0]
 if action=='P':return (F(0),F(1),F(0),F(0))
 if action=='Q':return (F(1),F(0),F(0),F(0))
 if action=='T':return (F(1)-z,z,F(0),F(0))
 def cont():
  c=[M(ch,w,z) for ch in kids(s)]
  return (sum(p*x[0] for p,x in zip(P,c)),sum(q*x[1] for q,x in zip(Q,c)),
          1+sum(p*x[2] for p,x in zip(P,c)),1+sum(q*x[3] for q,x in zip(Q,c)))
 if action=='D':
  x=cont();y=(F(1),F(0),F(0),F(0))
  return tuple(w*a+(1-w)*b for a,b in zip(y,x))
 return cont()
def root(w,z):return M((0,0,0),w,z)
def minus(x,y):return tuple(a-b for a,b in zip(x,y))
b=root(F(0),F(0));dw=minus(root(F(1),F(0)),b);dz=minus(root(F(0),F(1)),b)
assert dw==(F(593265625,5283615080448),F(-430671875,5015306502144),
            F(-34607609375,1981355655168),F(-17355203125,417942208512))
assert dz==(F(-614375,75144747810816),F(614375,80244904034304),F(0),F(0))
assert root(F(1),F(1))==tuple(b[i]+dw[i]+dz[i] for i in range(4))
rho=-(dz[0]-dz[1])/(dw[0]-dw[1])
assert rho==F(118943,1488694400)
endw=w115+rho
eta=(rho*dw[0]+dz[0])
a116=F(900390062503198401793,2592933255351443128320)
v116=F(132635679890866772493569,10371733021405772513280)
left=root(w115,F(0));right=root(endw,F(1))
assert left[:3]==(a115,a115,v115)
assert endw==F(374319733261181,1042086080000000)
assert eta==F(22731875,28581715777683456)
assert (right[0],right[1],right[2])==(a116,a116,v116)
assert H((0,0,0))==v115+S*a115 and v116==v115-S*eta
assert left[2]-left[3]==F(444360026883234885715,691448868093718167552)>0
assert right[2]-right[3]==F(1333084068027931219645,2074346604281154502656)>0
front={(0,0,0):(1,F(1),F(1))};hits={}
for n in range(N+1):
 for s in (D,T):
  if s in front and s[0]==n:hits[s]=front[s]
 if n==N:break
 nxt=defaultdict(lambda:(0,F(0),F(0)))
 for s,(count,pm,qm) in front.items():
  if s==D or acts[s][0]=='C':
   for ch,p,q in zip(kids(s),P,Q):
    cnt,pp,qq=nxt[ch];nxt[ch]=(cnt+count,pp+pm*p,qq+qm*q)
 front=nxt
assert hits[D]==(172,F(671875,53747712),F(671875,20155392))
assert hits[T]==(9830,F(614375,75144747810816),F(614375,80244904034304))
print('PASS_STAGE116_BELLMAN_AND_FULL_REAL_AFFINE')
