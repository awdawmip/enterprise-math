#!/usr/bin/env python3
"""53rd affine N14 auxiliary iid exact Fraction verification; author-side only."""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
import json
N=14
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
A=(10,8,2); B=(12,0,1)
SP={(6,6,0),(7,6,0),(7,7,0),(8,6,0),(8,7,0),(8,8,0),
(9,6,0),(9,7,0),(9,7,1),(9,8,0),(9,8,1),
(10,5,0),(10,6,0),(10,7,0),(10,7,1),(10,8,1),
(11,5,0),(11,7,1),(11,8,2),(11,6,1),(8,7,1),(11,4,0),(9,5,0)}
SQ={(4,0,3),(4,0,4),(5,0,3),(5,0,4),(5,0,5),(5,1,4),
(6,0,3),(6,0,4),(6,1,4),(6,1,5),(6,2,4),
(7,0,3),(7,1,4),(7,2,4),(7,2,5),
(8,0,3),(8,1,3),(8,2,4),(8,3,4),(8,3,5),
(9,1,3),(9,3,4),(9,4,5),(10,0,2),(10,5,5),(10,2,3),
(7,1,3),(10,4,4),(3,0,3)}
AL=F(1292956446600961517,3725075438477770752)
V=F(24752812520708302205,1862537719238885376)
S=F(264923490880289,417792000000000)
K=F(297764424,19019)
LP=F(72)+F(8,9)*K;LQ=K;G=LP+LQ
def child(st,i):
 n,a,b=st
 return (n+1,a+(i==0),b+(i==1))
def act(st):
 if st in SP:return 'P'
 if st in SQ:return 'Q'
 n,a,b=st;t=N-n
 if 8*3**a>=9*2**(a+b+t):return 'P'
 if 8*3**(a+t)<9*2**(a+b+t):return 'Q'
 assert n<N,st
 return 'C'
def firsthit(st):
 cur={(0,0):(F(1),F(1),1)}
 for n in range(st[0]):
  nxt=defaultdict(lambda:(F(),F(),0))
  for (a,b),(p,q,k) in cur.items():
   if act((n,a,b))!='C':continue
   for i in range(3):
    key=(a+(i==0),b+(i==1));x,y,l=nxt[key]
    nxt[key]=(x+p*P[i],y+q*Q[i],l+k)
  cur=dict(nxt)
 return cur.get(st[1:],(F(),F(),0))
@lru_cache(None)
def suffix(st):
 z=act(st)
 if z=='P':return F(),F(1),F(),F()
 if z=='Q':return F(1),F(),F(),F()
 kids=[suffix(child(st,i)) for i in range(3)]
 return (sum((P[i]*kids[i][0] for i in range(3)),F()),
         sum((Q[i]*kids[i][1] for i in range(3)),F()),
         F(1)+sum((P[i]*kids[i][2] for i in range(3)),F()),
         F(1)+sum((Q[i]*kids[i][3] for i in range(3)),F()))
def dual():
 D={};ties=[];positive=negative=checked=0
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    st=(n,a,b)
    opts={'P':LQ*F(2**(a+b),3**a),'Q':LP}
    if n<N:opts['C']=F(1)+sum((P[i]*D[child(st,i)] for i in range(3)),F())
    z=act(st);base=opts[z]
    for mode,value in opts.items():
     if mode==z:continue
     checked+=1
     if value<base:negative+=1
     elif value==base:ties.append((st,z,mode))
     else:positive+=1
    D[st]=base
 return D[(0,0,0)],ties,positive,negative,checked,len(D)
def forward(u,s):
 cur={(0,0):(F(1),F(1))};ep=eq=tp=tq=F()
 for n in range(N+1):
  nxt=defaultdict(lambda:(F(),F()))
  for (a,b),(p,q) in cur.items():
   st=(n,a,b)
   if st==A:
    eq+=q*u;p*=1-u;q*=1-u
   elif st==B:
    ep+=p*s;p*=1-s;q*=1-s
   else:
    z=act(st)
    if z=='P':eq+=q;continue
    if z=='Q':ep+=p;continue
   assert n<N,st
   tp+=p;tq+=q
   for i in range(3):
    key=(a+(i==0),b+(i==1));x,y=nxt[key]
    nxt[key]=(x+p*P[i],y+q*Q[i])
  cur=dict(nxt)
 assert not cur
 return ep,eq,tp,tq
def next_dual():
 vals={};points=[]
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    st=(n,a,b);z='P' if st==A else act(st)
    opts={'P':(F(),F(2**(a+b),3**a)),'Q':(F(72),F(8,9))}
    if n<N:opts['C']=(F(1)+sum((P[i]*vals[child(st,i)][0] for i in range(3)),F()),
                            sum((P[i]*vals[child(st,i)][1] for i in range(3)),F()))
    vals[st]=opts[z]
    for mode,v in opts.items():
     if mode==z or st in (A,B):continue
     c0=v[0]-opts[z][0];c1=v[1]-opts[z][1]
     assert c0+c1*K>0,(st,z,mode)
     if c1>0:
      nk=-c0/c1
      if nk<K:points.append((nk,st,z,mode))
 return max(points)
def check():
 pa,qa,live=firsthit(A);pb,qb,liveb=firsthit(B)
 ca=suffix(A);cb=suffix(B)
 X=pa*ca[0];Y=qa*(1-ca[1]);E=pb*(1-cb[0]);H=qb*cb[1]
 h=(X+Y)/(E+H);eta=E*h-X
 root,ties,positive,negative,checked,states=dual()
 assert (states,checked,positive,negative)==(680,1240,1238,0)
 assert set(ties)=={(A,'C','P'),(B,'C','Q')}
 assert root==V+G*AL
 assert (pa,qa,live)==(F(3,1073741824),F(1,2293235712),27)
 assert (pb,qb,liveb)==(F(48828125,725594112),F(48828125,362797056),12)
 assert ca==(F(61,331776),F(20705,20736),F(14945,13824),F(75,64))
 assert cb==(F(63,64),F(1,144),F(9,8),F(13,12))
 assert h==F(13077,22282240000000)
 assert eta==F(19019,183954342640877568)==Y-H*h
 assert 0<S<S+h<1
 assert forward(F(),S)[:3]==(AL,AL,V)
 for u in (F(),F(1,4),F(1,2),F(3,4),F(1)):
  ep,eq,tp,tq=forward(u,S+h*u)
  assert ep==eq==AL+eta*u
  assert tp==V-G*eta*u and tp>tq
  assert tp+LP*ep+LQ*eq==root
 end=forward(F(1),S+h)
 assert end[:3]==(AL+eta,AL+eta,V-G*eta)
 assert (AL+eta,V-G*eta)==(F(5171825786405386607,14900301753911083008),F(24752812514999692745,1862537719238885376))
 nxt=next_dual()
 assert nxt==(F(19909275768,1359829),(7,3,4),'C','Q')
 return {'A53_live':live,'pA53':str(pa),'qA53':str(qa),
         'K53':str(K),'Gamma53':str(G),'eta53':str(eta),
         'h53':str(h),'alpha53':str(AL+eta),'V53':str(V-G*eta),
         'bellman_states':states,'comparisons':checked,'strict':positive,
         'ties':str(ties),'next_dual':str(nxt)}
if __name__=='__main__':
 print(json.dumps(check(),indent=2))
