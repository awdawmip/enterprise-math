#!/usr/bin/env python3
"""Exact reproducible N14-49 author certificate; finite auxiliary iid model ONLY."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
N=14
P=tuple(map(lambda x:F(x,24),(3,1,20)))
Q=tuple(map(lambda x:F(x,24),(2,2,20)))
A=(7,1,3);B=(12,0,1)
SP={(6,6,0),(7,6,0),(7,7,0),(8,6,0),(8,7,0),(8,8,0),
(9,6,0),(9,7,0),(9,7,1),(9,8,0),(9,8,1),
(10,5,0),(10,6,0),(10,7,0),(10,7,1),(10,8,1),
(11,5,0),(11,7,1),(11,8,2),(11,6,1),(8,7,1),(11,4,0)}
SQ={(4,0,3),(4,0,4),(5,0,3),(5,0,4),(5,0,5),(5,1,4),
(6,0,3),(6,0,4),(6,1,4),(6,1,5),(6,2,4),
(7,0,3),(7,1,4),(7,2,4),(7,2,5),
(8,0,3),(8,1,3),(8,2,4),(8,3,4),(8,3,5),
(9,1,3),(9,3,4),(9,4,5),(10,0,2),(10,5,5),(10,2,3)}
K=F(56719116,2807);LP=F(72)+F(8,9)*K;LQ=K;G=LP+LQ
AL=F(5171824538157082397,14900301753911083008)
V=F(12379139146742512069,931268859619442688)
S=F(8824703195037923,13926400000000000)

def child(st,i):
 n,a,b=st;return n+1,a+(i==0),b+(i==1)
def act(st):
 if st in SP:return 'P'
 if st in SQ:return 'Q'
 n,a,b=st;t=N-n
 if 8*3**a>=9*2**(a+b+t):return 'P'
 if 8*3**(a+t)<9*2**(a+b+t):return 'Q'
 assert n<N,st
 return 'C'
def reached(target):
 cur={(0,0):(F(1),F(1),1)}
 for n in range(target[0]):
  nxt=defaultdict(lambda:(F(),F(),0))
  for (a,b),(p,q,v) in cur.items():
   if act((n,a,b))!='C':continue
   for i in range(3):
    k=(a+(i==0),b+(i==1));x,y,w=nxt[k]
    nxt[k]=(x+p*P[i],y+q*Q[i],w+v)
  cur=dict(nxt)
 return cur.get(target[1:],(F(),F(),0))
@lru_cache(None)
def suffix(st):
 z=act(st)
 if z=='P':return F(),F(1),F(),F()
 if z=='Q':return F(1),F(),F(),F()
 xs=[suffix(child(st,i)) for i in range(3)]
 return (sum((P[i]*xs[i][0] for i in range(3)),F()),
         sum((Q[i]*xs[i][1] for i in range(3)),F()),
         F(1)+sum((P[i]*xs[i][2] for i in range(3)),F()),
         F(1)+sum((Q[i]*xs[i][3] for i in range(3)),F()))
def dual():
 d={};ties=[];checked=0
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    st=(n,a,b)
    options={'P':LQ*F(2**(a+b),3**a),'Q':LP}
    if n<N:options['C']=F(1)+sum((P[i]*d[child(st,i)] for i in range(3)),F())
    z=act(st);chosen=options[z]
    for mode,value in options.items():
     if mode==z:continue
     checked+=1
     assert value>=chosen,(st,z,mode)
     if value==chosen:ties.append((st,z,mode))
    d[st]=chosen
 assert len(d)==680 and checked==1240
 assert set(ties)=={(A,'C','Q'),(B,'C','Q')}
 return d[(0,0,0)]
def forward(u,s):
 cur={(0,0):(F(1),F(1))};ep=eq=tp=tq=F()
 for n in range(N+1):
  nxt=defaultdict(lambda:(F(),F()))
  for (a,b),(p,q) in cur.items():
   st=(n,a,b)
   if st==A:ep+=p*u;p*=1-u;q*=1-u
   elif st==B:ep+=p*s;p*=1-s;q*=1-s
   elif act(st)=='P':eq+=q;continue
   elif act(st)=='Q':ep+=p;continue
   assert n<N
   tp+=p;tq+=q
   for i in range(3):
    k=(a+(i==0),b+(i==1));x,y=nxt[k]
    nxt[k]=(x+p*P[i],y+q*Q[i])
  cur=dict(nxt)
 assert not cur
 return ep,eq,tp,tq


def next_dual_candidate():
 # Fix A49 to immediate Q at endpoint. Other actions as in 49th policy.
 vals={}; points=[]
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    st=(n,a,b)
    z='Q' if st==A else act(st)
    opts={'P':(F(),F(2**(a+b),3**a)),'Q':(F(72),F(8,9))}
    if n<N:
     opts['C']=(F(1)+sum((P[i]*vals[child(st,i)][0] for i in range(3)),F()),
                sum((P[i]*vals[child(st,i)][1] for i in range(3)),F()))
    vals[st]=opts[z]
    for move,v in opts.items():
     if move==z or st in (A,B):continue
     c0=v[0]-opts[z][0];c1=v[1]-opts[z][1];slack=c0+c1*K
     assert slack>0,(st,z,move)
     if c1>0:
      k=-c0/c1
      if k<K:points.append((k,st,z,move))
 assert max(points)==(F(137448576,7601),(9,5,0),'C','P')
 return max(points)

def check():
 pa,qa,live=reached(A);pb,qb,liveb=reached(B)
 assert live==106 and liveb==12
 assert (pa,qa)==(F(6625,11943936),F(6625,2239488))
 ca=suffix(A);cb=suffix(B)
 assert ca==(F(18868399,18874368),F(487,11943936),F(1029359,786432),F(393323,331776))
 assert cb==(F(63,64),F(1,144),F(9,8),F(13,12))
 X=pa*(1-ca[0]);Y=qa*ca[1];E=pb*(1-cb[0]);H=qb*cb[1]
 h=(X+Y)/(E+H);eta=X-h*E
 assert h==F(129735679,870400000000)
 assert eta==-Y+h*H==F(241752875,12934289716936704)
 root=dual()
 assert next_dual_candidate()==(F(137448576,7601),(9,5,0),'C','P')
 assert root==V+G*AL
 for u in (F(),F(1,4),F(1,2),F(3,4),F(1)):
  s=S-h*u;ep,eq,tp,tq=forward(u,s)
  assert F()<s<F(1)
  assert ep==eq==AL+eta*u
  assert tp==V-G*eta*u and tp>=tq
  assert tp+LP*ep+LQ*eq==root
 assert AL+eta==F(5171824816656394397,14900301753911083008)
 assert V-G*eta==F(12378473542489900069,931268859619442688)
 print('AUTHOR exact N14 49th PASS (not Driver review/native transfer)')
 print('alpha49=',AL+eta,'V49=',V-G*eta,'eta=',eta,'h=',h)
if __name__=='__main__':check()
