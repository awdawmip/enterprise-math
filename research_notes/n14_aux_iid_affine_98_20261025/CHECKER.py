#!/usr/bin/env python3
"""Stage98 exact-rational portable author checker, Python stdlib only."""
from fractions import Fraction as F
from functools import cache
from collections import defaultdict
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6));N=14
A=(13,6,4);B=(12,0,1)
K=F(17496,13);LP=F(72)+F(8,9)*K;G=LP+K
ALPHA0=F(2586269934456514327,7450150876955541504)
V0=F(757686080746453135,58204303726215168)
S0=F(12365744850625211,20889600000000000)
def child(v,i):
 n,a,b=v
 return n+1,a+(i==0),b+(i==1)
@cache
def bell(v):
 n,a,b=v
 opts={'P':K*F(2**(a+b),3**a),'Q':LP}
 if n<N:opts['C']=1+sum((P[i]*bell(child(v,i))[0] for i in range(3)),F())
 val=min(opts.values())
 z=next(z for z in ('C','P','Q') if z in opts and opts[z]==val)
 return val,z,opts
def action(v):
 if v==A:return 'Q'
 if v==B:return 'C'
 return bell(v)[1]
def forward(u,s):
 state={(0,0):(F(1),F(1),1)}
 ep=eq=tp=tq=F()
 hit={A:(F(),F(),0),B:(F(),F(),0)}
 for n in range(N+1):
  nxt=defaultdict(lambda:(F(),F(),0))
  for (a,b),(p,q,c) in state.items():
   v=n,a,b
   if v==A:
    pp,qq,cc=hit[A];hit[A]=(pp+p,qq+q,cc+c)
    ep+=p*(1-u);p*=u;q*=u
   elif v==B:
    pp,qq,cc=hit[B];hit[B]=(pp+p,qq+q,cc+c)
    ep+=p*s;p*=1-s;q*=1-s
   else:
    z=action(v)
    if z=='P':eq+=q;continue
    if z=='Q':ep+=p;continue
   assert n<N
   tp+=p;tq+=q
   for i in range(3):
    aa,bb=a+(i==0),b+(i==1)
    x,y,k=nxt[(aa,bb)]
    nxt[(aa,bb)]=(x+p*P[i],y+q*Q[i],k+c)
  state=dict(nxt)
 assert not state
 return (ep,eq,tp,tq),hit
@cache
def suffix(v):
 z='C' if v==A else action(v)
 if z=='P':return F(),F(1),F(),F(),1
 if z=='Q':return F(1),F(),F(),F(),1
 k=[suffix(child(v,i)) for i in range(3)]
 return (sum((P[i]*k[i][0] for i in range(3)),F()),
         sum((Q[i]*k[i][1] for i in range(3)),F()),
         F(1)+sum((P[i]*k[i][2] for i in range(3)),F()),
         F(1)+sum((Q[i]*k[i][3] for i in range(3)),F()),
         sum(x[4] for x in k))
def next_dual():
 def add(x,y):return x[0]+y[0],x[1]+y[1]
 def scale(x,w):return w*x[0],w*x[1]
 @cache
 def fixed(v):
  n,a,b=v
  opts={'P':(F(),F(2**(a+b),3**a)),'Q':(F(72),F(8,9))}
  if n<N:
   v0=(F(1),F())
   for i in range(3):v0=add(v0,scale(fixed(child(v,i))[0],P[i]))
   opts['C']=v0
  z='C' if v in (A,B) else action(v)
  return opts[z],z,opts
 crossings=[]
 for n in range(N+1):
  for a in range(n+1):
   for b in range(n-a+1):
    v=(n,a,b);base,z,opts=fixed(v)
    for alt,y in opts.items():
     if alt==z:continue
     d0,d1=y[0]-base[0],y[1]-base[1]
     gap=d0+d1*K
     assert gap>=0
     if gap>0 and d1>0:
      t=-d0/d1
      if 0<t<K:crossings.append((t,v,z,alt))
 return max(crossings)
def check():
 gaps=[];ties=[]
 for n in range(N+1):
  for a in range(n+1):
   for b in range(n-a+1):
    v=(n,a,b);m,z,opts=bell(v)
    for alt,x in opts.items():
     if alt==z:continue
     g=x-m;gaps.append(g)
     if g==0:ties.append((v,z,alt))
 assert bell.cache_info().currsize==680
 assert len(gaps)==1240 and sum(x>0 for x in gaps)==1238 and all(x>=0 for x in gaps)
 assert set(ties)=={(A,'C','Q'),(B,'C','Q')}
 assert min(x for x in gaps if x>0)==F(1,156)
 assert bell((0,0,0))[0]==V0+G*ALPHA0
 (ep0,eq0,tp0,tq0),hits=forward(F(),S0)
 assert ep0==eq0==ALPHA0 and tp0==V0
 pA,qA,nA=hits[A];pB,qB,nB=hits[B]
 assert nA==18438 and nB==12
 assert (pA,qA)==(F(384125,3131031158784),F(384125,2229025112064))
 RA,RB=suffix(A),suffix(B)
 assert RA==(F(7,8),F(1,12),F(1),F(1),3)
 assert RB==(F(63,64),F(1,144),F(9,8),F(13,12),5)
 X=pA*(1-RA[0]);Y=qA*RA[1]
 E=pB*(1-RB[0]);H=qB*RB[1]
 h=(X+Y)/(E+H);eta=E*h-X
 assert h==F(2602831,174080000000)
 assert eta==F(4993625,12934289716936704)>0
 assert 0<S0<S0+h<1
 assert ALPHA0+eta==F(2586269937332842327,7450150876955541504)
 assert V0-G*eta==F(757686022002985135,58204303726215168)
 for u in (F(),F(1,7),F(1,2),F(1)):
  (ep,eq,tp,tq),_=forward(u,S0+h*u)
  assert ep==eq==ALPHA0+eta*u
  assert tp==V0-G*eta*u and tp>tq
  assert tp+LP*ep+K*eq==bell((0,0,0))[0]
 assert tp0-tq0==F(1207593511071079775,1862537719238885376)
 (_,_,tp1,tq1),_=forward(F(1),S0+h)
 assert tp1-tq1==F(1207595370727759775,1862537719238885376)
 assert next_dual()==(F(6696,5),(11,3,0),'C','P')
 print('PASS Stage98: 680 states, 1240 comparisons, 1238 strict gaps, 2 ties')
 print('A98 first hits=18438; B first hits=12; cones disjoint')
 print('K98',K,'Gamma98',G,'eta98',eta,'h98',h)
 print('alpha98',ALPHA0+eta,'V98',V0-G*eta,'s98',S0+h)
 print('Next *dual candidate* K99=6696/5 at (11,3,0), C/P tie')
if __name__=='__main__':check()
