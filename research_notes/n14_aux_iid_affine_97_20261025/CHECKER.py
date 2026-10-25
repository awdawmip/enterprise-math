#!/usr/bin/env python3
"""Portable author-side exact-rational Stage97 checker, Python stdlib only."""
from fractions import Fraction as F
from functools import cache
from collections import defaultdict
from math import factorial
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6));N=14
A=(4,4,0);B=(12,0,1);K=F(893307577584960,619337901137)
LP=F(72)+F(8,9)*K;G=LP+K
alpha0=F(5172538010899325243,14900301753911083008)
V0=F(24246604065543953699,1862537719238885376)
s0=F(8237051660682949,13926400000000000)
def child(v,i):
 n,a,b=v;return n+1,a+(i==0),b+(i==1)
@cache
def bell(v):
 n,a,b=v
 opts={'P':K*F(2**(a+b),3**a),'Q':LP}
 if n<14:opts['C']=1+sum((P[i]*bell(child(v,i))[0] for i in range(3)),F())
 x=min(opts.values());z=next(z for z in ('C','P','Q') if z in opts and opts[z]==x)
 return x,z,opts
def first(v):
 state={(0,0):(F(1),F(1),1)}
 for n in range(v[0]):
  future=defaultdict(lambda:(F(),F(),0))
  for (a,b),(p,q,c) in state.items():
   if bell((n,a,b))[1]!='C':continue
   for i in range(3):
    w=a+(i==0),b+(i==1);x,y,z=future[w]
    future[w]=x+p*P[i],y+q*Q[i],z+c
  state=dict(future)
 return state.get(v[1:],(F(),F(),0))
@cache
def suffix(v):
 z=bell(v)[1]
 if z=='P':return F(),F(1),F(),F()
 if z=='Q':return F(1),F(),F(),F()
 kids=[suffix(child(v,i)) for i in range(3)]
 return (sum((P[i]*kids[i][0] for i in range(3)),F()),
         sum((Q[i]*kids[i][1] for i in range(3)),F()),
         F(1)+sum((P[i]*kids[i][2] for i in range(3)),F()),
         F(1)+sum((Q[i]*kids[i][3] for i in range(3)),F()))
def forward(u,s):
 state={(0,0):(F(1),F(1))};ep=eq=tp=tq=F()
 for n in range(15):
  future=defaultdict(lambda:(F(),F()))
  for (a,b),(p,q) in state.items():
   v=n,a,b
   if v==A:eq+=q*u;p*=1-u;q*=1-u
   elif v==B:ep+=p*s;p*=1-s;q*=1-s
   else:
    z=bell(v)[1]
    if z=='P':eq+=q;continue
    if z=='Q':ep+=p;continue
   assert n<N
   tp+=p;tq+=q
   for i in range(3):
    w=a+(i==0),b+(i==1);x,y=future[w]
    future[w]=x+p*P[i],y+q*Q[i]
  state=dict(future)
 assert not state
 return ep,eq,tp,tq
def check():
 root=bell((0,0,0))[0];assert bell.cache_info().currsize==680
 gaps=[];ties=[]
 for n in range(15):
  for a in range(n+1):
   for b in range(n-a+1):
    v=n,a,b;x,z,opts=bell(v)
    for alt,y in opts.items():
     if alt==z:continue
     gaps.append(y-x)
     if y==x:ties.append((v,z,alt))
 assert len(gaps)==1240 and gaps.count(0)==2
 assert all(x>=0 for x in gaps)
 assert min(x for x in gaps if x>0)==F(19154578828699,237825754036608)
 assert set(ties)=={(A,'C','P'),(B,'C','Q')}
 pA,qA,na=first(A);pB,qB,nb=first(B)
 assert na==1 and nb==12 and (pA,qA)==(F(1,4096),F(1,20736))
 RA,RB=suffix(A),suffix(B)
 assert RA==(F(100522980343,63403380965376),F(61173201761,61917364224),
             F(3374593929691,2641807540224),F(8332602073,5159780352))
 assert RB==(F(63,64),F(1,144),F(9,8),F(13,12))
 X=pA*RA[0];Y=qA*(1-RA[1]);E=pB*(1-RB[0]);H=qB*RB[1]
 h=(X+Y)/(E+H);eta=E*h-X
 assert h==F(813388768063,1671168000000000)
 assert eta==F(619337901137,4966767251303694336)
 assert 0<s0<s0+h<1
 assert root==V0+G*alpha0
 for u in (F(),F(1,101),F(1,7),F(1,3),F(2,3),F(97,101),F(1)):
  ep,eq,tp,tq=forward(u,s0+h*u)
  assert ep==eq==alpha0+eta*u
  assert tp==V0-G*eta*u and tp>tq
  assert tp+LP*ep+K*eq==root
 assert alpha0+eta==F(2586269934456514327,7450150876955541504)
 assert V0-G*eta==F(757686080746453135,58204303726215168)
 print("PASS: 680 states, 1240 action comparisons, all exact affine identities")
if __name__=="__main__":check()
