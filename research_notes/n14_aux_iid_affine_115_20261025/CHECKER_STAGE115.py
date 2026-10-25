#!/usr/bin/env python3
"""Exact rational Stage115 Bellman and primal affine certificate, standard library."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
N=14; P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6))
K=F(2533113,2734); L=F(1181272,1367)
D=(9,1,2); E=(12,4,1)
alpha114=F(900372060659842701793,2592933255351443128320)
V114=F(132764620121352969281069,10371733021405772513280)
w114=F(170386233161181,1042086080000000)
def kids(s):
 n,a,b=s
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
@lru_cache(None)
def H(s):
 n,a,b=s
 vals={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<N:vals['C']=1+sum(p*H(c) for p,c in zip(P,kids(s)))
 return min(vals.values())
states=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
choice={}; gaps=[]
for s in states:
 n,a,b=s
 vals={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<N:vals['C']=1+sum(p*H(c) for p,c in zip(P,kids(s)))
 choice[s]=[a for a,c in vals.items() if c==H(s)]
 gaps.extend(c-H(s) for c in vals.values() if c>H(s))
assert len(states)==680 and len(gaps)==1238
assert min(gaps)==F(11023,7086528)
assert {s:c for s,c in choice.items() if len(c)>1}=={D:['Q','C'],E:['P','C']}
@lru_cache(None)
def moments(s,w,v):
 act=choice[s][0]
 def cont():
  k=[moments(ch,w,v) for ch in kids(s)]
  return (sum(p*y[0] for p,y in zip(P,k)),
          sum(q*y[1] for q,y in zip(Q,k)),
          1+sum(p*y[2] for p,y in zip(P,k)),
          1+sum(q*y[3] for q,y in zip(Q,k)))
 if s==D:
  c=cont()
  return tuple(w*x+(1-w)*y for x,y in zip((F(1),F(0),F(0),F(0)),c))
 if s==E:
  c=cont()
  return tuple(v*x+(1-v)*y for x,y in zip((F(0),F(1),F(0),F(0)),c))
 if act=='P':return (F(0),F(1),F(0),F(0))
 if act=='Q':return (F(1),F(0),F(0),F(0))
 return cont()
def root(w,v):return moments((0,0,0),w,v)
b=root(F(0),F(0))
dw=tuple(root(F(1),F(0))[i]-b[i] for i in range(4))
dv=tuple(root(F(0),F(1))[i]-b[i] for i in range(4))
assert dw==(F(593265625,5283615080448),F(-430671875,5015306502144),F(-34607609375,1981355655168),F(-17355203125,417942208512))
assert dv==(F(-9921875,660451885056),F(9921875,417942208512),F(-248046875,27518828544),F(-128984375,34828517376))
assert root(F(1),F(1))==tuple(b[i]+dw[i]+dv[i] for i in range(4))
assert root(w114,F(0))[:3]==(alpha114,alpha114,V114)
gamma=-(dv[0]-dv[1])/(dw[0]-dw[1])
assert gamma==F(637032,3256519)
wstar=w114+gamma
eta=gamma*dw[0]+dv[0]
end=root(wstar,F(1))
assert wstar==F(374236473161181,1042086080000000)
assert eta==F(2712640625,390765645398016)
assert end[:2]==(alpha114+eta,alpha114+eta)
assert end[0]==F(900390060440962701793,2592933255351443128320)
assert end[2]==F(132635694365041929281069,10371733021405772513280)
assert end[2]==V114-(K+L)*eta
assert H((0,0,0))==V114+(K+L)*alpha114
assert root(w114,F(0))[2]>root(w114,F(0))[3] and end[2]>end[3]
front={(0,0,0):(1,F(1),F(1))}
first={}
for depth in range(15):
 for s in (D,E):
  if s in front and s[0]==depth:first[s]=front[s]
 if depth==14:break
 nxt=defaultdict(lambda:(0,F(0),F(0)))
 for s,(count,pm,qm) in front.items():
  if s in (D,E) or choice[s][0]=='C':
   for ch,p,q in zip(kids(s),P,Q):
    count0,p0,q0=nxt[ch]
    nxt[ch]=(count0+count,p0+pm*p,q0+qm*q)
 front=nxt
assert first[D]==(172,F(671875,53747712),F(671875,20155392))
assert first[E]==(3048,F(9921875,1146617856),F(9921875,2902376448))
print('PASS_STAGE115_EXACT_BELLMAN_680_1238_2_TIES_FULL_REAL_SHARP')
